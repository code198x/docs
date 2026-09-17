# Quickstep — prototype brief

**Status:** The user chose the crossing-and-timing direction after Drift. The first native trial worked but was too easy and occupied too little of the screen. The revised prototype expands the crossing before a finished scope or lesson count is agreed.
**Target:** Stock 48K PAL ZX Spectrum, Sinclair BASIC, keyboard and ROM-loaded tape. No machine-code helper or expansion.
**Sources:** `code-samples/sinclair-zx-spectrum/basic/quickstep/prototype/`. The earlier catalogue supplies only the name and hazard-pattern theme; no earlier playable implementation was found.

## Experience

Cross two banks of three lanes of predictable moving vehicles, rest at the halfway strip, and reach the marked exit. Observe a gap, choose a step, then decide whether to continue or wait. One board filling nearly the whole play area, fixed repeating patterns, immediate failure and retry. No countdown or life budget. Success ends the crossing and offers another attempt.

I/J/K/L move up/left/down/right, matching the earlier Tail Chase layout. S starts, R retries and Q quits. Movement uses a discrete rhythm; held input repeats and a recognised short press can be retained for the next step. A new direction replaces a queued one. Resting strips remain safe regardless of vehicle phase.

The prototype succeeds if the player can read danger, act on that knowledge and understand a failed crossing. Human play feedback must assess response and appeal separately from scripted completion. If simultaneous animation is too slow or crossings look ambiguous, revise the cadence or representation within BASIC before expanding scope.

## Rules and representation

A 15-column, nine-row logical board uses 16×16-pixel cells: 240×144 pixels, compared with the first trial’s 208×112. Only rows 0, 4 and 8 are safe, leaving two uninterrupted banks of three hazard lanes. Each lane has three vehicles occupying two cells apiece, separated by three-cell gaps. Lane positions wrap and directions alternate. From top to bottom, lanes advance every three, four, two, three, four and two updates. The opening phases require lateral movement and timing; holding up does not cross the board.

For each update, propose the player destination and reject out-of-bounds movement. Test against current vehicle occupancy before accepting a step. Then advance due lanes and test the accepted player position again. This order catches entering occupied cells, swaps with a vehicle, and a vehicle arriving at a waiting player. The logical rectangles include the transparent corners of the artwork; colour does not decide collisions. The goal is the centre cell of the top strip.

Stored phases and countdowns drive the rules. Two character strings per lane hold its drawing; rotating these by two characters moves its artwork one cell. Only due lanes redraw. A separate player overlay restores its old background before redrawing. No per-pixel collision scan or full-screen redraw is required per update.

## Presentation and learning

Original UDG artwork gives the player and vehicles recognisable silhouettes. Lane arrows distinguish travel direction; dotted blue resting strips and a green exit provide context, with textual instructions explaining their roles. The first version is deliberately silent. Source DATA owns all artwork; there are no external assets.

Potential teaching includes periodic events, different update rates, input buffering, cyclic coordinates, collision order, state separate from drawing, and deterministic patterns as level design. Arrays, strings, loops and subroutines receive local explanation when lessons are designed. This builds on Tail Chase's clocked movement and Crates' grid rules while making waiting an active choice. Shared conceptual links remain an authoring task.

## Development and verification

First prove the board, movement and readable vehicles; then the independent lane cycles and input; then contact, completion and replay. These are prototype concerns, not a settled lesson sequence.

Enter the maintained source through the stock ROM keyboard, save a self-starting tape, and load it in a fresh process. Check source identity, an independent host occupancy model, both wrap directions, safe waits, bounds, both contact phases, a complete crossing, frozen results, retry and phase exits. Check short and held input with ordinary video-frame execution separately from CPU-stepped state checks. Retain original screenshots, source/tape/executable hashes and observed timing. Native approval and original-hardware performance remain unestablished until separately observed.

The ROM's LAST K byte (23560) retains a newly pressed key; FRAMES begins at 23672. Primary reference: Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming*, second edition (Sinclair Research, 1983), [chapter 25, system-variable table](https://worldofspectrum.org/ZXBasicManual/zxmanchap25.html). The prototype combines the key latch with INKEY$ and reads the frame counter without changing its value. A 32-frame target spaces update starts; processing may exceed it. Overruns do not trigger a burst of catch-up steps. Each update consumes one input command; the player stays visible on safe strips while due lanes redraw.
