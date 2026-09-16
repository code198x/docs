# Crates — replacement brief

**Status:** The user accepted the three-room prototype and agreed to settle that game scope and develop the teaching sequence. The array holds game state and rendering remains separate. The [lesson brief](lesson-brief.md) defines the approved eleven-lesson course, supported by thirteen executed checkpoints. The approved overview and eleven lessons are published; legacy samples remain available.
**Route:** Meet BASIC → Bright Spark → Volley → Touchdown → Sonar → Crates. Crates is not the final BASIC project or an assumed prerequisite for a named successor.
**Target:** Stock 48K ZX Spectrum, PAL, Sinclair BASIC; keyboard input and tape save/load.
**Publication:** The [implementation record](lessons.md) owns executed teaching checkpoints, website checks and live publication evidence.

Apply the [project charter](../../../../PROJECT.md), [game brief specification](../../../../specifications/brief.md) and [curriculum design](../../../../specifications/curriculum.md). The [source assessment](assessment.md) distinguishes the retained brief, authored lessons and actual samples. Earlier reasoning remains in Git history.

## The game

Move around a warehouse and push each crate onto a target. Walking into a crate attempts a push: the player needs space to stand behind it and the cell beyond it must be free. Crates cannot be pulled or pushed in pairs. The interesting choice is often where to stand before pushing, or which crate to move first. A locally legal push can leave the room impossible to finish.

A completed room needs instructions, visible targets and crates, deliberate single-step controls, a clear success state, restart, replay and exit. One well-designed room can fulfil that promise. It is not automatically a demo because it has only one level.

The agreed finished package is **three short original rooms**, each fitting an 8×8 board. The first demonstrates pushing and delivery, the second requires a change of approach, and the third uses two crates to make access matter. All three have executed solutions and were accepted in native play. Keep their layouts and visual direction as the teaching endpoint; do not add a larger campaign or treat the solver's shortest routes as learner performance targets.

Allow the player time to think. A move counter records successful player steps, including pushes; blocked moves and unrelated keys do not increment it. Do not introduce a timer, lives, compulsory par or rating. Restart restores the current room. After completion, let the player explicitly continue, replay or quit; after the last room, offer a fresh run or exit.

## What changes after Sonar

Sonar's array records knowledge about a hidden object. Crates' array describes the warehouse, and a successful push changes it. The teaching focus is **inspect the proposed change, decide whether it is legal, then update the affected state**.

New work includes decoding text maps with the DATA/READ techniques introduced in Touchdown, identifying the cell beyond a crate, preserving the underlying target when an object moves, checking the goal condition, and reloading a known starting state. Two-dimensional arrays, nested loops, PRINT AT, colour, routine calls, conditions and reset already have local precedents. Recall them briefly at the point of use.

INKEY$ and keyboard polling are not first-time concepts on the current route. The useful contrast is between Touchdown's continuously changing world and a puzzle that changes only on accepted commands. One step per key press is a choice for this puzzle, not a universal input technique. No attendance at Cipher, Three in a Row or The Caverns is assumed; recall DATA, READ and RESTORE locally and explain string slicing when it is used.

## Representation

Retain the existing sample's useful model: one numeric grid, with player row and column stored separately. Use explicit cell codes: 0 floor, 1 wall, 2 target, 3 crate on floor and 4 crate on target. The last code represents a combination; it does not make the underlying target disappear. A player standing on a target leaves code 2 in the grid.

A walk checks the destination before updating the player position. A push checks both the adjacent crate cell and the cell beyond before changing anything. Restore the old crate cell to floor or target, place the crate on its new floor or target, then advance the player. A rejected action changes neither the player, grid nor count.

Draw cells from the grid and overlay the player at its coordinates. Moving the player away should redraw the underlying cell from the grid, avoiding a second variable that duplicates whether the player stands on a target. Reuse the cell renderer for ordinary changes and full reconstruction. The accepted prototype verifies this without a duplicate `ps` display flag.

Use the array as the authority for movement and victory. Colour and symbols present its values. ATTR is not needed to decide collisions here; a later investigation of reading screen attributes would be a separate machine-specific comparison.

Begin with one known map. Show why repeated assignments become awkward before introducing readable row strings and a loader. When the second room makes a single DATA section insufficient, introduce explicit level selection and RESTORE. Do not require an opaque framework to draw the first warehouse or bind level identity to an unexplained arithmetic line-number convention.

Before indexing, establish that candidate coordinates lie within the grid. Enclosing walls help level design, but malformed or learner-edited maps must not cause out-of-range array access. Define and check the map contract: eight rows of eight recognised symbols, exactly one player, at least one crate, equal crate and target totals, and legal starting occupancy. Count combined states in both totals. Structural validity does not establish solvability.

## Controls, appearance and recovery

Use I/J/K/L for up/left/down/right, matching the retained game, with R to restart and Q to quit. Show the mapping on screen. Accept either case; ignore other keys. Remember the previous key so a held direction cannot race across a small room. A different direction can be accepted immediately; an empty reading clears the remembered key. Check held and overlapping keys, restart, and the transition into completion prompts. A movement key must not also dismiss success or begin the next room.

Use the accepted square 16×16-pixel UDG tiles, dark floor, brick walls, wooden crates, target rings and small player. A target beneath the player remains visible; delivered crates turn green. Collision reads only the array. Teach how the tiles are made and assembled rather than supplying an unexplained asset bank. Assess an additional non-colour delivery cue during source preparation, as described in the lesson brief.

Keep the accepted game silent. Sound, scrolling and animation are not unfinished requirements.

Restart is part of the first complete room, not late polish. The old blanket ban on undo is not retained: first test whether restarting these short rooms is comfortable. If play reveals that recovering from a mistaken input dominates the puzzle, compare a single-step undo or smaller rooms before adding more content. Undo history is not a prerequisite for proving the push mechanic.

## Runnable investigation

These development stages describe observable results. The [lesson brief](lesson-brief.md) now owns the teaching order and its provisional unit boundaries. Keep each source complete and readable, and split a checkpoint if its teaching load is too large.

| Stage | Result | Change to explain | Check |
|---|---|---|---|
| 1. Inspect a room | A small fixed warehouse with a player, crate and target | Cell codes, grid-to-screen positions, player overlay; start with explicit state | Symbols are distinguishable; drawing does not change state |
| 2. Walk deliberately | One step per command; walls and board edges block movement | Direction offsets, candidate coordinates, bounds before lookup, release handling | All directions, blocked/invalid input, long holds and Q exit |
| 3. Push a crate | A legal push moves the crate and player; a blocked push changes nothing | Two-cell lookahead and coordinated updates | Push towards floor, wall and another crate; preserve crate count |
| 4. Complete one room | Targets survive movement; success, restart, replay and exit work | Combined cell state, renderer from state, goal check and reset | Push onto and off a target; walk across targets; restart after getting stuck; held keys do not skip success |
| 5. Make the map editable | The same room loads from readable DATA strings | Parsing symbols and map validation; replace the awkward initial setup visibly | Loaded state equals the earlier room; reject malformed data; redraw reconstructs the same picture |
| 6. Give each room a purpose | A small sequence of verified puzzles, with explicit transitions | Reuse the loader, select DATA, reset per-room state and finish the sequence | Solve every room; restart each; no state leaks; compare human decisions and recovery costs |
| 7. Keep the game | Saved program starts reliably and supports a complete visit | Instructions, provenance, tape save/load and any justified presentation refinements | Fresh-load, play, solve, advance, restart, finish, replay and exit |

Stage 4 is already a complete fixed-room game. The accepted prototype extends it to three rooms. The teaching loader is implemented and checked against the accepted layouts; the prototype retains its explicit assignments.

## Evidence and finishing

Read and reuse donor routines deliberately; do not inherit their verification claims. Sources belong in `code-samples/sinclair-zx-spectrum/basic/crates/prototype/`, separate from the six published legacy checkpoints. Keep verification helpers and executed captures with the prototype. Use released Emu198x Spectrum with the configured stock 48K ROM; record the executable version and hash, ROM identity, input sequence and source hash. Type source and any declared test edits through the ROM editor, and save/load through ROM commands. Do not claim original-hardware behaviour from emulator checks.

For each accepted action, compare the complete grid and player coordinates before and after. Crate count and target count must remain constant; only a push changes crate positions. A blocked action must preserve the whole state. Check zero, one and multiple uncovered targets, including a player standing on an uncovered target. Do not accept an empty or invalid map as an immediate win.

Redraw after clearing the display and verify the same state and picture. Reset must restore the original layout, player, counter and messages. Test keys held through restart and completion, lowercase/uppercase commands and every exit phase. Test coordinate bounds even when an edge wall is missing.

Record actual puzzle solutions and verify them through the target program. A separate solver can check solvability or compare layouts, but it does not establish BASIC correctness or human enjoyment. A crate in a non-target wall corner is a useful trap demonstration; a crate already on a corner target is not automatically a failure. Other deadlocks also exist. Never teach that equal counts or an absence of corner crates proves a level solvable.

Ask the player which push changed their plan and whether restarting was useful or frustrating. Reconsider the room designs or recovery mechanic if play becomes mostly retracing known moves. Reconsider presentation if targets beneath objects are hard to recognise. Keep original level maps and character graphics, state their licence, and add only sourced historical context that helps the lesson.

Source language details from Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming*, second edition (Sinclair Research, 1983): chapters 4–5 (loops and routines), 6 (DATA/READ/RESTORE), 8 (strings), 12 (arrays), 15–16 (printing and colour), 18 (keyboard input), 19 (sound, if used) and 20 (tape). Confirm the relevant passages during implementation. The samples use the repository's MIT licence.

Potential later Pattern Library material includes two-cell movement checks, reconstructing a display from stored state and loading a restartable map. Link these back to the finished game if extracted; they are not additional requirements for the first prototype. A level editor, large campaign, automatic deadlock detection, solver, scoring targets and extended undo history remain possible later work, not the assumed ending of BASIC.
