"""Observe bounded character-code examples through ROM entry and Z80 execution."""
import argparse
import hashlib
import importlib.util
import json
import re
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
        raise RuntimeError('Cannot load ROM keyboard driver')
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), out)
    checks = []

    def read(address: int, size: int) -> bytes:
        data = bytes(machine.call('memory_read', addr=address, len=size)['bytes'])
        if len(data) != size:
            raise AssertionError('Incomplete memory read')
        return data

    try:
        keywords = {'CODE': 'i', 'CHR$': 'u', 'VAL': 'j', 'LEN': 'k'}
        cases = [('CODE "A"', '65'), ('CODE "a"', '97'), ('CODE "7"', '55'),
                 ('CHR$ 66', 'B'), ('CODE "7"-CODE "0"', '7'),
                 ('CODE "A"-CODE "0"', '17'), ('CODE "73"', '55'),
                 ('CODE ""', '0'), ('LEN "73"', '2'), ('VAL "73"', '73'),
                 ('VAL "2*3"', '6'), ('CHR$ (CODE "A"+32)', 'a')]
        for expression, expected in cases:
            machine.statement('CLS')
            machine.key('p')
            for part in re.split(r'("[^"]*"|CODE|CHR\$|VAL|LEN)', expression):
                if part in keywords:
                    machine.key('caps', 'symbol')
                    machine.key(keywords[part])
                else:
                    machine.text(part)
            machine.enter()
            rows = machine.rows()
            if rows[0] != expected or any(rows[1:22]) or not rows[-1].startswith('0 OK'):
                raise AssertionError((expression, expected, rows))
            checks.append({'expression': expression, 'expected': expected, 'rows': rows})
        inputs = [64, 65, 90, 91, 96, 97, 122, 123, 55, 48, 57, 47, 58]
        lines = ['; Audit-only ASCII boundary fixture. Not learner pseudocode.', 'org 32768', 'start:', 'di']
        for index, value in enumerate(inputs):
            address = 0xa000 + index * 5
            lines += [f'ld a,{value}', 'or 32', f'ld ({address}),a',
                      f'ld a,{value}', 'and 223', f'ld ({address+1}),a']
            for label, low, high, operation, offset in [('lower', 65, 91, 'or 32', 2), ('upper', 97, 123, 'and 223', 3)]:
                done = f'{label}_{index}'
                lines += [f'ld a,{value}', f'cp {low}', f'jr c,{done}', f'cp {high}',
                          f'jr nc,{done}', operation, done + ':', f'ld ({address+offset}),a']
            invalid, done = f'invalid_{index}', f'digit_{index}'
            lines += [f'ld a,{value}', 'cp 48', f'jr c,{invalid}', 'cp 58', f'jr nc,{invalid}',
                      'sub 48', f'jr {done}', invalid + ':', 'ld a,255', done + ':', f'ld ({address+4}),a']
        lines += ['ld a,165', 'ld ($a1ff),a', 'hold:', 'jr hold', 'end start']
        source = out / 'ascii-boundaries.asm'
        source.write_text('\n'.join(lines) + '\n')
        binary, tape = out / 'ascii-boundaries.bin', out / 'ascii-boundaries.tap'
        for target, options in [(binary, []), (tape, ['--tapbas'])]:
            subprocess.run([str(args.assembler), '--dialect', 'pasmo', '--cpu', 'z80', *options, str(source), '-o', str(target)], check=True)
        rom = b''.join(read(address, 256) for address in range(0, 16384, 256))
        machine.call('load_media', slot='tape-1', kind='tape', path=str(tape))
        machine.statement('LOAD ""')
        machine.call('media_transport', slot='tape-1', transport='start')
        machine.frames(7000)
        code = binary.read_bytes()
        if not 0 < len(code) < 8192:
            raise AssertionError('Fixture overlaps result memory or is empty')
        loaded = b''.join(read(32768 + i, min(256, len(code)-i)) for i in range(0, len(code), 256))
        if loaded != code or read(0xa1ff, 1) != b'\xa5':
            raise AssertionError('Loaded fixture differs or did not finish')
        observations = []
        for index, value in enumerate(inputs):
            actual = list(read(0xa000 + index * 5, 5))
            expected = [value | 32, value & 223, value + 32 if 65 <= value <= 90 else value,
                        value - 32 if 97 <= value <= 122 else value,
                        value - 48 if 48 <= value <= 57 else 255]
            if actual != expected or actual[0] & 223 != value & 223:
                raise AssertionError((value, actual, expected))
            observations.append({'input': value, 'raw_or32': actual[0], 'raw_and223': actual[1],
                                 'checked_lower': actual[2], 'checked_upper': actual[3], 'checked_digit_or_invalid255': actual[4]})
        report = {'status': 'passed', 'emulator': machine.server['serverInfo'],
                  'emulator_sha256': sha(args.emulator), 'assembler_sha256': sha(args.assembler),
                  'driver_sha256': sha(driver), 'rom_sha256': hashlib.sha256(rom).hexdigest(),
                  'fixture_sha256': sha(source), 'code_sha256': sha(binary), 'tape_sha256': sha(tape),
                  'basic_checks': checks, 'z80_observations': observations,
                  'limits': 'Configured Spectrum 48K only; representative ASCII boundaries, not all encodings. No learner, original hardware, C64 or performance claim.'}
        (out / 'native-characters.json').write_text(json.dumps(report, indent=2) + '\n')
        print('PASS: twelve ROM outputs and thirteen executed Z80 boundary cases')
    finally:
        machine.close()


if __name__ == '__main__':
    main()
