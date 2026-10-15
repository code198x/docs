"""Check a strict positive condition and input-dependent output through the ROM."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", required=True, type=Path)
    parser.add_argument("--emulator", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    driver = args.samples / "sinclair-zx-spectrum/basic/meet-basic/lucky-number/verification/verify.py"
    spec = importlib.util.spec_from_file_location("lucky", driver)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load the maintained ROM keyboard driver")
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    args.output.mkdir(parents=True, exist_ok=True)
    machine = transport.Spectrum(str(args.emulator), args.output.resolve())
    source = '10 INPUT "Value ";g\n20 IF g>0 THEN PRINT "positive"\n30 PRINT g\n'

    def require_output(expected: list[str]) -> None:
        screen = [row.rstrip() for row in machine.screen()]
        if (
            screen[:len(expected)] != expected
            or any(screen[len(expected):22])
            or not screen[-1].startswith("0 OK")
        ):
            raise AssertionError((expected, screen))

    try:
        for line in source.splitlines():
            machine.statement(line)
        for value, expected in [(-1, ["-1"]), (0, ["0"]), (1, ["positive", "1"])]:
            machine.statement("RUN")
            machine.text(str(value))
            machine.enter()
            require_output(expected)
            machine.check(f"strict-positive-{value}", expected, capture=False)
        machine.statement('20 PRINT g+1')
        machine.text("30")
        machine.enter()
        for value, expected in [(0, "1"), (1, "2")]:
            machine.statement("RUN")
            machine.text(str(value))
            machine.enter()
            require_output([expected])
            machine.check(f"straight-line-{value}", [expected], capture=False)
        sample = args.samples / "sinclair-zx-spectrum/basic/meet-basic/lucky-number/unit-05/steps/step-03.bas"
        for line in sample.read_text().splitlines():
            machine.statement(line)
        for value, message in [(4, "Too low"), (7, "Correct!"), (9, "Too high")]:
            machine.statement("RUN")
            machine.text(str(value))
            machine.enter()
            require_output(["Guess a whole number 1 to 10", message])
            machine.check(f"published-comparisons-{value}", [message], capture=False)
        machine.statement('50 IF g>secret THEN PRINT "Too low"')
        machine.statement("RUN")
        machine.text("9")
        machine.enter()
        require_output(["Guess a whole number 1 to 10", "Too low", "Too high"])
        machine.check("deliberately-overlapping-tests", ["Too low", "Too high"], capture=False)
        rom = bytes(
            byte
            for address in range(0, 16384, 256)
            for byte in machine.call("memory_read", addr=address, len=256)["bytes"]
        )
        if len(rom) != 16384:
            raise AssertionError("Incomplete configured ROM fingerprint")
        report = {
            "status": "passed",
            "target": "48K Spectrum; ROM keyboard entry through MCP",
            "emulator": machine.server["serverInfo"],
            "binary_sha256": hashlib.sha256(args.emulator.read_bytes()).hexdigest(),
            "driver_sha256": hashlib.sha256(driver.read_bytes()).hexdigest(),
            "rom_sha256": hashlib.sha256(rom).hexdigest(),
            "conditional_source": source,
            "straight_line_source": '10 INPUT "Value ";g\n20 PRINT g+1\n',
            "published_sample_sha256": hashlib.sha256(sample.read_bytes()).hexdigest(),
            "checks": machine.evidence,
            "limits": "Emulated ROM observations, not original hardware or learner evidence.",
        }
        (args.output / "boundaries.json").write_text(json.dumps(report, indent=2) + "\n")
    finally:
        machine.close()


if __name__ == "__main__":
    main()
