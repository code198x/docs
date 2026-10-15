"""Observe pre/post-test progress and guarded non-progress through Spectrum ROM entry."""
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
    parser.add_argument('--missing-update', action='store_true', help='Known-red: require a missing-decrement loop to finish naturally')
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    driver = args.samples / 'sinclair-zx-spectrum/basic/meet-basic/completion-verification/verify.py'
    spec = importlib.util.spec_from_file_location('completion', driver)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load maintained ROM transport')
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    machine = transport.Spectrum(str(args.emulator), out)
    report = {'status': 'running', 'control': args.missing_update, 'cases': []}

    def read(address: int, size: int) -> bytes:
        if size == 0:
            return b''
        data = bytes(machine.call('memory_read', addr=address, len=size)['bytes'])
        if len(data) != size:
            raise AssertionError('Incomplete trace read')
        return data

    def enter(line: str) -> None:
        if ' POKE ' in line:
            number, body = line.split(' POKE ', 1)
            machine.text(number + ' ')
            machine.key('o')
            machine.text(body)
            machine.enter()
        else:
            machine.statement(line)

    try:
        cases = [('pre', n) for n in range(4)] + [('post', n) for n in range(4)] + [('reset', 3)]
        if args.missing_update:
            cases = [('missing', 3)]
        for kind, initial in cases:
            source = [f'10 LET l={initial}: LET p=0',
                      '20 LET z=0' if kind == 'post' else '20 IF l<1 THEN GO TO 90',
                      '30 LET l=3: LET p=p+1' if kind == 'reset' else '30 LET p=p+1',
                      '40 POKE 40000+p,l',
                      '50 LET l=l' if kind == 'missing' else '50 LET l=l-1',
                      '60 IF p=4 THEN GO TO 100',
                      '70 IF l>0 THEN GO TO 30' if kind == 'post' else '70 GO TO 20',
                      '90 PRINT "Done ";p;",";l: GO TO 120',
                      '100 PRINT "Guard ";p;",";l', '120 PRINT "End"']
            fixture = out / f'{kind}-{initial}.bas'
            fixture.write_text('\n'.join(source) + '\n')
            for line in source:
                enter(line)
            machine.statement('RUN')
            machine.frames(150)
            rows = machine.rows()
            if rows[1] != 'End' or any(rows[2:22]) or not rows[-1].startswith('0 OK'):
                raise AssertionError(('Audit did not complete', rows))
            header = rows[0].split(' ')
            if len(header) != 2 or header[0] not in ['Done', 'Guard']:
                raise AssertionError('Missing natural/guard distinction')
            passes, final = map(int, header[1].split(','))
            if passes not in range(5):
                raise AssertionError('Unbounded audit pass count')
            trace = list(read(40001, passes))
            row = {'kind': kind, 'initial': initial, 'completion': header[0], 'passes': passes, 'final_lives': final, 'actual_trace': trace, 'rows': rows}
            report['cases'].append(row)
            if kind == 'reset':
                expected = ('Guard', 4, 2, [3, 3, 3, 3])
            elif kind == 'post' and initial == 0:
                expected = ('Done', 1, -1, [0])
            else:
                expected = ('Done', initial, 0, list(range(initial, 0, -1)))
            if (header[0], passes, final, trace) != expected:
                raise AssertionError('Expected natural progress differs: ' + repr(row))
        if not args.missing_update and (len(report['cases']) != 9 or sum(len(row['actual_trace']) for row in report['cases']) != 17):
            raise AssertionError('Missing natural or guarded cases')
        rom = b''.join(read(i, 256) for i in range(0, 16384, 256))
        report.update(status='passed', emulator=machine.server['serverInfo'], emulator_sha256=sha(args.emulator), driver_sha256=sha(driver), verifier_sha256=sha(Path(__file__)), rom_sha256=hashlib.sha256(rom).hexdigest(), fixtures={p.name: sha(p) for p in out.glob('*.bas')}, limits='Eight bounded natural exits and one guard intervention through configured Spectrum 48K ROM IF/GO TO. Four-pass audit guard is not natural termination. Actual trace bytes and screen results, not native WHILE/REPEAT pseudocode, every starting value, keyboard waiting, performance, physical hardware or learner effectiveness.')
        print('PASS eight natural pre/post cases, reset guard intervention, and 17 actual trace bytes')
    except BaseException as error:
        report.update(status='failed', failure=repr(error))
        raise
    finally:
        (out / 'native-progress.json').write_text(json.dumps(report, indent=2) + '\n')
        machine.close()


if __name__ == '__main__':
    main()
