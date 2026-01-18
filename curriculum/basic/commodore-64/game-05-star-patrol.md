# Game 05: Star Patrol

**Track:** C64 BASIC
**Genre:** Fixed Shooter
**Units:** 8
**BASIC Version:** Stock BASIC V2

---

## Overview

Space shooter using custom character graphics. Introduces redefining the character set via POKE.

### What You Build

- Player ship (custom character)
- Enemy waves (custom characters)
- Shooting (character movement)
- Lives system

---

## Unit Breakdown

### Unit 1: Custom Character Setup
**Concepts:** Copying ROM to RAM, character memory location

### Unit 2: Designing Characters
**Concepts:** 8x8 grid, DATA statements, POKEing character data

### Unit 3: Player Ship
**Concepts:** Display custom character, movement

### Unit 4: Shooting
**Concepts:** Bullet character, vertical movement

### Unit 5: Enemies
**Concepts:** Enemy characters, positioning

### Unit 6: Enemy Movement
**Concepts:** Wave patterns, descent

### Unit 7: Collision
**Concepts:** PEEK for hit detection

### Unit 8: Complete Game
**Concepts:** Scoring, lives, waves

---

## Custom Character Setup

```basic
100 REM COPY CHARACTER ROM TO RAM
110 POKE 56334,0: REM TURN OFF INTERRUPTS
120 POKE 1,51: REM SWITCH IN CHARACTER ROM
130 FOR I=0 TO 2047
140   POKE 12288+I,PEEK(53248+I)
150 NEXT I
160 POKE 1,55: REM SWITCH OUT ROM
170 POKE 56334,1: REM RESTORE INTERRUPTS
180 POKE 53272,(PEEK(53272)AND240)+12: REM POINT TO NEW SET
```

### Defining a Ship Character

```basic
200 REM DEFINE CHARACTER 128 AS SHIP
210 FOR I=0 TO 7: READ D
220   POKE 12288+128*8+I,D
230 NEXT I
240 DATA 24,60,126,255,255,90,36,102
```

### Display Custom Character

```basic
300 PRINT CHR$(128);: REM SHOW SHIP
```

---

## Skills Learned

- Character set copying
- Custom character design
- Character memory manipulation
- PETSCII codes above 127
- Wave-based game design
