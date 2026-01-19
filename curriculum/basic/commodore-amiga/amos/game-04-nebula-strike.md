# Game 04: Nebula Strike

**Track:** AMOS
**Genre:** Vertical Shooter
**Units:** 8
**BASIC Version:** AMOS Professional

---

## Overview

Vertical scrolling shooter with hardware scrolling and wave-based enemies.

### What You Build

- Scrolling starfield
- Player ship
- Shooting mechanics
- Enemy waves
- Collision and explosions
- Boss battles

---

## Unit Breakdown

### Unit 1: Starfield
**Concepts:** Screen scrolling, layers

### Unit 2: Player Ship
**Concepts:** Sprite, 8-way movement

### Unit 3: Shooting
**Concepts:** Bullet sprites, firing rate

### Unit 4: Enemies
**Concepts:** Wave spawning, patterns

### Unit 5: Enemy AI
**Concepts:** Movement patterns, diving

### Unit 6: Collision
**Concepts:** Spritebob Col, explosions

### Unit 7: Power-ups
**Concepts:** Weapon upgrades, shields

### Unit 8: Boss Battle
**Concepts:** Boss patterns, health bars

---

## Hardware Scrolling

```basic
' PARALLAX STARFIELD
Screen Open 0,320,256,8,Lowres
Screen Open 1,320,512,4,Lowres  ' Double height for scroll

' Draw stars on screen 1
Screen 1
For I=1 To 100
  Plot Rnd(319),Rnd(511),Rnd(3)+1
Next I

' Scroll loop
Screen 0
Do
  Screen Offset 1,0,SCROLLY
  Add SCROLLY,2
  If SCROLLY>255 Then SCROLLY=0
  Wait Vbl
Loop
```

---

## Skills Learned

- Hardware scrolling
- Sprite management
- Bullet systems
- Wave spawning
- Boss design
