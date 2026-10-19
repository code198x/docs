# Bank or risk: short result sounds

This pass adds an explained fading tone and separate bank, bust and success
checkpoints to the AMOS opening. The sound additions preserve the accepted
10/5/30 rules, board, die and fresh-key input. Native PCM recordings measure
whether cues occur, their relative pitch/volume/duration, silence and clipping.
Those measurements do not establish pleasantness or human listening acceptance.
The clips are retained for that review; beginner effectiveness remains untested.

## Sources and event design

[inputs.json](inputs.json) pins source, stages, firmware/media and tool revisions.
The configuration is AMOS Professional 2.00 through Emu198x 0.34.2 at
`6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, PAL A1200, stock 2 MiB chip RAM,
no fast RAM and the recorded Kickstart 3.1 image. Tools built offline with their
existing locked dependencies. No language/runtime dependency was added.

The [original Music chapter](https://amospromanual.dev/08-01-music.html) defines
the native sine wave, envelope phases and Play's instruction delay. The source
uses wave 1 on four channels, overall Volume 24, an envelope rising for one
unit and fading for nine, followed by explicitly silent phases. `Play pitch,0`
starts it without a program delay. No sample bank, custom wave or blocking Wait
is added. Initial setup, replay and quit stop any preceding sound with Play Off.

The result call is after the once-only award and session decision, outside the
redraw/input routines. Positive awards use pitch 49, busts use 25 and success
uses 61. The success branch replaces the last bank cue. Unreachable-target
failure uses its final bust cue, with no extra failure sound. A new Play uses
the same channels; replay and quit stop the tail instead of waiting for it.

`short-tone.amos` teaches the sound parameters. `bank-cue.amos` adds only a bank
cue; `bust-cue.amos` adds the lower bust; `success-cue.amos` is identical to this
revision's maintained endpoint. Their complete sources share the existing game
body and differ only in the result-sound routine. The stage README explains
exact edits and their prerequisites. Removing only setup, stop commands, the
single event call and appended routine reproduces revision `231ba666` exactly.

## Recorded checks

Every import has a separate listing checkpoint before F2/F1, avoiding the early
import/run timing fault found in the board pass. Inspect both the listing and
No errors capture; the script exit code alone establishes neither. WAV windows
use explicit start/stop recording actions, so startup silence is not mistaken
for a cue. Screenshots are unedited native framebuffers.

| Check | Required observation | Evidence |
| --- | --- | --- |
| Default tone | One short fading burst, both stereo channels, no clipping. | [WAV](audio/tone.wav), [screen](captures/tone-title.png) |
| Lower supplied pitch | Pitch 37 measures about half the frequency of 49; fade stays short. | [WAV](audio/lower.wav) |
| Lower volume | Volume 12 is lower amplitude than 24, with the same pitch and fade. | [WAV](audio/quieter.wav) |
| Longer fade | Phase-1 duration 18 extends the fade compared with 9, without changing pitch. | [WAV](audio/longer.wav) |
| Bank-only stage | Three perfect rounds give three medium-pitch bank cues. | [WAV](audio/bank-test.wav) |
| Bust stage | Recovery gives bank, bust, bank, bank, bank; success is not added yet. | [WAV](audio/bust-test.wav) |
| Final perfect run | Two bank cues and one higher success cue; secured 30 in round 3. | [WAV](audio/perfect.wav), [result](captures/perfect-08-R.png) |
| Final recovery | Bank, bust, bank, bank, success; secured 30 on round 5. Zero award does not erase earlier points. | [WAV](audio/recover.wav), [bust](captures/recover-07-R.png), [result](captures/recover-16-R.png) |
| Early failure | Three low bust cues, secured 0, total 12 and target unreachable after round 3. | [WAV](audio/fail.wav), [result](captures/fail-08-R.png) |
| Held/wait/invalid controls | One bank cue while B is held for 90 frames, then quiet while waiting and holding invalid X. Held SPACE opens one new round; held R rolls once without a result cue. | [WAV](audio/held-controls.wav), [round](captures/held-Space.png), [roll](captures/held-R.png) |
| Immediate next round | SPACE starts round 2 while the bank cue is still above the measured signal threshold. | [WAV](audio/rapid-next.wav), [screen](captures/rapid-next.png) |
| Replay during success | A starts one fresh challenge and stops the existing success tail. A is held for 90 frames without acting twice. | [WAV](audio/replay-tail.wav), [screen](captures/replay-quiet.png) |
| Quit during success | Q stops the tail and Return completes the editor transition. | [WAV](audio/quit-tail.wav), [editor](captures/quit-quiet.png) |
| Muted challenge | Volume 0 gives no detectable cue; all corresponding rendered game states match the audible perfect run byte for byte. | [WAV](audio/muted.wav), [result](captures/muted-08-R.png) |
| Startup | The maintained source reaches its title without a cue. | [WAV](audio/base-startup.wav), [title](captures/base-title.png) |

[Audio measurements](audio-measurements.json) records the measured values and
all required cue counts. `measure_audio.py` reads the native 48 kHz stereo
16-bit PCM, chooses the higher-energy channel for pitch/count measurement, and
also records both channel peaks. Five-millisecond RMS windows above the greater
of 8 PCM units or 3% of that clip's peak RMS define activity. Gaps over 50 ms
separate bursts. Pitch is estimated from interpolated zero crossings away from
the envelope edges. These are signal measurements, not perceptual loudness or
an analogue-hardware reference comparison.

`verify_audio.py` fails on missing/empty files, positive cases without their
expected bursts, wrong counts/pitch ratios/durations, clipping and non-silent
negative controls. Native variants test parameter changes instead of inferring
them from command names. The verification's negative controls replace a positive
recording with silence and remove a required recording; both must fail. A third
control substitutes the passive fade for an active stop and must also fail. Visual
outcomes are inspected separately. Native owner listening/play acceptance,
desktop audio-device integration and a learner trial are not established here.

The initial ending-control test sent its key before the fresh-choice handover
had completed. A brief Q left the result visible; holding A eventually replayed
without demonstrating that Play Off cut the current tail. The silent baseline
at revision `231ba666`, with only prescribed rolls substituted, ignores the
same early Q window and produces the identical result image. This is existing
fresh-key behaviour, not a demonstrated sound regression or emulator defect.
Those initial recordings/actions are retained in [diagnostics/](diagnostics/).

The passing tests restore the same success state, allow three more native frames
for the choice to become ready, then compare no key against A/Q. The passive
tail lasts about 85 ms; replay and quit reduce it to about 25 ms. The check
requires shortening relative to that passive control, rather than an arbitrary
absolute cutoff. These results cover the named input windows, not every possible
arrival time during drawing. No input-handling code was changed.

## Reproduction

Build `emu198x-amiga` with `--release --offline --locked --no-default-features`
and `build198x-adf` with `--release --offline --locked` at the recorded revisions.
Use matching lawful local firmware/AMOS inputs and isolated build/run folders.

Run `python3 prepare.py --disk-tool TOOL --amos AMOS --samples SAMPLES
--run-root RUN`. SAMPLES is the pinned `prototype/` folder beside `stages/`.
The verified boot disk contains all 78 original runtime file contents and no
curriculum source. The data disk contains our source, stages and prescribed
probes. The boot disk is byte-identical before/after game integration. The
initial pilot's earlier data-disk hash is recorded; its tone was rerun with the
final data disk. [media-checks.json](media-checks.json) records preserved file
hashes and both final disk identities. Original media was not changed or shared.

Use `python3 replay.py PHASE --emulator EMULATOR --kickstart ROM --amos AMOS
--run-root RUN`. First replay `work-boot-1000.json` and `work-editor.json`.
Then each of `tone`, `lower`, `quieter`, `longer`, `base`, `perfect`, `recover`,
`fail`, `muted`, `bank-test` and `bust-test` has an `-import.json` phase, followed
by `-run.json`. Inspect `-imported.png` before continuing to run. For game cases
other than base, follow with `-play.json`.

After perfect/recover play, run `held-controls.json`, `rapid-next.json`,
`success-ready.json`, `replay-tail.json` and `quit-tail.json`. Those restore retained intermediate
states; they do not depend on transport success being interpreted as gameplay.
`tone-timing.json` captures the continuation message while its tone is active.
For the silent comparison, `baseline-import.json`, `baseline-run.json` and
`baseline-play.json` use the retained prescribed old source on `baseline.adf`.

Run `python3 verify_audio.py RUN` for the PCM assertions and compare every
perfect/muted action PNG by its suffix. All nine matching states must agree.

[scripts/](scripts/) retains exact actions; [reports/](reports/) retains emulator
observations with the local run root replaced by `${RUN}`. [artifact-hashes.json](artifact-hashes.json) binds PNGs and WAVs.
No licensed runtime contents, ROMs, disks or snapshots are committed. Each
emulator subprocess has a 50-second timeout and boot is split into bounded
phases. The optional [MP3 preview](audio/cue-preview.mp3) is derived from three native
WAV excerpts in bank, bust, success order: 0.45 seconds each from perfect at
1.775 s, recovery at 7.985 s and perfect at 5.970 s, encoded using the existing
ffmpeg tool at 96 kbit/s. It is for listening, not measurement.

The [rules/input/persistence](../2026-10-amos-bank-or-risk-emu198x/REPORT.md),
[palette](../2026-10-amos-bank-or-risk-palette/REPORT.md),
[die](../2026-10-amos-bank-or-risk-die/REPORT.md) and
[board](../2026-10-amos-bank-or-risk-board/REPORT.md) records keep their original
pins. Save/reopen was not repeated for the sound revision. Remaining teaching
checkpoints and full-route learner evidence still need their own work.
