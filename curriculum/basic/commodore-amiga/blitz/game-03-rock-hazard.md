# Game 03: Rock Hazard

**Track:** Blitz Basic
**Genre:** Asteroids
**Units:** 8
**BASIC Version:** Blitz Basic 2

---

## Overview

Asteroids clone with rotation, thrust physics, and asteroid splitting.

### What You Build

- Rotating ship
- Thrust physics
- Screen wrapping
- Asteroid splitting
- Bullet system
- Lives and scoring

---

## Unit Breakdown

### Unit 1: Ship Rotation
**Concepts:** Angle, Sin/Cos tables

### Unit 2: Thrust Physics
**Concepts:** Velocity, acceleration

### Unit 3: Screen Wrapping
**Concepts:** Edge detection, teleport

### Unit 4: Bullets
**Concepts:** Projectile array

### Unit 5: Asteroids
**Concepts:** Object management

### Unit 6: Collision
**Concepts:** Distance checking

### Unit 7: Splitting
**Concepts:** Large → Medium → Small

### Unit 8: Complete Game
**Concepts:** Waves, scoring

---

## Rotation and Thrust

```blitz
; PRECOMPUTED SIN/COS TABLES
DEFTYPE .w
Dim sine.q(360)
Dim cosine.q(360)

For a = 0 To 359
  sine(a) = Sin(a * Pi / 180)
  cosine(a) = Cos(a * Pi / 180)
Next a

; SHIP PHYSICS
angle.w = 0
vx.q = 0 : vy.q = 0
thrust.q = 0.2

; THRUST
If Joyb(1) & 1  ; Fire button
  vx = vx + cosine(angle) * thrust
  vy = vy + sine(angle) * thrust
End If

; MOVEMENT
x.q = x + vx
y.q = y + vy

; FRICTION
vx = vx * 0.99
vy = vy * 0.99
```

---

## Skills Learned

- Trigonometry tables
- Vector physics
- Object splitting
- Screen wrapping
- Projectile management
