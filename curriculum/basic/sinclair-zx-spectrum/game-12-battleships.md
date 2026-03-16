# Game 12: Battleships

**Track:** Spectrum BASIC
**Genre:** Two-player strategy game
**Units:** 32 (2 phases × 16 units)
**Language:** Sinclair BASIC
**Max lines:** ~300

---

## Premise

Two players share a keyboard. Each places a fleet of ships on a hidden 10×10 grid, then takes turns calling coordinates to find and sink the opponent's fleet. "B7." "Miss." "D4." "Hit!" "You sank my destroyer!"

Battleships is the classic hidden-information game. Each player has two grids: one showing their own ships and where the opponent has fired, and one tracking their own shots against the opponent (hits, misses, and unknowns). The game manages four 2D arrays simultaneously — the most complex data structure the learner has handled so far.

The "pass the keyboard" mode is the heart of the design. After each turn, the screen clears completely so the next player can't see the opponent's ships. A "Press any key when Player 2 is ready" prompt ensures privacy. It's low-tech security, and it works perfectly — just like the cardboard divider in the board game.

---

## Core Mechanics

### The Grids

Each player has a 10×10 grid. Columns are labelled A-J, rows 1-10. Every cell starts as water (empty).

Each player sees two grids displayed side by side:

| Grid | Purpose | Shows |
|------|---------|-------|
| My Ships | Your own fleet | Your ships, opponent's hits and misses against you |
| My Shots | Your attacks | Where you've fired: hits, misses, sunk ship markers |

### The Fleets

Each player places 5 ships:

| Ship | Length | Symbol |
|------|--------|--------|
| Carrier | 5 | C |
| Battleship | 4 | B |
| Destroyer | 3 | D |
| Submarine | 3 | S |
| Patrol boat | 2 | P |

Ships are placed horizontally or vertically. They cannot overlap, extend off the grid, or be placed diagonally.

### Ship Placement

Each player places ships one at a time. The game prompts for a starting coordinate (e.g. "B3") and direction (H for horizontal, V for vertical). The game validates that the ship fits on the grid and doesn't overlap an existing ship. If invalid, it explains why and asks again.

The player sees their grid update as each ship is placed. After all 5 ships are placed, the screen clears for the other player to place theirs.

### Taking Shots

On their turn, a player enters a coordinate (e.g. "D7"). The game checks the opponent's ship grid:

| Result | What happens |
|--------|-------------|
| Miss | Water. Mark with `·` on the shooting player's tracking grid. Short low BEEP. |
| Hit | Part of a ship. Mark with `X` on the tracking grid. Mark the hit on the opponent's ship grid too. Sharp high BEEP. |
| Sunk | The final hit on a ship. "You sank the [ship name]!" All cells of that ship change to a sunk marker. |
| Already fired | "You already fired there." No penalty, but the shot is wasted. |

### Display

Each player's view shows two grids side by side, drawn with PRINT AT:

```
  YOUR SHIPS           YOUR SHOTS
  A B C D E F G H I J  A B C D E F G H I J
1 . . C C C C C . . . 1 . . . . . . . . . .
2 . . . . . . . . . . 2 . . · . . . . . . .
3 . B . . . . . . . . 3 . . . . X . . . . .
4 . B . . . D D D . . 4 . . . . . . · . . .
5 . B . . . . . . . . 5 . . . . . . . . . .
6 . B · . . . . . . . 6 . . . . . . . . . .
7 . . . . S . . . . . 7 . . . . . . . . . .
8 . . . . S . . X . . 8 . . . . . . . . . .
9 . P P . S . . . . . 9 . . . . . . . . . .
10. . . . . . . . . . 10. . . . . . . . . .

Player 1's turn. Enter target (e.g. D7):
```

The `·` marks are misses (shots that hit water). The `X` marks are hits. On the "Your Ships" grid, `X` marks where the opponent has hit your ships. Ships are shown with their letter (C, B, D, S, P).

### Visual Feedback

- **Hit:** FLASH 1 briefly on the hit cell. INVERSE 1 on the `X` marker. A sharp ascending BEEP.
- **Miss:** The `·` appears quietly. A low short BEEP.
- **Sunk:** The entire ship's cells change to INVERSE. "You sank the [name]!" appears. A descending BEEP sequence.

### Win Condition

A player wins when all 5 of the opponent's ships are sunk (all 17 ship cells hit). The game announces the winner, displays how many shots each player took, and offers a rematch.

---

## Phase Breakdown

### Phase 1: Grids, Ships and Shots (Units 1-16)

Build the grid display, ship placement with validation, and the core shot mechanic. By the end, two players can place ships and fire at each other, seeing hits and misses.

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|---------------|
| 1 | Four Arrays | DIM four 10×10 arrays: Player 1's ships, Player 1's tracking grid, Player 2's ships, Player 2's tracking grid. All start as 0 (water). | Parallel state, four 2D arrays, naming conventions |
| 2 | Drawing One Grid | A subroutine that draws a 10×10 grid using PRINT AT. Column headers A-J, row numbers 1-10. Each cell shows its contents: `.` for water, ship letter, `X` for hit, `·` for miss. | Grid display subroutine, parameterised drawing |
| 3 | Two Grids Side by Side | Display both "Your Ships" and "Your Shots" grids on the same screen. Calculate column offsets so they sit next to each other with a gap between. | Screen layout with offsets, dual-grid display |
| 4 | Grid Colours | Dark PAPER for water (blue or black), distinct INK colours for ships, hits, and misses. The grids look clean and readable. | Colour as information, PAPER/INK per cell type |
| 5 | Coordinate Input | INPUT a coordinate string like "D7". Parse the letter into a column (A=1, B=2... J=10) and the number into a row. Validate that both are in range. | Coordinate parsing, CODE conversion, range validation |
| 6 | Placing One Ship | Prompt for a starting coordinate and direction (H/V). Calculate which cells the ship occupies. Check that all cells are within the grid. Place the ship by writing its letter code into the array. | Ship placement logic, bounds checking |
| 7 | Overlap Detection | Before placing a ship, check that none of its cells are already occupied by another ship. Reject with "Ships cannot overlap" if any cell is taken. | Pre-placement validation, array scanning |
| 8 | Placement Display | After placing each ship, redraw the grid so the player can see where their ships are. Confirm each placement: "Carrier placed at B3 horizontal." | Visual confirmation, iterative placement |
| 9 | Full Fleet Placement | Loop through all 5 ships for one player. Prompt for each in order (largest first). Show the updated grid after each placement. All 5 ships on the board. | Iterative placement loop, ship data in arrays |
| 10 | The Handover | After Player 1 places their fleet, CLS and display "Pass the keyboard to Player 2. Press any key when ready." Player 2 then places their fleet. Neither player sees the other's grid. | Hidden information, screen clearing between players |
| 11 | Firing a Shot | On their turn, a player enters a target coordinate. The game checks the opponent's ship array at that position. Report "Hit!" or "Miss!" and update the tracking grid. | Shot resolution, cross-array lookup |
| 12 | Hit and Miss Markers | Write the result into the appropriate arrays. The tracking grid gets `X` for hit or `·` for miss. The opponent's ship grid gets a hit marker too (for display on their turn). | Dual-array update, consistent state |
| 13 | Already Fired Check | If the player fires at a coordinate they've already targeted, say "You already fired there" and let them try again. No wasted turn. | Duplicate detection, retry logic |
| 14 | Turn Flow | Full turn sequence: display current player's grids, prompt for shot, resolve, show result, pause, CLS, prompt for handover, display next player's grids. | Complete turn cycle, screen management |
| 15 | Shot Sound Effects | Hit: sharp ascending BEEP. Miss: low dull BEEP. Distinct and immediate — the player knows the result before reading the text. | Audio feedback, BEEP design |
| 16 | Playable Shots | Two players can place fleets, take alternating turns, fire shots, and see hits and misses on their tracking grids. The core game loop works. | Integration milestone, end-to-end play |

**Milestone:** A working two-player Battleships game with fleet placement (validated), shot mechanics, hit/miss tracking, and a turn-based handover system. Players can fire at each other and see results — but sunk detection, win conditions, and polish are still to come.

### Phase 2: Sinking, Winning and Polish (Units 17-32)

Add sunk detection per ship, the win condition, visual feedback, and all the polish that makes the game feel complete.

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|---------------|
| 17 | Ship Health Tracking | Each ship needs a hit counter. Use arrays to store how many cells each ship has and how many have been hit. When hits equal length, the ship is sunk. | Per-ship state tracking, parallel arrays for ship data |
| 18 | Which Ship Was Hit | When a shot hits, determine which ship occupies that cell. The ship array stores the ship's type code (1-5), so the hit counter for that specific ship increments. | Cell-to-ship mapping, type lookup |
| 19 | Sunk Detection | After each hit, check if that ship's hit count equals its length. If so, the ship is sunk. Display "You sank the [ship name]!" | Threshold comparison, ship name lookup |
| 20 | Sunk Display | When a ship is sunk, change all its cells on the tracking grid to a sunk marker (INVERSE text, or a different character). The player can see exactly which ships they've destroyed. | INVERSE for sunk ships, visual state change |
| 21 | Ships Remaining | Display a list below each grid showing which ships are still afloat and which are sunk. Strike through or dim the sunk ones. Both players can see their own fleet status. | Status panel, fleet summary display |
| 22 | Win Condition | After each shot, check if all 5 of the opponent's ships are sunk. If so, the game ends: "Player N wins!" Display the final boards (both players' ships revealed). | Win check, game end state, full reveal |
| 23 | Shot Counter | Track how many shots each player has taken. Display at game end: "Player 1 won in 43 shots." Fewer shots is more impressive. | Performance metric, turn counting |
| 24 | Direct Attribute POKE | Hit feedback using direct POKE to the attribute file (22528+) for speed. When a shot hits, a flash ripple races across the ship's cells — faster than PRINT AT could manage. When a ship sinks, colour drains cell by cell as the ship fades to black, with a descending tone. Every hit and miss is a dramatic event. | Direct attribute POKE (22528+), fast colour effects, visual drama |
| 25 | Sunk Fanfare | When a ship sinks, play a descending BEEP sequence — three or four notes dropping in pitch. The sunk ship's cells change to INVERSE. "You sank the [name]!" appears. More dramatic than a single BEEP. | Multi-note BEEP sequences, INVERSE for sunk ships, audio design |
| 26 | Win Celebration | The winner gets a full celebratory sequence: ascending BEEPs, FLASH on the winning message, both boards revealed showing all ships. The loser sees where their hidden ships were. FLASH and INVERSE carry information throughout — not decoration. | End-game presentation, board reveal, FLASH/INVERSE as information design |
| 27 | Input Robustness | Handle all bad input gracefully: too short, too long, letters out of range, numbers out of range, missing direction during placement, lowercase letters. Never crash, always explain. | Defensive input handling, string length checks |
| 28 | Placement Review | After placing all 5 ships, show the complete fleet and ask "Happy with this layout? (Y/N)". If no, clear the grid and start placement again. A chance to fix mistakes. | Confirmation step, grid reset |
| 29 | Rematch | After a game ends, offer "Play again? (Y/N)". If yes, clear all four arrays, reset all counters, and start fresh placement. No need to re-run the program. | Full game reset, replay loop |
| 30 | Grid Borders | Add border characters around both grids using `+`, `-`, and `|`. The grids look like proper game boards, not just floating characters. Clean, professional display. | Box drawing with PRINT AT, visual framing |
| 31 | Edge Case Testing | Test and fix: ships placed at grid edges, shots at corners, sinking the last ship on a multi-hit turn, placing all ships in one row, firing at every single cell. | Systematic testing, boundary conditions |
| 32 | The Finished Game | Clean the listing. Play a full game from start to finish — placement, shots, sinks, win. 300 lines of working strategy game with hidden information, four parallel arrays, and a polished two-player experience. | Code review, final integration, polish |

**Milestone:** A complete two-player Battleships game with validated ship placement, hit/miss/sunk detection, ship health tracking, win conditions, shot counters, visual feedback (FLASH, INVERSE), sound effects, rematch option, and robust input handling. Two people can play a full, satisfying game of Battleships.

---

## Technical Notes

### Array Structure

```
DIM s1(10,10)  - Player 1's ship grid
DIM t1(10,10)  - Player 1's tracking grid (shots fired)
DIM s2(10,10)  - Player 2's ship grid
DIM t2(10,10)  - Player 2's tracking grid (shots fired)
```

Ship grid values:
```
0 = water
1 = Carrier
2 = Battleship
3 = Destroyer
4 = Submarine
5 = Patrol boat
9 = hit (ship cell that's been hit)
```

Tracking grid values:
```
0 = unknown (not fired at)
1 = miss
2 = hit
3 = sunk
```

### Ship Data

```
DIM sl(5)  - ship lengths:  5, 4, 3, 3, 2
DIM sh(5)  - ship hit counts: starts at 0, increments on each hit
DIM sn$(5) - ship names stored in DATA: "CARRIER", "BATTLESHIP", etc.
```

Two sets needed — one per player (sl is shared since both fleets are identical).

### Key Variables

```
cp   - current player (1 or 2)
tc   - target column (parsed from input)
tr   - target row (parsed from input)
sc   - shots taken by current player
s1c  - Player 1's total shots
s2c  - Player 2's total shots
sk   - ships sunk count for opponent
```

### Grid Drawing

The draw subroutine takes a base column offset as a parameter. "Your Ships" draws at column 1, "Your Shots" draws at column 17 (or similar). The same subroutine draws both grids — the only difference is which array it reads and the column offset.

```basic
500 REM DRAW GRID
510 REM g = grid array base, ox = column offset
520 FOR r = 1 TO 10
530   FOR c = 1 TO 10
540     LET v = ... (read from appropriate array)
550     PRINT AT r+2, ox+c*2; ...
560   NEXT c
570 NEXT r
580 RETURN
```

Since Sinclair BASIC arrays can't be passed as parameters, the subroutine uses a flag variable to decide which array to read.

### Input Parsing

The coordinate "D7" is parsed as:
- `CODE a$(1) - CODE "A" + 1` → column (4)
- `VAL a$(2 TO LEN a$)` → row (7)

For two-digit rows (row 10), the string is 3 characters long. The VAL handles both "7" and "10" correctly.

### No ELSE

All branching uses `IF condition THEN GO TO line`. The validation chain for ship placement runs through several checks in sequence, each jumping to an error handler if the condition fails, or falling through to the next check.

### Screen Management

CLS between turns is essential — one player must never see the other's ships. The handover sequence:
1. Display shot result ("Hit!" or "Miss!")
2. PAUSE or "Press any key"
3. CLS (complete screen clear)
4. "Pass the keyboard to Player N. Press any key when ready."
5. Wait for keypress
6. CLS again
7. Draw the next player's grids

### Line Numbering

- 1-49: Initialisation, DIM arrays, ship data
- 50-99: Title screen, game setup
- 100-199: Ship placement (input, validation, placement loop)
- 200-249: Main game loop (turn flow, handover)
- 250-299: Shot input and parsing
- 300-349: Shot resolution (hit/miss/sunk)
- 350-399: Ship health and sunk detection
- 400-449: Win condition and end game
- 450-499: Grid drawing subroutine
- 500-549: Status display (ships remaining, shot count)
- 550-599: Sound effects
- 600-649: New game / reset
- 650-699: Input validation helpers
- 900-999: DATA (ship names, lengths)

### Memory

Four 10×10 arrays (400 numeric values), ship tracking arrays, and ~300 lines of BASIC. Total memory use is well within the 48K Spectrum's capacity.

---

## Changelog

- **v1.1 (2026-03-16):** Added direct attribute-file POKE for hit ripples and sunk colour drain (Unit 24). FLASH/INVERSE positioned as information design throughout. Per visual progression plan.
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
