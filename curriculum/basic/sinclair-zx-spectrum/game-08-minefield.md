# Game 08: Minefield

**Track:** Spectrum BASIC
**Genre:** Grid logic game
**Units:** 16
**Language:** Sinclair BASIC
**Max lines:** ~80

---

## Premise

A grid of hidden cells. Somewhere beneath them, mines. Your job: cross from the left edge to the right edge alive.

Each step reveals the cell you're standing on. If it's a mine, you're dead. If it's safe, it shows a number — how many of the eight surrounding cells contain mines. Use those numbers to deduce which cells are safe and plot a route to the exit.

This is not Minesweeper. You don't click to reveal — you walk. Every step is a commitment. You can't reveal a cell without standing on it. The numbers are your only guide, and sometimes the only way forward is a calculated risk: two cells ahead, one shows "1" and the other is unknown. Which way?

The game plays out on a 10x10 grid. The first level has 10 mines. By level five there are 25, and safe paths through the field are narrow. A flag system lets you mark cells you believe are mined — a memory aid, not a guarantee.

---

## Core Mechanics

### The Grid

A 10x10 grid of cells, displayed with PRINT AT in the centre of the screen. Each cell is two characters wide (to appear roughly square). The grid is surrounded by a border. The left column is the entrance, the right column is the exit.

| Display | Meaning | INK colour |
|---------|---------|------------|
| `[]` | Hidden cell | Blue (1) on blue PAPER |
| ` 3` | Revealed safe cell (adjacent mine count) | White (7) on black PAPER |
| `!!` | Mine (revealed on death) | Red (2), BRIGHT |
| `@@` | Player | White (7), BRIGHT |
| `<>` | Flagged cell | Yellow (6) on blue PAPER |
| `>>` | Exit | Green (4), BRIGHT |

### Movement

QAOP keys move the player one cell at a time. The player can only move to adjacent cells (up, down, left, right — not diagonal). Moving onto a hidden cell reveals it.

The player cannot move onto a flagged cell (flags must be removed first). This prevents accidental steps onto suspected mines.

### Revealing Cells

When the player steps onto a hidden cell:
1. Check the mine array. If the cell contains a mine: game over.
2. If safe: count adjacent mines (all 8 neighbours) and display the count.
3. If the count is 0: the cell is blank (no adjacent mines). In the basic version, only the stepped-on cell is revealed — no flood fill.

### Adjacent Mine Count

For a cell at position (r, c), check all 8 neighbours:

```
(r-1,c-1)  (r-1,c)  (r-1,c+1)
(r,c-1)    [cell]   (r,c+1)
(r+1,c-1)  (r+1,c)  (r+1,c+1)
```

Count how many contain mines. Display that number (0-8) on the cell. Edge and corner cells have fewer than 8 neighbours — skip any that fall outside the grid.

### Flagging

Press F while adjacent to a hidden cell to toggle a flag on it. Flags are visual reminders — "I think this is a mine." The game doesn't verify whether the flag is correct. Flags prevent accidental movement onto the flagged cell.

### Winning

Reach any cell in the rightmost column. The level is complete. All mines are revealed (safe cells turn green, mines turn red), and a bonus is awarded based on how many flags were correctly placed.

### Losing

Step on a mine. The mine flashes red, all mines are revealed, "GAME OVER" appears. The player sees where every mine was — a learning moment for the next attempt.

### Levels

Five levels with increasing mine density:

| Level | Grid | Mines | Safe cells |
|-------|------|-------|------------|
| 1 | 10x10 | 10 | 90 |
| 2 | 10x10 | 15 | 85 |
| 3 | 10x10 | 18 | 82 |
| 4 | 10x10 | 22 | 78 |
| 5 | 10x10 | 25 | 75 |

Mine placement is random but guaranteed: the starting column (leftmost) is always mine-free, and at least one path from left to right exists (verified at generation time by a simple check).

### Scoring

| Event | Points |
|-------|--------|
| Cell safely revealed | 5 |
| Level completed | 100 × level number |
| Correct flag bonus | 10 per correctly flagged mine |

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | The Mine Array | Create a 2D array with DIM m(10,10). Fill it with zeros. Place 10 mines (value 1) at random positions using RND. Print the raw array to the screen to verify placement. | 2D arrays (DIM with two dimensions), array initialisation, random placement in a grid |
| 2 | Drawing the Grid | Draw a 10x10 grid of hidden cells (`[]` in blue) using nested FOR/NEXT loops and PRINT AT. Each cell is two characters wide. Add a border around the grid. | Nested loops for 2D display, mapping array positions to screen positions |
| 3 | The Player | Place the player (`@@`) in the top-left cell of the grid. QAOP moves the player one cell at a time. Erase old position, draw new. Boundary checks keep the player inside the grid. | Player movement on a 2D grid, coordinate mapping (array position to screen position) |
| 4 | Revealing a Cell | When the player moves onto a hidden cell, reveal it. For now, just show "0" — no mine counting yet. Track which cells are revealed in a second array: DIM v(10,10) where 0=hidden, 1=revealed. | Flags as array values (0 and 1), parallel arrays (mine grid and visibility grid) |
| 5 | Counting Neighbours | Write a GO SUB that counts adjacent mines for a given cell. Check all 8 neighbours. Handle edges: if a neighbour would be outside the grid (row 0 or row 11), skip it. Display the count on the revealed cell. | Reading 8 neighbours, boundary guarding for array access, GO SUB with input/output via variables |
| 6 | Stepping on a Mine | Check the mine array when the player moves. If m(r,c)=1: the cell is a mine. Flash the border red, BEEP, print "BOOM!" — game over. Reveal all mines on the grid in red. | Game over trigger, revealing hidden state, visual feedback |
| 7 | The Numbers in Colour | Colour the revealed numbers to aid readability. 0=grey, 1=blue, 2=green, 3=red, 4=cyan, 5=magenta, 6=yellow, 7=white, 8=bright white. Matches classic Minesweeper convention. | INK per value, colour as information |
| 8 | Safe Start | Guarantee the leftmost column has no mines. After random placement, check column 1 — if any mines exist there, move them to a random empty cell elsewhere. The player always has a safe starting column. | Post-placement validation, moving array values, ensuring fair play |
| 9 | The Exit | Mark the rightmost column with `>>` in green. When the player reaches any cell in that column, the level is complete. Display "LEVEL COMPLETE", reveal all mines, show the score. | Win condition, level completion detection |
| 10 | Flagging Cells | Press F to flag the cell the player is facing (one step in the last-moved direction). Flagged cells show `<>` in yellow. Press F again to remove the flag. The player cannot walk onto flagged cells. | Toggle flags, directional context, input beyond movement |
| 11 | The HUD | Top of screen: level number, score, cells revealed, flags placed. Update after each move. Keep it compact — one line. | HUD layout, multiple values on one line, formatted display |
| 12 | GO SUB Architecture | The code has grown. Reorganise: GO SUB 500 for drawing, GO SUB 600 for neighbour counting, GO SUB 700 for mine checking, GO SUB 800 for flag toggling. The main loop calls subroutines — each does one job. | Multiple GO SUBs, subroutine architecture, separating data from display |
| 13 | Level Progression | Five levels. After completing a level, increase the mine count, clear the grid, regenerate mines, reset the player to the left edge. Each level is harder but the grid size stays the same. | Level parameters, regeneration, progressive difficulty |
| 14 | Path Guarantee | After placing mines, verify that at least one path exists from left to right. Simple check: for each row, can you step from column 1 to column 10 without hitting a mine? If no path exists, regenerate. | Validation after generation, path existence check, regeneration loop |
| 15 | Sound and Polish | Step onto safe cell: quiet click. Flag placed: short tone. Mine hit: explosion BEEP (descending). Level complete: ascending fanfare. Border colour changes per level. | Sound design, per-level visual identity |
| 16 | The Finished Game | Play all five levels. Verify mine counts, neighbour counting at edges and corners, flag toggling, path guarantee, scoring. Clean the listing. A complete logic game in ~80 lines. | Full integration testing, code review, the finished product |

**Milestone:** The learner understands 2D arrays as the backbone of grid-based games. They can initialise arrays, read neighbours, use flags (0/1 values) to track state, and organise code into multiple GO SUBs. The separation between data (the mine array) and display (what's on screen) is now second nature.

---

## Technical Notes

### Data Structures

```
DIM m(10,10)   - mine grid: 0=safe, 1=mine
DIM v(10,10)   - visibility: 0=hidden, 1=revealed, 2=flagged
```

Two parallel arrays. The mine grid is generated once per level and never changes. The visibility grid updates as the player explores. The display is derived from both: if v(r,c)=0, show hidden; if v(r,c)=1, show the neighbour count from m(); if v(r,c)=2, show a flag.

### Neighbour Counting GO SUB

```
600 REM COUNT NEIGHBOURS AT (nr, nc) → result in nn
610 LET nn = 0
620 FOR dr = -1 TO 1
630   FOR dc = -1 TO 1
640     IF dr = 0 AND dc = 0 THEN GO TO 680
650     LET tr = nr + dr: LET tc = nc + dc
660     IF tr < 1 OR tr > 10 OR tc < 1 OR tc > 10 THEN GO TO 680
670     LET nn = nn + m(tr, tc)
680   NEXT dc
690 NEXT dr
700 RETURN
```

The double loop checks all 8 neighbours. Boundary guarding (line 660) skips positions outside the grid. Since mines are stored as 1 and safe cells as 0, summing the array values gives the count directly.

### Screen Mapping

Array position (r, c) maps to screen position:
- Screen row = r + 3 (offset for border and HUD)
- Screen column = (c - 1) × 3 + 2 (each cell is 2 chars wide with 1 char spacing)

A GO SUB converts array coordinates to screen coordinates before every PRINT AT.

### No ELSE on the 48K

Sequential IF/THEN lines handle the three cell states (hidden, revealed, flagged). After checking v(r,c)=0, v(r,c)=1, and v(r,c)=2 in separate lines, exactly one branch fires.

### Path Guarantee

The simplest guarantee: check that no row is completely blocked by mines from left to right. For a 10x10 grid with 25 mines (level 5), this is almost always true, but the check prevents the rare unwinnable layout. A more thorough check (flood fill from left column to right column) would be better but costs more lines — the row check is good enough for 80 lines.

### Line Numbering

- 1-49: Initialisation, DIM arrays, title screen
- 50-99: Level setup (place mines, validate path, draw grid)
- 100-199: Main game loop (input, move, check)
- 200-299: Level complete / game over screens
- 500-599: Draw subroutine (hidden/revealed/flagged cells)
- 600-699: Neighbour counting subroutine
- 700-799: Mine check and death subroutine
- 800-899: Flag toggle subroutine

### Memory and Performance

Two 10x10 arrays use ~200 bytes. The program is ~80 lines (~4-5 KB). No performance concerns — the game is turn-paced (nothing moves until the player presses a key), so there's no frame rate pressure.

---

## Changelog

- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
