# Lesson 029: Platform and Wall Collision

**Arc:** Platform Game
**Position:** Lesson 2 of 5 in arc
**Type:** Standard
**Estimated Completion:** 130 lines of code

## Learning Objectives
- Detect collision with platform tiles
- Implement wall collision (left/right)
- Handle ceiling collision
- Integrate collision with gravity system

## Prerequisites
- Gravity and jumping (L28)
- Character-based maps (L19)
- Tile collision concepts

## Key Concepts
**Tile Collision** - Check map array at player position
**Four-Direction Checks** - Test movement before applying
**Solid vs Empty** - Different tile types (0=empty, 1+=solid)
**Collision Response** - Stop movement, set velocity to zero

## Code Pattern
```basic
10 REM Platform collision demo
20 REM Map array (20×22)
30 DIM map(31,21)
40 REM Initialize simple level
50 FOR y=0 TO 21
60   FOR x=0 TO 31
70     LET map(x,y)=0: REM Empty by default
80     IF y=20 THEN LET map(x,y)=1: REM Ground
90     IF x=0 OR x=31 THEN LET map(x,y)=1: REM Walls
100   NEXT x
110 NEXT y
120 REM Add some platforms
130 FOR x=5 TO 10: LET map(x,15)=1: NEXT x
140 FOR x=15 TO 20: LET map(x,12)=1: NEXT x
150 REM Player state (from L28)
160 LET px=5: LET py=10
170 LET vx=0: LET vy=0
180 LET gravity=1: LET jumpSpeed=-5
190 LET onGround=0
200 REM Main loop
210 REM Input
220 LET k$=INKEY$
230 LET vx=0
240 IF k$="q" THEN LET vx=-1
250 IF k$="w" THEN LET vx=1
260 IF k$=" " AND onGround=1 THEN LET vy=jumpSpeed: LET onGround=0
270 REM Apply gravity
280 LET vy=vy+gravity
290 IF vy>3 THEN LET vy=3
300 REM Horizontal movement with collision
310 LET nx=px+vx
320 REM Check left/right collision
330 IF map(nx,py)=0 THEN LET px=nx: REM Move if empty
340 IF map(nx,py)<>0 THEN LET vx=0: REM Stop if solid
350 REM Vertical movement with collision
360 LET ny=py+vy
370 LET onGround=0
380 REM Check downward collision (landing)
390 IF vy>0 AND map(px,ny)<>0 THEN LET py=ny-1: LET vy=0: LET onGround=1: GO TO 450
400 REM Check upward collision (ceiling)
410 IF vy<0 AND map(px,ny)<>0 THEN LET vy=0: GO TO 450
420 REM No collision, move freely
430 IF map(px,ny)=0 THEN LET py=ny
440 REM Check if standing on solid tile (ground detection)
450 IF map(px,py+1)<>0 THEN LET onGround=1
460 REM Render
470 CLS
480 REM Draw map
490 FOR y=0 TO 21
500   FOR x=0 TO 31
510     IF map(x,y)>0 THEN INK 7: PRINT AT y,x;CHR$ 145
520   NEXT x
530 NEXT y
540 REM Draw player
550 INK 6: PRINT AT py,px;CHR$ 144
560 REM Frame delay
570 FOR d=1 TO 15: NEXT d
580 GO TO 210
```

## Hardware
**Performance:**
- Collision checks: ~3-5 array lookups per frame (~1ms)
- Map rendering: ~200ms (only at level start, not every frame)
- Total per-frame cost: negligible

**Memory:** 32×22 array = 704 bytes

## Common Pitfalls
1. **Testing after movement:** Check BEFORE moving, not after
2. **Wrong tile coordinates:** Integer division issues (px vs INT(px))
3. **Falling through floors:** Not detecting ground properly
4. **Stuck in walls:** Moving into solid tile without check

## Extension Ideas
- One-way platforms (can jump up through)
- Slippery surfaces (ice physics)
- Ladders (climb up/down)
- Breakable tiles

## Builds Toward
**In This Arc:**
- L30: Moving platforms
- L31: Multi-screen levels
- L32: Complete platformer

## Quick Reference
### Collision Check Pattern
```basic
REM Before horizontal movement:
LET nx=px+vx
IF map(nx,py)=0 THEN LET px=nx  REM Move if empty
IF map(nx,py)<>0 THEN LET vx=0  REM Stop if solid

REM Before vertical movement:
LET ny=py+vy
IF map(px,ny)=0 THEN LET py=ny  REM Move if empty
IF map(px,ny)<>0 AND vy>0 THEN LET vy=0: LET onGround=1  REM Land
IF map(px,ny)<>0 AND vy<0 THEN LET vy=0  REM Hit ceiling
```

### Ground Detection
```basic
REM After movement, check tile below:
IF map(px,py+1)<>0 THEN LET onGround=1 ELSE LET onGround=0
```

---

**Version:** 1.0
**Created:** 2025-10-27
