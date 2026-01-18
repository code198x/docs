# Game 08: Block Slider

**Track:** C64 BASIC
**Genre:** Sokoban Puzzle
**Units:** 16
**BASIC Version:** Simons' BASIC

---

## Overview

Sokoban-style puzzle game. Push blocks onto targets. **Capstone project** combining all skills.

### What You Build

- Push-block mechanics
- Multiple puzzle levels
- Win detection
- Move counter
- Undo system
- Level select

---

## Unit Breakdown

### Phase 1: Core Mechanics (Units 1-4)

#### Unit 1: Level Display
**Concepts:** Level data, tile drawing

#### Unit 2: Player Movement
**Concepts:** Grid movement, collision

#### Unit 3: Block Pushing
**Concepts:** Push detection, block movement

#### Unit 4: Target Detection
**Concepts:** Win condition checking

### Phase 2: Levels (Units 5-8)

#### Unit 5: Multiple Levels
**Concepts:** Level data array, level loading

#### Unit 6: Level Progression
**Concepts:** Next level, completion

#### Unit 7: Level Select
**Concepts:** Menu system, level choice

#### Unit 8: Level Design
**Concepts:** Creating good puzzles

### Phase 3: Features (Units 9-12)

#### Unit 9: Move Counter
**Concepts:** Counting, display

#### Unit 10: Undo System
**Concepts:** State history, array stack

#### Unit 11: Restart Level
**Concepts:** State reset, original data

#### Unit 12: Best Scores
**Concepts:** Tracking best moves per level

### Phase 4: Polish (Units 13-16)

#### Unit 13: Graphics
**Concepts:** Custom characters, colors

#### Unit 14: Sound
**Concepts:** SOUND command, feedback

#### Unit 15: Title Screen
**Concepts:** Menu, instructions

#### Unit 16: Complete Game
**Concepts:** Final testing, polish

---

## Push Mechanics

```basic
100 REM CHECK PUSH
110 NX = PX + DX: NY = PY + DY: REM NEXT CELL
120 IF LEVEL(NX,NY) = WALL THEN RETURN
130 IF LEVEL(NX,NY) = BOX THEN GOSUB 500: REM TRY PUSH
140 IF CANMOVE THEN PX = NX: PY = NY

500 REM PUSH BOX
510 BX = NX + DX: BY = NY + DY
520 IF LEVEL(BX,BY) <> EMPTY THEN CANMOVE = 0: RETURN
530 LEVEL(BX,BY) = BOX
540 LEVEL(NX,NY) = EMPTY
550 CANMOVE = 1
560 RETURN
```

---

## Skills Learned

- Complex game state
- Undo/history systems
- Puzzle design
- Level data management
- Menu systems
- All previous skills combined
