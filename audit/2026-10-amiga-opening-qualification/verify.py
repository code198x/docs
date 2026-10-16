"""Verify retained guest results; this does not rerun the Amiga or a browser."""
from __future__ import annotations

import json
import re
from pathlib import Path


def check(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def values(output: str, kind: str) -> tuple[int, int, int]:
    lines = output.splitlines()
    check(len(lines) == 6, 'Expected six guest output lines')
    check(lines[0].startswith('A long holds big numbers:'), 'Missing long label')
    check(lines[1].startswith(f'A {kind} holds'), 'Wrong type label')
    check(lines[4].startswith(f'100 + 50 in a {kind} gives:'), 'Missing sum label')
    result = tuple(int(lines[i].rsplit(':', 1)[1]) for i in [0, 1, 4])
    initial = result[1]
    total = initial + 50
    expected = (total + 128) % 256 - 128 if kind == 'byte' else total
    check(result == (1_000_000, 100, expected), f'Unexpected {kind} values: {result}')
    return result


def verify() -> dict[str, object]:
    root = Path(__file__).parent / 'runtime'
    outputs = {kind: (root / name).read_text() for kind, name in [('byte', 'types.txt'), ('word', 'word.txt')]}
    observed = {kind: values(output, kind) for kind, output in outputs.items()}
    check(observed['byte'][:2] == observed['word'][:2], 'Initial values differ between paths')
    check(observed['word'][2] - observed['byte'][2] == 256, 'Byte/word difference is not one byte modulus')
    try:
        values(outputs['byte'].replace('-106', '150'), 'byte')
    except ValueError:
        pass
    else:
        raise ValueError('Wrong-value control was accepted')
    counts = {}
    for name in ['types', 'word', 'blitzmode']:
        log = (root / (name + '-compile.txt')).read_text()
        match = re.search(r'^(\d+) line\(s\) compiled, 0 errors\.$', log, re.MULTILINE)
        check(match is not None, f'No successful compiler summary for {name}')
        check(f'Saving executable as "Tools:{name}.exe".' in log, f'No executable for {name}')
        counts[name] = int(match.group(1))
    previous = Path(__file__).parent.parent / '2026-10-amiga-claims/probes'
    for name in ['types', 'word', 'blitzmode']:
        check((root / (name + '.ab3')).read_bytes() == (previous / (name + '.ab3')).read_bytes(), f'Prepared probe changed: {name}')
    return {'byteValues': observed['byte'], 'wordValues': observed['word'], 'wrongValueControl': 'rejected',
            'compilerLines': counts, 'priorProbeIdentity': 'pass',
            'graphicsVisualResult': 'manual observation recorded in observations.json; not asserted by this verifier'}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
