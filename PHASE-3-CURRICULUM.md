# Phase 3: Puzzle Games (Lessons 1025-1536)

**Total:** 512 lessons across 8 tiers (64 lessons per tier)

**Phase Goal:** Master logic-based puzzle games. Learn grid systems, rotation algorithms, pattern matching, and multi-unit pathfinding.

**Prerequisites:** Phases 1-2 complete (action game foundations, basic AI, grid concepts from Pac-Man/Frogger)

**Phase Philosophy:**
- Logic over reflexes
- Pattern recognition and spatial reasoning
- Algorithmic thinking (rotation, matching, cascades)
- Multi-unit management
- Proper pacing - puzzles need depth

**Game Progression:**
- **Tier 1:** Tetris - The definitive falling block puzzle
- **Tier 2:** Columns - Match-3 with rotation and cascades
- **Tier 3:** Dr. Mario - Dual-axis matching with viruses
- **Tier 4:** Klax - Conveyor belt + stacking mechanics
- **Tier 5:** Lemmings - Multi-unit pathfinding and jobs
- **Tier 6:** Pipe Mania - Flow systems and time pressure
- **Tier 7:** Chip's Challenge - Grid puzzles with monsters
- **Tier 8:** Sokoban - Push-only puzzles with undo

**What Students Master:**
- Grid-based game architecture
- Rotation algorithms (Tetris, Dr. Mario)
- Pattern matching (lines, clusters, colors)
- Cascade/combo logic
- Multi-unit AI (Lemmings)
- Pathfinding (A*, flow fields)
- Undo/redo systems
- Puzzle generation and validation
- Difficulty curves

---

## Phase 3 Overview

| Tier | Game | Deliverable | Key Skills |
|------|------|-------------|------------|
| 1 | Tetris | Falling blocks | Rotation, line clearing, gravity, speed increase |
| 2 | Columns | Match-3 vertical | Gem rotation, cascade clearing, combos |
| 3 | Dr. Mario | Virus puzzle | Match-4, pill rotation, dual-axis, viruses |
| 4 | Klax | Conveyor stacking | Belt mechanics, diagonal matching, timing |
| 5 | Lemmings | Multi-unit puzzle | Pathfinding, job assignment, save quota |
| 6 | Pipe Mania | Flow puzzle | Tile placement, flow system, time limit |
| 7 | Chip's Challenge | Grid adventure | Block pushing, keys/doors, monster AI |
| 8 | Sokoban | Push puzzles | Push-only, undo, puzzle validation, difficulty |

**Technical Progression:**
- Tiers 1-4: Single-focus puzzles (rotation, matching, stacking)
- Tiers 5-6: Time pressure and flow systems
- Tiers 7-8: Strategic thinking and planning

---

## Tier 1: Tetris (Lessons 1025-1088)

**Goal:** Build complete Tetris with rotation, line clearing, and progression.

**Why this game:** THE definitive puzzle game. Teaches rotation algorithms, grid management, line clearing, and difficulty progression.

**Game Requirements:**
- 7 tetrominoes (I, O, T, L, J, S, Z)
- 10×20 playfield
- Rotation (4 orientations for most pieces)
- Line clearing (1-4 lines simultaneously)
- Scoring (lines, combos, level)
- Gravity (speed increases with level)
- Next piece preview
- Game over when pieces stack to top
- High score table

**Skills Introduced:**
- Grid representation (10×20 array)
- Tetromino data structures (4×4 grids)
- Rotation algorithm (matrix transformation)
- Collision detection (piece vs playfield)
- Line detection (full rows)
- Line clearing (collapse above)
- Gravity system (timed dropping)
- Progressive difficulty (speed curve)

### Lesson Structure

**Lessons 1025-1032: Grid System**
- L1025-1026: Playfield grid (10×20 byte array)
- L1027-1028: Drawing grid with characters
- L1029-1030: Cell states (empty, occupied, color)
- L1031-1032: Grid-to-screen mapping

**Lessons 1033-1040: Tetrominoes**
- L1033-1034: Tetromino data structure (7 pieces × 4 rotations)
- L1035-1036: Current piece position (X, Y, rotation)
- L1037-1038: Drawing active piece
- L1039-1040: Piece colors

**Lessons 1041-1048: Rotation**
- L1041-1042: Rotation algorithm (90° clockwise)
- L1043-1044: Wall kicks (adjustment when rotation hits wall)
- L1045-1046: Floor kicks
- L1047-1048: Rotation collision detection

**Lessons 1049-1056: Movement**
- L1049-1050: Left/right movement
- L1051-1052: Soft drop (faster falling)
- L1053-1054: Hard drop (instant placement)
- L1055-1056: Movement collision detection

**Lessons 1057-1064: Gravity**
- L1057-1058: Timer-based falling
- L1059-1060: Lock delay (grace period at bottom)
- L1061-1062: Piece locking (transfer to playfield)
- L1063-1064: Spawn next piece

**Lessons 1065-1072: Line Clearing**
- L1065-1066: Detect full lines
- L1067-1068: Clear lines (remove from grid)
- L1069-1070: Collapse above cleared lines
- L1071-1072: Multiple simultaneous clears (1-4 lines)

**Lessons 1073-1080: Scoring & Levels**
- L1073-1074: Scoring system (40/100/300/1200 points)
- L1075-1076: Level progression (every 10 lines)
- L1077-1078: Speed increase per level
- L1079-1080: Score display

**Lessons 1081-1088: Polish & Completion**
- L1081-1082: Next piece preview
- L1083-1084: Game over detection
- L1085-1086: High score table (save to disk)
- L1087-1088: Sound effects and final polish

### Example Code Pattern (Rotation)

```assembly
; Rotate piece 90° clockwise
ROTATE_PIECE:
    LDA CURRENT_ROTATION
    CLC
    ADC #1
    AND #$03        ; Wrap 0-3
    STA TEMP_ROT

    ; Check collision with new rotation
    JSR CHECK_COLLISION
    BCC ROTATION_OK ; Carry clear = no collision

    ; Try wall kick
    JSR TRY_WALL_KICK
    BCC ROTATION_OK

    RTS             ; Failed to rotate

ROTATION_OK:
    LDA TEMP_ROT
    STA CURRENT_ROTATION
    RTS
```

---

## Tier 2: Columns (Lessons 1089-1152)

**Goal:** Build Columns with gem matching, rotation, and cascades.

**Why this game:** Introduces vertical match-3, in-flight rotation, and cascade combos.

**Game Requirements:**
- 3-gem columns fall from top
- Rotate gems within column (in-flight)
- Match 3+ horizontal, vertical, or diagonal
- Gems above fall when matches clear
- Cascade combos (chain reactions)
- Magic gems (clear all of one color)
- Increasing difficulty
- Filling pattern at bottom

**Skills Introduced:**
- In-flight rotation (column gem swapping)
- Multi-directional matching (horizontal, vertical, diagonal)
- Cascade detection and combos
- Gravity for individual gems (not whole pieces)
- Magic gem system
- Difficulty via starting pattern

---

## Tier 3: Dr. Mario (Lessons 1153-1216)

**Goal:** Build Dr. Mario with pill rotation and virus clearing.

**Why this game:** Two-part pieces, dual-axis matching, specific targets (viruses).

**Game Requirements:**
- Viruses fill bottom of bottle (random placement)
- Two-color pills fall
- Match 4+ (horizontal or vertical) to clear
- Pills split if one half matches
- Clear all viruses to win
- Level selection (virus count/speed)
- Music (Fever, Chill)

**Skills Introduced:**
- Two-segment pieces (pills can split)
- Dual-axis matching (horizontal AND vertical)
- Target-based victory (clear all viruses, not score)
- Piece splitting (half clears, half remains)
- Suspended pieces (hanging after split)

---

## Tier 4: Klax (Lessons 1217-1280)

**Goal:** Build Klax with conveyor belt and diagonal matching.

**Why this game:** Timing-based puzzle, diagonal matches, catch-and-stack mechanics.

**Game Requirements:**
- Conveyor belt delivers tiles
- Paddle catches tiles (5 capacity)
- Drop tiles into columns (5 columns)
- Match 3+ horizontal, vertical, or diagonal
- Different goals per level (X matches, X diagonals)
- Drop tiles off screen (penalty)
- Wave progression

**Skills Introduced:**
- Conveyor belt system (scrolling tiles)
- Catch mechanics (timing)
- Stack limit (paddle capacity)
- Diagonal matching
- Goal-based levels (different objectives)
- Drop penalty system

---

## Tier 5: Lemmings (Lessons 1281-1344)

**Goal:** Build Lemmings with pathfinding and job assignment.

**Why this game:** Most complex puzzle game. Multi-unit pathfinding, job system, real-time puzzle solving.

**Game Requirements:**
- Lemmings spawn from entrance
- Walk until obstacle (turn around)
- Fall (die if too far)
- Exit when reaching goal
- 8 jobs (climber, floater, bomber, blocker, builder, basher, miner, digger)
- Assign jobs to individual lemmings
- Save X% to win level
- Time limit
- Release rate control
- Nuke (destroy all)

**Skills Introduced:**
- **Multi-unit pathfinding** (100 lemmings simultaneously)
- **Job system** (assign behaviors to units)
- **Terrain modification** (dig, build, bash)
- **Save quota** (X% must survive)
- **Real-time puzzle** (not turn-based)
- **Spawn rate control**

### Lesson Structure

**Lessons 1281-1288: Lemmings AI**
- L1281-1282: Basic walker AI (move until obstacle)
- L1283-1284: Falling physics (velocity, death height)
- L1285-1286: Turning at walls
- L1287-1288: Exit detection

**Lessons 1289-1296: Terrain**
- L1289-1290: Terrain bitmap (1-bit per pixel)
- L1291-1292: Collision with terrain
- L1293-1294: Terrain modification (digging)
- L1295-1296: Terrain display

**Lessons 1297-1304: Jobs - Digging**
- L1297-1298: Basher (horizontal tunnel)
- L1299-1300: Miner (diagonal down)
- L1301-1302: Digger (vertical down)
- L1303-1304: Digging animation and terrain removal

**Lessons 1305-1312: Jobs - Building**
- L1305-1306: Builder (stairs)
- L1307-1308: Building animation
- L1309-1310: Stair creation (add terrain)
- L1311-1312: Builder limit (12 bricks)

**Lessons 1313-1320: Jobs - Special**
- L1313-1314: Blocker (wall)
- L1315-1316: Bomber (explosion + terrain removal)
- L1317-1318: Climber (climb walls)
- L1319-1320: Floater (umbrella, safe falling)

**Lessons 1321-1328: Job Assignment**
- L1321-1322: Cursor control
- L1323-1324: Select lemming under cursor
- L1325-1326: Assign job to selected
- L1327-1328: Job icon UI

**Lessons 1329-1336: Level Management**
- L1329-1330: Spawn rate control
- L1331-1332: Time limit countdown
- L1333-1334: Save percentage calculation
- L1335-1336: Win/loss conditions

**Lessons 1337-1344: Polish**
- L1337-1338: Nuke command
- L1339-1340: Pause/fast-forward
- L1341-1342: Level select
- L1343-1344: Sound effects and completion

---

## Tier 6: Pipe Mania (Lessons 1345-1408)

**Goal:** Build Pipe Mania with flow system and time pressure.

**Why this game:** Real-time tile placement, flow simulation, planning under pressure.

**Game Requirements:**
- Random pipe pieces in queue
- Place pipes on grid (before flow starts)
- Flow starts from entry point
- Flow follows connected pipes
- Points for pipe length
- Cross pieces required
- Leaks end game
- Time pressure

**Skills Introduced:**
- Flow simulation (liquid moving through pipes)
- Pipe connectivity (valid connections)
- Real-time tile placement
- Planning under time pressure
- Piece queue system

---

## Tier 7: Chip's Challenge (Lessons 1409-1472)

**Goal:** Build Chip's Challenge with puzzles, monsters, and items.

**Why this game:** Grid-based puzzle-adventure hybrid. Keys, doors, blocks, monsters.

**Game Requirements:**
- Grid-based movement (tile-by-tile)
- Collect chips to unlock exit
- Keys open colored doors
- Push blocks (Sokoban-style)
- Monsters patrol (simple AI)
- Items (flippers for water, boots for fire)
- 149 levels
- Time limit per level

**Skills Introduced:**
- Grid puzzle design
- Key/door systems
- Block pushing (Sokoban mechanics)
- Monster AI (patrol patterns)
- Item-based abilities
- Level progression (puzzle sequences)

---

## Tier 8: Sokoban (Lessons 1473-1536)

**Goal:** Build Sokoban with push-only mechanics and undo.

**Why this game:** Pure logic puzzles. Undo system. Puzzle validation. Perfect synthesis of Phase 3.

**Game Requirements:**
- Push blocks onto goal squares
- Cannot pull blocks (push only)
- Undo moves (essential for trial-and-error)
- Detect unsolvable states (block in corner)
- 50+ levels (increasing difficulty)
- Move counter
- Level select

**Skills Introduced:**
- **Undo/redo system** (move stack)
- **Push-only mechanics** (directional puzzle design)
- **Unsolvable state detection** (blocks in corners)
- **Puzzle validation** (ensure solvable)
- **Difficulty progression** (puzzle complexity curve)

### Lesson Structure

**Lessons 1473-1480: Grid and Movement**
- L1473-1474: Grid representation (walls, floor, goals)
- L1475-1476: Player movement (tile-based)
- L1477-1478: Block positions
- L1479-1480: Goal squares

**Lessons 1481-1488: Push Mechanics**
- L1481-1482: Push detection (player → block)
- L1483-1484: Block movement (push direction)
- L1485-1486: Cannot push two blocks
- L1487-1488: Push collision (walls, other blocks)

**Lessons 1489-1496: Undo System**
- L1489-1490: Move stack (last 100 moves)
- L1491-1492: Push move stack entry (player + block positions)
- L1493-1494: Undo command (pop stack, restore state)
- L1495-1496: Redo command

**Lessons 1497-1504: Win Detection**
- L1497-1498: Check all blocks on goals
- L1499-1500: Level complete
- L1501-1502: Victory animation
- L1503-1504: Next level

**Lessons 1505-1512: Unsolvable Detection**
- L1505-1506: Detect block in corner (cannot escape)
- L1507-1508: Detect block against wall + not on goal
- L1509-1510: Warning to player
- L1511-1512: Auto-undo to before unsolvable move

**Lessons 1513-1520: Level System**
- L1513-1514: Level data format (compact representation)
- L1515-1516: Level loading
- L1517-1518: Level select screen
- L1519-1520: 50 levels (data)

**Lessons 1521-1528: UI and Display**
- L1521-1522: Move counter
- L1523-1524: Level number display
- L1525-1526: On-screen goals (blocks on goals indicator)
- L1527-1528: Graphics and tiles

**Lessons 1529-1536: Polish and Completion**
- L1529-1530: Restart level command
- L1531-1532: Save progress (last level)
- L1533-1534: Sound effects
- L1535-1536: Final polish

---

## Phase 3 Outcome

Students have built **8 complete puzzle games** and mastered:

**Grid Systems:**
- Tile-based world representation
- Grid-to-screen rendering
- Cell states and properties
- Grid collision detection

**Algorithms:**
- Rotation (matrix transformation, wall kicks)
- Pattern matching (lines, clusters, diagonals)
- Cascade detection (chain reactions)
- Flow simulation
- Unsolvable state detection

**Multi-Unit Management:**
- Pathfinding (Lemmings)
- Job assignment
- Individual unit AI
- Spawn control

**Puzzle Design:**
- Difficulty progression
- Puzzle validation
- Goal-based levels
- Time pressure vs pure logic

**Game Systems:**
- Undo/redo
- Save/load progress
- Level selection
- Scoring and combos
- High scores

**Ready for Phase 4:** Students transition from pure logic puzzles to platformers, combining puzzle-solving with action mechanics.

---

**Version:** 3.0
**Date:** 2025-10-20
**Status:** Complete restructure for 512-lesson phase
**Focus:** 8 puzzle games from Tetris to Sokoban
