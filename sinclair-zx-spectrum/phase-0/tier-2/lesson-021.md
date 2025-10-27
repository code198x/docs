# Lesson 021: Maze Game Synthesis

**Arc:** UDG Graphics System
**Position:** Lesson 5 of 5 in arc (DELIVERABLE)
**Type:** Synthesis
**Estimated Completion:** 250-300 lines of code

## Learning Objectives
- Synthesize UDG, maps, attributes, and input
- Create complete playable maze game
- Implement win condition and game loop
- Deliver polished, full-featured game

## Prerequisites
- All Arc 1 lessons (L17-20)
- Input handling (Tier 1)
- Game loop structure (Tier 1)

## Key Concepts
**Complete Game Structure** - Title → Gameplay → Win/Lose → Restart
**Collision Detection** - Check tile type before moving
**Collectible System** - Keys, gems, or dots to collect
**Win Condition** - Reach exit after collecting items

## Code Pattern
```basic
10 REM Maze Game - Complete Synthesis
20 LET base=USR "a"
30 REM Define tiles: 0=empty, 1=wall, 2=key, 3=exit
40 FOR t=0 TO 3
50   FOR r=0 TO 7
60     READ byte
70     POKE base+t*8+r,byte
80   NEXT r
90 NEXT t
100 DATA 0,0,0,0,0,0,0,0: REM Empty
110 DATA 255,255,255,255,255,255,255,255: REM Wall
120 DATA 60,66,165,129,165,153,66,60: REM Key
130 DATA 24,36,66,129,129,66,36,24: REM Exit
140 REM Map (20×16, simplified)
150 DIM map(31,21)
160 FOR y=0 TO 21
170   FOR x=0 TO 31
180     READ map(x,y)
190   NEXT x
200 NEXT y
210 DATA 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
220 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
230 REM ... more map data ...
240 REM Player state
250 LET px=2: LET py=2: REM Start position
260 LET keys=0: LET totalKeys=3
270 REM Draw map
280 GOSUB 1000
290 REM Main loop
300 LET k$=INKEY$
310 LET nx=px: LET ny=py
320 IF k$="q" THEN LET nx=px-1
330 IF k$="w" THEN LET nx=px+1
340 IF k$="a" THEN LET ny=py-1
350 IF k$="z" THEN LET ny=py+1
360 REM Collision check
370 LET tile=map(nx,ny)
380 IF tile=1 THEN GO TO 300: REM Wall, don't move
390 IF tile=2 THEN LET keys=keys+1: LET map(nx,ny)=0: REM Collect key
400 IF tile=3 AND keys=totalKeys THEN GO TO 2000: REM Win!
410 IF tile=3 AND keys<totalKeys THEN GO TO 300: REM Need more keys
420 REM Move player
430 PRINT AT py,px;" ": REM Erase old position
440 LET px=nx: LET py=ny
450 INK 6: PRINT AT py,px;CHR$ 144: REM Draw player
460 PRINT AT 0,0;"Keys: ";keys;"/";totalKeys
470 GO TO 300
1000 REM Draw map subroutine
1010 CLS
1020 FOR y=0 TO 21
1030   FOR x=0 TO 31
1040     LET t=map(x,y)
1050     IF t>0 THEN PRINT AT y,x;CHR$ (143+t)
1060   NEXT x
1070 NEXT y
1080 RETURN
2000 REM Win screen
2010 CLS
2020 PRINT AT 10,10;"YOU WIN!"
2030 PRINT AT 12,8;"Press any key"
2040 PAUSE 0
2050 STOP
```

## Hardware
**Memory:**
- 32×22 map = 704 bytes
- 4 UDGs = 32 bytes
- Code + variables = ~2KB
- Total: < 3KB (fits easily in 48K)

**Performance:**
- Full map redraw: ~200ms (only at start)
- Per-frame updates: instant (only 2-3 characters)

## Extension Ideas
- Multiple maze levels
- Enemies with simple AI
- Time limit with countdown
- Score system
- Sound effects (BEEP)

## Builds Toward
**Next Arc:**
- Fast sprite movement (Arc 2)
- Multiple moving objects
- Arcade-style games

---

**Version:** 1.0
**Created:** 2025-10-27
**Note:** This is the DELIVERABLE for Arc 1. Students create a complete, playable maze game demonstrating mastery of UDG graphics, character maps, and attribute management.
