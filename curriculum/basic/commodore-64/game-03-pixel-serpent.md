# Game 03: Pixel Serpent

**Track:** C64 BASIC
**Genre:** Snake
**Units:** 8
**BASIC Version:** Stock BASIC V2 with PEEK/POKE

---

## Overview

Classic Snake game using character graphics. First introduction to screen memory and real-time input.

### What You Build

- Character-based snake
- Food collection and growth
- Wall and self-collision
- Increasing speed
- Score display

---

## Unit Breakdown

### Unit 1: Screen Memory
**Concepts:** Screen at 1024, POKE characters

### Unit 2: Drawing the Snake
**Concepts:** Head position, drawing characters

### Unit 3: Movement
**Concepts:** Direction variables, position updates

### Unit 4: Keyboard Input
**Concepts:** PEEK(197), real-time input

### Unit 5: Food and Growth
**Concepts:** Random food, snake length array

### Unit 6: Collision Detection
**Concepts:** PEEK screen memory, wall checks

### Unit 7: Game Loop Timing
**Concepts:** FOR/NEXT delays, speed increase

### Unit 8: Polish
**Concepts:** Score, lives, game over

---

## Key Techniques

```basic
100 REM SCREEN MEMORY
110 S = 1024: REM SCREEN START
120 POKE S + Y*40 + X, 81: REM DRAW BLOCK

200 REM KEYBOARD READ
210 K = PEEK(197)
220 IF K = 17 THEN DY = -1: DX = 0: REM UP
230 IF K = 41 THEN DY = 1: DX = 0: REM DOWN
```

---

## Skills Learned

- PEEK and POKE
- Screen memory (1024-2023)
- Real-time keyboard input
- Game loop structure
- Collision detection
