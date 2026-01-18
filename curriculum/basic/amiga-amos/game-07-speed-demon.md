# Game 07: Speed Demon

**Track:** AMOS
**Genre:** Top-Down Racing
**Units:** 8
**BASIC Version:** AMOS Professional

---

## Overview

Top-down racing with car physics, AI opponents, and lap timing.

### What You Build

- Scrolling track
- Car physics (acceleration, friction, drift)
- AI racers
- Lap system
- Split times
- Championship mode

---

## Unit Breakdown

### Unit 1: Track Display
**Concepts:** Dual playfield, track tiles

### Unit 2: Car Control
**Concepts:** Rotation, acceleration

### Unit 3: Car Physics
**Concepts:** Velocity, friction, drift

### Unit 4: Track Collision
**Concepts:** Grass slowdown, barriers

### Unit 5: Checkpoints
**Concepts:** Lap detection, timing

### Unit 6: AI Racers
**Concepts:** Waypoints, AI driving

### Unit 7: Race Structure
**Concepts:** Countdown, positions

### Unit 8: Championship
**Concepts:** Multiple tracks, points

---

## Car Physics

```basic
' TOP-DOWN CAR PHYSICS
Procedure CARPHYSICS
  ' Acceleration
  If Jup(1) Then Add SPEED#,ACCEL#
  If Jdown(1) Then Add SPEED#,-BRAKE#

  ' Friction
  SPEED#=SPEED#*FRICTION#

  ' Rotation
  If Jleft(1) Then Add ANGLE#,-TURNSPEED#
  If Jright(1) Then Add ANGLE#,TURNSPEED#

  ' Movement
  VX#=SPEED#*Cos(ANGLE#)
  VY#=SPEED#*Sin(ANGLE#)
  Add PX#,VX# : Add PY#,VY#

  ' Track check
  TILE=GETTILE(PX#,PY#)
  If TILE=GRASS Then SPEED#=SPEED#*0.8
End Proc
```

---

## Skills Learned

- Top-down car physics
- Angle-based movement
- AI waypoints
- Lap/checkpoint systems
- Race structure
