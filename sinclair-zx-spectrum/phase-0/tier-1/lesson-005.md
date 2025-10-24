# Lesson 005: Quiz Master

**Arc:** Knowledge Base
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 30 lines of code

## Learning Objectives

- Use RESTORE to replay DATA from the start
- Create menu systems for quiz categories
- Track high scores across multiple attempts
- Improve quiz game structure

## Prerequisites

**From Previous Lessons:**
- L4: READ, DATA statements

**BASIC Knowledge:**
- DATA management and scoring

## Key Concepts Introduced

### RESTORE Command
RESTORE resets the READ pointer back to the first DATA statement, allowing you to read through DATA multiple times.

### Menu Systems
Present choices to the player and branch to different sections based on input.

### High Score Tracking
Keep track of the best score across multiple game sessions (until program stops).

### Structured Programs
Use line number ranges for different sections (100s for menu, 1000s for quiz, etc.).

## Code Pattern

```basic
10 REM Quiz Master
20 LET highscore=0
30 CLS
40 PRINT AT 5,10;"QUIZ MASTER"
50 PRINT AT 8,8;"1. Animals"
60 PRINT AT 10,8;"2. Geography"
70 PRINT AT 12,8;"3. History"
80 INPUT "Choose: ";choice
90 IF choice=1 THEN GOSUB 1000
100 IF choice=2 THEN GOSUB 2000
110 GO TO 30
1000 REM Animals Quiz
1010 RESTORE
1020 LET score=0
1030 REM Quiz loop here
1090 RETURN
2000 DATA "Biggest mammal?","Whale"
```

## Hardware Interaction

**Chips Involved:**
- Z80 CPU (DATA pointer management)
- ULA (menu display)

**Memory:**
- RESTORE resets internal DATA pointer
- High score stored in variable (RAM)

## Common Pitfalls

1. **Forgetting RESTORE:** Trying to read DATA twice without RESTORE causes error
2. **Wrong subroutine structure:** Must RETURN from GOSUB
3. **Score not updating:** Check highscore comparison logic
4. **Poor menu layout:** Use PRINT AT for clean visual hierarchy

## Extension Ideas

- Add difficulty levels (easy/hard questions)
- Show percentage score (score/total * 100)
- Add timer (PAUSE between questions)
- Create lifelines (skip question)
- Allow player name entry for high score

## Builds Toward

**In This Tier:**
- L6: Arrays for more complex quiz data
- L7-9: Structured programs with graphics

**In Next Tier:**
- Menu systems for game selection
- High score tables with multiple entries

## Quick Reference

**Essential Commands:**
- `RESTORE` - Reset DATA read pointer to start
- `GOSUB linenumber` - Call subroutine
- `RETURN` - Return from subroutine

**Program Structure:**
```basic
10-90:   Main menu
100-900: Menu handling
1000+:   Subroutines
9000+:   DATA statements
```

**Highscore Pattern:**
```basic
10 LET highscore=0
...
100 IF score>highscore THEN LET highscore=score
110 PRINT "High Score: ";highscore
```

**Multiple RESTORE:**
- Can use RESTORE in different subroutines
- Each section can read DATA independently
- Useful for category-based quizzes

---

**Version:** 1.0
**Created:** 2025-10-24
**Status:** Lesson specification complete
