# Game 05: Star Patrol

**Track:** C64 BASIC
**Genre:** Fixed Shooter
**Units:** 8
**BASIC Version:** Simons' BASIC

---

## Overview

Space Invaders-style fixed shooter. Multiple sprites, shooting mechanics, and wave-based gameplay.

### What You Build

- Player ship (sprite)
- Enemy formation
- Shooting mechanics
- Collision detection
- Wave system
- Lives and scoring

---

## Unit Breakdown

### Unit 1: Starfield Background
**Concepts:** PLOT points, scrolling effect

### Unit 2: Player Ship
**Concepts:** Sprite definition, movement

### Unit 3: Player Shooting
**Concepts:** Bullet sprite, firing logic

### Unit 4: Enemy Formation
**Concepts:** Multiple sprites, arrays

### Unit 5: Enemy Movement
**Concepts:** Wave patterns, direction changes

### Unit 6: Collision Detection
**Concepts:** SPRITEBOB COL, hit detection

### Unit 7: Scoring and Lives
**Concepts:** Score display, game state

### Unit 8: Waves and Difficulty
**Concepts:** Level progression, speed increase

---

## Multiple Sprite Handling

```basic
100 REM SETUP ENEMIES
110 FOR I = 1 TO 5
120   SPRITE I+1,1,2,0,0: REM RED ENEMIES
130   MOB SET I+1, I*50, 50
140 NEXT I

200 REM MOVE ALL ENEMIES
210 FOR I = 1 TO 5
220   X = X SPRITE(I+1)
230   MOB SET I+1, X+DX, Y SPRITE(I+1)
240 NEXT I
```

---

## Skills Learned

- Multiple sprite management
- Arrays for game objects
- Bullet mechanics
- Wave-based design
- Sprite collision
