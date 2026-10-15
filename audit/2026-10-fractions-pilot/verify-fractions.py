"""Observe Spectrum fractional storage and actual scaled-integer execution."""
import argparse
import hashlib
import importlib.util
import json
import subprocess
from fractions import Fraction
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode(data: bytes) -> Fraction:
    if len(data) != 5 or data[0] == 0:
        raise AssertionError("Expected five-byte non-integer floating representation")
    sign = -1 if data[1] & 128 else 1
    fraction = Fraction((int.from_bytes(data[1:], "big") & 0x7fffffff) + 0x80000000, 2**32)
    exponent = data[0] - 128
    power = Fraction(2**exponent) if exponent >= 0 else Fraction(1, 2**(-exponent))
    return sign * fraction * power


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
        raise RuntimeError("Cannot load ROM keyboard driver")
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), out)
    checks = []

    def read(address: int, size: int) -> bytes:
        data = bytes(machine.call("memory_read", addr=address, len=size)["bytes"])
        if len(data) != size:
            raise AssertionError("Incomplete memory read")
        return data

    def printed(expression: str, answer: str) -> None:
        machine.statement("CLS")
        machine.statement("PRINT " + expression)
        rows = machine.rows()
        if rows[0] != answer or any(rows[1:22]) or not rows[-1].startswith("0 OK"):
            raise AssertionError((expression, answer, rows))
        checks.append({"check": "ROM PRINT", "expression": expression, "rows": rows})

    try:
        for expression, answer in [("0.5+0.25", "0.75"), ("0.5+0.25=0.75", "1"),
                                   ("(10000000000+1)-10000000000", "0"),
                                   ("384/256", "1.5"), ("INT (384/256)", "1"),
                                   ("26/256", "0.1015625")]:
            printed(expression, answer)
        for literal, target, exact_required in [("1/2", Fraction(1, 2), True), ("3/4", Fraction(3, 4), True), ("1/10", Fraction(1, 10), False), ("0.5", Fraction(1, 2), None), ("0.75", Fraction(3, 4), None), ("0.1", Fraction(1, 10), None)]:
            machine.statement("LET x=" + literal)
            pointer = int.from_bytes(read(23627, 2), "little")
            record = read(pointer, 6)
            if record[0] != 0x78:
                raise AssertionError(("Unexpected single-letter numeric variable", list(record)))
            printed("x", {Fraction(1, 2): "0.5", Fraction(3, 4): "0.75", Fraction(1, 10): "0.1"}[target])
            actual = decode(record[1:])
            if exact_required is True and actual != target:
                raise AssertionError("Expected exactly representable binary fraction")
            if exact_required is False and actual == target:
                raise AssertionError("Finite binary representation cannot exactly equal 1/10")
            # Positive normalisation and finite denominator must hold independently.
            if actual <= 0 or actual.denominator & (actual.denominator-1):
                raise AssertionError("Invalid positive binary representation")
            checks.append({"check": "actual variable storage", "literal": literal,
                           "bytes": list(record[1:]), "stored_rational": str(actual),
                           "target_rational": str(target), "error": str(actual-target),
                           "exact": actual == target, "exact_required": exact_required})
        source = out / "scaled-add.asm"
        source.write_text("""; Audit-only unsigned 16-bit scaled addition and whole-part extraction.
org 32768
start:
    di
    ld hl,384
    ld de,128
    add hl,de
    ld ($9000),hl
    ld hl,384
    ld a,h
    ld ($9002),a
    ld hl,65535
    ld de,1
    add hl,de
    ld ($9003),hl
    push af
    pop hl
    ld ($9005),hl
hold:
    jr hold
end start
""")
        binary, tape = out / "scaled-add.bin", out / "scaled-add.tap"
        for target, options in [(binary, []), (tape, ["--tapbas"])]:
            subprocess.run([str(args.assembler), "--dialect", "pasmo", "--cpu", "z80", *options, str(source), "-o", str(target)], check=True)
        rom = b"".join(read(address, 256) for address in range(0, 16384, 256))
        machine.call("load_media", slot="tape-1", kind="tape", path=str(tape))
        machine.statement('LOAD ""')
        machine.call("media_transport", slot="tape-1", transport="start")
        machine.frames(7000)
        code = binary.read_bytes()
        if not code or read(32768, len(code)) != code:
            raise AssertionError("Loaded fixture differs")
        result = read(0x9000, 7)
        total = int.from_bytes(result[:2], "little")
        whole = result[2]
        wrapped = int.from_bytes(result[3:5], "little")
        carry = bool(result[5] & 1)
        if total != 384+128 or Fraction(total, 256) != Fraction(3, 2)+Fraction(1, 2):
            raise AssertionError("Matching-scale addition disagrees with rational addition")
        if whole != 384//256 or Fraction(whole) == Fraction(384, 256):
            raise AssertionError("Whole-part extraction must differ from full fraction here")
        if wrapped != 0 or not carry:
            raise AssertionError("16-bit unsigned boundary not observed")
        checks.append({"check": "executed scaled integer fixture", "bytes": list(result), "scaled_sum": total,
                       "decoded_sum": str(Fraction(total, 256)), "whole_part_of_384": whole,
                       "wrapped_sum": wrapped, "carry": carry})
        quantised = []
        for target in [Fraction(1, 10), Fraction(1, 3), Fraction(3, 2)]:
            scaled = target*256
            nearest = (scaled.numerator*2+scaled.denominator)//(scaled.denominator*2)
            quantised.append({"target": str(target), "scaled_integer": nearest,
                              "decoded": str(Fraction(nearest, 256)), "error": str(Fraction(nearest, 256)-target)})
        report = {"status": "passed", "target": "configured Spectrum 48K, ROM entry and fresh tape",
                  "emulator": machine.server["serverInfo"], "emulator_sha256": sha(args.emulator),
                  "assembler_sha256": sha(args.assembler), "driver_sha256": sha(driver),
                  "fixture_sha256": sha(source), "code_sha256": sha(binary), "tape_sha256": sha(tape),
                  "rom_sha256": hashlib.sha256(rom).hexdigest(), "checks": checks,
                  "host_rational_quantisation": quantised,
                  "limits": "Host rational calculations are not emulator observations; no timing, other float format, pseudocode or learner claim."}
        (out / "native-fractions.json").write_text(json.dumps(report, indent=2) + "\n")
        print("PASS: twelve ROM outputs, six storage observations and one executed integer fixture")
    finally:
        machine.close()


if __name__ == "__main__":
    main()
