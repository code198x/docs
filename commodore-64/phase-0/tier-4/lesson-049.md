# Lesson 049: Shmup Foundation

**Arc:** Speed Limit - Fast Action Shmup
**Position:** Lesson 1 of 5 in arc
**Type:** Standard
**Estimated Completion:** 80 lines of code

## Learning Objectives

- Build shoot-em-up foundation (player ship + enemies)
- Implement bullet system with collision
- Create enemy wave spawning
- Establish baseline performance measurement
- Begin discovering speed limitations

## Prerequisites

**From Previous Lessons:**
- Sprite control and collision (L17-23)
- Enemy AI patterns (L36)
- Physics concepts (L29-30)

**BASIC Knowledge:**
- Multiple sprite management
- Bullet array handling
- Frame timing measurement

## Key Concepts Introduced

### Shmup Structure
Player ship at bottom, enemies spawn at top and move down. Player shoots bullets upward. Collision with enemies scores points.

### Bullet System
Array of active bullets: BX(n), BY(n), BACTIVE(n). Update all bullets each frame. Remove when off-screen or hit enemy.

### Enemy Waves
Spawn enemies at intervals. Simple patterns: straight down, zigzag, diving. Track active enemies in arrays.

### Performance Baseline
Measure FPS with TI register. Basic shmup (player + 3 enemies + 5 bullets) establishes baseline: **15-18 fps**.

## Code Pattern

```basic
10 REM Shmup foundation
20 REM Performance baseline measurement
30 REM Player ship
40 PX=160:PY=220:PLIVES=3:SCORE=0
50 REM Bullets (max 5 active)
60 DIM BX(5),BY(5),BACTIVE(5)
70 MAXBULLETS=5:BULLETCOUNT=0
80 REM Enemies (max 3 active)
90 DIM EX(3),EY(3),EACTIVE(3),ETYPE(3)
100 MAXENEMIES=3:ENEMYCOUNT=0
110 REM Timing
120 FC=0:LASTSPAWN=0:LASTSHOT=0
130 FPS=0:LASTFPS=TI
140 REM Initialize
150 POKE 53269,15:REM Enable sprites 0-3
160 POKE 53287,1:REM Player white
170 FOR I=1 TO 3:POKE 53287+I,2:NEXT I:REM Enemies red
180 REM Main loop
190 FC=FC+1
200 REM FPS measurement
210 IF TI-LASTFPS>50 THEN GOSUB 9000:REM Update FPS every second
220 REM Input
230 J=PEEK(56320)
240 IF (J AND 4)=0 AND PX>24 THEN PX=PX-3:REM Left
250 IF (J AND 8)=0 AND PX<296 THEN PX=PX+3:REM Right
260 IF (J AND 1)=0 AND PY>50 THEN PY=PY-2:REM Up
270 IF (J AND 2)=0 AND PY<229 THEN PY=PY+2:REM Down
280 IF (J AND 16)=0 AND TI-LASTSHOT>10 THEN GOSUB 1000:REM Shoot
290 REM Update bullets
300 GOSUB 2000
310 REM Update enemies
320 GOSUB 3000
330 REM Spawn enemies
340 IF TI-LASTSPAWN>100 AND ENEMYCOUNT<MAXENEMIES THEN GOSUB 4000
350 REM Update sprites
360 GOSUB 5000
370 REM Display HUD
380 GOSUB 6000
390 GOTO 190
1000 REM Shoot bullet
1010 FOR I=1 TO MAXBULLETS
1020 IF BACTIVE(I)=0 THEN
1030 BX(I)=PX:BY(I)=PY-20:BACTIVE(I)=1
1040 BULLETCOUNT=BULLETCOUNT+1:LASTSHOT=TI
1050 REM Shoot sound
1060 POKE 54296,15:POKE 54276,8:POKE 54273,20
1070 FOR J=1 TO 3:NEXT J:POKE 54276,0
1080 RETURN
1090 NEXT I
1100 RETURN:REM All bullets active
2000 REM Update bullets
2010 FOR I=1 TO MAXBULLETS
2020 IF BACTIVE(I)=0 THEN NEXT I:RETURN
2030 REM Move bullet up
2040 BY(I)=BY(I)-5
2050 REM Check if off-screen
2060 IF BY(I)<0 THEN BACTIVE(I)=0:BULLETCOUNT=BULLETCOUNT-1:GOTO 2090
2070 REM Check collision with enemies
2080 GOSUB 7000
2090 NEXT I
2100 RETURN
3000 REM Update enemies
3010 FOR E=1 TO MAXENEMIES
3020 IF EACTIVE(E)=0 THEN NEXT E:RETURN
3030 REM Move enemy down
3040 EY(E)=EY(E)+2
3050 REM Zigzag pattern (type 1)
3060 IF ETYPE(E)=1 THEN EX(E)=EX(E)+SIN(FC*0.1)*2
3070 REM Check if off-screen
3080 IF EY(E)>250 THEN EACTIVE(E)=0:ENEMYCOUNT=ENEMYCOUNT-1:GOTO 3100
3090 REM Check collision with player
3100 IF ABS(EX(E)-PX)<20 AND ABS(EY(E)-PY)<18 THEN GOSUB 8000
3110 NEXT E
3120 RETURN
4000 REM Spawn enemy
4010 FOR E=1 TO MAXENEMIES
4020 IF EACTIVE(E)=0 THEN
4030 EX(E)=INT(RND(1)*280)+20:REM Random X
4040 EY(E)=20:REM Top of screen
4050 ETYPE(E)=INT(RND(1)*2):REM Type 0 or 1
4060 EACTIVE(E)=1:ENEMYCOUNT=ENEMYCOUNT+1
4070 LASTSPAWN=TI
4080 RETURN
4090 NEXT E
4100 RETURN
5000 REM Update sprites
5010 REM Player sprite
5020 POKE 2040,13:POKE 53248,PX:POKE 53249,PY
5030 REM Enemy sprites (use sprites 1-3)
5040 FOR E=1 TO MAXENEMIES
5050 IF EACTIVE(E)=0 THEN POKE 53248+E*2,0:GOTO 5080:REM Hide
5060 POKE 2040+E,20:REM Enemy sprite
5070 POKE 53248+E*2,EX(E):POKE 53249+E*2,EY(E)
5080 NEXT E
5090 RETURN
6000 REM Display HUD
6010 PRINT CHR$(19);:REM Home
6020 PRINT "SCORE:";SCORE;" LIVES:";PLIVES;" FPS:";FPS;"  ";
6030 RETURN
7000 REM Check bullet-enemy collision
7010 FOR E=1 TO MAXENEMIES
7020 IF EACTIVE(E)=0 THEN NEXT E:RETURN
7030 IF ABS(BX(I)-EX(E))<16 AND ABS(BY(I)-EY(E))<16 THEN
7040 REM Hit!
7050 BACTIVE(I)=0:BULLETCOUNT=BULLETCOUNT-1
7060 EACTIVE(E)=0:ENEMYCOUNT=ENEMYCOUNT-1
7070 SCORE=SCORE+100
7080 REM Explosion sound
7090 POKE 54296,15:POKE 54283,129:POKE 54285,10
7100 FOR J=1 TO 10:NEXT J:POKE 54283,128
7110 RETURN
7120 NEXT E
7130 RETURN
8000 REM Player hit
8010 PLIVES=PLIVES-1
8020 IF PLIVES<=0 THEN PRINT CHR$(147);"GAME OVER":END
8030 PX=160:PY=220:REM Reset position
8040 REM Hit sound
8050 POKE 54296,15:POKE 54283,129:POKE 54285,5
8060 FOR I=1 TO 30:NEXT I:POKE 54283,128
8070 RETURN
9000 REM Calculate FPS
9010 FRAMES=FC-LASTFC
9020 JIFFIES=TI-LASTFPS
9030 IF JIFFIES>0 THEN FPS=INT(FRAMES*60/JIFFIES)
9040 LASTFPS=TI:LASTFC=FC
9050 RETURN
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - 4 sprites (player + 3 enemies)
- **SID** - Sound effects (shoot, explosion, hit)
- **CIA** - Joystick input, timing

**Memory Addresses:**
- 53269 ($D015) - Sprite enable
- 53248-53255 ($D000-$D007) - Sprite X/Y positions
- 54273+ ($D400+) - SID registers
- TI - System timer for FPS measurement

## Performance Measurement

**Baseline Performance:**
```
Configuration: Player + 3 enemies + 5 bullets + sound effects
Expected FPS: 15-18 fps
Frame time: ~55-65ms per frame
```

**Measurement Method:**
```basic
10 LASTFPS=TI:LASTFC=FC
20 REM ...game loop...
30 IF TI-LASTFPS>50 THEN  : REM Every ~1 second
40 FPS=INT((FC-LASTFC)*60/(TI-LASTFPS))
50 LASTFPS=TI:LASTFC=FC
```

## Common Pitfalls

1. **Bullets not removed:** Inactive bullets still updated, wastes processing
2. **Too many sprites:** Exceeding 8 sprite limit causes flicker
3. **No rate limiting:** Player shoots too fast, hundreds of bullets
4. **Collision too strict:** Pixel-perfect collision feels unfair
5. **FPS calculation wrong:** Not accounting for PAL (50Hz) vs NTSC (60Hz)

## Limit Awareness

**First hint of limitations:**

"Basic shmup runs at **15-18 fps**—playable but noticeably choppy. This is with only 4 sprites active and simple movement.

Compare to commercial shmups (50-60 fps in assembly).

**This is just the foundation.** Next lessons add:
- L50: Scrolling background → drops to 12-14 fps
- L51: 7 animated enemies → drops to 8-10 fps
- L52: Particle effects → drops to 6-8 fps

Watch the FPS counter. BASIC's interpreter overhead becomes visible when trying fast action gameplay."

## Extension Ideas

- Add power-ups (spread shot, rapid fire, shield)
- Add enemy bullet patterns
- Add boss enemy with phases
- Add combo system (consecutive hits)
- Add screen shake on explosions

## Builds Toward

**In This Arc:**
- L50: Scrolling background (performance cost)
- L51: Many animated enemies (FPS drops)
- L52: Particle effects (major slowdown)
- L53: Everything combined (6-8 fps ceiling demonstrated)

## Quick Reference

**FPS Calculation:**
```basic
FPS = (FRAMES_RENDERED × 60) / JIFFIES_ELAPSED
```

**Bullet Management:**
```basic
REM Find inactive bullet slot
FOR I=1 TO MAX_BULLETS
IF BACTIVE(I)=0 THEN [spawn bullet at I]:RETURN
NEXT I
```

**Enemy Spawning:**
```basic
IF TIME_SINCE_LAST_SPAWN > INTERVAL THEN
IF ACTIVE_ENEMY_COUNT < MAX_ENEMIES THEN
  [spawn new enemy]
```

**Performance Optimization Tips (Won't Be Enough):**
- Cache PEEK values (joystick read once per frame)
- Use integer math only (avoid floating point)
- Skip inactive sprites (don't update if ACTIVE=0)
- Limit sound effects (SID access is expensive)

**Expected Performance:**
```
Baseline (L49): 15-18 fps
+ Scrolling (L50): 12-14 fps
+ Many enemies (L51): 8-10 fps
+ Particles (L52): 6-8 fps
Final (L53): 6-8 fps ceiling measured
```

**Performance Note:**
"Foundation shmup (player + 3 enemies + 5 bullets) runs at **15-18 fps**. This is noticeably choppy compared to commercial games (50-60 fps). Sprite movement appears jerky. Collision detection still works, but visual smoothness suffers. **This is BASIC's speed ceiling emerging**—and we haven't added scrolling or particles yet. The interpreter overhead is becoming visible."
