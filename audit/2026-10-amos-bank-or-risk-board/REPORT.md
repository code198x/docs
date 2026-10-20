# Bank or risk: labelled board progression

This pass groups the current round separately from secured points and the session
target. It checks supplied one-round/challenge snapshots and the live display
in AMOS Professional 2.00 through Emu198x. Limit 10, five rounds, target 30,
fresh-key input, the explicit palette and die drawing stay unchanged. Sound
remains separate work; these sources are authoring checkpoints, not published
replacement lessons or learner-trial evidence.

## Source and scope

[inputs.json](inputs.json) pins the maintained source, two snapshots, firmware,
original AMOS image, derived media and tool revisions. The setup remains Emu198x
0.34.2 at `6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, PAL A1200, stock
2 MiB chip RAM, no fast RAM and the recorded Kickstart 3.1 image. Both tools
built offline with existing locked dependencies. Original inputs are unchanged.

Only `BR_DRAW_STATE` changes in the live game. Removing that routine reproduces
the previous source exactly, including scoring, input and the die routine.
The supplied challenge snapshot uses the exact live display block. A changed
label fails that equality check. Both snapshots retain the existing explicit
die routine. The README explains the pixel boxes, text rows, supplied edits,
subtraction and display decisions; it distinguishes snapshots from live play.

The board groups values by their jobs:

- The upper left box shows secured points, target and the current round.
- The lower left box shows this round's total, limit and award or at-risk text.
- The right side labels the last roll beside the unchanged die picture.
- Later rounds, result text and controls occupy separate lines/boxes below.

`BR_MAXTURN-BR_TURNNO` counts rounds after the current one. It is calculated on
each draw instead of using `BR_REMAIN`, whose scoring update has not yet happened
at the first active display. At a final result the label is **Unused rounds**:
remaining capacity does not offer another round after success or failure.
That label decision changes no game state.

The first native layout put the status on text row 13, whose pixels reached
the box bottom at y=111. The [rejected capture](captures/rejected-round-border.png)
shows the collision. Moving that line to row 12 leaves a full text-row gap
above the border. [Rejected source hashes](rejected-source-hashes.json) identify
that earlier layout; all retained pass scripts/inputs use the corrected source
and a fresh boot. This was our layout fault, not an emulator defect.

## Inspected native results

Captures are unedited emulator framebuffers inspected manually. A successful
script exit or syntax test alone does not establish readable labels or agreement
between the numbers and picture. Raw captures retain the emulator's pixel shape.

| Check | Observation to inspect | Capture |
| --- | --- | --- |
| Supplied single round | Total 4, limit 10, last roll 4 and four pips; no session score/target implied. | [One round](captures/rboard-title.png) |
| Supplied challenge bust | Secured 4, target 30, round 2 of 5; total 11, award 0, last roll 5 and three later rounds. | [Challenge snapshot](captures/cboard-title.png) |
| Ready | Secured 0, target 30, round 1 of 5, total/roll 0, empty die and four later rounds. | [Ready](captures/faces-00-Space.png) |
| Six faces | Pips agree with the printed roll and remain separate from the running total. | [1](captures/faces-01-R.png), [2](captures/faces-02-R.png), [3](captures/faces-03-R.png), [4](captures/faces-04-R.png), [5](captures/faces-06-R.png), [6](captures/faces-07-R.png) |
| Exact-limit bank | Round total 10, award 10, secured 10 and four later rounds; SPACE/Q controls. | [Perfect bank](captures/perfect-02-R.png) |
| Chosen bank | Total/award 4, secured 4 and last roll 4 remain distinct. | [Bank](captures/recover-04-B.png) |
| Bust | Total 11, award 0, secured 4, last roll 5 and three later rounds; bust text is readable. | [Bust](captures/recover-07-R.png) |
| New round | Round 3 starts with total/roll 0 and empty die; secured 10 remains and two later rounds are shown. | [Reset](captures/faces-08-Space.png) |
| Early success | Round 3, secured 30, round total/award 10, last roll 6 and two unused rounds; A/Q controls. | [Success](captures/perfect-08-R.png) |
| Fifth-round recovery | Round 5 reaches secured 30 with zero unused rounds; no sixth round is offered. | [Recovery](captures/recover-16-R.png) |
| Early failure | Round 3, score/award 0, total 12, roll 6 and two unused rounds; unreachable-target explanation. | [Failure](captures/fail-08-R.png) |
| Replay | A held for 90 frames starts one fresh challenge; score/total/roll reset, die empty, round 1 and four later rounds. | [Replay](captures/replay-ready.png) |

Both snapshots and the maintained source were imported with Merge ASCII and
run with F1. Independent F2 checks are retained after returning each successful
program to the editor, or in the split import/run phases. Four deterministic game copies cover the
named transitions. The fifth generated case, range-and-limit, was not rerun in
this pass. These checks do not measure random fairness. The maintained random
source was separately run to its title.

The first base/failure replays sent F2/F1 while AMOS was still merging. The
[early failure check](captures/rejected-fail-syntax.png) and
[base check](captures/rejected-base-syntax.png) show that neither established
a syntax pass. The subsequent [failure actions](captures/rejected-fail-08-R.png)
landed in the editor, not the game. [Original actions](rejected-scripts/) and
rejected phase reports are retained. Those attempts are rejected evidence. Base
and failure imports now have longer, separate import-completion phases that
are inspected before running. The other three fixtures did execute their game
sequences, but their early F2 captures also did not establish a syntax check;
the final `syntax-games.json` checks their loaded source after quitting. This
was an authoring-script timing fault; no emulator defect is established.

The [original rules/input/save audit](../2026-10-amos-bank-or-risk-emu198x/REPORT.md),
[palette audit](../2026-10-amos-bank-or-risk-palette/REPORT.md) and
[die audit](../2026-10-amos-bank-or-risk-die/REPORT.md) keep their historical
source pins. Native save/reopen was not repeated for the board revision.

## Reproduction and verification

Build `emu198x-amiga` with `--release --offline --locked --no-default-features`
and `build198x-adf` with `--release --offline --locked` at the recorded revisions.
Use lawful matching local inputs and isolated build/run directories.

Run `python3 prepare.py --disk-tool TOOL --amos AMOS --samples SAMPLES
--run-root RUN`. SAMPLES is the pinned `prototype/` folder, next to `stages/`.
Preparation checks source hashes, generates five probes, and reuses the earlier
audit's qualified OFS reader. The work disk preserves all 78 original AMOS file
contents plus the maintained source. A data disk holds four game probes and the
two snapshots. Both filesystems must verify. [media-checks.json](media-checks.json)
records their identities; a second build must reproduce both disk hashes.

Replay with `python3 replay.py PHASE --emulator EMULATOR --kickstart ROM
--amos AMOS --run-root RUN`, in this order:

1. `work-boot-1000.json`, `work-editor.json`.
2. `rboard-import.json`, `cboard-import.json`.
3. `base-import.json`, inspect `base-imported.png`, then `base-run.json`.
4. `faces-import.json`, `faces-play.json`.
5. `perfect-import.json`, `perfect-play.json`, `replay.json`.
6. `recover-import.json`, `recover-play.json`.
7. `fail-import.json`, inspect `fail-imported.png`, then `fail-run.json` and `fail-play.json`.
8. `syntax-games.json`, `syntax-snapshots.json`. Inspect their `*-checked.png` captures.

Imports restore the blank editor snapshot. Data-disk imports swap back to the
system disk before running; original images stay read-only and work-disk writes
are in emulator memory. Each subprocess has a 50-second timeout, with boot split
into two bounded phases. Inspect screenshots rather than relying on the
emulator's display-active boot flag. [scripts/](scripts/) records exact actions,
[reports/](reports/) records emulator observations, and
[capture-hashes.json](capture-hashes.json) binds the retained PNGs. ROMs, disks,
snapshots and original runtime contents are excluded.

Five exact probe transformations/hashes and nonempty-output refusal pass.
Ruff lint/format, prose, JSON, relative links and public-path/media checks pass;
original firmware/media hashes remain unchanged. The board is ready for review
on the named configuration. Native owner play feedback, an uncoached learner
trial, sound and remaining teaching sources still need their own evidence.
