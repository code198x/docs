# Night Patrol — teaching implementation

The user agreed the [ten-lesson progression](lesson-brief.md) and authorised its
eight teaching checkpoints. The complete sources, precise editing transitions,
prepared-data excerpts and execution evidence are implemented in
`code-samples/sinclair-zx-spectrum/basic/night-patrol/teaching/`.
The user subsequently authorised authoring. The overview and ten website lessons
are approved and published in Hidden worlds. Release and live checks pass.

## Runnable states

| Checkpoint | Native check groups | What is established |
|---|---:|---|
| archive | 3 | Fresh tape and stored tokens; full map/object positions; deliberate STOP |
| movement | 6 | Movement, uppercase and held keys, blocked/ignored input, retry and quit |
| mission | 10 | Empty-handed return, pickup and safe return, frozen result and complete retry |
| patrol | 14 | Autonomous circuit, contact capture and complete mission/recovery |
| scans | 15 | All eight stationary corner-facing changes, circuit wrap and contact rules |
| sight | 14 | Stationary guard and exact opening mask, sight capture, mission and recovery |
| stealth | 16 | Moving masks, corner scans and capture during a stationary look-back |
| finished | 18 | The full approved prototype suite, including cover, both sight-capture paths and fresh-tape start |

All 96 execution groups pass in the recorded stock 48K PAL Emu198x configuration.
Each checkpoint was entered independently in a fresh ROM through keyboard
keywords, saved as an auto-starting tape and loaded in a fresh test process.
These are execution checks, not independent learner comprehension reviews or
original-hardware evidence.

The finished listing is byte-identical to the approved source:
`72d436d316de7f278934846d68bc0c7b2125509c105fc3135a89cbd0ddbd5ae8`.
There are no changes to the accepted gameplay endpoint.

## Editing and prepared data

`checkpoints.json` names exact additions, replacements and deletions. Each
checkpoint supplies its full listing and `changes.bas`. The opening is a new
program; subsequent states reconstruct from those explicit edits. The sight
checkpoint deliberately removes the moving patrol while perception is examined;
stealth restores it with the prepared sight records.

The data folder separates the three-field position table, the opening sight
record and the finished change table. `worked-example.json` decodes the first
movement: five cells change while ten remain visible afterwards. These excerpts
are already included in the complete BASIC programs; the learner does not need
an extra runtime loader or Python installation.

The preparation audit compares supplied excerpts with their checkpoint sources,
reconstructs the masks through three complete circuits and a zero-change record,
and checks the worked example against the geometry. The source/token/TAP audit
also binds each record to the emulator binary and checks tape block checksums.
The teaching README contains reproducible build, check, capture and audit commands.

## Verification limits and media

The checker drives ordinary keys and reads BASIC state without writing it. A
host model searches input routes and checks each transition; it does not inject
positions, inventory or winning states. After CPU debug stepping, the checker
advances against the ROM interrupt counter to avoid the recorded binary's
step/frame clock mismatch.

Ordinary-frame captures were made and inspected for all eight checkpoints. Some
headless PNGs omit white glyphs present in the screen-memory readout. A separate
attribute check on the mission checkpoint verifies the bright white player and
normal white controls on black. Treat these images as diagnostic evidence, not
publication artwork. Public media needs a reliable capture path during website
authoring; the user's native play approval applies to the final game.

## Authored pages and review

The website has a House overview and ten lessons under
`src/content/curriculum/sinclair-zx-spectrum/basic/night-patrol/`, plus the
canonical units catalogue. Numeric game identity 23 is retained. The local
catalogue places the game in Hidden worlds with status complete for the approved release.

Each program transition gives exact additions, replacements and deletions from
`checkpoints.json`, with maintained source includes and complete checkpoints.
Lessons 7 and 10 explicitly make no edits. The sight lesson explains its
stationary diagnostic stage, candidate fan, sampled wall and diagonal checks,
and logical mask. The next lesson works through the real five-change record
before exposing the full table. Lesson 8 derives the attribute address and
colour values; lesson 9 explains keyboard buffering and reset; lesson 10 saves
and recovers the finished program.

The candidate-fan SVG is an original explanatory diagram, explicitly distinguished
from a game capture. No diagnostic PNG is used as public media. Original-manual
chapters were checked for arrays, strings, DATA, graphics, attributes, keyboard,
system variables and saving. Chapter 4 confirms that Sinclair BASIC skips an
empty FOR range; the zero-change guard is described as an explicit no-work return,
not as a workaround for a nonexistent language restriction.

Validation: production build passes (69 unit checks passed, nine existing skips).
The prose editing instructions also match all seven exact checkpoint transitions.
All eleven rendered pages have their source includes, unique IDs and resolving
local link targets. The checkpoint audit still passes all eight sources and
96 recorded native groups, source/token/TAP identities and the unchanged final
hash. All eighteen unrelated baseline paths retain their hashes/deletions.
The existing desktop and mobile navigation tests pass (two checks).
The original SVG was visually inspected and its heading clearance corrected.
The local overview and sight lesson were inspected through Chrome, including
the narrow layout, the rebuilt fan diagram and the ten-lesson navigation. Release checks now cover desktop and Pixel 7 mobile emulation: 24 browser groups
pass for all eleven pages, local links, source rendering, keyboard disclosures,
expanded-code overflow and BASIC navigation. All 44 light/dark accessibility
checks report zero axe violations. The mobile check identified an unfocusable
scrolling pseudocode block; it now supports keyboard access and the complete
suite passes. The desktop overview and mobile sight lesson were visually
inspected. Compact evidence is in `verification/lesson-browser.json` and
`verification/lesson-accessibility.json`.

The Spectrum system and both track landing pages were reviewed. The BASIC
Hidden worlds description now includes reading a guard's sight; the other
landing pages retain accurate independent-entry and target wording. Numeric
identity 23 and the approved game are preserved. The release note stays draft.

## Publication

Samples PR [25](https://github.com/code198x/code-samples/pull/25) is merged at
`e0b4f46`; samples CI passes. Website PR
[438](https://github.com/code198x/website/pull/438) is merged at `c31bc01c`;
website CI, offline link checks and code analysis pass. Pages deployment
[35430407066](https://github.com/code198x/website/actions/runs/35430407066)
succeeded.

Twenty-six live checks verify the overview, ten lessons, Spectrum landing pages,
fan diagram, all eight published checkpoint source hashes, both preparation
utilities and the draft release note’s absence from RSS. Evidence is in
`verification/lesson-live.json`. The [published overview](https://code198x.com/systems/sinclair-zx-spectrum/basic/night-patrol/)
links the complete sequence. All eighteen unrelated local edits retain their
prior contents or deletion state.
