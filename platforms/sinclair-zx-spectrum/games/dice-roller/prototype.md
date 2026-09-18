# Dice Roller — native prototype

The compact probability experiment is implemented in
`code-samples/sinclair-zx-spectrum/basic/dice-roller/prototype/`. The user
approved the native prototype after trying the live-results revision.
Replacement lessons and publication are the next separate stages. The user requested live results
rather than a separate progress screen; the chart now develops during a batch.

## Behaviour

Choose 12, 60, 300 or 1,200 rolls. Exact counts and rounded percentages appear
beside the previous result, with twenty-cell bars on a fixed 0–100% scale.
Small batches redraw every roll; the larger two redraw after the opening roll
and every ten rolls. The final and stopped displays include every counted roll.
All six proportions must be recalculated because every roll changes their
shared denominator, even though only one tally increases.

R starts a fresh batch, A extends the sample, N selects a new size, and Q quits.
During rolling, Q stops early and keeps the partial sample. Previous means the
last result; an extended sample overlaps its predecessor. Additions stop at
9,600 rolls. No result claims to prove fairness or guarantees that a larger
sample will be more balanced.

## Reproduction and evidence

The sample README contains build, check, audit and native launch commands.
`verification/build.py` enters the maintained listing through actual ROM
keyword keys and records `SAVE "dice" LINE 10`. `check.py` loads that TAP in a
fresh emulator and observes memory without writing it. Its boundary fixture
uses labelled ordinary ROM commands to supply exact zero/100% bars and an
8,400-roll starting total, then ordinary keys to reach the 9,600 limit. The
maximum-count capture is diagnostic; other screenshots show ordinary play.

Target: stock 48K PAL ZX Spectrum with a configured ROM, using native Emu198x.
Evidence in `verification/evidence/` records source, tape and emulator binary
hashes, stored program tokens, execution groups and original screenshots.
This establishes behaviour in the recorded emulator configuration; it is not
original-hardware timing evidence or player acceptance.

The current tape passes 19 execution groups and two labelled boundary fixtures,
including two intermediate live-chart observations before a batch completes.
Source/tape identities, stored tokens and TAP block checksums pass. Samples
commit: `6f129e6`.

Some headless PNG captures show incomplete glyph rendering even after allowing
additional frames, while screen-memory checks pass. Retain these as diagnostic
evidence, not publication assets; the user has accepted the native preview. The capture issue remains separate
from that acceptance and must be resolved before using these images publicly.
