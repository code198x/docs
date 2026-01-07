# Tetrad: 64-Unit Outline

**Game:** 8 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 64 (4 phases)
**Concept:** Falling blocks puzzle with Blitter rendering.

---

## Why This Game Eighth?

Tetrad completes the foundation with puzzle mechanics:

1. **Piece rotation** - Mathematical transformation
2. **Grid collision** - Complex detection
3. **Line clearing** - Blitter scroll operations
4. **Two-player mode** - Split display
5. **Preview system** - Next piece display

The last foundation game before advanced techniques.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Grid systems | All | Playfield |
| Blitter tiles | All | Block rendering |
| Collision | All | Piece placement |
| Ring buffer | Venom | Next queue |
| State machines | Gobble | Game states |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Piece rotation | 1 | Coordinate transform |
| Kick detection | 2 | Wall kicks |
| Line detection | 2 | Full row scan |
| Blitter scroll | 2 | Line clearing |
| Split display | 4 | Two playfields |

---

## Phase 1: Piece System (Units 1-16)
*Tetromino handling.*

### Units 1-4: Piece Data
- **Unit 1:** Tetromino shapes - 7 pieces
- **Unit 2:** Piece representation - 4 cells
- **Unit 3:** Rotation states - 4 per piece
- **Unit 4:** Piece data tables - all rotations

### Units 5-8: Piece Display
- **Unit 5:** Block sprite - single cell
- **Unit 6:** Block colours - per piece type
- **Unit 7:** Piece drawing - 4 blocks
- **Unit 8:** Active piece - current falling

### Units 9-12: Piece Movement
- **Unit 9:** Left/right - horizontal shift
- **Unit 10:** Soft drop - faster fall
- **Unit 11:** Hard drop - instant
- **Unit 12:** Rotation - state change

### Units 13-16: Basic Play
- **Unit 13:** Gravity - automatic fall
- **Unit 14:** Fall timing - per-frame
- **Unit 15:** Spawn new - from preview
- **Unit 16:** Piece demo - falling, moving

**Phase Goal:** Falling, rotating pieces.

---

## Phase 2: Playfield Mechanics (Units 17-32)
*Grid and line clearing.*

### Units 17-20: Playfield
- **Unit 17:** Playfield array - 10×20 grid
- **Unit 18:** Cell states - empty, filled, colour
- **Unit 19:** Playfield rendering - Blitter
- **Unit 20:** Border display - frame

### Units 21-24: Collision Detection
- **Unit 21:** Movement collision - can move?
- **Unit 22:** Rotation collision - can rotate?
- **Unit 23:** Wall kicks - shift and rotate
- **Unit 24:** Floor collision - lock piece

### Units 25-28: Line Clearing
- **Unit 25:** Line detection - scan rows
- **Unit 26:** Full line - all cells filled
- **Unit 27:** Line removal - clear row
- **Unit 28:** Blitter scroll - drop rows above

### Units 29-32: Locking
- **Unit 29:** Lock delay - time before lock
- **Unit 30:** Piece to field - copy cells
- **Unit 31:** Spawn next - new piece
- **Unit 32:** Clear animation - flash effect

**Phase Goal:** Complete playfield mechanics.

---

## Phase 3: Scoring and Levels (Units 33-48)
*Points and progression.*

### Units 33-36: Scoring
- **Unit 33:** Lines to points - 1,2,3,4
- **Unit 34:** Tetris bonus - 4-line clear
- **Unit 35:** Level multiplier - more points
- **Unit 36:** Score display - 6+ digits

### Units 37-40: Level System
- **Unit 37:** Lines for level - threshold
- **Unit 38:** Speed increase - faster gravity
- **Unit 39:** Level display - current
- **Unit 40:** Speed table - per level

### Units 41-44: Preview System
- **Unit 41:** Next piece - preview area
- **Unit 42:** Next queue - multiple preview
- **Unit 43:** Random generation - bag system
- **Unit 44:** Hold piece - store for later

### Units 45-48: Ghost Piece
- **Unit 45:** Ghost concept - landing preview
- **Unit 46:** Ghost position - project down
- **Unit 47:** Ghost display - translucent
- **Unit 48:** Ghost toggle - option

**Phase Goal:** Full scoring and features.

---

## Phase 4: Modes and Polish (Units 49-64)
*Two-player and completion.*

### Units 49-52: Two-Player Mode
- **Unit 49:** Split screen - two fields
- **Unit 50:** Separate controls - P1/P2
- **Unit 51:** Independent games - simultaneous
- **Unit 52:** Garbage lines - attacks

### Units 53-56: Versus Features
- **Unit 53:** Line attacks - send garbage
- **Unit 54:** Garbage queue - pending lines
- **Unit 55:** Victory condition - top out
- **Unit 56:** Match system - best of

### Units 57-60: Audio
- **Unit 57:** Move sounds - shift, rotate
- **Unit 58:** Lock sound - piece placed
- **Unit 59:** Clear sounds - by lines
- **Unit 60:** Music - gameplay theme

### Units 61-64: Release
- **Unit 61:** Title screen
- **Unit 62:** High scores
- **Unit 63:** Full testing
- **Unit 64:** Release build - ADF

**Phase Goal:** Complete Tetris clone.

---

## Summary

**Tetrad** completes foundation with puzzle mechanics.

### Technical Specifications

- **Display:** 320×256, 5 bitplanes
- **Playfield:** 10×20 grid
- **Pieces:** 7 tetrominoes, 4 rotations
- **Features:** Ghost, hold, preview queue
- **Line clear:** Blitter scroll
- **Modes:** Marathon, versus
- **Players:** 1-2 split screen
- **Distribution:** Bootable ADF

### Skills for Next Game

Ready for advanced techniques:
- All Blitter operations
- Complex collision systems
- Two-player split display
- Efficient data structures
- Full game state management

**Next: Dual playfield and parallax scrolling**
