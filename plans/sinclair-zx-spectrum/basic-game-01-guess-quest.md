# Guess Quest: 64-Unit Outline

**Game:** 1 - Guess Quest
**Platform:** Sinclair ZX Spectrum
**Language:** Sinclair BASIC
**Units:** 64 (4 phases)
**Prerequisite:** None
**Concept:** Number guessing game with visual feedback. First introduction to Sinclair BASIC.

---

## Overview

Guess Quest is a text-based guessing game that introduces learners to the Spectrum BASIC environment. The computer picks a secret number, and the player must guess it with visual hints guiding them. Simple mechanics allow focus on fundamental programming concepts while showcasing Sinclair BASIC's built-in colour commands.

---

## Learning Goals

By completing Guess Quest, learners will:

- Navigate the Spectrum BASIC environment
- Understand program editing and RUN
- Use variables and basic data types
- Implement input/output with INPUT and PRINT
- Create conditional logic with IF/THEN/ELSE
- Build loops with FOR/NEXT and GO TO
- Generate random numbers with RND
- Use INK/PAPER for colour feedback

---

## Phase 1: BASIC Environment (Units 1-16)
*First steps in Spectrum BASIC.*

### Units 1-4: Getting Started
- **Unit 1:** The Spectrum screen - command mode, editing
- **Unit 2:** PRINT statement - displaying text
- **Unit 3:** Program editing - entering and running programs
- **Unit 4:** Line editing - modifying, deleting lines

### Units 5-8: Variables and Data
- **Unit 5:** Numeric variables - LET, assignment
- **Unit 6:** String variables - text storage
- **Unit 7:** INPUT statement - getting user data
- **Unit 8:** Combining PRINT and INPUT

### Units 9-12: Program Flow
- **Unit 9:** GO TO - unconditional jumps
- **Unit 10:** IF/THEN - conditional execution
- **Unit 11:** IF/THEN/ELSE - two branches
- **Unit 12:** Comparison operators - =, <, >, <>

### Units 13-16: First Program
- **Unit 13:** Simple guessing loop - fixed number
- **Unit 14:** Too high/too low hints
- **Unit 15:** Win condition - correct guess
- **Unit 16:** Phase 1 complete - basic guesser working

**Phase Goal:** Working guess-the-number with fixed target.

---

## Phase 2: Random Numbers and Colour (Units 17-32)
*Adding unpredictability and visual feedback.*

### Units 17-20: Random Numbers
- **Unit 17:** RND function - generating randomness
- **Unit 18:** INT function - whole numbers
- **Unit 19:** Range control - numbers between 1 and 100
- **Unit 20:** Random target number - unpredictable games

### Units 21-24: Counting and Display
- **Unit 21:** Counter variable - tracking attempts
- **Unit 22:** CLS - clearing the screen
- **Unit 23:** PRINT AT - positioning text
- **Unit 24:** Formatted display layout

### Units 25-28: Colour Introduction
- **Unit 25:** INK command - text colour
- **Unit 26:** PAPER command - background colour
- **Unit 27:** Colour feedback - red for wrong, green for right
- **Unit 28:** BORDER command - screen border

### Units 29-32: Game Structure
- **Unit 29:** Game initialisation
- **Unit 30:** Main game loop
- **Unit 31:** Win and lose conditions
- **Unit 32:** Phase 2 complete - colourful random game

**Phase Goal:** Random number guessing with colour feedback.

---

## Phase 3: Scoring and Polish (Units 33-48)
*Making it a proper game.*

### Units 33-36: Scoring System
- **Unit 33:** Score calculation - fewer guesses = higher
- **Unit 34:** High score tracking
- **Unit 35:** Score display with colour
- **Unit 36:** Score persistence during session

### Units 37-40: FOR/NEXT Loops
- **Unit 37:** FOR/NEXT basics - counted loops
- **Unit 38:** STEP parameter - different increments
- **Unit 39:** Countdown display - dramatic reveal
- **Unit 40:** Animation with loops

### Units 41-44: User Experience
- **Unit 41:** Input validation - handling bad input
- **Unit 42:** Range indicator - showing valid guesses
- **Unit 43:** Guess history display
- **Unit 44:** BEEP for audio feedback

### Units 45-48: Play Again
- **Unit 45:** Play again prompt
- **Unit 46:** Game reset
- **Unit 47:** Running total across games
- **Unit 48:** Phase 3 complete - polished game

**Phase Goal:** Complete game with scoring and replay.

---

## Phase 4: Advanced Features (Units 49-64)
*Extra features and BASIC techniques.*

### Units 49-52: Difficulty Levels
- **Unit 49:** Difficulty menu
- **Unit 50:** Range adjustment - 1-50, 1-100, 1-200
- **Unit 51:** Attempt limits per difficulty
- **Unit 52:** Score multipliers

### Units 53-56: GO SUB Subroutines
- **Unit 53:** GO SUB/RETURN - subroutine concept
- **Unit 54:** Organising code - routines for tasks
- **Unit 55:** Title screen subroutine
- **Unit 56:** Score display subroutine

### Units 57-60: Visual Polish
- **Unit 57:** Title screen design
- **Unit 58:** BRIGHT for emphasis
- **Unit 59:** FLASH for celebration
- **Unit 60:** Consistent colour scheme

### Units 61-64: Final Game
- **Unit 61:** All features integrated
- **Unit 62:** Full testing
- **Unit 63:** Documentation - REM statements
- **Unit 64:** **RELEASE: Guess Quest complete**

**Phase Goal:** Feature-complete first Sinclair BASIC game.

---

## Summary

**Guess Quest** establishes core Sinclair BASIC skills:

### Technical Specifications

- **Display:** Text mode with colour
- **Input:** Keyboard (INPUT statement)
- **Colour:** INK, PAPER, BORDER, BRIGHT, FLASH
- **Audio:** BEEP for feedback
- **Control flow:** IF/THEN/ELSE, FOR/NEXT, GO TO, GO SUB

### Skills Learned

- Spectrum BASIC environment navigation
- Variable declaration and use
- Input/output operations
- Conditional logic with ELSE
- Loop structures
- Random number generation
- Colour command usage
- Subroutine organisation

### Progression

This game prepares learners for **Pixel Rain** where they'll move beyond text to pixel graphics using the PLOT command.
