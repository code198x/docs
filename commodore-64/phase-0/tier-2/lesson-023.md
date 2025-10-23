# Lesson 023: Galactic Defender

**Arc:** Space Shooter Evolution
**Position:** Lesson 7 of 7 in arc
**Type:** Synthesis
**Estimated Completion:** 150 lines of code

## Learning Objectives

- Synthesize all Space Shooter arc concepts into complete game
- Implement title screen, game loop, and game over
- Balance gameplay difficulty and progression
- Experience first performance awareness (12-15 fps with complex systems)
- Create professional-feeling space shooter

## Prerequisites

**From Previous Lessons:**
- Complete Space Shooter arc (L17-22)
- Sound effects library (L11)
- All sprite techniques

**BASIC Knowledge:**
- All Tier 1-2 concepts
- Complex program organization
- State management

## Key Concepts Introduced

### Complete Game Structure
Title screen → Instructions → Game loop → Game over → High score → Play again. Full game flow.

### Difficulty Progression
Increase enemy count, speed, fire rate over time. Score thresholds trigger waves.

### Performance Awareness
With 7 animated enemies + bullets + power-ups, game runs at 12-15 fps. Still playable but noticeable slowdown. First limit discovery.

### Polish Elements
HUD display, wave announcements, visual/audio feedback on all events, satisfying game feel.

## Code Pattern

```basic
10 REM Title screen
20 PRINT CHR$(147):"GALACTIC DEFENDER"
30 PRINT "PRESS FIRE TO START"
40 J=PEEK(56320):IF (J AND 16)=0 THEN 100
50 GOTO 40
100 REM Initialize game
110 DIM EX(7),EY(7),EA(7),EF(7):REM Enemies
120 DIM BX(4),BY(4),BA(4):REM Bullets
130 DIM PX(3),PY(3),PT(3),PA(3):REM Powerups
140 SC=0:L=3:WL=1:W=1:REM Score, lives, weapon, wave
200 REM Main game loop
210 REM [Player input and movement from L18]
220 REM [Fire bullets from L19]
230 REM [Update enemies from L20-21]
240 REM [Check collisions from L19]
250 REM [Update power-ups from L22]
260 REM [Update HUD]
270 POKE 1024,SC:REM Display score
280 POKE 1064,L:REM Display lives
290 REM Check wave progression
300 IF SC>W*1000 THEN W=W+1:GOSUB 5000:REM New wave
310 REM Check game over
320 IF L=0 THEN GOSUB 6000:GOTO 10
330 GOTO 210
5000 REM New wave
5010 PRINT "WAVE";W
5020 REM Spawn more enemies, increase difficulty
5030 RETURN
6000 REM Game over
6010 PRINT "GAME OVER"
6020 PRINT "SCORE:";SC
6030 INPUT "PLAY AGAIN (Y/N)";A$
6040 IF A$="Y" THEN RETURN
6050 END
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - All 8 sprites, collision detection
- **SID** - Music and sound effects
- **CIA** - Joystick input

**Memory Addresses:**
- All sprite systems
- All collision registers
- Sound effects as needed

## Common Pitfalls

1. **Too complex too fast:** Start simple, add features gradually during development
2. **No game over state:** Must handle lives=0 gracefully
3. **Difficulty too hard/easy:** Playtest and balance
4. **Missing feedback:** Every action needs sound/visual response
5. **Performance ignored:** With many sprites, slowdown is noticeable (12-15 fps)

## Extension Ideas

- Add background music (non-blocking from L26 preview)
- Add parallax scrolling background
- Add boss enemies at end of waves
- Add co-op two-player mode
- Save high scores to disk
- Add different enemy types per wave

## Builds Toward

**In Next Tier:**
- Non-blocking music integration (L24-28)
- More complex games with additional systems

**Performance Note:**
"With 7 animated enemies, bullets, and power-ups, the game runs at approximately 12-15 fps. This is BASIC's comfortable ceiling for action games - still playable, but you'll notice the speed difference compared to commercial assembly games running at 50-60 fps."

## Quick Reference

**Game State Machine:**
```basic
10 GS=0  :REM 0=title, 1=playing, 2=gameover
20 ON GS+1 GOTO 100,200,300
100 REM Title screen
200 REM Game loop
300 REM Game over screen
```

**Wave Progression:**
```basic
10 IF SC>W*1000 THEN W=W+1:[increase difficulty]
```

**Difficulty Scaling:**
```basic
10 ENEMY_COUNT = 3 + W  :REM More enemies per wave
20 ENEMY_SPEED = 1 + W/3  :REM Faster enemies
30 FIRE_RATE = 0.01 + W*0.005  :REM More enemy shots
```

**HUD Display Pattern:**
```basic
10 POKE 1024,ASC("S"):REM "S" for Score
20 FOR I=0 TO 4:POKE 1025+I,[score digit]:NEXT I
30 FOR I=1 TO L:POKE 1984+I,3:NEXT I:REM Hearts for lives
```

**Complete Game Checklist:**
- ✓ Title screen with instructions
- ✓ Player movement and shooting (L18-19)
- ✓ Enemy AI and patterns (L20)
- ✓ Sprite animation (L21)
- ✓ Collision detection (L19)
- ✓ Power-up system (L22)
- ✓ Score and lives tracking
- ✓ Wave progression
- ✓ Game over and restart
- ✓ Sound effects on all actions
- ✓ HUD display
- ✓ Visual feedback

**Arc 1 Complete - Space Shooter Mastered!**
Performance note: 12-15 fps is the first hint of BASIC's limits.
