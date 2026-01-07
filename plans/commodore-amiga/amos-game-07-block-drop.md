# Block Drop: 64-Unit Outline

**Game:** 7 of 8 (AMOS BASIC)
**Platform:** Commodore Amiga
**Language:** AMOS BASIC
**Units:** 64 (4 phases)
**Concept:** Falling blocks puzzle. Tetris-style rotation and line clearing.

---

## Why This Game Seventh?

Block Drop introduces puzzle game mechanics:

1. **Piece rotation** - Mathematical transformation
2. **Grid collision** - Complex detection
3. **Line clearing** - Row detection and removal
4. **Preview system** - Next piece display
5. **Two-player** - Competitive mode

Applies grid logic in new context.

---

## Skills Applied from Previous Games

| Skill | From | Application in Block Drop |
|-------|------|--------------------------|
| Grid systems | Maze Runner | Playfield |
| Bob rendering | All | Block drawing |
| Collision | All | Piece collision |
| Score systems | All | Points and levels |
| State management | Dungeon Doors | Game state |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Piece rotation | 1 | Coordinate transform |
| Grid collision | 2 | Complex detection |
| Line detection | 2 | Full row check |
| Line clearing | 2 | Row removal |
| Two-player mode | 4 | Competitive play |

---

## Phase 1: Piece Mechanics (Units 1-16)
*Tetromino handling.*

### Units 1-4: Piece Data
- **Unit 1:** Tetromino shapes - 7 pieces
- **Unit 2:** Piece data - cell coordinates
- **Unit 3:** Rotation states - 4 per piece
- **Unit 4:** Rotation data - all states

### Units 5-8: Piece Display
- **Unit 5:** Block bobs - coloured cells
- **Unit 6:** Piece rendering - from data
- **Unit 7:** Piece colours - per type
- **Unit 8:** Piece preview - next piece

### Units 9-12: Piece Movement
- **Unit 9:** Horizontal move - left/right
- **Unit 10:** Rotation - clockwise
- **Unit 11:** Soft drop - faster fall
- **Unit 12:** Hard drop - instant

### Units 13-16: Basic Play
- **Unit 13:** Fall timing - gravity
- **Unit 14:** Current piece - active
- **Unit 15:** Spawn new - after lock
- **Unit 16:** Basic demo - falling pieces

**Phase Goal:** Moving, rotating pieces.

---

## Phase 2: Playfield Mechanics (Units 17-32)
*Grid and line clearing.*

### Units 17-20: Playfield
- **Unit 17:** Playfield array - 10×20 grid
- **Unit 18:** Playfield rendering - draw all
- **Unit 19:** Cell states - empty, filled, colour
- **Unit 20:** Field display - visible area

### Units 21-24: Collision
- **Unit 21:** Movement collision - can move?
- **Unit 22:** Rotation collision - can rotate?
- **Unit 23:** Wall kicks - rotation assist
- **Unit 24:** Floor collision - piece landed

### Units 25-28: Locking and Lines
- **Unit 25:** Piece locking - add to field
- **Unit 26:** Line detection - full rows
- **Unit 27:** Line clearing - remove rows
- **Unit 28:** Lines dropping - collapse above

### Units 29-32: Line Effects
- **Unit 29:** Clear animation - flash effect
- **Unit 30:** Multiple lines - 1,2,3,4
- **Unit 31:** Tetris bonus - 4-line clear
- **Unit 32:** Cascade effect - visual

**Phase Goal:** Complete playfield with line clearing.

---

## Phase 3: Game Features (Units 33-48)
*Scoring, levels, polish.*

### Units 33-36: Scoring
- **Unit 33:** Line scoring - points per line
- **Unit 34:** Level multiplier - more points
- **Unit 35:** Soft drop points - bonus
- **Unit 36:** Hard drop points - bonus

### Units 37-40: Level Progression
- **Unit 37:** Lines for level - threshold
- **Unit 38:** Speed increase - faster gravity
- **Unit 39:** Level display - current
- **Unit 40:** Max level - end point

### Units 41-44: Game Features
- **Unit 41:** Ghost piece - landing preview
- **Unit 42:** Hold piece - store for later
- **Unit 43:** Next queue - multiple preview
- **Unit 44:** Statistics - piece counts

### Units 45-48: Audio
- **Unit 45:** Move sounds - shift, rotate
- **Unit 46:** Lock sound - piece placed
- **Unit 47:** Clear sounds - by lines
- **Unit 48:** Background music - theme

**Phase Goal:** Full single-player features.

---

## Phase 4: Modes and Polish (Units 49-64)
*Two-player and completion.*

### Units 49-52: Two-Player Mode
- **Unit 49:** Split screen - two fields
- **Unit 50:** Separate controls - P1/P2
- **Unit 51:** Separate scores - tracking
- **Unit 52:** Garbage lines - attacks

### Units 53-56: Two-Player Features
- **Unit 53:** Line attacks - send garbage
- **Unit 54:** Garbage display - pending
- **Unit 55:** Victory condition - top out
- **Unit 56:** Match structure - best of

### Units 57-60: Game Modes
- **Unit 57:** Marathon - endless
- **Unit 58:** Sprint - 40 lines
- **Unit 59:** Ultra - time limit
- **Unit 60:** Versus - two player

### Units 61-64: Completion
- **Unit 61:** Title screen
- **Unit 62:** High score system
- **Unit 63:** Full testing
- **Unit 64:** Release build

**Phase Goal:** Complete puzzle game.

---

## Summary

**Block Drop** teaches puzzle game mechanics.

### Game Specifications

- **Pieces:** 7 tetrominoes, 4 rotations each
- **Playfield:** 10×20 grid
- **Controls:** Move, rotate, soft/hard drop
- **Features:** Ghost, hold, next preview
- **Lines:** 1-4, Tetris bonus for 4
- **Levels:** Speed increases with lines
- **Modes:** Marathon, Sprint, Ultra, Versus
- **Two-Player:** Split-screen competitive
- **Display:** AMOS screen, bobs for blocks
- **Sound:** Effects and music
- **Distribution:** AMOS source + compiled
