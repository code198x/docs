"""Finite output models and actual ROM PRINT separator contrasts."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


def need(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cases() -> list[dict[str, Any]]:
    # Structured model inputs, not a parser for arbitrary pseudocode.
    records = [
        ("literal", ["2 + 2"], "2 + 2", 'PRINT "2 + 2"'),
        ("sum", [2 + 2], "4", "PRINT 2+2"),
        (
            "labelled",
            ["Two plus two is ", 2 + 2],
            "Two plus two is 4",
            'PRINT "Two plus two is ";2+2',
        ),
        ("missing-space", ["Score:", 2 + 3], "Score:5", 'PRINT "Score:";2+3'),
        ("repaired-space", ["Score: ", 2 + 3], "Score: 5", 'PRINT "Score: ";2+3'),
        ("visible-boundary", [" A ", "Z"], " A Z", 'PRINT " A ";"Z"'),
        (
            "multiple-items",
            ["You have ", 2 + 1, " lives left"],
            "You have 3 lives left",
            'PRINT "You have ";2+1;" lives left"',
        ),
        ("digit-text", ["2", "3"], "23", 'PRINT "2";"3"'),
        ("empty-text", ["", 2 + 3], "5", 'PRINT "";2+3'),
    ]
    records.extend(
        [
            ("question-literal", ["3 + 4"], "3 + 4", 'PRINT "3 + 4"'),
            ("question-sum", [3 + 4], "7", "PRINT 3+4"),
        ]
    )
    result = []
    for label, parts, expected, basic in records:
        output = "".join(str(part) for part in parts)
        need(output == expected, "Finite output model disagrees: " + label)
        result.append(
            {"label": label, "parts": parts, "output": output, "basic": basic}
        )
    need(len(result) == 11, "Missing model cases")
    need(result[3]["output"] != result[4]["output"], "Space repair not distinguished")
    need(
        " ".join(str(x) for x in result[4]["parts"]) != result[4]["output"],
        "Wrong automatic-space join undetected",
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples", type=Path)
    parser.add_argument("--emulator", type=Path)
    parser.add_argument("--wrong-only", action="store_true")
    args = parser.parse_args()
    args.output = args.output.resolve()
    args.output.mkdir(parents=True, exist_ok=True)
    models = cases()
    (args.output / "model-output.json").write_text(
        json.dumps(
            {
                "status": "passed",
                "cases": models,
                "limits": "Finite literal/integer output models, not a pseudocode parser or arbitrary number formatter.",
            },
            indent=2,
        )
        + "\n"
    )
    if not args.samples and not args.emulator:
        print("PASS 11 finite output models and wrong automatic-space contrast")
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
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    machine = module.Spectrum(str(args.emulator), args.output)
    report: dict[str, Any] = {
        "status": "running",
        "checks": [],
        "control": args.wrong_only,
    }

    def printed(label: str, source: str, expected: list[str]) -> None:
        machine.statement("CLS")
        machine.statement(source)
        rows = machine.rows()
        report["checks"].append(
            {
                "label": label,
                "source": source,
                "expected_output": expected,
                "rows": rows,
            }
        )
        need(
            len(rows) == 24 and rows[-1].startswith("0 OK"),
            "Missing normal ROM completion",
        )
        need(
            rows[: len(expected)] == expected and not any(rows[len(expected) : 23]),
            "Complete ROM output differs: " + label,
        )
        if label in {"comma-zone", "repaired-space"}:
            machine.call("save_screenshot", path=str(args.output / (label + ".png")))

    try:
        if args.wrong_only:
            printed("comma-is-not-immediate-join", 'PRINT "Score: ",2+3', ["Score: 5"])
        else:
            for case in models:
                printed(case["label"], case["basic"], [case["output"]])
            # Zone positions are independently checked as exact text offsets.
            printed("comma-zone", 'PRINT "Score: ",2+3', ["Score:" + " " * 10 + "5"])
            need(
                report["checks"][-1]["rows"][0].index("5") == 16,
                "Comma zone column differs",
            )
            printed("comma-letters", 'PRINT "A","B"', ["A" + " " * 15 + "B"])
            printed("continued-print", 'PRINT "A";: PRINT "B"', ["AB"])
            printed("new-print-line", 'PRINT "A": PRINT "B"', ["A", "B"])
        rom = bytearray()
        for address in range(0, 16384, 256):
            chunk = bytes(machine.call("memory_read", addr=address, len=256)["bytes"])
            need(len(chunk) == 256, "Incomplete ROM identity read")
            rom.extend(chunk)
        need(len(report["checks"]) == 15, "Missing native cases")
        report.update(
            status="passed",
            emulator=machine.server["serverInfo"],
            emulator_sha256=sha(args.emulator),
            driver_sha256=sha(driver),
            opening_driver_sha256=sha(opening),
            verifier_sha256=sha(Path(__file__)),
            rom_sha256=hashlib.sha256(rom).hexdigest(),
            limits="48K ROM keyboard-entered immediate PRINT commands. Significant final "
            "spaces followed by visible sentinel, not inferred from screen padding. "
            "Only short ASCII items, small integer sums and selected separator positions; "
            "no arbitrary formatter, parser, wrapping, other dialect, hardware or learner trial.",
        )
        print("PASS 15 native PRINT contrasts with complete output and completion")
    except BaseException as error:
        report.update(status="failed", failure=repr(error))
        raise
    finally:
        (args.output / "native-output.json").write_text(
            json.dumps(report, indent=2) + "\n"
        )
        machine.close()
        need(machine.process.poll() is not None, "Native emulator did not exit")


if __name__ == "__main__":
    main()
