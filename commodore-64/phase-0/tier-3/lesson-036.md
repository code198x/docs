# Lesson 036: Enemies & AI

**Arc:** Platform Adventure
**Position:** Lesson 4 of 7 in arc
**Type:** Standard
**Estimated Completion:** 100 lines of code

## Learning Objectives

- Implement multiple enemy types with different AI behaviors
- Create patrol, chase, and flying enemy patterns
- Handle enemy-player collision detection
- Build enemy management system for platformers

## Prerequisites

**From Previous Lessons:**
- Platform mechanics with animation (L33-34)
- Level design with data-driven approach (L35)
- Sprite management (L17-23)
- Collision detection (L19)

**BASIC Knowledge:**
- Multiple sprite control
- AI state machines
- Distance calculations

## Key Concepts Introduced

### Enemy Types
Three distinct enemy behaviors: patrol (walks back and forth), chase (follows player), flying (circular pattern). Each type uses different AI logic.

### AI State Management
Each enemy tracks its own state (EST): direction, target position, behavior mode. Updated independently each frame.

### Multi-Sprite Collision
Check collision between player sprite and each enemy sprite. Use sprite coordinates and bounding boxes.

### Enemy Arrays
Store enemy data in parallel arrays: EX(enemy number), EY, ETYPE (0=patrol, 1=chase, 2=fly), EDIR (direction), EACTIVE (alive/dead).

## Code Pattern

```basic
10 REM Enemy system variables
20 EMAX=3:REM Maximum enemies
30 DIM EX(3),EY(3),ETYPE(3),EDIR(3),EACTIVE(3),EFRAME(3)
40 REM Player variables
50 SX=20:SY=150:VX=0:VY=0:GR=0:LIVES=3
60 GRAV=0.2:JMP=-3:FC=0
70 REM Platform setup (simplified)
80 PX=50:PY=200:PW=250
90 REM Initialize enemies
100 GOSUB 2000
110 REM Setup sprites (player + 3 enemies)
120 POKE 53269,15:REM Enable sprites 0-3
130 POKE 53287,1:POKE 53288,2:POKE 53289,10:POKE 53290,7
140 REM Main loop
150 J=PEEK(56320):FC=FC+1
160 REM Player movement
170 VX=0
180 IF (J AND 4)=0 THEN VX=-2
190 IF (J AND 8)=0 THEN VX=2
200 IF (J AND 16)=0 AND GR=1 THEN VY=JMP:GR=0
210 REM Player physics
220 VY=VY+GRAV
230 SX=SX+VX:SY=SY+VY
240 REM Platform collision
250 GR=0
260 IF SX>PX-12 AND SX<PX+PW+12 THEN
270 IF SY>PY-21 AND SY<PY AND VY>0 THEN SY=PY-21:VY=0:GR=1
280 IF SY>229 THEN SY=229:VY=0:GR=1
290 REM Update enemies
300 FOR E=1 TO EMAX
310 IF EACTIVE(E)=0 THEN NEXT E:GOTO 500
320 REM Enemy AI based on type
330 IF ETYPE(E)=0 THEN GOSUB 3000:REM Patrol AI
340 IF ETYPE(E)=1 THEN GOSUB 3100:REM Chase AI
350 IF ETYPE(E)=2 THEN GOSUB 3200:REM Flying AI
360 REM Animate enemy
370 EFRAME(E)=(EFRAME(E)+1) AND 3
380 POKE 2040+E,25+EFRAME(E)
390 REM Check collision with player
400 IF ABS(EX(E)-SX)<20 AND ABS(EY(E)-SY)<18 THEN GOSUB 4000
410 REM Update enemy sprite position
420 POKE 53248+E*2,EX(E)
430 POKE 53249+E*2,EY(E)
440 NEXT E
500 REM Update player sprite
510 POKE 2040,13+(FC/5) AND 3
520 POKE 53248,SX:POKE 53249,SY
530 GOTO 150
2000 REM Initialize enemies
2010 REM Enemy 1: Patrol at ground level
2020 EX(1)=100:EY(1)=PY-21:ETYPE(1)=0:EDIR(1)=1:EACTIVE(1)=1
2030 REM Enemy 2: Chase enemy
2040 EX(2)=200:EY(2)=PY-21:ETYPE(2)=1:EDIR(2)=1:EACTIVE(2)=1
2050 REM Enemy 3: Flying enemy
2060 EX(3)=150:EY(3)=100:ETYPE(3)=2:EDIR(3)=0:EACTIVE(3)=1
2070 RETURN
3000 REM Patrol AI (walks back and forth)
3010 EX(E)=EX(E)+EDIR(E)*2
3020 REM Turn around at boundaries
3030 IF EX(E)<PX OR EX(E)>PX+PW THEN EDIR(E)=-EDIR(E)
3040 RETURN
3100 REM Chase AI (follows player)
3110 IF SX>EX(E) THEN EX(E)=EX(E)+1.5
3120 IF SX<EX(E) THEN EX(E)=EX(E)-1.5
3130 REM Stay on platform
3140 IF EX(E)<PX THEN EX(E)=PX
3150 IF EX(E)>PX+PW THEN EX(E)=PX+PW
3160 RETURN
3200 REM Flying AI (circular pattern)
3210 EDIR(E)=EDIR(E)+5:IF EDIR(E)>=360 THEN EDIR(E)=0
3220 EX(E)=150+SIN(EDIR(E)*0.0174)*60:REM Circle radius 60
3230 EY(E)=100+COS(EDIR(E)*0.0174)*40:REM Ellipse for variety
3240 RETURN
4000 REM Player hit by enemy
4010 LIVES=LIVES-1
4020 IF LIVES=0 THEN PRINT CHR$(147);"GAME OVER":END
4030 REM Reset player position
4040 SX=20:SY=150:VX=0:VY=0
4050 RETURN
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Multiple sprite display (4 sprites: player + 3 enemies)
- **CIA** - Joystick input

**Memory Addresses:**
- 53269 ($D015) - Sprite enable register (bits 0-3 enabled)
- 2040-2043 ($07F8-$07FB) - Sprite pointers for player + enemies
- 53248-53255 ($D000-$D007) - X/Y positions for 4 sprites

## Common Pitfalls

1. **All enemies same behavior:** Forgetting to check ETYPE before AI routine
2. **Collision box too large:** 24×21 sprite bounds make hits feel unfair
3. **Enemy walks off platform:** Patrol AI needs boundary checks
4. **Chase enemy gets stuck:** Not handling equal X positions (SX=EX)
5. **Sprite overlap invisibility:** Multiple enemies at same position become invisible

## Extension Ideas

- Add enemy health (multiple hits to defeat)
- Add enemy death animation and respawn
- Add jumping enemies (apply gravity to ground enemies)
- Add shooting enemies (enemy bullets)
- Add boss enemy with multi-phase attack patterns
- Add enemy spawn points (enemies appear from off-screen)

## Builds Toward

**In This Tier:**
- L37: Collectibles that power up player vs enemies
- L38: Enemy-specific sound effects and reactions
- L39: Complete platformer with balanced enemy challenge

## Quick Reference

**Enemy Type Patterns:**
```basic
REM Patrol AI (back and forth)
10 EX=EX+EDIR*SPEED
20 IF EX<LEFTBOUND OR EX>RIGHTBOUND THEN EDIR=-EDIR

REM Chase AI (follow player)
10 IF PLAYER_X>EX THEN EX=EX+SPEED
20 IF PLAYER_X<EX THEN EX=EX-SPEED

REM Flying AI (circular)
10 ANGLE=ANGLE+SPEED
20 EX=CENTER_X+SIN(ANGLE)*RADIUS
30 EY=CENTER_Y+COS(ANGLE)*RADIUS
```

**Collision Detection:**
```basic
10 REM Sprite bounding boxes
20 PLAYER: SX±12, SY-21 to SY
30 ENEMY: EX±12, EY-21 to EY
40 REM Simple overlap check
50 IF ABS(EX-SX)<20 AND ABS(EY-SY)<18 THEN [collision]
```

**Enemy Array Structure:**
```
EX(n)      - Enemy X position
EY(n)      - Enemy Y position
ETYPE(n)   - 0=patrol, 1=chase, 2=fly
EDIR(n)    - Direction or angle
EACTIVE(n) - 0=dead, 1=alive
EFRAME(n)  - Animation frame counter
```

**AI Tuning Parameters:**
- Patrol speed: 1-2 pixels/frame (slower = easier)
- Chase speed: 1-1.5 pixels/frame (slower than player)
- Flying speed: 3-5 degrees/frame (rotation speed)
- Detection range: Chase activates when player within range

**Performance Note:**
"Three animated enemies + player (4 sprites total) runs smoothly at 12-15 fps. Each additional enemy adds collision checks and AI overhead. With 5-7 enemies, frame rate drops noticeably to 10-12 fps (sprite animation + AI calculations)."
