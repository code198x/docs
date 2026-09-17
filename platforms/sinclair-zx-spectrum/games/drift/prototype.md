# Drift prototype record

The user agreed to try the [bounded steering and docking prototype](brief.md), noting the likely challenge in BASIC. A runnable stock 48K PAL listing and ROM-saved tape now exist in `code-samples/sinclair-zx-spectrum/basic/drift/prototype/`. Native playability and a teaching progression remain pending review. No website lessons have been authored or published.

The original white vector ship has eight headings and continuous position/velocity. O/P turn, SPACE adds thrust, and releasing it preserves momentum. Counterthrust brakes. One fixed docking box requires a low resultant speed and the ship's centre inside its inner bounds; fast passage is not a win. Walls end the attempt. S starts, R retries and Q quits. Turning and thrust are separate actions. Very short taps can fall between BASIC keyboard polls.

## Execution evidence

Emu198x Spectrum 0.25.0 ran the stock 48K PAL ROM. The builder entered the maintained source through ROM keyword keys, recorded `SAVE "drift" LINE 10`, and verification loaded that tape in a fresh process. No game-state injection or machine-code runtime helper was used. The verification manifest identifies source, tape, emulator, ROM and original captures.

Fourteen main execution groups compare 360 keyboard-driven updates against a host vector model: eight headings and wrap, retained two-component velocity, rotation without changing momentum, equal opposite burns, restart, speed cap, all four wall collisions, frozen failure, a two-axis transfer and low-speed docking, and frozen success. Instruction stepping finds BASIC line boundaries for these state comparisons; its session clock is not used to claim runtime performance.

Additional keyboard trials cover quitting from the title, held turning without translation and passing through the docking region too fast to win. A separate ordinary-frame trial covers held thrust, coasting, restart, a wall collision and quitting its result screen. These checks are distinct from a human judgement of control feel.

Ordinary frame execution observed 41 complete movement-commit intervals at rest: median 19 PAL frames, range 18–19, about 2.6 updates per second. This is a baseline for the loop, not a fixed frame rate or a measurement of thrust, collision or host-input latency. Trigonometry and triangle vertices are calculated once; the loop still pays for BASIC interpretation, array lookups and two triangle draws. There is no explicit delay.

The native preview was opened from the recorded tape. Title, arena and docked captures were inspected. Original-hardware performance, independent learner outcomes and native play acceptance remain unestablished. Keep performance/assembly revisits deferred; judge this BASIC docking trial before committing to lessons.
