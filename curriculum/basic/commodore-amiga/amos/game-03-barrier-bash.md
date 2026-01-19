# Game 03: Barrier Bash

**Track:** AMOS
**Genre:** Breakout
**Units:** 8
**BASIC Version:** AMOS Professional

---

## Overview

Classic Breakout with AMOS's powerful sprite and bob collision.

### What You Build

- Paddle control (mouse/joystick)
- Ball physics
- Brick array (bobs)
- Bob collision detection
- Power-ups
- Multiple levels

---

## Unit Breakdown

### Unit 1: Playfield Setup
**Concepts:** Screen, borders

### Unit 2: The Paddle
**Concepts:** Sprite, mouse/joy control

### Unit 3: The Ball
**Concepts:** Bob, velocity, movement

### Unit 4: Bouncing
**Concepts:** Wall reflection, angles

### Unit 5: Brick Layout
**Concepts:** Bob array, positioning

### Unit 6: Collision
**Concepts:** Bob Col(), brick destruction

### Unit 7: Power-ups
**Concepts:** Special bricks, effects

### Unit 8: Levels
**Concepts:** Patterns, progression

---

## AMOS Collision

```basic
' BOB COLLISION
Double Buffer
Do
  Bob Clear

  ' Move ball
  Add BX,DX : Add BY,DY
  Bob 1,BX,BY,1

  ' Check collision with bricks (bobs 10-50)
  C=Bob Col(1,10 To 50)
  If C>0
    ' Hit brick C
    Bob Off C
    DY=-DY
    Inc SCORE
  End If

  Bob Draw
  Wait Vbl
Loop
```

---

## Skills Learned

- Bob Col() function
- Multiple bob management
- Ball physics
- Power-up systems
- Level design
