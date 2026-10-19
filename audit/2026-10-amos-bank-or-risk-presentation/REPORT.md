# AMOS session-to-presentation bridge

Six complete sources connect the checked session program to a shared display,
grouped board, separate bank/bust/success sounds and a ready screen. The
continuous teaching route keeps its completed-round counter. It no longer asks
a learner to jump into the older prototype's different For loop and quit flags.
These are executed authoring checkpoints, not published replacement lessons or
findings about beginner understanding.

## Configuration and identity

[inputs.json](inputs.json) pins the sources, original media and tools. Execution
uses AMOS Professional 2.00, Emu198x 0.34.2 at
`6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, PAL A1200 with stock 2 MiB chip RAM
and no fast RAM. Build198x `f7016398deb1fff9dc1efb6713dfab8c7bacf2d0`
masters and verifies the OFS disks. Both tools build offline from locked existing
dependencies. This is configuration-specific evidence, not a minimum machine
claim. No emulator, disk-tool or dependency changes are part of this work.

The [preparation helper](prepare.py) reuses the qualified
[sound filesystem builder](../2026-10-amos-bank-or-risk-sound/prepare.py), which
preserves all 78 original runtime file contents. The six ASCII sources and
[eleven variants](variants.json) occupy a separate source disk. Constant-roll
variants replace one assignment; the muted copy additionally sets Volume to 0.
The session's replay source with roll 4 supplies the extraction baseline.
These explicit variants are authoring tests, not random-play observations.

The older prototype and top-level presentation samples are unchanged. Their
historical audits retain their original source pins. The integrated source here
is [ready-screen.amos](https://github.com/code198x/code-samples/blob/97a6004802a4b86269f42baf7bc1ed0fd9468ca2/commodore-amiga/amos/bank-or-risk/stages/presentation/ready-screen.amos).

## What the bridge teaches

`shared-display` moves the existing active/result display blocks into one named
routine. Expanding those calls restores the complete session source exactly.
The renderer reads state and draws; input and score changes remain outside it.

`grouped-board` changes only that routine and the three control-text positions.
It reuses the explained supplied board's shapes and coordinates. The earlier
board names the current round, whereas the session counts completed rounds.
During play, rounds after the current one are `maximum-completed-1`; at a result,
remaining opportunities are `maximum-completed`. An ending calls that capacity
unused rounds. The source never increments the score counter to repair a label.

The three sound stages reuse the earlier exact setup and event routines.
One call follows the award, completed increment and session decision. Bank,
bust and success enter separately; success replaces the last bank cue.
Playback does not introduce a blocking Wait. Replay and exit stop sound.

`ready-screen` introduces the instructions and Space/Q choice separately.
Space enters the existing session; A after an ending resets directly to play.
The seed stays outside replay and the last scan code survives it. All six
sources retain the session's exact fresh-key and die routine bodies. The guide
explains each edit, routine contract and prediction/repair answer, with links
to the supplied graphics and tone experiments before their live integration.

## Capture setup correction

The first board script requested a screenshot immediately after restoring a
snapshot, before running a native frame. The tool rejected it with
`script execution failed: no frame has been captured`. The corrected script
runs 30 frames before the initial capture. [diagnostics](diagnostics/) retains
the rejected script and error. No source change was needed. A snapshot restore
alone is not treated as a captured display.

## Observed checks

| Check | Outcome | Evidence |
| --- | --- | --- |
| Syntax and entry | Each complete source and supplied variant imports, passes F2 and reaches its initial view. | [scripts](scripts/), [captures](captures/) |
| Display extraction | B/X at zero, held R, bank, wait and next-round reset have identical pictures before/after extraction. | [baseline bank](captures/baseline-3.png), [shared bank](captures/shared-3.png) |
| Completed versus current | Initial completed 0 leaves four rounds after this one. Active round 2 has completed 1 and three later rounds. Its bust completes round 2, keeps secured 4 and leaves three opportunities. | [initial](captures/board-initial.png), [next](captures/board-next.png), [bust](captures/board-bust.png) |
| Once-only cues | A perfect bank sounds once; bust sounds once at one quarter of the bank frequency. Holding/invalid controls and waiting do not repeat a result cue. | [audio](audio/), [stable bank](captures/bank-stable.png) |
| Third-round success | Three perfect rounds reach 30 at completed 3 with two unused rounds. The first two cues are banks; the third has twice their frequency. | [success](captures/ready-result-3.png) |
| Strict impossibility | Two opening busts leave a possible 30 and permit another round; three leave at most 20 and stop. | [equality boundary](captures/loss-result-2.png), [ending](captures/loss-result-3.png) |
| Fifth-round success | Five chosen banks of 6 reach 30 at completed 5. Terminal input cannot begin a sixth round. | [fifth result](captures/fifth-result-5.png), [held ending](captures/fifth-no-sixth.png) |
| Stable endings and replay | Waiting and X/R/Space preserve terminal pictures. Held A resets once; held fresh R acts once. A new bank starts from zero secured points. | [reset](captures/ready-reset.png), [fresh roll](captures/ready-fresh.png), [new bank](captures/ready-new-bank.png) |
| Sound off | Muted and audible perfect-run pictures agree, including each roll and result. Muted recordings are silent. | [muted success](captures/muted-result-3.png) |
| Ready screen and quit | R/X leave the title unchanged; held Space enters an empty challenge. Q returns to the editor from title, active, between-round and terminal states. | [title](captures/title-stable.png), [entered](captures/ready-active.png) |
| Ordinary play | The random source starts, rolls, banks, continues and exits. | [bank](captures/random-bank.png), [next](captures/random-next.png) |
| Native storage | A verified disk export cold-boots independently, loads the native saved program, reaches its ready screen, rolls/banks, continues and exits. | [loaded](captures/integrated-reopened-listing.png), [bank](captures/reopened-bank.png) |

[verify.py](verify.py) checks source/variant identities, exact extraction
restoration, isolated renderer and cue edits, unchanged routine bodies, required
nonempty captures, meaningful identical-picture pairs, PCM counts/frequencies,
valid exported media and preserved runtime files. Image equality checks stability
and agreement; it does not read numerical labels or F2 banners. Those, the die
pips and layout are inspected directly.

The [audio measurements](verification.json) distinguish one bank, lower bust and
higher success cue, silence and no full-scale PCM samples in these recordings.
They do not judge pleasantness or listening comfort. A retained sound setting
is not evidence of learner preference.

## Reproduction and limits

Build the pinned emulator with `--release --offline --locked
--no-default-features` and Build198x with `--release --offline --locked`.
Run `prepare.py --disk-tool TOOL --amos AMOS --samples SAMPLES --run-root RUN`
with lawful matching inputs and an empty output folder. SAMPLES is the
bank-or-risk folder containing prototype and stages. Populated output is refused.

Run `replay.py PHASE.json --emulator EMULATOR --kickstart ROM --amos AMOS
--run-root RUN` in [sequence.json](sequence.json) order. Each subprocess has a
50-second bound. Restore points split longer runs without pretending they are
native Load operations. Only the independent storage check cold-boots a saved
program. After `integrated-export-requests.json`, require `TOOL verify
RUN/integrated-settled.save.adf` before the cold boot.

The save sequence allows guest filesystem writes to finish before export.
Its waits are observations for this configuration, not a universal safe delay.
The earlier [incomplete-write diagnostic](../2026-10-amos-bank-or-risk-session/REPORT.md#complete-disk-writes-before-trusting-the-export)
explains why a closed Save As requester alone is insufficient. A failed export
must preserve the edited session for recovery, rather than being treated as a
successful save.

[verification.json](verification.json) records 183 capture checks, 36
identical-picture pairs and 21 PCM checks. The native saved program is 5,726
bytes. Six negative controls reject a missing required capture, a valid but
wrong reset picture, silent bank audio, a valid disk without the saved program,
a changed source and populated preparation output.
[media-checks.json](media-checks.json) records media identities, independent
reconstruction and negative controls. [reports](reports/) replace local run
roots with `${RUN}`. [artifact-hashes.json](artifact-hashes.json) binds unedited
native captures and PCM. ROMs, licensed runtime contents, ADFs, native programs
and snapshots are excluded.

The named input windows do not establish every possible arrival time. Exact
source restoration does not prove all latency conditions equivalent. The
separate random-range/angle investigation remains outside this work. Authored
replacement lessons, human play/listening feedback and the uncoached learner
trial remain pending. No public lessons change.
