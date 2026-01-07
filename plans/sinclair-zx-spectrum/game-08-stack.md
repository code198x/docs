# Stack: 64-Unit Outline

**Game:** 8 of 16
**Platform:** ZX Spectrum
**Units:** 64 (4 phases)
**Concept:** Falling blocks puzzle game. Rotate and place tetrominoes, clear lines, survive increasing speed.

---

## Why This Game Eighth?

Stack introduces piece rotation and line clearing - puzzle game fundamentals:

1. **Piece rotation** - Rotating shapes around a centre
2. **Collision with rotated pieces** - Complex shape testing
3. **Line clearing** - Detecting and removing complete rows
4. **Falling mechanics** - Gravity on pieces vs placed blocks
5. **Preview system** - Showing next piece

This completes the foundation phase with a different genre entirely.

---

## Skills Applied from Previous Games

| Skill | From | Application in Stack |
|-------|------|---------------------|
| Grid-based display | Slither | Play field grid |
| Frame timing | All | Drop speed control |
| Input handling | All | Rotation, movement |
| Score tracking | All | Points for lines |
| Game state | All | Level progression |
| Collision detection | All | Piece placement |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Piece rotation | 1 | Rotating shapes mathematically |
| Rotation collision | 2 | Testing rotated piece fits |
| Wall kicks | 2 | Adjusting position when rotation blocked |
| Line detection | 2 | Finding complete rows |
| Line clearing | 2 | Removing and collapsing rows |
| Ghost piece | 3 | Preview drop position |
| Next piece preview | 3 | Showing upcoming piece |
| Soft/hard drop | 3 | Fast placement options |

---

## Phase 1: Pieces and Grid (Units 1-16)
*Tetromino display and basic movement.*

### Units 1-4: Play Field
- **Unit 1:** Grid data structure - 10×20 play area
- **Unit 2:** Grid display - drawing the well
- **Unit 3:** Cell states - empty, filled, piece colours
- **Unit 4:** Grid borders - walls and floor

### Units 5-8: Tetromino Data
- **Unit 5:** Piece shapes - 7 standard tetrominoes (I, O, T, S, Z, J, L)
- **Unit 6:** Piece storage - 4×4 grid per piece
- **Unit 7:** Rotation states - 4 rotations per piece (except O)
- **Unit 8:** Piece colours - distinct colour per piece type

### Units 9-12: Piece Display
- **Unit 9:** Current piece tracking - type, rotation, position
- **Unit 10:** Piece rendering - draw piece at position
- **Unit 11:** Piece on grid - combine piece with field
- **Unit 12:** Piece colours on grid - correct attributes

### Units 13-16: Basic Movement
- **Unit 13:** Left/right input - horizontal movement
- **Unit 14:** Movement collision - stop at walls
- **Unit 15:** Piece in bounds - position validation
- **Unit 16:** Playable foundation - piece moves in well

**Phase Goal:** Display tetromino that moves left/right in play field.

---

## Phase 2: Rotation and Placement (Units 17-32)
*Piece rotation, landing, and line clearing.*

### Units 17-20: Piece Rotation
- **Unit 17:** Rotation input - clockwise/anticlockwise
- **Unit 18:** Rotation state change - cycle through states
- **Unit 19:** Rotation collision - check rotated piece fits
- **Unit 20:** Wall kicks - adjust position for blocked rotation

### Units 21-24: Piece Falling
- **Unit 21:** Gravity timer - piece drops over time
- **Unit 22:** Downward collision - stop at floor and blocks
- **Unit 23:** Piece locking - piece becomes part of grid
- **Unit 24:** New piece spawn - next piece appears at top

### Units 25-28: Line Clearing
- **Unit 25:** Line detection - check each row for completeness
- **Unit 26:** Single line clear - remove complete row
- **Unit 27:** Row collapse - move rows down after clear
- **Unit 28:** Multi-line clear - detect 2, 3, 4 lines

### Units 29-32: Game Rules
- **Unit 29:** Game over detection - piece blocked at spawn
- **Unit 30:** Score calculation - points per lines cleared
- **Unit 31:** Line counter - total lines cleared
- **Unit 32:** Complete game loop - playable Tetris

**Phase Goal:** Full piece mechanics with rotation and line clearing.

---

## Phase 3: Polish and Features (Units 33-48)
*Preview, ghost piece, and enhanced controls.*

### Units 33-36: Next Piece Preview
- **Unit 33:** Piece queue - generate next piece in advance
- **Unit 34:** Preview display area - side panel
- **Unit 35:** Preview rendering - show next piece
- **Unit 36:** Queue management - advance queue on spawn

### Units 37-40: Ghost Piece
- **Unit 37:** Ghost calculation - where piece would land
- **Unit 38:** Ghost display - translucent/outline piece
- **Unit 39:** Ghost updating - recalculate on movement
- **Unit 40:** Ghost toggle - option to show/hide

### Units 41-44: Advanced Controls
- **Unit 41:** Soft drop - hold down for faster fall
- **Unit 42:** Hard drop - instant placement
- **Unit 43:** Delayed auto-shift - hold left/right for repeat
- **Unit 44:** Lock delay - time before piece locks

### Units 45-48: Sound and Feedback
- **Unit 45:** Move sound - piece movement
- **Unit 46:** Rotate sound - rotation feedback
- **Unit 47:** Line clear sound - satisfying clear effect
- **Unit 48:** Tetris sound - 4-line clear fanfare

**Phase Goal:** Polished game with preview and advanced controls.

---

## Phase 4: Levels and Release (Units 49-64)
*Difficulty progression and presentation.*

### Units 49-52: Level System
- **Unit 49:** Level progression - advance after X lines
- **Unit 50:** Speed increase - faster drop per level
- **Unit 51:** Speed table - defined speeds per level
- **Unit 52:** Level display - show current level

### Units 53-56: Scoring Depth
- **Unit 53:** Scoring formula - more points at higher levels
- **Unit 54:** Combo scoring - consecutive line clears
- **Unit 55:** High score tracking - best scores
- **Unit 56:** Statistics display - pieces placed, time

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Level select - start at higher levels
- **Unit 59:** Pause functionality - pause game
- **Unit 60:** Game over screen - final score, high score

### Units 61-64: Release
- **Unit 61:** Instructions display
- **Unit 62:** Control customisation - key mapping
- **Unit 63:** Balance testing - speed curve tuning
- **Unit 64:** Release build - final TAP file

**Phase Goal:** Complete puzzle game with level progression.

---

## Summary

**Stack** teaches puzzle game fundamentals with piece manipulation:

**Phase 1 (Grid):** Play field, tetrominoes, basic movement.

**Phase 2 (Mechanics):** Rotation, landing, line clearing.

**Phase 3 (Polish):** Preview, ghost piece, advanced controls.

**Phase 4 (Levels):** Difficulty progression, presentation.

### Skills Transferred Forward

1. **Piece rotation** → Rotating objects in any game
2. **Grid manipulation** → Puzzle games, tile editors
3. **Line detection** → Pattern matching, row operations
4. **Preview systems** → Showing upcoming events
5. **Lock delay** → Timing windows for player actions
6. **Speed progression** → Difficulty curves

### Game Specifications

- **Play Field:** 10×20 cells
- **Pieces:** 7 standard tetrominoes
- **Rotations:** 4 states per piece (O has 1)
- **Controls:** Left, right, rotate CW, rotate CCW, soft drop, hard drop
- **Scoring:** 40/100/300/1200 for 1/2/3/4 lines (×level)
- **Levels:** 10+ levels with increasing speed
- **Preview:** 1 next piece shown
- **Ghost:** Optional drop preview
- **Audio:** Beeper effects
- **Distribution:** TAP file
