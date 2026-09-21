# Meteor Storm — lesson implementation

**Status:** The user approved all twenty-four lessons and the overview, using
nineteen complete runnable programs. The module is published and live-verified.
The accepted native game remains the endpoint; its one-hit loss, unlimited boost,
vertical stars, gentle meteor drift and separate time/score records are preserved.
Meet Assembly is already published and leads into this module.

## Teaching progression

The earlier outline grouped systems, not mandatory lesson boundaries. Addressing
and drawing now have separate programs. Records and pool walking, decimal score
and pickups, elapsed time and time formatting, and simulation and rendering each
have separate lessons even where they share a runnable state.

| Lesson | Investigation | Runnable checkpoint |
|---|---|---|
| 1 | Carry a pixel into the next byte | `one-row-shift` |
| 2 | Prepare eight horizontal positions | `eight-shifts` |
| 3 | Find a pixel in Spectrum memory | `pixel-address` |
| 4 | Draw the whole ship | `draw-ship` |
| 5 | Erase before moving | `pixel-motion` |
| 6 | Give the interrupt a small job | `interrupt-clock` |
| 7 | Count frames, choose updates | `half-rate-clock` |
| 8 | Put steering on the frame clock | `clocked-steering` |
| 9 | Let a meteor move independently | `one-meteor` |
| 10 | Distinguish a hit from a near miss | `first-dodge` |
| 11 | Give each object a record | `object-pool` |
| 12 | Walk the pool and reuse a slot | `object-pool` |
| 13 | Make a storm with an end | `fixed-course` |
| 14 | Give meteors a gentle drift | `drift` |
| 15 | Collect something worth the risk | `stars` |
| 16 | Turn a score into readable digits | `stars` |
| 17 | Measure time without counting distance | `timed-course` |
| 18 | Show seconds and hundredths | `timed-course` |
| 19 | Hold Space to boost | `boost` |
| 20 | Draw once, check twice | `render-budget` |
| 21 | Keep the best time and score | `records` |
| 22 | Give the game clear phases | `finished` |
| 23 | Make the instructions fit | `finished` |
| 24 | Keep and share the game | `finished` |

## Browser implementation

Each lesson includes maintained assembly through `MeteorExperiment` and selected
source through `AssemblyExcerpt` / `CodeFromFile`. Companion artwork is editable
and downloadable; source and companion edits become effective together on assembly.
Only explicitly supplied companion files can be included. Revert restores both.
The browser runs Asm198x and the published Spectrum emulator package 0.4.0.
The separate native route supports Asm198x 0.0.58 and upstream Pasmo 0.5.5.

The first exercises magnify actual bitmap bytes. Later experiments expose named
bytes, words and the active object records directly from RAM. The first contact
lesson uses bounded real-CPU break, step and resume controls. Its registers show
the paused CPU; the picture can show the last rendered frame. Downloaded tape
uses the edited source and artwork. No fabricated animation stands in for code
execution, and no checkpoint needs to load from tape before a browser experiment.

The module sits after Meet Assembly in the published assembly catalogue. Existing
legacy lesson routes are preserved. The lesson markers wrap on narrow screens,
so lesson count no longer determines whether navigation fits.

## Verification

Native checkpoint and endpoint evidence is owned by [checkpoints.md](checkpoints.md).
The additional address and static-ship programs pass twenty checks, including
independent Asm198x/Pasmo binary parity. Browser scripts and curated evidence live
in `website/scripts/verification/` and `evidence/meteor-storm/` respectively:

- `meteor-storm.mjs`: all twenty-four programs, maintained source/artwork identity,
  real memory, source and companion edits/revert, missing-include feedback,
  collision break/step/resume, loss/retry/title and source/tape downloads.
- `meteor-storm-flight.mjs`: keyboard-driven browser completion, with read-only
  state observations selecting steering. No game state is written. The tested
  run takes 1047 PAL frames (20.94 seconds), scores 960 points, and records both
  results. All 640 score-line pixels match actual ROM glyphs, bitmap RAM and canvas.
- `meteor-storm-tape.py`: checksums and payload parity with native assembly, then
  a fresh 48K ROM tape load, launch, first-hit loss, retry and title return.

The production build and its required checks pass, including 72 unit tests (9
skipped). Representative lessons 1, 5, 10, 12, 22 and 24 pass main-region axe checks
in both themes and fit 390, 1280 and 1920 pixel viewports. The existing Meet
Assembly regression also passes its border-edit, source/navigation, accessibility
and responsive-layout checks. No browser JavaScript errors were recorded.

Browser completion is configuration-specific execution evidence, not a judgement
of human difficulty. The extra launch frame in that browser input sequence is
not the 1046-frame native benchmark. Browser result screenshots are inspected;
older incomplete batched native screenshots are not illustrations. Their capture
root cause remains undiagnosed. No physical-hardware result is claimed.

## Publication

The user approved the completed module and explicitly authorised publication.
Website [PR #442](https://github.com/code198x/website/pull/442) publishes the
lessons and catalogue; samples are published at `c3995d4`. Required CI checks,
GitHub Pages deployment and the live verification pass. The release retains the
What's New entry as a draft, matching the existing editorial publication state.

Live verification repeats all twenty-four browser programs, source and companion
identity, selected edits, collision stepping, loss/retry/title, downloads,
representative accessibility and responsive-layout checks. A separate keyboard
route verifies the complete winning result and its bitmap/ROM/canvas agreement.
The release record and reports accompany this document in `publication/`.
No unrelated local BASIC, Maths or Craft work is included in the release.
