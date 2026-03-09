# Game 02: Neon Nexus

**Track:** C64 BASIC
**Genre:** Character grid action game
**Units:** 64 (4 phases × 16 units)
**Language:** Stock BASIC V2
**Max lines:** ~500
**Save/load:** No — each run is 5-15 minutes

---

## Premise

A dark maze pulsing with neon light. You move through corridors collecting data fragments while security programs hunt you down. The maze is built from PETSCII characters, POKEd directly to screen memory at $0400. Colour RAM at $D800 paints each cell in vivid neon: cyan walls, magenta hazards, yellow collectibles, green exits. The player moves with the joystick, and every game element — walls, floors, enemies, items — is a byte at a memory address.

This is the C64 doing what magazine type-ins did: PEEK and POKE to screen RAM. The game looks like Tron. It plays like Pac-Man meets a heist.

---

## Core Mechanics

### The Maze

Each level is a 38×22 grid (leaving row 0 and row 24 for the HUD). The maze is drawn by POKEing character codes to screen RAM (1024-2023) and colour values to colour RAM (55296-56295).

| Element | Character | Screen code | Colour |
|---------|-----------|-------------|--------|
| Wall | █ (solid block) | 160 | Cyan (3) |
| Floor | Space | 32 | Black (0) |
| Player | ● | 81 | White (1) |
| Hunter (patrol) | ◆ | 122 | Red (2) |
| Hunter (alert) | ◆ | 122 | Light red (10) |
| Data fragment | * | 42 | Yellow (7) |
| Power cell | ♦ | 90 | Green (5) |
| Exit | ↑ | 94 | Light green (13) |
| Trail (fading) | · | 46 | Dark grey (11) |

### Movement

Joystick in port 2: `J = PEEK(56320)`. Bit masking for directions:
- `(J AND 1) = 0` → up
- `(J AND 2) = 0` → down
- `(J AND 4) = 0` → left
- `(J AND 8) = 0` → right

The player moves one cell per game tick. Before moving, PEEK the target cell — if it's a wall (character 160), the move is blocked. If it's a data fragment (42), collect it. If it's a hunter (122), game over.

### Hunters

Security programs that patrol the maze. Two types:

**Patrol hunters**: Follow fixed routes through the corridors. Predictable, like Night Patrol's guards. The player learns their patterns and times their crossing.

**Alert hunters**: Activated when the player collects more than half the data fragments. They move toward the player using simple chase AI (compare positions, move in the direction that reduces distance). Slower than the player — but relentless.

Hunters are drawn with POKE, same as everything else. Their movement erases the old position (POKE with floor character) and draws the new position (POKE with hunter character). Colour RAM is updated simultaneously.

### Data Fragments

Scattered throughout the maze. Collect all to unlock the exit. Each fragment collected:
- Score increases
- Fragment counter updates in HUD
- Brief colour flash on the collected cell (POKE colour RAM to white, then back to black after 1 tick)

### Power Cells

Rare collectibles (1-2 per level) that temporarily freeze all hunters for 5 seconds. The freeze is visible: hunter colours change to dark grey. The player has a window to pass through dangerous areas.

### The Exit

Locked until all data fragments are collected. When unlocked, it appears on the maze (POKE to the exit cell). Reach it to complete the level.

### The Trail

As the player moves, they leave a fading trail — cells they've passed through briefly show a dot in dark grey before fading to black. This helps the player see where they've been, especially in complex mazes. No gameplay effect — purely visual.

---

## Level Design

### Scale

12 levels, increasing in complexity.

### Progression

| Level | Size | Fragments | Hunters | Hunter speed | New element |
|-------|------|-----------|---------|-------------|-------------|
| 1 | Simple corridors | 5 | 1 patrol | Slow | Learn movement and PEEK/POKE |
| 2 | L-shaped corridors | 8 | 1 patrol | Slow | More fragments, longer route |
| 3 | Grid corridors | 10 | 2 patrol | Slow | Two hunters, timing needed |
| 4 | Open rooms + corridors | 12 | 2 patrol | Medium | Open spaces, less cover |
| 5 | Complex maze | 15 | 2 patrol + 1 alert | Medium | Alert hunter introduction |
| 6 | Wide corridors | 15 | 3 patrol | Medium | More simultaneous threats |
| 7 | Multiple rooms | 18 | 2 patrol + 1 alert | Fast | Speed increase |
| 8 | Narrow passages | 18 | 3 patrol + 1 alert | Fast | Tight spaces, less escape room |
| 9 | Maze with dead ends | 20 | 3 patrol + 2 alert | Fast | Dead ends are dangerous |
| 10 | Open arena | 22 | 4 patrol + 2 alert | Fast | Minimal cover |
| 11 | Labyrinth | 25 | 4 patrol + 2 alert | Very fast | Complex, disorienting |
| 12 | The Core | 30 | 5 patrol + 3 alert | Very fast | Everything combined |

### Level Data

Levels are stored as DATA strings — one string per maze row:

```basic
5000 DATA "########################################"
5010 DATA "#......#........#....*..........#......#"
5020 DATA "#......#........#..............##......#"
```

Where `#`=wall, `.`=floor, `*`=data fragment, `P`=power cell, `@`=player start, `^`=exit location, `1-9`=hunter start positions.

---

## Visual Design

### The Neon Look

The C64's colour RAM allows per-character colour. The maze walls are cyan (dark neon), the background is black, and the game elements pop in bright colours. The effect is a dark room lit by neon — the grid-like display of PETSCII characters actually enhances the Tron aesthetic.

### Screen Update Pattern

Every game tick:
1. Erase player at old position: `POKE 1024 + OY*40 + OX, 32` (space) + colour
2. Erase hunter at old position: same pattern
3. Calculate new positions
4. PEEK new positions for collision
5. POKE player at new position: `POKE 1024 + PY*40 + PX, 81` + `POKE 55296 + PY*40 + PX, 1`
6. POKE hunters at new positions

This erase-move-draw cycle is the fundamental pattern for all C64 character-based games. It's the same concept as assembly's LDA/STA to screen RAM — just slower.

---

## Phase Breakdown

### Phase 1: The Maze (Units 1-16)

Build and display a maze. Move the player through it. No enemies, no items yet.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | Screen Memory | POKE 1024, 81 puts a ball on screen. POKE 1024+1, 81 puts one next to it. The screen IS memory. | POKE, screen RAM address (1024), direct hardware |
| 2 | Colour RAM | POKE 55296, 1 colours that character white. Every character has a colour byte 54272 addresses above its screen byte. | Colour RAM (55296), per-character colour |
| 3 | Border and Background | POKE 53280, 0 (border black). POKE 53281, 0 (background black). The neon look starts here. | VIC-II border/background registers |
| 4 | Drawing a Wall | POKE a row of solid blocks (character 160) in cyan. A wall appears on screen. | Loops with POKE, character codes |
| 5 | Drawing a Row | FOR loop POKEs a complete row from a DATA string. Read each character, translate to screen code, POKE it. | DATA strings, MID$, character translation |
| 6 | Drawing the Maze | Read all 22 rows of DATA, POKE the entire maze. The screen fills with neon corridors. | Full maze rendering, nested loops |
| 7 | Colour the Maze | Second pass: POKE colour RAM for every cell. Walls=cyan, floor=black. Different elements get different colours. | Colour RAM pass, dual-POKE pattern |
| 8 | The Player | POKE the player character at the start position. White, bright, distinct from the maze. | Player rendering, position variables |
| 9 | Joystick Input | J=PEEK(56320). Bit masking for directions. First real-time input — the joystick is a memory address. | PEEK, bit masking (AND), joystick reading |
| 10 | Player Movement | Move the player: erase old position (POKE space), POKE new position. Feels immediate. | Erase-move-draw pattern |
| 11 | Wall Collision | Before moving, PEEK the target cell. If it's character 160 (wall), don't move. PEEK is collision detection. | PEEK for collision, look-before-move |
| 12 | Smooth Movement | Tune the game loop speed. The player should move responsively but not too fast. FOR/NEXT delay loop. | Timing control, game feel |
| 13 | Multiple Mazes | Load level 2 from DATA after completing level 1 (for now, "complete" = reach a specific cell). Different layout. | Multiple DATA blocks, level loading |
| 14 | The HUD | Top row: level number, score, fragment counter, lives. POKEd directly to row 0 of screen memory. | HUD via screen POKE, formatted display |
| 15 | Three Mazes | Three complete maze layouts. Player progresses through them. | Data organisation, progression |
| 16 | Level Transition | Clear screen (POKE 32 to all cells), brief "LEVEL 2" message, draw new maze. Transition feel. | Screen clearing, inter-level pacing |

**Milestone:** Three explorable mazes with neon colours. Player moves with the joystick, blocked by walls. Feels like a real game — just missing enemies and items.

### Phase 2: The Hunt (Units 17-32)

Data fragments, hunters, and the game loop.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | Data Fragments | POKE fragment characters (* in yellow) at specific maze positions. Walk over one → it disappears, score increases. | Collectible objects, PEEK-to-collect |
| 18 | Fragment Counter | HUD shows "DATA: 3/10". Decrements as fragments are collected. | Counter display, progress tracking |
| 19 | The Exit | When all fragments collected, POKE the exit character at the exit position. Walk onto it → level complete. | Conditional appearance, level completion |
| 20 | One Patrol Hunter | A hunter character on screen. Follows a fixed route (DATA string of directions). Moves one cell per N ticks. | NPC movement, route following |
| 21 | Hunter POKE/PEEK | Hunter erases old position, PEEKs new position (check for wall), POKEs new position. Same pattern as the player. | Shared movement pattern for NPCs |
| 22 | Collision with Hunter | If the player PEEKs a hunter at their target cell, or a hunter PEEKs the player at its target cell: caught. Lose a life. | Bidirectional collision, death handling |
| 23 | Death and Respawn | Caught: brief flash (POKE colour RAM to red on player cell), BEEP-equivalent sound, respawn at maze start. Lives decrement. | Death animation, respawn, lives |
| 24 | Two Hunters | Second hunter with a different route. Both move independently. Game loop handles N hunters. | Multiple NPC arrays, indexed movement |
| 25 | Hunter Timing | Hunters move every N ticks. Player moves every tick. The player is faster — but not by much. | Speed differential, tick counting |
| 26 | Alert Hunters | After collecting half the fragments, one hunter becomes alert: it moves toward the player instead of following a route. | Chase AI, mode switching |
| 27 | Simple Chase AI | Alert hunter: compare positions, move in the axis with the larger difference. Check for walls before moving. | AI direction choice, Manhattan distance |
| 28 | Power Cells | Rare collectible. Collecting one freezes all hunters for 5 seconds (N ticks). Hunters turn grey during freeze. | Timed power-up, global state change |
| 29 | Game Over | Zero lives → "GAME OVER" screen. Show final score and level reached. High score comparison. | Game over state, score display |
| 30 | Sound | CHR$(7) for collection. Border flash (POKE 53280 to white then back) for death. No SID yet — that's Game 4. | Minimal audio, visual feedback |
| 31 | Levels 1-6 | Design 6 maze layouts with hunter routes. Increasing fragment count and hunter count. | Level design, balance |
| 32 | Six Levels Playable | Smooth progression through 6 levels. Hunters get faster and more numerous. Alert hunters appear from level 5. | Integration milestone |

**Milestone:** A complete maze chase game with data fragments, patrol and alert hunters, power cells, lives, and 6 levels. PEEK and POKE are second nature.

### Phase 3: Depth (Units 33-48)

All 12 levels, visual polish, and the features that make it replayable.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | The Trail | Player leaves fading dots behind (POKE dot character in dark grey, then erase after 3 ticks). Shows where you've been. | Timed visual effect, trail array |
| 34 | Fragment Radar | When near an uncollected fragment (within 3 cells), its colour pulses brighter. Helps navigation in complex mazes. | Distance check, colour pulsing |
| 35 | Hunter Warning | When an alert hunter is within 5 cells, the border subtly changes to dark red. Ambient threat indicator. | Distance-based warning, border colour |
| 36 | Level 7-9 | Three more mazes. Faster hunters, narrow passages, dead ends. | Harder level design |
| 37 | Level 10-12 | Final three mazes. Maximum difficulty. Level 12 is a dense labyrinth with 8 hunters. | End-game design |
| 38 | Score Multiplier | Collecting fragments in quick succession (within N ticks) builds a multiplier: ×2, ×3, ×4. Broken by pausing. | Combo system, time-windowed tracking |
| 39 | Level Timer | Each level has a par time. Beating par adds bonus points. Timer in HUD counts up. | Timer, par system |
| 40 | High Score Table | Top 5 scores tracked in session. Enter 3-letter initials on game over. | Score table, initial entry |
| 41 | Difficulty Select | Easy (slow hunters, more power cells), Normal, Hard (fast hunters, fewer power cells, alert hunters from level 3). | Difficulty parameters |
| 42 | Level Select | After completing a level, it's unlocked for replay. A level-select screen shows which levels are available. | Unlock progression, menu |
| 43 | Colour Themes per Level | Each level has a wall colour: levels 1-3 cyan, 4-6 green, 7-9 magenta, 10-12 red. Atmosphere shifts with difficulty. | Per-level colour parameter |
| 44 | Between-Level Briefing | "LEVEL 7: THE LABYRINTH — 18 fragments, 3 hunters, 1 alert" displayed before the maze appears. | Inter-level information, pacing |
| 45 | Hunter Patrol Variety | Some patrol hunters speed up on their route (fast on straightaways, pause at corners). More realistic movement. | Variable-speed patrol, route modifiers |
| 46 | Edge Cases | Hunter and player move to the same cell simultaneously — caught. Two hunters collide — they pass through each other (they're programs, not physical). | Simultaneous movement, NPC collision rules |
| 47 | Bug Sweep | Every level, every hunter route, every fragment position. Systematic testing. | QA methodology |
| 48 | Balance Pass | Play all 12 levels on all difficulties. Smooth difficulty curve? Any unfair levels? | Full playthrough, balance |

**Milestone:** 12 levels with visual variety, score multiplier, par times, high score table, difficulty select. A complete, replayable game.

### Phase 4: Polish and Bridge (Units 49-64)

Title screen, final polish, and the bridge to sprites (Game 3).

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Title Screen | "NEON NEXUS" — POKE large letters to screen memory in neon colours. Animated maze fragments in the background. | POKE-based title art |
| 50 | Attract Mode | Demo: automated player moves through level 1. Show the game in action before the player starts. | Automated input, attract loop |
| 51 | Instructions | One screen: controls, elements (with their characters and colours shown), and objective. | Visual instructions |
| 52 | Smooth Screen Clear | Instead of instant clear, animate: POKE columns to black from left to right. Wipe effect. | Animated transition via sequential POKE |
| 53 | Hunter Death Stare | When caught, the hunter "looks at" the player for a brief moment before the death sequence. POKE the hunter to face the player. | Directional character, dramatic pause |
| 54 | Completion Celebration | Beat level 12: cascade animation (walls change colour from top to bottom), "ACCESS GRANTED" message, total score and time. | Victory sequence, cascading colour |
| 55 | Speed Optimisation | Only POKE cells that changed, not the entire screen each tick. Player: 2 POKEs (erase old, draw new). Hunters: 2 POKEs each. | Selective update, performance |
| 56 | What POKE Can't Do | Discussion: POKE to screen RAM gives character-cell resolution (8×8 pixels). For smooth movement within a cell, you need sprites. That's Game 3. | Limitations, motivation for sprites |
| 57 | Keyboard Alternative | PEEK(197) for keyboard input alongside joystick. Some players prefer keys. Support both. | Dual input, PEEK(197) keyboard matrix |
| 58 | Run-Length Encoding | Maze DATA takes many lines. Compress: "W10F3W5" = 10 walls, 3 floors, 5 walls. Saves DATA lines for the line budget. | Simple compression, DATA efficiency |
| 59 | Final Bug Hunt | Edge case: what if all fragments spawn behind hunters? (Ensure at least one safe path.) What if the player doesn't move? (Hunters still patrol.) | Design validation |
| 60 | Performance Profiling | Time the game loop at level 1 (2 hunters) vs level 12 (8 hunters). Each hunter adds ~10ms. Is level 12 playable? | Performance measurement |
| 61 | Final Colour Pass | Review every level's colour scheme. Are hunters visible against all wall colours? Is yellow readable on every background? | Visual accessibility |
| 62 | Final Sound Pass | Every event has feedback — even if just a border flash. No silent interactions. | Feedback completeness |
| 63 | Line Count | Under 500 lines? 12 maze DATAs are the biggest cost (~180 lines). Game logic ~300 lines. Tight. | Scope management |
| 64 | The Finished Game | Clean listing. Title, attract mode, 12 levels, hunters, power cells, trail, score multiplier, high score table. PEEK and POKE mastery. | Completion |

**Milestone:** A polished maze game that looks like Tron, plays like a heist, and teaches PEEK/POKE as the fundamental way to interact with C64 hardware.

---

## Technical Notes

### Screen Memory Map

```
Screen RAM: 1024-2023 (40 columns × 25 rows)
Colour RAM: 55296-56295 (same layout, one colour byte per character)

Cell address = BASE + ROW * 40 + COLUMN
Screen: 1024 + Y*40 + X
Colour: 55296 + Y*40 + X
```

### Joystick Reading

```basic
100 J = PEEK(56320)
110 IF (J AND 1)=0 THEN DY=-1: DX=0
120 IF (J AND 2)=0 THEN DY=1: DX=0
130 IF (J AND 4)=0 THEN DX=-1: DY=0
140 IF (J AND 8)=0 THEN DX=1: DY=0
```

Active-low: bit is 0 when direction pressed. AND masks the relevant bit.

### PEEK for Collision

```basic
200 NX=PX+DX: NY=PY+DY
210 NC=PEEK(1024+NY*40+NX)
220 IF NC=160 THEN 300: REM WALL - CAN'T MOVE
230 IF NC=42 THEN GOSUB 500: REM FRAGMENT - COLLECT
240 IF NC=122 THEN GOSUB 600: REM HUNTER - CAUGHT
250 REM SAFE TO MOVE
260 POKE 1024+PY*40+PX, 32: POKE 55296+PY*40+PX, 0
270 PX=NX: PY=NY
280 POKE 1024+PY*40+PX, 81: POKE 55296+PY*40+PX, 1
```

### Memory Budget

- Program logic: ~8-10 KB
- Maze DATA (12 levels): ~5-6 KB
- Arrays (hunter state, trail, fragments): ~1 KB
- Total: ~14-17 KB — comfortable

### Line Numbering

- 1-49: Initialisation, POKE setup (border, background)
- 50-99: Title screen, attract mode
- 100-199: Maze loading (DATA → screen POKE)
- 200-299: Main game loop
- 300-349: Player movement, joystick, collision
- 350-399: Hunter movement (patrol + chase)
- 400-449: Fragment collection, power cells
- 450-499: HUD update, score, lives
- 500-549: Death, respawn, game over
- 550-599: Level transitions, completion
- 600-699: High score, menus, difficulty
- 700-799: Animations, trail, radar
- 800-999: Level DATA (12 mazes × ~20 lines + hunter routes)

---

## Design Notes

### Why a Maze Game

The C64 BASIC track's second game needs to teach POKE to screen RAM and colour RAM. A maze game is the perfect vehicle: every wall, floor, enemy, and item is a POKE. Collision detection is a PEEK. The entire game is "write bytes to memory, read bytes from memory." This IS how C64 BASIC games worked — and it's one step from assembly's LDA/STA to the same addresses.

### The Neon Aesthetic

PETSCII characters on a black background in bright colours naturally look like neon. The C64's colour palette (16 colours including cyan, magenta, light green) supports this. The "Neon Nexus" theme isn't forced — it emerges from the hardware. Block characters in cyan on black ARE neon walls.

### Patrol vs Chase

Patrol hunters are predictable (like Night Patrol's guards). Alert hunters introduce chase AI when the game needs more pressure (after half the fragments are collected). This two-phase system creates a pacing shift within each level: the early half is methodical exploration, the late half is tense evasion.

### The Bridge to Game 3

Unit 56 explicitly discusses what POKE to screen RAM can't do: sub-cell movement, smooth animation, overlapping objects. VIC-II sprites solve all three — and they're also memory addresses (53248-53294). The jump from POKEing screen RAM to POKEing sprite registers is conceptually small but visually dramatic.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Replaces old Game 3 (Pixel Serpent, snake game) with a neon maze game teaching PEEK/POKE to screen and colour RAM.
