"""Host analysis of the retained BASIC policy; not Spectrum execution.

Run from any directory. The default samples checkout is the sibling repository.
Only legal integer player moves are modelled. Input, drawing, sound and ROM
semantics require a separate native trial.
"""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--samples', type=Path, default=HERE.parents[5] / 'code-samples')
args = parser.parse_args()
rel = Path('sinclair-zx-spectrum/basic/three-in-a-row/unit-06/three-in-a-row.bas')
source = (args.samples / rel).read_bytes()
lines = {int(n): text.strip() for n, text in re.findall(r'^\s*(\d+)\s+(.*)$', source.decode(), re.M)}
# Fail rather than silently analysing a changed policy with the old model.
assert hashlib.sha256(source).hexdigest() == 'aa7940d439adf48abaf001357b04f7e4b4cfeb45406ffaa2073669d5b44e1d26'
triples = []
for n in (1200, 1210, 1220):
    nums = [int(x) for x in lines[n].removeprefix('DATA ').split(',')]
    triples.extend(tuple(nums[i:i+3]) for i in range(0, len(nums), 3))
assert len(triples) == 8 and len(set(triples)) == 8


def winner(b):
    found = 0
    for p, q, f in triples:
        if b[p] and b[p] == b[q] == b[f]:
            found = b[p]
    return found


def choose(b):
    """Translate lines 610–850, including first-match and last-edge ties."""
    for mark, reason in ((2, 'win'), (1, 'block')):
        mv = 0
        for p, q, f in triples:
            if mv == 0 and b[p] == mark and b[q] == mark and b[f] == 0:
                mv = f
            if mv == 0 and b[p] == mark and b[f] == mark and b[q] == 0:
                mv = q
            if mv == 0 and b[q] == mark and b[f] == mark and b[p] == 0:
                mv = p
        if mv:
            return mv, reason
    for i in (5, 1, 3, 7, 9):
        if not b[i]:
            return i, 'centre' if i == 5 else 'corner'
    mv = 0
    for i in range(1, 10):
        if not b[i]:
            mv = i
    return mv, 'edge'


def winning_moves(b, mark):
    result = []
    for i in range(1, 10):
        if not b[i]:
            trial = b.copy()
            trial[i] = mark
            if winner(trial) == mark:
                result.append(i)
    return result


outcomes = Counter()
examples = {}
computer_boards = set()
priority_counts = Counter()


def visit(b, turn, trace):
    win = winner(b)
    end = 'player_win' if win == 1 else 'computer_win' if win == 2 else 'draw' if all(b[1:]) else None
    if end:
        outcomes[end] += 1
        if end not in examples or len(trace) < len(examples[end]):
            examples[end] = trace
        return
    if turn == 1:
        options = [(i, 'player') for i in range(1, 10) if not b[i]]
    else:
        mv, reason = choose(b)
        assert 1 <= mv <= 9 and b[mv] == 0
        wins, threats = winning_moves(b, 2), winning_moves(b, 1)
        assert not wins or mv in wins
        assert wins or not threats or mv in threats
        key = tuple(b[1:])
        if key not in computer_boards:
            computer_boards.add(key)
            priority_counts[reason] += 1
        options = [(mv, reason)]
    for mv, reason in options:
        nxt = b.copy()
        nxt[mv] = turn
        visit(nxt, 3-turn, trace + [{'mark': 'X' if turn == 1 else 'O', 'cell': mv, 'reason': reason}])


visit([0]*10, 1, [])
assert outcomes['player_win'] > 0
result = dict(
    status='passed', method='Exhaustive host traversal of legal integer player replies against a source-pinned translation of the deterministic BASIC policy. Not native execution.',
    source=str(rel), sha256=hashlib.sha256(source).hexdigest(),
    terminal_move_sequences=dict(outcomes), computer_positions=len(computer_boards),
    priority_counts_on_distinct_positions=dict(priority_counts), shortest_examples=examples,
    limitations=['Sequence counts are not human win probabilities.', 'Only the existing player-first mode is modelled.', 'No input, drawing, sound, ROM loading or human playability claims.'])
(HERE / 'review.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
