# Lesson 030: Moving Platforms

**Arc:** Platform Game
**Position:** Lesson 3 of 5 in arc
**Type:** Standard
**Estimated Completion:** 150 lines of code

## Learning Objectives
- Create moving platform entities
- Implement player-on-platform physics
- Handle different platform movement patterns
- Manage platform collision separately from static tiles

## Prerequisites
- Gravity and jumping (L28)
- Platform collision (L29)
- Multiple entities (L23)

## Key Concepts
**Platform Entity** - Moving object player can stand on
**Rider Detection** - Check if player position matches platform
**Inherited Velocity** - Player moves with platform
**Pattern Movement** - Horizontal slide, vertical lift, circular

## Code Pattern
```basic
10 REM Moving platforms demo
20 REM Platform arrays
30 DIM px(5),py(5),pvx(5),pvy(5),pa(5),pdir(5)
40 REM px/py=position, pvx/pvy=velocity, pa=active, pdir=direction
50 LET maxP=5
60 REM Initialize platforms
70 LET px(1)=10: LET py(1)=15: LET pvx(1)=1: LET pvy(1)=0: LET pa(1)=1
80 LET px(2)=20: LET py(2)=12: LET pvx(2)=0: LET pvy(2)=1: LET pa(2)=1
90 REM Player state
100 LET plx=5: LET ply=10
110 LET vx=0: LET vy=0
120 LET gravity=1: LET jumpSpeed=-5
130 LET onGround=0: LET onPlatform=-1: REM -1=no platform
140 REM Main loop
150 REM Input
160 LET k$=INKEY$
170 LET vx=0
180 IF k$="q" THEN LET vx=-1
190 IF k$="w" THEN LET vx=1
200 IF k$=" " AND onGround=1 THEN LET vy=jumpSpeed: LET onGround=0: LET onPlatform=-1
210 REM Update platforms
220 FOR i=1 TO maxP
230   IF pa(i)=0 THEN GO TO 300
240   REM Move platform
250   LET px(i)=px(i)+pvx(i)
260   LET py(i)=py(i)+pvy(i)
270   REM Bounce at boundaries (horizontal)
280   IF px(i)<5 OR px(i)>25 THEN LET pvx(i)=-pvx(i)
290   REM Bounce at boundaries (vertical)
295   IF py(i)<8 OR py(i)>18 THEN LET pvy(i)=-pvy(i)
300 NEXT i
310 REM Apply gravity
320 LET vy=vy+gravity
330 IF vy>3 THEN LET vy=3
340 REM Horizontal movement
350 LET plx=plx+vx
360 IF plx<1 THEN LET plx=1
370 IF plx>30 THEN LET plx=30
380 REM Vertical movement
390 LET ply=ply+vy
400 REM Platform collision
410 LET onGround=0: LET onPlatform=-1
420 FOR i=1 TO maxP
430   IF pa(i)=0 THEN GO TO 510
440   REM Check if player landing on platform
450   IF vy>=0 AND plx=px(i) AND ply=py(i)-1 THEN GOSUB 1000
460 510 NEXT i
470 REM Ground collision (static)
480 IF ply>=20 THEN LET ply=20: LET vy=0: LET onGround=1: LET onPlatform=-1
490 REM Render
500 CLS
510 REM Draw ground
520 FOR x=0 TO 31: PRINT AT 20,x;CHR$ 145: NEXT x
530 REM Draw platforms
540 FOR i=1 TO maxP
550   IF pa(i)=1 THEN INK 3: PRINT AT py(i),px(i);CHR$ 146
560 NEXT i
570 REM Draw player
580 INK 6: PRINT AT ply,plx;CHR$ 144
590 REM Debug info
600 PRINT AT 0,0;"OnPlat:";onPlatform;" OnGrd:";onGround
610 REM Frame delay
620 FOR d=1 TO 15: NEXT d
630 GO TO 150
1000 REM Player landed on platform i
1010 LET ply=py(i)-1
1020 LET vy=0
1030 LET onGround=1
1040 LET onPlatform=i
1050 REM Inherit platform velocity
1060 LET plx=plx+pvx(i)
1070 LET ply=ply+pvy(i)
1080 RETURN
```

## Hardware
**Performance:** 5 platforms + player physics = ~5ms per frame
**Memory:** 5 platforms × 5 vars × 2 bytes = 50 bytes

## Common Pitfalls
1. **Player doesn't move with platform:** Forgetting to add platform velocity
2. **Jittery riding:** Adding velocity every frame instead of only when standing
3. **Falling through moving platform:** Not checking platform collision
4. **Platform pushes player through ceiling:** Need boundary checks

## Extension Ideas
- Crumbling platforms (break after standing time)
- Springboard platforms (launch player upward)
- Disappearing platforms (on/off timer)
- Rotating platforms (circular paths)

## Builds Toward
**In This Arc:**
- L31: Multi-screen levels with scrolling
- L32: Complete platformer synthesis

## Quick Reference
### Platform Movement Patterns
```basic
REM Horizontal slider
LET pvx=1: LET pvy=0
IF px<minX OR px>maxX THEN LET pvx=-pvx

REM Vertical lift
LET pvx=0: LET pvy=1
IF py<minY OR py>maxY THEN LET pvy=-pvy

REM Circular (simple)
LET angle=angle+5
LET px=centerX+INT(radius*COS(angle))
LET py=centerY+INT(radius*SIN(angle))
```

### Rider Physics
```basic
REM Check if player on platform i:
IF plx=px(i) AND ply=py(i)-1 THEN
  LET onPlatform=i
  LET ply=py(i)-1  REM Snap to platform
  LET vy=0
  LET onGround=1
  REM Inherit velocity
  LET plx=plx+pvx(i)
  LET ply=ply+pvy(i)
END IF
```

---

**Version:** 1.0
**Created:** 2025-10-27
