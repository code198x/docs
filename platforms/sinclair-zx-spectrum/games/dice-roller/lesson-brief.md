# Dice Roller — teaching progression

**Status:** The user authorised the teaching sequence and runnable checkpoints
following acceptance of the live prototype. This specification defines five
building lessons, supported by [five verified checkpoints](lessons.md). Website replacement and publication are not part of this
checkpoint preparation; existing lessons remain available.

## Endpoint and audience

Build a small probability experiment in stock 48K PAL Sinclair BASIC. It is an
optional route, without a game number change or a prerequisite game. Introduce
numbered lines, variables and RUN locally, and link to the established Spectrum
setup and saving instructions during authoring. Silence is deliberate.

The maintained sources live in
`code-samples/sinclair-zx-spectrum/basic/dice-roller/teaching/`.
The finished listing must remain byte-identical to the approved prototype.

| Lesson | Checkpoint | Inspectable result | Explanation and check |
|---|---|---|---|
| Roll a die | roll | Twelve numbered results, each from 1 to 6 | RND, multiplying a range, INT, adding one, FOR/NEXT, semicolons and STOP. Count twelve results; another RUN need not produce the same sequence. |
| Keep the tallies | tally | Six counters whose total is twelve | DIM creates six zeroed array entries; the face chooses the entry to increment. Separate the loop counter from the number of counted rolls. A display subroutine separates calculation from presentation. Add all six counts by hand. |
| Compare shares | shares | Counts and percentages on six rows | Count divided by total gives a proportion; multiply by 100 for percent. Rounding to one decimal uses INT after adding half. Predict why three of twelve is 25%, then check every row against its count. |
| Watch the distribution | live | The chart grows after every roll; Q keeps a partial batch | GO SUB/RETURN redraws an evolving state; row mapping, fixed-scale bars, string slices and clearing old characters. All six shares change denominator on each roll. Check that Q retains a positive total and RUN resets it. |
| Compare experiments | finished | Select a batch, repeat it, extend it and compare the previous result | Copy before resetting; fresh versus accumulated samples; key release and case handling; bounded choices; display cadence. Reopen a saved auto-starting tape and exercise the complete cycle. |

These five boundaries follow different observable questions, rather than the
old lesson count. The first three stop after twelve rolls. Tally and shares
briefly show the numbered rolls before replacing them with a final table; they
do not yet have a live chart or batch controls. Live still uses a fixed batch
of twelve and stops to BASIC after its result. Do not imply that these temporary
limits are the finished program's behaviour.

## Editing and explanation

The opening checkpoint is a new program: show its full listing without telling
the learner to add every numbered line. Subsequent checkpoints have exact
add/replace/delete metadata in `checkpoints.json` and maintained `changes.bas`
listings. Show short full programs directly; introduce changed routines with
exact line instructions as the source grows. The audit reconstructs each state
from those changes. There are no line deletions in this progression.

Explain each new routine where it first appears. In tally, the header at 1000
prints labels, the loop beginning at 1100 reads the array, and line 750 prevents
execution falling through into subroutines. A row is `5+2*(j-1)`: six faces map
to rows 5, 7, 9, 11, 13 and 15. Leave the intervening rows for bars introduced
later; this spacing is a layout decision, not an array requirement.

In shares, `INT(1000*t(j)/n+0.5)/10` rounds a percentage to one decimal.
For example, one of twelve is shown as 8.3%. Counts remain exact integers.
Rounded percentages need not total exactly 100; do not correct one row to force
them to do so. The fair-model reference of about 16.7% is not a promised result.

Live replaces the per-roll PRINT with a call to the display routine. Explain
why the first roll precedes division, and why a count that stays unchanged can
have a falling percentage. The bar has twenty cells: round `20*t(j)/n` to a
whole cell. Each cell represents five percentage points. Slice the hash string
to that width, then print enough spaces to erase the remainder of an older,
longer bar. Zero-length slices produce empty strings. CHR$ 91 and CHR$ 93 supply
the brackets. A small nonzero count may produce no filled cell; the number is
still visible. Fixed bars allow comparison without stretching each sample's
largest face to full width.

Teach the final lesson in four connected parts, with the complete checkpoint
available throughout:

1. Store the old counts in p(), retain their total in pn, then either clear t()
   for a fresh run or retain it for an addition. Copy before clearing. Render
   the previous percentages once; keep updating the current side.
2. Introduce the release/read routine at 8000, lowercase normalisation, valid
   menu choices and result actions. Explain why a held Q stops but does not
   immediately dismiss the result, and why unknown keys change nothing.
3. Select 12, 60, 300 or 1,200 rolls. The first two refresh every roll, the larger
   two every ten plus the first and final roll. Calculation still counts every
   roll. The 9,600 limit bounds accumulation; rejection preserves both samples.
   `target` records the intended total; `done` records this batch's actual work.
4. Save with `SAVE "dice" LINE 10`, export the tape using the documented emulator
   workflow, and load it in a fresh session. Saving this program does not promise
   to preserve the active comparison after auto-start initialises its arrays.

## Questions and experiments to author

- Before INT, `RND*6` spans from zero up to but not including six. Explain why
  adding one after INT maps this to the six array positions, rather than seven.
- Trace faces 2, 2, 6 and 1: counts are 1, 2, 0, 0, 0, 1, total four. Face 2 is
  50%; its bar occupies ten cells. This is a paper trace, not a claimed random run.
- If face 2 stays at two while total rolls rise from four to five, its share
  falls from 50% to 40%. Another face's roll can shorten its bar.
- Repeat several twelve-roll samples. Compare their shares without requiring
  any particular pattern or treating unevenness as a bug.
- Compare R with A: R replaces the sample; A includes its predecessor, so those
  two results are not independent. Larger samples need not be more balanced on
  every particular trial, and neither appearance proves the generator fair.

Use these as selected prompts with explained answers, not a test after every
listing. Experiments must not depend on a lucky random outcome. Do not ask the
reader to enlarge the early numbered-roll listings beyond the screen; larger
batches belong to the finished bounded menu.

## Verification and next authoring work

Enter all five programs independently through ROM keyword keys, save tapes and
load each in a fresh emulator. Check first-stage range and roll count, tally
accounting, rounded shares, intermediate live displays, stopping, restart and
stored-program identity. Run the full accepted prototype suite against the
independently built finished tape. Audit editing transitions and final identity.

During website authoring, verify primary manual references for the language
features, preserve existing routes or redirect by subject, and keep this in the
optional experiment area. Do not use the prototype's imperfect headless PNGs as
public media. Check the rendered editing instructions, keyboard notes, worked
answers, complete source includes, links and saving workflow before review.

## Source basis

Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming*
(Sinclair Research, second edition, 1983), chapter 11, p. 73, describes the
half-open RND range and the same INT-based die mapping. Chapter 8, p. 51,
explains omitted slice bounds and empty slices when the start exceeds the end.
These passages were inspected for the progression; the maintained programs
supply configuration-specific execution evidence separately.
