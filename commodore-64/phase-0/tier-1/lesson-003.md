# Lesson 003: Guess the Number

**Arc:** Number Challenge
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis
**Estimated Completion:** 25 lines of code

## Learning Objectives

- Generate random numbers with RND
- Create a complete game loop with win/lose conditions
- Track score and attempts across multiple rounds
- Synthesize all Number Challenge arc concepts into a playable game

## Prerequisites

**From Previous Lessons:**
- Variables and PRINT (L1)
- INPUT and IF/THEN (L2)
- Program loops (L1)

**BASIC Knowledge:**
- `PRINT`, `INPUT`, `IF/THEN`, `GOTO`
- Variables for storage

## Key Concepts Introduced

### Random Number Generation
`RND(1)` generates a random decimal between 0 and 1. Multiply and add to get the range you need: `INT(RND(1)*10)+1` gives 1-10.

### Game Loop Structure
A complete game has: setup → play round → check win/lose → score → play again. This pattern appears in almost every game.

### Comparative Feedback
Good games guide players. "Too high" and "Too low" hints make the game interactive and fair rather than frustrating.

## Code Pattern

```basic
10 S=0:A=0
20 N=INT(RND(1)*10)+1
30 INPUT "GUESS (1-10)";G
40 A=A+1
50 IF G=N THEN S=S+10:PRINT "YES!":GOTO 80
60 IF G<N THEN PRINT "TOO LOW"
70 IF G>N THEN PRINT "TOO HIGH":GOTO 30
80 PRINT "SCORE:";S;" ATTEMPTS:";A
90 GOTO 20
```

## Hardware Interaction

**Chips Involved:**
- None - pure BASIC game logic

**Memory Addresses:**
- None yet

## Common Pitfalls

1. **RND without INT:** Forgetting `INT()` gives decimals, not whole numbers
2. **Range errors:** `RND(1)*10` gives 0-9, need `+1` for 1-10
3. **Infinite loops:** Make sure there's a path to win condition
4. **Not resetting variables:** Score should persist, but attempts/number should reset

## Extension Ideas

- Increase range (1-100 for harder gameplay)
- Limit number of attempts before losing
- Add difficulty levels (easy/medium/hard ranges)
- Display high score across sessions
- Add time pressure (preview of TI timer from L15)

## Builds Toward

**In This Tier:**
- L4: Quiz system uses similar INPUT/check pattern
- L5: High score tracking extends scoring concept
- L14: Star Catcher applies game loop to action game

**In Next Tier:**
- Random number generation for enemy positions
- Game loop structure for all arcade games

## Quick Reference

**Random Number Functions:**
- `RND(1)` - Random decimal 0.0 to 0.999...
- `INT(RND(1)*N)` - Random integer 0 to N-1
- `INT(RND(1)*N)+1` - Random integer 1 to N

**Common Ranges:**
- 1-10: `INT(RND(1)*10)+1`
- 1-100: `INT(RND(1)*100)+1`
- 0-255: `INT(RND(1)*256)`

**Game Loop Pattern:**
```basic
10 REM Setup
20 REM Generate challenge
30 REM Get input
40 REM Check result
50 REM Update score
60 REM Next round
```
