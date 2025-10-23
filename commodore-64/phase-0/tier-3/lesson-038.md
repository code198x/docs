# Lesson 038: Polish & HUD

**Arc:** Platform Adventure
**Position:** Lesson 6 of 7 in arc
**Type:** Standard
**Estimated Completion:** 150 lines of code

## Learning Objectives

- Create professional title screen and menus
- Design informative HUD (heads-up display)
- Integrate sound effects and background music
- Add visual polish and player feedback
- Build complete game presentation

## Prerequisites

**From Previous Lessons:**
- Complete platformer mechanics (L33-37)
- Sound effects library (L27)
- Background music concepts (L26, L28)
- Screen memory manipulation (L8)

**BASIC Knowledge:**
- Menu systems with input handling
- Music playback during gameplay
- Visual feedback techniques

## Key Concepts Introduced

### Title Screen
Display game title, instructions, and "Press Fire" prompt. Wait for fire button, then start game. Includes animated elements.

### HUD Design
Top screen area shows persistent game info: score, lives, gems, keys. Updates every frame without flickering.

### Music Integration
Non-blocking background music plays during gameplay. Uses TI-based timing to update notes without pausing game loop.

### Visual Feedback
Particle effects for collection, screen flash for damage, sprite blink for invincibility. Communicates game state visually.

## Code Pattern

```basic
10 REM Game state: 0=title, 1=playing, 2=game over, 3=win
20 GSTATE=0
30 REM Game variables
40 SCORE=0:LIVES=3:GEMS=0:GEMTOTAL=10:HASKEY=0
50 INVINCIBLE=0:INVTIME=0
60 REM Player variables
70 SX=20:SY=150:VX=0:VY=0:GR=0:FC=0
80 REM Music variables
90 DIM NOTES(32):NOTEPOS=0:LASTNOTE=0
100 REM Initialize
110 GOSUB 9000:REM Setup music data
120 REM Main state machine
130 IF GSTATE=0 THEN GOSUB 1000:REM Title screen
140 IF GSTATE=1 THEN GOSUB 2000:REM Game loop
150 IF GSTATE=2 THEN GOSUB 3000:REM Game over
160 IF GSTATE=3 THEN GOSUB 4000:REM Win screen
170 GOTO 130
1000 REM Title screen
1010 PRINT CHR$(147):REM Clear screen
1020 POKE 53280,0:POKE 53281,0:REM Black background
1030 REM Draw title
1040 PRINT TAB(10);"CRYSTAL COLLECTOR"
1050 PRINT:PRINT
1060 PRINT TAB(5);"COLLECT ALL 10 GEMS"
1070 PRINT TAB(5);"FIND THE KEY"
1080 PRINT TAB(5);"REACH THE DOOR"
1090 PRINT:PRINT
1100 PRINT TAB(5);"JOYSTICK: MOVE"
1110 PRINT TAB(5);"FIRE: JUMP"
1120 PRINT:PRINT:PRINT
1130 PRINT TAB(8);"PRESS FIRE TO START"
1140 REM Animate title
1150 FC=FC+1
1160 POKE 53280,(FC/10) AND 15:REM Cycling border
1170 REM Wait for fire button
1180 IF PEEK(56320) AND 16 THEN 1150
1190 REM Start game
1200 GSTATE=1
1210 GOSUB 5000:REM Initialize game
1220 RETURN
2000 REM Main game loop
2010 J=PEEK(56320):FC=FC+1
2020 REM Update music
2030 IF TI-LASTNOTE>10 THEN GOSUB 6000
2040 REM Handle invincibility timer
2050 IF INVINCIBLE>0 THEN INVINCIBLE=INVINCIBLE-1
2060 REM Player movement
2070 VX=0
2080 IF (J AND 4)=0 THEN VX=-2
2090 IF (J AND 8)=0 THEN VX=2
2100 IF (J AND 16)=0 AND GR=1 THEN VY=-3:GR=0:GOSUB 7010
2110 REM Physics
2120 VY=VY+0.2
2130 SX=SX+VX:SY=SY+VY
2140 REM Platform collision (simplified)
2150 GR=0
2160 IF SY>200 THEN SY=200:VY=0:GR=1
2170 REM Collectible/enemy collision (from L36-37)
2180 REM [collision code here]
2190 REM Update sprites
2200 POKE 2040,13+(FC/5) AND 3
2210 POKE 53248,SX:POKE 53249,SY
2220 REM Invincibility blink
2230 IF INVINCIBLE>0 AND (FC AND 4) THEN POKE 53269,0:GOTO 2250
2240 POKE 53269,255:REM All sprites visible
2250 REM Update HUD
2260 GOSUB 8000
2270 REM Check game over
2280 IF LIVES<=0 THEN GSTATE=2:RETURN
2290 REM Check win condition
2300 IF GEMS>=GEMTOTAL AND HASKEY=1 AND SX>270 THEN GSTATE=3:RETURN
2310 RETURN
3000 REM Game over screen
3010 PRINT CHR$(147)
3020 PRINT:PRINT:PRINT
3030 PRINT TAB(10);"GAME OVER"
3040 PRINT:PRINT
3050 PRINT TAB(8);"FINAL SCORE: ";SCORE
3060 PRINT TAB(8);"GEMS: ";GEMS;"/";GEMTOTAL
3070 PRINT:PRINT:PRINT
3080 PRINT TAB(7);"PRESS FIRE TO RETRY"
3090 IF PEEK(56320) AND 16 THEN 3090
3100 GSTATE=0:REM Return to title
3110 RETURN
4000 REM Win screen
4010 PRINT CHR$(147)
4020 PRINT:PRINT:PRINT
4030 PRINT TAB(12);"YOU WIN!"
4040 PRINT:PRINT
4050 PRINT TAB(8);"FINAL SCORE: ";SCORE
4060 PRINT TAB(8);"GEMS: ";GEMS;"/";GEMTOTAL
4070 PRINT:PRINT:PRINT
4080 PRINT TAB(7);"PRESS FIRE FOR MENU"
4090 REM Celebration animation
4100 POKE 53280,(TI AND 15):REM Flashing border
4110 IF PEEK(56320) AND 16 THEN 4090
4120 GSTATE=0
4130 RETURN
5000 REM Initialize game
5010 SCORE=0:LIVES=3:GEMS=0:HASKEY=0:INVINCIBLE=0
5020 SX=20:SY=150:VX=0:VY=0:FC=0
5030 PRINT CHR$(147)
5040 POKE 53280,6:POKE 53281,14:REM Game colors
5050 REM Setup sprites, platforms, enemies, collectibles
5060 RETURN
6000 REM Update background music
6010 LASTNOTE=TI
6020 NOTEPOS=NOTEPOS+1
6030 IF NOTEPOS>32 THEN NOTEPOS=1
6040 IF NOTES(NOTEPOS)=0 THEN RETURN:REM Rest
6050 REM Play note
6060 POKE 54296,15:REM Volume
6070 POKE 54276,33:REM Attack/Decay
6080 POKE 54277,240:REM Sustain/Release
6090 HI=INT(NOTES(NOTEPOS)/256)
6100 LO=NOTES(NOTEPOS)-HI*256
6110 POKE 54273,LO:POKE 54274,HI
6120 POKE 54276,33:REM Trigger note
6130 RETURN
7000 REM Sound effects
7010 REM Jump sound
7020 POKE 54296,15:POKE 54278,17
7030 POKE 54280,10:FOR I=1 TO 5:NEXT I:POKE 54278,0
7040 RETURN
7050 REM Collect sound (from L37)
7060 POKE 54296,15:POKE 54276,17:POKE 54273,20
7070 FOR I=1 TO 10:NEXT I:POKE 54276,0
7080 RETURN
7090 REM Hit sound
7100 POKE 54296,15:POKE 54283,129:POKE 54285,5
7110 FOR I=1 TO 20:NEXT I:POKE 54283,128
7120 RETURN
8000 REM Update HUD
8010 PRINT CHR$(19);:REM Home cursor
8020 PRINT "SCORE:";SCORE;"  LIVES:";LIVES;"  GEMS:";GEMS;"/";GEMTOTAL;" ";
8030 IF HASKEY=1 THEN PRINT "KEY:YES ";
8040 IF HASKEY=0 THEN PRINT "KEY:NO  ";
8050 RETURN
9000 REM Initialize music data (simple melody)
9010 FOR I=1 TO 32:READ NOTES(I):NEXT I
9020 RETURN
9100 REM Music notes (C major scale pattern)
9110 DATA 268,301,319,358,402,451,477,0
9120 DATA 477,451,402,358,319,301,268,0
9130 DATA 268,319,358,402,268,319,358,402
9140 DATA 477,402,358,319,301,268,0,0
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Sprites, screen colors, border effects
- **SID** - Background music and sound effects simultaneously
- **CIA** - Joystick input, timing for music

**Memory Addresses:**
- 53280-53281 ($D020-$D021) - Border and background colors
- 54273-54295 ($D400-$D417) - SID chip (3 voices for music + effects)
- Screen memory - HUD display area

## Common Pitfalls

1. **HUD flicker:** PRINTing HUD every frame without CHR$(19) causes screen flicker
2. **Music stops gameplay:** Blocking music loops prevent game updates
3. **Sound effects interrupt music:** Not using separate SID voices
4. **Title screen unresponsive:** Not debouncing fire button (continues to game immediately)
5. **Invisible sprites:** Forgetting to restore sprite enable after blink effect

## Extension Ideas

- Add high score persistence (save to disk)
- Add difficulty selection (easy/normal/hard)
- Add pause menu (space bar to pause)
- Add particle systems for explosions
- Add screen shake on damage
- Add level transition animations

## Builds Toward

**In This Tier:**
- L39: Complete Crystal Collector game with all systems integrated

## Quick Reference

**State Machine Pattern:**
```basic
10 GSTATE=0:REM 0=title, 1=play, 2=gameover, 3=win
20 IF GSTATE=0 THEN GOSUB [title]
30 IF GSTATE=1 THEN GOSUB [game]
40 IF GSTATE=2 THEN GOSUB [gameover]
50 IF GSTATE=3 THEN GOSUB [win]
60 GOTO 20
```

**Non-Blocking Music:**
```basic
10 IF TI-LASTUPDATE>DELAY THEN GOSUB [update_music]
20 REM Game continues regardless of music timing
```

**HUD Without Flicker:**
```basic
10 PRINT CHR$(19);:REM Home (no clear)
20 PRINT "INFO  ";:REM Trailing spaces clear old text
30 REM Rest of game loop continues
```

**Invincibility Blink:**
```basic
10 IF INVINCIBLE>0 AND (FRAME_COUNT AND 4) THEN
20 POKE 53269,0:REM Hide sprites
30 ELSE
40 POKE 53269,255:REM Show sprites
```

**Screen Flash Effect:**
```basic
10 OLD_BG=PEEK(53281)
20 FOR I=1 TO 3
30 POKE 53281,2:FOR J=1 TO 10:NEXT J
40 POKE 53281,OLD_BG:FOR J=1 TO 10:NEXT J
50 NEXT I
```

**Title Screen Checklist:**
- Game title (large, centered)
- Brief instructions (controls, objective)
- "Press Fire to Start" with animation
- Credits (optional)
- Cyclic animation (colors, sprites) to show it's alive

**HUD Best Practices:**
- **Top line only:** Don't cover play area
- **Consistent position:** Always same place
- **Clear labels:** "SCORE:" not just number
- **Trailing spaces:** Clear old longer values
- **Minimal updates:** Only update changed values (optimization)

**Performance Note:**
"HUD updates via PRINT are expensive (20-30ms per update). Using screen memory POKEs is faster but more complex. Background music adds ~5% overhead. Sound effects (short duration) add negligible overhead. Complete polished game runs at 10-12 fps with all features."
