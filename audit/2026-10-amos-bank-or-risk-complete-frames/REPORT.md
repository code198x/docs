# Complete pictures and clearer lettering

The user accepted the brighter arcade direction but reported brief flicker and
partial redraws. Three further complete stages address the display defect,
introduce ROM graphical text, then give the title and scores their own bitmap
lettering. The current endpoint is [styled-board.amos](https://github.com/code198x/code-samples/blob/1b0a7a5ed28344ba4829e351654734e8ef7d447e/commodore-amiga/amos/bank-or-risk/stages/arcade/styled-board.amos). The earlier
sources remain available as explained intermediate stages. No public lessons
change, and the new presentation still needs the user's review.

## Reproduction and cause

The preceding [native roll clip](../2026-10-amos-bank-or-risk-arcade/video/roll.mp4)
reproduces the reported partial board in frames 23–24. Cls and the following
shapes/text modify the visible image while the display scans it. Frame 23
contains coloured blocks and missing fields. The previous sparse preview samples
and settled-picture comparisons missed those intermediate frames. The
[rejected record](rejected/original.json) pins the original clip and keeps raw
extracted frames. This is a game drawing defect; the observed output does not
establish an Emu198x bug.

`stable-display` uses Double Buffer, Autoback 0 and Bob Update Off to draw into
the hidden logical image. BR_PRESENT swaps, waits for vertical blank, then copies
the physical image back to the logical image. Partial edits therefore begin from
the same complete board. BR_READ_FRESH presents after the caller has supplied its
controls; each preview presents only after its whole die is drawn. The rest of
the fresh-key reader, rule decisions and sounds are unchanged. The
[guide](https://github.com/code198x/code-samples/tree/amos-bank-or-risk-prototype/commodore-amiga/amos/bank-or-risk/stages/arcade/complete-display.md)
explains the extra bitmap's memory cost and why simply enabling two buffers is
insufficient. The original manual's screen and updating chapters establish those
AMOS facilities.

## Typography and its teaching boundary

The user selected ROM text with distinctive title/score lettering. The native
ROM probe reports topaz.font, height 8, Rom; Text Base is 6 and Text Length for
Bank or Risk is 96. `rom-text` replaces Locate/Print output with baseline-aware
pixel positions, string construction and a small graphical Text routine.
Set Font affects Text, not Print. The selected index is verified for this pinned
ROM rather than asserted for every possible configuration.

`styled-board` adds 18 authored five-by-seven glyphs for digits and the letters
in BANK OR RISK. The ready title and main scores use scale 2; the board title
uses scale 1. Ordinary instructions, Best, goal, limit, progress and awards stay
in the ROM face. Glyph arrays and loops affect only drawing. The
[typography guide](https://github.com/code198x/code-samples/tree/amos-bank-or-risk-prototype/commodore-amiga/amos/bank-or-risk/stages/arcade/typography.md)
explains every representation and coordinate formula, palette/background roles,
string conversions and repairs. No external font or new dependency is added.
This is source authoring evidence, not authored replacement lessons or learner
understanding.

The first scale-1 glyph attempt stopped at a one-point Bar with “Illegal
function call”. The corrected routine uses Plot at scale 1 and Bar for larger
cells. The failed source and native error picture are retained. A source check
alone did not establish execution. The verifier now rejects a native error
palette where it expects a game picture.

Graphical text and interpreted glyph drawing have a cost. The earlier 40-frame
script gaps did not qualify this renderer: a nominal fifth-result capture still
showed three completed rounds. The repeated cases use explicit 90-frame settled
waits and require the actual five-round/record/replay outcomes. Those windows
qualify the recorded configuration, not every possible key-arrival time. This
pass does not claim an optimised font renderer or a universal response-time bound.

## Native outcomes

The configuration remains AMOS Professional 2.00, pinned Emu198x 0.34.2 at
`6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, PAL A1200, stock 2 MiB chip RAM,
no fast RAM. Build198x is `f7016398deb1fff9dc1efb6713dfab8c7bacf2d0`.
[inputs.json](inputs.json) pins lawful media and source identities. This is not
a minimum-machine claim. Existing locked tools build offline; no tool code changes.

- The buffered stage's fourteen settled views exactly match the preceding
  arcade stage, including five awards, Best and replay.
- The styled perfect run reaches secured 30 at completed 3, continues through
  five, records Best 50 and shows five tens. Replay clears secured points,
  completion, awards and rescue while retaining Best 50.
- Motion and static settled pictures agree. Pending rescue remains stable under
  invalid choices; U restores six and spends rescue; B accepts zero and keeps it.
  A later spent-token bust displays total 12, awards zero and retains secured six.
- The ROM-only intermediate rolls and banks. The maintained styled source is
  exercised separately from the fixed suppliers. Q stops the program during the
  reveal, at title/active/pending prompts, between rounds and after five rounds.
- Audio checks require one result cue per completed-round phase. The third
  perfect round uses the high target cue; later rounds return to the bank cue.
  The reveal and invalid pending choices are silent. Full-scale PCM samples are
  rejected. Rule and sound routines remain tied to the accepted source.

These outcomes are checked through native captures, source contracts, stable
pairs, PCM and continuous video. The failed script runs are not counted as game
completion. [verification.json](verification.json) records 137 required captures, 20 PCM
recordings, fourteen unchanged buffered pictures and twelve styled/static pairs.
The component status explicitly preserves the blocked native persistence check.

## Every recorded transition frame

[check_frames.py](check_frames.py) reads every decoded frame. The native screen
is sampled at logical pixel centres and near-lossless MP4 colours are mapped
back to the known palette. Outside the moving die and control line, every cell
must match either the complete before board or the complete after board. No
mismatched cells are allowed. The check also requires that the recording really
reaches the changed settled result; a clip containing only the old state fails.

The original clip fails at frame 23 with 17,495 cells differing from the before
state and 17,522 from the after state. The buffered recording passes all 61 frames, including 30 settled frames.
The styled recording passes all 181 frames, including 140 settled frames.
Both have zero mismatched cells. [continuous-checks.json](continuous-checks.json)
retains every frame result. This checks the reported board defect, not
every possible pip animation, display mode or host timing. Direct inspection
also checks the pip meanings, labels and spacing. The unchanged contrast pairs
remain in the preceding arcade record; the new type uses those same roles.

## Storage and reproduction

`prepare.py --disk-tool TOOL --amos AMOS --samples SAMPLES --run-root RUN`
requires the pinned sources, explicit controlled copies and an empty output
folder. SAMPLES is bank-or-risk, containing prototype and stages. The qualified
runtime builder preserves all 78 original file contents. Three source/test disks
and an empty data disk are built separately. [variants.json](variants.json)
identifies the exact constant-roll and static transformations plus the ROM probe.

Run `replay.py PHASE.json --emulator EMULATOR --kickstart ROM --amos AMOS
--run-root RUN` in [sequence.json](sequence.json) order. Every emulator subprocess
has a 50-second bound. A 1,000-frame boot exceeded that bound on this run, so
boot progress is retained in separate 500-frame phases. The longer ASCII import
also has a separate bounded completion phase before syntax/run commands.
Neither a timeout nor queued F2/F1 presses establishes a source failure.

The first native Save ran out of space on AMOSPro_System. Its requester says
“Volume AMOSPro_System is full”; extra waiting cannot fix that. The larger
program uses the empty data disk instead. The first data-disk export validated
but was empty: the captured requester still held the entered filename. The
smaller confirmation check requires the native program in the manifest before
another cold boot. Filesystem validity alone cannot prove a program was saved.
The retained exports/requester pictures are identified as failed and do not
count as storage evidence. The explicit confirmation then produces an export rejected
with `build198x-adf: corrupt ADF: block pointer out of range`. Its native requester
still names AMOSPro_System and reports it full after the blank data-disk swap.
The cause remains unconfirmed; [Emu198x #1877](https://github.com/emu198x/emu198x/issues/1877)
tracks the bounded reproduction. Save experiments stopped after the smaller
check failed. No successful native save/reopen is claimed for this endpoint.

Rebuild into another empty directory and compare all five generated disks.
The default `verify.py RUN --disk-tool TOOL --samples SAMPLES --rebuilt REBUILT`
remains red at native storage. The separate verify_game function records the
passed game checks; verify_storage rejects the invalid export. Neither check
is disabled. The component result explicitly says game_verified_storage_blocked
and native_storage_verified is false.
Decode each native MP4 with ffmpeg and run `check_frames.py FRAMES BEFORE AFTER`;
keep decoded diagnostic frames outside Git. [media-checks.json](media-checks.json)
records reconstruction, original-file preservation and failure controls.
[artifact-hashes.json](artifact-hashes.json) binds raw captures/PCM/video and
normalised reports. Original inputs remain unchanged. ROMs, ADFs, snapshots,
native programs and private paths are excluded from Git.

Human acceptance of this new lettering and pacing, explicit listening preference,
authored replacement lessons and an uncoached beginner trial remain pending.
