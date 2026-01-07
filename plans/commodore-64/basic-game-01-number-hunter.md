# Number Hunter: 64-Unit Outline

**Game:** 1 - Number Hunter
**Platform:** Commodore 64
**Language:** BASIC V2
**Units:** 64 (4 phases)
**Prerequisite:** None
**Concept:** Number guessing game with scoring. First introduction to C64 BASIC programming.

---

## Overview

Number Hunter is a text-based guessing game that introduces learners to the C64 BASIC environment. The computer picks a secret number, and the player must guess it with hints guiding them. Simple mechanics allow focus on fundamental programming concepts.

---

## Learning Goals

By completing Number Hunter, learners will:

- Navigate the C64 BASIC environment
- Understand program mode vs direct mode
- Use variables and basic data types
- Implement input/output with INPUT and PRINT
- Create conditional logic with IF/THEN
- Build loops with FOR/NEXT and GOTO
- Generate random numbers with RND
- Structure a complete game loop

---

## Phase 1: BASIC Environment (Units 1-16)
*First steps in C64 BASIC.*

### Units 1-4: Getting Started
- **Unit 1:** The C64 screen - direct mode, cursor, typing commands
- **Unit 2:** PRINT statement - displaying text
- **Unit 3:** Program mode - line numbers, LIST, RUN
- **Unit 4:** Editing programs - modifying, deleting lines

### Units 5-8: Variables and Data
- **Unit 5:** Numeric variables - LET, assignment
- **Unit 6:** String variables - text storage
- **Unit 7:** INPUT statement - getting user data
- **Unit 8:** Combining PRINT and INPUT

### Units 9-12: Program Flow
- **Unit 9:** GOTO - unconditional jumps
- **Unit 10:** IF/THEN - conditional execution
- **Unit 11:** Comparison operators - =, <, >, <>
- **Unit 12:** Combining conditions

### Units 13-16: First Program
- **Unit 13:** Simple guessing loop - fixed number
- **Unit 14:** Too high/too low hints
- **Unit 15:** Win condition - correct guess
- **Unit 16:** Phase 1 complete - basic guesser working

**Phase Goal:** Working guess-the-number with fixed target.

---

## Phase 2: Random Numbers and Counting (Units 17-32)
*Adding unpredictability and tracking.*

### Units 17-20: Random Numbers
- **Unit 17:** RND function - generating randomness
- **Unit 18:** INT function - whole numbers
- **Unit 19:** Range control - numbers between 1 and 100
- **Unit 20:** Random target number - unpredictable games

### Units 21-24: Counting Guesses
- **Unit 21:** Counter variable - tracking attempts
- **Unit 22:** Incrementing counter - each guess
- **Unit 23:** Displaying guess count
- **Unit 24:** Guess limit - maximum attempts

### Units 25-28: FOR/NEXT Loops
- **Unit 25:** FOR/NEXT basics - counted loops
- **Unit 26:** STEP parameter - different increments
- **Unit 27:** Nested loops - loops within loops
- **Unit 28:** Using loops for delays

### Units 29-32: Game Structure
- **Unit 29:** Game initialisation - setup phase
- **Unit 30:** Main game loop - structured flow
- **Unit 31:** Game over conditions - win and lose
- **Unit 32:** Phase 2 complete - random game with limits

**Phase Goal:** Random number guessing with attempt counter.

---

## Phase 3: Scoring and Polish (Units 33-48)
*Making it a proper game.*

### Units 33-36: Scoring System
- **Unit 33:** Score calculation - fewer guesses = higher score
- **Unit 34:** High score tracking - best performance
- **Unit 35:** Score display - formatted output
- **Unit 36:** Score persistence - during session

### Units 37-40: Screen Management
- **Unit 37:** Clearing screen - CHR$(147)
- **Unit 38:** Cursor positioning - TAB function
- **Unit 39:** Text formatting - centering, spacing
- **Unit 40:** Title screen - game presentation

### Units 41-44: User Experience
- **Unit 41:** Input validation - handling bad input
- **Unit 42:** Error messages - helpful feedback
- **Unit 43:** Range display - showing valid guesses
- **Unit 44:** Guess history - showing previous attempts

### Units 45-48: Play Again
- **Unit 45:** Play again prompt - Y/N choice
- **Unit 46:** Game reset - reinitialising variables
- **Unit 47:** Running total - cumulative score
- **Unit 48:** Phase 3 complete - polished game experience

**Phase Goal:** Complete game with scoring and replay.

---

## Phase 4: Advanced Features (Units 49-64)
*Extra features and BASIC techniques.*

### Units 49-52: Difficulty Levels
- **Unit 49:** Difficulty menu - easy, medium, hard
- **Unit 50:** Range adjustment - 1-50, 1-100, 1-200
- **Unit 51:** Attempt adjustment - more or fewer guesses
- **Unit 52:** Score multiplier - harder = more points

### Units 53-56: GOSUB Subroutines
- **Unit 53:** GOSUB/RETURN - subroutine concept
- **Unit 54:** Organising code - routines for tasks
- **Unit 55:** Title screen subroutine
- **Unit 56:** Score display subroutine

### Units 57-60: Data Statements
- **Unit 57:** DATA statement - storing values
- **Unit 58:** READ statement - retrieving data
- **Unit 59:** RESTORE - re-reading data
- **Unit 60:** Messages in DATA - congratulations, hints

### Units 61-64: Final Game
- **Unit 61:** Code organisation - clean structure
- **Unit 62:** Final testing - all features working
- **Unit 63:** Documentation - REM statements
- **Unit 64:** **RELEASE: Number Hunter complete**

**Phase Goal:** Feature-complete first BASIC game.

---

## Summary

**Number Hunter** establishes core BASIC programming skills:

### Technical Specifications

- **Display:** Text mode (40×25)
- **Input:** Keyboard (INPUT statement)
- **Variables:** Numeric and string
- **Control flow:** IF/THEN, FOR/NEXT, GOTO, GOSUB
- **Functions:** RND, INT, CHR$

### Skills Learned

- C64 BASIC environment navigation
- Variable declaration and use
- Input/output operations
- Conditional logic and loops
- Random number generation
- Subroutine organisation
- Game loop structure

### Progression

This game prepares learners for **Cosmic Drift** where they'll move beyond text to character-based graphics using POKE to screen memory.
