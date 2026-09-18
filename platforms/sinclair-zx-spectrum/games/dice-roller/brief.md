# Dice Roller — BASIC prototype brief

**Status:** The user approved the native prototype with live results. Existing
lessons remain available; replacement lesson count and publication remain to
be settled. See the [source review](review.md) and [prototype record](prototype.md).

## Experience and scope

Choose 12, 60, 300 or 1,200 simulated rolls of one six-sided die. Inspect counts
and percentages for all six faces. Repeat a fresh batch, or add another batch
to the current sample. The previous result's percentages stay alongside the new
ones, with both denominators visible. Changing the size begins a fresh sample.

The fixed menu makes the allowed batch sizes explicit and rejects other keys.
The first result has no previous comparison. Later comparisons use the last
result, including a stopped partial result; they are not a separate accumulated
history. An added sample contains its predecessor's rolls and is not independent
of it. Fresh batches draw further values from the same pseudorandom sequence.

Use Q while rolling to stop early and retain the rolls already counted. The
first roll happens before the stop check, so the result always has a positive
denominator. Q at a result or size menu quits to BASIC. R repeats a fresh batch,
A adds, and N returns to size selection. A release gate prevents a held result
key from starting multiple batches. Adding is capped at 9,600 total rolls;
rejecting an addition must preserve both current and previous counts.

There is no wager, win/loss rule, fairness verdict, forced convergence or race.
The display labels one-sixth as the fair-model reference, approximately 16.7%.
A finite sample does not prove the generator fair; a larger realised sample need
not look more balanced than every smaller one. The experiment compares relative
frequencies rather than declaring large absolute differences to be bias.

## Target and presentation

Stock 48K PAL ZX Spectrum, Sinclair BASIC, keyboard and tape. Use the native
family emulator with a lawfully configured ROM; the development host is not a
runtime dependency. Build through ROM keyword entry and a saved auto-starting
TAP. The prototype is deliberately silent.

The results use six two-line rows: face, exact count, current percentage and
previous percentage, followed by a twenty-cell horizontal bar. Every bar uses
the same 0–100% scale. Round its length to the nearest cell (five percentage
points); show percentages rounded to one decimal separately. Small nonzero
shares can have no visible bar, and displayed percentages need not sum to
exactly 100. Colour supplements labels and numbers. The chart develops while rolling, retaining the previous sample alongside it.
Refresh after every roll for batches of 12 and 60; for 300 and 1,200, refresh
after the opening roll and every ten rolls so BASIC spends less time printing.
Always display the exact final or stopped count. Stopping early is visible in the report.

## Teaching value and boundaries

The useful relationships are a random face mapped to one tally, counts whose
sum equals the sample size, proportions with an explicit denominator, and a
bounded picture of those proportions. Use a six-element array rather than
preserving the old prohibition on arrays. The relative size of samples and the
difference between extending and restarting are part of the experiment.

A later compact teaching sequence may start with rolls, accumulate counts,
compute shares, draw the chart and compare runs. It should follow the accepted
prototype rather than inherit a five-unit quota or preceding-course assumptions.
Decide the optional experiment's navigation placement after play review.

## Verification and review gate

Check every allowed batch, ignored inputs, integer nonnegative tallies, total
counts, percentage rounding, bounded bars, previous-sample preservation, fresh
repeat, addition, upper limit, cancellation, held keys and quit. Exercise exact
zero and 100% bars with labelled ROM-command diagnostic setup, separate from
ordinary-play captures. Never test success by requiring a random sample to be
balanced. Inspect the normal, compared and stopped screens at native scale.

Native checks establish behaviour in that emulator configuration, not player
interest or original-hardware timing. Play feedback should determine whether
the comparison is readable and the batch sizes are useful before lessons grow.
