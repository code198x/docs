"""Check finite accumulator traces and observe selected ROM BASIC runs."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


def need(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def models() -> list[dict[str, Any]]:
    result = []
    for label, initial, visits, increment in [
        ("original", 0, 1000, 1),
        ("short", 0, 3, 1),
        ("question", 10, 3, 1),
        ("empty", 10, 0, 1),
        ("changed-increment", 10, 3, 2),
        ("one", 10, 1, 1),
    ]:
        total = initial
        trace = []
        for counter in range(1, visits + 1):
            before = total
            total += increment
            trace.append({"visit": counter, "before": before, "after": total})
        need(
            len(trace) == visits and total == initial + visits * increment,
            "Count/formula disagreement",
        )
        need(
            all(row["after"] == initial + row["visit"] * increment for row in trace),
            "Trace/formula disagreement",
        )
        result.append(
            {
                "label": label,
                "initial": initial,
                "visits": visits,
                "increment": increment,
                "trace": trace,
                "final": total,
            }
        )
    need(len(result) == 6, "Missing model coverage")
    need(
        [row["after"] for row in result[2]["trace"]] == [11, 12, 13],
        "Question trace differs",
    )
    wrong = 10
    for _ in range(3):
        wrong = 10
        wrong += 1
    need(wrong != result[2]["final"], "Wrong reset policy undetected")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--samples", type=Path)
    parser.add_argument("--emulator", type=Path)
    parser.add_argument("--wrong-only", action="store_true")
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    cases = models()
    (out / "model-trace.json").write_text(
        json.dumps(
            {
                "status": "passed",
                "cases": cases,
                "limits": "Finite whole-number paper traces, not a pseudocode interpreter, instruction count or timing measurement.",
            },
            indent=2,
        )
        + "\n"
    )
    if args.samples is None and args.emulator is None:
        print("PASS six finite traces and wrong-reset contrast")
        return
    need(
        args.samples is not None and args.emulator is not None,
        "Supply both native paths",
    )
    driver = (
        args.samples
        / "sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py"
    )
    opening = driver.parents[1] / "opening/verification/verify.py"
    spec = importlib.util.spec_from_file_location("completion", driver)
    need(spec is not None and spec.loader is not None, "Missing maintained transport")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    machine = module.Spectrum(str(args.emulator), out)
    report: dict[str, Any] = {
        "status": "running",
        "checks": [],
        "control": args.wrong_only,
    }

    def read(address: int, size: int) -> bytes:
        data = bytearray()
        for offset in range(0, size, 256):
            count = min(256, size - offset)
            chunk = bytes(
                machine.call("memory_read", addr=address + offset, len=count)["bytes"]
            )
            need(len(chunk) == count, "Incomplete memory read")
            data.extend(chunk)
        return bytes(data)

    def program() -> dict[str, Any]:
        start = int.from_bytes(read(23635, 2), "little")
        end = int.from_bytes(read(23627, 2), "little")
        need(23755 <= start < end < 32768, "Unexpected program bounds")
        raw = read(start, end - start)
        offset = 0
        lines = []
        while offset < len(raw):
            need(offset + 4 <= len(raw), "Truncated line header")
            number = int.from_bytes(raw[offset : offset + 2], "big")
            size = int.from_bytes(raw[offset + 2 : offset + 4], "little")
            body = raw[offset + 4 : offset + 4 + size]
            need(
                size > 0 and len(body) == size and body[-1] == 13, "Malformed line body"
            )
            lines.append({"number": number, "body": list(body)})
            offset += 4 + size
        need(offset == len(raw) and len(lines) >= 5, "Incomplete line records")
        tokens = [bytes(line["body"]).lstrip(b" ")[0] for line in lines]
        need(
            tokens[0:3] == [241, 235, 241] and tokens[-2:] == [243, 245],
            "LET/FOR/LET/NEXT/PRINT tokens differ",
        )
        return {
            "start": start,
            "end": end,
            "bytes": list(raw),
            "lines": lines,
            "leading_tokens": tokens,
        }

    def execute(
        label: str, source: list[str], wanted: list[str], install: bool = True
    ) -> None:
        if install:
            machine.key("a")
            machine.enter()
            for _ in range(10):
                if machine.rows()[-1].endswith("Sinclair Research Ltd"):
                    break
                machine.frames(25)
            else:
                raise ValueError("NEW did not return to positive ready state")
            for line in source:
                machine.statement(line)
        fixture = out / (label + ".bas")
        fixture.write_text("\n".join(source) + "\n")
        before = program()
        machine.statement("CLS")
        machine.statement("RUN")
        for _ in range(80):
            rows = machine.rows()
            if rows[-1].startswith("0 OK"):
                break
            machine.frames(25)
        else:
            raise ValueError("RUN did not reach normal completion within frame bound")
        after = program()
        report["checks"].append(
            {
                "label": label,
                "source": fixture.name,
                "source_sha256": sha(fixture),
                "expected_output": wanted,
                "rows": rows,
                "before": before,
                "after": after,
                "installed": install,
            }
        )
        need(
            len(rows) == 24 and rows[-1].startswith("0 OK"), "Normal completion missing"
        )
        need(
            rows[: len(wanted)] == wanted and not any(rows[len(wanted) : 23]),
            "Complete ROM output differs: " + label,
        )
        need(before == after, "RUN changed stored program records")
        if label in {"question", "instrumented"}:
            machine.call("save_screenshot", path=str(out / (label + ".png")))

    try:
        for case in [cases[2]] if args.wrong_only else cases:
            source = [
                f"10 LET s={case['initial']}",
                f"20 FOR i=1 TO {case['visits']}",
                f"30 LET s=s+{case['increment']}",
                "40 NEXT i",
                "50 PRINT s",
            ]
            label = case["label"]
            if args.wrong_only:
                source.insert(2, "25 LET s=10")
                label = "wrong-reset"
            execute(label, source, [str(case["final"])])
            if label == "question":
                execute("question-repeat", source, ["13"], install=False)
        instrumented = [
            "10 LET s=10",
            "20 FOR i=1 TO 3",
            "30 LET s=s+1",
            "35 PRINT s",
            "40 NEXT i",
            '50 PRINT "FINAL ";s',
        ]
        execute("instrumented", instrumented, ["11", "12", "13", "FINAL 13"])
        need(len(report["checks"]) == 8, "Missing native cases")
        rom = read(0, 16384)
        report.update(
            status="passed",
            emulator=machine.server["serverInfo"],
            emulator_sha256=sha(args.emulator),
            driver_sha256=sha(driver),
            opening_driver_sha256=sha(opening),
            verifier_sha256=sha(Path(__file__)),
            rom_sha256=hashlib.sha256(rom).hexdigest(),
            limits="Keyboard-entered ROM BASIC; stored records and selected outputs, not a CPU execution trace, instruction count, performance comparison, hardware or learner trial. Instrumented output changes the program and is not timing evidence.",
        )
        print("PASS eight ROM runs, complete output and unchanged stored records")
    except BaseException as error:
        report.update(status="failed", failure=repr(error))
        raise
    finally:
        (out / "native-trace.json").write_text(json.dumps(report, indent=2) + "\n")
        machine.close()
        need(machine.process.poll() is not None, "Emulator process did not exit")


if __name__ == "__main__":
    main()
