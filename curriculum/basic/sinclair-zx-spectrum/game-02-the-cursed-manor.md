# Game 02: The Cursed Manor

**Track:** Spectrum BASIC
**Genre:** Text Adventure
**Units:** 16
**BASIC Version:** Sinclair BASIC

---

## Overview

Complete text adventure - hugely popular genre on the Spectrum. Games like The Hobbit proved text adventures could be commercial successes.

### What You Build

- 10-room haunted mansion
- Inventory system (6 items)
- Two-word parser
- Puzzles (locked door, dark room)
- Atmospheric descriptions

---

## Unit Breakdown

### Phase 1: World (Units 1-4)
1. Room descriptions with DATA
2. Room connections
3. Movement commands
4. Game loop with status

### Phase 2: Items (Units 5-8)
5. Item placement
6. GET command
7. DROP command
8. Inventory display

### Phase 3: Parser (Units 9-12)
9. Two-word parser
10. Verb handling (GO SUB)
11. EXAMINE command
12. Utility commands

### Phase 4: Puzzles (Units 13-16)
13. Locked door puzzle
14. Dark room (need candle)
15. Victory condition
16. Complete testing

---

## Key Code

```basic
100 REM PARSE INPUT
110 INPUT "> ";c$
120 LET sp = 0
130 FOR i = 1 TO LEN c$
140   IF c$(i) = " " THEN LET sp = i
150 NEXT i
160 LET v$ = c$(1 TO sp-1)
170 LET n$ = c$(sp+1 TO )
```

---

## Skills Learned

- DIM for arrays
- DATA/READ/RESTORE
- String slicing (Spectrum style)
- GO SUB/RETURN
- Complex game state
