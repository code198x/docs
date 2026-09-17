# Drift prototype record

The user agreed to try the [bounded steering and docking prototype](brief.md), noting the likely challenge in BASIC. A runnable stock 48K PAL listing and ROM-saved tape now exist in `code-samples/sinclair-zx-spectrum/basic/drift/prototype/`. The user reported a successful native docking, but found speed hard to read. After the readout revision the user confirmed, “Yeah, I can dock fine”, and agreed to keep it as the BASIC baseline. The [teaching progression](lesson-brief.md) now has [six executed checkpoints](lessons.md) for eight lessons. The overview and eight website lessons are authored for local review; publication remains pending.

The original white vector ship has eight headings and continuous position/velocity. O/P turn, SPACE adds thrust, and releasing it preserves momentum. Counterthrust brakes. One fixed docking box requires a low resultant speed and the ship's centre inside its inner bounds; fast passage is not a win. Walls end the attempt. S starts, R retries and Q quits. Turning and thrust are separate actions. Very short taps can fall between BASIC keyboard polls.

## Execution evidence

Emu198x Spectrum 0.25.0 ran the stock 48K PAL ROM. The builder entered the maintained source through ROM keyword keys, recorded `SAVE "drift" LINE 10`, and verification loaded that tape in a fresh process. No game-state injection or machine-code runtime helper was used. The verification manifest identifies source, tape, emulator, ROM and original captures.

Fifteen main execution groups compare 360 keyboard-driven updates against a host vector model: eight headings and wrap, retained two-component velocity, rotation without changing momentum, equal opposite burns, restart, speed cap, all four wall collisions, frozen failure, a two-axis transfer and low-speed docking, frozen success, and speed/direction readouts matching actual velocity and the exact docking rule. Instruction stepping finds BASIC line boundaries for these state comparisons; its session clock is not used to claim runtime performance.

Additional keyboard trials cover quitting from the title, held turning without translation and passing through the docking region too fast to win. A separate ordinary-frame trial covers held thrust, coasting, restart, a wall collision and quitting its result screen. These checks are distinct from a human judgement of control feel.

The top row shows resultant speed in pixels per update and an explicit DOCK OK / TOO FAST cue. The lower DRIFT row shows east/west and north/south components. Numbers are rounded to tenths; the cue uses the exact squared-speed condition used by docking. DOCK OK describes speed, not the ship's position. The display updates on initialisation and after thrust, once the ship has been drawn. Coasting and turning preserve its values.

Ordinary frame execution observed 40 complete movement-commit intervals at rest: median 19 PAL frames, range 19–20, about 2.6 updates per second. The held-thrust trial observed a median of 44 frames across eight intervals; its range of 28–45 includes the transition from coasting into the first burn. Updating the readout has a measurable cost during thrust. These observations do not establish a fixed frame rate or host-input latency. There is no explicit delay.

The native preview was opened from the recorded tape. Title, arena, velocity and docked captures were inspected. Original-hardware performance and independent learner outcomes remain unestablished. The accepted native feedback applies to the endpoint, not independent learner outcomes for intermediate stages. Performance/assembly revisits remain deferred.
