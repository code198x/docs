"""Compare ROM BASIC arithmetic with actual Z80 fixed-width ADD results."""
import argparse
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--emulator", type=Path, required=True)
    parser.add_argument("--assembler", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    driver = args.samples / "sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py"
    spec = importlib.util.spec_from_file_location("completion", driver)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load maintained ROM keyboard driver")
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), args.output.resolve())
    checks = []
    source = Path(__file__).with_name("byte-sums.asm")
    tape = args.output.resolve() / "byte-sums.tap"
    binary = args.output.resolve() / "byte-sums.bin"
    try:
        for value in [255, 65535]:
            machine.statement("CLS")
            commands = [f"LET n={value}", "LET n=n+1", "PRINT n"]
            for command in commands:
                machine.statement(command)
            rows = machine.rows()
            if rows[0] != str(value + 1) or any(rows[1:22]) or not rows[-1].startswith("0 OK"):
                raise AssertionError((commands, rows))
            checks.append({"check": "BASIC numeric variable", "commands": commands, "rows": rows})
        rom = []
        for address in range(0, 16384, 256):
            chunk = machine.call("memory_read", addr=address, len=256)["bytes"]
            if len(chunk) != 256:
                raise AssertionError("Incomplete ROM read")
            rom.extend(chunk)
        for target, options in [(tape, ["--tapbas"]), (binary, [])]:
            subprocess.run([str(args.assembler), "--dialect", "pasmo", "--cpu", "z80", *options, str(source), "-o", str(target)], check=True)
        machine.call("load_media", slot="tape-1", kind="tape", path=str(tape))
        machine.statement('LOAD ""')
        machine.call("media_transport", slot="tape-1", transport="start")
        machine.frames(7000)
        code = binary.read_bytes()
        actual = machine.call("memory_read", addr=32768, len=len(code))["bytes"]
        if actual != list(code):
            raise AssertionError("Tape-loaded code differs from assembled fixture")
        values = machine.call("memory_read", addr=0x9000, len=6)["bytes"]
        if len(values) != 6:
            raise AssertionError("Incomplete result read")
        for i, (left, right) in enumerate([(255, 1), (127, 1), (5, 251)]):
            flags, result = values[2*i:2*i+2]
            signed = lambda n: n if n < 128 else n - 256
            full_signed = signed(left) + signed(right)
            expected = {"result": (left + right) % 256, "carry": left + right > 255, "signed_overflow": not -128 <= full_signed <= 127}
            observed = {"result": result, "carry": bool(flags & 1), "signed_overflow": bool(flags & 4)}
            if observed != expected:
                raise AssertionError((left, right, expected, observed))
            checks.append({"check": "Z80 ADD A,n", "operands": [left, right], "flags_byte": flags, "expected": expected, "observed": observed})
        report = {"status": "passed", "target": "configured Spectrum 48K, ROM keyboard entry and tape load", "emulator": machine.server["serverInfo"], "emulator_sha256": sha(args.emulator), "assembler_sha256": sha(args.assembler), "driver_sha256": sha(driver), "fixture_sha256": sha(source), "code_sha256": sha(binary), "tape_sha256": sha(tape), "rom_sha256": hashlib.sha256(bytes(rom)).hexdigest(), "checks": checks, "limits": "No original hardware, pseudocode execution, all-dialect or learner claim."}
        (args.output / "native-numbers.json").write_text(json.dumps(report, indent=2) + "\n")
        print("PASS: two BASIC results and three Z80 result/carry/overflow cases")
    finally:
        machine.close()


if __name__ == "__main__":
    main()
