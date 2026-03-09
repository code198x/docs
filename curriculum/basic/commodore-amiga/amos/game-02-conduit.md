# AMOS Game 02: Conduit

**Track:** AMOS
**Genre:** Pipe-routing puzzle
**Units:** 64 (4 phases × 16 units)
**Language:** AMOS Professional
**Max lines:** ~500

---

## Premise

Fluid is about to flow. You have a grid of empty cells and a queue of pipe segments. Click to place, right-click to rotate. Connect the source to the drain before the timer runs out and the fluid starts flowing. If it reaches a dead end or leaks off the grid, you lose.

Pipemania defined this genre. Conduit brings it to AMOS with the Amiga's mouse as the natural interface: point at a cell, click to place, right-click to rotate. The mouse makes this feel intuitive where joystick-based versions felt clumsy.

---

## Core Mechanics

### The Grid

A grid of cells (8×8 for early puzzles, up to 12×10 for later ones). Each cell is empty or contains a pipe segment. The source cell emits fluid from one edge; the drain cell accepts fluid from one edge.

### Pipe Segments

| Segment | Shape | Connections |
|---------|-------|-------------|
| Straight | ═ | Left-right or up-down (rotatable) |
| Corner | ╗ | Two adjacent edges (4 orientations) |
| T-junction | ╦ | Three edges (4 orientations) |
| Cross | ╬ | All four edges (no rotation needed) |
| Dead end | ╡ | One edge only (4 orientations) — penalty piece |

Segments appear in a queue (next 3-5 visible). The player places the current segment, and the queue advances. Rotation cycles through valid orientations.

### Fluid Flow

After a countdown timer expires (or when the player presses GO), fluid begins flowing from the source. It advances one cell per tick, following connected pipe edges. If it reaches:
- **The drain**: level complete, points awarded
- **A dead end or gap**: fluid leaks, level failed
- **An unconnected edge**: fluid leaks

The fluid animation is drawn with AMOS Ink and Paint commands — flood-filling pipe interiors with a bright colour as the fluid advances.

### Scoring

| Factor | Points |
|--------|--------|
| Reaching the drain | 100 × level |
| Each pipe segment fluid passes through | 10 |
| Time bonus (seconds remaining on placement timer) | 5 per second |
| No dead-end pieces placed | +50 bonus |

### Mouse Controls

| Action | Input |
|--------|-------|
| Move cursor | Mouse movement (automatic — cursor follows) |
| Place segment | Left click |
| Rotate segment | Right click |
| Start flow early | Spacebar or middle click |

---

## Phase Breakdown

### Phase 1: Grid and Placement (Units 1-16)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | The Grid | Draw an 8×8 grid using AMOS Box and Line commands. Empty cells with visible borders. | Box, Line, Ink, grid rendering |
| 2 | Mouse Cursor | Custom mouse cursor (a highlighted cell border) that tracks mouse position. | X Mouse, Y Mouse, screen-to-grid conversion |
| 3 | Cell Selection | Click a cell → it highlights. The mouse position maps to a grid coordinate. Zone detection. | Zone, click mapping, grid coordinates |
| 4 | Pipe Sprites | Load pipe segment sprites. Display one in the "next piece" area. | Sprite loading, display |
| 5 | Placing a Pipe | Click an empty cell → current pipe segment appears there. Cell is now occupied. | Grid state array, placement |
| 6 | Rotation | Right-click rotates the current segment (cycles through orientations). Visual update. | Rotation states, modular arithmetic |
| 7 | The Queue | Next 3 segments shown in a sidebar. Placing advances the queue. Random selection from pool. | Queue data structure, random selection |
| 8 | Source and Drain | Special cells: source emits from one edge, drain accepts from one edge. Placed on the grid at level start. | Fixed cells, level setup |
| 9 | Connection Logic | Each pipe segment stores which edges it connects (N/S/E/W). Check if adjacent pipes connect. | Edge arrays, adjacency checking |
| 10 | Connection Highlighting | Connected pipes glow green. Unconnected show red edges. The player sees their network forming. | Visual feedback, state-based colour |
| 11 | Level Data | Level 1 layout in DATA: grid size, source position/direction, drain position/direction, timer. | DATA-driven levels |
| 12 | Placement Timer | Countdown before fluid flows. Displayed as a bar or number. Pressure to place quickly. | Timer, countdown display |
| 13 | Three Levels | Three levels with different source/drain positions and grid sizes. | Multiple levels |
| 14 | Level Select | Choose a level from a menu. Completed levels show a tick. | Menu, progress tracking |
| 15 | Sound | Click sound on placement. Rotation sound. Timer warning beep in last 5 seconds. | Sample Play, audio feedback |
| 16 | Grid Polish | Clean rendering, clear pipe shapes, readable queue. The grid looks professional. | Visual polish |

**Milestone:** Place and rotate pipe segments on a grid with mouse control. Three levels with source and drain. Connection logic works. Ready for fluid flow.

### Phase 2: Flow and Failure (Units 17-32)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | Fluid Start | Timer reaches zero → fluid begins at source cell. First cell fills with colour (Ink, Paint or Bar). | Flood animation, cell filling |
| 18 | Flow Direction | Fluid enters a cell from one edge, flows through the pipe to the connected edge, enters the next cell. | Directional flow, edge tracing |
| 19 | Flow Animation | Fluid fills a cell gradually (draw a coloured bar that extends from entry edge to exit edge over 3-4 frames). | Animated fill, incremental drawing |
| 20 | Dead End Detection | Fluid reaches a cell with no connected exit → LEAK. Red flash. Level failed. | Failure detection, dead-end check |
| 21 | Drain Reached | Fluid reaches the drain → SUCCESS. Green flash, fanfare, points. | Victory detection, celebration |
| 22 | Path Length Scoring | Count cells the fluid passes through. Longer paths = more points. Encourages winding routes. | Path counting, score bonus |
| 23 | Early Start | Player presses GO before timer expires → fluid starts immediately. Earns time bonus. Risk/reward. | Optional early trigger |
| 24 | Replace Pieces | Click an already-placed pipe → replace it with current piece (the old piece is lost). Costs points but fixes mistakes. | Cell overwrite, penalty |
| 25 | Cross Pieces | Cross (╬) pieces allow fluid to pass through in both directions independently. Powerful but rare in queue. | Multi-path flow, special segment |
| 26 | Dead End Pieces | Dead ends (╡) appear in the queue occasionally. Useless — the player must place them somewhere harmless. | Penalty pieces, waste management |
| 27 | Levels 4-8 | Larger grids, trickier source/drain positions, more dead-end pieces in queue. | Mid-game level design |
| 28 | Obstacle Cells | Some cells are blocked (wall). Pipes can't be placed there. Routes must go around. | Obstacles, constrained routing |
| 29 | Flow Speed | Later levels: fluid flows faster. Less time to react if the path isn't ready. | Difficulty via speed |
| 30 | Multiple Paths | Some levels benefit from branching paths (via T-junctions and crosses). Fluid takes all open routes. | Branching flow, simultaneous paths |
| 31 | Fluid Colours | Different fluid colours per level (blue water, green acid, red lava). Cosmetic but adds variety. | Per-level theming |
| 32 | Eight Levels | Eight playable levels with escalating difficulty. | Content milestone |

**Milestone:** Fluid flows through placed pipes. Dead ends cause leaks. The player builds paths under time pressure. Eight levels with obstacles and varied difficulty.

### Phase 3: Depth (Units 33-48)

More levels, advanced mechanics, and replayability features.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | Wrap-Around Pipes | Pipes at grid edges can connect to the opposite edge (like Pac-Man wrapping). Mind-bending routing. | Edge wrapping, modular coordinates |
| 34 | One-Way Valves | Special segment: fluid can only flow in one direction through it. Strategic placement required. | Directional constraint, flow validation |
| 35 | Levels 9-12 | Wrap-around, one-way valves, larger grids, faster flow. | Advanced level design |
| 36 | Two Sources | Some levels have two sources that must both reach their respective drains. Two independent networks on one grid. | Multi-network flow |
| 37 | Levels 13-16 | Two-source levels, maximum difficulty. | Expert levels |
| 38 | Star Rating | 1-3 stars per level based on: path length, time bonus, no replacements. | Rating system |
| 39 | Statistics | Total stars, average path length, fastest completion. Session stats. | Aggregate tracking |
| 40 | Hint System | Press H: briefly flash the shortest valid path. Costs the 3-star rating. | Pathfinding hint, penalty |
| 41 | Undo | Press U: remove the last placed pipe and return it to the queue. Limited to 3 undos per level. | Undo stack, limited resource |
| 42 | Palette Themes | Each level group has a colour theme: levels 1-4 blue, 5-8 green, 9-12 amber, 13-16 red. | Visual variety |
| 43 | Flow Sound | Fluid flowing makes a sound (water gurgle via Sample Play). Pitch rises as path gets longer. | Dynamic audio |
| 44 | Leak Sound | Leak: harsh buzzer. Drain reached: satisfying glug. Distinct audio for success/failure. | Outcome-based audio |
| 45 | Transition Effects | Between levels: grid fades (palette manipulation), new grid draws. | Palette fade transitions |
| 46 | Edge Cases | Fluid reaches a T-junction: does it split correctly? Cross piece with two independent flows? Test thoroughly. | Flow logic validation |
| 47 | Balance Pass | All 16 levels, all difficulties. Is the queue fair? Are dead-end pieces too frequent? | Balance testing |
| 48 | Sixteen Levels | 16 complete levels with star ratings, hints, undo, varied mechanics. | Content-complete |

### Phase 4: Completion (Units 49-64)

Title, polish, puzzle editor, and final presentation.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Title Screen | "CONDUIT" with animated fluid flowing through title-screen pipes. | Animated title |
| 50 | Instructions | Visual tutorial: show a 3×3 grid, place pipes, flow. Interactive, not text-heavy. | Interactive instructions |
| 51 | MOD Music | Background music during placement phase. Stops during flow (tension). Resumes on success. | Track Load/Play, conditional music |
| 52 | Puzzle Editor | Place source, drain, obstacles on a blank grid. Test the puzzle. Export as DATA. | Editor mode, content creation |
| 53-60 | Polish: animations, sound, editor refinement, testing | Various improvements | Multiple techniques |
| 61-63 | Bug sweep, balance, line count | QA and scope | Various |
| 64 | The Finished Game | 16 pipe puzzles, star ratings, hints, undo, puzzle editor, MOD music. A complete mouse-driven puzzle game. | Completion |

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. New AMOS Game 2 in the restructured Amiga BASIC track. Pipe-routing puzzle with mouse control.
