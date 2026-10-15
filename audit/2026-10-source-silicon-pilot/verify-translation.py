"""Audit a finite toy model and observe BASIC data versus loaded Z80 code."""
import argparse
import hashlib
import importlib.util
import itertools
import json
import subprocess
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def translate(words: tuple[str, ...], old: bool) -> tuple[list[int], list[str]]:
    names, codes, pending, errors = ['INC', 'DOUBLE', 'SHOW'], [1, 2, 3], [], []
    valid = True
    for word in words:
        found = False
        for index, name in enumerate(names):
            if word == name:
                pending.append(codes[index])
                found = True
        if not found and not old:
            errors.append('Unknown instruction: ' + word)
            valid = False
    if not valid:
        errors.append('Translation failed; no code emitted')
    return pending if valid else [], errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ['samples', 'emulator', 'assembler', 'output']:
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--old', action='store_true', help='Known-red silent-omission control; no native run')
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    report = {'status': 'running', 'control': args.old, 'toy_cases': []}
    machine = None
    try:
        valid = [words for length in range(5) for words in itertools.product(['INC', 'DOUBLE', 'SHOW'], repeat=length)]
        invalid = sorted({words[:i] + ('MYSTERY',) + words[i:] for words in valid if len(words) < 4 for i in range(len(words) + 1)} | {('MYSTERY', 'MYSTERY'), ('INC', 'mystery', 'SHOW')})
        for words in [*valid, *invalid]:
            emitted, errors = translate(words, args.old)
            known = all(word in {'INC', 'DOUBLE', 'SHOW'} for word in words)
            expected = [{'INC': 1, 'DOUBLE': 2, 'SHOW': 3}[word] for word in words] if known else []
            row = {'source': words, 'emitted': emitted, 'diagnostics': errors, 'valid': known}
            report['toy_cases'].append(row)
            if emitted != expected or bool(errors) == known:
                raise AssertionError('Unknown name silently omitted or valid encoding differs: ' + repr(row))
            if known:
                direct, actual, shown_direct, shown_actual = 0, 0, [], []
                for word in words:
                    if word == 'INC':
                        direct += 1
                    elif word == 'DOUBLE':
                        direct *= 2
                    else:
                        shown_direct.append(direct)
                for code in emitted:
                    if code == 1:
                        actual += 1
                    elif code == 2:
                        actual *= 2
                    elif code == 3:
                        shown_actual.append(actual)
                    else:
                        raise AssertionError('Unsupported emitted code')
                if (actual, shown_actual) != (direct, shown_direct):
                    raise AssertionError('Direct names and encoded execution disagree')
                row.update(final=actual, shown=shown_actual)
        report.update(valid_cases=len(valid), invalid_cases=len(invalid))
        driver = args.samples / 'sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py'
        spec = importlib.util.spec_from_file_location('completion', driver)
        if spec is None or spec.loader is None:
            raise RuntimeError('Cannot load maintained ROM transport')
        transport = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(transport)
        machine = transport.Spectrum(str(args.emulator), out)

        def read(address: int, size: int) -> bytes:
            data = bytes(machine.call('memory_read', addr=address, len=size)['bytes'])
            if len(data) != size:
                raise AssertionError('Incomplete read')
            return data

        def program() -> dict:
            start = int.from_bytes(read(23635, 2), 'little')
            end = int.from_bytes(read(23627, 2), 'little')
            if not 23755 <= start < end < 32768:
                raise AssertionError('Unexpected BASIC bounds')
            data = read(start, end - start)
            lines, offset = [], 0
            while offset < len(data):
                number = int.from_bytes(data[offset:offset + 2], 'big')
                length = int.from_bytes(data[offset + 2:offset + 4], 'little')
                body = data[offset + 4:offset + 4 + length]
                if len(body) != length or not body or body[-1] != 13:
                    raise AssertionError('Invalid BASIC line record')
                lines.append({'number': number, 'body': list(body)})
                offset += length + 4
            report['last_parsed_lines'] = lines
            if offset != len(data) or [line['number'] for line in lines] != [10, 20, 30] or [bytes(line['body']).lstrip(b' ')[0] for line in lines] != [241, 241, 245]:
                raise AssertionError('Expected LET/LET/PRINT tokenised lines')
            return {'start': start, 'end': end, 'bytes': list(data), 'lines': lines}

        for line in ['10 LET s=0', '20 LET s=s+10', '30 PRINT s']:
            machine.statement(line)
        before = program()
        machine.statement('RUN')
        rows = machine.rows()
        if rows[0] != '10' or not rows[-1].startswith('0 OK') or program() != before:
            raise AssertionError(('RUN output or stored bytes differ', rows))
        machine.statement('20 LET s=s+20')
        edited = program()
        if edited['bytes'] == before['bytes']:
            raise AssertionError('Edit did not change stored source')
        machine.statement('RUN')
        edited_rows = machine.rows()
        if edited_rows[0] != '20' or not edited_rows[-1].startswith('0 OK') or program() != edited:
            raise AssertionError(('Edited RUN differs', edited_rows))
        report['basic'] = {'before': before, 'rows': rows, 'edited': edited, 'edited_rows': edited_rows, 'after_run_unchanged': True}
        source = out / 'source-byte-contrast.asm'
        source.write_text('''; Native arithmetic contrast; not the invented instruction codes.
org 32768
start:
 di
 xor a
 inc a
 inc a
 add a,a
 ld ($a000),a
 ld a,165
 ld ($b100),a
hold:
 jr hold
end start
''')
        binary, tape = out / 'source-byte-contrast.bin', out / 'source-byte-contrast.tap'
        for target, options in [(binary, []), (tape, ['--tapbas'])]:
            subprocess.run([str(args.assembler), '--dialect', 'pasmo', '--cpu', 'z80', *options, str(source), '-o', str(target)], check=True)
        expected = bytes.fromhex('f3 af 3c 3c 87 32 00 a0 3e a5 32 00 b1 18 fe')
        code = binary.read_bytes()
        if code != expected:
            raise AssertionError('Native encoding differs from independent Z80 bytes')
        machine.call('load_media', slot='tape-1', kind='tape', path=str(tape))
        machine.statement('LOAD ""')
        machine.call('media_transport', slot='tape-1', transport='start')
        machine.frames(7000)
        loaded = read(32768, len(code))
        if loaded != code or read(0xa000, 1) != b'\x04' or read(0xb100, 1) != b'\xa5':
            raise AssertionError('Load, execution result or completion differs')
        rom = b''.join(read(i, 256) for i in range(0, 16384, 256))
        report.update(status='passed', emulator=machine.server['serverInfo'], emulator_sha256=sha(args.emulator), assembler_sha256=sha(args.assembler), driver_sha256=sha(driver), verifier_sha256=sha(Path(__file__)), rom_sha256=hashlib.sha256(rom).hexdigest(), fixture_sha256=sha(source), code_sha256=sha(binary), tape_sha256=sha(tape), loaded_bytes=list(loaded), code_bytes=len(code), tape_bytes=tape.stat().st_size, actual_result=4, completion_marker=165, limits='Finite host model mirrors the pseudocode; it is not execution of that notation. ROM observations and separate Z80 fixture establish selected stored bytes/results, not all interpreter internals, compilation, performance, physical hardware or learner effectiveness.')
        print(f'PASS {len(valid)} valid and {len(invalid)} invalid toy cases; two ROM runs and native result 4')
    except BaseException as error:
        report.update(status='failed', failure=repr(error))
        raise
    finally:
        (out / 'translation.json').write_text(json.dumps(report, indent=2) + '\n')
        if machine is not None:
            machine.close()


if __name__ == '__main__':
    main()
