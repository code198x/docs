# Bank or risk: native palette check

**Explicit white text on black passes the inspected native display checks.**
This addresses [samples #105](https://github.com/code198x/code-samples/issues/105)
without changing the accepted limit 10, five rounds, target 30 or fresh-key input.
The maintained source change is exactly `Palette $000,$FFF` after `Curs Off`.
`Paper 0` selects black; `Pen 1` selects white. Previously those entries inherited
the runtime palette, producing dark orange text on black in this configuration.

## Configuration and identities

[inputs.json](inputs.json) pins the source, firmware, original AMOS disk, derived
work disk and tool revisions. This uses AMOS Professional 2.00 through Emu198x
0.34.2 at revision `6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, PAL A1200,
stock 2 MiB chip RAM and no fast RAM. Both tools built offline with locked
existing dependencies. No original media was changed or redistributed.

The [earlier execution audit](../2026-10-amos-bank-or-risk-emu198x/REPORT.md)
retains the pre-palette rules, naming, input and save/reopen evidence. Its source
identities remain unchanged. This pass does not repeat native save/reopen or the
separate random-range and angle-mode investigation.

## Observed screens

These are manual inspections of unedited emulator framebuffers, not OCR or
assertions inferred from a successful script exit. Each named screen displays
white text on black. Outcomes are described in words and numbers without using
colour to distinguish success, banking or loss.

| State | Observation | Capture |
| --- | --- | --- |
| Maintained source title | Rules and SPACE/Q choices are readable. | [Title](captures/base-title.png) |
| Active play | Round 1, total 4, last roll 4, secured 0 and R/B/Q choices. | [Active](captures/perfect-01-R.png) |
| Exact-limit bank | Total 10, secured 10 and automatic-bank explanation. | [Perfect bank](captures/perfect-02-R.png) |
| Chosen bank | Total 4, secured 4 and safe-points explanation. | [Bank](captures/recover-04-B.png) |
| Bust | Total 11, round secured 0, earlier secured 4 retained; loss explained. | [Bust](captures/recover-07-R.png) |
| Early success | Three perfect rounds secure 30 in round 3; replay/quit choices. | [Round 3 result](captures/perfect-08-R.png) |
| Recovery success | Contributions 4, 0, 6, 10, 10 secure 30 in round 5. | [Round 5 result](captures/recover-16-R.png) |

The maintained source and both prescribed-roll copies were imported with Merge
ASCII, syntax-checked with F2 and run with F1. The full action sequences and
intermediate captures are retained. Prescribed rolls qualify these displays;
they do not measure random fairness. The other two generated cases were not
rerun in this palette pass.

## Reproduction

Use lawful local copies matching `inputs.json`. Build `emu198x-amiga` with
`--release --offline --locked --no-default-features`, and `build198x-adf` with
`--release --offline --locked`, at the recorded revisions. Keep the build target
and run directory isolated.

Run `python3 prepare.py --disk-tool TOOL --amos AMOS --samples SAMPLES
--run-root RUN`, where SAMPLES contains the pinned maintained ASCII source and
`prepare-probes.py`. This reuses the earlier audit's OFS payload reader, checks
the original image identity, rebuilds a bootable work disk and verifies all 78
original file contents plus the filesystem. [media-checks.json](media-checks.json)
records the preserved file hashes and derived disk identity. Only our ASCII
source and the two test copies are added. The work disk is writable in emulator
memory from boot; original inputs remain read-only.

Replay each phase with `python3 replay.py PHASE --emulator EMULATOR --kickstart
ROM --amos AMOS --run-root RUN`, in this order:

1. `work-boot-1000.json`, then `work-editor.json`.
2. `base-import.json` for the maintained source title.
3. `perfect-import.json`, then `perfect-play.json`.
4. `recover-import.json`, then `recover-play.json`.

Each import restores the blank editor snapshot, so programs do not accumulate.
The two boot phases are bounded separately; display-active detection alone is
not evidence of editor readiness. Inspect the captures after each phase.
[scripts/](scripts/) contains the exact actions; [reports/](reports/) contains
emulator observations. [capture-hashes.json](capture-hashes.json) binds the
retained PNGs. No snapshots, ROMs, disks or original runtime contents are stored
in the repository.

## Verification and limits

The source matches revision `0c55096` byte for byte after removing the single
inserted palette statement. All four generated probes match the exact supplier,
RESTORE and DATA transformation and their recorded hashes. A second generation
into the populated output directory fails and preserves every existing file.
Ruff lint/format, prose, JSON and relative-link checks pass.

This establishes the named display outcomes in one configuration. It does not
establish beginner understanding, minimum hardware requirements, desktop menu
integration, die artwork, sound or future lesson stages. Those additions need
their own checks. The next bounded presentation step is an explained fixed die,
then connecting its face to the stored roll.
