# Lesson 015: Enemy Chase

**Arc:** Mini Action Game
**Position:** Lesson 1 of 2 in arc
**Type:** Standard
**Estimated Completion:** 55 lines of code

## Learning Objectives

- Create AI-controlled enemy movement
- Implement simple chase behavior
- Add game over condition
- Manage multiple moving objects

## Key Concepts Introduced

### Simple AI
Enemy moves toward player each frame. Compare positions and move horizontally/vertically to close distance.

### Multiple Objects
Track player position (px,py) and enemy position (ex,ey) separately.

### Game Over
If player and enemy occupy same position, game ends.

## Code Pattern

```basic
10 LET px=5: LET py=5
20 LET ex=25: LET ey=15
30 REM Player move
40 REM ...
50 REM Enemy AI
60 IF ex<px THEN LET ex=ex+1
70 IF ex>px THEN LET ex=ex-1
80 IF ey<py THEN LET ey=ey+1
90 IF ey>py THEN LET ey=ey-1
100 IF px=ex AND py=ey THEN GOSUB 2000
```

## Quick Reference

- Separate variables for each object
- AI: Move toward player each step
- Collision: Check if positions match
- PAUSE to slow game speed

---

**Version:** 1.0
**Created:** 2025-10-24
