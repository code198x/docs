# Lesson 014: Star Catcher

**Arc:** Dodge & Catch
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis
**Estimated Completion:** 60 lines of code

## Learning Objectives

- Implement collision detection between player and objects
- Add game state (score, lives, game over)
- Integrate sound effects into gameplay
- Create complete game loop with win/lose conditions
- Synthesize all Dodge & Catch concepts

## Prerequisites

**From Previous Lessons:**
- Player movement (L12)
- Falling objects (L13)
- Sound effects (L11)
- Scoring system (L3)

**BASIC Knowledge:**
- Arrays for multiple objects
- Screen memory manipulation
- Game loop structure
- GOSUB for sound effects

## Key Concepts Introduced

### Collision Detection
Check if player position (PX, PY) matches any object position (FX(I), FY(I)). If match = collision occurred.

### Game State Management
Track lives, score, game-over state. Different game states control which code runs (playing vs game over).

### Feedback Integration
Collision triggers sound effect AND visual feedback AND score change. Multiple systems respond to one event.

### Complete Game Structure
Title → Instructions → Main loop → Game over → Play again. This is the standard game flow.

## Code Pattern

```basic
10 DIM FX(5),FY(5):S=0:L=3:PX=20:PY=23
20 REM Game loop
30 POKE 1024+(PY*40)+PX,32:REM Erase player
40 GET K$
50 IF K$="A" AND PX>0 THEN PX=PX-1
60 IF K$="D" AND PX<39 THEN PX=PX+1
70 REM Update falling stars
80 FOR I=1 TO 5
90 POKE 1024+(FY(I)*40)+FX(I),32
100 FY(I)=FY(I)+1
110 IF FY(I)>24 THEN FY(I)=0:FX(I)=INT(RND(1)*40)
120 REM Collision check
130 IF FX(I)=PX AND FY(I)=PY THEN GOSUB 1000
140 POKE 1024+(FY(I)*40)+FX(I),42
150 NEXT I
160 POKE 1024+(PY*40)+PX,81:REM Draw player
170 POKE 1024,S:REM Show score
180 IF L=0 THEN PRINT "GAME OVER":END
190 GOTO 30
1000 REM Collision handler
1010 S=S+10:GOSUB 2000:REM Score + sound
1020 FY(I)=0:FX(I)=INT(RND(1)*40):REM Respawn
1030 RETURN
2000 REM Coin sound
2010 POKE 54296,15:POKE 54272,100:POKE 54273,30
2020 POKE 54276,65:FOR D=1 TO 100:NEXT D
2030 POKE 54276,64:RETURN
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Screen and colour display
- **SID** - Sound effects on collision
- **CIA** - Keyboard input

**Memory Addresses:**
- `1024-2023` - Screen memory
- `54272-54296` - SID registers for sound

## Common Pitfalls

1. **Collision check timing:** Must check AFTER object moves but BEFORE drawing
2. **Off-by-one collision:** FX=PX±1 counted as hit (too lenient)
3. **Missing respawn:** Caught object must respawn or game becomes too easy
4. **Lives never decrease:** Need bad collision type (or time limit)
5. **Sound blocking game:** Sound effect too long = frozen gameplay

## Extension Ideas

- Add different object types (good stars = points, bad asteroids = damage)
- Add power-ups (extra lives, score multipliers, invincibility)
- Increase difficulty (speed up over time, add more objects)
- Add timer pressure (L15 countdown timer)
- Add vertical player movement (full 2D movement)
- Add high score table (L5 integration)

## Builds Toward

**In This Tier:**
- L16: Text adventure uses similar state management

**In Next Tier:**
- Sprite-based games use same collision concepts
- Hardware collision detection (VIC-II registers)
- More complex AI and enemy patterns

## Quick Reference

**Collision Detection Pattern:**
```basic
100 IF PX=OX AND PY=OY THEN GOSUB [collision handler]
```

**Game State Variables:**
```basic
10 S=0    :REM Score
20 L=3    :REM Lives
30 G=0    :REM Game over flag (0=playing, 1=game over)
```

**Complete Game Loop:**
```basic
10 REM Title screen
20 REM Initialize game state
30 REM Main game loop start
40 REM   Input
50 REM   Update player
60 REM   Update objects
70 REM   Collision detection
80 REM   Draw everything
90 REM   Check win/lose
100 REM   Repeat or end
110 GOTO 30 or END
```

**Collision Handler Pattern:**
```basic
1000 REM Collision detected
1010 S=S+10        :REM Update score
1020 GOSUB 2000    :REM Play sound
1030 [respawn object]
1040 RETURN
```

**Integration Checklist:**
- Player movement (WASD or left/right)
- Falling objects (spawning and moving)
- Collision detection (position matching)
- Score tracking and display
- Lives system (optional for this variant)
- Sound effects on events
- Game over condition
- Clear visual feedback
