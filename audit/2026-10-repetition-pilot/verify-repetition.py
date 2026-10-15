"""Observe counted loops, pre/post tests and repeatable draws through the ROM."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--emulator", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    driver = args.samples / "sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py"
    spec = importlib.util.spec_from_file_location("completion", driver)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load the maintained ROM keyboard driver")
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    args.output.mkdir(parents=True, exist_ok=True)
    machine = transport.Spectrum(str(args.emulator), args.output.resolve())
    sources: dict[str, str] = {}

    def load(source: str) -> None:
        machine.key("a")  # NEW in keyword mode, clearing the earlier program.
        machine.enter()
        for _ in range(10):
            if machine.rows()[-1].endswith("Sinclair Research Ltd"):
                break
            machine.frames(25)
        else:
            raise AssertionError("NEW did not return to the ready copyright screen")
        for line in source.splitlines():
            machine.statement(line)

    def check(name: str, expected: list[str]) -> None:
        rows = machine.rows()
        if rows[:len(expected)] != expected or any(rows[len(expected):22]):
            raise AssertionError((name, expected, rows))
        if not rows[-1].startswith("0 OK"):
            raise AssertionError((name, rows[-1]))
        machine.check(name, expected, capture=False)

    def draws() -> list[int]:
        machine.statement("RANDOMIZE 1")
        values: list[int] = []
        for _ in range(32):
            machine.statement("CLS")
            machine.statement("PRINT INT (RND*10)+1")
            value = int(machine.rows()[0])
            if not 1 <= value <= 10:
                raise AssertionError(("range", value))
            values.append(value)
        return values

    try:
        for count in [0, 1, 3]:
            source = f'10 FOR i=1 TO {count}\n20 PRINT i\n30 NEXT i\n40 PRINT "DONE"\n'
            sources[f"for-{count}"] = source
            load(source)
            machine.statement("RUN")
            check(f"for-{count}", [str(i) for i in range(1, count + 1)] + ["DONE"])
        for lives in [0, 1, 3]:
            source = f'10 LET lives={lives}\n20 IF lives=0 THEN GO TO 60\n30 PRINT lives\n40 LET lives=lives-1\n50 GO TO 20\n60 PRINT "DONE"\n'
            sources[f"pretest-{lives}"] = source
            load(source)
            machine.statement("RUN")
            check(f"pretest-{lives}", [str(i) for i in range(lives, 0, -1)] + ["DONE"])
        source = '10 LET lives=0\n20 PRINT lives\n30 LET lives=lives-1\n40 IF lives>0 THEN GO TO 20\n50 PRINT "DONE"\n'
        sources["posttest-zero"] = source
        load(source)
        machine.statement("RUN")
        check("posttest-zero", ["0", "DONE"])
        first, second = draws(), draws()
        if first != second:
            raise AssertionError("Same explicit seed did not reproduce the sequence")
        if len(set(first)) == len(first):
            raise AssertionError("More draws than possible values cannot all be distinct")
        adjacent = [i for i in range(1, len(first)) if first[i] == first[i - 1]]
        machine.check("fixed-seed-sequence-reproduced", [], capture=False)
        machine.evidence[-1].update({"values": first, "repeated_values": sorted({x for x in first if first.count(x) > 1}), "adjacent_repeat_indexes": adjacent})
        rom = bytes(byte for address in range(0, 16384, 256) for byte in machine.call("memory_read", addr=address, len=256)["bytes"])
        if len(rom) != 16384:
            raise AssertionError("Incomplete ROM fingerprint")
        result = {
            "status": "passed",
            "target": "configured Spectrum 48K; ROM keyboard entry through MCP",
            "emulator": machine.server["serverInfo"],
            "binary_sha256": hashlib.sha256(args.emulator.read_bytes()).hexdigest(),
            "driver_sha256": hashlib.sha256(driver.read_bytes()).hexdigest(),
            "rom_sha256": hashlib.sha256(rom).hexdigest(),
            "sources": sources,
            "random_expression": "INT (RND*10)+1; RANDOMIZE 1 before each 32-draw series",
            "checks": machine.evidence,
            "limits": "No pseudocode interpreter, statistical fairness, original hardware or learner validation.",
        }
        (args.output / "native-repetition.json").write_text(json.dumps(result, indent=2) + "\n")
    finally:
        machine.close()


if __name__ == "__main__":
    main()
