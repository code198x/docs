"""Compare stock-ROM conversion in independent engines; test a disposable correction."""
import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import tempfile
from fractions import Fraction
from pathlib import Path

DECIMALS = ['0.5', '.5', '0.1', '0.75', '0.25', '0.2', '0.125', '0.0625', '0.3', '0.9', '1.5', '5e-1']
CALCULATIONS = [('1/2', 1, 2, False), ('3/4', 3, 4, False), ('1/10', 1, 10, False),
                ('5/10', 5, 10, False), ('(1/10)*5', 1, 10, True)]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'Cannot import {name}')
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def fixture() -> str:
    lines = ['; Audit fixture. ASCII conversion and ROM calculator operations, not injected results.',
             'org 32768', 'start:', ' di']

    def copy_result(index: int) -> None:
        # STKEND is 23653. Remove/copy the last five-byte calculator result.
        lines.extend([' ld hl,(23653)', ' ld de,5', ' or a', ' sbc hl,de',
                      ' ld (23653),hl', f' ld de,${0x9000+5*index:04x}',
                      ' ld bc,5', ' ldir'])

    for index, _ in enumerate(DECIMALS):
        lines.extend([f' ld hl,text{index}', ' ld (23645),hl', ' ld a,(hl)', ' call $2c9b'])
        copy_result(index)
    for index, (_, numerator, denominator, multiply) in enumerate(CALCULATIONS, len(DECIMALS)):
        lines.extend([f' ld bc,{numerator}', ' call $2d2b', f' ld bc,{denominator}',
                      ' call $2d2b', ' rst $28', ' defb $05,$38'])
        if multiply:
            lines.extend([' ld bc,5', ' call $2d2b', ' rst $28', ' defb $04,$38'])
        copy_result(index)
    lines.extend([' ld a,$a5', ' ld ($91ff),a', 'hold:', ' jr hold'])
    for index, literal in enumerate(DECIMALS):
        lines.append(f'text{index}: defb "{literal}",13')
    return '\n'.join([*lines, 'end start', ''])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ['samples', 'rom', 'emulator', 'assembler', 'fuse', 'output']:
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    rom = args.rom.read_bytes()
    if len(rom) != 16384 or rom[0x31ff:0x3201] != bytes([0x28, 0xe1]):
        raise AssertionError('Expected stock 48K ROM with JR Z,$31E2 at $31FF')
    corrected = bytearray(rom)
    corrected[0x3200] = 0xda
    source = out / 'conversion.asm'
    source.write_text(fixture())
    binary, tape = out / 'conversion.bin', out / 'conversion.tap'
    for target, options in [(binary, []), (tape, ['--tapbas'])]:
        subprocess.run([str(args.assembler), '--dialect', 'pasmo', '--cpu', 'z80',
                        *options, str(source), '-o', str(target)], check=True, timeout=20)
    code = binary.read_bytes()
    if not code or len(code) >= 4096:
        raise AssertionError('Fixture empty or overlaps result area')
    holds = [i for i in range(len(code)-1) if code[i:i+2] == bytes([0x18, 0xfe])]
    if len(holds) != 1:
        raise AssertionError('Cannot identify unique completion loop')
    hold = 32768 + holds[0]
    names = [*DECIMALS, *[value[0] for value in CALCULATIONS]]
    count = len(names) * 5
    driver = args.samples / 'sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py'
    transport = module('keyboard', driver)
    prior = Path(__file__).parent.parent / '2026-10-fractions-pilot/verify-fractions.py'
    decode = module('prior_audit', prior).decode
    machine = transport.Spectrum(str(args.emulator), out)
    interactive = []

    def read(address: int, length: int) -> bytes:
        result = bytearray()
        for offset in range(0, length, 256):
            size = min(256, length-offset)
            chunk = machine.call('memory_read', addr=address+offset, len=size)['bytes']
            if len(chunk) != size:
                raise AssertionError('Incomplete native memory read')
            result.extend(chunk)
        return bytes(result)

    try:
        if read(0, 16384) != rom:
            raise AssertionError('Native mapped ROM differs from requested ROM')
        for expression in ['0.5', '1/2', '0.1', '1/10', '5e-1', '5/10']:
            machine.statement('LET x=' + expression)
            pointer = int.from_bytes(read(23627, 2), 'little')
            record = read(pointer, 6)
            if record[0] != 0x78:
                raise AssertionError('Unexpected first variable record')
            machine.statement('CLS')
            machine.statement('PRINT x')
            rows = machine.rows()
            answer = '0.1' if expression in ['0.1', '1/10'] else '0.5'
            if rows[0] != answer or any(rows[1:22]) or not rows[-1].startswith('0 OK'):
                raise AssertionError((expression, rows))
            interactive.append({'expression': expression, 'bytes': list(record[1:]),
                                'rational': str(decode(record[1:])), 'display': rows[0],
                                'completion': rows[-1]})
        machine.call('load_media', slot='tape-1', kind='tape', path=str(tape))
        machine.statement('LOAD ""')
        machine.call('media_transport', slot='tape-1', transport='start')
        machine.frames(7000)
        if read(32768, len(code)) != code or read(0x91ff, 1) != bytes([165]):
            raise AssertionError('Native fixture did not load and complete')
        native = read(0x9000, count)
        server = machine.server['serverInfo']
    finally:
        machine.close()

    def reference(label: str, firmware: bytes) -> bytes:
        # Current-directory default name avoids Fuse's custom-ROM autoload guard.
        # TemporaryDirectory owns the only files modified. No firmware is retained.
        with tempfile.TemporaryDirectory(prefix='fuse-' + label + '-', dir=out) as location:
            cwd = Path(location)
            (cwd / '48.rom').write_bytes(firmware)
            commands = '\n'.join([*[f'print [{i}]' for i in range(16384)],
                                   f'breakpoint {hold}', 'commands 1', 'print [0x91ff]',
                                   *[f'print [{0x9000+i}]' for i in range(count)], 'exit 0', 'end'])
            result = subprocess.run([str(args.fuse.resolve()), '--machine', '48', '--no-sound',
                                     '--no-autosave-settings', '--no-confirm-actions', '--speed', '1000',
                                     '--auto-load', '--tape', str(tape), '--debugger-command', commands],
                                    cwd=cwd, capture_output=True, text=True, check=False, timeout=20)
            if result.returncode != 0 or result.stderr:
                raise AssertionError((label, result.returncode, result.stderr))
            values = [int(value, 16) for value in re.findall(r'^0x([0-9a-f]+)$', result.stdout, re.MULTILINE)]
            if len(values) != 16384 + 1 + count or values[16384] != 165:
                raise AssertionError('Incomplete reference dump or missing completion marker')
            if bytes(values[:16384]) != firmware:
                raise AssertionError('Reference mapped ROM differs')
            return bytes(values[16385:])

    stock = reference('stock', rom)
    patched = reference('counterfactual', bytes(corrected))
    if native != stock:
        raise AssertionError('Independent engines disagree on the stock ROM')
    results = []
    for i, name in enumerate(names):
        original = stock[i*5:i*5+5]
        alternative = patched[i*5:i*5+5]
        results.append({'input': name, 'stock_bytes': list(original),
                        'stock_rational': str(decode(original)),
                        'corrected_bytes': list(alternative),
                        'corrected_rational': str(decode(alternative))})
    (out / 'observations.json').write_text(json.dumps({'interactive': interactive, 'results': results}, indent=2) + '\n')
    by_name = {item['input']: item for item in results}
    for name in ['0.5', '.5']:
        if Fraction(by_name[name]['stock_rational']) == Fraction(name):
            raise AssertionError('Expected stock decimal conversion discrepancy')
        if Fraction(by_name[name]['corrected_rational']) != Fraction(name):
            raise AssertionError('Documented correction did not restore exact binary fraction')
    if by_name['0.5']['stock_bytes'] != by_name['(1/10)*5']['stock_bytes']:
        raise AssertionError('Decimal conversion does not match division/multiply path')
    for name in ['1/2', '3/4', '5/10', '5e-1']:
        if by_name[name]['stock_bytes'] != by_name[name]['corrected_bytes']:
            raise AssertionError('Exact-division control changed')
    if by_name['1/10']['stock_bytes'][-1] != 204 or by_name['1/10']['corrected_bytes'][-1] != 205:
        raise AssertionError('Expected rounding-bit discriminator not observed')
    for observation in interactive:
        if observation['bytes'] != by_name[observation['expression']]['stock_bytes']:
            raise AssertionError('Interactive and direct-ROM paths differ')
    report = {'status': 'passed', 'native_engine': server,
              'native_binary_sha256': sha(args.emulator.read_bytes()),
              'reference_version': subprocess.run([str(args.fuse), '--version'], capture_output=True,
                                                  text=True, check=True, timeout=5).stdout.strip(),
              'reference_binary_sha256': sha(args.fuse.read_bytes()), 'driver_sha256': sha(driver.read_bytes()),
              'decoder_sha256': sha(prior.read_bytes()), 'fixture_sha256': sha(source.read_bytes()),
              'code_sha256': sha(code), 'tape_sha256': sha(tape.read_bytes()),
              'stock_rom_sha256': sha(rom), 'counterfactual_rom_sha256': sha(corrected),
              'both_mapped_roms_verified': True, 'native_loaded_code_verified': True,
              'completion_marker': 165, 'independent_stock_bytes_equal': True,
              'counterfactual_patch': {'address': 0x3200, 'before': 225, 'after': 218,
                                       'stock_target': 0x31e2, 'corrected_target': 0x31db},
              'interactive': interactive, 'results': results,
              'limits': 'Configured stock ROM and named engines only; correction is a disposable counterfactual, not shipped firmware. No original hardware, other ROM or learner qualification.'}
    (out / 'conversion-results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(f'PASS: {len(interactive)} interactive cases; {len(names)} independent ROM cases; mapped ROMs and counterfactual verified')


if __name__ == '__main__':
    main()
