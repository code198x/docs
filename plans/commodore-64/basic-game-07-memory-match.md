# Memory Match: 64-Unit Outline

**Game:** 7 - Memory Match
**Platform:** Commodore 64
**Language:** BASIC V2
**Units:** 64 (4 phases)
**Prerequisite:** Space Dodge complete
**Concept:** Card matching puzzle game with custom characters. Turn-based gameplay that works well in BASIC.

---

## Overview

Memory Match is a card-matching puzzle game where players flip cards to find matching pairs. This turn-based game demonstrates that BASIC can create polished experiences when not fighting against real-time constraints. Custom characters create distinct card designs.

---

## Learning Goals

By completing Memory Match, learners will:

- Create custom character definitions
- Implement two-dimensional arrays
- Build game state management
- Design turn-based mechanics
- Create match detection logic
- Implement move counting
- Build two-player mode
- Polish presentation and feedback

---

## Phase 1: Custom Characters (Units 1-16)
*Creating card graphics.*

### Units 1-4: Character Memory
- **Unit 1:** Character set location - where characters live
- **Unit 2:** POKE 53272 - character set pointer
- **Unit 3:** Character RAM - where to store custom
- **Unit 4:** Copying ROM to RAM

### Units 5-8: Character Definition
- **Unit 5:** 8×8 pixel grid - character structure
- **Unit 6:** Binary to decimal - calculating bytes
- **Unit 7:** DATA for character shapes
- **Unit 8:** POKEing character data

### Units 9-12: Card Characters
- **Unit 9:** Card back design - face down
- **Unit 10:** Card symbols - 8 different patterns
- **Unit 11:** Border characters - card frame
- **Unit 12:** Character set complete

### Units 13-16: Card Display
- **Unit 13:** Drawing a single card
- **Unit 14:** Multi-character card (2×2 or 2×3)
- **Unit 15:** Card grid layout - 4×4 grid
- **Unit 16:** Phase 1 complete - cards display correctly

**Phase Goal:** Custom character cards on screen.

---

## Phase 2: Game Board and Logic (Units 17-32)
*Setting up the match game.*

### Units 17-20: Two-Dimensional Arrays
- **Unit 17:** 2D array declaration - DIM(4,4)
- **Unit 18:** Row and column indexing
- **Unit 19:** Card values array - which symbol
- **Unit 20:** Card state array - face up/down

### Units 21-24: Board Setup
- **Unit 21:** Pair generation - two of each symbol
- **Unit 22:** Shuffle algorithm - randomise positions
- **Unit 23:** Board initialisation
- **Unit 24:** All cards face down

### Units 25-28: Card Selection
- **Unit 25:** Cursor position - which card
- **Unit 26:** Cursor movement - arrow keys
- **Unit 27:** Card flip input - spacebar/return
- **Unit 28:** Flip animation - card turns over

### Units 29-32: Selection Tracking
- **Unit 29:** First card selection
- **Unit 30:** Second card selection
- **Unit 31:** Both cards visible
- **Unit 32:** Phase 2 complete - cards can be flipped

**Phase Goal:** Interactive card flipping system.

---

## Phase 3: Match Detection and Scoring (Units 33-48)
*Finding pairs.*

### Units 33-36: Match Logic
- **Unit 33:** Compare two flipped cards
- **Unit 34:** Match found - cards stay up
- **Unit 35:** No match - flip both back
- **Unit 36:** Delay before flip back - memorisation

### Units 37-40: Progress Tracking
- **Unit 37:** Pairs found counter
- **Unit 38:** Moves taken counter
- **Unit 39:** All pairs found - win condition
- **Unit 40:** Victory celebration

### Units 41-44: Scoring
- **Unit 41:** Score calculation - fewer moves = better
- **Unit 42:** Par score - target moves
- **Unit 43:** Star rating - 3 stars, 2 stars, 1 star
- **Unit 44:** Score display - moves and rating

### Units 45-48: Game Flow
- **Unit 45:** New game option
- **Unit 46:** Different board sizes - 4×4, 6×4
- **Unit 47:** Difficulty selection
- **Unit 48:** Phase 3 complete - complete match game

**Phase Goal:** Full single-player match game.

---

## Phase 4: Two-Player and Polish (Units 49-64)
*Multiplayer and presentation.*

### Units 49-52: Two-Player Mode
- **Unit 49:** Player turn tracking
- **Unit 50:** Turn indicator display
- **Unit 51:** Player score arrays
- **Unit 52:** Winner determination

### Units 53-56: Turn Rules
- **Unit 53:** Match = extra turn
- **Unit 54:** Miss = opponent's turn
- **Unit 55:** Score per match - not moves
- **Unit 56:** Competitive balance

### Units 57-60: Polish
- **Unit 57:** Title screen - custom graphics
- **Unit 58:** Sound effects - flip, match, miss
- **Unit 59:** Colour schemes - card colours
- **Unit 60:** Smooth animations

### Units 61-64: Final Game
- **Unit 61:** Mode selection - 1P or 2P
- **Unit 62:** Full testing both modes
- **Unit 63:** Instructions screen
- **Unit 64:** **RELEASE: Memory Match complete**

**Phase Goal:** Polished puzzle game with multiplayer.

---

## Summary

**Memory Match** shows BASIC's strengths:

### Technical Specifications

- **Display:** Custom character mode
- **Grid sizes:** 4×4 (8 pairs), 6×4 (12 pairs)
- **Characters:** 8 custom symbols + card back
- **Players:** 1-2
- **Input:** Turn-based cursor control
- **Features:** Score, rating, two-player

### Skills Learned

- Custom character creation
- Character memory manipulation
- Two-dimensional array usage
- Game state management
- Turn-based game design
- Match detection logic
- Two-player implementation
- Polish and presentation

### Character Definition Example

```basic
100 REM HEART SYMBOL
110 DATA 0, 102, 255, 255, 255, 126, 60, 24
120 FOR I = 0 TO 7
130 READ V: POKE 12288 + I, V
140 NEXT
```

### BASIC Strengths Demonstrated

This game shows BASIC works well when:
- **Turn-based** - no real-time pressure
- **Limited animation** - cards flip, nothing else moves
- **Logic-focused** - matching pairs, not physics
- **Polish matters** - time for nice presentation

### Progression

This game prepares learners for **Platform Peril** - the final BASIC game that pushes real-time action to show exactly why assembly language is needed.
