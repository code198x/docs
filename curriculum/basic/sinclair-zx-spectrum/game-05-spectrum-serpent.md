# Game 05: Spectrum Serpent

**Track:** Spectrum BASIC
**Genre:** Snake
**Units:** 8
**BASIC Version:** Sinclair BASIC

---

## Overview

Classic Snake game. Spectrum BASIC is fast enough for smooth character-based gameplay.

### What You Build

- Growing snake
- Food collection
- Self-collision
- Wall collision
- Increasing speed
- High score

---

## Unit Breakdown

### Unit 1: Drawing the Snake
**Concepts:** PRINT AT, snake head

### Unit 2: Movement
**Concepts:** Direction, position update

### Unit 3: Keyboard Control
**Concepts:** INKEY$, direction change

### Unit 4: The Body
**Concepts:** Array for body segments

### Unit 5: Food and Growth
**Concepts:** Random food, length increase

### Unit 6: Collision
**Concepts:** Wall and self detection

### Unit 7: Speed Control
**Concepts:** PAUSE, difficulty curve

### Unit 8: Complete Game
**Concepts:** Score, lives, polish

---

## Snake Body Array

```basic
100 DIM sx(100): DIM sy(100)
110 LET length = 3
120 LET head = 3

200 REM MOVE SNAKE
210 LET head = head + 1
220 IF head > 100 THEN LET head = 1
230 LET sx(head) = x
240 LET sy(head) = y

300 REM ERASE TAIL
310 LET tail = head - length
320 IF tail < 1 THEN LET tail = tail + 100
330 PRINT AT sy(tail),sx(tail);" "
```

---

## Skills Learned

- Circular array buffer
- PRINT AT for graphics
- Real-time input
- Speed management
- Collision detection
