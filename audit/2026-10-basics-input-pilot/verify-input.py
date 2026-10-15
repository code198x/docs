"""Observe ordered PRINT and submitted string INPUT through the Spectrum ROM."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ['samples', 'emulator', 'output']:
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    driver = args.samples / 'sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py'
    spec = importlib.util.spec_from_file_location('completion', driver)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load maintained ROM key transport')
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), out)
    report = {'status': 'running', 'sequence': [], 'input': []}

    def read(address: int, size: int) -> bytes:
        if size == 0:
            return b''
        data = bytes(machine.call('memory_read', addr=address, len=size)['bytes'])
        if len(data) != size:
            raise AssertionError('Incomplete read')
        return data

    def vars_address() -> int:
        value = int.from_bytes(read(23627, 2), 'little')
        if not 23755 <= value < 32768:
            raise AssertionError('Unexpected variables address')
        return value

    try:
        sequence = ['10 PRINT "First"', '20 PRINT "Second"', '30 PRINT "Last"']
        # Deliberately enter line 20 first: BASIC line numbers choose execution order.
        for line in [sequence[1], sequence[0], sequence[2]]:
            machine.statement(line)
        for label, expected in [('original', ['First', 'Second', 'Last']), ('swapped', ['Second', 'First', 'Last'])]:
            if label == 'swapped':
                machine.statement('10 PRINT "Second"')
                machine.statement('20 PRINT "First"')
            machine.statement('RUN')
            rows = machine.rows()
            if rows[:3] != expected or any(rows[3:22]) or not rows[-1].startswith('0 OK'):
                raise AssertionError((label, rows))
            report['sequence'].append({'label': label, 'rows': rows})
        # Reuse the three line numbers; no separate NEW keyboard path is needed.
        source = ['10 LET n$="Ada"', '20 PRINT "n$"', '30 PRINT n$']
        for line in source:
            machine.statement(line)
        machine.statement('RUN')
        rows = machine.rows()
        if rows[:2] != ['n$', 'Ada'] or not rows[-1].startswith('0 OK'):
            raise AssertionError(('Quoted name versus value', rows))
        report['quoted_value'] = {'source': source, 'rows': rows}
        source = ['10 INPUT "Name? ";n$', '20 PRINT "Hello, ";n$', '30 PRINT "Done"']
        (out / 'greeting.bas').write_text('\n'.join(source) + '\n')
        for line in source:
            machine.statement(line)
        for answer in ['Ada', 'Ada', 'Sam', '', '   ', ' Ada ', '42']:
            machine.statement('RUN')
            machine.frames(150)
            before = machine.screen()
            header_before = read(vars_address(), 1)[0]
            if header_before != 128 or any('Hello,' in row or 'Done' in row for row in before[:22]):
                raise AssertionError('INPUT did not wait before submission')
            machine.text(answer)
            machine.frames(100)
            typed = machine.screen()
            if read(vars_address(), 1) != b'\x80' or any('Hello,' in row or 'Done' in row for row in typed[:22]):
                raise AssertionError('Typed text accepted before Enter')
            machine.enter()
            rows = machine.screen()
            expected = 'Hello, ' + answer
            if rows[0] != expected.ljust(32) or rows[1].rstrip() != 'Done' or not rows[-1].rstrip().startswith('0 OK'):
                raise AssertionError((answer, expected, rows))
            address = vars_address()
            header = read(address, 3)
            length = int.from_bytes(header[1:], 'little')
            if header[0] != 78 or length != len(answer):
                raise AssertionError(('String descriptor differs', header))
            value = read(address + 3, length)
            if value != answer.encode('ascii') or read(address + 3 + length, 1) != b'\x80':
                raise AssertionError('Actual string bytes or end marker differ')
            report['input'].append({'answer': answer, 'before_rows': before, 'typed_rows': typed, 'unset_header_before_enter': header_before, 'after_rows': rows, 'string_header': list(header), 'actual_string_bytes': list(value), 'actual_length': length})
        if len(report['sequence']) != 2 or len(report['input']) != 7:
            raise AssertionError('Missing observations')
        if report['input'][0]['after_rows'] != report['input'][1]['after_rows']:
            raise AssertionError('Repeated answer changed greeting')
        rom = b''.join(read(i, 256) for i in range(0, 16384, 256))
        report.update(status='passed', emulator=machine.server['serverInfo'], emulator_sha256=sha(args.emulator), driver_sha256=sha(driver), verifier_sha256=sha(Path(__file__)), rom_sha256=hashlib.sha256(rom).hexdigest(), fixture_sha256=sha(out / 'greeting.bas'), limits='ROM key-entry on one configured 48K Spectrum; INPUT n$ using its supplied quotation marks. Exact string bytes and screen padding observed. No generic ASK runtime, numeric INPUT, validation, maximum-length, non-ASCII, other platform, physical hardware or learner-effectiveness claim.')
        print('PASS two sequence runs, quoted/value contrast and seven submitted text cases with pre-Enter waiting')
    except BaseException as error:
        report.update(status='failed', failure=repr(error))
        raise
    finally:
        (out / 'native-input.json').write_text(json.dumps(report, indent=2) + '\n')
        machine.close()


if __name__ == '__main__':
    main()
