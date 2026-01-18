# Game 06: Starfire

**Track:** Spectrum BASIC
**Genre:** Space Shooter
**Units:** 8
**BASIC Version:** Sinclair BASIC

---

## Overview

Space shooter introducing User Defined Graphics (UDGs) for custom sprites.

### What You Build

- Player ship (UDG)
- Enemy waves (UDGs)
- Shooting mechanics
- Collision detection
- Wave progression
- Score system

---

## Unit Breakdown

### Unit 1: User Defined Graphics
**Concepts:** USR, POKE, character design

### Unit 2: Player Ship
**Concepts:** UDG display, movement

### Unit 3: Shooting
**Concepts:** Bullet character, movement

### Unit 4: Enemies
**Concepts:** Enemy UDGs, positioning

### Unit 5: Enemy Movement
**Concepts:** Wave patterns, descent

### Unit 6: Collision
**Concepts:** Hit detection, explosions

### Unit 7: Waves
**Concepts:** Level progression, speed

### Unit 8: Complete Game
**Concepts:** Title screen, polish

---

## User Defined Graphics

```basic
10 REM DEFINE PLAYER SHIP
20 FOR n = 0 TO 7
30   READ a
40   POKE USR "a"+n, a
50 NEXT n
60 DATA 24,60,126,255,255,90,36,102

100 REM DISPLAY UDG
110 PRINT AT 20,px; CHR$ 144

200 REM DEFINE ENEMY
210 FOR n = 0 TO 7
220   READ a
230   POKE USR "b"+n, a
240 NEXT n
250 DATA 60,126,219,255,255,90,102,36
```

---

## Skills Learned

- UDG definition
- USR function
- Multiple UDGs
- Wave-based design
- Collision detection
