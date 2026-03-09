# Game 01: Depth Charge

**Track:** C64 BASIC
**Genre:** Grid-based naval strategy
**Units:** 64 (4 phases × 16 units)
**Language:** Stock BASIC V2
**Max lines:** ~500
**Save/load:** No — each game is 10-20 minutes

---

## Premise

You command a destroyer on the surface. Somewhere below, submarines lurk on a hidden grid. Drop depth charges at grid coordinates. A hit shows an explosion. A miss shows the depth — how close you came. Sink all submarines before you run out of charges.

It's Battleships meets Minesweeper, but with a twist: near-misses give depth readings instead of simple "miss" feedback. A charge that lands one cell away from a sub reports "SONAR: CLOSE" with a direction indicator. Two cells away: "SONAR: FAINT". This turns a guessing game into a deduction game — the player triangulates sub positions from sonar returns.

No POKE. No PEEK. No hardware trickery. Pure BASIC: PRINT, INPUT, arrays, logic. A real game from line 1.

---

## Core Mechanics

### The Grid

A 10×10 grid representing ocean depth. Columns A-J, rows 1-10. The grid is displayed using PRINT statements — no screen memory manipulation.

```
    A  B  C  D  E  F  G  H  I  J
 1  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
 2  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
 3  ~  ~  *  ~  ~  ~  ~  ~  ~  ~
 4  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
 5  ~  ~  ~  ~  ~  ~  X  ~  ~  ~
```

- `~` = unexplored
- `*` = hit (submarine fragment)
- `X` = miss (depth charge detonation)
- `!` = sonar return (near miss with direction hint)
- `#` = sunk submarine (all cells revealed)

### Submarines

Each game places 4-5 submarines of varying sizes:

| Type | Size | Count |
|------|------|-------|
| Patrol sub | 2 cells | 2 |
| Attack sub | 3 cells | 1-2 |
| Missile sub | 4 cells | 1 |

Submarines are placed horizontally or vertically, not diagonally. They don't overlap. Placement is random each game.

### Depth Charges

The player has a limited supply: 40 charges for a standard game. Each turn, the player enters a coordinate (e.g., "D5"). The game reveals:

- **HIT**: "DIRECT HIT AT D5! Hull breach detected!" — cell shows `*`
- **NEAR MISS** (adjacent cell): "SONAR RETURN AT D5: Contact CLOSE, bearing NORTH" — cell shows `!`
- **FAR MISS** (2 cells away): "SONAR RETURN AT D5: Faint contact, bearing SOUTHWEST" — cell shows `!`
- **MISS** (3+ cells away): "DEPTH CHARGE AT D5: No contact." — cell shows `X`

### Sonar Bearing

The bearing points toward the nearest submarine cell. "NORTH" means a sub is somewhere above. "SOUTHWEST" means down-and-left. This gives the player information to triangulate from.

With two or three sonar returns, a skilled player can pinpoint a submarine's location. This is the game's core skill: deduction from incomplete information.

### Sinking

When all cells of a submarine are hit, it sinks: "SUBMARINE SUNK! Patrol sub destroyed." All its cells change to `#`. The player knows the sub's full shape, which helps identify where other subs aren't.

### Winning and Losing

- **Win**: Sink all submarines before running out of charges.
- **Lose**: Run out of charges with submarines remaining.
- **Rating**: Based on charges remaining when all subs are sunk (fewer charges used = better).

---

## Visual Design

### Screen Layout

The C64's 40-column display is ideal for a grid game:

```
╔══════════════════════════════════════╗
║         DEPTH CHARGE                 ║
║    CHARGES: 28   SUBS: 3/5          ║
║                                      ║
║      A  B  C  D  E  F  G  H  I  J   ║
║  1   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~   ║
║  2   ~  ~  !  ~  ~  ~  ~  ~  ~  ~   ║
║  3   ~  ~  *  ~  ~  ~  ~  ~  ~  ~   ║
║  4   ~  ~  *  ~  ~  ~  ~  ~  ~  ~   ║
║  5   ~  X  ~  ~  ~  ~  ~  ~  ~  ~   ║
║  6   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~   ║
║  7   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~   ║
║  8   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~   ║
║  9   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~   ║
║ 10   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~   ║
║                                      ║
║  > ENTER TARGET: _                   ║
║                                      ║
║  SONAR: Contact CLOSE, bearing N     ║
╚══════════════════════════════════════╝
```

### Colours

Using PRINT with CHR$ colour codes (C64 BASIC colour control characters):

| Element | Colour | How |
|---------|--------|-----|
| Water (~) | Blue | CHR$(31) before printing |
| Hit (*) | Red | CHR$(28) |
| Miss (X) | Grey | CHR$(155) |
| Sonar (!) | Yellow | CHR$(158) |
| Sunk (#) | Green | CHR$(30) |
| Prompt text | White | CHR$(5) |
| Title | Cyan | CHR$(159) |

### No POKE Required

The entire display is PRINT-based. No screen memory POKE, no colour RAM POKE. This is deliberate — Game 1 teaches BASIC fundamentals, not hardware. The C64's PRINT statement handles colour via embedded control characters, which is sufficient for a strategy game.

---

## Difficulty

### Standard Game
- Grid: 10×10
- Submarines: 5 (two 2-cell, two 3-cell, one 4-cell)
- Charges: 40
- Sonar: bearing and distance

### Easy Mode
- Grid: 8×8
- Submarines: 3 (two 2-cell, one 3-cell)
- Charges: 30
- Sonar: bearing, distance, AND "warmer/colder" on consecutive shots

### Hard Mode
- Grid: 10×10
- Submarines: 6
- Charges: 35
- Sonar: bearing only, no distance

---

## Phase Breakdown

### Phase 1: The Grid (Units 1-16)

Display the grid, accept input, track state. No submarines yet — just the infrastructure.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | Welcome to BASIC | Title screen: "DEPTH CHARGE" in PRINT statements. CHR$(147) to clear screen. CHR$(14) for lowercase mode. The C64 screen editor and how to type a program. | PRINT, CHR$, CLS, RUN, line numbers |
| 2 | Variables | Store the player's name. PRINT "HELLO, "; N$. Numeric variables for score. | Variables, string vs numeric, INPUT |
| 3 | The Grid: Part 1 | Print a row of tildes. Use a FOR/NEXT loop to print 10 of them. Add spacing. | FOR/NEXT, PRINT formatting, TAB |
| 4 | The Grid: Part 2 | Print all 10 rows with row numbers. Add column headers (A-J). The grid fills the screen. | Nested loops, CHR$ for letters (CHR$(65)=A) |
| 5 | Arrays | DIM G(10,10) to store grid state. 0=unexplored, 1=miss, 2=hit, 3=sonar, 4=sunk. | DIM, two-dimensional arrays |
| 6 | Drawing from Arrays | Redraw the grid from the array. Each cell value maps to a character: 0→"~", 1→"X", 2→"*", etc. | Array-to-display mapping, IF/THEN chains |
| 7 | Colour | Add colour control characters before each cell. Blue for water, red for hits. The grid looks alive. | CHR$ colour codes, embedded colour in PRINT |
| 8 | Input: Coordinates | INPUT "TARGET: "; T$. Parse "D5" into column (4) and row (5). Handle bad input ("INVALID TARGET"). | String parsing, LEFT$, MID$, VAL, ASC |
| 9 | Input Validation | Reject off-grid coordinates, already-targeted cells, non-letter/number combos. Clear error messages. | Input validation, multiple conditions |
| 10 | Marking the Grid | Player enters a coordinate → grid array updates → grid redraws with the new mark. First interactive loop. | State update, redraw cycle |
| 11 | The Game Loop | Structure: clear screen → draw grid → show status → get input → process → repeat. GOSUB for each section. | Game loop architecture, GOSUB/RETURN |
| 12 | Status Display | Show charges remaining and submarines remaining above the grid. Update each turn. | HUD, formatted numeric display |
| 13 | Message Area | Sonar and hit messages appear below the grid. Previous message clears when a new one appears. | Screen regions, message display |
| 14 | Multiple Rounds | After game over (charges exhausted), offer "PLAY AGAIN?". Reset arrays, re-randomise, restart. | Game reset, re-initialisation |
| 15 | Random Numbers | RND(1) for random placement (used next phase). Explore RND: generate 10 random numbers, see the distribution. Seed discussion. | RND, INT, random number basics |
| 16 | Grid Polish | The grid looks clean: aligned columns, clear colours, readable status. A satisfying display even without gameplay. | Visual polish, alignment, presentation |

**Milestone:** A clean, colourful grid that accepts coordinate input and marks cells. No submarines yet, but the infrastructure is solid. The learner can type coordinates and see the grid update.

### Phase 2: Submarines and Sonar (Units 17-32)

Place submarines, detect hits, calculate sonar bearings. The game becomes playable.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | Placing One Sub | Place a 2-cell submarine at a random position and orientation (horizontal or vertical). Store in a submarine array. | Random placement, orientation, array storage |
| 18 | Collision Checking | Before placing a sub, verify it doesn't overlap another sub or extend off the grid. Retry if invalid. | Placement validation, retry loops |
| 19 | Multiple Subs | Place all 5 submarines. Different sizes. No overlaps. Store start position, orientation, size, and hit count per sub. | Multiple array management, placement algorithm |
| 20 | Hit Detection | Player fires at a coordinate. Check if any submarine occupies that cell. If yes: HIT. Update sub's hit count. | Coordinate lookup, hit tracking |
| 21 | Hit Feedback | "DIRECT HIT AT D5! Hull breach detected!" in red text. Cell shows `*`. Satisfying PRINT sequence. | Dramatic feedback, colour text |
| 22 | Miss Feedback | "DEPTH CHARGE AT D5: No contact." Cell shows `X`. Charges decrement. | Miss handling, charge counting |
| 23 | Sinking | When all cells of a sub are hit, it sinks. "SUBMARINE SUNK! Attack sub destroyed." All cells show `#`. Sub counter decrements. | Sink detection, multi-cell reveal |
| 24 | Distance Calculation | Calculate distance from the fired coordinate to the nearest submarine cell. Used for sonar. | Distance formula, minimum search |
| 25 | Sonar: Close | If the nearest sub cell is 1 cell away: "SONAR: Contact CLOSE." Cell shows `!` in yellow. | Distance threshold, near-miss detection |
| 26 | Sonar: Faint | If the nearest sub cell is 2 cells away: "SONAR: Faint contact." Different feedback from close. | Multiple distance bands |
| 27 | Sonar: Bearing | Calculate the direction from the fired cell to the nearest sub cell. "Bearing NORTH", "Bearing SOUTHWEST", etc. | Direction calculation, 8-compass mapping |
| 28 | Bearing Display | Combine distance and bearing: "SONAR: Contact CLOSE, bearing N". The player now has triangulation data. | Combined feedback, information display |
| 29 | Winning | All subs sunk → "VICTORY! All submarines destroyed." Show charges remaining, calculate rating. | Win condition, rating calculation |
| 30 | Losing | Charges exhausted → "MISSION FAILED. X submarines remain." Reveal all sub positions. Educational — show what was missed. | Lose condition, board reveal |
| 31 | Rating System | "COMMANDER" (20+ charges left), "CAPTAIN" (10-19), "LIEUTENANT" (1-9), "CADET" (barely won). | Threshold ratings, rank system |
| 32 | Five Complete Games | Play 5 full games. Is the sonar useful? Is 40 charges enough? Too many? Adjust balance. | Playtesting, balance |

**Milestone:** A complete, playable game. Place submarines, fire depth charges, get sonar bearings, triangulate positions, sink subs, win or lose. The core game works.

### Phase 3: Depth (Units 33-48)

Two-player mode, difficulty settings, and polish that turns a prototype into a game.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | Two-Player Mode | Player 1 places subs manually (using INPUT for coordinates). Player 2 tries to find them. Alternating turns. | Two-player design, manual placement |
| 34 | Hidden Placement | During Player 1's placement phase, the screen shows the grid with subs. Then CHR$(147) clears before Player 2 looks. | Screen clearing for hidden information |
| 35 | Player 2 Places | Both players place subs, then take turns firing. Track two separate grids (attack grid and defence grid). | Dual state, per-player arrays |
| 36 | Two-Player Polish | Clear screen between turns with "PRESS ANY KEY" prompt. No peeking. Fair turn management. | Turn management, anti-cheat display |
| 37 | Difficulty Select | Easy/Normal/Hard menu at start. Adjusts grid size, sub count, charges, sonar detail. | Menu system, difficulty parameters |
| 38 | Easy Mode | 8×8 grid, 3 subs, 30 charges, enhanced sonar ("warmer/colder" on consecutive shots). Gentler introduction. | Parameter-driven difficulty |
| 39 | Hard Mode | 10×10 grid, 6 subs, 35 charges, bearing only (no distance). Real challenge. | Reduced information, harder deduction |
| 40 | Statistics | Track games played, wins, losses, average charges used, best rating. Display on a stats screen. | Session statistics, running averages |
| 41 | High Score | Best game (fewest charges to sink all subs). Shown on title screen. | Best-score tracking, display |
| 42 | Coordinate History | Show the last 5 shots in a sidebar or below the grid. Helps the player remember their sonar returns without writing them down. | History array, scrolling display |
| 43 | Sub Type Feedback | When a sub sinks, reveal its type and size. "Patrol sub (2 cells) sunk!" The player knows what sizes remain. | Type revelation, remaining fleet info |
| 44 | First Charge Tutorial | On the very first shot of a new player's first game, give extra guidance: "Try a coordinate like D5." Disabled after first game. | First-run tutorial, one-time flags |
| 45 | Sound Effects | Explosion on hit: simple PRINT CHR$(7) bell character (the C64 beep). Not SID — that's Game 4. Just the system bell for feedback. | CHR$(7) bell, minimal audio feedback |
| 46 | Victory Animation | On winning: the grid briefly flashes (reprint with different colours) and a "MISSION COMPLETE" banner scrolls. Simple but celebratory. | Colour cycling via reprint, celebration |
| 47 | Defeat Reveal | On losing: submarines are revealed one by one with a brief pause between each. The player sees where they went wrong. | Sequential reveal, educational feedback |
| 48 | Balance Final | Play all three difficulty levels. Two-player mode. Is it fun? Is the sonar too helpful or not helpful enough? | Final balance pass |

**Milestone:** Single-player and two-player modes. Three difficulty levels. Statistics, high score, coordinate history, contextual feedback. A complete strategy game.

### Phase 4: Polish (Units 49-64)

Title screen, presentation, and the bridge to Game 2's POKE-based approach.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Title Screen | "DEPTH CHARGE" title with submarine ASCII art. Waves (~) animate across the top of the screen. | PRINT-based art, simple animation |
| 50 | Instructions | How to play: grid explanation, coordinate entry, sonar interpretation, strategy tips. One screen. | User onboarding |
| 51 | Menu System | Title → Instructions → Difficulty → 1P/2P → Play → Game Over → Title. Clean flow with GOSUB for each screen. | Menu state machine |
| 52 | Grid Animation | When a depth charge is dropped: brief "sinking" animation — a `V` descends the grid before the result appears. 2-3 PRINT/PAUSE steps. | Sequential animation via PRINT |
| 53 | Sonar Pulse | On sonar return: the `!` character blinks 3 times (print, pause, clear, pause, print). Draws the eye to the new information. | Blink animation, attention direction |
| 54 | Sub Sinking Animation | When a sub sinks: its cells change from `*` to `#` one by one, left to right, with a brief pause. Feels like it's going down. | Sequential cell update, dramatic pacing |
| 55 | Colour Themes | Menu option: green-on-black (radar), blue-on-blue (ocean), amber-on-black (terminal). Cosmetic variety. | Colour theming, POKE 53280/53281 |
| 56 | The POKE Preview | Change border and background colour using POKE 53280 and POKE 53281. The player's first POKE — just two lines, but it changes the entire screen. Preview of Game 2. | First POKE, hardware register introduction |
| 57 | Custom Prompt | Replace the default cursor with a blinking `>` at the input line. More game-like, less BASIC-prompt-like. | Custom input presentation |
| 58 | Replay Value | After finishing, show: "Games played: 5, Best rating: COMMANDER, Average charges: 28." Encourages replay. | Aggregate statistics, session summary |
| 59 | Edge Cases | What if the player enters the same coordinate twice? (Already targeted.) What about lowercase input? (Convert with ASC/CHR$.) | Robust input handling, case conversion |
| 60 | Bug Sweep | Systematic testing: every sub placement valid? Every sonar bearing correct? Two-player screen clearing? | QA methodology |
| 61 | Code Review | Read through the entire listing. Are variable names consistent? Are GOSUBs labelled with REM? Is the structure clear? | Code quality, readability |
| 62 | Performance | Is the grid redraw fast enough? On a real C64, PRINT fills the screen noticeably. Optimise: only redraw changed cells, not the full grid. | Selective redraw, performance awareness |
| 63 | Line Count | Under 500 lines? Two-player mode and three difficulty levels are the biggest code consumers. If over, trim the least essential feature. | Scope management |
| 64 | The Finished Game | Clean listing. Title, instructions, difficulty select, 1P/2P modes, sonar triangulation, statistics, colour themes. A real strategy game in pure BASIC. | Completion |

**Milestone:** A polished naval strategy game. Sonar triangulation, two-player mode, three difficulties, animations, statistics. Pure PRINT/INPUT BASIC — no hardware tricks. The C64 BASIC track's starting point.

---

## Technical Notes

### Data Structures

```basic
DIM G(10,10)    : REM GRID STATE (0=UNKNOWN,1=MISS,2=HIT,3=SONAR,4=SUNK)
DIM S(5,4)      : REM SUBS: ROW, COL, SIZE, ORIENTATION (0=H,1=V)
DIM H(5)        : REM HIT COUNT PER SUB
DIM SZ(5)       : REM SIZE PER SUB
```

### Submarine Placement

```basic
1000 REM PLACE ONE SUB (SIZE=SZ, INDEX=SI)
1010 OK=0
1020 R=INT(RND(1)*10)+1: C=INT(RND(1)*10)+1
1030 O=INT(RND(1)*2): REM 0=HORIZONTAL, 1=VERTICAL
1040 REM CHECK FITS ON GRID
1050 IF O=0 AND C+SZ-1>10 THEN 1020
1060 IF O=1 AND R+SZ-1>10 THEN 1020
1070 REM CHECK NO OVERLAP
1080 FOR I=0 TO SZ-1
1090   IF O=0 THEN CR=R: CC=C+I
1100   IF O=1 THEN CR=R+I: CC=C
1110   IF G(CR,CC)<>0 THEN 1020
1120 NEXT I
1130 REM PLACE IT (IN HIDDEN ARRAY, NOT ON DISPLAY GRID)
```

### Sonar Bearing Calculation

```basic
2000 REM BEARING FROM (FR,FC) TO NEAREST SUB CELL
2010 REM FIND NEAREST SUB CELL
2020 BD=99: BR=0: BC=0
2030 FOR I=1 TO NS
2040   FOR J=0 TO SZ(I)-1
2050     IF S(I,4)=0 THEN SR=S(I,1): SC=S(I,2)+J
2060     IF S(I,4)=1 THEN SR=S(I,1)+J: SC=S(I,2)
2070     D=ABS(SR-FR)+ABS(SC-FC): REM MANHATTAN DISTANCE
2080     IF D<BD THEN BD=D: BR=SR: BC=SC
2090   NEXT J
2100 NEXT I
2110 REM CALCULATE BEARING
2120 DR=BR-FR: DC=BC-FC
2130 B$=""
2140 IF DR<0 THEN B$="N"
2150 IF DR>0 THEN B$="S"
2160 IF DC<0 THEN B$=B$+"W"
2170 IF DC>0 THEN B$=B$+"E"
```

### Memory Budget

- Program text: ~10-12 KB (500 lines × ~25 characters average)
- Arrays: ~500 bytes (grid + subs + stats)
- Total: ~12 KB — very comfortable in 48K

### Line Numbering

- 1-99: Initialisation, DIM, variables
- 100-199: Title screen, instructions, menu
- 200-299: Grid drawing
- 300-399: Main game loop, input parsing
- 400-499: Hit/miss/sonar calculation
- 500-599: Sub placement
- 600-699: Status display, messages
- 700-799: Game over, rating, statistics
- 800-899: Two-player mode
- 900-999: Animations, polish
- 1000+: DATA (if any — most state is generated, not DATA-driven)

---

## Design Notes

### Why a Strategy Game First

The C64 BASIC track's first game needs to be playable and engaging using only PRINT and INPUT. No POKE, no PEEK, no hardware knowledge. A strategy game fits perfectly: the grid is displayed with PRINT, coordinates are entered with INPUT, and the logic (placement, sonar, deduction) is pure programming.

Depth Charge also teaches the most important programming concepts — arrays, conditionals, loops, string parsing, random numbers, subroutines — through a game that has genuine replay value. Every game is different because submarine positions are random. The sonar system adds a deduction layer that rewards clever play.

### The Sonar Mechanic

Battleships' binary hit/miss feedback makes the game largely random until you get a hit, then mechanical (search adjacent cells). The sonar bearing system changes this: every shot gives information, even misses. A skilled player uses two sonar returns to triangulate a sub's position. This makes the game feel like skill, not luck — and it's more fun.

### The Bridge to Game 2

Unit 56 introduces POKE for the first time: `POKE 53280,0` (border black) and `POKE 53281,0` (background black). Two lines. But it changes the entire screen — and it's the player's first direct hardware interaction. The game remains pure PRINT/INPUT, but the seed is planted. Game 2 builds the entire display with POKE.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Replaces old Game 1 (Psychic Computer) with a substantially more ambitious grid strategy game. New to the restructured C64 BASIC track.
