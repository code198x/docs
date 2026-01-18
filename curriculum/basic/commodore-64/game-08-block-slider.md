# Game 08: Block Slider

**Track:** C64 BASIC
**Genre:** Sokoban Puzzle
**Units:** 16
**BASIC Version:** Stock BASIC V2

---

## Overview

Sokoban-style puzzle game - **perfect for character graphics**. Push boxes onto targets. Capstone project.

### What You Build

- Push-block mechanics
- Multiple puzzle levels
- Win detection
- Move counter
- Undo system (optional)

---

## Unit Breakdown

### Phase 1: Core (Units 1-4)

#### Unit 1: Level Display
**Concepts:** Level data in DATA, drawing with PRINT

#### Unit 2: Player Movement
**Concepts:** Joystick/keyboard, position update

#### Unit 3: Wall Collision
**Concepts:** PEEK ahead, blocking movement

#### Unit 4: Box Detection
**Concepts:** Detecting boxes, preparing for push

### Phase 2: Pushing (Units 5-8)

#### Unit 5: Push Mechanics
**Concepts:** Check two cells ahead, move box

#### Unit 6: Target Tiles
**Concepts:** Boxes on targets, visual feedback

#### Unit 7: Win Detection
**Concepts:** All boxes on targets

#### Unit 8: Move Counter
**Concepts:** Counting, display

### Phase 3: Levels (Units 9-12)

#### Unit 9: Multiple Levels
**Concepts:** Level data array, level loading

#### Unit 10: Level Select
**Concepts:** Menu, choosing levels

#### Unit 11: Level Complete
**Concepts:** Transition, next level

#### Unit 12: Best Scores
**Concepts:** Tracking fewest moves per level

### Phase 4: Polish (Units 13-16)

#### Unit 13: Graphics
**Concepts:** Custom characters for tiles

#### Unit 14: Sound
**Concepts:** POKE to SID for feedback

#### Unit 15: Title Screen
**Concepts:** Menu, instructions

#### Unit 16: Complete Game
**Concepts:** Final testing, polish

---

## Push Mechanics

```basic
100 REM GET DIRECTION
110 J=PEEK(56320)
120 DX=0: DY=0
130 IF (J AND 1)=0 THEN DY=-1: REM UP
140 IF (J AND 2)=0 THEN DY=1: REM DOWN
150 IF (J AND 4)=0 THEN DX=-1: REM LEFT
160 IF (J AND 8)=0 THEN DX=1: REM RIGHT

200 REM CHECK NEXT CELL
210 NX=PX+DX: NY=PY+DY
220 NC=PEEK(1024+NY*40+NX)
230 IF NC=87 THEN RETURN: REM WALL - CAN'T MOVE
240 IF NC<>66 THEN 400: REM NOT BOX - JUST MOVE

300 REM BOX - CHECK IF CAN PUSH
310 BX=NX+DX: BY=NY+DY
320 BC=PEEK(1024+BY*40+BX)
330 IF BC=87 OR BC=66 THEN RETURN: REM CAN'T PUSH
340 REM PUSH THE BOX
350 POKE 1024+BY*40+BX,66: REM BOX TO NEW POSITION
360 POKE 1024+NY*40+NX,32: REM CLEAR OLD BOX POSITION

400 REM MOVE PLAYER
410 POKE 1024+PY*40+PX,32: REM CLEAR OLD
420 PX=NX: PY=NY
430 POKE 1024+PY*40+PX,64: REM DRAW PLAYER
```

### Win Detection

```basic
500 REM CHECK IF ALL TARGETS HAVE BOXES
510 WIN=1
520 FOR I=1 TO NT
530   TX=TX(I): TY=TY(I)
540   IF PEEK(1024+TY*40+TX)<>66 THEN WIN=0
550 NEXT I
560 IF WIN=1 THEN GOSUB 800: REM LEVEL COMPLETE
```

---

## Why Sokoban is Perfect for C64 BASIC

| Reason | Benefit |
|--------|---------|
| **Turn-based** | No speed issues |
| **Character-based** | Perfect fit for PETSCII |
| **Logic-focused** | Gameplay over graphics |
| **Expandable** | Easy to add levels |
| **Classic** | Real game with real challenge |

---

## Skills Learned

- Complex game state
- Two-cell-ahead checking
- Win condition logic
- Level data management
- Undo/history systems
- All previous skills combined
