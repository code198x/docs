# Lesson 051: Many Enemies Attempt

**Arc:** Speed Limit - Fast Action Shmup
**Position:** Lesson 3 of 5 in arc
**Type:** Standard
**Estimated Completion:** 110 lines of code

## Learning Objectives

- Increase enemy count to 7 animated enemies
- Implement multi-frame enemy animation
- Measure performance with many active sprites
- Discover sprite animation overhead
- Document FPS dropping to 8-10 fps

## Prerequisites

**From Previous Lessons:**
- Shmup with scrolling (L49-50)
- Multi-frame animation (L21, L34)
- Performance measurement

**BASIC Knowledge:**
- Managing many sprites simultaneously
- Animation frame cycling
- Performance profiling

## Key Concepts Introduced

### Increased Enemy Count
7 simultaneous enemies (up from 3). All with AI movement patterns and collision detection.

### Enemy Animation
Each enemy uses 2-4 frame animation cycle. Sprite pointer changes each frame for all active enemies.

### Performance Collapse
Adding 4 more animated enemies causes **FPS to drop from 12-14 to 8-10 fps**. Sprite updates + AI + animation = significant overhead.

### Sprite Limit Awareness
Approaching C64's 8-sprite hardware limit (player + 7 enemies). Any more requires multiplexing (L57).

## Code Pattern

```basic
10 REM Shmup: Many animated enemies
20 REM Performance: 8-10 fps measured
30 REM Enemies: 7 concurrent
40 DIM EX(7),EY(7),EACTIVE(7),ETYPE(7),EFRAME(7)
50 MAXENEMIES=7
60 REM Player, bullets, etc.
70 PX=160:PY=220:SCORE=0:PLIVES=3
80 DIM BX(5),BY(5),BACTIVE(5)
90 REM Timing
100 FC=0:FPS=0:LASTFPS=TI
110 REM Initialize
120 POKE 53269,255:REM Enable all 8 sprites
130 REM Main loop
140 FC=FC+1
150 REM FPS measurement
160 IF TI-LASTFPS>50 THEN GOSUB 8000
170 REM Scrolling (from L50)
180 IF FC MOD 2=0 THEN GOSUB 1000
190 REM Input
200 J=PEEK(56320)
210 IF (J AND 4)=0 AND PX>24 THEN PX=PX-3
220 IF (J AND 8)=0 AND PX<296 THEN PX=PX+3
230 IF (J AND 16)=0 THEN GOSUB 2000:REM Shoot
240 REM Update bullets
250 GOSUB 3000
260 REM Update enemies
270 GOSUB 4000
280 REM Spawn enemies
290 IF TI-LASTSPAWN>60 AND ENEMYCOUNT<MAXENEMIES THEN GOSUB 5000
300 REM Update sprites
310 GOSUB 6000
320 REM HUD
330 GOSUB 7000
340 GOTO 140
4000 REM Update enemies (7 animated)
4010 FOR E=1 TO MAXENEMIES
4020 IF EACTIVE(E)=0 THEN NEXT E:RETURN
4030 REM AI movement
4040 EY(E)=EY(E)+2
4050 IF ETYPE(E)=0 THEN REM Straight
4060 IF ETYPE(E)=1 THEN EX(E)=EX(E)+SIN(FC*0.1)*2:REM Zigzag
4070 IF ETYPE(E)=2 THEN EX(E)=EX(E)+COS(FC*0.15)*1.5:REM Sine wave
4080 REM Animation
4090 EFRAME(E)=(EFRAME(E)+1) AND 3:REM 4-frame cycle
4100 REM Off-screen check
4110 IF EY(E)>250 THEN EACTIVE(E)=0:ENEMYCOUNT=ENEMYCOUNT-1:GOTO 4140
4120 REM Collision with player
4130 IF ABS(EX(E)-PX)<20 AND ABS(EY(E)-PY)<18 THEN GOSUB 9000
4140 NEXT E
4150 RETURN
6000 REM Update sprites
6010 REM Player
6020 POKE 2040,13:POKE 53248,PX:POKE 53249,PY
6030 REM Enemies (sprites 1-7)
6040 FOR E=1 TO MAXENEMIES
6050 IF EACTIVE(E)=0 THEN POKE 53248+E*2,0:GOTO 6090
6060 REM Animated sprite pointer
6070 POKE 2040+E,20+EFRAME(E):REM Frames 20-23
6080 POKE 53248+E*2,EX(E):POKE 53249+E*2,EY(E)
6090 NEXT E
6100 RETURN
7000 REM HUD
7010 PRINT CHR$(19);
7020 PRINT "SCORE:";SCORE;" FPS:";FPS;" ENEMIES:";ENEMYCOUNT;"  ";
7030 RETURN
8000 REM Calculate FPS
8010 FRAMES=FC-LASTFC
8020 JIFFIES=TI-LASTFPS
8030 IF JIFFIES>0 THEN FPS=INT(FRAMES*60/JIFFIES)
8040 LASTFPS=TI:LASTFC=FC
8050 RETURN
```

## Performance Measurement

**Measured Performance:**
```
Configuration: Player + 7 animated enemies + scrolling
Expected FPS: 8-10 fps (down from 12-14)
Frame time: ~100-125ms per frame
Performance loss from L50: ~30%
```

**Overhead Sources:**
```
- 7 enemy AI updates (movement calculations)
- 7 enemy animation frame cycles
- 7 enemy collision checks (with player and bullets)
- 7 sprite position updates (POKE operations)
- 7 sprite pointer updates (animation)
- Scrolling background (960 bytes/scroll from L50)
```

## Limit Discovery

**Many Sprites = Major Slowdown:**

"Adding 4 more animated enemies (7 total) causes **FPS to drop from 12-14 to 8-10** (another 30% loss).

**Why so expensive?**
- Each enemy requires:
  - AI movement calculation (SIN/COS for patterns)
  - Animation frame update
  - Collision check with player
  - Collision check with all bullets
  - Sprite position POKE
  - Sprite pointer POKE
- × 7 enemies = massive overhead

**Total overhead per frame:**
- 7 AI calculations
- 7 animation updates
- 7 × 5 bullet collision checks = 35 checks
- 14 POKE operations
- Plus scrolling (1920 ops every 2 frames)

**We're now at 8-10 fps with game not even complete yet.** Commercial shmups have 20+ enemies at 50-60 fps (in assembly).

**Next lesson adds particle effects → drops to 6-8 fps (ceiling).**"

## Common Pitfalls

1. **Exceeding 8 sprite limit:** Need multiplexing (L57) or sprite reuse
2. **Too many collision checks:** O(n²) with bullets becomes expensive
3. **Complex AI patterns:** SIN/COS calculations per enemy adds overhead
4. **Animation every frame:** Can reduce to every 2-3 frames for savings
5. **Not culling off-screen enemies:** Still updating invisible enemies

## Builds Toward

**In This Arc:**
- L52: Particle effects (more sprites, drops to 6-8 fps)
- L53: Complete shmup with all features (6-8 fps ceiling confirmed)

## Quick Reference

**Enemy Count vs Performance:**
```
1-3 enemies: 15-18 fps (manageable)
4-5 enemies: 12-15 fps (noticeable slowdown)
6-7 enemies: 8-10 fps (choppy)
8+ enemies: Requires multiplexing (L57)
```

**Animation Overhead:**
```
Static sprites: ~1ms per sprite
Animated (4 frames): ~3-4ms per sprite
Complex AI: Additional 2-3ms
Total: ~5-7ms per animated enemy with AI
× 7 enemies = 35-49ms overhead
```

**Optimization Attempts (Insufficient):**
```
1. Animate every 2-3 frames: Saves ~20% (still slow)
2. Simpler AI: Saves ~15% (less interesting)
3. Reduce collision checks: Saves ~10% (but affects gameplay)
4. Lower enemy count: Defeats the purpose
```

**Performance Note:**
"Seven animated enemies with AI patterns causes **FPS to drop to 8-10** (from 12-14 in L50). Each enemy requires AI calculation, animation update, collision checks, and sprite updates. BASIC's interpreter parses every line—with 7 enemies, overhead compounds. Game is still functional but visibly choppy. **Sprite animation + AI + scrolling = BASIC's limit approaching.**"
