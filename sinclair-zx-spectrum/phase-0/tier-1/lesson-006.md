# Lesson 006: Fact Finder

**Arc:** Knowledge Base
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis (Complete Game)
**Estimated Completion:** 50 lines of code

## Learning Objectives

- Use arrays (DIM) to store multiple related values
- Create searchable knowledge database
- Complete quiz game with categories and scoring
- Master DATA, READ, and array interaction

## Prerequisites

**From Previous Lessons:**
- L4: READ, DATA
- L5: RESTORE, menu systems

**BASIC Knowledge:**
- DATA management and program structure

## Key Concepts Introduced

### Arrays (DIM)
Arrays are numbered lists of variables. Use `DIM q$(10)` to create 10 string variables: q$(1) through q$(10).

### Indexed Access
Access array elements by number: `q$(1)`, `q$(2)`, etc. Use loops with counters to process all elements.

### Loading Arrays from DATA
Read DATA into arrays for flexible data manipulation and search capabilities.

### Search Algorithms
Loop through array comparing each element to find matches.

## Code Pattern

```basic
10 DIM q$(20),a$(20)
20 LET count=0
30 READ q$,a$
40 IF q$="END" THEN GO TO 100
50 LET count=count+1
60 LET q$(count)=q$
70 LET a$(count)=a$
80 GO TO 30
100 REM Quiz using arrays
110 FOR i=1 TO count
120 PRINT q$(i)
130 NEXT i
200 DATA "Question 1","Answer 1"
210 DATA "Question 2","Answer 2"
220 DATA "END","END"
```

## Hardware Interaction

**Chips Involved:**
- Z80 CPU (array index calculation)
- RAM (array storage - ~2KB available typically)

**Memory:**
- Arrays stored in variable memory
- Each string array element can hold ~255 characters

## Common Pitfalls

1. **Forgetting DIM:** Must declare arrays before using them
2. **Off-by-one errors:** Arrays start at index 1 (or use base 0 with DIM)
3. **Array too small:** DIM must be large enough for all data
4. **Wrong subscript:** `q(i)` for numbers, `q$(i)` for strings

## Extension Ideas

- Add search by keyword
- Create multiple categories with separate arrays
- Sort questions by difficulty
- Random question order (using RND and arrays)
- Allow user to add new questions

## Builds Toward

**In This Tier:**
- L12-14: Arrays for sprite positions in games
- L15-16: Arrays for game state management

**In Next Tier:**
- 2D arrays for game maps (DIM map(20,20))
- Dynamic data structures

## Quick Reference

**Essential Commands:**
- `DIM variable(size)` - Create array
- `variable(index)` - Access array element
- `FOR i=1 TO n` - Loop through array

**Array Rules:**
- Must DIM before use
- Default: indices start at 1
- Can use 0-based: `DIM(0 TO 10)` gives 11 elements
- Strings: `DIM name$(100)`
- Numbers: `DIM score(100)`

**Loading Pattern:**
```basic
10 DIM item$(50)
20 FOR i=1 TO 50
30 READ item$(i)
40 NEXT i
```

**Search Pattern:**
```basic
10 FOR i=1 TO count
20 IF item$(i)=search$ THEN PRINT "Found at ";i
30 NEXT i
```

---

**Version:** 1.0
**Created:** 2025-10-24
**Status:** Lesson specification complete
