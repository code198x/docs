# Crates — three-room prototype

The local source is `code-samples/sinclair-zx-spectrum/basic/crates/prototype/crates.bas`. It implements three fixed rooms for a stock 48K ZX Spectrum in Sinclair BASIC. The three-room game and visual direction are accepted after native play. This is the reference endpoint for teaching development, not a set of replacement lessons. Existing public Crates content remains unchanged.

## What to review

One crate begins below a short internal wall. The player must get to the correct side to push it towards the target. The room is deliberately introductory: it checks whether a player can understand moving versus pushing and recognise a blocked approach. A short solution is expected; this room does not establish sustained difficulty.

Room two puts a wall between the crate and its target, with a trap to the right. The player must choose a useful approach before committing to a push. The independent solver finds a ten-step, four-push solution; a legal push into the right-hand nook has no solution. Both the successful route and trap/restart route are exercised in the BASIC program. The revised visual direction and two-room prototype were accepted in native play.

Room three introduces two crates and two targets in a narrow delivery aisle. One crate blocks the space needed to push its neighbour. The solver finds a fourteen-step, six-push solution that first parks a crate sideways, delivers its neighbour deeper into the aisle, then brings the parked crate back. This is a correctness example, not the only permitted route or a claim about human difficulty. Partial delivery leaves the room active; both targets must be occupied. The third puzzle was accepted in native play with the rest of the sequence.

I/J/K/L move up/left/down/right, R restarts or replays, and Q exits. S starts from the instructions. Commands do not need Enter. The program remembers the last single-key reading, accepting a different direction immediately and clearing the remembered key on an empty reading. Holding a movement key does not repeat a move. After completion, N advances from rooms one and two or starts a new game after room three. R replays the current room; Q exits. Movement cannot dismiss completion.

The grid stores floor, wall, target, crate and crate-on-target. The player's coordinates are separate. Twenty original UDGs form square 16×16-pixel tiles: blue brickwork, yellow wooden crates, cyan target rings and a white player. Delivered crates turn green. A player on a target retains its ring and turns cyan. Drawing leaves the underlying grid unchanged. No collision or goal check reads screen colour.

The renderer changes only affected tiles. A remaining-target count is initialised with the room and adjusted only when a crate enters or leaves a target, avoiding a full-board scan after every step. Blocked attempts preserve state without repainting a status message. Very short key presses during BASIC processing can still be missed; native play must judge the resulting feel.

Restart rebuilds the fixed room and clears moves and completion. Successful player steps, including pushes, count once; blocked moves and invalid keys do not. The prototype is silent. It has no undo or room loader yet. All three maps are constructed by explicit assignments; editable-map validation belongs with the later loader.

## Verification approach

The runner enters the program through ROM keyboard events and compares all 64 array values, player coordinates, move count and completion against separately computed transitions. Screens are checked against those expected cells. Declared line edits create target-preservation, adjacent-crate and open-edge fixtures, then the original lines are restored before saving.

Execution passed on released Emu198x Spectrum 0.25.0 with a stock 48K ROM. The samples' `verification/results.json` records executable, ROM, source and tape hashes, the input trace and fifteen passing check groups. These cover held keys, blocked pushes, target preservation, reconstruction after CLS, array bounds, completion, restart, exit and fresh tape loading. All thirteen retained captures were visually inspected; the player-on-target capture uses a declared test fixture.

The harness waits for expected state and drawing to finish, then allows the input loop to become ready before sending another key. Tape creation uses ROM SAVE, and a fresh emulator successfully loads, solves all three rooms, replays, starts a new game and exits the saved program. Scripted checks are distinct from native host-input acceptance, human enjoyment and original-hardware behaviour.

The timing record for the two-room source hash measures the reduction in the sampled walk from 78 to 26 PAL frames (1.56 to 0.52 seconds), and the following push from 88 to 37 frames (1.76 to 0.74 seconds). These measurements include drawing and return to the input loop; they do not measure native host latency. The samples retain the measurement method and hashes in `verification/timing.py` and `verification/timing.json`.

## Teaching hand-off

The user agreed to settle the game at these three rooms and develop its teaching sequence. The [lesson brief](lesson-brief.md) owns the initial eleven-lesson plan and the remaining implementation work. The [teaching implementation](lessons.md) now has thirteen executed checkpoints, including the map loader and its validation. Preserve this accepted prototype as the behavioural reference.
