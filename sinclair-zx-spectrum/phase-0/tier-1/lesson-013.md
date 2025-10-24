# Lesson 013: Maze Runner

**Arc:** Moving Sprites
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 40 lines of code

## Learning Objectives

- Detect collisions with screen characters
- Create walls and boundaries
- Implement simple maze navigation
- Use SCREEN$ for collision detection

## Key Concepts Introduced

### SCREEN$ Function
SCREEN$ (row,col) returns the character at that screen position. Use to detect walls.

### Collision Detection
Check destination before moving. If it's a wall character, don't move.

### Maze Design
Use PRINT to draw maze walls with graphics characters or letters.

## Code Pattern

```basic
10 REM Draw maze
20 FOR x=0 TO 31: PRINT AT 0,x;"#": NEXT x
30 FOR y=0 TO 21: PRINT AT y,0;"#": PRINT AT y,31;"#": NEXT y
40 LET px=15: LET py=10
50 PRINT AT py,px;"@"
60 REM Movement with collision
70 LET nx=px: LET ny=py
80 IF INKEY$="q" THEN LET ny=ny-1
90 IF INKEY$="a" THEN LET ny=ny+1
100 IF SCREEN$(ny,nx)=" " THEN LET px=nx: LET py=ny
```

## Quick Reference

- `SCREEN$ (row,col)` - Read character at position
- Check before move: collision detection
- Use "#" or block graphics for walls
- Boundary checking prevents walking off screen

---

**Version:** 1.0
**Created:** 2025-10-24
