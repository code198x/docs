# Pattern Match: 64-Unit Outline

**Game:** 7 - Pattern Match
**Platform:** Sinclair ZX Spectrum
**Language:** Sinclair BASIC
**Units:** 64 (4 phases)
**Prerequisite:** Asteroid Dodge complete
**Concept:** Memory/puzzle game with UDG tiles. Turn-based matching pairs.

---

## Overview

Pattern Match is a card-matching memory game where players flip tiles to find matching symbol pairs. This turn-based game demonstrates that Sinclair BASIC can create polished, enjoyable games when not fighting against real-time constraints. Full UDG capabilities create distinctive tile designs.

---

## Learning Goals

By completing Pattern Match, learners will:

- Create a complete UDG character set
- Implement two-dimensional arrays
- Build game state management
- Design turn-based mechanics
- Create match detection logic
- Use the FRAMES timer
- Implement two-player competitive mode
- Polish presentation and feedback

---

## Phase 1: UDG Tile Set (Units 1-16)
*Creating tile graphics.*

### Units 1-4: UDG Planning
- **Unit 1:** Full UDG set planning - 21 characters
- **Unit 2:** Tile back design - face down
- **Unit 3:** Symbol designs - 8+ patterns
- **Unit 4:** Border/frame design

### Units 5-8: UDG Implementation
- **Unit 5:** Bulk UDG definition - DATA blocks
- **Unit 6:** UDG loading routine
- **Unit 7:** All symbols defined
- **Unit 8:** Verification display

### Units 9-12: Tile Display
- **Unit 9:** Single tile drawing - multiple characters
- **Unit 10:** Tile positioning on grid
- **Unit 11:** Face up vs face down display
- **Unit 12:** Coloured tiles

### Units 13-16: Grid Layout
- **Unit 13:** 4×4 grid layout - 16 tiles
- **Unit 14:** Grid drawing routine
- **Unit 15:** All tiles face down
- **Unit 16:** Phase 1 complete - tile grid displayed

**Phase Goal:** Custom tile graphics on screen.

---

## Phase 2: Game Logic (Units 17-32)
*Flipping and matching.*

### Units 17-20: Two-Dimensional Arrays
- **Unit 17:** 2D array declaration - DIM t(4,4)
- **Unit 18:** Row and column indexing
- **Unit 19:** Tile values array - which symbol
- **Unit 20:** Tile state array - face up/down

### Units 21-24: Board Setup
- **Unit 21:** Pair generation - two of each symbol
- **Unit 22:** Shuffle algorithm
- **Unit 23:** Board initialisation
- **Unit 24:** Hidden symbols ready

### Units 25-28: Tile Selection
- **Unit 25:** Cursor for selection
- **Unit 26:** Cursor movement - Q/A/O/P
- **Unit 27:** Select tile - spacebar
- **Unit 28:** Flip tile animation

### Units 29-32: Two-Tile Selection
- **Unit 29:** First tile remembered
- **Unit 30:** Second tile selected
- **Unit 31:** Both tiles visible
- **Unit 32:** Phase 2 complete - tiles can be flipped

**Phase Goal:** Interactive tile flipping system.

---

## Phase 3: Match Detection (Units 33-48)
*Finding pairs.*

### Units 33-36: Match Logic
- **Unit 33:** Compare two flipped tiles
- **Unit 34:** Match found - tiles stay up
- **Unit 35:** No match - flip back
- **Unit 36:** Delay for memorisation

### Units 37-40: Progress Tracking
- **Unit 37:** Pairs found counter
- **Unit 38:** Moves taken counter
- **Unit 39:** All pairs found - victory
- **Unit 40:** Victory celebration

### Units 41-44: Timer System
- **Unit 41:** FRAMES variable - PEEK(23672)
- **Unit 42:** Start time recording
- **Unit 43:** Elapsed time calculation
- **Unit 44:** Time display

### Units 45-48: Scoring
- **Unit 45:** Score based on moves and time
- **Unit 46:** Star rating system
- **Unit 47:** Score display
- **Unit 48:** Phase 3 complete - complete game

**Phase Goal:** Full single-player match game.

---

## Phase 4: Two-Player and Polish (Units 49-64)
*Multiplayer and presentation.*

### Units 49-52: Two-Player Mode
- **Unit 49:** Player turn tracking
- **Unit 50:** Turn indicator
- **Unit 51:** Player scores
- **Unit 52:** Winner determination

### Units 53-56: Turn Rules
- **Unit 53:** Match = extra turn
- **Unit 54:** Miss = opponent's turn
- **Unit 55:** Competitive scoring
- **Unit 56:** Two-player balance

### Units 57-60: Visual Polish
- **Unit 57:** Title screen with UDG art
- **Unit 58:** BEEP for flip, match, miss
- **Unit 59:** Colour scheme
- **Unit 60:** Smooth transitions

### Units 61-64: Final Game
- **Unit 61:** Mode selection - 1P or 2P
- **Unit 62:** Grid size options - 4×4 or 6×4
- **Unit 63:** Instructions screen
- **Unit 64:** **RELEASE: Pattern Match complete**

**Phase Goal:** Polished puzzle game with multiplayer.

---

## Summary

**Pattern Match** showcases BASIC's strengths:

### Technical Specifications

- **Display:** Character mode with full UDGs
- **Grid:** 4×4 (8 pairs) or 6×4 (12 pairs)
- **UDGs:** 21 characters defined
- **Players:** 1-2
- **Timer:** FRAMES system variable
- **Features:** Scoring, ratings, two-player

### Skills Learned

- Complete UDG character set creation
- Two-dimensional array usage
- Game state management
- Turn-based game design
- Match detection algorithms
- FRAMES timer usage
- Two-player implementation
- Polish and presentation

### FRAMES Timer

```basic
10 LET start = PEEK 23672 + 256 * PEEK 23673
...
100 LET now = PEEK 23672 + 256 * PEEK 23673
110 LET elapsed = now - start
120 LET seconds = INT(elapsed / 50)
```

### When BASIC Works Well

- Turn-based - no real-time pressure
- Logic-focused - matching pairs
- UDG showcase - custom graphics shine
- Polish time - attention to detail

### Progression

This game prepares learners for **Platform Jump** - the final BASIC game that attempts real-time platforming to show exactly why Z80 assembly is needed.
