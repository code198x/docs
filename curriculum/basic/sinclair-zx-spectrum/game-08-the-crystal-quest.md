# Game 08: The Crystal Quest

**Track:** Spectrum BASIC
**Genre:** Puzzle Adventure
**Units:** 16
**BASIC Version:** Sinclair BASIC

---

## Overview

**Capstone project** combining text adventure elements with graphical screens. Collect crystals, solve puzzles, escape the dungeon.

### What You Build

- Multiple graphical screens
- Inventory system
- Puzzle elements
- NPCs with dialogue
- Crystal collection quest
- Complete game experience

---

## Unit Breakdown

### Phase 1: World (Units 1-4)

#### Unit 1: Screen Design
**Concepts:** Room graphics, layout

#### Unit 2: Screen Connections
**Concepts:** Movement between screens

#### Unit 3: Player Character
**Concepts:** UDG, position, movement

#### Unit 4: Main Loop
**Concepts:** Game state, display cycle

### Phase 2: Items (Units 5-8)

#### Unit 5: Item Placement
**Concepts:** Items on screens

#### Unit 6: Collecting Items
**Concepts:** Pickup mechanics

#### Unit 7: Inventory Display
**Concepts:** Status panel

#### Unit 8: Using Items
**Concepts:** Context-sensitive use

### Phase 3: Puzzles (Units 9-12)

#### Unit 9: Locked Doors
**Concepts:** Keys and doors

#### Unit 10: Push Blocks
**Concepts:** Sokoban-style blocks

#### Unit 11: NPCs
**Concepts:** Characters, dialogue

#### Unit 12: Crystal Collection
**Concepts:** Quest tracking

### Phase 4: Polish (Units 13-16)

#### Unit 13: Sound Effects
**Concepts:** BEEP command

#### Unit 14: Title Screen
**Concepts:** Presentation

#### Unit 15: Save/Load
**Concepts:** (Optional) Tape operations

#### Unit 16: Complete Game
**Concepts:** Balance, testing, polish

---

## Combining Graphics and Adventure

```basic
100 REM DRAW ROOM
110 CLS
120 GO SUB 1000+room*100: REM Room graphics
130 GO SUB 5000: REM Draw items in room
140 GO SUB 6000: REM Draw player
150 GO SUB 7000: REM Status bar

200 REM MAIN LOOP
210 LET k$ = INKEY$
220 IF k$ = "5" THEN GO SUB 3000: REM LEFT
230 IF k$ = "8" THEN GO SUB 3100: REM RIGHT
240 IF k$ = "i" THEN GO SUB 4000: REM INVENTORY
250 IF k$ = "u" THEN GO SUB 4500: REM USE ITEM
260 GO TO 200
```

---

## Skills Learned

- All previous skills combined
- Screen-based adventure design
- Quest/goal tracking
- NPC interaction
- BEEP for sound
- Complete game structure
