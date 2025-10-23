# Lesson 005: High Score Hall

**Arc:** Knowledge Base
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 35 lines of code

## Learning Objectives

- Use arrays to store multiple values
- Implement simple sorting algorithm
- Create a persistent high score table
- Combine numeric and string arrays for structured data

## Prerequisites

**From Previous Lessons:**
- String variables (L4)
- Scoring system (L3)
- Loops and conditionals (L1-3)

**BASIC Knowledge:**
- Variables, strings, IF/THEN, loops
- Basic program structure

## Key Concepts Introduced

### Arrays
Arrays store multiple values under one name: `DIM N$(5)` creates 5 string slots: N$(1) through N$(5). Arrays are perfect for lists like high scores.

### DIM Statement
`DIM` allocates array space. Must come before using the array. `DIM N$(5),S(5)` creates two arrays: one for names, one for scores.

### Sorting Algorithm
Bubble sort compares adjacent values and swaps them if out of order. Repeat until sorted. Simple but effective for small lists.

## Code Pattern

```basic
10 DIM N$(5),S(5)
20 REM Input new score
30 INPUT "NAME";N$
40 INPUT "SCORE";SC
50 REM Find insertion point
60 FOR I=1 TO 5
70 IF SC>S(I) THEN 100
80 NEXT I
90 GOTO 200
100 REM Insert and shift down
110 FOR J=5 TO I+1 STEP -1
120 N$(J)=N$(J-1):S(J)=S(J-1)
130 NEXT J
140 N$(I)=N$:S(I)=SC
```

## Hardware Interaction

**Chips Involved:**
- None - pure BASIC data structures

**Memory Addresses:**
- None yet

## Common Pitfalls

1. **Array index errors:** Arrays start at 1 (or 0), not random numbers. Stay within DIM bounds.
2. **Forgetting DIM:** Must DIM arrays before using them
3. **Off-by-one errors:** FOR loop to 5 but array only has 4 slots = crash
4. **Parallel arrays:** N$(I) and S(I) must stay synchronized (same player)

## Extension Ideas

- Expand to top 10 instead of top 5
- Add date/time of score
- Save high scores to disk (preview of L44)
- Show ranking change ("You're #3!")
- Add score categories (difficulty levels)

## Builds Toward

**In This Tier:**
- L6: DATA statements use array principles
- L14: Game integrates high score tracking

**In Next Tier:**
- Arrays for sprite positions (8 sprites = 8 array slots)
- Enemy data arrays for AI patterns
- Level data arrays

## Quick Reference

**Array Operations:**
- `DIM A(N)` - Create numeric array of N elements
- `DIM A$(N)` - Create string array of N elements
- `A(I)` - Access element I
- Arrays start at index 0 unless using 1-based

**Sorting Pattern (Bubble Sort):**
```basic
100 FOR I=1 TO N-1
110 FOR J=I+1 TO N
120 IF A(J)>A(I) THEN SWAP
130 NEXT J
140 NEXT I
```

**Parallel Arrays:**
```basic
DIM N$(5),S(5)  :REM Names and Scores
N$(1)="ALICE":S(1)=100
N$(2)="BOB":S(2)=85
```
