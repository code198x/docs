# Lesson 016: Spectrum Survivor

**Arc:** Mini Action Game
**Position:** Lesson 2 of 2 in arc
**Type:** Synthesis (Complete Game)
**Estimated Completion:** 60 lines of code

## Learning Objectives

- Combine all Tier 1 concepts into complete game
- Implement lives system
- Add increasing difficulty
- Create full game loop (intro, play, game over)

## Key Concepts Introduced

### Lives System
Track lives variable. Decrement on collision. Game over when lives=0.

### Difficulty Progression
Increase enemy speed or add more enemies as score increases.

### Complete Game Structure
- Title screen
- Game loop
- Game over screen with final score
- Option to restart

## Code Pattern

```basic
10 REM Title
20 PRINT AT 10,8;"SPECTRUM SURVIVOR"
30 PAUSE 0
40 REM Initialize
50 LET score=0: LET lives=3
60 REM Main game loop
70 GOSUB 1000: REM Player input
80 GOSUB 2000: REM Enemy AI
90 GOSUB 3000: REM Collision check
100 GOSUB 4000: REM Draw
110 IF lives>0 THEN GO TO 70
120 REM Game over
130 PRINT AT 11,8;"GAME OVER"
140 PRINT AT 12,7;"Score: ";score
```

## Builds Toward

**Next Tier:**
- User-Defined Graphics (UDG) for better sprites
- More sophisticated AI
- Level progression systems
- Multi-screen games

## Quick Reference

**Tier 1 Concepts Mastered:**
- PRINT AT positioning
- INPUT and IF...THEN
- READ/DATA
- Arrays (DIM)
- PLOT/DRAW/CIRCLE graphics
- INK/PAPER/BRIGHT attributes
- BEEP sound
- INKEY$ input
- SCREEN$ collision
- Character-based sprites
- Simple AI

**Ready for Tier 2:** Professional game systems

---

**Version:** 1.0
**Created:** 2025-10-24
