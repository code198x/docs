# Game 04: Wall Smasher

**Track:** C64 BASIC
**Genre:** Breakout
**Units:** 8
**BASIC Version:** Stock BASIC V2

---

## Overview

Classic brick-breaking game using character graphics and PEEK/POKE - exactly like magazine type-ins.

### What You Build

- Paddle (PETSCII character)
- Bouncing ball (character)
- Breakable bricks (coloured characters)
- Score display

---

## Unit Breakdown

### Unit 1: Screen Setup
**Concepts:** Clear screen, border/background colours, drawing the playfield

### Unit 2: The Paddle
**Concepts:** PRINT AT position, joystick reading with PEEK(56320)

### Unit 3: The Ball
**Concepts:** Character position, velocity variables

### Unit 4: Ball Physics
**Concepts:** Bouncing off walls, direction reversal

### Unit 5: Brick Layout
**Concepts:** Drawing bricks with colour, brick array

### Unit 6: Collision Detection
**Concepts:** PEEK screen memory, detecting what ball hit

### Unit 7: Scoring
**Concepts:** Points, lives, game over

### Unit 8: Polish
**Concepts:** Sound (POKE SID), title screen

---

## Key Techniques

### Joystick Reading
```basic
100 J=PEEK(56320): REM READ JOYSTICK PORT 2
110 IF (J AND 4)=0 THEN PX=PX-1: REM LEFT
120 IF (J AND 8)=0 THEN PX=PX+1: REM RIGHT
```

### Ball Movement
```basic
200 REM MOVE BALL
210 BX=BX+DX: BY=BY+DY
220 REM WALL BOUNCE
230 IF BX<1 OR BX>38 THEN DX=-DX
240 IF BY<1 THEN DY=-DY
```

### Collision Detection
```basic
300 REM CHECK WHAT BALL HIT
310 C=PEEK(1024+BY*40+BX)
320 IF C=160 THEN GOSUB 500: REM HIT BRICK
330 IF C=32 THEN 400: REM EMPTY SPACE
340 DY=-DY: REM BOUNCE
```

---

## Skills Learned

- Joystick input (PEEK(56320))
- Character-based collision
- Ball physics with characters
- PETSCII graphics
- Screen memory direct access
