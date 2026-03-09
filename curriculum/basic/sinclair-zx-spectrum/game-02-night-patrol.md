# Game 02: Night Patrol

**Track:** Spectrum BASIC
**Genre:** Top-down stealth game
**Units:** 64 (4 phases × 16 units)
**Language:** Sinclair BASIC
**Max lines:** ~500
**Save/load:** No — each run is 10-15 minutes once skilled

---

## Premise

The name is ironic. Night Patrol is what the guards are doing. You're the reason they're doing it.

You break into a building after dark. Guards walk fixed patrol routes through the corridors. You can see them moving — torchlight bobbing in the darkness — but they can't see you unless you step into their line of sight. Reach the objective (a safe, a document, an exit), avoid detection, get out. Each floor is harder: more guards, tighter routes, longer sightlines.

The game looks and feels like a magazine type-in from Crash or Sinclair User: PRINT AT characters on a grid, simple but tense, "just one more go" addictive.

---

## Core Mechanics

### The Grid

Each floor is a character-cell grid (roughly 28×20 usable area, leaving space for the HUD at the top or bottom). Walls, floors, doors, and objectives are all characters placed with PRINT AT.

| Character | Meaning | INK colour |
|-----------|---------|------------|
| Block (█ or CHR$ 143) | Wall | Blue (1) |
| Space | Floor (walkable) | Black (0) |
| Player (custom or ○) | The intruder | White (7) |
| Guard (custom or ●) | Patrol guard | Red (2) |
| Guard sightline (·) | Detection zone | Dark red (2), dim |
| Objective (★ or ◆) | Target item | Yellow (6) |
| Door (▌) | Passable barrier | Cyan (5) |
| Exit (⊞ or ↑) | Level exit | Green (4) |
| Collectible (•) | Bonus points | Magenta (3) |

### Movement

The player moves one character cell per keypress (or per game-loop tick if a key is held). QAOP or cursor keys. Movement is grid-locked — no sub-cell positioning.

The player cannot move through walls. Walking onto the exit with the objective collected completes the floor.

### Guards

Guards follow fixed patrol routes defined as sequences of directions and step counts:

```
Guard 1: E4, S2, W4, N2 (rectangle patrol)
Guard 2: S8, N8 (corridor pace)
Guard 3: E2, S2, E2, S2, W4, N4 (L-shape)
```

Each guard moves one step per N game-loop ticks (adjustable per floor for difficulty). Guards cycle their route endlessly. They don't react to the player — they're predictable. The challenge is reading and exploiting the pattern.

### Detection

Each guard has a **sightline**: a straight line extending in the direction they're currently facing, until it hits a wall. If the player is anywhere on this sightline, they're detected.

Detection is instant — step into a sightline and you're caught. No grace period, no hiding. This is harsh but fair: the sightlines are visible on screen (dim dots), so the player always knows where danger is.

On detection:
- BEEP (alarm sound)
- Flash the screen red
- Lose a life
- Reset to the floor's start position (guards also reset)

### Fog of War (Optional Enhancement)

Rooms and corridors start dark (INK 0 on PAPER 0 — invisible). As the player moves, nearby cells are revealed permanently. This means the player discovers the layout as they explore — they can't plan a route until they've seen it.

This is a Phase 4 enhancement. The base game works without it (all rooms visible from the start). Fog of war adds replayability and tension but requires more code.

### Objectives

Each floor has one primary objective:
- **Floors 1-3**: Reach the safe (★), GET it, reach the exit
- **Floors 4-6**: Reach the document, GET it, reach the exit (safe is now a decoy)
- **Floors 7+**: Multiple items to collect before the exit opens

Collectible bonus items (•) are scattered for score. Optional — the player can ignore them for a faster, safer run.

---

## Floor Design

### Scale

8-10 floors, increasing in difficulty. Each floor fits on one screen (no scrolling).

### Floor Progression

| Floor | Guards | Patrol speed | Layout | New element |
|-------|--------|-------------|--------|-------------|
| 1 | 1 | Slow | Simple L-corridor | Learn movement and sightlines |
| 2 | 2 | Slow | T-junction | Two guards, timing windows |
| 3 | 2 | Medium | Loop corridor | Guards moving in opposite directions |
| 4 | 3 | Medium | Open rooms with pillars | Line-of-sight blocking, decoy safe |
| 5 | 3 | Medium | Multi-room with doors | Doors block sightlines when closed |
| 6 | 4 | Fast | Long corridors | Tight timing, long sightlines |
| 7 | 4 | Fast | Complex layout | Multiple collectibles required |
| 8 | 5 | Fast | Maze-like | The hardest floor — everything combined |

### Floor Data

Each floor is stored as string data:

```basic
5000 DATA "############################"
5010 DATA "#......#........#..........#"
5020 DATA "#......#........#....*.....#"
5030 DATA "#..............##..........#"
5040 DATA "####..####..####...........#"
```

Where `#` = wall, `.` = floor, `*` = objective, `^` = exit, `@` = player start.

Guard data is separate:

```basic
6000 DATA 2
6010 DATA 10,5,"E4S2W4N2"
6020 DATA 20,8,"S6N6"
```

Line 6000: number of guards. Subsequent lines: start X, start Y, patrol string.

---

## HUD

Two lines at the top or bottom of the screen:

```
FLOOR 3    LIVES: ♥♥♥    SCORE: 0450    ITEM: [SAFE]
```

Or if objective not yet collected:

```
FLOOR 3    LIVES: ♥♥♥    SCORE: 0250    ITEM: ---
```

The HUD uses BRIGHT 1 to stand out from the game area.

---

## Score System

| Action | Points |
|--------|--------|
| Completing a floor | 100 × floor number |
| Collecting a bonus item | 25 |
| Collecting the objective | 50 |
| Speed bonus (floor under par time) | 50 |

Lives: 3. No extra lives. Game over shows final score and floor reached.

---

## Controls

| Key | Action |
|-----|--------|
| Q | Up |
| A | Down |
| O | Left |
| P | Right |
| SPACE | Pause |

QAOP is the Spectrum standard for type-in games. Optional: support cursor keys too (read via IN).

---

## Phase Breakdown

### Phase 1: The Grid (Units 1-16)

A player moves around a single floor. Walls block movement. No guards, no objectives yet. The focus is on PRINT AT, keyboard input, and game loop structure.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | The Dark Building | Title screen. "NIGHT PATROL" in white on black, atmospheric BEEP. Set INK/PAPER/BORDER to black. | CLS, INK, PAPER, BORDER, BEEP, PRINT AT |
| 2 | Drawing Walls | Draw a simple room from hardcoded PRINT AT statements. Wall character in blue, floor in black. | PRINT AT, CHR$, INK, character positioning |
| 3 | The Intruder | Place a player character on screen. PRINT AT player position. | Variables for position (px, py) |
| 4 | Movement | INKEY$ reads keyboard. Q/A/O/P move the player one cell. Player redraws at new position. | INKEY$, IF/THEN, position update |
| 5 | Leaving a Trail | Erase the old position before drawing the new one. PRINT AT old position with space, then PRINT AT new position with player. | Erase-and-redraw pattern, flicker management |
| 6 | Hitting Walls | Before moving, check if the target cell is a wall. ATTR or SCREEN$ to read what's there. Don't move if it's a wall. | ATTR function, collision detection, look-before-move |
| 7 | Floor Data | Move the room layout into DATA strings. Loop reads each row and PRINT ATs the characters. | DATA, READ, FOR/NEXT, string indexing |
| 8 | A Proper Room | Design a proper floor layout — corridors, corners, a room with a door. Still hardcoded as DATA, but it looks like a building. | Level design, DATA layout, visual design |
| 9 | The Game Loop | Structure the code: initialise → draw floor → main loop (input → update → draw) → repeat. GOSUB for each phase. | Game loop architecture, GOSUB/RETURN |
| 10 | Speed Control | The game loop runs at different speeds on different Spectrums. Add a PAUSE or timing loop to normalise speed. | PAUSE, timing, frame rate |
| 11 | The Objective | Place an objective character (★) on the floor. Walk over it to "collect" it. Track whether it's been collected. | State flags, conditional display |
| 12 | The Exit | Place an exit character. Exit only works if objective is collected. Walk onto exit → floor complete message. | Win condition, multi-state logic |
| 13 | Floor Complete | "FLOOR COMPLETE" message with score. BEEP fanfare. Pause, then... what? For now, restart the same floor. | Victory feedback, score display |
| 14 | Multiple Floors | Load floor 2 from DATA after completing floor 1. Floor number increments. Different layout each time. | Multiple DATA blocks, RESTORE to specific lines |
| 15 | Three Floors | Three complete floor layouts. Player progresses through all three. Floor counter in HUD. | Data organisation, progression |
| 16 | The HUD | Status bar showing floor number, lives (just display for now — no death yet), and score. BRIGHT 1 to distinguish from game area. | HUD design, PRINT AT for fixed UI, BRIGHT |

**Milestone:** A working game with three floors. Player moves through corridors, collects objectives, reaches exits, progresses through floors. No enemies yet — but the movement feels solid and the floors look like a real building.

### Phase 2: The Guards (Units 17-32)

Guards appear, patrol, and detect the player. The game becomes tense.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | A Stationary Guard | One guard character on the floor. Red INK. Doesn't move. If player walks onto guard's cell, detection. | New character type, simple collision |
| 18 | Detection | When detected: BEEP alarm, FLASH screen, "DETECTED!" message, reset player to start. Lose a life. | FLASH, BEEP, game state reset |
| 19 | Lives and Game Over | Three lives. Lose all three → game over screen with final score. | Life counter, game over state |
| 20 | Guard Movement | The guard takes one step along a predefined path each game tick. Moves like the player: erase, update position, redraw. | NPC movement, shared erase-redraw pattern |
| 21 | Patrol Routes | Guard follows a route string: "E4S2W4N2". Parse the string: direction + count. Guard walks 4 east, 2 south, 4 west, 2 north, then repeats. | String parsing, direction encoding, route cycling |
| 22 | Route Data | Move patrol routes into DATA. Read at floor load. Guard position, route string, current step all tracked in arrays. | Parallel arrays, guard state |
| 23 | Two Guards | Second guard with a different route. Both move independently each tick. | Multiple NPC management, array indexing |
| 24 | Patrol Timing | Guards don't move every tick — they move every N ticks (slower than the player). Adjust N per floor for difficulty. | Tick counters, speed control, difficulty tuning |
| 25 | Sightlines | Each guard faces the direction they last moved. A line of dots extends from the guard in that direction until hitting a wall. | Line drawing with PRINT AT, directional logic |
| 26 | Sightline Detection | If the player occupies any cell on a guard's sightline, detection triggers. Check after every player move AND every guard move. | Array/line search, detection check |
| 27 | Sightline Display | Show sightlines as dim dots (dark red or similar). Player can SEE where danger is. Update sightlines when guards turn corners. | Visual feedback, dynamic display update |
| 28 | Guard Turning | When a guard changes direction (corner of patrol route), the sightline changes too. Old sightline erased, new one drawn. | State change, cleanup on direction change |
| 29 | Timing Windows | With visible sightlines and predictable patrols, the player can time their crossing. Test: is Floor 1 solvable? Adjust guard route if needed. | Playtesting, difficulty balance |
| 30 | Floor 2 Guards | Floor 2 gets two guards with routes that create timing puzzles. Player must wait for a gap between sightlines. | Level design with guard patterns |
| 31 | Floor 3 Guards | Floor 3 gets faster guards or tighter routes. The difficulty ramp should feel fair but challenging. | Difficulty progression, pacing |
| 32 | Detection Polish | Vary detection response: alarm BEEP sequence (not just one tone), brief red border flash, slight pause before reset. Make it feel dramatic, not frustrating. | Sound design, feedback feel, pacing |

**Milestone:** Guards patrol corridors with visible sightlines. The game is now a stealth puzzle: watch the patterns, find the gap, move. Three floors with increasing guard count and speed. Detection is dramatic and fair.

### Phase 3: Depth (Units 33-48)

More floors, more mechanics, more reasons to replay.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | Doors | Door characters block sightlines but not movement. Walk through a door and it closes behind you — safe from the guard on the other side. | Terrain types, sightline blocking |
| 34 | Door Behaviour | Doors close after the player passes through (1-2 tick delay). A guard's sightline stops at a closed door but passes through an open one. | Timed state change, interaction between systems |
| 35 | Bonus Collectibles | Scatter bonus items (•) on floors. 25 points each. Optional — greedy players risk more exposure for a higher score. | Risk/reward design, optional objectives |
| 36 | Floor 4: The Open Plan | An open room with pillars. Guards can see long distances. Pillars block sightlines. Different feel from corridors. | Open layout design, sightline blocking geometry |
| 37 | Floor 5: Doors and Rooms | Multi-room layout where doors are essential for survival. Guards patrol between rooms. | Complex level using all existing mechanics |
| 38 | Floor 6: Long Corridors | Long straight corridors with fast guards. Tight timing. Nowhere to hide except side rooms. | Speed challenge, tension design |
| 39 | Floor 7: Multiple Items | Exit doesn't open until ALL collectibles are gathered. Forces the player to explore the whole floor. | Multi-item objective, exit gating |
| 40 | Floor 8: The Vault | The final floor. Five guards, fast patrols, a maze-like layout. Everything combined. | Capstone level, combined difficulty |
| 41 | Par Times | Each floor has a par time (in game ticks). Beat par = 50 bonus points. Display "UNDER PAR!" on floor complete. | Timer tracking, bonus conditions |
| 42 | High Score | Track the best score across runs (in memory — lost on power off). Display on game over and title screen. | Persistent state within session, max tracking |
| 43 | Floor Intro | Brief text before each floor: "Floor 3: The Loop. Two guards patrol in opposite directions." Context and warning. | Inter-level narrative, pacing |
| 44 | Guard Variety | Some guards move faster. Some have longer sightlines (carry a brighter torch). Visual distinction: BRIGHT 1 for alert guards. | Enemy variety, visual differentiation |
| 45 | Sound Design | Different BEEPs for: footsteps (very quiet tick), collecting items (rising note), approaching a sightline (low warning hum — optional, if detectable). | Audio feedback layers, BEEP variety |
| 46 | Death Animation | On detection, brief animation: guard turns to face player, exclamation mark appears, alarm sounds THEN reset. Not instant — dramatic. | Sequential animation, PAUSE for timing |
| 47 | Victory Sequence | Complete all 8 floors: "YOU ESCAPED!" Ascending BEEP scale, final score, guard count avoided. Sense of achievement. | End game sequence, stats summary |
| 48 | Balance Pass | Play all 8 floors in sequence. Is the difficulty curve right? Are any floors unfair? Adjust guard routes and speeds. | Full playtesting, balance iteration |

**Milestone:** Eight complete floors with doors, bonus items, par times, guard variety, and a victory sequence. The game has depth and replayability — players will retry for higher scores and faster times.

### Phase 4: Polish (Units 49-64)

Make it feel professional. Title screen, visual polish, optional fog of war, final testing.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Title Screen | "NIGHT PATROL" title with atmospheric design. Building silhouette in block characters? Flickering window lights? | PRINT AT art, visual design |
| 50 | Instructions | "HOW TO PLAY" screen. Controls, objective, what guards and sightlines mean. Brief — one screen. | User onboarding, clear writing |
| 51 | Difficulty Select | Easy (slow guards, short sightlines), Normal, Hard (fast guards, long sightlines). Affects guard tick rate and sightline length. | Difficulty as parameter, config variables |
| 52 | Floor Transition | Smooth transition between floors: current floor fades (INK changes to black), new floor draws. Not instant. | Transition effects, INK animation |
| 53 | Colour Themes | Each floor has a different wall colour. Floor 1: blue walls. Floor 4: green. Floor 8: red. Variety without new code. | Palette as atmosphere, colour per level |
| 54 | Fog of War | Cells start hidden (INK 0 on PAPER 0). Reveal a 3×3 area around the player as they move. Previously seen cells stay visible. | Visibility arrays, reveal radius |
| 55 | Fog and Guards | Guards are only visible when in revealed cells. Sightlines only visible in revealed areas. This makes fog of war feel fair — you can see danger, but only where you've been. | Conditional rendering, fog interaction |
| 56 | Guard Footsteps | When a guard moves in an unrevealed area, play a quiet BEEP. The player can HEAR guards they can't see. Directional? (louder = closer) | Audio as information, distance calculation |
| 57 | The Minimap | Small 8×6 minimap in the HUD corner showing explored areas as dots. Player position blinking. Guards as red dots (if visible). | Scaled rendering, minimap design |
| 58 | Response Feel | Tune the game loop so input feels responsive. Player should move the instant a key is pressed, not on the next tick. | Input responsiveness, loop timing |
| 59 | Visual Polish | Consistent character design across all floors. Guard character looks distinct from all directions (or just one icon). Objective sparkles (alternate between two characters). | Visual consistency, animation via alternation |
| 60 | Edge Cases | What if the player stands still and a guard walks into them? (Detection.) What if a guard patrols over the objective? (Objective reappears when guard leaves.) | Edge case handling, robust state |
| 61 | Bug Sweep | Every floor, every guard route, every door, every sightline. Systematic testing. | QA methodology |
| 62 | Difficulty Curve | Play Easy through all floors, then Normal, then Hard. Is each mode fair? Is Hard actually hard? | Multi-difficulty testing |
| 63 | Line Count | Are we under 500 lines? If fog of war pushes us over, it becomes a documented "extended version" — the base game stays under 500. | Code budget, scope management |
| 64 | The Finished Game | Clean listing. Title, difficulty select, 8 floors, guards, sightlines, fog of war (if under budget), high score, victory. A complete game. | Completion, final review |

**Milestone:** A polished stealth game. 8 floors, predictable but challenging guard patrols, visible sightlines, optional fog of war, difficulty select, par times, high scores. The kind of game that would fill two pages of a magazine listing and keep you playing all weekend.

---

## Technical Notes

### Game Loop

```
Main loop:
  1. Read input (INKEY$)
  2. Move player (if valid)
  3. Check sightline detection
  4. Increment guard tick counter
  5. If guard tick: move all guards, update sightlines
  6. Check sightline detection again (guard moved into view of player)
  7. Check objective collection
  8. Check exit condition
  9. Update HUD
  10. GO TO main loop
```

Detection is checked twice per loop: after the player moves (did they step into a sightline?) and after guards move (did a sightline sweep over the player?).

### Sightline Calculation

For each guard, extend a line from their position in their facing direction:

```basic
500 REM DRAW SIGHTLINE FOR GUARD g
510 LET sx = gx(g): LET sy = gy(g)
520 LET dx = gdx(g): LET dy = gdy(g)
530 FOR i = 1 TO 20
540   LET sx = sx + dx: LET sy = sy + dy
550   IF sx < 1 OR sx > 28 OR sy < 1 OR sy > 20 THEN GO TO 590
560   IF ATTR(sy, sx) = wall_colour THEN GO TO 590
570   PRINT AT sy, sx; INK 2; "."
580 NEXT i
590 RETURN
```

Before drawing a new sightline, erase the old one by reprinting floor characters over the old dots. This is the most complex piece of code in the game — but it's just a FOR loop with PRINT AT.

### Guard State

Parallel arrays:

```
gx()    - guard X position
gy()    - guard Y position
gdx()   - current movement direction X (-1, 0, 1)
gdy()   - current movement direction Y (-1, 0, 1)
gr$()   - patrol route string
gs()    - current step within route
gc()    - steps remaining in current direction
```

### Floor Data Format

```
DATA "############################"    : REM row 1 of floor layout
...
DATA 3                                 : REM number of guards
DATA 10, 5, "E4S2W4N2"               : REM guard 1: x, y, route
DATA 20, 8, "S6N6"                    : REM guard 2
DATA 15, 12, "W3S3E3N3"              : REM guard 3
DATA 14, 3                            : REM objective position (x, y)
DATA 2, 18                            : REM exit position (x, y)
DATA 2, 2                             : REM player start (x, y)
DATA 180                              : REM par time (game ticks)
```

### Memory Budget

Tighter than The Cursed Manor because the game loop is more code-dense:
- Floor data (8 floors × ~20 DATA lines): ~3-4 KB
- Game logic, guard AI, sightlines, parser: ~8-10 KB
- Variables and arrays: ~1 KB
- Total: ~12-15 KB — well within 48K BASIC limits

### Line Numbering

- 1-99: Initialisation, difficulty select
- 100-199: Title screen and instructions
- 200-299: Floor loading (READ DATA, draw floor)
- 300-399: Main game loop
- 400-499: Player movement and collision
- 500-599: Guard movement and sightlines
- 600-699: Detection, lives, game over
- 700-799: HUD, score, floor complete
- 800-899: Fog of war (if implemented)
- 900-999: Victory sequence, high score
- 1000-1999: Floor DATA (8 floors)
- 2000+: Guard route DATA

---

## Design Notes

### Why This Game Works in BASIC

BASIC's speed limitation is actually an asset here. The player moves one cell per keypress. Guards move one cell per N ticks. The game is inherently turn-like — not twitch action, but pattern reading and timing. BASIC can handle this pace.

The sightline calculation is the most expensive operation, but it only runs when guards move (not every tick). With 3-5 guards and sightlines of 10-15 cells, the calculation is ~50-75 ATTR checks per guard move — fast enough.

### Why Stealth, Not Chase

Chase games (enemy follows player) are simple but monotonous — the player just runs. Stealth games (player reads patterns, finds gaps) create tension through knowledge: "I can see the guard will turn left in 3 steps, giving me 4 steps to cross." This is more interesting gameplay AND better teaching material. The learner implements predictable AI (patrol routes) rather than reactive AI (pathfinding), which is both simpler and more game-design-educational.

### The Magazine Test

Would this fill two pages of a Crash type-in listing and keep someone playing all weekend? The answer should be yes: 8 floors of increasing difficulty, visible sightlines creating puzzle-like tension, optional bonus items for score chasers, difficulty select for replayability, par times for speedrunners. It's a complete game, not a demo.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. New Game 2 in the restructured BASIC track. Stealth game concept (intruder avoiding guards with visible sightlines).
