# Game 07: Battle Grid

**Track:** Blitz Basic
**Genre:** Turn-Based Tactics
**Units:** 8
**BASIC Version:** Blitz Basic 2

---

## Overview

Turn-based tactical combat on a grid. Different unit types, terrain effects, and AI opponents.

### What You Build

- Grid-based movement
- Unit types (infantry, armour, artillery)
- Terrain effects
- Combat system
- AI opponent
- Campaign mode

---

## Unit Breakdown

### Unit 1: Grid Display
**Concepts:** Tile map, cursor

### Unit 2: Unit Placement
**Concepts:** Unit data, teams

### Unit 3: Selection/Movement
**Concepts:** Move range, pathfinding

### Unit 4: Combat
**Concepts:** Attack, damage, defence

### Unit 5: Unit Types
**Concepts:** Stats, abilities

### Unit 6: Terrain
**Concepts:** Cover, movement cost

### Unit 7: AI Opponent
**Concepts:** Decision making

### Unit 8: Victory Conditions
**Concepts:** Win/lose, campaign

---

## Turn System

```blitz
; TURN-BASED STRUCTURE
DEFTYPE .w

currentTeam.w = 1
selectedUnit.w = -1
gameState.w = #STATE_SELECT

Statement GameLoop{}
  Select gameState
    Case #STATE_SELECT
      HandleSelection{}
    Case #STATE_MOVE
      HandleMovement{}
    Case #STATE_ATTACK
      HandleAttack{}
    Case #STATE_AI
      AITurn{}
  End Select
End Statement

Statement EndTurn{}
  ; Reset unit actions
  For u = 0 To numUnits-1
    If unitTeam(u) = currentTeam
      unitMoved(u) = False
      unitAttacked(u) = False
    End If
  Next u

  ; Switch teams
  currentTeam = 3 - currentTeam  ; Toggle 1<->2
  If currentTeam = 2 Then gameState = #STATE_AI Else gameState = #STATE_SELECT
End Statement
```

---

## Skills Learned

- Turn-based structure
- Unit management
- Grid-based pathfinding
- Tactical AI
- Campaign structure
