# Crates — Brief

**Title (working):** Crates
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 2, Game 8 of 8 (slot 16)
**Headline concept:** The Rule IS the Game — the mechanic is the experience
**Embedded concept:** Constraint as gameplay — limitation creates the puzzle
**Topics:** 12 topics, ~12–16 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic.md`](../../../../specifications/brief-basic.md)

---

## 1. Pedagogical Role

Teach that a single mechanic rule — "you can push a crate but not pull it" — creates the entire game, and that ATTR (reading attribute bytes) enables character-cell collision detection — so the learner arrives at Volume 3 with attribute-driven game logic as a working tool.

---

## 2. Classic Ancestors

- **Sokoban** (Hiroyuki Imabayashi, 1982) — the warehouse puzzle. Push crates onto target squares. Cannot pull. Cannot push two crates at once. The mechanic is the constraint; the constraint is the puzzle. One of the most deeply studied puzzle games in computing.
- **Spectrum warehouse puzzles** — published in magazines from 1984 onwards. The Sokoban mechanic translates perfectly to character-cell graphics.

---

## 3. Core Experience

Push crates onto target squares in a small warehouse. You can only push, never pull. You can only push one crate at a time. Push a crate into a corner and it is stuck forever. Each level is a spatial puzzle — the solution is a sequence of pushes that avoids trapping any crate. Short levels (5–10 moves) that feel like "I almost had it."

---

## 4. Visual Direction

- **Character-cell warehouse.** Walls as solid PAPER blocks. Floor as dark background. Crates as coloured characters (BRIGHT 1 blocks). Targets as differently coloured marks on the floor. Player as a distinct character.
- **ATTR-driven.** The colour of each cell *is* its identity: wall cells have one PAPER colour, floor cells another, crates another, targets another. The player reads the screen through colour, and the code reads the screen through ATTR.
- **Small levels.** 8×8 or 10×10. The entire level fits on screen without scrolling.
- **Magazine-screenshot test:** a small warehouse — walls, three crates, three targets, the player mid-puzzle — the reader tracing the solution.

---

## 5. Audio Direction

- **Push.** Short tone when a crate moves.
- **Crate on target.** Ascending chime — progress.
- **Level complete.** Fanfare — all crates on targets.
- **Move.** Quiet click — the player's movement, distinct from pushing.

---

## 6. Level Design Direction

- **Content source:** DATA statements hold level layouts as strings — one string per row. Each character represents a cell type: `#` = wall, `.` = floor, `@` = player, `$` = crate, `*` = target, `+` = crate on target.
- **Difficulty curve.** Level 1: one crate, one target, no traps possible. Level 2: two crates, a corner to avoid. Level 3+: three crates, multiple dead-end risks. The constraint (push only, one at a time) creates the difficulty — the level designer just provides the space.
- **Scale:** 5–8 hand-designed levels. The learner designs their own.
- **Onboarding.** Level 1 is solvable in 3 pushes. The player learns: push works, pull doesn't, corners are death.

---

## 7. Anti-goals

- No undo — push a crate into a corner and it is stuck. Restart the level. The consequence *is* the puzzle's discipline.
- No pull mechanic — push only. Pulling would halve the puzzle's difficulty.
- No scrolling — every level fits on one screen.
- No animation — movement is instant (PRINT AT, clear old position, draw new). Smooth animation is V3 territory.
- Maximum ~60 lines of BASIC + DATA.

---

## 8. Topic Progression

1. **The warehouse.** Draw a level from DATA: walls, floor, targets. Use PRINT AT with PAPER colours for each cell type. The level is a visual grid — walls in one colour, floor in another, targets in a third. **New:** DATA-driven level layout, colour-as-type. **Program:** ~10 lines + DATA.

2. **The player.** Place the player character (`@`) on the floor. Move with INKEY$ (or INPUT for turn-based). Clear old position, draw new. Walls block movement — check the cell before moving. **New:** character movement with wall collision (check before move). **Program:** ~18 lines + DATA.

3. **ATTR.** Instead of checking a separate array, read the *screen* directly: `LET a = ATTR(row, col)`. The attribute byte encodes INK and PAPER for that cell. If the PAPER matches the wall colour, the cell is a wall. The screen *is* the data. **New:** ATTR function, reading the screen as game state. **Program:** ~22 lines + DATA.

4. **Pushing a crate.** When the player moves toward a crate, check the cell *beyond* the crate. If it is floor (or target), push: move the crate one cell, move the player into the crate's old position. If the cell beyond is a wall or another crate, the push fails. **New:** two-cell lookahead (player → crate → beyond), conditional move. **Program:** ~30 lines + DATA.

5. **Crate on target.** When a crate lands on a target cell, mark it (change colour or character). Track how many crates are on targets. When all crates are placed, the level is complete. **New:** state tracking per object (crate placed vs unplaced), win condition. **Program:** ~34 lines + DATA.

6. **Multiple levels.** Store several levels in DATA. When a level is complete, read the next one and redraw. A level counter shows progress. **New:** sequential DATA-driven levels, level transitions. **Program:** ~40 lines + DATA.

7. **Restart.** If the player gets stuck (crate in a corner), a key (R) restarts the current level by re-reading its DATA. The RESTORE + counted READ pattern from Cipher, applied to level data. **New:** level restart without program restart. **Program:** ~44 lines + DATA.

8. **Move counter.** Track pushes per level. Display on screen. The player's goal shifts from "solve" to "solve efficiently." The optimal push count for each level is a target to beat. **New:** efficiency metric, optimal-play target. **Program:** ~48 lines + DATA.

9. **Designing levels.** The learner writes their own level DATA. Rules for valid levels: every crate must have a reachable target, no crate should start in a corner (unsolvable). The DATA format is the level editor — change the strings, change the puzzle. **New:** level design as a discipline. **Program:** ~52 lines + DATA.

10. **INKEY$ for smooth movement.** Replace INPUT with INKEY$ polling — the player presses Q/A/O/P (or cursor equivalents) and the character moves immediately, one step per press. Key draining prevents repeated movement from a held key. **New:** INKEY$ for responsive movement (reinforces Bright Spark's key drain pattern). **Program:** ~56 lines + DATA.

11. **Polish.** Title screen. Per-level par display ("Par: 8 pushes"). Level select (INPUT a level number). Colour refinement — make the warehouse look like a warehouse. **New:** level select menu. **Program:** ~58 lines + DATA.

12. **Make it yours.** The design lesson: the rule ("push, don't pull, one at a time") *is* the entire game. No power-ups, no enemies, no timer. The constraint creates the puzzle. That is the headline concept: **The Rule IS the Game**. When the mechanic is simple enough, the level design carries everything. **New:** none (design reflection). **Program:** ~60 lines + DATA.

---

## 9. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum
- [ ] ATTR correctly identifies wall, floor, crate, and target cells
- [ ] Pushing works: player → crate → empty cell moves both
- [ ] Pushing fails: crate against wall or another crate does not move
- [ ] Crate-on-target detection works and updates the display
- [ ] All levels are solvable (test each by hand)
- [ ] Restart correctly reloads the current level
- [ ] Level transition works when all crates are placed
- [ ] British English throughout
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 10. Pattern Library Extractions

- **basic** — ATTR-based collision: reading the screen's attribute byte to determine cell type. The Spectrum-specific technique that makes the screen itself the game map. Avoids maintaining a separate collision array.
- **physics** — push mechanic: two-cell lookahead (player position + direction = crate; crate position + direction = destination). The pattern behind every push-block puzzle.
- **framework** — DATA-driven levels with restart: string-encoded level layouts, RESTORE for level select and restart. The simplest level-loading system.

---

## 11. Vault Tie-ins

- **Sokoban** (Hiroyuki Imabayashi, 1982) — the warehouse puzzle as direct ancestor.
- **ZX Spectrum ATTR function** — the hardware feature that makes colour-as-collision possible.
- **Constraint-based game design** — the design principle that a single restrictive rule can generate infinite puzzle depth.
