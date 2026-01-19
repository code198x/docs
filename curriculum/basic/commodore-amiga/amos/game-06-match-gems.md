# Game 06: Match Gems

**Track:** AMOS
**Genre:** Match-3 Puzzle
**Units:** 8
**BASIC Version:** AMOS Professional

---

## Overview

Match-3 puzzle game with cascading gems and combo scoring.

### What You Build

- Gem grid (8x8)
- Swap mechanics
- Match detection
- Cascade/refill
- Combo scoring
- Time/moves modes

---

## Unit Breakdown

### Unit 1: Grid Display
**Concepts:** 2D array, bob grid

### Unit 2: Selection
**Concepts:** Mouse/cursor, highlighting

### Unit 3: Swapping
**Concepts:** Gem exchange, animation

### Unit 4: Match Detection
**Concepts:** Row/column checking

### Unit 5: Removing Matches
**Concepts:** Clearing, animation

### Unit 6: Cascade
**Concepts:** Falling gems, refill

### Unit 7: Combos
**Concepts:** Chain detection, scoring

### Unit 8: Game Modes
**Concepts:** Timed vs moves

---

## Match Detection

```basic
' CHECK FOR MATCHES
Procedure CHECKMATCHES
  For Y=0 To 7
    For X=0 To 5
      ' Check horizontal
      If GRID(X,Y)=GRID(X+1,Y) And GRID(X,Y)=GRID(X+2,Y)
        MARK(X,Y)=True
        MARK(X+1,Y)=True
        MARK(X+2,Y)=True
        MATCHED=True
      End If
    Next X
  Next Y

  For X=0 To 7
    For Y=0 To 5
      ' Check vertical
      If GRID(X,Y)=GRID(X,Y+1) And GRID(X,Y)=GRID(X,Y+2)
        MARK(X,Y)=True
        MARK(X,Y+1)=True
        MARK(X,Y+2)=True
        MATCHED=True
      End If
    Next Y
  Next X
End Proc
```

---

## Skills Learned

- 2D array manipulation
- Pattern matching
- Cascade logic
- Animation timing
- Combo systems
