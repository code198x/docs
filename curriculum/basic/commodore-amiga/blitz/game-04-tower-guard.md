# Game 04: Tower Guard

**Track:** Blitz Basic
**Genre:** Tower Defence
**Units:** 8
**BASIC Version:** Blitz Basic 2

---

## Overview

Fixed-position defence game with aiming, waves of enemies, and upgrade systems.

### What You Build

- Aiming turret
- Wave spawning
- Enemy pathfinding
- Shooting mechanics
- Upgrade system
- Resource management

---

## Unit Breakdown

### Unit 1: The Tower
**Concepts:** Fixed position, drawing

### Unit 2: Aiming
**Concepts:** Mouse/joystick angle

### Unit 3: Shooting
**Concepts:** Projectiles, fire rate

### Unit 4: Enemies
**Concepts:** Spawning, movement

### Unit 5: Enemy Waves
**Concepts:** Wave structure, difficulty

### Unit 6: Collision
**Concepts:** Hit detection, damage

### Unit 7: Upgrades
**Concepts:** Fire rate, damage, range

### Unit 8: Resources
**Concepts:** Money, spending, strategy

---

## Aiming System

```blitz
; AIM AT MOUSE
DEFTYPE .w

Statement CalcAngle{tx.w, ty.w, mx.w, my.w, RETURN angle.w}
  dx.w = mx - tx
  dy.w = my - ty

  If dx = 0
    If dy < 0 Then angle = 270 Else angle = 90
  Else
    angle = ATan(dy / dx) * 180 / Pi
    If dx < 0 Then angle = angle + 180
    If angle < 0 Then angle = angle + 360
  End If
End Statement

; IN GAME LOOP
mx.w = MouseX
my.w = MouseY
CalcAngle{towerX, towerY, mx, my, aimAngle}
```

---

## Skills Learned

- Angle calculation
- Wave management
- Upgrade systems
- Resource economy
- Tower defence design
