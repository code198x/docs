# Tail Chase — prototype brief

**Status:** The playable prototype is accepted after native play: “Works, just fine”. See the [execution record](prototype.md). The [teaching sequence](lesson-brief.md) now has twelve executed checkpoints and ten approved lessons published after Crates; see the [implementation record](lessons.md).
**Target:** Stock 48K ZX Spectrum, PAL, Sinclair BASIC; keyboard and ROM tape loading. No target extensions.
**Sources:** `code-samples/sinclair-zx-spectrum/basic/tail-chase/prototype/`. The website catalogue currently lists Tail Chase as a proposal; its inherited “first custom graphics” claim is obsolete after Touchdown and Crates.

## The accepted prototype round

A snake moves continuously through a 24×16 arena. Steer towards eight pieces of food, growing from four to twelve cells. The wall and the snake's body end the attempt; R restarts and Q leaves. Eight foods complete the round. I/J/K/L steer; an opposite direction is ignored. Only one perpendicular turn can be queued per movement update, so two quick inputs cannot reverse into the neck.

The player continually chooses a route to food while keeping turning space. Food appears only in a free cell. There are no extra obstacles, speed ramp, lives or campaign in this first trial. A finite round makes completion and replay concrete. Food positions are random rather than a designed solution.

The prototype uses original eight-pixel character artwork: brick borders, four directional faces, a rounded body and a distinct fruit shape. White head, cyan body and yellow fruit separate roles; shape also distinguishes them. FOOD and LENGTH display progress. The game is deliberately silent for this movement trial.

## Teaching question

How can several moving parts follow one another? This combines continuous updates from Volley/Touchdown with the stored spatial state developed in Sonar/Crates. Custom characters and polling are recalls, not new subjects. An ordered body and an occupancy grid serve different purposes: order identifies the head and departing tail, while occupancy tests a candidate square.

The endpoint stores body coordinates in a twelve-slot circular array. Advancing head/tail indices avoids shifting every coordinate on every move. A future teaching plan must motivate and explain this representation, possibly comparing a short shifted array first; the prototype is not an unexplained starter engine or a settled lesson count.

A non-growing head may enter the square its tail vacates on that same update. A rejected move must preserve the body. Growth keeps the tail and increases length by exactly one. Rendering reads these rules; colour never decides collision.

## Timing and tools

The ROM's low FRAMES byte supplies elapsed time modulo 256; the initial movement threshold is 18 PAL frames. It is a minimum interval, not a promise that BASIC finishes each move within 18 frames. Measure actual movement at several lengths and inspect native keyboard responsiveness before deciding the pace is suitable. The low-byte calculation assumes the active loop samples within one 256-frame wrap; no pause is implemented.

Host Python scripts enter source using ROM keyword keys, save a tape and observe state through Emu198x. They are verification tools, not runtime game dependencies. The recorded tape must load in a fresh 48K session and begin with instructions.

## Checks and decision

Check held steering, invalid and opposite directions, the queued-turn rule, wall and self collisions, departing-tail entry, food exclusion, growth, full completion, restart and Q from title/play/end. Compare ordered positions and every occupancy cell with an independent model. Inspect captured artwork and messages. Record configuration and source/tape identities.

The recommendation depends on native play: steering must be predictable, the head and food readable, and the full-length body must retain an acceptable pace. Adjust speed, arena or scope if the trial is tedious or too demanding. The endpoint has earned native approval; agree the teaching sequence before writing lessons.

Language and timing reference: Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming*, second edition (Sinclair Research, 1983), chapters 4–6, 12, 14–16, 18 (keyboard and FRAMES), and 20. Artwork and game source are original project material under the samples repository's MIT licence.
