# Game 07: Speed Circuit

**Track:** C64 BASIC
**Genre:** Top-Down Racing
**Units:** 8
**BASIC Version:** Simons' BASIC

---

## Overview

Top-down racing game with custom character graphics for the track. Lap timing and obstacles.

### What You Build

- Car sprite with rotation
- Custom character track
- Lap counting system
- Timer display
- Track collision
- Best time tracking

---

## Unit Breakdown

### Unit 1: Custom Characters
**Concepts:** Character redefinition, track tiles

### Unit 2: Track Layout
**Concepts:** Screen layout, track design

### Unit 3: The Car
**Concepts:** Sprite, 8-direction movement

### Unit 4: Car Physics
**Concepts:** Acceleration, friction, turning

### Unit 5: Track Collision
**Concepts:** Character detection, slowdown

### Unit 6: Lap System
**Concepts:** Checkpoint detection, lap counting

### Unit 7: Timer
**Concepts:** TI variable, time display

### Unit 8: Polish
**Concepts:** Best times, game complete

---

## Custom Characters

```basic
100 REM REDEFINE CHARACTERS FOR TRACK
110 POKE 56334,0: REM DISABLE INTERRUPTS
120 POKE 1,51: REM SWITCH TO RAM
130 FOR I = 0 TO 7
140   READ D: POKE 12288 + 8*128 + I, D
150 NEXT I
160 DATA 255,129,129,129,129,129,129,255
170 POKE 1,55: POKE 56334,1
180 POKE 53272, (PEEK(53272) AND 240) OR 12
```

---

## Skills Learned

- Custom character graphics
- 8-direction movement
- Simple car physics
- Lap/checkpoint systems
- Timer implementation
