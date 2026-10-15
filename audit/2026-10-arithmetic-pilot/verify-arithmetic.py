"""Read actual Spectrum ROM arithmetic results and assignment traces."""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from math import floor
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
        raise RuntimeError('Cannot load ROM transport')
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), out)
    report = {'status': 'running', 'checks': [], 'assignments': [], 'reconstruction': []}

    def statement(line: str) -> None:
        machine.statement(line)
        if not machine.rows()[-1].startswith('0 OK'):
            raise AssertionError((line, machine.rows()))
        report['assignments'].append(line)

    def printed(expression: str, expected: Fraction | int | None) -> Fraction | None:
        machine.statement('CLS')
        machine.statement('PRINT ' + expression)
        rows = machine.rows()
        if expected is None:
            if not rows[-1].startswith('6 Number too big'):
                raise AssertionError((expression, rows))
            actual = None
        else:
            if any(rows[1:22]) or not rows[-1].startswith('0 OK'):
                raise AssertionError((expression, rows))
            actual = Fraction(rows[0])
            if actual != expected:
                raise AssertionError((expression, str(expected), rows))
        report['checks'].append({'expression': expression, 'expected': str(expected), 'actual': str(actual), 'rows': rows})
        return actual

    try:
        for expression, expected in [
            ('2+3*4', 14), ('(2+3)*4', 20), ('20/5*2', 8), ('20/(5*2)', 2),
            ('20-5-2', 13), ('20-(5-2)', 17), ('7/2', Fraction(7, 2)),
            ('INT (7/2)', 3), ('INT (-7/2)', -4), ('INT (7/2+1/2)', 4),
            ('INT (13/4+1/2)', 3), ('INT (15/4+1/2)', 4),
            ('INT ((22-7)/2)', 7),
        ]:
            printed(expression, expected)
        for n, d in [(0, 2), (1, 2), (7, 2), (8, 2), (9, 2), (0, 4), (3, 4), (4, 4), (5, 4), (31, 32), (32, 32), (33, 32)]:
            quotient, remainder = divmod(n, d)
            q = printed(f'INT ({n}/{d})', quotient)
            r = printed(f'{n}-{d}*INT ({n}/{d})', remainder)
            if q is None or r is None or q * d + r != n or not 0 <= r < d:
                raise AssertionError('Actual quotient/remainder do not reconstruct input')
            report['reconstruction'].append({'original': n, 'divisor': d, 'quotient': int(q), 'remainder': int(r), 'reconstructed': int(q * d + r)})
        for line in ['LET score=0', 'LET score=score+10', 'LET score=score+10']:
            statement(line)
        printed('score', 20)
        statement('LET a=2')
        statement('LET b=5')
        statement('LET a=b')
        statement('LET b=a')
        printed('a', 5)
        printed('b', 5)
        for line in ['LET a=2', 'LET b=5', 'LET spare=a', 'LET a=b', 'LET b=spare']:
            statement(line)
        printed('a', 5)
        printed('b', 2)
        printed('1/0', None)
        chunks = [bytes(machine.call('memory_read', addr=address, len=256)['bytes'])
                  for address in range(0, 16384, 256)]
        if any(len(chunk) != 256 for chunk in chunks):
            raise AssertionError('Incomplete ROM chunk')
        rom = b''.join(chunks)
        if len(rom) != 16384 or floor(Fraction(-7, 2)) != -4:
            raise AssertionError('Incomplete ROM read or invalid floor oracle')
        report.update(status='passed', emulator=machine.server['serverInfo'], emulator_sha256=sha(args.emulator), driver_sha256=sha(driver), verifier_sha256=sha(Path(__file__)), rom_sha256=hashlib.sha256(rom).hexdigest(), limits='One configured Spectrum ROM. INT maps floor; remainder and non-negative half-up are explicit expressions, not BASIC REMAINDER/ROUND keywords. No other target, timing or learner claim.')
        print(f"PASS: {len(report['checks']) - 1} numeric outputs, one zero-divisor error, {len(report['reconstruction'])} reconstruction invariants")
    except BaseException as error:
        report.update(status='failed', failure=repr(error))
        raise
    finally:
        (out / 'native-arithmetic.json').write_text(json.dumps(report, indent=2) + '\n')
        machine.close()


if __name__ == '__main__':
    main()
