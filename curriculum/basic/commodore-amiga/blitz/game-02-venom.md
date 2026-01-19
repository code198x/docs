# Game 02: Venom

**Track:** Blitz Basic
**Genre:** Snake
**Units:** 8
**BASIC Version:** Blitz Basic 2

---

## Overview

Fast Snake implementation showcasing Blitz's speed advantage over interpreted BASICs.

### What You Build

- Smooth snake movement
- Growth mechanics
- Speed progression
- High score system
- Clean game loop

---

## Unit Breakdown

### Unit 1: Blitz Shapes
**Concepts:** LoadShapes, Blit

### Unit 2: Snake Head
**Concepts:** Position, movement

### Unit 3: Direction Control
**Concepts:** Joyx(), Joyy()

### Unit 4: Snake Body
**Concepts:** Queue data structure

### Unit 5: Food System
**Concepts:** Spawning, collision

### Unit 6: Growth
**Concepts:** Length management

### Unit 7: Collision
**Concepts:** Self/wall detection

### Unit 8: Speed and Score
**Concepts:** Difficulty curve

---

## Queue-Based Snake

```blitz
; SNAKE BODY AS QUEUE
DEFTYPE .w

MaxLen = 100
Dim snakeX.w(MaxLen)
Dim snakeY.w(MaxLen)
head.w = 0
tail.w = 0
length.w = 3

Statement AddSegment{x.w, y.w}
  head = (head + 1) Mod MaxLen
  snakeX(head) = x
  snakeY(head) = y
End Statement

Statement RemoveTail{}
  If length < (head - tail + MaxLen) Mod MaxLen
    tail = (tail + 1) Mod MaxLen
  End If
End Statement
```

---

## Skills Learned

- Blitz shapes system
- Queue data structures
- Fast game loops
- Joystick input
- Speed management
