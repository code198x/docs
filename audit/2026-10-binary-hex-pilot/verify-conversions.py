"""Observe ROM BIN literals and all 256 executed Z80 byte decompositions."""
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
    for name in ['samples', 'emulator', 'assembler', 'output']:
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    driver = args.samples / 'sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py'
    spec = importlib.util.spec_from_file_location('completion', driver)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load maintained transport')
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), out)
    report = {'status': 'running', 'rom_checks': [], 'byte_rows': []}

    def read(address: int, size: int) -> bytes:
        result = bytes(machine.call('memory_read', addr=address, len=size)['bytes'])
        if len(result) != size:
            raise AssertionError('Incomplete memory read')
        return result

    try:
        for bits in ['0', '1', '101', '00000101', '1101', '1111', '10000', '10000000', '11110000', '11111111', '100000000']:
            machine.statement('CLS')
            machine.key('p')
            machine.key('caps', 'symbol')
            machine.key('b')
            machine.text(bits)
            machine.enter()
            rows = machine.rows()
            expected = int(bits, 2)
            if rows[0] != str(expected) or any(rows[1:22]) or not rows[-1].startswith('0 OK'):
                raise AssertionError((bits, expected, rows))
            report['rom_checks'].append({'bits': bits, 'expected': expected, 'rows': rows})
        source = out / 'byte-conversions.asm'
        source.write_text('''; Audit-only fixture. Emit eight binary digits and two nibble values per byte.
org 32768
start:
 di
 ld hl,$a000
 ld c,0
value:
 ld e,c
 ld b,8
bit:
 sla e
 ld a,0
 adc a,0
 ld (hl),a
 inc hl
 djnz bit
 ld a,c
 srl a
 srl a
 srl a
 srl a
 ld (hl),a
 inc hl
 ld a,c
 and 15
 ld (hl),a
 inc hl
 inc c
 jr nz,value
 ld a,165
 ld ($b100),a
hold:
 jr hold
end start
''')
        binary, tape = out / 'byte-conversions.bin', out / 'byte-conversions.tap'
        for target, options in [(binary, []), (tape, ['--tapbas'])]:
            subprocess.run([str(args.assembler), '--dialect', 'pasmo', '--cpu', 'z80', *options, str(source), '-o', str(target)], check=True)
        machine.call('load_media', slot='tape-1', kind='tape', path=str(tape))
        machine.statement('LOAD ""')
        machine.call('media_transport', slot='tape-1', transport='start')
        machine.frames(7000)
        code = binary.read_bytes()
        if not 0 < len(code) < 8192:
            raise AssertionError('Unexpected fixture size')
        loaded = b''.join(read(32768 + i, min(256, len(code) - i)) for i in range(0, len(code), 256))
        if loaded != code or read(0xb100, 1) != b'\xa5':
            raise AssertionError('Fixture differs or did not finish')
        data = b''.join(read(0xa000 + i, 256) for i in range(0, 2560, 256))
        if len(data) != 2560:
            raise AssertionError('Incomplete byte table')
        for value in range(256):
            actual = list(data[value * 10:(value + 1) * 10])
            bits, nibbles = actual[:8], actual[8:]
            if any(b not in [0, 1] for b in bits) or any(n not in range(16) for n in nibbles):
                raise AssertionError('Invalid output digit')
            binary_text = ''.join(str(b) for b in bits)
            hex_text = ''.join(format(n, 'X') for n in nibbles)
            weighted = sum(bit * (2 ** (7 - i)) for i, bit in enumerate(bits))
            if binary_text != format(value, '08b') or hex_text != format(value, '02X'):
                raise AssertionError((value, binary_text, hex_text))
            if weighted != value or nibbles[0] * 16 + nibbles[1] != value or int(binary_text, 2) != int(hex_text, 16):
                raise AssertionError('Independent representations disagree')
            report['byte_rows'].append({'value': value, 'bits': binary_text, 'nibbles': nibbles, 'hex': hex_text})
        rom = b''.join(read(address, 256) for address in range(0, 16384, 256))
        report.update(status='passed', emulator=machine.server['serverInfo'], emulator_sha256=sha(args.emulator), assembler_sha256=sha(args.assembler), driver_sha256=sha(driver), verifier_sha256=sha(Path(__file__)), rom_sha256=hashlib.sha256(rom).hexdigest(), fixture_sha256=sha(source), code_sha256=sha(binary), tape_sha256=sha(tape), code_bytes=len(code), tape_bytes=tape.stat().st_size, observed_bytes=len(data), completion_marker=165, limits='One configured Spectrum ROM and executed Z80 fixture. Hex text is host formatting of actual nibble output values, not a claimed BASIC HEX keyword or machine-rendered ASCII. All 256 unsigned byte values, not signed/floating representations, electrical behaviour, speed or learner evidence.')
        print('PASS: 11 ROM BIN literals and 256 actual Z80 byte rows (2560 bytes)')
    except BaseException as error:
        report.update(status='failed', failure=repr(error))
        raise
    finally:
        (out / 'native-conversions.json').write_text(json.dumps(report, indent=2) + '\n')
        machine.close()


if __name__ == '__main__':
    main()
