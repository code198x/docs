# Lesson 019: Character-Based Maps

**Arc:** UDG Graphics System
**Position:** Lesson 3 of 5 in arc
**Type:** Standard
**Estimated Completion:** 70 lines of code

## Learning Objectives
- Store game maps in strings or arrays
- Render maps using UDG characters
- Implement scrolling or screen transitions
- Create multi-screen game worlds

## Prerequisites
- UDG basics (L17)
- Tile sets (L18)
- PRINT AT positioning (L1-3)

## Key Concepts
**String-Based Maps** - Compact storage using CHR$ codes
**Array Maps** - 2D arrays for larger worlds with editing
**Screen Rendering** - Draw entire screen from map data
**Map Scrolling** - Redraw portions as player moves

## Code Pattern
```basic
10 REM String map (small, compact)
20 LET map$=""
30 FOR y=0 TO 21
40   FOR x=0 TO 31
50     IF x=0 OR x=31 OR y=0 OR y=21 THEN LET t$=CHR$ 145: REM Wall
60     IF NOT (x=0 OR x=31 OR y=0 OR y=21) THEN LET t$=CHR$ 144: REM Empty
70     LET map$=map$+t$
80   NEXT x
90 NEXT y
100 REM Draw map
110 FOR y=0 TO 21
120   FOR x=0 TO 31
130     LET i=y*32+x+1
140     PRINT AT y,x;map$(i)
150   NEXT x
160 NEXT y
```

## Hardware
**Memory:**
- 32×22 screen = 704 bytes
- String map: 704 bytes + overhead
- Array map: 704 bytes (more flexibility)

**Performance:**
- Full screen redraw: ~200ms (acceptable for room transitions)
- Partial redraw: ~50ms (smooth enough for slow scrolling)

## Quick Reference
- String access: `map$(position)` (1-based)
- Array access: `map(x,y)` (0-based)
- Screen: 32 columns × 22 rows
- Position formula: `y*32+x+1` (string), `y*32+x` (array)

---

**Version:** 1.0
**Created:** 2025-10-27
