# Dice Roller — source and scope review

Inspected the retained brief and the final source at
`code-samples/sinclair-zx-spectrum/basic/dice-roller/unit-05/dice-roller.bas`,
with samples main at `953e809`. This is source review, not fresh execution of
the old program.

Line 50 accepts a numeric expression without requiring a positive whole-number
sample size or bounding it. The six separate counters and six conditional
increments at 120–180 implement a tally. Lines 190–240 redraw all six counters
for every roll, although only one changes. Lines 270–320 print one block per
occurrence, with no scaling to the screen width. The old final lesson's proposed
10,000-roll experiment therefore does not keep each face's chart on one row.
The program stops after its result, without an explicit comparison/replay loop.

The retained brief claims that larger samples resolve randomness into order and
uses a roughly equal 1,000-roll result as a ship test. Replace that criterion
with accounting and range invariants. Sampling variability is part of the
experiment, not a failure. Neither one apparently balanced sample nor one uneven
sample settles a fairness claim.

The new brief keeps counted repetition and visible tallies, but uses an array,
fixed percentage scale and explicit previous-result denominator. It removes the
old line budget, compulsory sequence position and artificial ban on arrays.
