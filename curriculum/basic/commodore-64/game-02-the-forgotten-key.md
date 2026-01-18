# Game 02: The Forgotten Key

**Track:** C64 BASIC
**Genre:** Text Adventure
**Units:** 16
**BASIC Version:** Stock BASIC V2

---

## Overview

A complete text adventure with rooms, items, puzzles, and a goal. Rich tradition in gaming history.

### What You Build

- 8-10 room mansion
- Inventory system
- Locked door puzzle
- Two-word parser (VERB NOUN)
- Win/lose conditions

---

## Unit Breakdown

### Phase 1: Foundation (Units 1-4)
1. Room descriptions with DATA/READ
2. Room connections array
3. Movement commands
4. Main game loop

### Phase 2: Items (Units 5-8)
5. Item placement in rooms
6. GET command
7. DROP command
8. Inventory display

### Phase 3: Parser (Units 9-12)
9. Two-word parser (string functions)
10. Verb routing with GOSUB
11. EXAMINE command
12. HELP, QUIT commands

### Phase 4: Puzzles (Units 13-16)
13. Locked door puzzle
14. Victory condition
15. Polish and atmosphere
16. Complete testing

---

## Key Data Structures

```basic
100 DIM R$(10): REM ROOM DESCRIPTIONS
110 DIM N(10),S(10),E(10),W(10): REM EXITS
120 DIM I$(6): REM ITEM NAMES
130 DIM L(6): REM ITEM LOCATIONS
```

---

## Skills Learned

- Arrays (DIM)
- DATA/READ statements
- String functions (LEFT$, MID$, LEN)
- GOSUB/RETURN
- Complex game state
