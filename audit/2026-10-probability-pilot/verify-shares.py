"""ROM-enter the maintained shares sample and observe exact counts versus display."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load maintained driver: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_case(case: dict) -> None:
    counts = case["counts"]
    total = case["total"]
    require(len(counts) == 6 and total > 0, "Missing six-face positive sample")
    require(all(isinstance(n, int) and n >= 0 for n in counts), "Invalid tally")
    require(sum(counts) == total, "Tallies do not account for the sample")
    exact = [Fraction(100 * count, total) for count in counts]
    require(sum(exact) == 100, "Exact shares do not conserve the sample")
    # Exact rational rounding supplies an oracle independent of ROM arithmetic.
    rounded = [
        Fraction((value * 10 + Fraction(1, 2)).__floor__(), 10) for value in exact
    ]
    observed = [Fraction(text) for text in case["displayed_percentages"]]
    require(observed == rounded, "Displayed shares disagree with exact rounding")
    require(case["displayed_counts"] == counts, "Screen and memory counts differ")
    require(case["displayed_total"] == total, "Screen and memory totals differ")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("samples", "emulator", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    base = args.samples / "sinclair-zx-spectrum/basic"
    entry = base / "dice-roller/prototype/verification/entry.py"
    core = base / "meet-basic/opening/verification/verify.py"
    observer = base / "tail-chase/prototype/verification/verify.py"
    driver = load("entry", entry)
    state = load("probability_state", observer).state
    source = base / "dice-roller/teaching/shares/dice-roller.bas"
    machine = driver.Spectrum(str(args.emulator), out)
    report = {"status": "running", "cases": [], "diagnostic_commands": []}

    def wait_for(text: str) -> None:
        for _ in range(600):
            if any(text in row for row in machine.screen()):
                return
            machine.frames(10)
        raise AssertionError(("Timeout", text, machine.screen()))

    def observe(label: str, kind: str) -> dict:
        actual = state(machine)
        rows = machine.screen()
        require(len(rows) == 24, "Incomplete screen observation")
        case = {
            "label": label,
            "kind": kind,
            "counts": actual["t"],
            "total": int(actual["n"]),
            "displayed_total": int(rows[1].split()[1]),
            "displayed_counts": [int(rows[5 + 2 * j][7:14].strip()) for j in range(6)],
            "displayed_percentages": [rows[5 + 2 * j][15:23].strip() for j in range(6)],
            "screen_rows": rows,
        }
        check_case(case)
        report["cases"].append(case)
        print("PASS", label, case["counts"], case["displayed_percentages"], flush=True)
        return case

    try:
        machine.load_source(source)
        stored = machine.program_lines()
        expected_lines = {
            int(line.split()[0]) for line in source.read_text().splitlines()
        }
        require(
            set(stored) == expected_lines, "Stored lines differ from maintained source"
        )
        (out / "stored-lines.json").write_text(json.dumps(stored, indent=2) + "\n")
        for label in ("ordinary-first-run", "ordinary-fresh-run"):
            machine.statement("RUN")
            wait_for("9 STOP statement")
            case = observe(label, "ordinary maintained program")
            require(case["total"] == 12, "RUN did not start a fresh twelve-roll sample")
        for label, counts in [
            ("balanced-twelve", [2, 2, 2, 2, 2, 2]),
            ("unequal-twelve", [0, 1, 2, 3, 4, 2]),
            ("same-count-smaller-total", [0, 0, 2, 0, 2, 0]),
            ("single-face", [0, 0, 0, 0, 0, 1]),
        ]:
            commands = (
                ["LET n=" + str(sum(counts))]
                + [f"LET t({i})={count}" for i, count in enumerate(counts, 1)]
                + ["GO SUB 1000: GO SUB 1100"]
            )
            report["diagnostic_commands"].append({"label": label, "commands": commands})
            for command in commands:
                machine.statement(command)
            wait_for("0 OK")
            case = observe(
                label, "audit-only direct BASIC commands; not random sampling"
            )
            require(case["counts"] == counts, "Diagnostic commands were not accepted")
        balanced = report["cases"][2]
        require(
            sum(map(Fraction, balanced["displayed_percentages"])) == Fraction(501, 5),
            "Balanced rounded total should be 100.2",
        )
        # Known-red claim: forcing the displayed total to 100 must be rejected.
        try:
            require(
                sum(map(Fraction, balanced["displayed_percentages"])) == 100,
                "Rounded total is not exactly 100",
            )
        except AssertionError as error:
            report["negative_control"] = {
                "claim": "rounded shares must total 100",
                "rejected": True,
                "reason": str(error),
            }
        else:
            raise AssertionError("False conservation claim was accepted")
        damaged = json.loads(json.dumps(balanced))
        damaged["displayed_percentages"][0] = "16.5"
        try:
            check_case(damaged)
        except AssertionError:
            report["altered_display_rejected"] = True
        else:
            raise AssertionError("Altered display was accepted")
        machine.statement("RUN")
        wait_for("9 STOP statement")
        case = observe("ordinary-after-diagnostic-reset", "ordinary maintained program")
        require(case["total"] == 12, "Diagnostic state leaked into fresh RUN")
        require(machine.program_lines() == stored, "Diagnostics changed the program")
        require(len(report["cases"]) == 7, "Missing observed cases")
        rom = b"".join(
            bytes(machine.call("memory_read", addr=addr, len=256)["bytes"])
            for addr in range(0, 16384, 256)
        )
        require(len(rom) == 16384, "Incomplete ROM fingerprint")
        report.update(
            status="passed",
            emulator=machine.server["serverInfo"],
            emulator_sha256=sha(args.emulator),
            rom_sha256=hashlib.sha256(rom).hexdigest(),
            source_sha256=sha(source),
            verifier_sha256=sha(Path(__file__)),
            driver_hashes={
                str(p.relative_to(args.samples)): sha(p)
                for p in (entry, core, observer)
            },
            direct_memory_writes=False,
            configuration="Native Spectrum 48K PAL; configured ROM",
            limits="No browser, original hardware, fairness/independence test, timing or learner trial. Four fixtures set BASIC variables through ROM commands; not ordinary generated samples.",
        )
    except BaseException as error:
        report.update(status="failed", failure=repr(error))
        raise
    finally:
        (out / "native-shares.json").write_text(json.dumps(report, indent=2) + "\n")
        machine.close()


if __name__ == "__main__":
    main()
