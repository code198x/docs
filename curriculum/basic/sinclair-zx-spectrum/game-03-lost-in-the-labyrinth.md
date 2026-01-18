# Game 03: Lost in the Labyrinth

**Track:** Spectrum BASIC
**Genre:** Maze Game
**Units:** 8
**BASIC Version:** Sinclair BASIC

---

## Overview

Navigate a maze to find the exit. Introduction to Spectrum's built-in graphics commands.

### What You Build

- Generated or designed maze
- Player movement
- Wall collision using ATTR
- Exit goal
- Timer challenge

---

## Unit Breakdown

### Unit 1: Drawing with PLOT/DRAW
**Concepts:** PLOT, DRAW, coordinates

### Unit 2: Maze Layout
**Concepts:** Drawing walls, maze design

### Unit 3: The Player
**Concepts:** PRINT AT, character display

### Unit 4: Movement
**Concepts:** INKEY$, position update

### Unit 5: Collision with ATTR
**Concepts:** ATTR function, colour detection

### Unit 6: The Exit
**Concepts:** Goal detection, winning

### Unit 7: Timer
**Concepts:** Frames counter, time pressure

### Unit 8: Multiple Mazes
**Concepts:** Level data, progression

---

## Spectrum Graphics

```basic
100 REM DRAW MAZE WALL
110 PLOT 10,10
120 DRAW 100,0
130 DRAW 0,80
140 DRAW -100,0
150 DRAW 0,-80

200 REM CHECK COLLISION
210 LET a = ATTR(py,px)
220 IF a = 1 THEN REM HIT WALL
```

---

## Skills Learned

- PLOT and DRAW commands
- PRINT AT positioning
- INKEY$ for input
- ATTR for collision
- Spectrum coordinate system
