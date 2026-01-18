# Game 06: Jump Quest

**Track:** C64 BASIC
**Genre:** Platformer
**Units:** 8
**BASIC Version:** Simons' BASIC

---

## Overview

Single-screen platformer with jumping, platforms, and collectibles. Introduction to gravity physics.

### What You Build

- Jumping character
- Platform collision
- Gravity simulation
- Collectible items
- Level completion
- Multiple levels

---

## Unit Breakdown

### Unit 1: The Character
**Concepts:** Player sprite, basic movement

### Unit 2: Gravity
**Concepts:** Falling, velocity, acceleration

### Unit 3: Jumping
**Concepts:** Jump velocity, arc physics

### Unit 4: Platforms
**Concepts:** Platform data, drawing

### Unit 5: Platform Collision
**Concepts:** Landing detection, standing

### Unit 6: Collectibles
**Concepts:** Items, collision, score

### Unit 7: Level Design
**Concepts:** DATA for levels, level loading

### Unit 8: Complete Game
**Concepts:** Multiple levels, win condition

---

## Gravity Physics

```basic
100 REM GRAVITY CONSTANTS
110 GR = 0.5: REM GRAVITY
120 JP = -8: REM JUMP POWER

200 REM APPLY GRAVITY
210 VY = VY + GR: REM ACCELERATE
220 Y = Y + VY: REM MOVE
230 IF Y > FLOOR THEN Y = FLOOR: VY = 0

300 REM JUMP
310 IF FIRE AND GROUNDED THEN VY = JP
```

---

## Skills Learned

- Gravity simulation
- Jump physics
- Platform collision
- Level data structures
- Game state (grounded/airborne)
