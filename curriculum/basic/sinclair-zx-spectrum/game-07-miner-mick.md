# Game 07: Miner Mick

**Track:** Spectrum BASIC
**Genre:** Platformer
**Units:** 8
**BASIC Version:** Sinclair BASIC

---

## Overview

Single-screen platformer - homage to Manic Miner, which defined Spectrum gaming.

### What You Build

- Jumping character
- Platform collision
- Collectible items
- Hazards/enemies
- Level completion
- Multiple caverns

---

## Unit Breakdown

### Unit 1: Level Display
**Concepts:** Platform layout, UDGs

### Unit 2: The Miner
**Concepts:** Character display, position

### Unit 3: Movement
**Concepts:** Left/right, animation

### Unit 4: Gravity
**Concepts:** Falling, floor detection

### Unit 5: Jumping
**Concepts:** Jump arc, landing

### Unit 6: Collectibles
**Concepts:** Items, score, level complete

### Unit 7: Hazards
**Concepts:** Enemies, death, lives

### Unit 8: Multiple Levels
**Concepts:** Level data, progression

---

## Platform Detection

```basic
100 REM CHECK BELOW PLAYER
110 LET below$ = SCREEN$(py+1,px)
120 IF below$ = " " THEN LET falling = 1
130 IF below$ = "=" THEN LET falling = 0

200 REM JUMPING
210 IF falling = 0 AND jump = 1 THEN
220   LET vy = -3
230   LET falling = 1
240 END IF
```

---

## Historical Context

Manic Miner (1983) was written in assembly, but BASIC platformers were common in magazines. This captures the essence while being achievable in BASIC.

---

## Skills Learned

- Gravity physics
- Platform collision
- Level design
- UDGs for graphics
- Game state management
