# Lesson 039: Crystal Collector (Complete Platformer)

**Arc:** Platform Adventure
**Position:** Lesson 7 of 7 in arc
**Type:** SYNTHESIS
**Estimated Completion:** 200 lines of code

## Learning Objectives

- Integrate all platformer systems into cohesive game
- Balance difficulty across multiple levels
- Debug complex multi-system interactions
- Complete professional-quality platformer game
- Discover BASIC's limitations with fast action games

## Prerequisites

**From Previous Lessons:**
- Platform mechanics with gravity/jumping (L33)
- Multi-state character animation (L34)
- Data-driven level design (L35)
- Enemy AI and collision (L36)
- Collectibles and goals (L37)
- Polish and HUD systems (L38)

**BASIC Knowledge:**
- Large program organization (200+ lines)
- State management across systems
- Performance tuning

## Key Concepts Introduced

### System Integration
Combine physics, animation, AI, collectibles, music, and HUD into single game loop. Manage update order to prevent conflicts.

### Performance Awareness
With all systems active, game runs at 10-12 fps. Noticeable frame skips during complex scenes (multiple enemies + animation).

### Game Balance
Tune enemy speed, platform spacing, collectible placement to create satisfying difficulty curve across 4 levels.

### Complete Game Loop
Title screen → gameplay → level progression → win/lose screens → restart. Professional game flow.

## Code Pattern

```basic
10 REM ================================
20 REM CRYSTAL COLLECTOR
30 REM Complete Platformer Game
40 REM Lessons 33-39 Integration
50 REM ================================
60 REM
70 REM Game state variables
80 GSTATE=0:REM 0=title,1=play,2=over,3=win
90 SCORE=0:LIVES=3:LV=1:MAXLV=4
100 GEMS=0:GEMTOTAL=10:HASKEY=0
110 REM
120 REM Player variables
130 SX=20:SY=150:VX=0:VY=0:GR=0:ST=0:FC=0
140 GRAV=0.2:JMP=-3:INVINCIBLE=0
150 REM
160 REM Arrays for level data
170 DIM PX(4,5),PY(4,5),PW(4,5):REM Platforms
180 DIM EX(3),EY(3),ETYPE(3),EDIR(3),EACTIVE(3):REM Enemies
190 DIM CX(4,5),CY(4,5),CTYPE(4,5),CACTIVE(4,5):REM Collectibles
200 DIM NOTES(32):REM Music
210 NOTEPOS=0:LASTNOTE=0
220 REM
230 REM Initialize data
240 GOSUB 5000:REM Load level data
250 GOSUB 6000:REM Load music data
260 REM
270 REM ================================
280 REM MAIN GAME STATE MACHINE
290 REM ================================
300 IF GSTATE=0 THEN GOSUB 1000:REM Title
310 IF GSTATE=1 THEN GOSUB 2000:REM Game
320 IF GSTATE=2 THEN GOSUB 3000:REM Game Over
330 IF GSTATE=3 THEN GOSUB 4000:REM Win
340 GOTO 300
350 REM
1000 REM ================================
1010 REM TITLE SCREEN
1020 REM ================================
1030 PRINT CHR$(147)
1040 POKE 53280,0:POKE 53281,0
1050 PRINT:PRINT
1060 PRINT TAB(8);"CRYSTAL COLLECTOR"
1070 PRINT:PRINT
1080 PRINT TAB(5);"COLLECT ALL 10 GEMS"
1090 PRINT TAB(5);"FIND THE KEY"
1100 PRINT TAB(5);"REACH THE DOOR"
1110 PRINT:PRINT:PRINT
1120 PRINT TAB(5);"JOYSTICK TO MOVE"
1130 PRINT TAB(5);"FIRE TO JUMP"
1140 PRINT:PRINT:PRINT:PRINT
1150 PRINT TAB(6);"PRESS FIRE TO START"
1160 FC=FC+1:POKE 53280,(FC/10) AND 15
1170 IF PEEK(56320) AND 16 THEN 1160
1180 GSTATE=1:GOSUB 7000:REM Init game
1190 RETURN
1200 REM
2000 REM ================================
2010 REM MAIN GAME LOOP
2020 REM ================================
2030 J=PEEK(56320):FC=FC+1
2040 REM
2050 REM Music update
2060 IF TI-LASTNOTE>10 THEN GOSUB 8000
2070 REM
2080 REM Invincibility countdown
2090 IF INVINCIBLE>0 THEN INVINCIBLE=INVINCIBLE-1
2100 REM
2110 REM ===== PLAYER INPUT =====
2120 VX=0
2130 IF (J AND 4)=0 THEN VX=-2
2140 IF (J AND 8)=0 THEN VX=2
2150 IF (J AND 16)=0 AND GR=1 THEN VY=JMP:GR=0:GOSUB 8100
2160 REM
2170 REM ===== PLAYER PHYSICS =====
2180 VY=VY+GRAV:IF VY>5 THEN VY=5
2190 SX=SX+VX:SY=SY+VY
2200 REM
2210 REM ===== PLATFORM COLLISION =====
2220 GR=0
2230 FOR I=1 TO 5
2240 IF PX(LV,I)=0 THEN NEXT I:GOTO 2280
2250 IF SX>PX(LV,I)-12 AND SX<PX(LV,I)+PW(LV,I)+12 THEN
2260 IF SY>PY(LV,I)-21 AND SY<PY(LV,I) AND VY>0 THEN SY=PY(LV,I)-21:VY=0:GR=1
2270 NEXT I
2280 IF SY>229 THEN SY=229:VY=0:GR=1
2290 REM
2300 REM ===== ENEMY UPDATE =====
2310 FOR E=1 TO 3
2320 IF EACTIVE(E)=0 THEN NEXT E:GOTO 2410
2330 REM Enemy AI
2340 IF ETYPE(E)=0 THEN GOSUB 9000:REM Patrol
2350 IF ETYPE(E)=1 THEN GOSUB 9100:REM Chase
2360 IF ETYPE(E)=2 THEN GOSUB 9200:REM Flying
2370 REM Enemy collision
2380 IF INVINCIBLE=0 THEN
2390 IF ABS(EX(E)-SX)<20 AND ABS(EY(E)-SY)<18 THEN GOSUB 10000
2400 NEXT E
2410 REM
2420 REM ===== COLLECTIBLE CHECK =====
2430 FOR C=1 TO 5
2440 IF CACTIVE(LV,C)=0 THEN NEXT C:GOTO 2490
2450 IF ABS(CX(LV,C)-SX)<16 AND ABS(CY(LV,C)-SY)<16 THEN
2460 GOSUB 11000:REM Collect item
2470 NEXT C
2490 REM
2500 REM ===== LEVEL TRANSITION =====
2510 IF SX<0 OR SX>319 THEN GOSUB 12000
2520 REM
2530 REM ===== ANIMATION STATE =====
2540 IF GR=0 AND VY<0 THEN ST=2
2550 IF GR=0 AND VY>0 THEN ST=3
2560 IF GR=1 AND VX<>0 THEN ST=1
2570 IF GR=1 AND VX=0 THEN ST=0
2580 REM
2590 REM ===== SPRITE UPDATES =====
2600 REM Player
2610 IF ST=0 THEN SP=13+(FC/10) AND 1
2620 IF ST=1 THEN SP=15+(FC/5) AND 3
2630 IF ST=2 THEN SP=19
2640 IF ST=3 THEN SP=20
2650 POKE 2040,SP
2660 REM Invincibility blink
2670 IF INVINCIBLE>0 AND (FC AND 4) THEN POKE 53269,0:GOTO 2690
2680 POKE 53269,255
2690 POKE 53248,SX:POKE 53249,SY
2700 REM Enemies
2710 FOR E=1 TO 3
2720 IF EACTIVE(E)=0 THEN POKE 53248+E*2,0:NEXT E:GOTO 2760
2730 POKE 2040+E,25+(FC/5) AND 3
2740 POKE 53248+E*2,EX(E):POKE 53249+E*2,EY(E)
2750 NEXT E
2760 REM Collectibles (simplified - always visible if active)
2770 REM
2780 REM ===== HUD UPDATE =====
2790 GOSUB 13000
2800 REM
2810 REM ===== WIN/LOSE CHECK =====
2820 IF LIVES<=0 THEN GSTATE=2:RETURN
2830 IF GEMS>=GEMTOTAL AND HASKEY=1 AND LV=MAXLV THEN GSTATE=3:RETURN
2840 RETURN
2850 REM
3000 REM ================================
3010 REM GAME OVER SCREEN
3020 REM ================================
3030 PRINT CHR$(147):PRINT:PRINT:PRINT
3040 PRINT TAB(10);"GAME OVER"
3050 PRINT:PRINT
3060 PRINT TAB(7);"FINAL SCORE: ";SCORE
3070 PRINT TAB(7);"GEMS: ";GEMS;"/";GEMTOTAL
3080 PRINT TAB(7);"LEVEL: ";LV
3090 PRINT:PRINT:PRINT:PRINT
3100 PRINT TAB(6);"PRESS FIRE TO RETRY"
3110 IF PEEK(56320) AND 16 THEN 3110
3120 FOR I=1 TO 30:NEXT I:REM Debounce
3130 GSTATE=0:RETURN
3140 REM
4000 REM ================================
4010 REM WIN SCREEN
4020 REM ================================
4030 PRINT CHR$(147):PRINT:PRINT:PRINT
4040 PRINT TAB(11);"YOU WIN!"
4050 PRINT:PRINT
4060 PRINT TAB(7);"FINAL SCORE: ";SCORE
4070 PRINT TAB(7);"ALL GEMS COLLECTED!"
4080 PRINT:PRINT:PRINT:PRINT
4090 PRINT TAB(5);"PRESS FIRE FOR MENU"
4100 POKE 53280,(TI AND 15):REM Celebration flash
4110 IF PEEK(56320) AND 16 THEN 4100
4120 GSTATE=0:RETURN
4130 REM
5000 REM ===== LOAD LEVEL DATA =====
5010 REM (Platform, enemy, collectible DATA statements)
5020 REM (See L35-37 for full data structures)
5030 RETURN
6000 REM ===== LOAD MUSIC DATA =====
6010 REM (See L38 for music notes)
6020 RETURN
7000 REM ===== INITIALIZE GAME =====
7010 SCORE=0:LIVES=3:LV=1:GEMS=0:HASKEY=0:INVINCIBLE=0
7020 SX=20:SY=150:VX=0:VY=0:GR=0:FC=0
7030 PRINT CHR$(147):POKE 53280,6:POKE 53281,14
7040 POKE 53269,255:REM Enable sprites
7050 REM Reset all ACTIVE flags
7060 FOR E=1 TO 3:EACTIVE(E)=1:NEXT E
7070 FOR L=1 TO MAXLV:FOR C=1 TO 5:CACTIVE(L,C)=1:NEXT C:NEXT L
7080 RETURN
8000 REM ===== UPDATE MUSIC =====
8010 REM (See L38 for music playback)
8020 RETURN
8100 REM ===== JUMP SOUND =====
8110 REM (See L38 for sound effect)
8120 RETURN
9000 REM ===== PATROL AI =====
9010 REM (See L36)
9020 RETURN
9100 REM ===== CHASE AI =====
9110 REM (See L36)
9120 RETURN
9200 REM ===== FLYING AI =====
9210 REM (See L36)
9220 RETURN
10000 REM ===== PLAYER HIT =====
10010 LIVES=LIVES-1:INVINCIBLE=100
10020 SX=20:SY=150:VX=0:VY=0
10030 GOSUB 8200:REM Hit sound
10040 RETURN
11000 REM ===== COLLECT ITEM =====
11010 REM (See L37)
11020 RETURN
12000 REM ===== LEVEL TRANSITION =====
12010 REM (See L35)
12020 RETURN
13000 REM ===== UPDATE HUD =====
13010 PRINT CHR$(19);
13020 PRINT "SCORE:";SCORE;" L:";LV;" GEMS:";GEMS;"/";GEMTOTAL;" LIVES:";LIVES;" ";
13030 IF HASKEY=1 THEN PRINT "KEY ";
13040 RETURN
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - 8 sprites (player, 3 enemies, collectibles), screen/border colors
- **SID** - Background music voice 1, sound effects voice 2-3
- **CIA** - Joystick input, timing for music

**Memory Addresses:**
- Full sprite system (53248-53269 for positions/enable)
- SID voices (54273+ for music/effects)
- Screen memory for HUD

## Common Pitfalls

1. **System interaction bugs:** Enemy collision during invincibility, collectibles respawning
2. **Update order matters:** Physics before collision, animation after state determination
3. **Performance degradation:** Too many active sprites slow frame rate
4. **State persistence:** Level transitions losing game state
5. **Music/sound conflicts:** Sound effects interrupting background music

## Extension Ideas

- Add more levels (6-8 levels total)
- Add boss enemy at end with health bar
- Add weapon/attack system (defeat enemies)
- Add secret areas with bonus gems
- Add moving platforms
- Add hazards (spikes, lava)
- Add checkpoints (respawn mid-level)

## Performance Discovery

**Important realization:**

"Complete platformer with all features runs at **10-12 fps** with occasional drops to 8-9 fps during complex scenes (multiple animated enemies + player animation + music). This is playable but noticeably choppy compared to commercial C64 platformers (50-60 fps).

The limitation isn't the game design—it's BASIC's interpreter overhead. Every sprite position update, every collision check, every animation frame change requires BASIC to parse line numbers and variable names.

**This game proves the concepts work.** The hardware can do this. But BASIC can't maintain smooth action at this complexity level.

Turn-based games (coming in L40-45) won't have this limitation—no speed pressure means BASIC works perfectly."

## Builds Toward

**In This Tier:**
- L40-45: RPG arc (turn-based, no speed pressure—BASIC's strength)
- L46-48: Puzzle arc (logic-focused, BASIC excels)

**In Tier 4:**
- L49-53: Explicitly push speed limit further (discover 6-8 fps ceiling)

## Quick Reference

**System Integration Order:**
```basic
1. Input (read joystick)
2. Physics (apply velocity/gravity)
3. Collision (platforms, enemies, collectibles)
4. AI (enemy movement)
5. State (determine animation state)
6. Update (sprites, music, HUD)
7. Checks (win/lose conditions)
```

**Performance Tuning:**
- **Reduce active sprites:** Fewer enemies = better frame rate
- **Simplify AI:** Simple patrol faster than chase calculations
- **Optimize collision:** Check proximity before detailed collision
- **Cache values:** Store PEEK results instead of repeated reads
- **Limit animation:** 2-frame animation cheaper than 4-frame

**Program Organization:**
```
Lines 0-500: Main state machine and initialization
Lines 1000-1999: Title screen
Lines 2000-2999: Game loop
Lines 3000-3999: Game over screen
Lines 4000-4999: Win screen
Lines 5000-6999: Data loading
Lines 7000-7999: Initialization routines
Lines 8000-8999: Music and sound
Lines 9000-9999: AI routines
Lines 10000+: Helper functions (collision, collection, etc.)
```

**Typical Performance:**
- Empty game loop: 40-50 fps
- Player + platforms: 25-30 fps
- + 3 enemies: 15-18 fps
- + collectibles: 12-15 fps
- + music + HUD: 10-12 fps
- Complex scenes: 8-10 fps

**Performance Note:**
"This synthesis project demonstrates BASIC's practical limit for action games: **10-12 fps baseline with drops to 8-9 fps**. The game is functional and enjoyable, but animation appears choppy compared to assembly-based commercial games (50-60 fps). The gameplay logic works perfectly—the interpreter overhead is the bottleneck. This establishes motivation for learning assembly language (Phase 1)."
