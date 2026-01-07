# Ink War: 64-Unit Outline

**Game:** 1 of 16
**Platform:** ZX Spectrum
**Units:** 64 (4 phases)
**Concept:** Territory control game where the attribute system *is* the gameplay. Player vs AI, taking turns to claim 8×8 attribute cells. Control the majority to win.

---

## Why This Game First?

The attribute system is what made Spectrum games look distinctly Spectrum. Unlike the C64's hardware sprites or the Amiga's bitplanes, the Spectrum's 8×8 attribute cells created both its limitations (colour clash) and its visual identity.

Ink War makes the attribute system the core mechanic rather than fighting against it:
- Each cell is a territory to claim
- Colours represent ownership
- The constraint becomes the game

By the end of this game, learners will deeply understand how the Spectrum's display works - knowledge that informs every subsequent game.

---

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Screen memory layout | 1 | The Spectrum's unusual screen organisation |
| Attribute memory | 1 | INK, PAPER, BRIGHT, FLASH control |
| Z80 fundamentals | 1 | LD, ADD, SUB, JP, CALL basics |
| Keyboard input | 2 | Reading keys via ROM and ports |
| Game state management | 2 | Tracking board, turns, scores |
| Simple AI | 3 | Decision-making for computer opponent |
| ROM routines | 1-2 | Using built-in Spectrum routines |
| Beeper sound | 3 | Basic sound effects |
| Title screen | 4 | Game presentation |

---

## Phase 1: Display Foundation (Units 1-16)
*Understanding the Spectrum's unique screen system.*

### Units 1-4: Screen Memory
- **Unit 1:** The Spectrum's display - 256×192 pixels, how it maps to memory
- **Unit 2:** Screen memory layout - the interleaved addressing ($4000-$57FF)
- **Unit 3:** Calculating screen addresses - the formula for any Y coordinate
- **Unit 4:** Drawing pixels - setting individual bits in screen memory

### Units 5-8: Attribute System
- **Unit 5:** Attribute memory location ($5800-$5AFF)
- **Unit 6:** Attribute byte structure - INK (3 bits), PAPER (3 bits), BRIGHT, FLASH
- **Unit 7:** Setting attributes - colour an 8×8 cell
- **Unit 8:** The 32×24 attribute grid - mapping cells to addresses

### Units 9-12: Z80 Basics
- **Unit 9:** Z80 registers - A, BC, DE, HL, IX, IY, SP, PC
- **Unit 10:** Load and store - LD instructions
- **Unit 11:** Arithmetic - ADD, SUB, INC, DEC
- **Unit 12:** Jumps and calls - JP, JR, CALL, RET

### Units 13-16: First Display
- **Unit 13:** Clear screen routine - filling screen and attributes
- **Unit 14:** Draw the game board - 8×8 grid of attribute cells visible
- **Unit 15:** Colour the board - initial neutral colours
- **Unit 16:** Display test - all attributes working, board visible

**Phase Goal:** Understand screen/attribute memory and display an 8×8 game board.

---

## Phase 2: Game Mechanics (Units 17-32)
*Input, turns, and core gameplay.*

### Units 17-20: Keyboard Input
- **Unit 17:** ROM keyboard routine - using RST $38 and system variables
- **Unit 18:** Direct port reading - keyboard half-rows
- **Unit 19:** Cursor movement - navigate the board with keys
- **Unit 20:** Cursor display - highlight current cell

### Units 21-24: Turn System
- **Unit 21:** Game state structure - board array, current player, scores
- **Unit 22:** Turn logic - alternating between players
- **Unit 23:** Cell claiming - change attribute to player's colour
- **Unit 24:** Move validation - can only claim adjacent or neutral cells

### Units 25-28: Scoring and Win Condition
- **Unit 25:** Score calculation - count cells per player
- **Unit 26:** Score display - show current territory count
- **Unit 27:** Win detection - majority control or board full
- **Unit 28:** Game over display - winner announcement

### Units 29-32: Two-Player Mode
- **Unit 29:** Player 1 controls - one set of keys
- **Unit 30:** Player 2 controls - different key set
- **Unit 31:** Turn indicator - whose turn is it
- **Unit 32:** Complete two-player game - playable hot-seat mode

**Phase Goal:** Playable two-player territory control game.

---

## Phase 3: AI and Polish (Units 33-48)
*Computer opponent and game feel.*

### Units 33-36: Simple AI Framework
- **Unit 33:** AI decision structure - evaluate, choose, act
- **Unit 34:** Valid move detection - find all legal moves
- **Unit 35:** Random move selection - simple random AI
- **Unit 36:** AI vs human mode - single-player option

### Units 37-40: Smarter AI
- **Unit 37:** Territory evaluation - value of each cell
- **Unit 38:** Greedy strategy - take highest-value available cell
- **Unit 39:** Edge and corner preference - strategic positions
- **Unit 40:** Difficulty levels - random vs greedy vs strategic

### Units 41-44: Sound and Feedback
- **Unit 41:** Beeper basics - OUT to port $FE
- **Unit 42:** Move sound - audio feedback on cell claim
- **Unit 43:** Win/lose sounds - distinct audio for outcomes
- **Unit 44:** Turn change sound - indicate player switch

### Units 45-48: Visual Polish
- **Unit 45:** Cell claim animation - flash effect on capture
- **Unit 46:** Cursor animation - pulsing or blinking highlight
- **Unit 47:** Score display formatting - clean number display
- **Unit 48:** Board border - visual frame around play area

**Phase Goal:** Single-player mode with AI opponent and polished feedback.

---

## Phase 4: Presentation and Mastery (Units 49-64)
*Complete game with menus and options.*

### Units 49-52: Title Screen
- **Unit 49:** Title design - game logo using attributes
- **Unit 50:** Title display routine - show title screen
- **Unit 51:** Menu options - 1P vs AI, 2P, difficulty
- **Unit 52:** Menu navigation and selection

### Units 53-56: Game Options
- **Unit 53:** Board size options - 6×6, 8×8, 10×10
- **Unit 54:** Starting positions - different initial layouts
- **Unit 55:** Time limit option - timed turns
- **Unit 56:** Settings persistence - remember choices

### Units 57-60: Advanced Features
- **Unit 57:** Special cells - power-up positions on board
- **Unit 58:** Chain captures - claiming triggers adjacent claims
- **Unit 59:** Undo move - take back last move option
- **Unit 60:** Match mode - best of 3/5 games

### Units 61-64: Release
- **Unit 61:** Instructions screen - how to play
- **Unit 62:** Bug fixing and edge cases
- **Unit 63:** Final balance - AI difficulty tuning
- **Unit 64:** Release build - complete TAP file

**Phase Goal:** Complete, polished game ready for distribution.

---

## Summary

**Ink War** teaches the Spectrum's defining characteristic - the attribute system - by making it the core game mechanic:

**Phase 1 (Display):** Screen memory, attribute bytes, Z80 basics - understand how the Spectrum draws.

**Phase 2 (Gameplay):** Input, turns, claiming cells - the game mechanics work.

**Phase 3 (AI):** Computer opponent, sound, polish - single-player is engaging.

**Phase 4 (Presentation):** Menus, options, release - professional presentation.

### Skills Transferred Forward

The following skills debut in Ink War and will be applied in every subsequent game:

1. **Screen memory layout** → All graphics in all games
2. **Attribute understanding** → Colour clash management throughout
3. **Z80 fundamentals** → Every subsequent game
4. **Keyboard input** → Player control in all games
5. **Game state management** → All game logic
6. **ROM routine usage** → Common Spectrum patterns
7. **Simple AI** → Enemy behaviour in later games
8. **Beeper sound** → Audio throughout curriculum

### Why Attributes First?

Unlike the C64 curriculum which starts with the SID (audio), the Spectrum curriculum starts with attributes (visuals) because:

1. **No equivalent audio hook** - The beeper is limited; the attribute system is unique
2. **Visual platform identity** - Colour clash defines the Spectrum look
3. **Constraint as feature** - Ink War turns the limitation into gameplay
4. **Foundation for everything** - Every game must manage attributes

### Game Specifications

- **Board:** 8×8 grid (64 cells) with size options
- **Players:** 1 (vs AI) or 2 (hot-seat)
- **AI Difficulty:** 3 levels (random, greedy, strategic)
- **Controls:** Keyboard (cursor keys + fire)
- **Win Condition:** Control majority when board is full
- **Features:** Chain captures, special cells, match mode
- **Audio:** Beeper sound effects
- **Distribution:** TAP file
