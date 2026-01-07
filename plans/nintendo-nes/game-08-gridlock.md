# Gridlock: 64-Unit Outline

**Game:** 8 of 16
**Platform:** Nintendo Entertainment System
**Units:** 64 (4 phases)
**Concept:** Falling blocks puzzle game. Rotate tetrominoes, clear lines, survive the gridlock. Tetris-style classic.

---

## Why This Game Eighth?

Gridlock introduces piece rotation and line clearing:

1. **Piece rotation** - Rotating shapes mathematically
2. **Rotation collision** - Testing rotated pieces fit
3. **Line detection** - Finding complete rows
4. **Line clearing** - Removing and collapsing
5. **Preview systems** - Showing next piece

This completes the foundation with a different genre.

---

## Skills Applied from Previous Games

| Skill | From | Application in Gridlock |
|-------|------|------------------------|
| Grid display | Fangs | Play field grid |
| Background modification | Fracture Point | Placing/clearing blocks |
| Frame timing | All | Drop speed control |
| Input handling | All | Movement, rotation |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Piece rotation | 1 | Rotating shapes |
| Rotation collision | 2 | Testing fit |
| Wall kicks | 2 | Position adjustment |
| Line detection | 2 | Complete row check |
| Line clearing | 2 | Row removal |
| Ghost piece | 3 | Drop preview |
| Next piece preview | 3 | Queue display |

---

## Phase 1: Pieces and Grid (Units 1-16)
*Tetromino display and movement.*

### Units 1-4: Play Field
- **Unit 1:** Grid structure - 10×20 well
- **Unit 2:** Grid display - drawing the well
- **Unit 3:** Cell states - empty, filled, colours
- **Unit 4:** Grid borders - walls and floor

### Units 5-8: Tetromino Data
- **Unit 5:** Piece shapes - 7 tetrominoes (I, O, T, S, Z, J, L)
- **Unit 6:** Piece storage - 4×4 grid per piece
- **Unit 7:** Rotation states - 4 rotations per piece
- **Unit 8:** Piece colours - distinct per type

### Units 9-12: Piece Display
- **Unit 9:** Current piece - type, rotation, position
- **Unit 10:** Piece rendering - draw at position
- **Unit 11:** Piece on grid - combine with field
- **Unit 12:** Piece colours - correct attributes

### Units 13-16: Basic Movement
- **Unit 13:** Left/right input - horizontal movement
- **Unit 14:** Movement collision - stop at walls
- **Unit 15:** Piece bounds - validation
- **Unit 16:** Playable foundation - piece moves in well

**Phase Goal:** Tetromino moves left/right in well.

---

## Phase 2: Rotation and Placement (Units 17-32)
*Rotation, landing, and line clearing.*

### Units 17-20: Piece Rotation
- **Unit 17:** Rotation input - clockwise/anticlockwise
- **Unit 18:** Rotation state change - cycle states
- **Unit 19:** Rotation collision - check fit
- **Unit 20:** Wall kicks - adjust position when blocked

### Units 21-24: Piece Falling
- **Unit 21:** Gravity timer - piece drops over time
- **Unit 22:** Downward collision - stop at floor/blocks
- **Unit 23:** Piece locking - become part of grid
- **Unit 24:** New piece spawn - next appears at top

### Units 25-28: Line Clearing
- **Unit 25:** Line detection - check rows complete
- **Unit 26:** Single line clear - remove row
- **Unit 27:** Row collapse - move rows down
- **Unit 28:** Multi-line clear - detect 2, 3, 4 lines

### Units 29-32: Game Rules
- **Unit 29:** Game over - blocked at spawn
- **Unit 30:** Score calculation - points per lines
- **Unit 31:** Line counter - total cleared
- **Unit 32:** Complete game loop - playable Tetris

**Phase Goal:** Full piece mechanics with line clearing.

---

## Phase 3: Features and Polish (Units 33-48)
*Preview, ghost, advanced controls.*

### Units 33-36: Next Piece Preview
- **Unit 33:** Piece queue - generate next
- **Unit 34:** Preview area - side panel
- **Unit 35:** Preview rendering - show next
- **Unit 36:** Queue management - advance on spawn

### Units 37-40: Ghost Piece
- **Unit 37:** Ghost calculation - where piece lands
- **Unit 38:** Ghost display - outline version
- **Unit 39:** Ghost updating - recalculate on move
- **Unit 40:** Ghost toggle - option to show/hide

### Units 41-44: Advanced Controls
- **Unit 41:** Soft drop - hold down for faster
- **Unit 42:** Hard drop - instant placement
- **Unit 43:** Delayed auto-shift - hold for repeat
- **Unit 44:** Lock delay - time before lock

### Units 45-48: Sound
- **Unit 45:** Move sound - piece movement
- **Unit 46:** Rotate sound - rotation feedback
- **Unit 47:** Line clear sound - satisfying effect
- **Unit 48:** Tetris sound - 4-line fanfare

**Phase Goal:** Polished with preview and controls.

---

## Phase 4: Levels and Release (Units 49-64)
*Difficulty and presentation.*

### Units 49-52: Level System
- **Unit 49:** Level progression - advance after X lines
- **Unit 50:** Speed increase - faster per level
- **Unit 51:** Speed table - defined per level
- **Unit 52:** Level display - show current

### Units 53-56: Scoring Depth
- **Unit 53:** Scoring formula - more at higher levels
- **Unit 54:** Combo scoring - consecutive clears
- **Unit 55:** High score - best scores
- **Unit 56:** Statistics - pieces placed

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Level select - start higher
- **Unit 59:** Pause - pause game
- **Unit 60:** Game over screen - final score

### Units 61-64: Release
- **Unit 61:** Instructions display
- **Unit 62:** Control options - key mapping
- **Unit 63:** Balance testing - speed curve
- **Unit 64:** Release build - final iNES ROM

**Phase Goal:** Complete puzzle game.

---

## Summary

**Gridlock** teaches puzzle game fundamentals:

**Phase 1 (Grid):** Play field, tetrominoes, movement.

**Phase 2 (Mechanics):** Rotation, landing, line clearing.

**Phase 3 (Features):** Preview, ghost, controls.

**Phase 4 (Levels):** Difficulty, presentation.

### Skills Transferred Forward

1. **Piece rotation** → Rotating objects
2. **Grid manipulation** → Puzzle games
3. **Line detection** → Pattern matching
4. **Preview systems** → Showing upcoming
5. **Lock delay** → Timing windows

### Game Specifications

- **Play Field:** 10×20 cells
- **Pieces:** 7 standard tetrominoes
- **Rotations:** 4 states per piece
- **Scoring:** 40/100/300/1200 for 1/2/3/4 lines
- **Levels:** 10+ with increasing speed
- **Preview:** 1 next piece
- **Ghost:** Optional
- **Mapper:** NROM
- **ROM Size:** 16KB PRG + 8KB CHR
- **Controls:** D-pad + A/B (rotate)
- **Audio:** APU effects
- **Distribution:** iNES ROM file
