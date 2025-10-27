# Lesson 031: Multi-Screen Levels

**Arc:** Platform Game
**Position:** Lesson 4 of 5 in arc
**Type:** Standard
**Estimated Completion:** 140 lines of code

## Learning Objectives
- Create multiple level screens
- Implement screen transitions
- Store level data compactly
- Load and display different levels

## Prerequisites
- Character-based maps (L19)
- Platform collision (L29)
- Level data management

## Key Concepts
**Screen-Sized Levels** - 32×22 maps fit exactly on screen
**DATA Storage** - Compact level representation
**Screen Transitions** - Instant or scrolling between screens
**Level Progression** - Move to next screen when reaching edge/exit

## Code Pattern
```basic
10 REM Multi-screen platformer demo
20 DIM map(31,21)
30 LET currentLevel=1
40 REM Level data pointers
50 REM Initialize player
60 LET plx=2: LET ply=18
70 LET vx=0: LET vy=0
80 LET gravity=1: LET jumpSpeed=-5
90 GOSUB 2000: REM Load level 1
100 REM Main loop
110 REM Input
120 LET k$=INKEY$
130 LET vx=0
140 IF k$="q" THEN LET vx=-1
150 IF k$="w" THEN LET vx=1
160 IF k$=" " AND onGround=1 THEN LET vy=jumpSpeed: LET onGround=0
170 REM Physics (from L28-29)
180 LET vy=vy+gravity
190 IF vy>3 THEN LET vy=3
200 REM Horizontal movement with collision
210 LET nx=plx+vx
220 IF nx>=0 AND nx<=31 THEN IF map(nx,ply)=0 THEN LET plx=nx
230 REM Vertical movement with collision
240 LET ny=ply+vy
250 LET onGround=0
260 IF map(plx,ny)=0 THEN LET ply=ny ELSE IF vy>0 THEN LET vy=0: LET onGround=1
270 REM Ground detection
280 IF map(plx,ply+1)<>0 THEN LET onGround=1
290 REM Check for level exit
300 IF map(plx,ply)=9 THEN GOSUB 3000: REM Level complete
310 REM Render
320 CLS
330 FOR y=0 TO 21
340   FOR x=0 TO 31
350     LET t=map(x,y)
360     IF t=1 THEN INK 7: PRINT AT y,x;CHR$ 145: REM Wall
370     IF t=9 THEN INK 6: PRINT AT y,x;CHR$ 149: REM Exit
380   NEXT x
390 NEXT y
400 REM Draw player
410 INK 2: PRINT AT ply,plx;CHR$ 144
420 REM UI
430 PRINT AT 0,0;"Level ";currentLevel
440 REM Frame delay
450 FOR d=1 TO 15: NEXT d
460 GO TO 110
2000 REM =====================================
2010 REM LOAD LEVEL
2020 REM =====================================
2030 IF currentLevel=1 THEN RESTORE 5000
2040 IF currentLevel=2 THEN RESTORE 6000
2050 IF currentLevel=3 THEN RESTORE 7000
2060 REM Read map dimensions (always 32×22 for ZX)
2070 READ w,h
2080 REM Read tile data
2090 FOR y=0 TO 21
2100   FOR x=0 TO 31
2110     READ map(x,y)
2120   NEXT x
2130 NEXT y
2140 REM Read spawn point
2150 READ plx,ply
2160 LET vx=0: LET vy=0: LET onGround=0
2170 RETURN
3000 REM =====================================
3010 REM LEVEL COMPLETE
3020 REM =====================================
3030 LET currentLevel=currentLevel+1
3040 IF currentLevel>3 THEN GO TO 4000: REM Game complete
3050 REM Load next level
3060 GOSUB 2000
3070 RETURN
4000 REM =====================================
4010 REM GAME COMPLETE
4020 REM =====================================
4030 CLS
4040 PRINT AT 10,8;"CONGRATULATIONS!"
4050 PRINT AT 12,6;"You completed all levels!"
4060 PAUSE 0
4070 STOP
5000 REM =====================================
5010 REM LEVEL 1 DATA
5020 REM =====================================
5030 DATA 32,22
5040 REM Row 0 (top border)
5050 DATA 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
5060 REM Rows 1-19 (interior)
5070 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5080 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5090 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5100 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5110 DATA 1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5120 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5130 DATA 1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5140 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5150 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1
5160 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5170 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5180 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5190 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5200 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5210 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5220 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5230 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5240 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,1
5250 DATA 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
5260 REM Row 20 (ground)
5270 DATA 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
5280 REM Row 21 (bottom border)
5290 DATA 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
5300 REM Spawn point
5310 DATA 2,18
5320 RETURN
6000 REM Level 2 DATA (similar structure)
7000 REM Level 3 DATA (similar structure)
```

## Hardware
**Memory:** 3 levels × 704 bytes = 2.1KB of DATA
**Performance:** Loading level = ~500ms (acceptable for transition)

## Common Pitfalls
1. **Wrong RESTORE pointer:** Loading wrong level data
2. **Not resetting player state:** Velocity carries over between levels
3. **No bounds checking:** Reading past DATA causes crash
4. **Hardcoded level count:** Add level properly or game breaks

## Extension Ideas
- Scrolling transitions between screens
- Save/load system (tape or disk)
- Level editor (create DATA from play mode)
- Compressed level format (RLE)

## Builds Toward
- L32: Complete platformer with all features

## Quick Reference
### Level DATA Format
```basic
REM Level structure:
DATA width,height          REM Always 32,22 for ZX
DATA tile,tile,...         REM width×height tiles
DATA spawnX,spawnY         REM Player start position
```

### Loading Pattern
```basic
IF level=N THEN RESTORE levelNData
READ w,h
FOR y=0 TO h-1
  FOR x=0 TO w-1
    READ map(x,y)
  NEXT x
NEXT y
READ spawnX,spawnY
```

---

**Version:** 1.0
**Created:** 2025-10-27
