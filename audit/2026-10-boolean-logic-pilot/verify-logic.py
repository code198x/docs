"""Observe Boolean truth rows in Spectrum BASIC and an executed Z80 fixture."""
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
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    driver = args.samples/'sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py'
    spec = importlib.util.spec_from_file_location('completion', driver)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load ROM transport')
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), out)
    checks = []

    def read(address: int, size: int) -> bytes:
        result = bytes(machine.call('memory_read', addr=address, len=size)['bytes'])
        if len(result) != size:
            raise AssertionError('Incomplete read')
        return result

    def printed(expression: str, expected: int | None) -> None:
        machine.statement('CLS')
        machine.key('p')
        keys = {'AND': 'y', 'OR': 'u', 'NOT': 's', '<>': 'w'}
        for part in re.split(r'(<>|AND|OR|NOT)', expression):
            if part in keys:
                machine.key('symbol', keys[part])
            else:
                machine.text(part)
        machine.enter()
        rows = machine.rows()
        if expected is None:
            if not rows[-1].startswith('6 Number too big'):
                raise AssertionError((expression, rows))
        elif rows[0] != str(expected) or any(rows[1:22]) or not rows[-1].startswith('0 OK'):
            raise AssertionError((expression, expected, rows))
        checks.append({'expression': expression, 'expected_number': expected, 'rows': rows})

    try:
        for a in [0, 1]:
            for b in [0, 1]:
                values = [int(bool(a) and bool(b)), int(bool(a) or bool(b)), int(a != b),
                          int(not (bool(a) or bool(b))), int((not bool(a)) and (not bool(b))),
                          int(not (bool(a) and bool(b))), int((not bool(a)) or (not bool(b)))]
                expressions = [f'{a} AND {b}', f'{a} OR {b}', f'{a}<>{b}',
                               f'NOT ({a} OR {b})', f'(NOT {a}) AND (NOT {b})',
                               f'NOT ({a} AND {b})', f'(NOT {a}) OR (NOT {b})']
                for expression, expected in zip(expressions, values, strict=True):
                    printed(expression, expected)
        for expression, expected in [('10 AND 5', 10), ('10 OR 0', 10), ('10 OR 5', 1),
                                     ('NOT 10', 0), ('0 AND 1 OR 1', 1), ('0 AND (1 OR 1)', 0)]:
            printed(expression, expected)
        for expression in ['0 AND (1/0)', '1 OR (1/0)']:
            printed(expression, None)
        rom = b''.join(read(address, 256) for address in range(0, 16384, 256))
        lines = ['; Audit-only 0/1 inputs. XOR 1 complements these Boolean bits.', 'org 32768', 'start:', 'di']
        expected_bytes = []
        for a in [0, 1]:
            for b in [0, 1]:
                values = [int(bool(a) and bool(b)), int(bool(a) or bool(b)), int(a != b),
                          int(not (bool(a) or bool(b))), int((not bool(a)) and (not bool(b))),
                          int(not (bool(a) and bool(b))), int((not bool(a)) or (not bool(b)))]
                operations = [[f'ld a,{a}', f'and {b}'], [f'ld a,{a}', f'or {b}'],
                              [f'ld a,{a}', f'xor {b}'], [f'ld a,{a}', f'or {b}', 'xor 1'],
                              [f'ld a,{a}', 'xor 1', 'ld b,a', f'ld a,{b}', 'xor 1', 'and b'],
                              [f'ld a,{a}', f'and {b}', 'xor 1'],
                              [f'ld a,{a}', 'xor 1', 'ld b,a', f'ld a,{b}', 'xor 1', 'or b']]
                for operation, value in zip(operations, values, strict=True):
                    lines += operation+[f'ld ({0xa000+len(expected_bytes)}),a']
                    expected_bytes.append(value)
        guards = []
        for button in [0, 1]:
            for ground in [0, 1]:
                for stunned in [0, 1]:
                    value = int(bool(button) and bool(ground) and not bool(stunned))
                    lines += [f'ld a,{button}', f'and {ground}', 'ld b,a', f'ld a,{stunned}',
                              'xor 1', 'and b', f'ld ({0xa000+len(expected_bytes)}),a']
                    expected_bytes.append(value)
                    guards.append({'button': button, 'ground': ground, 'stunned': stunned, 'jump': value})
        lines += ['ld a,165', 'ld ($a100),a', 'hold:', 'jr hold', 'end start']
        source = out/'boolean-rows.asm'
        source.write_text('\n'.join(lines)+'\n')
        binary, tape = out/'boolean-rows.bin', out/'boolean-rows.tap'
        for target, options in [(binary, []), (tape, ['--tapbas'])]:
            subprocess.run([str(args.assembler), '--dialect', 'pasmo', '--cpu', 'z80', *options, str(source), '-o', str(target)], check=True)
        machine.call('load_media', slot='tape-1', kind='tape', path=str(tape))
        machine.statement('LOAD ""')
        machine.call('media_transport', slot='tape-1', transport='start')
        machine.frames(7000)
        code = binary.read_bytes()
        if not 0 < len(code) < 8192:
            raise AssertionError('Invalid fixture size')
        loaded = b''.join(read(32768+i, min(256, len(code)-i)) for i in range(0, len(code), 256))
        if loaded != code or read(0xa100, 1) != b'\xa5':
            raise AssertionError('Fixture differs or did not finish')
        actual = list(read(0xa000, len(expected_bytes)))
        if actual != expected_bytes or sum(actual[-8:]) != 1:
            raise AssertionError((actual, expected_bytes))
        report = {'status': 'passed', 'emulator': machine.server['serverInfo'],
                  'emulator_sha256': sha(args.emulator), 'assembler_sha256': sha(args.assembler),
                  'driver_sha256': sha(driver), 'fixture_sha256': sha(source),
                  'code_sha256': sha(binary), 'tape_sha256': sha(tape),
                  'rom_sha256': hashlib.sha256(rom).hexdigest(), 'basic_checks': checks,
                  'z80_bytes': actual, 'jump_guard_rows': guards,
                  'limits': 'Configured 48K ROM and actual Z80 fixture only. BASIC <> implements Boolean XOR on 0/1 values; it is not a BASIC XOR keyword. No learner, hardware, other language or performance claim.'}
        (out/'native-logic.json').write_text(json.dumps(report, indent=2)+'\n')
        print('PASS: 34 ROM numeric outputs, two ROM error observations, 28 Boolean result bytes and eight jump-guard rows')
    finally:
        machine.close()


if __name__ == '__main__':
    main()
