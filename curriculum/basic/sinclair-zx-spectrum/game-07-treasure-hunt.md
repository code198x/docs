# Game 07: Treasure Hunt

**Track:** Spectrum BASIC
**Genre:** Grid collection game
**Units:** 16
**Language:** Sinclair BASIC
**Max lines:** ~60

---

## Premise

A treasure chamber. Gold coins scattered across a grid. A timer counting down. You have seconds to grab as many as you can — but the floor is trapped. Step on a hazard and you lose a life. Lose all three and the chamber seals forever.

Each level adds more hazards and less time. The coins are worth more as the danger grows. Clear every coin on a level and you earn a bonus before the next chamber opens. By level five the grid is more trap than treasure, and every step is a calculation.

This is the learner's first real-time game. Everything before this point — guessing games, quizzes, reaction timers — waited for the player. Treasure Hunt does not wait. The game loop runs continuously, reading the keyboard every tick, moving the character, checking for collisions, and counting down the timer whether the player is ready or not.

---

## Core Mechanics

### The Grid

The playing field is a 20×16 character-cell area displayed with PRINT AT. The top two rows are reserved for the HUD (score, lives, timer, level). The grid contains:

| Character | Meaning | INK colour |
|-----------|---------|------------|
| `@` | Player | White (7), BRIGHT |
| `o` | Coin | Yellow (6) |
| `#` | Hazard (spike trap) | Red (2) |
| `.` | Empty floor | Black (0) |

### Movement

QAOP keys. The player moves one cell per game-loop tick while a key is held. INKEY$ is polled every iteration — no blocking, no waiting. The old position is erased (printed as empty floor) and the new position is drawn.

Boundary checks prevent walking off the edge of the grid.

### Collision Detection

After moving, check what occupies the player's new cell:
- **Coin:** score increases, coin removed from grid, BEEP
- **Hazard:** lose a life, player resets to starting position, brief flash
- **Empty floor:** nothing happens

Collision is cell-based: if the player's row and column match a coin or hazard's row and column, that's a hit.

### Timer

A countdown timer displayed in the HUD. Decrements once per N loop iterations (tuned so one "second" feels roughly like one real second). When it reaches zero, the level ends — any remaining coins are lost.

### Lives

Three lives. Lose one on each hazard collision. Zero lives triggers game over. Lives shown as symbols in the HUD.

### Level Progression

After collecting all coins (or when the timer expires), the next level loads:
- More hazards placed on the grid
- Fewer seconds on the timer
- Each coin worth more points
- Player starts at a new position

Five levels. Completing all five shows a victory screen with the final score.

### Scoring

| Event | Points |
|-------|--------|
| Coin collected | 10 × level number |
| All coins cleared (bonus) | 50 × level number |
| Level completed (any coins remaining) | 0 bonus |

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | The Grid | Draw a 20×16 grid of dots using nested FOR/NEXT loops and PRINT AT. Place a single `@` character on the grid. The screen looks like a game board. | Formal game loop concept (introduced, not yet running), screen as a grid |
| 2 | Reading the Keyboard | Add an INKEY$ check inside a GO TO loop. Press Q/A/O/P and print which key was detected at the bottom of the screen. The loop runs continuously — the program never stops to wait. | INKEY$ polling in a loop, non-blocking input, continuous execution |
| 3 | Moving the Player | Connect INKEY$ to the player's position. Press a key, the `@` moves one cell. Old position erased with a space, new position drawn with `@`. The character slides around the grid. | Erase-old-draw-new pattern, position variables (row, column), updating position with LET |
| 4 | Boundary Checks | Stop the player walking off the edge. IF the new row is less than 2 (the HUD) or greater than 21, don't move. Same for columns 0 and 31. | Boundary conditions, guarding movement with IF/THEN |
| 5 | Placing Coins | Use a FOR loop and RND to scatter 10 coins (`o` in yellow INK) across the grid at random positions. Avoid placing them on the player's starting cell. | Random placement, avoiding overlap, INK with PRINT AT |
| 6 | Collecting Coins | After the player moves, check if the new cell contains a coin. If yes: add to score, BEEP, and the coin vanishes (replaced by empty floor). A counter tracks coins remaining. | Cell-based collision detection, score variable, counting items |
| 7 | The Score Display | Print the score at the top of the screen: `SCORE: 0040`. Update it each time a coin is collected. Use PRINT AT row 0 to keep the HUD in a fixed position. | HUD display, formatted number output, PRINT AT for status |
| 8 | Placing Hazards | Scatter hazard characters (`#` in red INK) across the grid alongside the coins. Hazards don't move — they just sit there, waiting. Five hazards on level one. | Multiple object types on the grid, visual distinction with colour |
| 9 | Losing a Life | Walk onto a hazard: BEEP (low tone), flash the border red, lose one life, reset the player to the starting position. Lives display in the HUD decreases. | Life counter, reset-on-death, BORDER flash for feedback |
| 10 | Game Over | Zero lives: clear the screen, print "GAME OVER" and the final score. Wait for a keypress, then restart. The game has stakes now — hazards matter. | Game over state, end screen, restart flow |
| 11 | The Timer | A countdown number in the HUD. Decrements once per N iterations of the game loop. When it hits zero, the level ends regardless of remaining coins. | Timer variable, decrement per N ticks, time pressure |
| 12 | Level Complete | All coins collected (or timer expired): brief "LEVEL COMPLETE" message with bonus points if all coins were grabbed. Then the next level loads. | Level transition, bonus scoring, state change between levels |
| 13 | Level Progression | Five levels, each harder. More hazards, fewer seconds, higher coin value. Level data stored in variables that change at each transition — no DATA statements needed for this. | Difficulty scaling, variables as level parameters |
| 14 | PEEK Timing | The game speed varies depending on how many coins and hazards are on screen. Fix it: `PEEK 23672` reads the Spectrum's frames counter. Wait until the counter changes before processing the next loop iteration. Now movement is consistent — smooth and predictable regardless of screen content. | `PEEK` 23672 (frames counter), consistent game speed, hardware access |
| 15 | Screen Transitions | Between levels, the screen doesn't just CLS — colour drains away. POKE to the attribute file (22528+) row by row, setting each character cell to PAPER 0 / INK 0. The level fades to black before the new one appears. Coins glitter with FLASH. Hazards pulse with alternating INK. Sound polish: coin collect, hazard hit, level complete, game over. | Attribute-file POKE (22528+), screen transitions, FLASH for items, sound design |
| 16 | The Finished Game | Play through all five levels. Fix any bugs. Verify scoring, lives, timer, level transitions. Clean up the listing — consistent line numbering, REM comments for each section. A complete, playable, real-time game in ~60 lines. | Integration testing, code tidying, the complete game loop |

**Milestone:** The learner has built their first real-time game and touched the hardware directly. They understand the game loop (input, update, draw), INKEY$ polling, erase-and-redraw movement, collision detection, PEEK timing for consistent speed, and attribute-file POKE for atmospheric screen transitions. The game *feels* smooth because it *is* timed.

---

## Technical Notes

### Game Loop Structure

```
Main loop (line 100):
  1. LET k$ = INKEY$
  2. IF k$ = "q" THEN move up (row - 1)
     IF k$ = "a" THEN move down (row + 1)
     IF k$ = "o" THEN move left (col - 1)
     IF k$ = "p" THEN move right (col + 1)
  3. Boundary check (don't move if out of range)
  4. GO SUB 500: erase old position, draw new position
  5. GO SUB 600: check collision (coin or hazard)
  6. GO SUB 700: update HUD (score, lives, timer)
  7. Decrement timer counter
  8. IF timer = 0 THEN level end
  9. IF coins = 0 THEN level complete
  10. GO TO 100
```

### Key Variables

```
r   - player row (2-21)
c   - player column (0-31)
s   - score
lv  - lives (starts at 3)
tm  - timer (counts down)
cn  - coins remaining on this level
ln  - current level number (1-5)
k$  - last key pressed
```

### Line Numbering

- 1-49: Initialisation, grid drawing, coin and hazard placement
- 50-99: Level setup (set timer, hazard count, coin value per level)
- 100-199: Main game loop
- 200-299: Level complete / game over screens
- 500-599: Draw subroutine (erase old, draw new)
- 600-699: Collision subroutine (coin or hazard check)
- 700-799: HUD update subroutine

### No ELSE on the 48K

The Spectrum 48K has no ELSE keyword. Every decision is a standalone IF/THEN. To handle mutually exclusive cases (coin vs hazard vs empty floor), use sequential IF/THEN lines — each checks independently. Since the player can only be on one cell, only one condition fires per tick.

### Coin and Hazard Placement

Coins and hazards are placed directly on screen with PRINT AT. There is no backing array — the screen IS the game state. To check what's at a position, the code reads the screen using SCREEN$ (which returns the character at a given row/column) or compares the player's position against a list of known hazard positions.

For ~60 lines, the simpler approach is to track coin and hazard positions in short arrays (DIM h(20,2) for hazards, DIM g(20,2) for coins) and compare against the player's position each tick.

### Memory and Performance

At ~60 lines with no UDGs or graphics commands, the program is tiny (~2-3 KB). Performance is not a concern — the game loop runs faster than the player can react. If anything, a short PAUSE may be needed to prevent the character moving too quickly.

---

## Changelog

- **v1.1 (2026-03-16):** Added PEEK 23672 timing (Unit 14) and attribute-file POKE screen transitions (Unit 15). Removed GO SUB introduction (now in Game 6). Per visual progression plan.
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
