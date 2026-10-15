"""Observe first-match dispatch, separate tests and saved flags in the Spectrum ROM."""
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
    parser.add_argument('--wrong-only', action='store_true', help='Known-red: require the wrong broad-first program to meet the intended bands')
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
    report = {'status': 'running', 'control': args.wrong_only, 'dispatch': [], 'state': []}

    def enter(line: str) -> None:
        if ' POKE ' in line:
            number, body = line.split(' POKE ', 1)
            machine.text(number + ' ')
            machine.key('o')
            machine.text(body)
            machine.enter()
        else:
            machine.statement(line)

    def read(address: int, size: int) -> bytes:
        data = bytes(machine.call('memory_read', addr=address, len=size)['bytes'])
        if len(data) != size:
            raise AssertionError('Incomplete memory read')
        return data

    def run_program(label: str, source: list[str]) -> list[str]:
        fixture = out / (label + '.bas')
        fixture.write_text('\n'.join(source) + '\n')
        for line in source:
            enter(line)
        machine.statement('RUN')
        machine.frames(150)
        rows = machine.rows()
        if not rows[-1].startswith('0 OK'):
            raise AssertionError((label, rows))
        return rows

    try:
        fixtures = {
            'ordered': ['10 FOR s=0 TO 100', '20 LET b=1', '30 IF s>79 THEN LET b=3: GO TO 70', '40 IF s>49 THEN LET b=2', '70 POKE 40000+s,b', '80 NEXT s', '90 PRINT "Done"'],
            'broad-first': ['10 FOR s=0 TO 100', '20 LET b=1', '30 IF s>49 THEN LET b=2: GO TO 70', '40 IF s>79 THEN LET b=3', '70 POKE 40000+s,b', '80 NEXT s', '90 PRINT "Done"'],
            'separate': ['10 FOR s=0 TO 100', '20 LET b=0', '30 IF s>49 THEN LET b=b+1', '40 IF s>79 THEN LET b=b+2', '70 POKE 40000+s,b', '80 NEXT s', '90 PRINT "Done"'],
        }
        for label in (['broad-first'] if args.wrong_only else fixtures):
            rows = run_program(label, fixtures[label])
            if rows[0] != 'Done' or any(rows[1:22]):
                raise AssertionError('Continuation output differs')
            observed = list(read(40000, 101))
            intended = [1 + int(score >= 50) + int(score >= 80) for score in range(101)]
            expected = intended if label == 'ordered' or args.wrong_only else [1 + int(score >= 50) for score in range(101)] if label == 'broad-first' else [int(score >= 50) + 2 * int(score >= 80) for score in range(101)]
            mismatches = [score for score in range(101) if observed[score] != intended[score]]
            report['dispatch'].append({'label': label, 'rows': rows, 'actual': observed, 'expected_for_policy': expected, 'mismatches_against_intended_bands': mismatches})
            if observed != expected:
                raise AssertionError('Branch policy differs at scores: ' + str([i for i in range(101) if observed[i] != expected[i]]))
            if label == 'broad-first' and mismatches != list(range(80, 101)):
                raise AssertionError('Broad-first fault did not expose all 21 high scores')
        # Remove prior loop/continuation lines through the ROM editor, not memory writes.
        for number in ['70', '80', '90']:
            enter(number)
        snapshots = ['10 LET g=4', '20 LET t=g<7', '30 LET g=9', '40 PRINT t;",";g<7', '50 LET t=g<7', '60 PRINT t']
        rows = run_program('snapshot', snapshots)
        if rows[:2] != ['1,0', '0'] or any(rows[2:22]):
            raise AssertionError(('Snapshot/refreshed comparison differs', rows))
        report['state'].append({'label': 'snapshot', 'rows': rows, 'meaning': 'saved true, fresh false, reassigned false'})
        latch = ['10 LET l=0', '20 LET o=0', '30 IF l=0 THEN LET o=1', '40 LET l=3', '50 PRINT o;",";l=0', '60 IF o THEN PRINT "Game over"', '70 LET o=0', '80 PRINT o', '90 PRINT "Done"']
        rows = run_program('latch-reset', latch)
        if rows[:4] != ['1,0', 'Game over', '0', 'Done'] or any(rows[4:22]):
            raise AssertionError(('Latch/reset differs', rows))
        report['state'].append({'label': 'latch-reset', 'rows': rows, 'meaning': 'restore lives retains latch; explicit reset clears it'})
        rom = b''.join(read(i, 256) for i in range(0, 16384, 256))
        report.update(status='passed', emulator=machine.server['serverInfo'], emulator_sha256=sha(args.emulator), driver_sha256=sha(driver), verifier_sha256=sha(Path(__file__)), rom_sha256=hashlib.sha256(rom).hexdigest(), fixtures={p.name: sha(p) for p in out.glob('*.bas')}, limits='Configured Spectrum 48K ROM execution. Integer scores 0–100, separate IF/GO TO dispatch and numeric 0/1 flags. This is not native execution of pseudocode ELSE IF, a general interpreter proof, performance, original hardware or learner evidence.')
        print('PASS 303 actual dispatch bytes, broad-first fault at 21 scores, snapshot and latch/reset runs')
    except BaseException as error:
        report.update(status='failed', failure=repr(error))
        raise
    finally:
        (out / 'native-state.json').write_text(json.dumps(report, indent=2) + '\n')
        machine.close()


if __name__ == '__main__':
    main()
