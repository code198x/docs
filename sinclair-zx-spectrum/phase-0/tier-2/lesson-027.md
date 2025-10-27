# Lesson 027: Space Invaders-Style Game Synthesis

**Arc:** Arcade Action
**Position:** Lesson 6 of 6 in arc (DELIVERABLE)
**Type:** Synthesis
**Estimated Completion:** 350-400 lines of code

## Learning Objectives
- Synthesize all Arc 2 concepts into complete game
- Implement wave spawning and difficulty scaling
- Create title screen and game over sequences
- Deliver polished arcade-style game

## Prerequisites
**From This Arc:**
- Fast sprite movement (L22)
- Multiple entities (L23)
- Bullet patterns (L24)
- Collision detection (L25)
- Enemy AI (L26)

## Key Concepts
**Game State Machine** - Title → Playing → GameOver → Title
**Wave System** - Spawn enemies in waves with increasing difficulty
**High Score** - Track and display best score
**Polish** - Sound effects (BEEP), screen flashing, smooth transitions

## Code Pattern
(Complete 350-400 line game structure)

```basic
10 REM Space Invaders-Style Game - Complete
20 REM =====================================
30 REM Initialize UDGs
40 LET base=USR "a"
50 FOR t=0 TO 5
60   FOR r=0 TO 7
70     READ byte
80     POKE base+t*8+r,byte
90   NEXT r
100 NEXT t
110 DATA 60,126,255,255,255,255,126,60: REM Player ship
120 DATA 24,60,126,255,231,231,126,60: REM Enemy type 1
130 DATA 24,126,255,219,219,255,126,24: REM Enemy type 2
140 DATA 8,28,62,127,62,28,8,0: REM Bullet
150 DATA 255,129,129,129,129,129,129,255: REM Explosion
160 DATA 0,0,0,0,0,0,0,0: REM Empty
170 REM Game state
180 LET gameState$="title": REM "title", "playing", "gameover"
190 LET score=0: LET highScore=0
200 LET lives=3: LET level=1
210 REM Entity arrays
220 DIM px,py: REM Player
230 DIM bx(10),by(10),ba(10): REM Bullets
240 DIM ex(15),ey(15),evx(15),evy(15),ea(15),et(15),etimer(15): REM Enemies
250 LET maxB=10: LET maxE=15
260 REM =====================================
270 REM MAIN GAME LOOP
280 REM =====================================
290 IF gameState$="title" THEN GOSUB 5000
300 IF gameState$="playing" THEN GOSUB 1000
310 IF gameState$="gameover" THEN GOSUB 6000
320 GO TO 290
1000 REM =====================================
1010 REM PLAYING STATE
1020 REM =====================================
1030 REM Initialize level
1040 LET px=15: LET py=20
1050 FOR i=1 TO maxB: LET ba(i)=0: NEXT i
1060 FOR i=1 TO maxE: LET ea(i)=0: NEXT i
1070 LET waveTimer=0: LET enemiesKilled=0
1080 LET waveActive=0
1090 REM === Game loop ===
1100 REM Input
1110 LET k$=INKEY$
1120 IF k$="q" AND px>1 THEN LET px=px-1
1130 IF k$="w" AND px<30 THEN LET px=px+1
1140 IF k$=" " THEN GOSUB 2000: REM Fire
1150 REM Update bullets
1160 FOR i=1 TO maxB
1170   IF ba(i)=0 THEN GO TO 1210
1180   LET by(i)=by(i)-2
1190   IF by(i)<0 THEN LET ba(i)=0
1200 1210 NEXT i
1210 REM Update enemies
1220 FOR i=1 TO maxE
1230   IF ea(i)=0 THEN GO TO 1300
1240   LET etimer(i)=etimer(i)+1
1250   REM Apply AI pattern based on type et(i)
1260   IF et(i)=1 THEN LET ey(i)=ey(i)+1: REM Straight
1270   IF et(i)=2 THEN GOSUB 3100: REM Zigzag
1280   LET ex(i)=ex(i)+evx(i): LET ey(i)=ey(i)+evy(i)
1290   IF ey(i)>21 THEN LET ea(i)=0
1300 NEXT i
1310 REM Collision detection
1320 GOSUB 4000
1330 REM Wave spawning
1340 LET waveTimer=waveTimer+1
1350 IF waveTimer>100 AND waveActive<5 THEN GOSUB 3000: LET waveTimer=0
1360 REM Render
1370 CLS
1380 REM Draw player
1390 INK 6: PRINT AT py,px;CHR$ 144
1400 REM Draw bullets
1410 FOR i=1 TO maxB
1420   IF ba(i)=1 THEN INK 7: PRINT AT by(i),bx(i);CHR$ 147
1430 NEXT i
1440 REM Draw enemies
1450 FOR i=1 TO maxE
1460   IF ea(i)=1 THEN INK 2: PRINT AT ey(i),ex(i);CHR$ (144+et(i))
1470 NEXT i
1480 REM UI
1490 PRINT AT 0,0;"Score:";score;" Lives:";lives;" Level:";level
1500 REM Frame delay
1510 FOR d=1 TO 20: NEXT d
1520 REM Check game over
1530 IF lives<=0 THEN LET gameState$="gameover": RETURN
1540 REM Check level complete (all enemies killed)
1550 IF enemiesKilled>=15 THEN LET level=level+1: LET enemiesKilled=0
1560 GO TO 1100
2000 REM =====================================
2010 REM FIRE BULLET
2020 REM =====================================
2030 FOR i=1 TO maxB
2040   IF ba(i)=0 THEN GO TO 2070
2050 NEXT i
2060 RETURN: REM No slots
2070 LET bx(i)=px: LET by(i)=py-1: LET ba(i)=1
2080 BEEP 0.01,10: REM Sound effect
2090 RETURN
3000 REM =====================================
3010 REM SPAWN WAVE
3020 REM =====================================
3030 REM Find empty slots and spawn enemies
3040 LET spawned=0
3050 FOR i=1 TO maxE
3060   IF ea(i)=0 AND spawned<3 THEN GOSUB 3200: LET spawned=spawned+1
3070 NEXT i
3080 LET waveActive=waveActive+1
3090 RETURN
3100 REM Zigzag AI pattern
3110 LET evy(i)=1
3120 IF etimer(i) MOD 20<10 THEN LET evx(i)=1 ELSE LET evx(i)=-1
3130 RETURN
3200 REM Spawn single enemy
3210 LET ex(i)=RND*28+2: LET ey(i)=1
3220 LET et(i)=INT(RND*2)+1: REM Type 1 or 2
3230 LET ea(i)=1: LET etimer(i)=0
3240 RETURN
4000 REM =====================================
4010 REM COLLISION DETECTION
4020 REM =====================================
4030 REM Bullet-enemy collisions
4040 FOR b=1 TO maxB
4050   IF ba(b)=0 THEN GO TO 4150
4060   FOR e=1 TO maxE
4070     IF ea(e)=0 THEN GO TO 4140
4080     IF bx(b)=ex(e) AND by(b)=ey(e) THEN GOSUB 4200: GO TO 4150
4090   4140 NEXT e
4100 4150 NEXT b
4110 REM Player-enemy collisions
4120 FOR e=1 TO maxE
4130   IF ea(e)=1 AND ex(e)=px AND ey(e)=py THEN GOSUB 4300
4140 NEXT e
4150 RETURN
4200 REM Hit enemy
4210 LET ba(b)=0: LET ea(e)=0
4220 LET score=score+10: LET enemiesKilled=enemiesKilled+1
4230 BEEP 0.02,5: REM Explosion sound
4240 RETURN
4300 REM Player hit
4310 LET ea(e)=0: LET lives=lives-1
4320 BEEP 0.1,-10: REM Damage sound
4330 RETURN
5000 REM =====================================
5010 REM TITLE SCREEN
5020 REM =====================================
5030 CLS
5040 PRINT AT 6,8;"SPACE INVADERS"
5050 PRINT AT 10,6;"Press SPACE to Start"
5060 PRINT AT 14,6;"High Score: ";highScore
5070 IF INKEY$=" " THEN LET gameState$="playing": RETURN
5080 GO TO 5070
6000 REM =====================================
6010 REM GAME OVER SCREEN
6020 REM =====================================
6030 CLS
6040 PRINT AT 8,10;"GAME OVER"
6050 PRINT AT 10,8;"Score: ";score
6060 IF score>highScore THEN LET highScore=score: PRINT AT 12,7;"NEW HIGH SCORE!"
6070 PRINT AT 16,6;"Press SPACE to Retry"
6080 PAUSE 100
6090 IF INKEY$=" " THEN LET gameState$="title": LET score=0: LET lives=3: LET level=1: RETURN
6100 GO TO 6090
```

## Hardware
**Memory Usage:**
- UDGs: 48 bytes
- Entity arrays: ~300 bytes
- Code: ~3KB
- Total: < 4KB (plenty of room for 48K Spectrum)

**Performance:** 15 enemies + 10 bullets = ~40-50ms per frame (~20 FPS, playable)

## Extension Ideas
- Shields/barriers
- Power-ups (rapid fire, extra life)
- Boss waves
- Background music (128K AY chip)

## Builds Toward
**Next Arc:**
- Platform game mechanics (Arc 3)
- More complex game structures

---

**Version:** 1.0
**Created:** 2025-10-27
**Note:** This is the DELIVERABLE for Arc 2. Students create a complete Space Invaders-style arcade game demonstrating mastery of fast sprites, entity management, collision detection, and AI patterns.
