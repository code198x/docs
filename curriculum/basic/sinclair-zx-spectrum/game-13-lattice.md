# Game 13: Lattice

**Track:** Spectrum BASIC
**Genre:** Node-connection puzzle
**Units:** 32 (2 phases × 16 units)
**Language:** Sinclair BASIC
**Max lines:** ~300

---

## Premise

A grid of dots. Some pairs must be connected. Lines can't cross.

That's the entire game. It sounds simple — and the first few puzzles are — but the constraint "lines can't cross" turns a drawing exercise into a spatial reasoning challenge. The player must plan routes, sometimes backtrack mentally, and find the one arrangement where every required connection exists without any intersection.

The game looks like a puzzle page from a newspaper, rendered in clean Spectrum geometry: PLOT for the dots, DRAW for the lines, colour for feedback. It's calm, contemplative, and satisfying when the last line clicks into place.

Lattice has no timer, no enemies, no lives. The player thinks for as long as they need. This is deliberate contrast with the action and tension of earlier games.

For the learner, Lattice is the introduction to the Spectrum's graphics commands. Every previous game used PRINT AT — placing characters on a 32×22 grid. Lattice moves to a 256×176 pixel canvas. PLOT places a dot. DRAW extends a line. CIRCLE makes a shape. POINT reads what's already there. These four commands turn the screen into both a renderer and a collision map. The learner discovers that graphics aren't just decorative — they're structural.

---

## Core Mechanics

### The Grid

Each puzzle has:
- **Nodes**: dots at fixed positions on screen, arranged in a grid or irregular pattern
- **Required connections**: pairs of nodes that must be linked
- **The rule**: no two lines may cross

Nodes are drawn with CIRCLE (radius 3). Lines are drawn with DRAW between node centres. The player selects a node, then selects another, and a line is drawn between them. If the line would cross an existing line, it's rejected.

### Node Layout

Early puzzles use a regular grid (3×3, 4×4). Later puzzles use irregular arrangements — nodes offset, clustered, or arranged in shapes (triangle, hexagon, circle). Irregular layouts make crossing-avoidance harder because straight lines between distant nodes cut through more of the space.

For circular and irregular arrangements, node positions are calculated using SIN and COS to distribute points evenly around a circle or arc.

### Connections

Each puzzle specifies which pairs must be connected. The player doesn't choose which nodes to connect — that's given. They choose the *order*: which lines to draw first, since a line drawn early may block a line needed later. Every line is a straight segment between two nodes.

### Crossing Detection

Before drawing a new line, the game checks POINT along its path. If any pixel is already green (INK 4, an existing line), the crossing is detected. This is simpler than mathematical line-segment intersection and exploits the Spectrum's strengths: PLOT and DRAW write pixels, POINT reads them. The screen is both the renderer and the physics engine.

### Input

The player uses QAOP to move a cursor between nodes and SPACE to select:

- **Q/A/O/P**: move cursor to the nearest node in that direction
- **SPACE**: select current node
- **D**: undo the last drawn line

Selection is two-step: select node A, then select node B. If A-B is a required connection and the line doesn't cross anything, it's drawn. Otherwise, feedback explains why not.

### Completion

A puzzle is complete when all required connections are drawn with no crossings. A celebratory BEEP sequence plays, score is awarded, and the next puzzle loads.

### Visual Design

```
+--------------------------------+
|          L A T T I C E         |  <- title bar (PRINT AT)
+--------------------------------+
|                                |
|      O-----------O            |  <- drawn line (green)
|      |            |            |
|      |    O       |            |  <- unconnected node (white)
|      |            |            |
|      O------O-----O            |
|             |                  |
|            [O]                 |  <- cursor node (yellow ring)
|                                |
+--------------------------------+
| PUZZLE 5/30   LINES: 3/5  **  |  <- HUD (PRINT AT)
+--------------------------------+
```

| Element | INK | Appearance |
|---------|-----|------------|
| Background | Black (0) | Clean dark canvas |
| Nodes (unconnected) | White (7) | CIRCLE radius 3 |
| Nodes (connected) | Green (4) | Shows progress |
| Cursor | Yellow (6) | Larger CIRCLE radius 6 around current node |
| Drawn lines | Green (4) / Cyan (5) / Magenta (3) | Colour varies by band |
| Rejected line (flash) | Red (2) | Drawn briefly, then erased |
| HUD text | White (7) | PRINT AT on bottom two rows |

### Scoring

| Factor | Points |
|--------|--------|
| Completing a puzzle | 100 |
| No undo used | +50 bonus |
| Clean solve (no rejections) | +25 bonus |

Stars per puzzle: one for completion, two for no undo, three for clean solve with no undo.

### Sound

| Event | Sound |
|-------|-------|
| Select node | Short high BEEP |
| Draw valid line | Ascending note (pitch rises with each line) |
| Line rejected | Low buzz |
| Undo | Descending note |
| Puzzle complete | Three-note ascending fanfare |

### Puzzle Design

30 puzzles across three difficulty bands:

| Band | Puzzles | Nodes | Connections | Layout | Challenge |
|------|---------|-------|-------------|--------|-----------|
| 1: Warm-up | 1-8 | 4-6 | 3-5 | Regular grid | Teaches mechanics. Almost impossible to fail. |
| 2: Thinking | 9-15 | 6-9 | 5-8 | Offset grid | Some draw orders cause crossings. Player must plan. |
| 3: Spatial | 16-30 | 8-14 | 7-12 | Irregular / circular | Non-obvious solutions. Layout tricks the eye. |

Puzzles are hand-designed, not generated. Hand design ensures every puzzle has at least one solution, difficulty is intentional, and visual layout is pleasing.

---

## Phase Breakdown

### Phase 1: Dots, Lines and Puzzles (Units 1-16)

Build the graphical foundation, then the full puzzle mechanic. By the end, the learner has a working puzzle game with 15 hand-designed puzzles across two difficulty bands.

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|---------------|
| 1 | A Dot on the Screen | Title screen with "LATTICE" in PRINT AT. Then: PLOT a single white dot on a black background. Explain the Spectrum's pixel coordinate system — 0,0 at bottom-left, 255,175 at top-right. How pixel coordinates differ from the character grid. | PLOT, pixel coordinates (256×176), coordinate origin |
| 2 | Drawing Lines | PLOT a dot, then DRAW a line from it. DRAW takes relative distances (dx, dy), not absolute positions. Draw several lines between pairs of dots to build intuition for the delta calculation. | DRAW, relative coordinates, dx/dy calculation |
| 3 | Circles for Nodes | Replace dots with CIRCLE — a clean filled-looking node at radius 3. Draw a row of evenly spaced circles. Then a 3×3 grid of them, calculating positions with FOR loops. | CIRCLE, radius, calculated spacing |
| 4 | Colour Coding | Set INK before drawing. White nodes on a black background. Draw a line between two nodes in green. Draw another in cyan. Colour distinguishes elements without any text. | INK with graphics commands, colour as information |
| 5 | Node Arrays | Store node positions in arrays: `nx()` for x-coordinates, `ny()` for y-coordinates. Load a 3×3 grid of nodes from DATA into arrays. Draw all nodes from the arrays. | Arrays for coordinates, DATA/READ for positions |
| 6 | Lines Between Nodes | A subroutine that draws a line between two nodes given their indices. Look up coordinates from the arrays, PLOT the start, DRAW to the end. Call it for several pairs. | GO SUB for line drawing, array lookup |
| 7 | The Cursor | Highlight one node as the "current" node — a yellow CIRCLE at larger radius (6) drawn around it. QAOP moves the cursor to the nearest node in that direction. Erase the old cursor (redraw in black), draw the new one. | Cursor state, nearest-node search, erase-and-redraw |
| 8 | Selecting Nodes | SPACE selects the current node. First press highlights it (INK 6, yellow). Second press on a different node attempts to draw a line between them. Two-phase input with a selection state variable. | Two-phase selection, state tracking |
| 9 | Connection Data | DATA defines which pairs of nodes must be connected. Read connection pairs into arrays `ca()` and `cb()`. Display required connections as faint cyan lines (thin, low contrast) so the player knows what to aim for. | Connection pair storage, visual hints |
| 10 | Valid Connection Check | When the player selects two nodes, check if that pair exists in the required connections list. Reject if not: "Not a required connection" in the HUD area. Only valid pairs draw a line. | Array search, pair matching, validation |
| 11 | Crossing Detection | Before drawing a line, sample POINT along its path at 20 evenly spaced intervals. If any sampled pixel is green (INK 4, an existing line), set a crossing flag and reject the line. Draw it briefly in red, BEEP a low buzz, then erase it. | POINT function, pixel colour reading, path sampling |
| 12 | Undo | D removes the last drawn line. Track drawn connections in an undo array. Erase the line by redrawing in black (INK 0), then redraw the nodes at both endpoints (the line may have overwritten them). | Undo stack, erase-by-overdraw, state rollback |
| 13 | Puzzle Complete | After each valid line, check if all required connections have been drawn. If so: "PUZZLE COMPLETE!" with an ascending three-note BEEP fanfare. Score 100 points, plus 50 bonus for no undo used. | Completion detection, score, conditional bonus |
| 14 | Next Puzzle | Store multiple puzzles in DATA. After completing one, RESTORE to the correct line number for the next puzzle. Load new node positions and connections, clear the screen, draw the new puzzle. | RESTORE, DATA sequencing, puzzle progression |
| 15 | The HUD | Reserve the bottom two character rows for status text using PRINT AT. Show "PUZZLE 3/30", "LINES: 2/5", and the current score. The HUD uses text; the play area above uses graphics. Both coexist. | Combining PRINT AT with PLOT/DRAW, screen partitioning |
| 16 | Fifteen Puzzles | Enter 15 hand-designed puzzles across two bands. Band 1 (puzzles 1-8): 4-6 nodes, 3-5 connections, regular grids — warm-ups. Band 2 (puzzles 9-15): 6-9 nodes, 5-8 connections, some with offset positions — the player must plan draw order. Play through all of them. | Puzzle design, difficulty banding, content creation |

**Milestone:** A working puzzle game with 15 puzzles across two difficulty bands. Nodes, lines, crossing detection via POINT, undo, score, puzzle progression, and a HUD. The core is complete.

### Phase 2: Depth and Polish (Units 17-32)

Irregular layouts, more puzzles, visual feedback, and the presentation that makes the game feel finished. By the end: 30 puzzles, three difficulty bands, and a polished experience.

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|---------------|
| 17 | Irregular Layouts | Nodes no longer sit on a regular grid. Place them at arbitrary pixel coordinates — offset, clustered, asymmetric. The crossing-detection and cursor-movement code already handles arbitrary positions because it works with arrays, not grid assumptions. | Free-form coordinate placement, testing existing code with new data |
| 18 | Circular Arrangements | Place nodes in a circle using SIN and COS. Given a centre point and radius, calculate positions: `x = cx + r * COS(a)`, `y = cy + r * SIN(a)` where `a` steps in equal increments around the circle. Visually striking and spatially tricky. | SIN, COS, angles in radians, circular distribution |
| 19 | Band 3 Puzzles | Design 15 harder puzzles (puzzles 16-30): 8-14 nodes, 7-12 connections, irregular and circular layouts. Non-obvious solutions where the draw order matters. Test each puzzle for solvability. Total puzzle count: 30. | Advanced puzzle design, solvability verification |
| 20 | Colour by Band | Each band has a distinct line colour. Band 1: green. Band 2: cyan. Band 3: magenta. The crossing check uses ATTR to read the colour attribute of the character cell rather than checking for a single colour — any non-black ink means collision. | ATTR function, character cell attributes, generalised collision |
| 21 | Connection Preview | After selecting node A, draw faint lines to every node that A has a required (and not yet drawn) connection with. The player sees their options. Erase the preview lines before drawing the real one. | Conditional preview, visual affordance |
| 22 | Rejection Animation | When a line is rejected for crossing, draw it in red INK, pause briefly so the player sees exactly where the crossing happens, then erase it. The player learns from the rejection — they see WHY it failed. | Temporary drawing, visual error feedback |
| 23 | Star Rating | Award 1-3 stars per puzzle. One star for completion. Two stars for no undo. Three stars for no undo and no rejected attempts (clean solve). Show stars next to "PUZZLE COMPLETE!" | Rating tiers, tracking attempts |
| 24 | Puzzle Select Screen | Instead of linear progression, show a numbered list of puzzles. Completed puzzles display their star count. Uncompleted puzzles in the current band show as available. The next band unlocks when the current one is finished. | Menu screen, progress display, band gating |
| 25 | Hint System | Press H to briefly flash all required connections as bright white lines for two seconds, then erase them. Using a hint forfeits the three-star rating for that puzzle. A gentle nudge, not a solution. | Help mechanic, penalty for assistance |
| 26 | Line Drawing Animation | When a valid line is confirmed, it doesn't appear instantly. PLOT the start, then DRAW in small increments from node A towards node B over several steps. The line extends across the screen. Satisfying to watch. | Incremental drawing, animation pacing |
| 27 | Sound Design | Each valid line plays a note — ascending pitch as more connections are made within a puzzle. A 5-connection puzzle plays notes C, D, E, F, G as lines 1-5 are drawn. Completion plays all notes together as a chord. Crossing rejection: low buzz. Undo: descending note. | Musical BEEP design, pitch progression |
| 28 | Node Highlighting | Connected nodes change from white to green. Partially connected nodes (some connections drawn, some remaining) pulse — alternate between white and yellow on each cursor move. The board shows progress at a glance. | Node state display, visual progress indicator |
| 29 | Title Screen | "LATTICE" drawn with PLOT/DRAW — the letters made of connected nodes and lines, in the style of the game itself. A decorative lattice pattern fills the background. Press any key to start. | Artistic use of PLOT/DRAW, title design |
| 30 | Full Game Flow | Title screen, then puzzle select, then play. After completing a puzzle, return to puzzle select. After completing all 30 puzzles, a congratulations screen with total score and total stars. | State machine, screen flow, end-game summary |
| 31 | Balance and Testing | Play every puzzle from 1 to 30 in order. Is the difficulty curve smooth? Any puzzles that feel unfair or trivial? Adjust node positions and connection lists. Test undo, hints, and star tracking across multiple plays. | Playtesting, difficulty tuning, regression testing |
| 32 | The Finished Game | Clean the listing. Remove dead code, tighten line numbers, verify all 30 puzzles load and complete correctly. A calm, contemplative puzzle game: 30 hand-designed puzzles, three difficulty bands, crossing detection via pixel colour, animated line drawing, musical feedback, star ratings, and a puzzle select screen. Under 300 lines. | Code review, final polish, scope verification |

**Milestone:** 30 puzzles across three difficulty bands (regular grids, offset grids, irregular and circular layouts). Puzzle select with star ratings, hints, connection preview, animated line drawing, musical note progression, and clean title-to-completion flow. A finished puzzle game in under 300 lines.

---

## Technical Notes

### Pixel vs Character Coordinates

The Spectrum has two coordinate systems. PRINT AT uses character coordinates (32 columns × 22 rows, origin top-left). PLOT, DRAW, CIRCLE, and POINT use pixel coordinates (256 × 176, origin bottom-left). Lattice uses both: PLOT/DRAW for the game area, PRINT AT for the HUD. The learner must keep track of which system each command expects.

### Crossing Detection via POINT

```basic
600 REM CHECK CROSSING FROM (x1,y1) TO (x2,y2)
610 LET cx = 0
620 LET steps = 20
630 LET dx = (x2 - x1) / steps
640 LET dy = (y2 - y1) / steps
650 LET tx = x1: LET ty = y1
660 FOR i = 1 TO steps - 1
670   LET tx = tx + dx: LET ty = ty + dy
680   IF POINT (INT tx, INT ty) <> 0 THEN LET cx = 1
690 NEXT i
700 RETURN
```

Sample 20 points along the proposed line. If any pixel is set (non-zero, meaning an existing line), the crossing flag `cx` is set. The screen IS the collision map — no mathematical intersection needed.

### Colour-Based Collision with ATTR

When lines use different colours per band, POINT alone isn't enough (it returns 1 or 0 for ink). ATTR reads the full attribute byte of a character cell:

```basic
710 REM CHECK ATTR AT PIXEL (px, py)
720 LET ar = 21 - INT (py / 8)
730 LET ac = INT (px / 8)
740 LET av = ATTR (ar, ac)
750 REM INK = av - 8 * INT (av / 8)
```

If the INK component is non-zero and non-white (not a node), an existing line occupies that cell.

### Node Proximity for Cursor

When the player presses a direction, find the nearest node in that direction:

```basic
500 REM FIND NEAREST NODE IN DIRECTION (ddx, ddy) FROM NODE cn
510 LET best = -1: LET bd = 9999
520 FOR i = 1 TO nn
530   IF i = cn THEN GO TO 580
540   LET ndx = nx(i) - nx(cn): LET ndy = ny(i) - ny(cn)
550   IF ddx <> 0 THEN IF SGN (ndx) <> ddx THEN GO TO 580
560   IF ddy <> 0 THEN IF SGN (ndy) <> ddy THEN GO TO 580
570   LET d = ndx * ndx + ndy * ndy: IF d < bd THEN LET bd = d: LET best = i
580 NEXT i
590 RETURN
```

### Puzzle DATA Format

```
DATA 6                           : REM number of nodes
DATA 40,120, 120,120, 200,120   : REM node pixel coordinates
DATA 40,60,  120,60,  200,60
DATA 5                           : REM number of connections
DATA 1,5, 2,6, 1,3, 4,2, 3,6   : REM connection pairs (node indices)
```

30 puzzles at ~3-4 DATA lines each is ~100-120 DATA lines. With game logic at ~180 lines, total stays under 300.

### Undo Stack

```
DIM ua(20)  - node A of each drawn connection
DIM ub(20)  - node B of each drawn connection
up          - undo pointer (number of drawn connections)
```

Undo: read the top pair, redraw the line in black (INK 0), redraw both endpoint nodes (the line may have overwritten them), decrement the pointer.

### SIN/COS for Circular Layouts

Sinclair BASIC's SIN and COS take radians. To place `n` nodes in a circle of radius `r` centred at `(cx, cy)`:

```basic
FOR i = 1 TO n
  LET a = (i - 1) * 2 * PI / n
  LET nx(i) = cx + r * COS a
  LET ny(i) = cy + r * SIN a
NEXT i
```

### Line Numbering

- 1-49: Initialisation, DIM arrays, variables
- 50-99: Title screen
- 100-149: Puzzle select screen
- 150-199: Puzzle loading (READ DATA, draw nodes)
- 200-299: Main game loop (input, cursor, selection)
- 300-399: Line drawing, crossing detection, undo
- 400-449: HUD, score, stars, puzzle complete
- 450-499: Animations, sound, transitions
- 500-599: Subroutines (cursor movement, node search)
- 600-699: Crossing check, ATTR check
- 1000-1999: Puzzle DATA (30 puzzles)

### Memory

- Game logic: ~6-8 KB
- Puzzle DATA (30 puzzles): ~3 KB
- Variables and arrays: ~1 KB
- Total: ~10-12 KB — comfortable in 48K

---

## Changelog

- **v2.0 (2026-03-13):** Restructured for v5.0 curriculum. Compressed from 64 units (4 phases) to 32 units (2 phases). Puzzle count reduced from 48 to 30 across three bands (down from five). Removed puzzle editor (out of scope at 32 units). Removed puzzle select unlock gating per-band (simplified to linear unlock). Added SIN/COS for circular node layouts and ATTR for multi-colour collision. Carried forward core mechanics, crossing detection via POINT, and design spirit from v1.0.
- **v1.0 (2026-03-09):** Initial game outline as Game 03 in v4.0 curriculum.
