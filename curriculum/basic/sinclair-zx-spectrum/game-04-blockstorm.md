# Game 04: Blockstorm

**Track:** Spectrum BASIC
**Genre:** Vertical shooter with UDG graphics
**Units:** 64 (4 phases × 16 units)
**Language:** Sinclair BASIC
**Max lines:** ~500
**Save/load:** No — arcade game, each run is 5-15 minutes

---

## Premise

Alien blocks descend from the sky in waves. You fire upward. They explode. More come. Faster. In tighter formations. With new abilities.

Blockstorm is a vertical shooter built entirely with user-defined graphics — custom 8×8 characters that replace the Spectrum's built-in set. The player's ship, every enemy type, bullets, explosions, power-ups, and terrain are all UDGs placed with PRINT AT. The game looks like a real Spectrum arcade conversion, not a text-mode demo.

It's also the game where BASIC breaks. The first few waves are smooth. By wave 10, the screen is full of moving objects and the frame rate visibly drops. By wave 15, the player can feel the interpreter gasping. This is not a bug — it's the lesson. The learner has pushed BASIC to its absolute limit. They understand viscerally why assembly exists.

---

## Core Mechanics

### The Player

A ship at the bottom of the screen, moving left and right. Fires upward. One bullet on screen at a time (initially — upgradeable).

| Control | Key |
|---------|-----|
| Left | O |
| Right | P |
| Fire | SPACE |

The ship occupies one character cell and is drawn as a UDG: a recognisable spaceship shape in 8×8 pixels.

### Enemies

Enemies descend from the top of the screen. They move in formation patterns: rows that shift left/right (Space Invaders style), V-formations that dive, columns that snake. Each wave has a pattern.

Enemy types (each a different UDG):

| Type | UDG | Colour | Behaviour | Points | Hits |
|------|-----|--------|-----------|--------|------|
| Drone | A | Green | Moves with formation | 10 | 1 |
| Scout | B | Cyan | Breaks from formation, dives | 25 | 1 |
| Tank | C | Yellow | Slow, absorbs hits | 50 | 2 |
| Bomber | D | Magenta | Drops projectiles downward | 30 | 1 |
| Boss block | E | Red, BRIGHT | Large (2×2 UDGs), anchors a wave | 200 | 5 |

### Bullets

Player bullet: a single character (UDG F, a small arrow or dot) moving upward one cell per game tick. One on screen at a time (base). Power-ups allow two simultaneous bullets.

Enemy bombs (from Bombers): fall downward one cell per N ticks. Hit the player = lose a life.

### Collisions

All collision is character-cell based. Before moving a bullet upward, check if the target cell contains an enemy (ATTR or SCREEN$). If yes: hit. Before moving an enemy downward, check if the target cell contains the player. If yes: death.

### Explosions

When an enemy is destroyed, replace its UDG with an explosion UDG (G: a starburst shape) in red INK. The explosion persists for 2-3 game ticks, then disappears. Simple but satisfying.

For multi-hit enemies (Tank, Boss), show a damage flash — briefly change INK to white then back — before the final explosion.

### Power-Ups

Occasionally a destroyed enemy drops a power-up (falls downward like a bomb, but collectible):

| Power-up | UDG | Colour | Effect |
|----------|-----|--------|--------|
| Double shot | H | Cyan | Two bullets on screen simultaneously |
| Speed boost | I | Green | Player moves twice per tick for 10 seconds |
| Shield | J | Yellow | Absorb one hit without dying |
| Bonus points | K | Magenta | +100 points |

Power-ups disappear if they reach the bottom without being collected. Only one active power-up at a time (except bonus points, which stacks with anything).

---

## Wave Design

### Structure

The game has 20 waves. Each wave is a formation of enemies that must be entirely destroyed before the next wave begins. Waves get progressively harder: more enemies, faster movement, new enemy types, tighter formations.

### Wave Progression

| Wave | Enemies | Types | Speed | Pattern | New element |
|------|---------|-------|-------|---------|-------------|
| 1 | 8 | Drones only | Slow | Single row, shift L/R | Learn to aim |
| 2 | 10 | Drones | Slow | Two rows | More targets |
| 3 | 10 | Drones + 2 Scouts | Slow | Row + divers | Scouts break formation |
| 4 | 12 | Mixed | Medium | V-formation | Formation patterns |
| 5 | 12 | Mixed + 1 Tank | Medium | Row with Tank centre | Multi-hit enemies |
| 6 | 14 | Mixed | Medium | Two V-formations | Denser screen |
| 7 | 14 | Mixed + Bombers | Medium | Row + bomber support | Dodge bombs while shooting |
| 8 | 16 | Mixed | Fast | Snaking column | Speed increase |
| 9 | 16 | All types | Fast | Complex formation | Everything combined |
| 10 | Boss + 8 Drones | Boss block | Medium | Boss with escort | First boss |
| 11-14 | 16-20 | All types | Fast | Varied | Escalating density |
| 15 | Boss + 12 escorts | Boss block | Fast | Boss wave 2 | Harder boss |
| 16-19 | 20-24 | All types | Very fast | Varied | BASIC starts to struggle |
| 20 | Final boss + 16 | Large boss | Fast | Final wave | Everything at once |

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
- Final line: formation movement pattern

### Formation Movement

Formations move as a unit. The pattern string defines the group's movement:
- "E4S1W4S1" = shift right 4, descend 1, shift left 4, descend 1 (Space Invaders pattern)
- "E2W4E2S1" = wider sway
- When the formation descends to the player's row, game over (they've invaded)

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

### UDG Designs

21 UDGs available (A-U). Allocation:

| UDG | Character | Purpose |
|-----|-----------|---------|
| A | Drone | Basic enemy — blocky alien shape |
| B | Scout | Pointed, aggressive — dive attack shape |
| C | Tank | Heavy, wide — armoured appearance |
| D | Bomber | Distinctive — bomb bay visual |
| E-F | Boss (2×2) | Large enemy, 4 UDGs for quadrants (TL, TR, BL, BR) |
| G | Player ship | Arrow/wedge pointing up |
| H | Player bullet | Small upward arrow or dot |
| I | Enemy bomb | Small downward arrow |
| J | Explosion frame 1 | Starburst |
| K | Explosion frame 2 | Expanding fragments |
| L | Power-up: double | "D" icon or twin arrows |
| M | Power-up: speed | "S" icon or lightning bolt |
| N | Power-up: shield | Shield shape |
| O | Power-up: bonus | Star shape |
| P | Shield indicator | Shown on HUD when shield active |
| Q-U | Reserved | Stars/terrain/decoration |

### UDG Definition

Each UDG is 8 bytes, defined via BIN:

```basic
10 REM PLAYER SHIP (UDG "G")
20 FOR i = 0 TO 7
30   READ b
40   POKE USR "G" + i, b
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
| Boss | Red (2), BRIGHT | Menacing |
| Explosions | Red (2) then Yellow (6) | Two-frame colour shift |
| Power-ups | Cycle colours | FLASH 1 to attract attention |
| Enemy bombs | Red (2) | Danger |
| HUD | White (7), BRIGHT | Clear, readable |

---

## Scoring

| Event | Points |
|-------|--------|
| Drone destroyed | 10 |
| Scout destroyed | 25 |
| Bomber destroyed | 30 |
| Tank destroyed | 50 |
| Boss destroyed | 200 |
| Power-up collected | Varies (bonus = 100, others = 0 but useful) |
| Wave clear bonus | 50 × wave number |
| No-damage wave bonus | 100 |

Lives: 3. Extra life at 2,000 points (one only).

High score: tracked in memory for the session. Displayed on title screen and game over.

---

## Phase Breakdown

### Phase 1: Ship and Bullets (Units 1-16)

The player moves and shoots. No enemies yet — just the ship, bullets, and the UDG system.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | Custom Characters | Title screen. Then: define one UDG using POKE USR and BIN. Display it with PRINT AT. It's a custom character — not from the built-in set. | POKE, USR, BIN, UDG concept |
| 2 | Designing UDGs | Graph paper to binary: sketch an 8×8 sprite, convert rows to BIN, POKE them. Design the player ship. | UDG design workflow, binary representation |
| 3 | The Ship | Display the player ship UDG near the bottom of the screen. White INK on black PAPER. It looks like a real game sprite. | PRINT AT with UDG, INK, positioning |
| 4 | Movement | O/P keys move the ship left and right. Erase old position, draw new. Boundary checks (don't leave the screen). | INKEY$, erase-redraw, boundary checking |
| 5 | Smooth Movement | Hold a key and the ship moves continuously. Game loop reads INKEY$ each tick. Speed feels right. | Continuous input, game loop timing |
| 6 | The Bullet | Press SPACE: a bullet UDG appears above the ship and moves upward one cell per tick. Reaches the top and disappears. | Bullet state (active, position), upward movement |
| 7 | One Bullet Rule | Only one bullet on screen at a time. Fire again after it disappears or hits something. Teaches bullet pooling. | State flag, resource management |
| 8 | Bullet UDG | Design the bullet UDG — small, bright, fast-looking. Test that it's visible against the black background. | UDG design for small objects |
| 9 | Multiple UDGs | Define all player-side UDGs in a setup routine. Ship, bullet, explosion, shield indicator. Batch POKE with FOR/NEXT. | Batch UDG definition, DATA for multiple shapes |
| 10 | The HUD | Score, high score, lives, wave number. PRINT AT the top two rows. BRIGHT 1 to distinguish from game area. | HUD layout, formatted number display |
| 11 | Lives Display | Three ship UDGs in the HUD as life indicators. Lose one (later) and a ship disappears. | HUD with UDG characters |
| 12 | Sound Effects | Fire: short high BEEP. Bullet hits top: quiet tick. Design sounds that won't slow the game loop noticeably. | BEEP with minimal duration, sound design |
| 13 | Star Field | Background stars — a few dots (PRINT AT with "." or UDG) scattered on screen. Static, not scrolling. Adds depth to the space feel. | Background decoration, visual depth |
| 14 | Game Loop Structure | Formalise the loop: input → move player → move bullet → check collisions → update HUD → loop. GOSUB for each section. | Game architecture, GOSUB structure |
| 15 | Speed Tuning | The game loop should run at a consistent pace. Add PAUSE or timing adjustment. Test on 48K. | Frame rate management, PAUSE |
| 16 | Ship Polish | The ship movement feels good, the bullet feels snappy, the HUD is clear, sounds are satisfying. No enemies yet, but the player side is solid. | Integration testing, feel tuning |

**Milestone:** A polished player ship that moves and fires. UDGs look like real sprites. The HUD is clear. Sound effects are satisfying. Ready for enemies.

### Phase 2: The Invasion (Units 17-32)

Enemies appear, move in formation, and can be destroyed. The game becomes playable.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | One Drone | A single enemy UDG on screen. Static. Bullet hits it → explosion UDG appears → enemy gone. | Collision detection (SCREEN$ or position check) |
| 18 | Explosion Animation | Hit an enemy: replace with explosion UDG (frame 1), wait 2 ticks, replace with frame 2, wait 1 tick, clear. Red then yellow. | Two-frame animation, timed replacement |
| 19 | Explosion Sound | Explosion BEEP: descending tone burst. Different from fire sound. Test that it doesn't slow the loop too much. | Sound design, performance awareness |
| 20 | A Row of Drones | 8 drones in a row. Bullet hits any one → that one explodes. Others remain. Track active enemies in an array. | Enemy arrays, individual state tracking |
| 21 | Formation Movement | The row shifts left and right as a unit. All living enemies move together. Wrapping or bouncing at screen edges. | Group movement, offset tracking |
| 22 | Formation Descent | When the formation reaches a screen edge, it descends one row and reverses direction. Classic Space Invaders pattern. | Direction reversal, descent trigger |
| 23 | Formation Data | Move formation layout into DATA strings. "AAAAAAAAAA" = row of drones. Read and place at wave start. | Formation DATA, string-to-grid |
| 24 | Two Rows | Two rows of enemies. Different UDG per row (drones top, scouts bottom). Denser target area. | Multi-row formations, mixed types |
| 25 | Scout Behaviour | Scouts break from formation and dive toward the player. Independent movement after detaching. | Individual enemy AI, state switch |
| 26 | Enemy Types | Define all enemy UDGs. Drone, Scout, Tank, Bomber. Different colours per type. Tank takes 2 hits (damage state). | Multiple UDG types, hit counters |
| 27 | Bomber Drops | Bombers periodically drop bomb UDGs that fall downward. Player must dodge bombs while shooting. | Enemy projectiles, dual threat |
| 28 | Bomb Collision | Bomb hits player → lose a life. Ship explosion animation, brief pause, respawn. Lives decrement in HUD. | Player death, respawn, life management |
| 29 | Game Over | Zero lives → "GAME OVER" with final score. Compare to high score, update if beaten. Return to title screen. | End state, high score comparison |
| 30 | Wave Clear | All enemies destroyed → "WAVE COMPLETE" message, bonus points, brief pause, then next wave. | Wave completion detection, inter-wave flow |
| 31 | Wave 1-5 Data | Design and enter 5 complete waves with escalating difficulty. Test each one. | Level design, playtesting |
| 32 | Five Waves Playable | Waves 1-5 playable in sequence. Formation movement, diving scouts, bombing runs, wave clear bonuses. A real game. | Integration milestone |

**Milestone:** A playable vertical shooter with 5 waves, 4 enemy types, explosions, bombs, lives, game over, and wave progression. It looks and plays like a real Spectrum game.

### Phase 3: Depth (Units 33-48)

20 waves, power-ups, bosses, and the full arcade experience.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | Power-Up Drops | Destroyed enemies occasionally drop a power-up UDG. Falls downward. Collect by touching. | Random drops, collectible objects |
| 34 | Double Shot | Power-up: two bullets on screen simultaneously. Manage two bullet positions and collision checks. | Multiple active bullets, expanded state |
| 35 | Speed Boost | Power-up: player moves twice per tick for a duration. Timer counts down. | Timed effects, duration tracking |
| 36 | Shield | Power-up: absorb one hit. Shield UDG shown in HUD. Consumed on hit instead of losing a life. | Defensive power-up, HUD indicator |
| 37 | Boss Enemy | A 2×2 character boss (4 UDGs forming one large enemy). Takes 5 hits. Moves independently. | Multi-cell entities, composite objects |
| 38 | Boss Behaviour | Boss moves in a pattern (slow sway), fires bombs, escort drones protect it. Killing drones first is easier. | Complex enemy, tactical gameplay |
| 39 | Waves 6-10 | Design waves 6-10. Faster enemies, bombers, first boss at wave 10. | Mid-game level design |
| 40 | Waves 11-15 | Design waves 11-15. All enemy types, tight formations, second boss at wave 15. | Late-game level design |
| 41 | Waves 16-20 | Design waves 16-20. Maximum difficulty. BASIC is visibly struggling. Final boss at wave 20. | End-game design, performance ceiling |
| 42 | The Performance Wall | With 20+ enemies, bombs, bullets, and the player all moving, the game loop slows. Document the frame rate drop. Measure it. | Performance measurement, bottleneck identification |
| 43 | Optimisation Pass | Speed up the critical path: shorter variable names, integer arithmetic, fewer GOSUB calls, tighter loops. Measurable improvement. | BASIC optimisation techniques |
| 44 | More Optimisation | Move frequently called GOSUBs to low line numbers (BASIC searches from line 1). Use LET a=PEEK vs LET score=PEEK. Profile the difference. | Interpreter-specific optimisation |
| 45 | Extra Life | Award one extra life at 2,000 points. BEEP fanfare, life appears in HUD. One only — no infinite lives. | Threshold bonus, one-shot trigger |
| 46 | No-Damage Bonus | Clear a wave without being hit → 100 bonus points. "PERFECT!" flash on screen. | Wave-level state tracking, bonus condition |
| 47 | Enemy Invasion | If the formation descends to the player's row, instant game over regardless of lives. "INVADED!" The stakes are real. | Fail condition, escalating pressure |
| 48 | Twenty Waves | All 20 waves playable. Boss at wave 10, 15, 20. Power-ups, bonuses, invasion threat. Full arcade experience. | Content-complete game |

**Milestone:** 20 waves of escalating action with power-ups, bosses, and the visible performance ceiling that makes assembly necessary. The complete arcade experience in BASIC.

### Phase 4: Polish and Legacy (Units 49-64)

Title screen, presentation, the honest performance lesson, and the bridge to assembly.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Title Screen | "BLOCKSTORM" in UDG-constructed letters or large PRINT AT text. Enemy UDGs parade across the screen. Attract mode. | Title design, UDG art |
| 50 | Attract Mode | After the title sits for 10 seconds, run a brief demo: autopilot ship fires at a wave. Shows the game in action. | AI-controlled demo, attract loop |
| 51 | Instructions | "HOW TO PLAY" screen. Controls, enemy types with UDGs shown, power-up descriptions. One screen, clear and brief. | User onboarding |
| 52 | Difficulty Select | Easy (slow enemies, frequent power-ups), Normal, Hard (fast enemies, rare power-ups). Affects speed and drop rates. | Difficulty as parameter |
| 53 | Wave Intro | Brief flash before each wave: "WAVE 5" in large text. Enemy formation shown briefly before it starts moving. Warning. | Inter-wave pacing, anticipation |
| 54 | Background Variety | Different star patterns per wave group. Waves 1-5: sparse stars. Waves 11-15: dense starfield. Waves 16-20: nebula colours (INK changes). | Visual variety without new mechanics |
| 55 | Death Animation | Player destroyed: ship UDG replaced by expanding explosion (2-3 frames), screen border flashes red, descending BEEP. More dramatic than a simple replacement. | Multi-frame player death, border flash |
| 56 | Score Table | Game over: if high score beaten, enter 3 initials. Display top 5 scores (session only). | Name entry, score table, array sorting |
| 57 | Sound Polish | Review every sound. Fire should be punchy. Explosions should be satisfying. Power-up collection should feel rewarding. No sound should slow the loop. | Audio review, performance-aware sound |
| 58 | Enemy Animation | Enemies alternate between two UDG frames (e.g., legs open/closed) every N ticks. Formation looks alive, not static. | Animation via UDG switching |
| 59 | The Performance Lesson | A dedicated unit: measure the game loop time at wave 1 vs wave 20. Count ticks per frame. Document exactly where BASIC fails and why. | Performance analysis, educational reflection |
| 60 | What Assembly Would Do | Discussion unit: the same game in assembly would run at 50fps regardless of enemy count. Explain why (direct hardware access, no interpreter overhead). Preview the assembly track. | Bridge to assembly, motivation |
| 61 | Edge Cases | Bullet and bomb cross in the same cell — both destroyed? Power-up and bomb in same column? Test every combination. | Edge case testing, interaction matrix |
| 62 | Bug Sweep | Play all 20 waves on all difficulty levels. Fix any bugs. Verify score calculation, lives, game over, high score. | Systematic QA |
| 63 | Line Count | Under 500 lines? UDG DATA takes ~40 lines. Wave DATA takes ~60 lines. Game logic takes ~350 lines. Should fit. If not, optimise DATA packing. | Code budget, final scope check |
| 64 | The Finished Game | Clean listing. Title, attract mode, difficulty select, 20 waves, 4 enemy types, bosses, power-ups, high score table. The Spectrum BASIC track's peak — and its honest ending. | Completion, pride, transition |

**Milestone:** A complete vertical shooter that would fill three pages of a magazine listing. 20 waves, bosses, power-ups, attract mode, high score table. And the honest lesson: here's exactly where BASIC breaks, and exactly why the assembly track exists.

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
ex()  - enemy X positions
ey()  - enemy Y positions
et()  - enemy type (0=empty, 1=drone, 2=scout, 3=tank, 4=bomber, 5=boss)
eh()  - enemy hit points remaining
ea()  - enemy active flag (in formation / diving / dead)
```

Maximum 24 enemies per wave. Arrays DIMmed once at startup.

### Formation Movement

The formation has a base position (fx, fy) and a movement pattern. Each enemy's screen position = formation base + individual offset. When the formation moves, only the base changes — offsets stay constant. Dead enemies' offsets are skipped during drawing.

```basic
400 REM MOVE FORMATION
410 LET fx = fx + fdx
420 IF fx > 24 OR fx < 2 THEN LET fdx = -fdx: LET fy = fy + 1
430 FOR i = 1 TO ne
440   IF et(i) = 0 THEN GO TO 470
450   LET sx = fx + ox(i): LET sy = fy + oy(i)
460   PRINT AT sy, sx; INK et_colour(et(i)); CHR$ (143 + et(i))
470 NEXT i
```

### UDG Memory

UDGs are stored at USR "A" (65368 by default). 21 characters × 8 bytes = 168 bytes. Defined at startup via POKE loops reading DATA.

To use more than 21 UDGs, the UDG pointer can be redirected: POKE 23675/23676 to point to a different address. This gives up to 96 custom characters if needed, but 21 is enough for this game.

### Performance Budget

The critical question: how fast is the game loop with 20+ active enemies?

Each tick involves:
- 1 PRINT AT for the player (~0.3ms)
- 1-2 PRINT ATs for bullets (~0.6ms)
- 20 PRINT ATs for enemies (~6ms)
- 2-4 PRINT ATs for bombs (~1.2ms)
- INKEY$ + conditionals (~0.5ms)
- Array indexing and state checks (~2ms)

Total per frame: ~10-15ms of PRINT AT work + ~5ms of logic = ~15-20ms best case. At 50fps that's fine (20ms per frame). But BASIC overhead (interpreter lookup, floating point, GOSUB dispatch) multiplies this by 5-10×. Real frame time: ~100-200ms per loop = 5-10fps.

5-10fps is playable for a slow-paced shooter (enemies move every few ticks, not every tick). But with 20+ enemies it drops to 3-5fps. This is the performance wall — and the teaching moment.

### Optimisation Techniques (Taught in Phase 3)

1. **Short variable names**: `a` not `score` (interpreter searches variable table linearly)
2. **Integer arithmetic**: avoid floating point where possible
3. **Low line numbers for GOSUBs**: BASIC searches from line 1 each time
4. **Minimise PRINT AT calls**: only redraw what changed, not the entire screen
5. **Avoid string operations in the loop**: pre-compute anything string-based
6. **PAUSE 0 not PAUSE 1**: PAUSE 0 waits for a keypress OR interrupt, useful for frame sync

### Line Numbering

- 1-49: Initialisation, UDG definitions (POKE loops + DATA)
- 50-99: Title screen, instructions, difficulty select
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
- 700-749: Attract mode and demo
- 750-799: Sound effects
- 800-899: UDG DATA (ship, enemies, explosions, power-ups)
- 900-999: Wave DATA (20 waves)

### Memory Budget

- Game logic: ~10-12 KB
- UDG DATA: ~1 KB
- Wave DATA: ~2 KB
- Enemy arrays and variables: ~1 KB
- Total: ~14-16 KB — comfortable

---

## Design Notes

### Why a Vertical Shooter

Vertical shooters work at BASIC speeds because the core loop is simple: one player moves horizontally, bullets move vertically, enemies descend slowly. The geometry is constrained (everything moves on cardinal axes), collision detection is grid-based (SCREEN$ or position comparison), and the pacing naturally accommodates BASIC's interpreter overhead.

More importantly, vertical shooters are THE game that pushes BASIC to its limit. As enemy count increases, the frame rate drops visibly. This isn't a flaw in the game design — it's the curriculum's final lesson: "you've hit the ceiling. Here's why assembly exists."

### The Honest Ending

Unit 59 is explicitly about measuring performance. The learner times the game loop at wave 1 (fast, few enemies) and wave 20 (slow, many enemies). They calculate the bottleneck. They understand that BASIC's interpreter checks every line, converts every variable name to an address, and processes every GOSUB as a linear search.

Unit 60 previews what assembly would do differently: write directly to screen memory, use hardware interrupts for timing, process collision in microseconds instead of milliseconds. The same game in assembly would run at a locked 50fps with 100 enemies. The learner doesn't take this on faith — they've felt the problem. The assembly track is the solution.

### The Magazine Test

Three pages of a type-in listing. 20 waves of escalating shooter action with custom UDG graphics, explosions, power-ups, bosses, a high score table, and an attract mode. Would a teenager in 1987 spend a Saturday typing this in? Yes. Would they play it all weekend? Yes.

### The Four-Game Arc

The Spectrum BASIC track now has a complete emotional arc:
1. **The Cursed Manor**: Calm, narrative, text-based. Teaches logic and state.
2. **Night Patrol**: Tense, stealth, grid-based. Teaches real-time interaction and AI.
3. **Lattice**: Contemplative, geometric, turn-based. Teaches graphics and spatial reasoning.
4. **Blockstorm**: Frantic, explosive, arcade action. Teaches performance limits and bridges to assembly.

Four games, four moods, four sets of BASIC techniques. A complete education in what the language can do — and an honest conclusion about what it can't.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Game 4 in the restructured Spectrum BASIC track. Vertical shooter with UDG graphics, designed to demonstrate BASIC's performance ceiling.
