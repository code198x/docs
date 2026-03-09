# Game 03: Starswarm

**Track:** C64 BASIC
**Genre:** Sprite-based space shooter
**Units:** 64 (4 phases × 16 units)
**Language:** Stock BASIC V2
**Max lines:** ~500
**Save/load:** No — arcade game, each run is 5-15 minutes

---

## Premise

Swarms of alien ships descend on your position. You control a fighter — a VIC-II hardware sprite — and fire upward into the swarm. The aliens are sprites too: smooth, colourful, moving independently of the background. For the first time in the BASIC track, the game has real sprites — not PETSCII characters, but hardware-accelerated graphics objects that move at pixel precision.

The catch: BASIC can't update 8 sprites and run game logic at 50fps. The aliens glide smoothly (the VIC-II handles that), but the game logic crawls. This tension — smooth hardware vs. slow interpreter — is the lesson. And it's the motivation for assembly.

---

## Core Mechanics

### Sprites via POKE

The VIC-II provides 8 hardware sprites. Each sprite is 24×21 pixels (63 bytes of data). All sprite control is via POKE to VIC-II registers:

| Register | Address | Purpose |
|----------|---------|---------|
| Sprite X position | 53248-53262 (even) | Horizontal position (low 8 bits) |
| Sprite Y position | 53249-53263 (odd) | Vertical position |
| X high bit | 53264 | Bit 8 of X for each sprite (left side of screen) |
| Enable | 53269 | Each bit enables one sprite |
| Expand X | 53277 | Double width per sprite |
| Expand Y | 53271 | Double height per sprite |
| Colour | 53287-53294 | Per-sprite colour |
| Multicolour | 53276 | Enable multicolour mode per sprite |
| Data pointer | 2040-2047 | Which 64-byte block holds the sprite shape |
| Sprite-sprite collision | 53278 | Which sprites have collided |
| Sprite-background collision | 53279 | Which sprites hit background |

### The Player

Sprite 0: the player's ship. A 24×21 pixel design — a recognisable spaceship pointing up. White, bright, smooth movement. Joystick controls.

The player moves at pixel precision — not character cells. This is the first time in the BASIC track that movement isn't grid-locked. The ship slides smoothly across the screen.

### The Bullet

Sprite 1: the player's bullet. A small dot or arrow. Moves upward at fixed speed. One bullet on screen at a time (fire button = bit 4 of PEEK(56320)).

When the bullet reaches the top of the screen, it deactivates (disable sprite: clear bit in 53269, or move off-screen).

### Enemies

Sprites 2-7: up to 6 alien ships visible simultaneously. Each is a different sprite shape. They descend from the top in wave patterns — swooping, zigzagging, or diving.

With only 6 enemy sprites available (8 total minus player and bullet), waves work by recycling: when an alien is destroyed or exits the bottom, its sprite is reassigned to the next alien in the wave queue. The wave might define 20 aliens, but only 6 exist on screen at once.

### Collision Detection

VIC-II handles collision in hardware:
- `PEEK(53278)`: sprite-sprite collision register. Each bit indicates which sprite collided.
- Reading the register clears it, so read once per frame and store the result.

If bullet (sprite 1) collides with any enemy sprite: hit. If player (sprite 0) collides with any enemy sprite: death.

### Sprite Shapes

Each sprite is 63 bytes. Designed on a 24×21 grid, stored in DATA statements, POKEd to memory at startup.

Sprite data must be aligned to 64-byte boundaries. Standard location: start at address 832 (block 13) or 12288+ (if character ROM is relocated). The simpler approach: use the default location and POKE sprite shapes into blocks 13-20 (addresses 832-1343, which overlap the cassette buffer — safe if not using tape).

---

## Wave Design

### Structure

The game has 15 waves. Each wave defines a sequence of aliens with entry positions, movement patterns, and speeds. Only 6 appear on screen at once — destroyed or exited aliens are replaced by the next in the queue.

### Wave Progression

| Wave | Aliens | Speed | Pattern | New element |
|------|--------|-------|---------|-------------|
| 1 | 6 | Slow | Straight descent | Learn to aim |
| 2 | 8 | Slow | Zigzag descent | Moving targets |
| 3 | 10 | Slow | V-formation entry | Grouped targets |
| 4 | 10 | Medium | Sine wave descent | Smooth curves |
| 5 | 12 | Medium | Dive attacks | Aliens swoop toward player |
| 6 | 12 | Medium | Mixed patterns | Varied movement |
| 7 | 14 | Medium | Circling entry | Aliens loop before descending |
| 8 | 14 | Fast | Aggressive dives | Faster, less predictable |
| 9 | 16 | Fast | Split formation | Two groups from different sides |
| 10 | 16 | Fast | Boss + escorts | One tough alien with bodyguards |
| 11-15 | 18-24 | Very fast | Everything combined | Escalating chaos |

### Movement Patterns

Alien movement is defined per-wave as a sequence of position updates:

```basic
1000 DATA 10: REM NUMBER OF ALIENS IN WAVE
1010 DATA 100,0, 140,0, 180,0, 220,0, 260,0: REM START X,Y PAIRS
1020 DATA 100,0, 140,0, 180,0, 220,0, 260,0: REM SECOND BATCH
1030 DATA 1: REM PATTERN: 1=STRAIGHT, 2=ZIGZAG, 3=SINE, 4=DIVE
1040 DATA 2: REM SPEED (PIXELS PER MOVE)
```

Pattern functions calculate the X offset per tick:
- **Straight**: X unchanged, Y increases
- **Zigzag**: X alternates left/right every N ticks
- **Sine**: X = start_X + SIN(tick/period) × amplitude (requires SIN function — BASIC has it)
- **Dive**: alien tracks toward player X, accelerating downward

---

## Visual Design

### Screen Setup

```
Black background: POKE 53281, 0
Black border: POKE 53280, 0
```

A starfield drawn with POKE to screen RAM (random dots, character 46) provides depth. The sprites move over this background — hardware sprites are always on top of the character display.

### Sprite Shapes

| Sprite | Design | Colour |
|--------|--------|--------|
| Player ship | Pointed wedge, exhaust flames at bottom | White (1) |
| Bullet | Small dot or arrow | Yellow (7) |
| Alien type 1 | Rounded invader shape | Green (5) |
| Alien type 2 | Angular aggressive shape | Cyan (3) |
| Alien type 3 | Wide-wing bomber | Light red (10) |
| Boss alien | Large (expanded X+Y = 48×42 pixels) | Red (2) |
| Explosion frame 1 | Starburst | Yellow (7) |
| Explosion frame 2 | Scattered dots | Orange (8) |

### Multicolour Sprites

Aliens can use multicolour mode (53276) for more detailed shapes at half horizontal resolution (12 wide pixels instead of 24 thin). The player ship stays hi-res for a crisp look. Mixing modes within the same game demonstrates VIC-II flexibility.

---

## Scoring and Lives

| Event | Points |
|-------|--------|
| Alien type 1 destroyed | 10 |
| Alien type 2 destroyed | 20 |
| Alien type 3 destroyed | 30 |
| Boss alien destroyed | 100 |
| Wave clear bonus | 50 × wave number |
| No-death wave bonus | 100 |

Lives: 3. Extra life at 2,000 points (one only).

---

## Phase Breakdown

### Phase 1: Sprites (Units 1-16)

The player's ship and bullet work. No enemies yet — learn sprite fundamentals.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | Enabling a Sprite | POKE 53269, 1 — sprite 0 appears. It's a garbage shape (whatever's in memory). But it's there, on screen, immediately. | Sprite enable register, hardware sprites |
| 2 | Positioning a Sprite | POKE 53248, 170: POKE 53249, 140 — sprite 0 moves to the centre of the screen. Move it around by changing X and Y values. | Sprite position registers, X/Y coordinates |
| 3 | Sprite Colour | POKE 53287, 1 — sprite 0 is now white. Try all 16 colours. | Sprite colour register, C64 palette |
| 4 | Designing a Shape | 24×21 pixel grid on paper. Convert each row to three bytes (8 pixels per byte). 63 bytes total. Store in DATA. | Sprite data format, binary-to-decimal |
| 5 | Loading Sprite Data | FOR loop POKEs 63 bytes from DATA to memory at block 13 (address 832). POKE 2040, 13 tells VIC-II to use block 13 for sprite 0. | Sprite data pointer, POKE loop |
| 6 | The Player Ship | A recognisable spaceship appears on screen. White, pointing up. The learner designed this shape themselves. | Custom sprite design, pride of creation |
| 7 | Joystick Movement | PEEK(56320) reads the joystick. Move the sprite by POKEing new X/Y positions. Smooth, pixel-precise movement. | Joystick input, sprite position update |
| 8 | Screen Boundaries | Stop the sprite at screen edges. X: 24-343 (requires the X high bit at 53264 for X > 255). Y: 50-229. | Boundary checking, X high bit |
| 9 | The X High Bit | X positions above 255 need bit 0 of register 53264 set. POKE 53264, PEEK(53264) OR 1 to set, AND 254 to clear. Explain bitwise logic. | Bit manipulation, OR/AND for bit set/clear |
| 10 | The Bullet | Sprite 1: a small dot. Press fire (bit 4 of joystick) → bullet appears above the player and moves upward. | Second sprite, fire button, bullet state |
| 11 | Bullet Movement | Each game tick, decrease bullet Y by 2. When Y < 30, deactivate (disable sprite 1). One bullet on screen at a time. | Bullet lifecycle, activation/deactivation |
| 12 | Sprite Data for Bullet | Design a small bullet sprite. It doesn't need to fill the 24×21 frame — just a few pixels in the centre. | Minimal sprite design |
| 13 | Explosion Sprite | Design two explosion frames: a burst and scattered dots. Swap sprite pointer to show explosion for 3 ticks, then disable. | Animation via pointer swap |
| 14 | Starfield Background | POKE dots to screen RAM at random positions. Static stars — the sprites move over them. Depth illusion. | Background layering, sprites over characters |
| 15 | The HUD | PRINT score, lives, and wave number on row 0. Sprites render above this — no conflict. | HUD on character display, sprite priority |
| 16 | Player Polish | Ship moves smoothly, bullet fires and returns, explosions look satisfying. No enemies yet, but the player side is complete. | Integration, feel |

**Milestone:** A sprite-based ship that moves smoothly, fires bullets, and displays explosions. The learner has POKEd every VIC-II sprite register. Hardware sprites are no longer mysterious.

### Phase 2: The Swarm (Units 17-32)

Enemies appear as sprites, move in patterns, and can be destroyed.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | One Enemy Sprite | Sprite 2: an alien ship. Design the shape, load data, enable, position at top of screen. | Third sprite, enemy design |
| 18 | Alien Descent | The alien moves downward each tick. When it exits the bottom: disable, it's gone. | NPC vertical movement |
| 19 | Collision Detection | PEEK(53278) reads the collision register. If bit 1 (bullet) is set AND bit 2 (alien) is set: hit! | Hardware collision, bit reading |
| 20 | Hit Response | Collision detected → swap alien to explosion sprite → disable after 3 ticks → score increases. | Collision response, explosion sequence |
| 21 | Player Hit | If sprite 0 (player) collides with an alien: death. Flash, sound, respawn. | Player-enemy collision, death handling |
| 22 | Six Enemy Sprites | Sprites 2-7: six simultaneous aliens. Each with independent position and movement. | Six-sprite management, array state |
| 23 | Wave Queue | A wave defines 10-20 aliens. Only 6 on screen at once. Destroyed/exited aliens free a sprite slot for the next in queue. | Sprite recycling, queue management |
| 24 | Zigzag Pattern | Aliens zigzag: X alternates left/right every N ticks while Y increases. More challenging to hit. | Pattern movement, direction alternation |
| 25 | Sine Wave Pattern | X = start_X + SIN(tick × 0.1) × 30. Aliens weave smoothly. SIN is built into BASIC. | SIN function, smooth curves |
| 26 | Dive Attack | One alien tracks toward the player's X position. Accelerating downward. Must be dodged or shot quickly. | Tracking AI, acceleration |
| 27 | Wave Data | Wave definition in DATA: alien count, pattern type, speed. Load at wave start. | Wave DATA format, parameterised waves |
| 28 | Wave Clear | All aliens in the wave destroyed → "WAVE CLEAR" message, bonus points, next wave loads. | Wave completion, progression |
| 29 | Five Waves | Design waves 1-5 with increasing difficulty. Test each one. | Level design, difficulty progression |
| 30 | Multiple Alien Types | Different sprite shapes per wave. Type 1 (round, slow), type 2 (angular, fast), type 3 (bomber, drops projectiles?). Different colours. | Sprite shape variety, type-based behaviour |
| 31 | Score and Lives Polish | Score display updates cleanly. Lives shown as ship icons (PRINT sprite character). High score tracked. | Display polish |
| 32 | Five Waves Playable | A real space shooter with 5 waves, 3 alien types, hardware collision, smooth sprites. It looks like a C64 game. | Integration milestone |

**Milestone:** A sprite-based shooter with smooth alien movement, hardware collision detection, wave progression, and multiple alien types. The VIC-II is doing the heavy lifting — BASIC just updates positions.

### Phase 3: The Full Game (Units 33-48)

15 waves, boss encounters, and the performance lesson.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | Expanded Boss Sprite | POKE 53277 and 53271 to expand a sprite to double size (48×42 pixels). The boss alien is huge. | Sprite expansion registers |
| 34 | Boss Behaviour | The boss moves slowly, takes 5 hits, and fires back (a "bomb" sprite — repurpose one of the 6 enemy slots). | Multi-hit enemies, boss design |
| 35 | Boss Wave | Wave 10: boss with escort sprites. Kill escorts first (they shield the boss), then focus fire on the boss. | Tactical wave design |
| 36 | Waves 6-10 | Design waves 6-10. Faster enemies, mixed patterns, first boss at wave 10. | Mid-game design |
| 37 | Waves 11-15 | Design waves 11-15. Very fast, aggressive, complex patterns. Second boss at wave 15. | End-game design |
| 38 | Multicolour Aliens | Enable multicolour mode for alien sprites (POKE 53276). More detailed shapes at half horizontal resolution. Player stays hi-res. | Multicolour sprite mode |
| 39 | Shared Multicolour | POKE 53285 and 53286 set the two shared multicolour colours (used by all multicolour sprites). Design aliens using 4 colours. | Shared multicolour registers |
| 40 | The Speed Problem | With 6 enemy sprites, a bullet, and the player all updating every tick, measure the game loop time. It's slow. The sprites are smooth (hardware) but the BASIC logic lags behind. | Performance measurement |
| 41 | Optimisation Round 1 | Short variable names. Avoid floating point (INT everything). Minimise GOSUB calls. Measurable improvement. | BASIC optimisation techniques |
| 42 | Optimisation Round 2 | Only POKE positions that changed. Skip inactive sprites in the loop. Pre-calculate SIN table (store in array, don't call SIN each tick). | Lookup tables, selective update |
| 43 | Extra Life | Award one extra life at 2,000 points. Ship appears in HUD. | Bonus threshold |
| 44 | No-Death Bonus | Clear a wave without dying → 100 bonus points. "PERFECT!" flash. | Wave bonus condition |
| 45 | Invasion Fail | If an alien reaches the bottom of the screen, it's not just lost — the player loses a life. Stakes for missing. | Penalty for missed enemies |
| 46 | Sound Preview | POKE 54296, 15 (volume max). POKE 54273/54272 (frequency). POKE 54276, 17 (triangle, gate on). A single note plays. Preview of Game 4. | First SID POKE — just a taste |
| 47 | Edge Cases | Two aliens collide with bullet in same frame — both destroyed? (Yes, check all bits.) Alien and player collide while bullet hits different alien — both events fire? (Yes.) | Multi-collision handling |
| 48 | Fifteen Waves | All 15 waves playable. Bosses, multicolour aliens, smooth patterns, score tracking. Complete. | Content-complete game |

**Milestone:** 15 waves of sprite-based shooting action with bosses, multicolour sprites, and the honest performance lesson. BASIC can manage sprites — but it can't keep up with complex game logic at full speed.

### Phase 4: Polish (Units 49-64)

Title screen, presentation, and the bridge to SID sound.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Title Screen | "STARSWARM" with an animated sprite alien swooping across the title. Sprites work on the title screen too. | Title with active sprites |
| 50 | Attract Mode | Automated demo: sprite player shoots at wave 1 aliens. Shows the game running before the player starts. | Automated sprite demo |
| 51 | Instructions | Controls, alien types (show actual sprites), scoring. One screen. | Visual instructions with sprites |
| 52 | Difficulty Select | Easy (slow aliens, 5 lives), Normal (3 lives), Hard (fast aliens, 2 lives). | Difficulty parameters |
| 53 | Wave Intro | "WAVE 5" in large text, brief alien formation preview, then GO. | Inter-wave pacing |
| 54 | Smooth Transitions | Between waves: aliens fly off screen, brief pause, new wave enters from top. Not instant — choreographed. | Transition animation |
| 55 | Death Animation | Player death: sprite expands (POKE expand registers), changes to explosion shape, shrinks, disappears. 4-frame sequence. | Multi-frame sprite animation |
| 56 | High Score Table | Top 5 scores. Three-initial entry. Displayed on title screen. | Score table |
| 57 | Sprite Priority | POKE 53275: sprite-background priority. Aliens can fly behind character obstacles (future technique). Demonstrate with a character "asteroid" that sprites pass behind. | Sprite priority register |
| 58 | The Hardware Lesson | Unit dedicated to explaining what VIC-II does vs what BASIC does. VIC-II: positions sprites, detects collisions, renders pixels. BASIC: updates position variables, reads collision registers. VIC-II is fast. BASIC is the bottleneck. | Hardware vs software, educational reflection |
| 59 | What Assembly Would Do | Same 8 sprites, same wave patterns. Assembly updates all positions in microseconds. Raster interrupts sync to the display. The VIC-II is never the bottleneck — the 6510 is fast enough to orchestrate everything. | Bridge to assembly, motivation |
| 60 | Bug Sweep | All 15 waves, all difficulty levels. Collision edge cases. Sprite enable/disable lifecycle. | Systematic QA |
| 61 | Performance Final | Time the game loop: wave 1 (~8ms logic per frame?) vs wave 15 (~25ms?). Document where the time goes. | Final performance analysis |
| 62 | Visual Consistency | All sprite shapes consistent in style. Aliens from the same wave look like a family. Colours don't clash. | Visual coherence review |
| 63 | Line Count | Under 500 lines? Sprite DATA (~80 lines for 8 shapes). Wave DATA (~60 lines). Game logic (~350 lines). Should fit. | Code budget |
| 64 | The Finished Game | 15 waves, hardware sprites, multicolour aliens, bosses, explosions, high score table. The C64 doing what it does best — sprites — constrained only by BASIC's speed. | Completion |

**Milestone:** A complete sprite-based shooter. 15 waves, smooth hardware sprites, multicolour aliens, bosses, attract mode, high scores. The learner has mastered every VIC-II sprite register via POKE.

---

## Technical Notes

### Sprite Data Storage

Sprites must be at 64-byte aligned addresses. Using the cassette buffer area (blocks 13-20):

```
Block 13: address 832  → Player ship
Block 14: address 896  → Bullet
Block 15: address 960  → Alien type 1
Block 16: address 1024 → (conflicts with screen!) — use blocks 192+ instead
```

Safer approach: relocate sprite data to 12288+ (blocks 192+) after relocating the character set. Or use blocks 13-15 (832-1023, before screen RAM) for the first 3 sprites and accept the limitation.

Simplest approach for BASIC: use blocks 13, 14, 15 (832-1023) for player, bullet, explosion. Place alien shapes starting at block 192 (12288):

```basic
100 REM LOAD PLAYER SPRITE INTO BLOCK 13
110 FOR I=0 TO 62: READ D: POKE 832+I, D: NEXT
120 POKE 2040, 13: REM SPRITE 0 USES BLOCK 13
```

### Collision Register Behaviour

PEEK(53278) returns which sprites have collided with each other since the last read. **Reading clears the register.** Read it once per frame and store:

```basic
200 C = PEEK(53278)
210 IF (C AND 2) > 0 AND (C AND 4) > 0 THEN ... : REM BULLET HIT ALIEN 0
```

Bit 0 = sprite 0 (player), bit 1 = sprite 1 (bullet), bits 2-7 = sprites 2-7 (aliens).

To detect "bullet hit any alien": check if bit 1 is set AND any of bits 2-7 are set.

### SIN Table for Performance

Calling SIN() every tick is slow. Pre-calculate:

```basic
50 DIM ST(64)
60 FOR I=0 TO 63: ST(I)=INT(SIN(I/10)*30): NEXT
```

Then in the game loop: `X = SX + ST(TICK AND 63)` — array lookup instead of SIN call.

### Memory Budget

- Program logic: ~9-11 KB
- Sprite DATA (8 shapes × 63 bytes in DATA): ~2 KB
- Wave DATA: ~2 KB
- Variables and arrays: ~1 KB
- Total: ~14-16 KB — comfortable

### Line Numbering

- 1-49: Initialisation, sprite data loading, SIN table
- 50-99: POKE setup (border, background, screen)
- 100-149: Title screen, attract mode
- 150-199: Wave loading from DATA
- 200-299: Main game loop
- 300-349: Player movement (joystick, sprite POKE)
- 350-399: Bullet movement and lifecycle
- 400-449: Enemy movement (patterns, sprite POKE)
- 450-499: Collision detection and response
- 500-549: Explosions, scoring, HUD
- 550-599: Wave clear, game over, high score
- 600-699: Boss behaviour
- 700-799: Sprite DATA (player, bullet, aliens, explosions)
- 800-999: Wave DATA (15 waves)

---

## Design Notes

### Why a Sprite Shooter

Sprites are the C64's defining visual feature. After two games using PRINT and POKE to screen RAM, the learner is ready for the VIC-II's real power: hardware sprites that move at pixel precision, detect collisions automatically, and render independently of the background. A shooter is the most natural showcase — sprites were designed for exactly this kind of game.

### The Hardware/Software Split

The game makes the hardware/software split visceral. The sprites are always smooth — the VIC-II renders them at 50fps regardless of what BASIC is doing. But the game logic (position updates, collision checks, wave management) runs in BASIC at 5-10fps. The player sees smooth sprites with jerky position updates. This mismatch is the lesson.

### The Bridge to Game 4

Unit 46 introduces one SID register POKE — just a single note. The player hears the C64's sound chip for the first time through direct hardware access. Game 4 builds an entire soundtrack and sound effects system from these registers.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Replaces old Game 5 (Star Patrol) with a detailed sprite-focused shooter teaching all VIC-II sprite registers via POKE.
