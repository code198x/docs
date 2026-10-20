# A brighter board and a visible roll

Three complete sources develop the game's presentation: colour roles on the
existing board, a spaced board with a larger die, then a slowing die reveal.
The endpoint is [rolling-die.amos](https://github.com/code198x/code-samples/blob/c7c93b2f04be8433db634b29b08a057c4f9cab67/commodore-amiga/amos/bank-or-risk/stages/arcade/rolling-die.amos). The five-round score chase,
memory-only Best, awards, rescue and result cues are unchanged. Earlier sources
remain intact; no public lessons change.

The user played the previous rescue endpoint and reported that it works well,
then requested colour, spacing and an animated roll. They selected a brighter
arcade palette. This record establishes native behaviour for that refinement;
acceptance of the new presentation and learner understanding remain separate.

## Configuration and construction

[inputs.json](inputs.json) pins the three sources, lawful original media and
Emu198x 0.34.2 at `6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`. The profile is
PAL A1200, stock 2 MiB chip RAM and no fast RAM, running AMOS Professional 2.00.
Build198x is pinned at `f7016398deb1fff9dc1efb6713dfab8c7bacf2d0`. These are
configuration-specific observations, not minimum hardware claims. Existing
locked dependencies are used; neither tool changes.

[prepare.py](prepare.py) reconstructs a writable runtime disk preserving all 78
original file contents. `arcade.adf` contains three maintained sources and eight
controlled copies; the ninth variant, a 4,5,6,1 supplier, has its own disk.
[variants.json](variants.json) records every exact transformation and hash.
Constant suppliers, motion disabled, sound muted and a grayscale copy are
explicit test tools, not alternative random implementations.

## Teaching and presentation

`arcade-colours` changes palette and selected pens while retaining the previous
geometry. Flash Off stops AMOS’s default animation of palette entry 3 before
setting the stable palette. Cyan marks secured points, yellow points at risk, pink the title and
rescue question, mint rescue availability/new best, and lavender secondary
labels. Text, numbers and positions carry the same meanings without colour.
The grayscale copy reproduces the earlier baseline's settled pictures.
[contrast.json](contrast.json) lists actual RGB12 foreground/background pairs,
including text on the panel and dark pips on the cream die. All text pairs meet
the specified 4.5 ratio. This calculation does not establish every person's
colour perception or every physical display's output.

`arcade-layout` gives the header, secured score, round total, die, rescue,
message, five award slots and controls separate regions. The larger die has a
relative origin so that pips and outline move together. Its clearing region is
bounded away from neighbouring labels. Pen and Paper return to their documented
values. NEW BEST moves to the header, leaving the result message clear.

`rolling-die` changes only the roll picture routine and adds `BR_ANIMATE=1`.
Six preview faces move two pixels either side of the resting origin. Successive
waits of one through six vertical blanks slow the reveal: 21 waits plus drawing
and execution. The actual random face was already chosen once by the caller;
the preview never draws another random number or updates a score. The busy
prompt says Rolling... Q quits. Q is checked during the waits and exits before
committing that roll. Other busy-interval choices are discarded; the unchanged
fresh-key reader takes the next decision once settled. There is no reaction
timer. `BR_ANIMATE=0` gives the direct result without the moving preview.

The [guide](https://github.com/code198x/code-samples/tree/amos-bank-or-risk-prototype/commodore-amiga/amos/bank-or-risk/stages/arcade)
explains exact edits, coordinates, palette/Pen/Paper roles, slot calculation,
relative pips, preview/state separation and the static setting. Predictions and
repairs accompany the additions. Complete sources do not establish the right
lesson boundaries or learner understanding.

## Observed native outcomes

The confirmation batch shows stable pink title/question text, separate total and
die regions, readable two-digit awards, a distinct completed zero, current ?
and future dashes. The die clears its previous outline/pips without clearing the
last-roll label. NEW BEST remains separate from the final result message.

| Check | Observed result | Evidence |
| --- | --- | --- |
| Import and launch | Three maintained sources and nine controlled copies import, receive F2 checks and reach the ready screen through F1. The independently reopened endpoint also displays No errors. | [captures](captures/), [reports](reports/), [reopened syntax](captures/arcade-syntax.png) |
| Palette | All eight intended RGB12 colours occur in the final native image; the grayscale colour-stage views exactly match the old baseline at active, roll and result. | [final](captures/live-result-5.png), [contrast](contrast.json) |
| Five rounds | Perfect 10 advances through secured 10/20/30/40/50; the first target crossing continues, and the fifth completed round records Best 50. | [goal](captures/live-result-3.png), [record](captures/live-result-5.png) |
| Replay | A resets secured points, completed count, rescue and all award slots while retaining Best 50; held replay does not roll. | [reset](captures/live-reset.png), [stable](captures/live-reset-wait.png) |
| Rescue | A bust of 12 leaves completed zero and the first slot pending. Invalid choices are stable; U restores 6 and spends rescue, while B accepts zero and keeps it. A later spent-token bust completes immediately. | [pending](captures/risk-pending.png), [restored](captures/risk-restored.png), [accepted](captures/risk-accepted.png), [spent](captures/risk-spent-bust.png) |
| Distinct restored face | Supplied 4,5,6 busts at 15; U restores total 9 and face 5. A further 1 banks perfect 10. | [bust](captures/varied-bust.png), [restore](captures/varied-restored.png), [perfect](captures/varied-perfect.png) |
| Roll preview | Several changing pip patterns move inside the die region while total remains zero and accepted last roll is absent. The actual supplied five then appears once with total five. | [preview](captures/motion-09.png), [settled](captures/motion-30.png), [native clip](video/roll.mp4) |
| Static/muted agreement | All five settled roll/result views agree exactly with both static and muted copies; the latter recordings are silent. | [verification](verification.json), [audio](audio/) |
| Busy input and Q | A B tap during rolling does not bank the result. Q during the reveal stops before committing it. Title, active, pending rescue, between-round and final Q windows stop the program too. | [ignored bank](captures/busy-bank-ignored.png), [reveal exit](captures/motion-editor.png), [reports](reports/) |
| Result cues | Five perfect rounds produce bank, bank, target, bank, bank; spent/accepted busts have the low cue. Reveal and invalid pending choices are silent. No recording has full-scale PCM samples. | [audio](audio/), [measurements](verification.json) |
| Random source | The maintained source rolls and banks three, clears the next round and exits. The independently reopened source rolls and banks one. These are observations, not random-generator qualification. | [ordinary bank](captures/random-bank.png), [reopened bank](captures/reopened-bank.png) |
| Native storage | The exported filesystem validates before cold boot; the independent editor loads the 10,970-byte native program, checks/runs it, rolls, banks, continues and exits. All 78 original files remain unchanged. | [listing](captures/arcade-reopened-listing.png), [next](captures/reopened-next.png), [verification](verification.json) |

[verification.json](verification.json) records 146 required captures, 33
identical-picture pairs, 14 PCM recordings and a 63-frame native MP4 at 50 fps.
The early preview differences occupy pixels 1148,158 through 1391,279 in the
1536×576 native captures: only the moving die. They no longer include the header.
The clip lasts about 1.28 seconds including the settled hold; that is not the
roll duration. The actual roll has settled by the sampled frame 22 after the
three-frame press. Timing observations qualify these named windows and this
configuration, not every possible host/input arrival time.

## Rejected observations

The first batched screen review found palette entry 3 cycling through dark
colours: the title and pending-rescue text lost contrast, and motion comparisons
changed outside the die. Hiding the cursor and setting Palette do not cancel
AMOS’s preset flash. The [original manual](https://amospromanual.dev/06-03-screen-effects.html#flash-off)
identifies entry 3’s default flashing and the Flash Off control. All three new
sources now stop flashing before setting their palette. The [rejected evidence](rejected/)
retains the original sources, identities and affected unedited captures. Earlier
maintained stages are unchanged. This correction is included in the single
confirmation batch, rather than accepted as decorative animation.

The first motion script attempted to start video immediately after snapshot
restore and failed with “cannot start video recording before the first frame is
emitted”. The corrected script runs one idle frame before recording. This is
a script precondition failure, not an established emulator defect.

## Reproduction

Use the pinned emulator and Build198x builds with existing locked dependencies.
Run `prepare.py --disk-tool TOOL --amos AMOS --samples SAMPLES --run-root RUN`
with the identified lawful inputs and an empty output directory. SAMPLES is the
bank-or-risk folder containing prototype and stages. Populated output is refused.
Run `replay.py PHASE.json --emulator EMULATOR --kickstart ROM --amos AMOS
--run-root RUN` in [sequence.json](sequence.json) order. Each subprocess is
bounded to 50 seconds. After the export request, require
`TOOL verify RUN/arcade-settled.save.adf` before the independent cold boot.
A closed Save requester alone does not establish a completed filesystem write.

Run `verify.py RUN --disk-tool TOOL --samples SAMPLES`. Inspect the native
frames for syntax, text, values, pip meanings and spacing; hashes alone do not
interpret them. [media-checks.json](media-checks.json) records byte-identical independent
reconstruction of all three disks and ten rejected controls: changed source,
populated output, low contrast, missing capture, wrong pending picture, silent
bank cue, valid disk without the saved program, invalid video, corrupt PNG and
uncontrolled palette animation. A final green run follows those controls.
[artifact-hashes.json](artifact-hashes.json) binds the retained raw artefacts
and normalised reports. ROMs, runtime media, ADFs, snapshots and tokenised native
programs are excluded from Git. Raw captures, PCM, a native motion clip and
normalised reports retain the observable evidence. Original inputs remain
unchanged.

Explicit listening preference, acceptance of this presentation, authored
replacement lessons and an uncoached beginner trial remain pending. The user
has supplied positive play feedback for the preceding rescue version. That
feedback does not establish educational effectiveness.
