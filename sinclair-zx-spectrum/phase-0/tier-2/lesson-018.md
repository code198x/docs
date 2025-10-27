# Lesson 018: Complete Tile Sets

**Arc:** UDG Graphics System
**Position:** Lesson 2 of 5 in arc
**Type:** Standard
**Estimated Completion:** 60 lines of code

## Learning Objectives
- Create complete tile sets (walls, floors, items)
- Organize UDG data efficiently
- Design cohesive visual style within 8×8 constraints

## Prerequisites
- UDG basics (L17)
- DATA management

## Key Concepts
**Tile Set Design** - 10-15 tiles for complete game graphics
**Visual Consistency** - Similar style across all tiles
**Optimization** - Reuse patterns, vary attributes for more variety

## Code Pattern
```basic
10 REM Define 8 tile types
20 LET base=USR "a"
30 FOR tile=0 TO 7
40   FOR row=0 TO 7
50     READ byte
60     POKE base+tile*8+row,byte
70   NEXT row
80 NEXT tile
90 DATA 0,0,0,0,0,0,0,0: REM Empty
100 DATA 255,255,255,255,255,255,255,255: REM Wall
110 DATA 170,85,170,85,170,85,170,85: REM Floor
```

## Hardware
**Memory:** 168 bytes total (21 UDGs × 8 bytes)
**Performance:** Defining tiles once, instant display

## Quick Reference
- Empty: all zeros
- Solid: all 255
- Brick: alternating patterns
- Door: partial fill
- Key/gem: centered icon

---

**Version:** 1.0
**Created:** 2025-10-27
