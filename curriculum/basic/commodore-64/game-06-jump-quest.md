# Game 06: Jump Quest

**Track:** C64 BASIC
**Genre:** Platformer
**Units:** 8
**BASIC Version:** Stock BASIC V2

---

## Overview

Single-screen platformer using character graphics. Teaches gravity and platform collision.

### What You Build

- Jumping character
- Platforms (characters)
- Collectibles
- Level completion

---

## Unit Breakdown

### Unit 1: Level Display
**Concepts:** Drawing platforms with characters, DATA for level

### Unit 2: The Player
**Concepts:** Player character, position variables

### Unit 3: Movement
**Concepts:** Left/right, keyboard reading

### Unit 4: Gravity
**Concepts:** Falling, velocity, floor detection

### Unit 5: Jumping
**Concepts:** Jump velocity, grounded state

### Unit 6: Platform Collision
**Concepts:** PEEK below player, landing

### Unit 7: Collectibles
**Concepts:** Items, PEEK to collect, scoring

### Unit 8: Complete Game
**Concepts:** Lives, level complete, multiple levels

---

## Gravity and Jumping

```basic
100 REM GRAVITY SYSTEM
110 REM CHECK IF ON PLATFORM
120 BELOW=PEEK(1024+(PY+1)*40+PX)
130 IF BELOW=160 OR BELOW=96 THEN GROUNDED=1: VY=0: GOTO 200
140 GROUNDED=0
150 REM APPLY GRAVITY
160 VY=VY+1: IF VY>3 THEN VY=3
170 PY=PY+VY

200 REM JUMPING
210 K=PEEK(197): REM CHECK KEYBOARD
220 IF K=60 AND GROUNDED=1 THEN VY=-3: REM SPACE TO JUMP
```

### Platform Characters

```basic
300 REM PLATFORM = CHR$(160) (SOLID BLOCK)
310 REM LADDER = CHR$(96)
320 REM COIN = CHR$(87)
```

---

## Skills Learned

- Integer gravity physics
- Grounded state tracking
- PEEK for collision detection
- Level data in DATA statements
- Simple animation
