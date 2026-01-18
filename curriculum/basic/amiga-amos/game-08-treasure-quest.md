# Game 08: Treasure Quest

**Track:** AMOS
**Genre:** Action-Adventure
**Units:** 16
**BASIC Version:** AMOS Professional

---

## Overview

**Capstone project** - Zelda-style action-adventure with exploration, items, NPCs, and quests.

### What You Build

- Multi-screen world
- Inventory system
- NPC dialogue
- Combat system
- Puzzles
- Quest tracking
- Save/load game

---

## Unit Breakdown

### Phase 1: World (Units 1-4)

#### Unit 1: Screen System
**Concepts:** Room data, transitions

#### Unit 2: World Map
**Concepts:** Connected screens, exploration

#### Unit 3: Player Character
**Concepts:** Movement, animation

#### Unit 4: Scrolling
**Concepts:** Screen edge transitions

### Phase 2: Items (Units 5-8)

#### Unit 5: Item System
**Concepts:** Item database, properties

#### Unit 6: Inventory
**Concepts:** Menu, selection

#### Unit 7: Equipment
**Concepts:** Weapons, armor effects

#### Unit 8: Shops
**Concepts:** Buying, selling, gold

### Phase 3: Interaction (Units 9-12)

#### Unit 9: NPCs
**Concepts:** Characters, dialogue trees

#### Unit 10: Combat
**Concepts:** Attacking, damage, health

#### Unit 11: Enemies
**Concepts:** AI, attack patterns

#### Unit 12: Puzzles
**Concepts:** Switches, doors, keys

### Phase 4: Quest (Units 13-16)

#### Unit 13: Quest System
**Concepts:** Objectives, tracking

#### Unit 14: Boss Battles
**Concepts:** Unique enemies, patterns

#### Unit 15: Save/Load
**Concepts:** File operations, state

#### Unit 16: Complete Game
**Concepts:** Polish, balance, testing

---

## Dialogue System

```basic
' NPC DIALOGUE
Procedure TALKNPC[NPC]
  Read LINES : ' Number of dialogue lines
  For I=1 To LINES
    Read LINE$
    DIALOGUEBOX[LINE$]
    Repeat : Until Fire(1)
    Wait 10
  Next I
End Proc

Procedure DIALOGUEBOX[TEXT$]
  ' Draw dialogue box
  Ink 0 : Bar 20,180 To 300,240
  Ink 1 : Box 20,180 To 300,240
  Text 30,200,TEXT$
End Proc
```

---

## Save System

```basic
' SAVE GAME
Procedure SAVEGAME
  Open Out 1,"ram:savegame.dat"
  Print #1,PX;",";PY;",";ROOM
  Print #1,GOLD;",";HP;",";MAXHP
  For I=1 To 20
    Print #1,INVENTORY(I)
  Next I
  For I=1 To 10
    Print #1,QUESTFLAG(I)
  Next I
  Close 1
End Proc
```

---

## Skills Learned

- Complete game architecture
- NPC and dialogue systems
- Combat mechanics
- Quest design
- Save/load functionality
- All AMOS features combined
