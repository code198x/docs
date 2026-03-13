# Game 10: Night Patrol

**Track:** Spectrum BASIC
**Genre:** Top-down stealth game
**Units:** 16
**Language:** Sinclair BASIC
**Max lines:** ~100

---

## Premise

The name is ironic. Night Patrol is what the guards are doing. You're the reason they're doing it.

You break into a building after dark. Guards walk fixed patrol routes through the corridors. You can see them moving — torchlight bobbing in the gloom — but they can't see you unless you step into their line of sight. Reach the objective on each floor, then reach the exit. Five floors, each harder: more guards, tighter routes, longer sightlines.

The game looks and feels like a magazine type-in from Crash or Sinclair User: PRINT AT characters on a grid, simple but tense, "just one more go" addictive. BASIC's speed is an asset here — this isn't twitch action, it's pattern reading and timing. Watch the guards, find the gap, move.

---

## Core Mechanics

### The Grid

Each floor is a character-cell grid (28×18 usable area, with 2 rows reserved for the HUD at the bottom). Walls, floors, and objectives are all characters placed with PRINT AT.

| Character | Meaning | INK colour |
|-----------|---------|------------|
| Block (CHR$ 143) | Wall | Blue (1) |
| Space | Floor (walkable) | Black (0) |
| Player (○ or similar) | The intruder | White (7) |
| Guard (● or similar) | Patrol guard | Red (2) |
| Sightline (·) | Detection zone | Red (2) |
| Objective (★) | Target item | Yellow (6) |
| Exit (↑) | Level exit | Green (4) |

### Movement

The player moves one character cell per keypress. QAOP controls. Movement is grid-locked. The player cannot move through walls. Walking onto the exit with the objective collected completes the floor.

### Guards

Guards follow fixed patrol routes defined as sequences of directions and step counts, stored alongside the map data:

```
Guard 1: E4, S2, W4, N2 (rectangle patrol)
Guard 2: S6, N6 (corridor pace)
```

Each guard moves one step per N game-loop ticks. Guards cycle their route endlessly. They don't react to the player — they're predictable. The challenge is reading and exploiting the pattern.

### Detection and Sightlines

Each guard has a sightline: a straight line extending in the direction they're currently facing, until it hits a wall. Sightlines are visible on screen as dots, so the player always knows where danger is. Step into a sightline and you're caught.

On detection: alarm BEEP, border flashes red, lose a life, reset to the floor's start position. Guards also reset.

### Floor Progression

| Floor | Guards | Patrol speed | Layout | New element |
|-------|--------|-------------|--------|-------------|
| 1 | 1 | Slow | Simple L-corridor | Learn movement and sightlines |
| 2 | 2 | Slow | T-junction | Two guards, timing windows |
| 3 | 2 | Medium | Loop corridor | Guards in opposite directions |
| 4 | 3 | Medium | Open room with pillars | Sightline blocking |
| 5 | 3 | Fast | Multi-room | Everything combined |

### Scoring

| Event | Points |
|-------|--------|
| Completing a floor | 100 × floor number |
| Collecting the objective | 50 |

Lives: 3. No extra lives. Game over shows final score and floor reached.

### Controls

| Key | Action |
|-----|--------|
| Q | Up |
| A | Down |
| O | Left |
| P | Right |

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | The Dark Building | Title screen: "NIGHT PATROL" in white on black. Set INK, PAPER, BORDER to black. Atmospheric BEEP. "Press any key" to start. | Setting the mood with colour and sound, screen as atmosphere |
| 2 | Map Data | Define floor 1 as a string array: DIM m$(18,28). Each element is one row of the map. Read from DATA statements — "#" for wall, " " for floor. Print the map to verify it loaded. | String arrays as 2D map storage, DATA for level layout, reading strings character by character |
| 3 | Drawing the Map | Loop through the map array and PRINT AT each character. Walls in blue INK using CHR$ 143, floors as spaces. The building appears on screen, drawn from data rather than hardcoded PRINT AT statements. | Drawing a map from data, nested loops (row and column), INK per character type |
| 4 | The Intruder | Place a player character on screen. Player start position read from DATA after the map rows. QAOP moves the player one cell per keypress with erase-and-redraw. | Player position from data, combining map drawing with player drawing |
| 5 | Wall Collisions | Before moving, check if the target cell contains a wall. Read the map array at the target position: IF m$(ny)(nx TO nx) = "#" THEN don't move. The player slides along walls, never through them. | Collision detection against map data, look-before-move with string indexing |
| 6 | A Stationary Guard | One guard on floor 1, drawn in red INK. Guard position read from DATA. If the player walks onto the guard's cell, detection triggers: alarm BEEP, border flashes, "DETECTED!" message. | Enemy as data, simple same-cell collision |
| 7 | Guard Movement | The guard moves along a patrol route stored as a string in DATA: "E4S2W4N2" means 4 east, 2 south, 4 west, 2 north. Parse the route: read direction letter, read step count digit. Guard moves one step per N ticks, cycling the route endlessly. | Simple AI from data, string parsing for direction and count, tick-based NPC movement |
| 8 | Sightlines | Draw the guard's sightline: a line of dots extending from the guard in its facing direction until hitting a wall. Check the map array for each cell along the line. If the player occupies any sightline cell, detection triggers. | Line-of-sight calculation, iterating along a direction, detection as line intersection |
| 9 | Lives and Game Over | Three lives. On detection: lose a life, reset player and guard to starting positions. Lose all three: game over screen with final score. Display lives in the HUD (bottom two rows). | Life counter, state reset, game over condition |
| 10 | The Objective and Exit | Place an objective (★) and exit (↑) on the floor, positions from DATA. Collect the objective by walking over it. Exit only opens once the objective is collected. Floor complete: score awarded, congratulations message. | Multi-step win condition, objective as gate for exit |
| 11 | Two Guards | Floor 1 stays at one guard. Load a second floor from DATA with two guards. After completing floor 1, RESTORE to floor 2's DATA line and load the new map, guards, and positions. Two guards with independent routes and sightlines. | Multiple enemies (arrays for guard positions), RESTORE to specific line for level loading |
| 12 | Five Floors | All five floors defined in DATA. Each floor has its own map, guard count, guard routes, objective position, exit position, and player start. Floor number displayed in the HUD. Difficulty increases through guard count and patrol speed. | Level data in DATA blocks, RESTORE for each level, difficulty as data |
| 13 | Sightline Polish | Erase old sightlines before drawing new ones when a guard turns a corner. Track the previous sightline cells so they can be cleared cleanly. Sightlines stop at walls AND at other guards (guards block line of sight). | Cleanup on state change, tracking previous positions, interaction between game objects |
| 14 | Detection Drama | On detection: guard turns to face the player, exclamation mark appears above the guard, two-tone alarm BEEP, border flashes red twice, brief pause, then reset. Make it feel dramatic, not frustrating. The player always knows why they were caught. | Sequential animation, sound design, feedback pacing |
| 15 | Victory and Polish | Complete all five floors: "YOU ESCAPED!" with ascending BEEP fanfare and final score. Title screen gets a building silhouette in block characters. Floor intro text before each level: "Floor 3: The Loop — two guards patrol in opposite directions." Border colour changes per floor. | End game sequence, inter-level narrative, visual polish |
| 16 | The Finished Game | Play all five floors in sequence. Is every floor solvable? Is the difficulty curve fair? Test edge cases: guard walks over the objective (objective reappears when guard passes), player stands still while guard's sightline sweeps over them. Clean the listing. ~100 lines of working, tested code. | Full integration testing, edge cases, the finished product |

**Milestone:** The learner can store map layouts as string data, draw a world from that data, implement simple patrol-route AI, manage multiple enemies with arrays, and load different levels using RESTORE. These skills — data-driven maps, enemy AI, and level loading — are the foundation for every game that needs a world larger than one screen.

---

## Technical Notes

### Data Structures

```
DIM m$(18,28)   - map rows: 18 strings of 28 characters each
DIM gx(3)       - guard X positions (up to 3 guards)
DIM gy(3)       - guard Y positions
DIM gdx(3)      - guard current direction X (-1, 0, 1)
DIM gdy(3)      - guard current direction Y (-1, 0, 1)
DIM gr$(3,16)   - guard patrol route strings
DIM gs(3)       - current position within route string
DIM gc(3)       - steps remaining in current direction
```

### Map Data Format

Each floor is stored as a block of DATA statements:

```basic
5000 DATA "############################"
5010 DATA "#      #        #          #"
5020 DATA "#      #        #          #"
...
5170 DATA "############################"
5180 DATA 1
5190 DATA 10, 5, "E4S2W4N2"
5200 DATA 14, 3
5210 DATA 2, 16
5220 DATA 2, 2
5230 DATA 8
```

After the 18 map rows: guard count, guard data (x, y, route per guard), objective position, exit position, player start position, and patrol speed (ticks between guard moves — lower is faster).

### Sightline Calculation

For each guard, extend a line from their position in their facing direction:

```basic
500 REM DRAW SIGHTLINE FOR GUARD g
510 LET sx = gx(g): LET sy = gy(g)
520 LET dx = gdx(g): LET dy = gdy(g)
530 FOR i = 1 TO 20
540   LET sx = sx + dx: LET sy = sy + dy
550   IF sx < 1 OR sx > 28 OR sy < 1 OR sy > 18 THEN GO TO 590
560   IF m$(sy)(sx TO sx) = "#" THEN GO TO 590
570   PRINT AT sy, sx; INK 2; "."
575   IF sx = px AND sy = py THEN LET detected = 1
580 NEXT i
590 RETURN
```

Before drawing a new sightline, erase the old one by reprinting the floor character (space) over the previous dots. This is the most involved piece of code in the game — but it's just a FOR loop with PRINT AT.

### Route Parsing

A patrol route like "E4S2W4N2" is read two characters at a time: a direction letter and a step count digit. When the guard exhausts its steps in one direction, it reads the next pair. At the end of the string, it wraps to the start.

```basic
550 LET d$ = gr$(g)(gs(g) TO gs(g))
560 LET gc(g) = VAL gr$(g)(gs(g)+1 TO gs(g)+1)
570 IF d$ = "N" THEN LET gdx(g) = 0: LET gdy(g) = -1
580 IF d$ = "S" THEN LET gdx(g) = 0: LET gdy(g) = 1
590 IF d$ = "E" THEN LET gdx(g) = 1: LET gdy(g) = 0
600 IF d$ = "W" THEN LET gdx(g) = -1: LET gdy(g) = 0
610 LET gs(g) = gs(g) + 2
620 IF gs(g) > LEN gr$(g) THEN LET gs(g) = 1
```

### Game Loop

```
Main loop:
  1. Read input (INKEY$)
  2. Move player (if valid move)
  3. Check player vs sightlines
  4. Increment guard tick counter
  5. If guard tick: move all guards, update sightlines
  6. Check sightlines vs player again (guard moved toward player)
  7. Check objective collection
  8. Check exit condition
  9. Update HUD
  10. GO TO main loop
```

Detection is checked twice per loop: after the player moves (stepped into a sightline?) and after guards move (sightline swept over the player?).

### Line Numbering

- 1-49: Initialisation, DIM arrays, colour setup
- 50-99: Title screen, floor intro text
- 100-199: Floor loading (RESTORE, READ map and guard data, draw floor)
- 200-299: Main game loop
- 300-399: Player movement and collision
- 400-499: Guard movement and route parsing
- 500-599: Sightline drawing and detection
- 600-699: Detection response, lives, game over
- 700-799: HUD, score, floor complete, victory
- 5000+: Floor DATA (5 floors)

### Memory and Performance

Five floors of map data (5 × 18 rows × 28 chars = ~2.5 KB) plus guard routes and game logic fit comfortably in 48K. The sightline calculation runs only when guards move — with 1-3 guards and sightlines of ~10-15 cells, that's 30-45 ATTR checks per guard tick. Fast enough.

BEEP blocks the program. Keep all BEEPs very short (0.05 seconds) except during detection drama and victory, where the pause is intentional.

---

## Changelog

- **v1.0 (2026-03-13):** Adapted from Game 02 (v4.0, 64 units) to Game 10 (v5.0, 16 units). Compressed from 8 floors to 5. Removed fog of war, difficulty select, doors, bonus collectibles, par times, high score tracking, and minimap. Retained the core stealth loop: map from data, visible sightlines, patrol-route AI, pattern reading.
