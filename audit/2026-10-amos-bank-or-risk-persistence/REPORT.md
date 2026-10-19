# Sound-enabled AMOS game: native save and independent reopen

This pass checks persistence for the maintained bank-or-risk endpoint at
[samples revision 1fa0675](https://github.com/code198x/code-samples/tree/1fa0675b809ef6a40bcf01571b75d6196cce0e0e/commodore-amiga/amos/bank-or-risk/prototype).
The earlier text-only save evidence remains valid for its recorded revision;
this pass covers the later palette, die, board and result sounds together.
No game source, rules or input code changes are part of this pass.

## Method and scope

[inputs.json](inputs.json) pins the source and lawful local firmware/media.
The configuration matches the [sound audit](../2026-10-amos-bank-or-risk-sound/REPORT.md):
AMOS Professional 2.00, Emu198x 0.34.2 at
`6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, PAL A1200, stock 2 MiB chip RAM
and no fast RAM. Build198x at `f7016398deb1fff9dc1efb6713dfab8c7bacf2d0`
masters and verifies the OFS media. Both tools build offline with locked existing
dependencies. No new runtime or dependency is added.

The qualified sound-audit media helper creates a verified boot filesystem with
all 78 original runtime file contents preserved and no curriculum source.
Our ASCII sources occupy a separate data disk. The maintained source is
imported through Merge ASCII, inspected and checked with F2. The boot disk is
then mounted writable in memory, and native Save As creates `base.amos`.
The MCP `save_disk` tool exports the modified disk to a new sidecar path.
The original loaded files remain unchanged.

A second, independent process cold boots from that export. It has no imported
listing or running game snapshot. Native **Load** opens `DF0:base.amos`;
Merge ASCII is not used in the reopened route. Intermediate snapshots split
bounded commands after this new boot; they do not replace loading the saved
program. The exported boot disk contains the runtime and saved tokenised
program, with no ASCII source from which to reconstruct it.

The same route separately saves and reloads `perfect.amos`, the current
prescribed-roll copy. Its only source changes replace the die supplier with
Read, restore DATA for each challenge and append the recorded values. The nine
scripted game observations and recording windows are identical before and after
saving. This separates a repeatable persistence comparison from the maintained
source's random roll.

## Evidence

The scripts retain import, syntax check, Save As, sidecar export, cold boot,
Load and gameplay as distinct phases. Screenshots are unedited native
framebuffers. Inspect the listing, No errors banner, saved filename and reopened
behaviour; a successful tool response alone does not prove those outcomes.

The verifier reads each exported OFS filesystem, requires the named native
program with its AMOS header, and rechecks all 78 original file hashes. It
requires exactly nine matching game images and positive audio recordings with
the expected bank/bank/success pitch sequence. The maintained source's reopened
bank recording must contain one bank cue. PCM checks cover pitch, short duration
and absence of full-scale clipping; they do not establish listening acceptance.

## Observed results

Both exported disks pass filesystem validation and preserve all 78 runtime file
contents. The maintained program is 5,892 bytes; the prescribed-roll program is
5,932 bytes. Both have native AMOS headers; neither exported disk contains an
ASCII source. [verification.json](verification.json) records disk/program hashes
and the measured results.

| Check | Observed outcome | Evidence |
| --- | --- | --- |
| Maintained source | Save As names `base.amos`; the cold-boot Load listing contains sound setup and passes F2. | [saved](captures/base-saved.png), [loaded](captures/base-reopened-listing.png), [syntax](captures/base-reopened-syntax.png) |
| Random play after Load | One roll shows four pips and total 4; B secures 4 with one short bank cue; Q then Return reaches the editor. | [bank](captures/base-reopened-bank.png), [WAV](audio/base-reopened-bank.wav), [editor](captures/base-reopened-editor.png) |
| Prescribed play after Load | Three perfect rounds reach 30 in round 3, leaving two unused rounds. All nine corresponding game PNGs are byte-identical before/after saving. | [result](captures/perfect-reopened-08-R.png), [comparison](verification.json) |
| Sound survives saving | Both prescribed runs record bank, bank, success: about 525, 525 and 1,051 Hz, each 185 ms. The maintained bank is also about 525 Hz and 185 ms. No recording has full-scale clipped samples. | [before](audio/perfect.wav), [after](audio/perfect-reopened.wav), [measurements](verification.json) |
| Reopened replay and exit | A held for 90 frames starts one fresh challenge; Q then Return reaches the editor. | [replay](captures/perfect-reopened-replay.png), [editor](captures/perfect-reopened-editor.png) |

The two prescribed recordings are not byte-identical PCM: the sampling phase
and peaks differ slightly. Their cue counts, timing, pitch and duration agree;
the verifier also compares pitch, duration and peak level within stated bounds.
The image comparison is exact. Neither comparison is a human listening test.

The first replay/quit script sent Return immediately after Q, before the native
End prompt was ready. Its capture shows that prompt rather than the editor;
[diagnostics/](diagnostics/) preserves the rejected actions and capture. The
passing script allows 30 frames after Q before Return, as the maintained-source
check already did. This corrects the test sequence; the game source is unchanged.

Negative controls reject a mismatched source, a missing export, a valid boot
filesystem without the saved program and silence substituted for the reopened
positive recording. The original inputs and prepared work/data disks still
match their pinned hashes after execution. No emulator defect was established.

## Reproduction

Build the pinned tools as described in the sound audit. Run its `prepare.py`
with an empty run folder, the pinned source folder, matching lawful AMOS media
and Build198x executable. This pass reuses the helper without changing the old
audit. The boot/data disk hashes must match [inputs.json](inputs.json).

Run this directory's `replay.py PHASE.json --emulator EMULATOR --kickstart ROM
--amos AMOS --run-root RUN` for the retained phases in this order:

1. `work-boot-1000`, `work-editor`.
2. `base-import`, `base-save-request`, `base-save`, `base-export-requests`.
3. `base-cold-boot`, `base-cold-editor`, `base-load`, `base-reopened-run`,
   `base-reopened-play`.
4. `perfect-import`, `perfect-run`, `perfect-play`, `perfect-save-request`,
   `perfect-save`, `perfect-export-requests`.
5. `perfect-cold-boot`, `perfect-cold-editor`, `perfect-load`,
   `perfect-reopened-run`, `perfect-reopened-play`, `perfect-reopened-replay-quit`.

Inspect each import/load listing before continuing. Run `python3 -B verify.py
RUN --disk-tool TOOL --source SOURCE` for the filesystem, source identity,
image comparison and PCM checks. Each emulator subprocess has a 50-second
limit. The original helper refuses a populated run directory. Missing media,
missing program, wrong source or absent/incorrect recordings must fail.

[reports/](reports/) retains native observations with the local run root
normalised to `${RUN}`. [artifact-hashes.json](artifact-hashes.json) binds
screenshots and audio. Licensed runtime files, ROMs, ADFs, tokenised programs
and snapshots are excluded. Hashes and source-only scripts permit a lawful rerun.

Human listening/play acceptance and an uncoached learner trial remain pending.
This is execution evidence for the named endpoint and configuration, not
qualification of every earlier teaching checkpoint or a minimum hardware claim.
