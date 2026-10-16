"""Exact-rational condition models and actual ROM BASIC expression observations."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import Any

VALUES = [
    Fraction(s)
    for s in ["-1", "0", "1/2", "1", "3/2", "3", "4", "7", "10", "21/2", "11"]
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def numeric_row(value: Fraction) -> dict[str, Any]:
    # Membership in a closed interval is an independent reference for both guards.
    interval = min(Fraction(10), max(Fraction(1), value)) == value
    lower = value >= 1
    upper = value <= 10
    outside = value < 1 or value > 10
    inside = lower and upper
    require(
        inside == interval and outside != interval, "Complement/interval disagreement"
    )
    return {
        "input": str(value),
        "inside": int(inside),
        "outside": int(outside),
        "wrong_or": int(lower or upper),
        "wrong_outside_and": int(value < 1 and value > 10),
        "whole_and_inside": int(interval and value.denominator == 1),
        "positive": int(value > 0),
        "at_least_one": int(lower),
        "three_or_seven": int(value in {3, 7}),
    }


def model() -> dict[str, Any]:
    numeric = [numeric_row(v) for v in VALUES]
    guards = []
    for alive, ammo, grenades in itertools.product([0, 1], repeat=3):
        intended = bool(alive) and (ammo > 0 or grenades > 0)
        # Enumerate the allowed policy states independently of expression grouping.
        policy = (alive, ammo, grenades) in {(1, 0, 1), (1, 1, 0), (1, 1, 1)}
        ungrouped = (bool(alive) and ammo > 0) or grenades > 0
        require(intended == policy, "Shooting policy disagreement")
        guards.append(
            {
                "alive": alive,
                "ammo": ammo,
                "grenades": grenades,
                "grouped": int(intended),
                "ungrouped": int(ungrouped),
            }
        )
    require(len(numeric) == 11 and len(guards) == 8, "Missing cases")
    changed = [r for r in guards if r["grouped"] != r["ungrouped"]]
    require(
        len(changed) == 2
        and all(r["alive"] == 0 and r["grenades"] == 1 for r in changed),
        "Grouping counterexamples missing",
    )
    require(
        numeric[2]["positive"] == 1 and numeric[2]["at_least_one"] == 0,
        "Half-unit boundary not distinguished",
    )
    require(
        numeric[4]["inside"] == 1 and numeric[4]["whole_and_inside"] == 0,
        "Fractional input boundary not distinguished",
    )
    require(any(r["wrong_or"] != r["inside"] for r in numeric), "Wrong OR undetected")
    require(
        any(r["wrong_outside_and"] != r["outside"] for r in numeric),
        "Wrong AND undetected",
    )
    return {
        "status": "passed",
        "numeric": numeric,
        "shooting": guards,
        "grouping_counterexamples": changed,
        "limits": "Exact-rational host models and finite Boolean enumeration; "
        "not an implemented pseudocode runtime, parser, timing or learner evidence.",
    }


def native(args: argparse.Namespace, expected: dict[str, Any]) -> None:
    driver = (
        args.samples
        / "sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py"
    )
    opening = driver.parents[1] / "opening/verification/verify.py"
    spec = importlib.util.spec_from_file_location("completion", driver)
    require(
        spec is not None and spec.loader is not None, "Cannot load maintained transport"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    machine = module.Spectrum(str(args.emulator), args.output)
    report: dict[str, Any] = {
        "status": "running",
        "numeric": [],
        "shooting": [],
        "known_red": args.wrong_only,
    }
    commands: list[str] = []

    def expression(source: str) -> list[str]:
        machine.statement("CLS")
        machine.key("p")
        keys = {"AND": "y", "OR": "u", "NOT": "s", "<>": "w", ">=": "e", "<=": "q"}
        for part in re.split(r"(<>|>=|<=|AND|OR|NOT)", source):
            if part == "INT":
                raise AssertionError("INT must be tokenised separately")
            if part in keys:
                machine.key("symbol", keys[part])
            else:
                for segment in re.split(r"(INT)", part):
                    if segment == "INT":
                        machine.key("caps", "symbol")
                        machine.key("r")
                    else:
                        machine.text(segment)
        machine.enter()
        rows = machine.rows()
        require(
            len(rows) == 24 and rows[-1].startswith("0 OK"),
            "No normal ROM completion: " + repr(rows),
        )
        require(not any(rows[1:22]), "Unexpected additional output: " + repr(rows))
        commands.append("PRINT " + source)
        return rows

    def assign(name: str, value: str) -> None:
        source = f"LET {name}={value}"
        machine.statement(source)
        commands.append(source)

    try:
        for row in expected["numeric"][:1] if args.wrong_only else expected["numeric"]:
            assign("g", row["input"])
            source = '(g>=1 AND g<=10);",";(g<1 OR g>10);",";(g>=1 OR g<=10);",";(g<1 AND g>10)'
            rows = expression(source)
            numbers = [int(v) for v in rows[0].split(",")]
            wanted = [
                row[k] for k in ["inside", "outside", "wrong_or", "wrong_outside_and"]
            ]
            report["numeric"].append(
                {
                    "input": row["input"],
                    "expression": source,
                    "actual": numbers,
                    "expected": wanted,
                    "rows": rows,
                }
            )
            require(numbers == wanted, "Native numeric guards disagree")
            if args.wrong_only:
                require(
                    numbers[2] == wanted[0], "Known-red wrong OR accepts outside input"
                )
            source = '(g=INT g AND g>=1 AND g<=10);",";(g>0);",";(g>=1);",";(g=3 OR g=7);",";(g=3 OR 7)'
            rows = expression(source)
            wanted = [
                row[k]
                for k in [
                    "whole_and_inside",
                    "positive",
                    "at_least_one",
                    "three_or_seven",
                ]
            ] + [1]
            numbers = [int(v) for v in rows[0].split(",")]
            report["numeric"][-1]["validation_and_shorthand"] = {
                "expression": source,
                "actual": numbers,
                "expected": wanted,
                "rows": rows,
            }
            require(
                numbers == wanted,
                "Native numeric-domain or numeric-OR contrast differs",
            )
            if row["input"] == "3/2":
                machine.call(
                    "save_screenshot", path=str(args.output / "fraction-native.png")
                )
        for row in expected["shooting"]:
            for name, key in [("a", "alive"), ("m", "ammo"), ("n", "grenades")]:
                assign(name, str(row[key]))
            source = '(a AND (m>0 OR n>0));",";(a AND m>0 OR n>0)'
            rows = expression(source)
            numbers = [int(v) for v in rows[0].split(",")]
            wanted = [row["grouped"], row["ungrouped"]]
            report["shooting"].append(
                {
                    "inputs": {k: row[k] for k in ["alive", "ammo", "grenades"]},
                    "expression": source,
                    "actual": numbers,
                    "expected": wanted,
                    "rows": rows,
                }
            )
            require(numbers == wanted, "Native grouping differs")
            if row["alive"] == 0 and row["ammo"] == 0 and row["grenades"] == 1:
                machine.call(
                    "save_screenshot", path=str(args.output / "grouping-native.png")
                )
        rom = bytearray()
        for address in range(0, 16384, 256):
            chunk = bytes(machine.call("memory_read", addr=address, len=256)["bytes"])
            require(len(chunk) == 256, "Incomplete ROM identity read")
            rom.extend(chunk)
        report.update(
            status="passed",
            emulator=machine.server["serverInfo"],
            emulator_sha256=sha(args.emulator),
            driver_sha256=sha(driver),
            opening_driver_sha256=sha(opening),
            verifier_sha256=sha(Path(__file__)),
            rom_sha256=hashlib.sha256(rom).hexdigest(),
            output_numbers=sum(
                len(r["actual"]) + len(r["validation_and_shorthand"]["actual"])
                for r in report["numeric"]
            )
            + 2 * len(report["shooting"]),
            limits="ROM keyboard token entry and direct numeric expressions, not shared pseudocode execution. "
            "Exact halves expressed as division; no typed-text parsing, arbitrary numeric truth, "
            "short-circuit, performance, original-hardware or learner qualification.",
        )
        print("PASS actual ROM numeric outputs:", report["output_numbers"])
    except BaseException as error:
        report.update(status="failed", failure=repr(error))
        raise
    finally:
        (args.output / "native-conditions.json").write_text(
            json.dumps(report, indent=2) + "\n"
        )
        (args.output / "native-commands.txt").write_text("\n".join(commands) + "\n")
        machine.close()
        require(machine.process.poll() is not None, "Task emulator did not exit")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples", type=Path)
    parser.add_argument("--emulator", type=Path)
    parser.add_argument("--wrong-only", action="store_true")
    args = parser.parse_args()
    args.output = args.output.resolve()
    args.output.mkdir(parents=True, exist_ok=True)
    result = model()
    (args.output / "model-conditions.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    if args.samples or args.emulator:
        require(
            args.samples is not None and args.emulator is not None,
            "Supply both native paths",
        )
        native(args, result)
    else:
        print("PASS 11 exact-rational cases and all eight Boolean guard rows")


if __name__ == "__main__":
    main()
