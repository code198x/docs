"""Check BASIC conditions and Z80 masks/shifts through ROM entry and tape load."""
import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
from pathlib import Path

CASES = [
    ("and", 202, 15), ("and", 202, 0), ("and", 202, 255),
    ("or", 9, 2), ("or", 202, 0), ("or", 202, 255),
    ("xor", 255, 15), ("xor", 202, 15), ("xor_twice", 202, 15),
    ("cpl", 15, None),
    *[(op, value, None) for op in ["sla", "srl", "sra"] for value in [0, 1, 5, 128, 200, 255]],
    ("add", 5, None), ("add", 200, None),
]
BASIC = [("202 AND 15", "202"), ("202 AND 0", "0"), ("9 OR 2", "1"),
         ("9 OR 0", "9"), ("NOT 15", "0"), ("NOT 0", "1"),
         ("5*2", "10"), ("5/2", "2.5"), ("200*2", "400")]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected(op: str, value: int, mask: int | None) -> tuple[int, bool | None]:
    if op == "and" and mask is not None:
        return value & mask, None
    if op == "or" and mask is not None:
        return value | mask, None
    if op == "xor" and mask is not None:
        return value ^ mask, None
    if op == "xor_twice":
        return value, None
    if op == "cpl":
        return 255 - value, None
    if op in ["sla", "add"]:
        return value * 2 % 256, value * 2 > 255
    if op == "srl":
        return value // 2, value % 2 == 1
    if op == "sra":
        signed = value if value < 128 else value - 256
        return (signed // 2) % 256, value % 2 == 1
    raise ValueError((op, value, mask))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--emulator", type=Path, required=True)
    parser.add_argument("--assembler", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    driver = args.samples / "sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py"
    spec = importlib.util.spec_from_file_location("completion", driver)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load maintained keyboard driver")
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), out)
    checks = []

    def read(address: int, count: int) -> bytes:
        result = []
        for offset in range(0, count, 256):
            size = min(256, count-offset)
            chunk = machine.call("memory_read", addr=address+offset, len=size)["bytes"]
            if len(chunk) != size:
                raise AssertionError("Incomplete memory read")
            result.extend(chunk)
        return bytes(result)

    try:
        for expression, answer in BASIC:
            machine.statement("CLS")
            machine.key("p")  # PRINT in keyword mode.
            for part in re.split(r"(AND|OR|NOT)", expression):
                if part in ["AND", "OR", "NOT"]:
                    machine.key("symbol", {"AND": "y", "OR": "u", "NOT": "s"}[part])
                else:
                    machine.text(part)
            machine.enter()
            rows = machine.rows()
            if rows[0] != answer or any(rows[1:22]) or not rows[-1].startswith("0 OK"):
                raise AssertionError((expression, answer, rows))
            checks.append({"surface": "BASIC", "expression": expression, "rows": rows})
        rom = read(0, 16384)
        lines = ["; Audit fixture: actual CPU results; no result injection.", "org 32768", "start:", "    di"]
        for i, (op, value, mask) in enumerate(CASES):
            lines.append(f"    ld a,{value}")
            if op == "xor_twice":
                lines.extend([f"    xor {mask}", f"    xor {mask}"])
            elif mask is not None:
                lines.append(f"    {op} {mask}")
            else:
                lines.append("    cpl" if op == "cpl" else "    add a,a" if op == "add" else f"    {op} a")
            lines.extend(["    push af", "    pop hl", f"    ld (${0x9000+i*2:04X}),hl"])
        lines.extend(["hold:", "    jr hold", "end start", ""])
        source = out / "bits-shifts.asm"
        source.write_text("\n".join(lines))
        binary, tape = out / "bits-shifts.bin", out / "bits-shifts.tap"
        for target, options in [(binary, []), (tape, ["--tapbas"])]:
            subprocess.run([str(args.assembler), "--dialect", "pasmo", "--cpu", "z80", *options, str(source), "-o", str(target)], check=True)
        machine.call("load_media", slot="tape-1", kind="tape", path=str(tape))
        machine.statement('LOAD ""')
        machine.call("media_transport", slot="tape-1", transport="start")
        machine.frames(7000)
        code = binary.read_bytes()
        if not code or len(code) >= 4096 or read(32768, len(code)) != code:
            raise AssertionError("Loaded fixture differs or overlaps results")
        actual = read(0x9000, len(CASES)*2)
        for i, (op, value, mask) in enumerate(CASES):
            flags, result = actual[i*2:i*2+2]
            answer, carry = expected(op, value, mask)
            if result != answer or (carry is not None and bool(flags & 1) != carry):
                raise AssertionError((op, value, mask, result, flags, answer, carry))
            if mask is not None:
                # Bits outside the affected set must retain their earlier values.
                unaffected = mask if op == "and" else 255-mask
                if result & unaffected != value & unaffected:
                    raise AssertionError("Unrelated bits changed")
            checks.append({"surface": "Z80", "operation": op, "input": value, "mask": mask,
                           "result": result, "flags": flags, "expected_result": answer,
                           "carry": bool(flags & 1) if carry is not None else "not asserted"})
        report = {"status": "passed", "target": "configured Spectrum 48K; ROM entry and fresh tape load",
                  "emulator": machine.server["serverInfo"], "emulator_sha256": sha(args.emulator),
                  "assembler_sha256": sha(args.assembler), "driver_sha256": sha(driver),
                  "fixture_sha256": sha(source), "code_sha256": sha(binary), "tape_sha256": sha(tape),
                  "rom_sha256": hashlib.sha256(rom).hexdigest(), "checks": checks,
                  "limits": "No timing measurement, pseudocode interpreter, original hardware or learner validation."}
        (out / "native-bits.json").write_text(json.dumps(report, indent=2) + "\n")
        print(f"PASS: {len(BASIC)} BASIC cases; {len(CASES)} Z80 cases")
    finally:
        machine.close()


if __name__ == "__main__":
    main()
