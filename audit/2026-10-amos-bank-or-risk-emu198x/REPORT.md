# AMOS bank-or-risk native execution

The text-first rules prototype runs in AMOS Professional 2.00 through Emu198x.
The four prescribed-roll cases, held/released input, replay, phase-specific quit,
and a native save followed by an independent cold-boot load were checked.
The source naming faults are corrected in the pinned sample revision recorded
in [inputs.json](inputs.json). Graphics, a readable palette, sounds and learner
understanding remain separate work.

## Configuration and method

Emu198x 0.34.2, revision `6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, was
built with `--release --locked --offline --no-default-features`. Its `a1200`
profile supplies PAL AGA, stock 2 MiB chip RAM and no fast RAM. Firmware and AMOS
media identities are in [inputs.json](inputs.json). This is not the earlier
FS-UAE A1200 configuration with 8 MiB fast RAM or its official-repository AMOS
installation; no byte equivalence between those installations is claimed.

The original keyboard, file requester, tokeniser and interpreter ran on the
emulated machine. Native steps use key/chord events and mouse input where
recorded. Snapshots divide long runs into bounded phases; they do not inject
source, set scores or substitute host calculations for the program. A non-black
frame or `boot.detected` alone was not accepted as AMOS readiness: the editor
capture was inspected after 2,000 boot frames.

[Scripts](scripts/) and [runner reports](reports/) record transport and frame
progress. [Observations](observations.json) record manually inspected output;
script exit status alone does not assert that an expected game result appeared.
Captures are unedited native framebuffers, not final learner-facing media.

## Source defect and correction

The initial full listing reported `Syntax error` at `Gosub READ_FRESH`.
The [reduced case](probes/bad.asc) reproduces the split into `Read _FRESH`.
Partial renaming exposed further command-prefix collisions, so full-listing
retries stopped and the [isolated naming probe](probes/names.asc) was run.
It printed the expected values 5, 4 and 3, plus both subroutine markers.

The corrected source gives game identifiers a `BR_` prefix. Removing those
prefixes reproduces [the original source](probes/original.amos) exactly; the
input and scoring logic did not change. The fixture generator's anchors follow
the new names. This is an AMOS naming-rule violation in our source, not an
established emulator defect. The original manual's
[Naming variables](https://amospromanual.dev/05-01-the-bare-bones.html) and
[control structures](https://amospromanual.dev/05-04-control-structures.html)
explain naming and subroutine destinations.

## Observed results

| Check | Native observation |
| --- | --- |
| Perfect success | Three rounds of 4 then 6 secure 10, 20 and 30; success holds in round 3. |
| Preserve and recover | Contributions 4, 0, 6, 10, 10 reach 30 on round 5. Bust 11 awards zero and preserves the earlier 4. |
| Range and limit | Rolls 1, 6, 2, 1 show totals 1, 7, 9 and 10. Equality banks once. |
| Unreachable target | Three busts at 12 secure zero; failure holds in round 3. |
| Invalid/empty input | B and X at zero leave the total and secured score unchanged. |
| Held input and replay | Held R supplies one roll in the tested windows; held B awards once; held Space starts a round at zero; held A resets the challenge and the next prescribed roll is 4. |
| Quit | Q then Return reaches the editor from title, active play, between rounds and the final result. |
| Ordinary random source | Starts at zero, accepts a roll (observed 6), banks after a fresh choice and exits. This is not a randomness study. |
| Persistence | Save As produces a 3,728-byte native `bank.amos`. The exported disk verifies, a new cold boot loads that saved file, and the reloaded program rolls and banks 6 before returning to the editor. |

Representative captures: [perfect result](captures/perfect-08-R.png),
[bust preserving earlier points](captures/recover-07-R.png),
[round-five recovery](captures/recover-16-R.png),
[early failure](captures/fail-08-R.png), and
[play after cold-boot reopening](captures/reopened-bank.png).
The [observation record](observations.json) links the remaining checkpoints.
Held-key observations cover the recorded 60/90-frame windows on this setup,
not every possible timing, keyboard or emulator configuration.

## Media and persistence

The first Save attempt reported `Volume AMOSPro_System is write protected`.
Separately, the original AMOS disk failed Build198x verification:

```text
build198x-adf: corrupt ADF: filesystem structure
```

Its [manifest](amos-media-manifest.json) identifies a free bitmap bit for
non-existent block 1768. The newly mastered program disk passed. No emulator
bug was inferred from this combination of an archive-safe mount and a media
validation failure.

For the persistence check, a fresh OFS work disk was mastered with all 78
original file contents preserved byte-for-byte, plus `bank.asc`. It was mounted
writable in emulator memory from boot. Native Save As created `bank.amos`;
`save_disk` exported to a new sidecar path. The export passed filesystem
verification and contained that native program. A separate cold boot from the
export loaded the saved file with **Load**, not Merge ASCII or restoration of
the edited session. [Media checks](media-checks.json) retain both failures and
successful verification. The filesystem rebuild and mount policy were changed
together, so this pass does not attribute the earlier Save failure specifically
to the bitmap padding.

Neither the original ROM nor the original system disk was modified. Licensed
media, extracted runtime files and snapshots are excluded from this repository.
Hashes, filesystem manifests and source-only scripts permit a lawful rerun.
No emulator code change or confirmed emulator bug resulted from this pass.

## Reproduce

Supply the named emulator and `build198x-adf` binaries, matching lawful firmware
and system media, and the sample directory at the revision in inputs.json.
`prepare.py --help` and `replay.py --help` list the required arguments.
`prepare.py` needs an empty run directory; it reproduces the retained work-disk
and fixture-disk hashes and checks every original file's content.

Replay a phase filename from `scripts/` with `replay.py`, using the same run
root throughout. For the gameplay cases, run `boot.json`, `boot-2000.json`,
`editor.json`, `merge-request.json`, then each `*-import.json` and corresponding
`*-play.json`. `replay-held.json` and `quit-phases.json` consume those checkpoints.
The naming controls use `label-bad.json` and `names.json`.

For persistence, run `work-boot-1000.json`, `work-editor.json`,
`work-save-request.json`, `work-save.json`, `native-export-requests.json`,
`reopen-1000.json`, `reopen-editor.json`, and `reopen-load.json`.
The runner materialises `${RUN}` and `${AMOS}` paths and fails on process or
MCP tool errors. Inspect captures against the observation record; there is no
host-side mock standing in for AMOS. Do not keep rolling a finite prescribed
case after its named endpoint: its DATA would be exhausted.

Preparation was rerun independently and reproduced both retained disk hashes.
The replay wrapper was exercised against the naming probe. Ruff lint/format,
fixture transformations and hashes, nonempty-output refusal, JSON parsing,
relative links, prose and diff checks pass.

## What this establishes

Emu198x provides an effective native execution path for this rules prototype.
The accepted 10/5/30 design now has original-runtime correctness evidence in
addition to browser play feedback. The game is still an opening prototype:
palette/readability, original die graphics, event sounds and teaching stages
need their own checks before publication. No uncoached beginner trial or AMOS
play approval by the user is claimed. The separate random-range and angle-mode
reference investigation is not completed by these game checks.
