# Lesson 014: Collect and Score

**Arc:** Moving Sprites
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis (Mini-game)
**Estimated Completion:** 50 lines of code

## Learning Objectives

- Add collectible items to games
- Implement scoring system
- Create win condition (all items collected)
- Complete first action game

## Key Concepts Introduced

### Collectibles
Place items (*) around maze. When player moves onto one, increment score and remove item.

### Win Condition
Check if score equals total items. If so, display victory message.

### Game State
Track score, items remaining, player position.

## Code Pattern

```basic
10 LET score=0: LET items=5
20 REM Place items
30 PRINT AT 5,10;"*": PRINT AT 8,20;"*"
40 REM Movement loop
50 IF SCREEN$(ny,nx)="*" THEN GOSUB 1000
60 IF score=items THEN GOSUB 2000
70 GO TO 40
1000 REM Collect item
1010 LET score=score+1
1020 PRINT AT 0,0;"Score: ";score
1030 RETURN
2000 REM Win
2010 PRINT AT 11,10;"YOU WIN!"
2020 STOP
```

## Quick Reference

- Check for collectible character in SCREEN$
- Increment score when collected
- Erase collected item (print space)
- Display score with PRINT AT (fixed position)

---

**Version:** 1.0
**Created:** 2025-10-24
