"""Observe Spectrum fixed-array boundaries and shared subroutine variables."""
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
        raise RuntimeError('Cannot load maintained transport')
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), out)
    report = {'status': 'running', 'statements': [], 'checks': []}

    def statement(line: str) -> None:
        if line.startswith('DIM '):
            machine.key('d')
            machine.text(line[4:])
            machine.enter()
        else:
            machine.statement(line)
        rows = machine.rows()
        if line[0].isdigit():
            # ROM edit mode lists stored lines rather than reporting command completion.
            compact = ''.join(line.split())
            if not any(''.join(row.split()).replace('>', '') == compact for row in rows):
                raise AssertionError(('Stored line not shown', line, rows))
        elif not rows[-1].startswith('0 OK'):
            raise AssertionError((line, rows))
        report['statements'].append(line)

    def printed(expression: str, expected: int | None) -> None:
        machine.statement('CLS')
        machine.statement('PRINT ' + expression)
        rows = machine.rows()
        if expected is None:
            if not rows[-1].startswith('3 Subscript wrong'):
                raise AssertionError((expression, rows))
        elif rows[0] != str(expected) or any(rows[1:22]) or not rows[-1].startswith('0 OK'):
            raise AssertionError((expression, expected, rows))
        report['checks'].append({'expression': expression, 'expected_number': expected, 'rows': rows})

    try:
        statement('DIM a(3)')
        for i, value in enumerate([10, 20, 30], 1):
            statement(f'LET a({i})={value}')
            printed(f'a({i})', value)
        printed('a(0)', None)
        printed('a(4)', None)
        statement('LET a(2)=99')
        for i, value in enumerate([10, 99, 30], 1):
            printed(f'a({i})', value)
        statement('DIM a(4)')
        for i in range(1, 5):
            printed(f'a({i})', 0)
        statement('100 LET n=n*2')
        statement('110 RETURN')
        for value in [5, 3]:
            statement(f'LET n={value}')
            statement('GO SUB 100')
            printed('n', value * 2)
        chunks = [bytes(machine.call('memory_read', addr=address, len=256)['bytes'])
                  for address in range(0, 16384, 256)]
        if len(chunks) != 64 or any(len(c) != 256 for c in chunks):
            raise AssertionError('Incomplete ROM fingerprint')
        report.update(status='passed', emulator=machine.server['serverInfo'], emulator_sha256=sha(args.emulator), driver_sha256=sha(driver), verifier_sha256=sha(Path(__file__)), rom_sha256=hashlib.sha256(b''.join(chunks)).hexdigest(), limits='One configured Spectrum ROM. Fixed DIM arrays and ordinary shared GO SUB variables differ from the explanatory growable lists and copied numeric parameters. No pseudocode interpreter, other target or learner claim.')
        print(f"PASS: {len(report['checks']) - 2} numeric outputs and two array-bound errors")
    except BaseException as error:
        report.update(status='failed', failure=repr(error))
        raise
    finally:
        (out / 'native-structure.json').write_text(json.dumps(report, indent=2) + '\n')
        machine.close()


if __name__ == '__main__':
    main()
