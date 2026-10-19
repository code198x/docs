# Bank or risk: fixed die and stored faces

This record checks two drawing fragments and the game integration in original
AMOS Professional 2.00 through Emu198x. The accepted limit 10, five rounds,
target 30 and fresh-key handling stay unchanged. Sound and the fuller labelled
board progression remain separate work; these are not replacement lessons.

## Sources and configuration

[inputs.json](inputs.json) pins the source, both stage files, firmware, original
AMOS system disk, derived disks and tool revisions. The configuration remains
Emu198x 0.34.2 at `6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, PAL A1200,
stock 2 MiB chip RAM, no fast RAM and the recorded Kickstart 3.1 image. Tools
built offline with their existing locked dependencies. No dependencies were added.

The original manual's [Graphics chapter](https://amospromanual.dev/06-04-graphics.html)
defines `Ink`, `Box`, `Bar` and pixel coordinates. Its
[Keyboard chapter](https://amospromanual.dev/10-01-using-the-keyboard.html)
defines `Wait Key`. The stage README explains each drawing statement, separates
pixels from text coordinates, gives exact supplied-value edits and includes
prediction and repair exercises. Native authoring checks do not establish that
beginners can follow those explanations without help.

`fixed-die.amos` draws an outline and central square pip, with no variable,
decision or loop. `match-die.amos` adds a supplied face and six explicit decision
blocks, without arrays or a hidden renderer. The full game visits `BR_DRAW_DIE`
after printing the last roll. The routine reads that stored value; it never
chooses a roll, updates a score or accepts input. Zero draws an empty outline.
The game routine and supplied-face drawing block agree byte for byte after
substituting the input name and adding Return. Removing the drawing call and
appended routine reproduces the previous game source exactly.

## Native observations

Captures are unedited emulator framebuffers, inspected manually. Script completion
and syntax checking alone do not establish that the displayed picture is right.
The numeric result remains alongside the picture; white pips and outline use the
explicit white/black palette. Raw framebuffers retain the emulator's pixel shape.

| Check | Expected visible result | Evidence |
| --- | --- | --- |
| Fixed picture | One central pip; the picture remains until a key. | [Fixed die](captures/fixed-title.png), [syntax](captures/fixed-syntax.png) |
| Finish a fragment | Space, then Return, reaches the editor after its transition. | [Editor](captures/fixed-exit.png) |
| Supplied 1–6 | Printed supplied number and matching pip pattern for each source edit. | [1](captures/face1-title.png), [2](captures/face2-title.png), [3](captures/face3-title.png), [4](captures/face4-title.png), [5](captures/face5-title.png), [6](captures/face6-title.png) |
| Game ready | Last roll 0 and an empty outline. | [Ready](captures/faces-00-Space.png) |
| Game faces 1–6 | The prescribed sequence displays the same six patterns beside their numeric rolls. | [1](captures/faces-01-R.png), [2](captures/faces-02-R.png), [3](captures/faces-03-R.png), [4](captures/faces-04-R.png), [5](captures/faces-06-R.png), [6](captures/faces-07-R.png) |
| Clear old pips | Changing 1 to 2 removes the central pip; the labels remain readable. | [Face 2](captures/faces-02-R.png) |
| New round | Following the bust at 11, round 3 starts with roll 0, empty outline and secured 10. | [Round reset](captures/faces-08-Space.png) |
| Chosen bank | Last face 4 remains, with current total 4 and secured 4. | [Bank](captures/recover-04-B.png) |
| Bust | Last face 5 remains, total 11, round secured 0 and earlier secured 4. | [Bust](captures/recover-07-R.png) |
| Early success | Last face 6 and secured 30 in round 3. | [Success](captures/perfect-08-R.png) |
| Fifth-round success | Contributions 4, 0, 6, 10, 10 still secure 30. | [Recovery](captures/recover-16-R.png) |
| Early failure | Three busts at 12 leave score 0 and the target out of reach after round 3. | [Failure](captures/fail-08-R.png) |
| Replay | A held for 90 frames starts one new challenge, with zero scores and an empty die. | [Replay](captures/replay-ready.png) |

All imported stage variants and game copies were syntax-checked with F2 and run
with F1. The six standalone variants differ only in the supplied assignment,
not their decision blocks. The maintained random source was separately imported
and run to its title. Deterministic fixtures cover the named game outcomes; they
do not prove random fairness. The range-and-limit fixture is generated but not
rerun in this pass. Earlier [rules/input and persistence](../2026-10-amos-bank-or-risk-emu198x/REPORT.md)
and [palette](../2026-10-amos-bank-or-risk-palette/REPORT.md) audits retain their
original source pins. Native save/reopen has not been repeated for the drawing revision.

## Reproduction and media

Build `emu198x-amiga` with `--release --offline --locked --no-default-features`
and `build198x-adf` with `--release --offline --locked` at the recorded revisions.
Use matching lawful local inputs and an isolated target/run directory.

Run `python3 prepare.py --disk-tool TOOL --amos AMOS --samples SAMPLES
--run-root RUN`. SAMPLES is the pinned `prototype/` folder; its sibling `stages/`
contains both drawing fragments. Preparation checks source identities, generates
five fixed-roll fixtures and uses the earlier audit's qualified OFS reader.
It rebuilds a bootable work disk, preserving all 78 original runtime file
contents, and a separate data disk containing the stage variants and probes.
Both filesystems must pass verification. [media-checks.json](media-checks.json)
records the hashes. An initial attempt to put all inputs on the boot disk failed
with `build198x-adf: disk full: 10 blocks needed, 8 free`; separate data media
keeps every runtime file and follows the earlier audit's disk-swap route.

Use `python3 replay.py PHASE --emulator EMULATOR --kickstart ROM --amos AMOS
--run-root RUN` for these phases, in order:

1. `work-boot-1000.json`, `work-editor.json`.
2. `fixed-import.json`, `fixed-exit.json`.
3. `face1-import.json` through `face6-import.json`.
4. `base-import.json`.
5. `faces-import.json`, `faces-play.json`.
6. `perfect-import.json`, `perfect-play.json`, `replay.json`.
7. `recover-import.json`, `recover-play.json`.
8. `fail-import.json`, `fail-play.json`.

Each import restores the blank editor snapshot. Fixture imports mount the data
disk for Merge ASCII, then restore the system disk before running. The work disk
is writable only in emulator memory. Each subprocess has a 50-second timeout;
the two boot phases stay separate. Inspect frames rather than relying on the
emulator's display-active boot flag. [scripts/](scripts/) retains exact actions,
[reports/](reports/) retains emulator observations, and
[capture-hashes.json](capture-hashes.json) binds the retained PNGs. No original
runtime contents, ROMs, disks or snapshots are retained in this repository.

## Other checks and remaining work

The five probe transformations and hashes agree with the maintained source.
Generation into a populated output directory fails and preserves every file.
Ruff lint/format, prose, JSON, links, public-path/media exclusions and a repeated
byte-identical media build pass. Original firmware and system disk hashes remain
unchanged.

The two drawing checkpoints are ready for review as authoring material. Other
checkpoints, the board progression, event sounds, native owner play feedback and
an uncoached learner trial remain outstanding. Desktop-window integration and
minimum hardware requirements are not established by these checks.
