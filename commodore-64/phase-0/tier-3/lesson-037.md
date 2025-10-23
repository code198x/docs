# Lesson 037: Collectibles & Goals

**Arc:** Platform Adventure
**Position:** Lesson 5 of 7 in arc
**Type:** Standard
**Estimated Completion:** 120 lines of code

## Learning Objectives

- Implement collectible items (gems, keys, power-ups)
- Create goal system with locked doors and objectives
- Build item collection and inventory tracking
- Design win condition and level progression

## Prerequisites

**From Previous Lessons:**
- Platform mechanics (L33-34)
- Level design (L35)
- Enemy and collision systems (L36)
- Sprite management (L17-23)

**BASIC Knowledge:**
- Multiple sprite collision detection
- Inventory variables and flags
- Win condition logic

## Key Concepts Introduced

### Collectible System
Place collectible sprites (gems, keys) in levels. When player sprite overlaps collectible, increase counter and hide sprite.

### Inventory Flags
Track what player has collected: GEMS (count), HASKEY (0/1 flag), POWERUP (active/inactive). Affects gameplay and progression.

### Locked Doors
Place door sprites at level exit. Check if player has required item (HASKEY=1) before allowing passage.

### Goal Tracking
Track objectives (e.g., collect all 10 gems). Display progress. Trigger win condition when complete.

## Code Pattern

```basic
10 REM Game variables
20 GEMS=0:GEMTOTAL=10:HASKEY=0:POWERUP=0:LIVES=3
30 SCORE=0:LV=1:MAXLV=4
40 REM Player variables
50 SX=20:SY=150:VX=0:VY=0:GR=0
60 REM Collectible arrays (5 collectibles per level)
70 DIM CX(4,5),CY(4,5),CTYPE(4,5),CACTIVE(4,5)
80 REM Door position
90 DOORX=280:DOORY=150
100 REM Platform setup
110 PX=50:PY=200:PW=250
120 REM Initialize collectibles
130 GOSUB 2000
140 REM Setup sprites (player + collectibles + door)
150 POKE 53269,255:REM Enable sprites 0-7
160 POKE 53287,1:REM Player white
170 FOR I=1 TO 5:POKE 53287+I,7:NEXT I:REM Collectibles yellow
180 POKE 53293,2:REM Door red
190 REM Main loop
200 J=PEEK(56320):FC=FC+1
210 REM Player movement
220 VX=0
230 IF (J AND 4)=0 THEN VX=-2
240 IF (J AND 8)=0 THEN VX=2
250 IF (J AND 16)=0 AND GR=1 THEN VY=-3:GR=0
260 REM Player physics
270 VY=VY+0.2
280 SX=SX+VX:SY=SY+VY
290 REM Platform collision
300 GR=0
310 IF SX>PX-12 AND SX<PX+PW+12 THEN
320 IF SY>PY-21 AND SY<PY AND VY>0 THEN SY=PY-21:VY=0:GR=1
330 IF SY>229 THEN SY=229:VY=0:GR=1
340 REM Check collectible collection
350 FOR C=1 TO 5
360 IF CACTIVE(LV,C)=0 THEN NEXT C:GOTO 500
370 REM Check collision with collectible
380 IF ABS(CX(LV,C)-SX)<16 AND ABS(CY(LV,C)-SY)<16 THEN
390 GOSUB 3000:REM Collect item
400 NEXT C
500 REM Check door collision (if has key)
510 IF ABS(DOORX-SX)<20 AND ABS(DOORY-SY)<18 THEN
520 IF HASKEY=1 THEN GOSUB 4000:REM Enter door
530 REM Update collectible sprites
540 FOR C=1 TO 5
550 IF CACTIVE(LV,C)=0 THEN POKE 53248+C*2,0:GOTO 580
560 POKE 53248+C*2,CX(LV,C)
570 POKE 53249+C*2,CY(LV,C)
580 POKE 2040+C,30+CTYPE(LV,C):REM Sprite frames
590 NEXT C
600 REM Update door sprite
610 IF HASKEY=1 THEN POKE 2047,32:REM Open door sprite
620 IF HASKEY=0 THEN POKE 2047,31:REM Locked door sprite
630 POKE 53254,DOORX:POKE 53255,DOORY
640 REM Update player sprite
650 POKE 2040,13+(FC/5) AND 3
660 POKE 53248,SX:POKE 53249,SY
670 REM Display HUD
680 PRINT CHR$(19);:REM Home cursor
690 PRINT "GEMS:";GEMS;"/";GEMTOTAL;" ";
700 IF HASKEY=1 THEN PRINT "KEY:YES ";
710 IF HASKEY=0 THEN PRINT "KEY:NO  ";
720 PRINT "LIVES:";LIVES;" ";
730 REM Check win condition
740 IF GEMS>=GEMTOTAL AND HASKEY=1 THEN GOSUB 5000
750 GOTO 200
2000 REM Initialize collectibles for all levels
2010 FOR L=1 TO MAXLV
2020 FOR C=1 TO 5
2030 READ CX(L,C),CY(L,C),CTYPE(L,C)
2040 CACTIVE(L,C)=1
2050 NEXT C
2060 NEXT L
2070 RETURN
2100 REM Level 1 collectibles (3 gems, 1 key, 1 powerup)
2110 DATA 80,180,0, 140,160,0, 200,140,0, 260,180,1, 100,220,2
2120 REM Level 2 collectibles
2130 DATA 60,180,0, 120,160,0, 180,140,0, 240,160,0, 280,180,0
2140 REM Level 3 collectibles
2150 DATA 100,200,0, 150,180,0, 200,160,0, 250,140,0, 0,0,0
2160 REM Level 4 collectibles
2170 DATA 140,190,0, 180,170,0, 220,190,0, 0,0,0, 0,0,0
3000 REM Collect item (C = collectible index)
3010 IF CTYPE(LV,C)=0 THEN GEMS=GEMS+1:SCORE=SCORE+100
3020 IF CTYPE(LV,C)=1 THEN HASKEY=1:SCORE=SCORE+500
3030 IF CTYPE(LV,C)=2 THEN POWERUP=1:LIVES=LIVES+1
3040 CACTIVE(LV,C)=0:REM Hide collected item
3050 REM Play collection sound
3060 POKE 54296,15:REM Volume
3070 POKE 54276,17:REM Attack/Decay
3080 POKE 54273,20:REM Frequency high
3090 FOR I=1 TO 10:NEXT I
3100 POKE 54276,0:REM Sound off
3110 RETURN
4000 REM Enter door (level complete)
4010 LV=LV+1
4020 IF LV>MAXLV THEN GOSUB 5000:RETURN
4030 PRINT CHR$(147);"LEVEL ";LV
4040 SX=20:SY=150:VX=0:VY=0:HASKEY=0
4050 FOR I=1 TO 100:NEXT I:REM Pause
4060 RETURN
5000 REM Win game
5010 PRINT CHR$(147);"YOU WIN!"
5020 PRINT "GEMS COLLECTED: ";GEMS
5030 PRINT "FINAL SCORE: ";SCORE
5040 PRINT:PRINT "PRESS FIRE TO RESTART"
5050 IF PEEK(56320) AND 16 THEN 5050
5060 RUN:REM Restart game
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Multiple sprites (player, collectibles, door)
- **SID** - Collection sound effects
- **CIA** - Joystick input

**Memory Addresses:**
- 53269 ($D015) - Sprite enable (8 sprites active)
- 54273-54276 ($D400-$D404) - SID voice 1 for sound effects
- Screen memory - HUD display

## Common Pitfalls

1. **Collecting same item twice:** Not setting CACTIVE=0 after collection
2. **Door opens without key:** Not checking HASKEY before door entry
3. **Collectibles respawn:** Not persisting CACTIVE across level transitions
4. **Collision too precise:** Requiring pixel-perfect overlap frustrates players
5. **No feedback:** Silent collection feels unresponsive (needs sound/visual)

## Extension Ideas

- Add different collectible types (coins, health, weapons)
- Add collectible animations (rotating, bobbing)
- Add temporary power-ups (invincibility timer)
- Add combo system (consecutive collections = bonus)
- Add hidden collectibles (secret areas)
- Add collectible magnets (auto-collect nearby items)

## Builds Toward

**In This Tier:**
- L38: Polish with HUD improvements and collectible visual effects
- L39: Complete platformer with balanced collectible placement

## Quick Reference

**Collectible Type Codes:**
```
CTYPE:
0 = Gem (score + count toward goal)
1 = Key (unlocks door)
2 = Power-up (extra life or ability)
3 = Health (restore health points)
4 = Weapon (upgrade attack)
```

**Collection Pattern:**
```basic
10 FOR C=1 TO MAX_COLLECTIBLES
20 IF NOT CACTIVE(C) THEN NEXT C:GOTO [after loop]
30 IF ABS(CX(C)-PLAYER_X)<RANGE AND ABS(CY(C)-PLAYER_Y)<RANGE THEN
40 GOSUB [collect_item]
50 NEXT C
```

**Door Logic:**
```basic
10 REM Check door entry
20 IF PLAYER_AT_DOOR THEN
30 IF HAS_REQUIRED_ITEM THEN [proceed to next level]
40 IF NOT HAS_REQUIRED_ITEM THEN [show "locked" message]
```

**Win Condition Patterns:**
- **Collect all:** GEMS>=GEMTOTAL
- **Reach goal:** PLAYER_X near EXIT_X and HAS_KEY
- **Defeat boss:** BOSS_HP<=0 and AT_EXIT
- **Time limit:** COLLECTED_ALL and TIME_REMAINING>0

**HUD Display:**
```basic
10 PRINT CHR$(19);:REM Home cursor (no clear)
20 PRINT "GEMS:";COUNT;"/";TOTAL;" LIVES:";L;" SCORE:";S;"  ";
30 REM Trailing spaces clear old text
```

**Performance Note:**
"Eight sprites (player + 5 collectibles + door + enemy) with collision checks runs at 10-12 fps. Collectibles don't move, so no AI overhead. Most performance cost is sprite rendering and collision detection. Frame rate remains playable but animations appear slightly choppy."
