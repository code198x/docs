# Game 04: Block Breaker

**Track:** Spectrum BASIC
**Genre:** Breakout
**Units:** 8
**BASIC Version:** Sinclair BASIC

---

## Overview

Classic brick-breaking game using Spectrum's attribute system for colourful bricks.

### What You Build

- Paddle control
- Bouncing ball
- Coloured brick array
- Score and lives
- Level progression

---

## Unit Breakdown

### Unit 1: Playfield
**Concepts:** Border, play area

### Unit 2: Bricks
**Concepts:** PRINT AT, INK colours, brick array

### Unit 3: The Paddle
**Concepts:** Movement, INKEY$

### Unit 4: The Ball
**Concepts:** Position, velocity

### Unit 5: Ball Physics
**Concepts:** Bouncing, angle changes

### Unit 6: Brick Collision
**Concepts:** SCREEN$ or ATTR detection

### Unit 7: Scoring
**Concepts:** Points, lives, game over

### Unit 8: Levels
**Concepts:** Brick patterns, difficulty

---

## Attribute System

```basic
100 REM DRAW COLOURED BRICKS
110 FOR row = 2 TO 6
120   INK row
130   FOR col = 1 TO 30
140     PRINT AT row,col;"█"
150   NEXT col
160 NEXT row

200 REM CHECK BRICK HIT
210 LET c$ = SCREEN$(by,bx)
220 IF c$ = "█" THEN GO SUB 500
```

---

## Skills Learned

- INK/PAPER attributes
- SCREEN$ function
- Ball physics
- Array management
- Attribute clash awareness
