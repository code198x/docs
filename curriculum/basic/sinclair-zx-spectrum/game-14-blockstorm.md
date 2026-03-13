# Game 14: Blockstorm

**Track:** Spectrum BASIC
**Genre:** Vertical shooter with UDG graphics
**Units:** 32 (2 phases × 16 units)
**Language:** Sinclair BASIC
**Max lines:** ~400

---

## Premise

Alien blocks descend from the sky in waves. You fire upward. They explode. More come. Faster. In tighter formations.

Blockstorm is a vertical shooter built entirely with user-defined graphics — custom 8×8 characters that replace the Spectrum's built-in set. The player's ship, every enemy type, bullets, explosions, and power-ups are all UDGs placed with PRINT AT. The game looks like a real Spectrum arcade conversion, not a text-mode demo.

It's also the game where BASIC breaks. The first few waves are smooth. By wave 6, the screen is full of moving objects and the frame rate visibly drops. By wave 10, the player can feel the interpreter gasping. This is not a bug — it's the lesson. The learner has pushed BASIC to its absolute limit. They understand viscerally why assembly exists.

---

## Core Mechanics

### The Player

A ship at the bottom of the screen, moving left and right. Fires upward. One bullet on screen at a time (upgradeable to two with the double-shot power-up).

| Control | Key |
|---------|-----|
| Left | O |
| Right | P |
| Fire | SPACE |

The ship occupies one character cell and is drawn as a UDG: a recognisable spaceship shape in 8×8 pixels.

### Enemies

Enemies descend from the top of the screen. They move in formation patterns: rows that shift left and right, V-formations that dive, columns that snake. Each wave has a pattern.

| Type | UDG | Colour | Behaviour | Points | Hits |
|------|-----|--------|-----------|--------|------|
| Drone | A | Green (4) | Moves with formation | 10 | 1 |
| Scout | B | Cyan (5) | Breaks from formation, dives | 25 | 1 |
| Tank | C | Yellow (6) | Slow, absorbs hits | 50 | 2 |
| Bomber | D | Magenta (3) | Drops projectiles downward | 30 | 1 |

Four enemy types, each a different UDG. No bosses — the difficulty comes from density and speed, not spectacle.

### Bullets

Player bullet: a single character (UDG E, a small arrow or dot) moving upward one cell per game tick. One on screen at a time (base). The double-shot power-up allows two simultaneous bullets.

Enemy bombs (from Bombers): fall downward one cell per N ticks. Hit the player = lose a life.

### Collisions

All collision is character-cell based. Before moving a bullet upward, check if the target cell contains an enemy (position comparison against enemy arrays). If yes: hit. Before moving an enemy downward, check if the target cell contains the player. If yes: death.

### Explosions

When an enemy is destroyed, replace its UDG with an explosion UDG (F: a starburst shape) in red INK. The explosion persists for 2-3 game ticks, then disappears. Simple but satisfying.

For multi-hit enemies (Tank), show a damage flash — briefly change INK to white then back — before the final explosion.

### Power-Ups

Occasionally a destroyed enemy drops a power-up (falls downward like a bomb, but collectible):

| Power-up | UDG | Colour | Effect |
|----------|-----|--------|--------|
| Double shot | G | Cyan (5) | Two bullets on screen simultaneously |
| Shield | H | Yellow (6) | Absorb one hit without dying |

Two power-ups only. Power-ups disappear if they reach the bottom without being collected. Only one active power-up at a time.

### Scoring

| Event | Points |
|-------|--------|
| Drone destroyed | 10 |
| Scout destroyed | 25 |
| Bomber destroyed | 30 |
| Tank destroyed | 50 |
| Wave clear bonus | 50 × wave number |

Lives: 3. Extra life at 2,000 points (one only).

---

## Wave Design

The game has 10 waves. Each wave is a formation of enemies that must be entirely destroyed before the next wave begins. Waves get progressively harder: more enemies, faster movement, new enemy types, tighter formations.

| Wave | Enemies | Types | Speed | Pattern | New element |
|------|---------|-------|-------|---------|-------------|
| 1 | 8 | Drones only | Slow | Single row, shift L/R | Learn to aim |
| 2 | 10 | Drones | Slow | Two rows | More targets |
| 3 | 10 | Drones + 2 Scouts | Slow | Row + divers | Scouts break formation |
| 4 | 12 | Mixed | Medium | V-formation | Formation patterns |
| 5 | 12 | Mixed + 1 Tank | Medium | Row with Tank centre | Multi-hit enemies |
| 6 | 14 | Mixed + Bombers | Medium | Row + bomber support | Dodge bombs while shooting |
| 7 | 14 | All types | Fast | Two V-formations | Denser screen |
| 8 | 16 | All types | Fast | Snaking column | Speed increase |
| 9 | 18 | All types | Fast | Complex formation | Everything combined |
| 10 | 20 | All types | Very fast | Dense grid | BASIC at its limit |

### Wave Data

Each wave is stored as DATA:

```
DATA 10, 2, 3
DATA "AAAAAAAAAA"
DATA "..BBBB...."
DATA "E4S2W4"
```

- Line 1: enemy count, rows, speed (ticks per enemy move)
- Lines 2+: formation layout (characters = enemy types, dots = empty)
- Final line: formation movement pattern (E=east, W=west, S=south, number=repeat)

### Formation Movement

Formations move as a unit. The pattern string defines the group's movement:
- "E4S1W4S1" = shift right 4, descend 1, shift left 4, descend 1 (Space Invaders pattern)
- When the formation descends to the player's row, game over regardless of lives — they've invaded.

Individual enemies (Scouts) can break from the formation and dive — they follow their own path once detached.

---

## Visual Design

### Screen Layout

```
 SCORE: 0450  HI: 1200  LIVES: ♦♦♦  WAVE 5
╔══════════════════════════════════╗
║    ░ ░ ░ ░ ░ ░ ░ ░              ║  ← enemy formation
║      ░ ░ ░ ░ ░ ░                ║
║          ▼                       ║  ← scout diving
║                                  ║
║              ·                   ║  ← enemy bomb falling
║                                  ║
║          ↑                       ║  ← player bullet
║              ▲                   ║  ← player ship
╚══════════════════════════════════╝
```

### UDG Allocation

14 UDGs used (A-N). Allocation:

| UDG | Purpose |
|-----|---------|
| A | Drone — blocky alien shape |
| B | Scout — pointed, aggressive dive shape |
| C | Tank — heavy, wide, armoured |
| D | Bomber — distinctive, bomb bay visual |
| E | Player bullet — small upward arrow |
| F | Explosion — starburst |
| G | Power-up: double shot |
| H | Power-up: shield |
| I | Player ship — arrow/wedge pointing up |
| J | Enemy bomb — small downward arrow |
| K | Explosion frame 2 — expanding fragments |
| L | Shield indicator (HUD) |
| M | Drone animation frame 2 |
| N | Scout animation frame 2 |

### UDG Definition

Each UDG is 8 bytes, defined via BIN:

```basic
10 REM PLAYER SHIP (UDG "I")
20 FOR i = 0 TO 7
30   READ b
40   POKE USR "I" + i, b
50 NEXT i
60 DATA BIN 00010000
70 DATA BIN 00111000
80 DATA BIN 00111000
90 DATA BIN 01111100
100 DATA BIN 11111110
110 DATA BIN 11111110
120 DATA BIN 10000010
130 DATA BIN 00000000
```

### Colours

| Element | INK | Notes |
|---------|-----|-------|
| Background | Black (0) | Space |
| Player ship | White (7) | Stands out against everything |
| Player bullet | White (7) | Fast, bright |
| Drone | Green (4) | Common, non-threatening colour |
| Scout | Cyan (5) | Cool, fast |
| Tank | Yellow (6) | Warning colour, tough |
| Bomber | Magenta (3) | Distinctive, dangerous |
| Explosions | Red (2) then Yellow (6) | Two-frame colour shift |
| Power-ups | FLASH 1 | Attract attention |
| Enemy bombs | Red (2) | Danger |
| HUD | White (7), BRIGHT | Clear, readable |

---

## Phase Breakdown

### Phase 1: Ship, Bullets, and First Contact (Units 1-16)

Build the UDG system, the player ship, bullets, and the first enemies. By the end of this phase, the learner has a playable shooter with one enemy type and basic collision.

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|---------------|
| 1 | Custom Characters | Title screen: "BLOCKSTORM" in PRINT AT. Then define one UDG using POKE USR and BIN. Display it with PRINT AT. It's a custom character — not from the built-in set. | USR, POKE, BIN, UDG concept |
| 2 | Designing UDGs | Graph paper to binary: sketch an 8×8 sprite, convert each row to BIN, POKE them into memory. Design the player ship (UDG "I"). | UDG design workflow, binary representation of pixels |
| 3 | The Ship | Display the player ship UDG near the bottom of the screen. White INK on black PAPER. It looks like a real game sprite. Define the bullet UDG too. | PRINT AT with UDG characters, INK for UDGs |
| 4 | Movement and Firing | O/P keys move the ship left and right. Erase old position, draw new. Boundary checks. SPACE fires a bullet UDG that moves upward one cell per tick. | Erase-redraw pattern, bullet state (active flag, position) |
| 5 | One Bullet Rule | Only one bullet on screen at a time. The bullet moves upward each tick and disappears at the top. Fire again after it's gone. | Resource management, single-instance constraint |
| 6 | Multiple UDGs | Define all UDGs in a setup routine at program start. Ship, bullet, explosion, enemies — batch POKE with a FOR/NEXT loop reading DATA. | Batch UDG definition, DATA for multiple 8-byte shapes |
| 7 | The HUD | Score, high score, lives, wave number across the top row. PRINT AT with BRIGHT 1 to distinguish from the game area. Lives shown as ship UDGs. | HUD layout, formatted number display, UDGs in HUD |
| 8 | One Drone | A single drone UDG on screen. Static. Bullet hits it — compare positions. Hit: replace with explosion UDG in red, wait 2 ticks, clear. Score increases. | Position-based collision detection, explosion display |
| 9 | Explosion Animation | Two-frame explosions: starburst (UDG F) in red, then fragments (UDG K) in yellow, then clear. Timed with a counter variable. | Two-frame animation, timed replacement, counter variables |
| 10 | A Row of Drones | Eight drones in a row. Track each with arrays: `ex()` for x-position, `ea()` for alive flag. Bullet hits any one — that one explodes. Others remain. | Enemy arrays, individual state tracking per enemy |
| 11 | Formation Movement | The row shifts left and right as a unit. A formation offset variable moves all living enemies together. Bounce at screen edges. | Group movement via shared offset, direction reversal |
| 12 | Formation Descent | When the formation reaches a screen edge, it descends one row and reverses direction. Classic Space Invaders pattern. If it reaches the player's row: game over. | Descent trigger, invasion fail condition |
| 13 | Sound Effects | Fire: short high BEEP. Explosion: descending tone burst. Keep durations minimal — long BEEPs freeze the game loop. | BEEP with minimal duration, performance-aware sound |
| 14 | Lives and Death | Enemy reaches the player's row or bomb hits the ship: lose a life. Ship explosion animation, brief pause, respawn. Zero lives: game over with final score. | Player death, respawn, life management, game over state |
| 15 | Game Loop Structure | Formalise the loop: input → move player → move bullet → move enemies → check collisions → update HUD → loop. GO SUB for each section. | Game architecture, GO SUB structure for a real-time game |
| 16 | Playable Prototype | One wave of drones, formation movement, shooting, explosions, lives, score, game over. A real shooter, if a simple one. Polish the feel: movement speed, bullet speed, collision reliability. | Integration milestone, feel tuning |

**Milestone:** A playable vertical shooter with UDG graphics, one enemy type in formation, explosions, lives, scoring, and game over. The UDGs look like real sprites. The game feels like a game.

### Phase 2: The Full Assault (Units 17-32)

Multiple enemy types, 10 waves, power-ups, optimisation, and the honest performance lesson.

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|---------------|
| 17 | Scout Behaviour | Scouts (UDG B) break from formation and dive toward the player. Independent movement after detaching. Cyan INK. Hit detection works during the dive. | Individual enemy AI, state switch (in-formation vs diving) |
| 18 | Tank and Bomber | Tank (UDG C): yellow, takes 2 hits — damage flash on first hit, explosion on second. Bomber (UDG D): magenta, periodically drops a bomb UDG that falls downward. | Multi-hit enemies, hit counter per enemy, enemy projectiles |
| 19 | Bomb Collision | Falling bombs hit the player: lose a life. Bombs hit the bottom: disappear. Track bombs in a small array (max 3 active). Player must dodge while shooting. | Bullet pool for enemy projectiles, dual threat |
| 20 | Wave Data | Move formation layouts into DATA statements. Each wave: enemy count, row count, speed, layout string, movement pattern. READ at wave start, place enemies from the data. | DATA-driven level design, formation from strings |
| 21 | Waves 1-5 | Design and enter 5 complete waves with escalating difficulty. Drones only → mixed types → bombers. Test each one for feel and fairness. | Level design, difficulty curve, playtesting |
| 22 | Wave Clear and Progression | All enemies destroyed: "WAVE COMPLETE" message, bonus points (50 × wave number), brief pause, load next wave from DATA. RESTORE to the correct line for each wave. | Wave completion detection, RESTORE to specific DATA line |
| 23 | Power-Up: Double Shot | Destroyed enemies occasionally drop a double-shot power-up (UDG G, FLASH 1). Collect it: two bullets on screen simultaneously. Manage two bullet positions and two collision checks. | Random drops, multiple active bullets, expanded bullet state |
| 24 | Power-Up: Shield | Shield power-up (UDG H, FLASH 1). Collect it: absorb one hit without dying. Shield indicator UDG shown in the HUD. Consumed on the next hit instead of losing a life. | Defensive power-up, HUD state indicator |
| 25 | Enemy Animation | Drones and Scouts alternate between two UDG frames every few ticks. The formation looks alive, not static. Swap UDG characters in the PRINT AT call based on a frame counter. | Animation via UDG frame cycling, frame counter |
| 26 | Waves 6-10 | Design waves 6-10. All enemy types, faster movement, denser formations. Wave 10 has 20 enemies and BASIC is visibly struggling. The frame rate drops. | Late-game level design, encountering performance limits |
| 27 | The Performance Wall | With 20 enemies, bombs, bullets, and the player all moving, the game loop slows noticeably. Use PEEK 23672 (the system variable for frame count) to measure the loop time. Document the numbers: wave 1 vs wave 10. | PEEK for timing, performance measurement, bottleneck awareness |
| 28 | Optimisation Pass | Speed up the critical path. Shorter variable names (`a` not `score`). Move frequently called GO SUBs to low line numbers (the interpreter searches from line 1). Avoid unnecessary PRINT AT calls — only redraw what changed. Measure the improvement. | Short variable names, GO SUB placement, selective redraw, integer tricks |
| 29 | Extra Life and Invasion | Award one extra life at 2,000 points — BEEP fanfare, new life appears in HUD. One only. If the formation descends to the player's row: "INVADED!" and instant game over regardless of lives. | Threshold bonus, one-shot trigger, invasion fail state |
| 30 | High Score Table | Game over: if the score beats the high score, prompt for 3 initials. Store top 3 scores in arrays. Display the table: rank, initials, score. Session only — lost on reset. | Name entry, array sorting, formatted table display |
| 31 | The Limits of BASIC | A reflective unit. The learner measures loop time at wave 1 (fast) and wave 10 (slow). They calculate why: each PRINT AT takes time, each variable lookup is a linear search, each GO SUB scans from line 1. The same game in assembly would run at 50fps with 100 enemies. This is why the assembly track exists. | Performance analysis, interpreter overhead, bridge to assembly |
| 32 | The Finished Game | Clean listing. Title screen, 10 waves, 4 enemy types, 2 power-ups, explosions, formation movement, diving scouts, bombing runs, high score table. Under 400 lines. The Spectrum BASIC track's peak — and its honest ending. | Code review, final integration, completion |

**Milestone:** A complete vertical shooter with 10 waves, 4 enemy types, 2 power-ups, diving scouts, bombing runs, formation patterns, a high score table, and the measured, documented performance ceiling that makes assembly necessary. Would fill two pages of a magazine listing.

---

## Technical Notes

### Game Loop

```
Main loop:
  1. Read input (INKEY$)
  2. Move player
  3. Move player bullet(s)
  4. Check bullet-enemy collisions
  5. Increment enemy tick counter
  6. If enemy tick: move formation, move individual enemies (scouts, bombs)
  7. Check enemy-player collisions (bombs hitting player, formation reaching bottom)
  8. Handle explosions (decrement timers, clear expired)
  9. Handle power-up drops and collection
  10. Update HUD (score, lives)
  11. Check wave clear
  12. GO TO main loop
```

### Enemy State Arrays

```
ex()  - enemy X position (offset from formation base)
ey()  - enemy Y position (offset from formation base)
et()  - enemy type (0=empty, 1=drone, 2=scout, 3=tank, 4=bomber)
eh()  - enemy hit points remaining
ea()  - enemy state (0=dead, 1=in formation, 2=diving)
```

Maximum 20 enemies per wave. Arrays DIMmed once at startup.

### Formation Movement

The formation has a base position (fx, fy) and a movement pattern. Each enemy's screen position = formation base + individual offset. When the formation moves, only the base changes — offsets stay constant. Dead enemies' offsets are skipped during drawing.

```basic
400 REM MOVE FORMATION
410 LET fx = fx + fd
420 IF fx > 24 OR fx < 2 THEN LET fd = -fd: LET fy = fy + 1
430 FOR i = 1 TO ne
440   IF ea(i) = 0 THEN GO TO 470
450   LET sx = fx + ex(i): LET sy = fy + ey(i)
460   PRINT AT sy, sx; INK ec; CHR$ (143 + et(i))
470 NEXT i
```

### Bullet Pool

Player bullets tracked in arrays `bx(2)`, `by(2)`, `ba(2)` — x-position, y-position, active flag. Normally only `ba(1)` is used. The double-shot power-up activates `ba(2)`.

Enemy bombs tracked similarly: `mx(3)`, `my(3)`, `ma(3)` — maximum 3 active bombs.

### UDG Memory

UDGs are stored at USR "A" (65368 by default). 14 characters × 8 bytes = 112 bytes. Defined at startup via POKE loops reading DATA.

### Performance Budget

Each game tick involves:
- 1 PRINT AT for the player (~0.3ms)
- 1-2 PRINT ATs for bullets (~0.6ms)
- Up to 20 PRINT ATs for enemies (~6ms)
- 1-3 PRINT ATs for bombs (~0.9ms)
- INKEY$ + conditionals (~0.5ms)
- Array indexing and state checks (~2ms)

Total per frame: ~10ms of PRINT AT work + ~5ms of logic = ~15ms best case. But BASIC interpreter overhead (line lookup, variable search, floating point) multiplies this by 5-10×. Real frame time: ~100-200ms per loop = 5-10fps.

5-10fps is playable for a slow-paced shooter (enemies move every few ticks, not every tick). With 20 enemies it drops to 3-5fps. This is the performance wall — and the teaching moment.

### Optimisation Techniques (Taught in Unit 28)

1. **Short variable names**: `a` not `score` — the interpreter searches the variable table linearly
2. **Low line numbers for GO SUBs**: BASIC searches from line 1 each time
3. **Minimise PRINT AT calls**: only redraw what changed, not the entire screen
4. **Integer arithmetic**: avoid unnecessary floating point
5. **Avoid string operations in the loop**: pre-compute anything string-based

### Line Numbering

- 1-49: Initialisation, UDG definitions (POKE loops + DATA)
- 50-99: Title screen
- 100-199: Wave loading (READ formation DATA, place enemies)
- 200-299: Main game loop
- 300-349: Player movement and firing
- 350-399: Bullet movement and collision
- 400-449: Formation movement
- 450-499: Individual enemy movement (scouts, bombs)
- 500-549: Collision handling (explosions, damage, death)
- 550-599: Power-ups (drop, fall, collect)
- 600-649: HUD update
- 650-699: Wave clear, game over, high score
- 800-899: UDG DATA
- 900-999: Wave DATA (10 waves)

### No ELSE

The Spectrum 48K has no ELSE keyword. All branching uses `IF condition THEN GO TO line` to skip past the alternative. Multi-condition validation is built from layered IF/THEN checks, each jumping to a handler line or falling through to the next check.

### Memory

- Game logic: ~8-10 KB
- UDG DATA: ~0.5 KB
- Wave DATA: ~1 KB
- Enemy arrays and variables: ~1 KB
- Total: ~11-13 KB — comfortable on a 48K Spectrum

---

## Changelog

- **v2.0 (2026-03-13):** Rewritten for v5.0 curriculum. Now Game 14 with 32 units (was Game 4 with 64 units). Compressed from 20 waves to 10, 4 power-ups to 2, removed bosses, attract mode, and difficulty select. Core experience preserved: UDG graphics, formation shooting, the performance ceiling lesson.
- **v1.0 (2026-03-09):** Initial game outline as Game 4 in the v4.0 curriculum. 64 units across 4 phases.
