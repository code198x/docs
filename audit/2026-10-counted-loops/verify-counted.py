"""Model ascending counted ranges and observe fresh ROM body-placement cases."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

RANGES = [(1, 0), (1, 1), (1, 3), (0, 3), (-2, 1)]


def need(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def model() -> dict[str, Any]:
    cases = []
    for start, end in RANGES:
        visits = []
        counter = start
        while counter <= end:
            visits.append(counter)
            counter += 1
        count = max(0, end - start + 1)
        need(len(visits) == count, "Visit/count disagreement")
        need(sum(visits) == count * (start + end) // 2, "Sum/count disagreement")
        need(
            not visits or visits[0] == start and visits[-1] == end,
            "Endpoint disagreement",
        )
        output = ["BEFORE", *map(str, visits), "TOTAL " + str(sum(visits)), "AFTER"]
        inside = ["BEFORE"]
        for value in visits:
            inside += [str(value), "AFTER"]
        inside += ["TOTAL " + str(sum(visits))]
        cases.append(
            {
                "start": start,
                "end": end,
                "visits": visits,
                "count": count,
                "total": sum(visits),
                "outside_after": output,
                "inside_after": inside,
            }
        )
    need(
        len(cases) == 5 and {c["count"] for c in cases} >= {0, 1, 3, 4},
        "Missing range cases",
    )
    need(
        cases[2]["outside_after"].count("AFTER") == 1
        and cases[2]["inside_after"].count("AFTER") == 3,
        "Placement difference missing",
    )
    need(
        cases[0]["outside_after"].count("AFTER") == 1
        and cases[0]["inside_after"].count("AFTER") == 0,
        "Zero-pass placement missing",
    )
    return {
        "status": "passed",
        "cases": cases,
        "limits": "Whole-number endpoints, ascending increment of one, fixed bounds and "
        "unmodified counter. Host model, not a shared pseudocode runtime.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples", type=Path)
    parser.add_argument("--emulator", type=Path)
    parser.add_argument("--wrong-only", action="store_true")
    args = parser.parse_args()
    args.output = args.output.resolve()
    args.output.mkdir(parents=True, exist_ok=True)
    expected = model()
    (args.output / "model-counted.json").write_text(
        json.dumps(expected, indent=2) + "\n"
    )
    if not args.samples and not args.emulator:
        print("PASS five range models, count/sum/endpoints and body placement")
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
    need(
        spec is not None and spec.loader is not None,
        "Cannot load maintained ROM transport",
    )
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), args.output)
    report: dict[str, Any] = {
        "status": "running",
        "checks": [],
        "control": args.wrong_only,
    }

    def run(label: str, source: list[str], wanted: list[str]) -> None:
        machine.key("a")
        machine.enter()
        for _ in range(10):
            if machine.rows()[-1].endswith("Sinclair Research Ltd"):
                break
            machine.frames(25)
        else:
            raise AssertionError("NEW did not return to positive ready state")
        fixture = args.output / (label + ".bas")
        fixture.write_text("\n".join(source) + "\n")
        for line in source:
            machine.statement(line)
        machine.statement("RUN")
        machine.frames(120)
        rows = machine.rows()
        report["checks"].append(
            {
                "label": label,
                "source": fixture.name,
                "source_sha256": sha(fixture),
                "expected_output": wanted,
                "rows": rows,
            }
        )
        need(
            len(rows) == 24 and rows[-1].startswith("0 OK"),
            "Missing normal ROM completion",
        )
        need(
            rows[: len(wanted)] == wanted and not any(rows[len(wanted) : 22]),
            "Complete ROM output differs: " + label,
        )
        if label in {"outside-1-0", "inside-1-3"}:
            machine.call("save_screenshot", path=str(args.output / (label + ".png")))

    try:
        for case in expected["cases"][2:3] if args.wrong_only else expected["cases"]:
            start, end = case["start"], case["end"]
            label = f"outside-{start}-{end}"
            source = [
                '10 PRINT "BEFORE"',
                "20 LET t=0",
                f"30 FOR i={start} TO {end - 1 if args.wrong_only else end}",
                "40 PRINT i",
                "50 LET t=t+i",
                "60 NEXT i",
                '70 PRINT "TOTAL ";t',
                '80 PRINT "AFTER"',
            ]
            run(label, source, case["outside_after"])
            source.remove('80 PRINT "AFTER"')
            source.insert(5, '55 PRINT "AFTER"')
            run(f"inside-{start}-{end}", source, case["inside_after"])
        reset = [
            '10 PRINT "BEFORE"',
            "20 LET t=0",
            "30 FOR i=1 TO 3",
            "35 LET t=0",
            "40 PRINT i",
            "50 LET t=t+i",
            "60 NEXT i",
            '70 PRINT "TOTAL ";t',
            '80 PRINT "AFTER"',
        ]
        run("reset-inside", reset, ["BEFORE", "1", "2", "3", "TOTAL 3", "AFTER"])
        rom = bytearray()
        for address in range(0, 16384, 256):
            chunk = bytes(machine.call("memory_read", addr=address, len=256)["bytes"])
            need(len(chunk) == 256, "Incomplete ROM identity read")
            rom.extend(chunk)
        need(len(report["checks"]) == 11, "Native case count mismatch")
        report.update(
            status="passed",
            emulator=machine.server["serverInfo"],
            emulator_sha256=sha(args.emulator),
            driver_sha256=sha(driver),
            opening_driver_sha256=sha(opening),
            verifier_sha256=sha(Path(__file__)),
            rom_sha256=hashlib.sha256(rom).hexdigest(),
            limits="Fresh 48K ROM keyboard-entered programs: five ranges with AFTER "
            "outside/inside plus misplaced accumulator reset. No shared pseudocode "
            "execution, other dialect, changed-loop-counter, STEP, timing, original "
            "hardware or learner qualification.",
        )
        print("PASS 11 fresh ROM runs, complete outputs and normal completion")
    except BaseException as error:
        report.update(status="failed", failure=repr(error))
        raise
    finally:
        (args.output / "native-counted.json").write_text(
            json.dumps(report, indent=2) + "\n"
        )
        machine.close()
        need(machine.process.poll() is not None, "Native emulator did not exit")


if __name__ == "__main__":
    main()
