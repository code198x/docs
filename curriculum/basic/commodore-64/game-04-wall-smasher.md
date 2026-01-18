# Game 04: Wall Smasher

**Track:** C64 BASIC
**Genre:** Breakout
**Units:** 8
**BASIC Version:** Simons' BASIC

---

## Overview

Classic brick-breaking game. **First Simons' BASIC game** - introduces graphics and sprite commands.

### What You Build

- Paddle with joystick/keyboard control
- Bouncing ball with physics
- Destructible brick array
- Score and lives
- Level completion

---

## Unit Breakdown

### Unit 1: Simons' BASIC Setup
**Concepts:** Loading Simons' BASIC, HIRES mode

### Unit 2: Drawing the Playfield
**Concepts:** LINE, BOX, brick layout

### Unit 3: The Ball
**Concepts:** SPRITE commands, movement

### Unit 4: Ball Physics
**Concepts:** Direction, bouncing, angles

### Unit 5: The Paddle
**Concepts:** JOY() function, paddle control

### Unit 6: Brick Collision
**Concepts:** Collision detection, brick array

### Unit 7: Scoring System
**Concepts:** Points, lives, game over

### Unit 8: Levels and Polish
**Concepts:** Level progression, difficulty

---

## Simons' BASIC Introduction

```basic
10 HIRES 0,1: REM BLACK BG, WHITE FG
20 LINE 0,0,319,0,1: REM DRAW LINE
30 BOX 10,10,50,30,1: REM DRAW BOX
40 CIRCLE 160,100,20,1: REM DRAW CIRCLE
50 SPRITE 1,1,15,0,0: REM ENABLE SPRITE
60 MOB SET 1,160,100: REM POSITION SPRITE
```

---

## Skills Learned

- Simons' BASIC commands
- HIRES graphics mode
- Sprite handling (MOB)
- JOY() for joystick
- Ball physics
