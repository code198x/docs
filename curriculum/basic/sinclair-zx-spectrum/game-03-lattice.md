# Game 03: Lattice

**Track:** Spectrum BASIC
**Genre:** Node-connection puzzle
**Units:** 64 (4 phases × 16 units)
**Language:** Sinclair BASIC
**Max lines:** ~500
**Save/load:** No — puzzles are self-contained

---

## Premise

A grid of dots. Some pairs must be connected. Lines can't cross.

That's the entire game. It sounds simple — and the first few puzzles are — but the constraint "lines can't cross" turns a drawing exercise into a spatial reasoning challenge. The player must plan routes, sometimes backtrack mentally, and find the one arrangement where every required connection exists without any intersection.

The game looks like a puzzle page from a newspaper, rendered in clean Spectrum geometry: PLOT for the dots, DRAW for the lines, colour for feedback. It's calm, contemplative, and satisfying when the last line clicks into place.

---

## Core Mechanics

### The Grid

Each puzzle has:
- **Nodes**: dots at fixed positions on screen, arranged in a grid or irregular pattern
- **Required connections**: pairs of nodes that must be linked
- **The rule**: no two lines may cross

Nodes are drawn with PLOT (or small CIRCLE). Lines are drawn with DRAW between node centres. The player selects a node, then selects another node, and a line is drawn between them. If the line would cross an existing line, it's rejected.

### Node Layout

Early puzzles use a regular grid (3×3, 4×4). Later puzzles use irregular arrangements — nodes offset, clustered, or arranged in shapes (triangle, hexagon, circle). Irregular layouts make crossing-avoidance harder because straight lines between distant nodes cut through more of the space.

### Connections

Each puzzle specifies which pairs must be connected. The player doesn't choose which nodes to connect — that's given. They choose the *routing*: which order to draw the lines, and (in later puzzles with flexible routing) which path each line takes.

In the simplest version, every line is a straight segment between two nodes. In later puzzles, lines could route through intermediate waypoints — but that's a stretch goal. Straight lines only is the base game.

### Crossing Detection

Two line segments cross if they intersect geometrically. For straight lines between nodes on a grid, this is a standard line-segment intersection test.

In BASIC, the cleanest approach is **colour-based**: draw each line in a specific INK colour. Before drawing a new line, check POINT along its path — if any pixel is already coloured (a previous line), the crossing is detected.

This is simpler than mathematical intersection and exploits the Spectrum's strengths: PLOT and DRAW write pixels, POINT reads them.

### Input

The player uses keyboard (or cursor) to move a cursor between nodes:
- **Arrow keys / QAOP**: move cursor to the nearest node in that direction
- **SPACE / ENTER**: select current node
- **D**: delete the last drawn line (undo)

Selection is two-step: select node A, then select node B. If A-B is a required connection and the line doesn't cross anything, it's drawn. Otherwise, feedback explains why not ("Those nodes don't need connecting" or "That line would cross an existing one").

### Completion

A puzzle is complete when all required connections are drawn with no crossings. Celebratory BEEP sequence, score awarded, next puzzle loads.

---

## Puzzle Design

### Scale

40-50 puzzles across 5 difficulty bands (8-10 puzzles each).

### Difficulty Progression

| Band | Nodes | Connections | Layout | Challenge |
|------|-------|-------------|--------|-----------|
| 1: Warm-up (1-8) | 4-6 | 3-5 | Regular grid | Almost impossible to fail. Teaches mechanics. |
| 2: Thinking (9-18) | 6-9 | 5-8 | Regular grid | Some orderings cause crossings. Player must plan. |
| 3: Planning (19-28) | 9-12 | 7-10 | Offset grid | Multiple potential crossings. Undo becomes essential. |
| 4: Spatial (29-38) | 10-16 | 8-14 | Irregular | Non-obvious solutions. Layout tricks the eye. |
| 5: Expert (39-48+) | 12-20 | 10-18 | Complex irregular | Multiple valid solutions but narrow paths. Satisfying to complete. |

### Puzzle Data

Each puzzle is stored as DATA:

```basic
5000 DATA 6
5010 DATA 40,120, 120,120, 200,120
5020 DATA 40,60,  120,60,  200,60
5030 DATA 5
5040 DATA 1,5, 2,6, 1,3, 4,2, 3,6
```

- Line 5000: number of nodes
- Lines 5010-5020: node coordinates (x, y pairs)
- Line 5030: number of required connections
- Line 5040: connection pairs (node indices)

### Puzzle Generation

Puzzles are hand-designed, not generated. Hand design ensures:
- Every puzzle has at least one solution
- Difficulty is intentional, not accidental
- Visual layout is pleasing (symmetry, balance)
- Red herrings are deliberate (tempting lines that block later connections)

The designer (the learner, eventually) creates puzzles by placing nodes, defining connections, verifying solvability, and testing difficulty. This is taught in Phase 4.

---

## Visual Design

### Screen Layout

```
╔══════════════════════════════════╗
║          L A T T I C E           ║  ← title bar
╠══════════════════════════════════╣
║                                  ║
║      ●─────────────●            ║  ← drawn line (green)
║      │              │            ║
║      │    ●         │            ║  ← unconnected node
║      │              │            ║
║      ●──────●───────●            ║
║             │                    ║
║             ●                    ║  ← cursor here (flashing)
║                                  ║
╠══════════════════════════════════╣
║ PUZZLE 12/48   LINES: 3/5   ♦♦♦ ║  ← HUD
╚══════════════════════════════════╝
```

### Colours

| Element | INK | Appearance |
|---------|-----|------------|
| Background | Black (0) | Clean dark canvas |
| Nodes (unconnected) | White (7) | Bright dots, clearly visible |
| Nodes (connected) | Green (4) | Show progress |
| Cursor | Yellow (6), FLASH | Highlights current node |
| Drawn lines | Green (4) | Successful connections |
| Rejected line (flash) | Red (2) | Brief flash then disappears |
| Required connections (hint) | Cyan (5), faint | Optional: show which pairs need connecting |
| HUD text | White (7), BRIGHT | Status bar |

### Node Rendering

Nodes are drawn as small filled shapes:
- `CIRCLE x, y, 3` for a clean dot
- Or PLOT a 3×3 cluster for a blockier, more Spectrum feel

### Line Rendering

`PLOT x1, y1: DRAW x2-x1, y2-y1` draws a straight line between nodes. Green INK for valid lines.

### Cursor

The cursor highlights the current node with a flashing ring: `CIRCLE x, y, 6` in yellow with FLASH 1. Or alternate between yellow and black on a timer for a pulse effect.

### Rejection Animation

When a line would cross: draw it briefly in red, BEEP a low buzz, then erase it. The player sees WHY it was rejected — the crossing point is visible for a moment.

---

## Feedback and Scoring

### Per-Puzzle Score

| Factor | Points |
|--------|--------|
| Completing the puzzle | 100 |
| No undo used | +50 bonus |
| Under par moves | +25 bonus |
| Difficulty band multiplier | ×1 (band 1) to ×3 (band 5) |

"Par moves" equals the number of required connections — solving it with no wrong attempts is par.

### Stars

Each puzzle awards 1-3 stars:
- ★: completed
- ★★: completed with no undo
- ★★★: completed under par with no undo

Stars are displayed on the puzzle select screen. Completionists will replay for three stars.

### Sound

| Event | Sound |
|-------|-------|
| Select node | Short click (high BEEP) |
| Draw valid line | Satisfying rising tone |
| Line rejected (crossing) | Low buzz |
| Undo | Descending note |
| Puzzle complete | Ascending three-note fanfare |
| Band complete | Longer celebratory sequence |
| All puzzles complete | Full ascending scale |

---

## Phase Breakdown

### Phase 1: Dots and Lines (Units 1-16)

Draw nodes, draw lines between them, detect crossings. No puzzle structure yet — just the graphical foundation.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | A Dot on the Screen | Title screen. Then: PLOT a single dot. Explain Spectrum pixel coordinates (0,0 at bottom-left, 255,175 at top-right). | PLOT, coordinate system, CLS, INK |
| 2 | More Dots | PLOT multiple dots at specific positions. A row of evenly spaced dots. A grid of dots. | FOR/NEXT, calculated coordinates |
| 3 | Connecting Dots | DRAW a line between two dots. PLOT first point, DRAW delta-x, delta-y to second. | DRAW, coordinate maths (dx, dy) |
| 4 | Circles for Nodes | CIRCLE for cleaner node rendering. Size 3-4 pixels. Nodes look like proper game pieces. | CIRCLE, radius, visual design |
| 5 | Colour Coding | Green lines for connections, white nodes, black background. INK before PLOT/DRAW. | INK, colour planning |
| 6 | A Grid of Nodes | Draw a 3×3 grid of nodes at regular intervals. Store positions in arrays. | DIM, arrays, calculated positions |
| 7 | Node Data | Move node positions into DATA statements. Read into arrays at startup. | DATA, READ, array population |
| 8 | Drawing a Line Between Nodes | Given two node indices, look up their coordinates and DRAW between them. A GOSUB that takes node A and node B. | GOSUB with parameters via variables, array lookup |
| 9 | The Cursor | A highlighted node that the player can move between. QAOP moves to the nearest node in that direction. | INKEY$, nearest-node search, cursor state |
| 10 | Node Selection | SPACE selects the current node. First press = start node (highlighted). Second press = end node (draw line). | Two-phase input, selection state |
| 11 | Connection Pairs | DATA defines which pairs must be connected. Display required connections as faint cyan lines or indicators. | Connection data, pair storage |
| 12 | Valid Connection Check | When the player selects two nodes, check if that pair is in the required list. Reject if not: "Those nodes don't need connecting." | Array search, validation |
| 13 | Crossing Detection | Before drawing a line, POINT-check along its path. If any pixel is already green (existing line), the crossing is detected. | POINT function, pixel reading, path checking |
| 14 | Rejection Feedback | Rejected line: draw briefly in red, BEEP, erase. The player sees the crossing point. | Temporary drawing, erase, visual feedback |
| 15 | Undo | D key removes the last drawn line. Erase it (redraw in black), restore node colours, decrement connection count. | Undo stack (array of drawn connections), erase |
| 16 | First Puzzle | All mechanics working on a single 6-node puzzle. Select nodes, draw lines, detect crossings, undo. Playable. | Integration, first complete puzzle |

**Milestone:** The core mechanics work. Nodes, lines, crossing detection, undo. One puzzle is playable and solvable.

### Phase 2: The Puzzle Game (Units 17-32)

Multiple puzzles, completion detection, scoring, and the first 20 puzzles.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | Puzzle Complete | Detect when all required connections are drawn. "PUZZLE COMPLETE!" message with fanfare. | Completion check, all-pairs-connected |
| 18 | Score | Points for completion. Display score. No-undo bonus. | Score tracking, conditional bonus |
| 19 | Next Puzzle | After completion, load the next puzzle from DATA. RESTORE to the correct DATA line. | RESTORE, DATA sequencing, puzzle progression |
| 20 | Puzzle Counter | "PUZZLE 3/48" in the HUD. Track current puzzle and total. | Progress tracking, HUD display |
| 21 | Lines Counter | "LINES: 2/5" — how many connections drawn vs. how many required. Immediate visual progress. | Counter display, ratio |
| 22 | Star Rating | Award 1-3 stars per puzzle based on performance. Display stars on completion. | Rating calculation, conditional display |
| 23 | Band 1 Puzzles | Design and enter 8 warm-up puzzles (4-6 nodes, 3-5 connections). Regular grid layouts. | Puzzle design process, DATA entry |
| 24 | Band 1 Testing | Play all 8 band 1 puzzles. Are they solvable? Are they too easy? Too hard? Adjust. | Playtesting, difficulty assessment |
| 25 | Band 2 Puzzles | Design 10 thinking puzzles (6-9 nodes, 5-8 connections). Some orderings cause crossings — player must plan. | Harder puzzle design, deliberate traps |
| 26 | Band 2 Testing | Play all band 2 puzzles. The "aha" moment should happen here — the first time a player has to undo and rethink. | Difficulty curve, cognitive challenge |
| 27 | Difficulty Multiplier | Band 1 = ×1 score, Band 2 = ×1.5, etc. Higher bands reward more points. | Score multiplier, difficulty bands |
| 28 | Puzzle Select | Instead of linear progression, show a puzzle select screen. Completed puzzles show stars. Locked bands unlock as previous band is cleared. | Menu screen, unlock progression |
| 29 | Band Unlocking | Complete 6/8 puzzles in band 1 to unlock band 2. Don't require perfection — just completion. | Progress gating, threshold check |
| 30 | Hint System | Press H to briefly flash all required connections as faint lines. Costs the no-undo bonus (treated as assistance). | Help system, penalty for assistance |
| 31 | Connection Preview | After selecting node A, faint lines show which nodes A can legally connect to (from the required pairs list). Helps the player see options. | Conditional preview drawing, usability |
| 32 | Twenty Puzzles | Bands 1 and 2 complete (18 puzzles). Puzzle select shows progress. Stars track performance. | Milestone: substantial playable content |

**Milestone:** 18 puzzles across two difficulty bands. Puzzle select with star ratings, hints, connection preview, band unlocking. A complete puzzle game — just not finished yet.

### Phase 3: Depth and Challenge (Units 33-48)

The remaining puzzle bands, irregular layouts, and visual refinements.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | Irregular Layouts | Nodes no longer on a regular grid. Offset positions, clusters, asymmetric arrangements. | Free-form coordinate placement |
| 34 | Band 3 Puzzles | 10 planning puzzles (9-12 nodes, irregular grid). Multiple potential crossings. Undo essential. | Complex puzzle design |
| 35 | Band 3 Testing | Are the irregular layouts visually clear? Can the player distinguish nearby nodes? Adjust spacing if needed. | Visual clarity testing |
| 36 | Longer Lines | With irregular layouts, some lines cross large portions of the screen. Crossing detection must check more pixels. Performance? | Performance with longer POINT checks |
| 37 | Optimised Crossing Check | Instead of checking every pixel, check at regular intervals along the line (every 4 pixels). Faster, still accurate for game purposes. | Optimisation, sampling, trade-offs |
| 38 | Band 4 Puzzles | 10 spatial puzzles (10-16 nodes, irregular). Non-obvious solutions. The layout tricks the eye — lines that look safe aren't. | Advanced puzzle design, visual misdirection |
| 39 | Band 4 Testing | These should make the player think for minutes, not seconds. But they must be fair — solvable without guessing. | Fairness testing, cognitive difficulty |
| 40 | Band 5 Puzzles | 10 expert puzzles (12-20 nodes, complex irregular). The hardest puzzles in the game. Multiple valid solutions but narrow paths. | Expert-level design |
| 41 | Band 5 Testing | Can the designer solve them all? Time yourself. If any take more than 5 minutes, consider whether that's fun or frustrating. | Difficulty ceiling, player experience |
| 42 | Par Moves | Each puzzle has a par (minimum moves = number of connections). Under-par is impossible (you must draw every connection). But no-undo is the real challenge. | Par definition, bonus structure |
| 43 | Puzzle Variety | Review all 48 puzzles. Are there repeated patterns? Does each puzzle feel distinct? Replace duplicates. | Content review, variety |
| 44 | Visual Themes | Each band has a colour theme. Band 1: green lines on black. Band 3: cyan lines. Band 5: magenta. Variety without new mechanics. | Palette as progression marker |
| 45 | Transition Effects | Between puzzles: lines fade out (INK cycles to black), new puzzle fades in. Between bands: a "BAND COMPLETE" screen. | INK animation, transition pacing |
| 46 | Statistics | Track total stars earned, puzzles completed, average moves per puzzle. Display on a stats screen. | Aggregate data, statistics calculation |
| 47 | All Puzzles Complete | Finishing all 48 puzzles: special congratulations screen. Total stars, total score, completion time (if tracked). | End-game celebration |
| 48 | Balance Pass | Play every puzzle in order from band 1 to band 5. Is the difficulty curve smooth? Any spikes or lulls? | Full playthrough, curve adjustment |

**Milestone:** All 48 puzzles across 5 difficulty bands. Irregular layouts, colour themes, transitions, statistics. The puzzle game is content-complete.

### Phase 4: Polish (Units 49-64)

Title screen, presentation, the puzzle editor, and final testing.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Title Screen | "LATTICE" title with geometric design — connected nodes forming the letters, or a decorative lattice pattern drawn with PLOT/DRAW. | Artistic PLOT/DRAW, title design |
| 50 | Instructions | "HOW TO PLAY" screen with a tiny example puzzle. Show the rules visually: two lines crossing = bad, all connections made = good. | Visual instructions, example rendering |
| 51 | Menu Flow | Title → Instructions (optional) → Puzzle Select → Play → Puzzle Select. Clean navigation with INKEY$ menus. | Menu state machine, screen flow |
| 52 | Node Animation | Nodes pulse gently when unconnected (alternate between two sizes). Connected nodes glow solid. The board feels alive. | Timer-based animation, CIRCLE redraw |
| 53 | Line Drawing Animation | When a valid line is drawn, it doesn't appear instantly — it extends from node A to node B over a few frames. Satisfying. | Incremental DRAW, animation timing |
| 54 | Completion Celebration | When the last line is drawn: all lines briefly flash, nodes burst (expanding circles), fanfare plays. Moment of triumph. | Multi-element animation, sequenced effects |
| 55 | Colour-Blind Consideration | Lines and nodes must be distinguishable without relying solely on colour. Use BRIGHT for connected vs unconnected. Shapes differ for different states. | Accessibility, non-colour-dependent design |
| 56 | Sound Polish | Each valid line plays a note — ascending pitch as more connections are made. The puzzle builds a chord. Completion is the resolution. | Musical sound design, pitch progression |
| 57 | The Puzzle Editor | A separate mode: place nodes with cursor, define connections, test solvability, save as DATA statements. The learner becomes a designer. | Editor mode, creating content, DATA output |
| 58 | Editor: Place Nodes | Move cursor freely with QAOP, press SPACE to place a node. DRAW a grid for alignment. | Free cursor, placement mode |
| 59 | Editor: Define Connections | Select two placed nodes to create a required connection. Visual line appears. Build the puzzle interactively. | Two-phase selection in editor context |
| 60 | Editor: Test and Export | "TEST" mode: play the puzzle you just designed. "EXPORT": print DATA statements to screen for copying into the program. | Mode switching, DATA generation |
| 61 | Edge Cases | What if the player selects the same node twice? What if they try to connect already-connected nodes? Graceful handling for everything. | Defensive programming, input validation |
| 62 | Performance Sweep | With 20 nodes and 18 connections (band 5), is crossing detection still fast enough? Profile and optimise if needed. | Performance testing, optimisation |
| 63 | Line Count | Are we under 500 lines? The puzzle editor might push us over — if so, it's a documented "extended version." Base game stays under 500. | Scope management, code budget |
| 64 | The Finished Game | 48 puzzles, 5 bands, star ratings, puzzle select, hints, animated drawing, musical feedback, puzzle editor. Clean listing, under 500 lines. | Completion |

**Milestone:** A polished puzzle game with 48 hand-designed puzzles, animated line drawing, musical note progression, star ratings, and a puzzle editor for creating new challenges. Under 500 lines.

---

## Technical Notes

### Crossing Detection via POINT

The POINT function returns the INK colour at a pixel coordinate. To check if a new line would cross an existing one:

```basic
600 REM CHECK CROSSING FROM (x1,y1) TO (x2,y2)
610 LET cx = 0
620 LET steps = 20
630 LET dx = (x2 - x1) / steps
640 LET dy = (y2 - y1) / steps
650 LET tx = x1: LET ty = y1
660 FOR i = 1 TO steps - 1
670   LET tx = tx + dx: LET ty = ty + dy
680   IF POINT(INT tx, INT ty) = 4 THEN LET cx = 1
690 NEXT i
700 RETURN
```

Check 20 points along the line. If any pixel is green (INK 4, existing line), the crossing flag `cx` is set. 20 samples is enough for lines up to ~200 pixels; longer lines may need more.

The elegance: we don't need mathematical line-segment intersection. The screen IS the collision map. POINT reads what DRAW already wrote. Sinclair BASIC's graphics commands are both the renderer and the physics engine.

### Node Proximity for Cursor

When the player presses a direction, find the nearest node in that direction:

```basic
500 REM FIND NEAREST NODE IN DIRECTION (ddx, ddy) FROM CURRENT NODE cn
510 LET best = -1: LET bd = 9999
520 FOR i = 1 TO nn
530   IF i = cn THEN GO TO 570
540   LET ndx = nx(i) - nx(cn): LET ndy = ny(i) - ny(cn)
550   REM Check direction matches (signs agree)
560   IF SGN(ndx) = ddx OR SGN(ndy) = ddy THEN ...
570 NEXT i
```

This is approximate — "nearest in the right general direction." Good enough for a cursor that snaps between nodes.

### Undo Stack

An array of drawn connections, most recent first:

```
uc()  - undo stack: pairs of node indices
up    - undo pointer (number of drawn connections)
```

Undo: read the top pair, erase the line (redraw in black INK), decrement pointer. Redraw nodes at both endpoints (they may have been partially overwritten by the line).

### Puzzle DATA Format

```
DATA 6                           : REM nodes
DATA 40,120, 120,120, 200,120   : REM node coordinates (3 per line)
DATA 40,60,  120,60,  200,60
DATA 5                           : REM connections
DATA 1,5, 2,6, 1,3, 4,2, 3,6   : REM connection pairs
DATA 3                           : REM par (minimum moves)
```

48 puzzles × ~4 DATA lines = ~192 DATA lines. With the game logic at ~300 lines, total is ~490-500. Tight but achievable.

### Memory

- Game logic: ~8-10 KB
- Puzzle DATA (48 puzzles): ~4-5 KB
- Variables and arrays: ~1 KB
- Total: ~13-16 KB — comfortable in 48K

### Line Numbering

- 1-99: Initialisation, arrays, variables
- 100-199: Title screen, instructions, menu
- 200-299: Puzzle select screen
- 300-399: Puzzle loading (READ DATA, draw nodes)
- 400-499: Main game loop (input, selection, completion check)
- 500-599: Cursor movement and node selection
- 600-699: Line drawing, crossing detection, undo
- 700-799: HUD, score, stars, puzzle complete
- 800-899: Animations (line drawing, completion, transitions)
- 900-999: Puzzle editor (if within line budget)
- 1000-2999: Puzzle DATA (48 puzzles)

---

## Design Notes

### Why Connection Puzzles

Connection puzzles have a unique quality: the rules are trivially simple ("connect these, don't cross") but the solutions require genuine spatial reasoning. A 5-year-old understands the rules. A 50-year-old is challenged by puzzle 40. This wide accessibility matches the project's audience.

They're also perfectly suited to BASIC's graphics: PLOT dots, DRAW lines, POINT to check collisions. The game mechanic IS the language feature. Learning PLOT/DRAW isn't a prerequisite for the game — it IS the game.

### The Musical Progression

Each valid line plays a note. The notes ascend within a scale as more connections are drawn. A puzzle with 5 connections plays notes 1-5 of a major scale. Completing the puzzle plays the full chord (all notes together). This creates an unintentional melody unique to each puzzle — the player composes by solving.

### The Puzzle Editor

Including an editor in a 500-line BASIC game is ambitious. It may not fit. If it doesn't, it's documented as a "challenge extension" — the learner who wants to go further can build it from the specification. The base game (48 puzzles, no editor) is the priority.

The editor is valuable pedagogically: it teaches the learner to build tools, not just games. And it generates replayability — players can design puzzles for each other.

### Calm, Not Frantic

Lattice has no timer, no enemies, no lives. The player thinks for as long as they need. This is deliberate contrast with Night Patrol (tense, real-time) and Blockstorm (action, reflexes). The Spectrum BASIC track should offer variety in mood, not just mechanics.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. New Game 3 in the restructured BASIC track. Node-connection puzzle using PLOT/DRAW, crossing detection via POINT.
