# Lesson 023: Multiple Moving Objects

**Arc:** Arcade Action
**Position:** Lesson 2 of 6 in arc
**Type:** Standard
**Estimated Completion:** 120 lines of code

## Learning Objectives
- Manage arrays of moving entities
- Update multiple sprites efficiently
- Handle entity lifecycle (spawn, update, remove)
- Optimize loops for ZX Spectrum performance

## Prerequisites
- Fast sprite movement (L22)
- Arrays and FOR loops (Tier 1)
- UDG graphics (L17)

## Key Concepts
**Entity Arrays** - Store position, velocity, active state per object
**Update Loop** - Process all active entities each frame
**Object Pool** - Reuse array slots instead of creating new ones
**Performance Budget** - ~10-15 active sprites max on ZX Spectrum

## Code Pattern
```basic
10 REM Multiple moving objects demo
20 DIM ex(10): DIM ey(10): DIM evx(10): DIM evy(10): DIM ea(10)
30 REM ex/ey=position, evx/evy=velocity, ea=active (0/1)
40 LET maxE=10: LET numActive=0
50 REM Initialize some enemies
60 FOR i=1 TO 5
70   LET ex(i)=RND*30: LET ey(i)=1
80   LET evx(i)=0: LET evy(i)=1
90   LET ea(i)=1: LET numActive=numActive+1
100 NEXT i
110 REM Main loop
120 REM Update all enemies
130 FOR i=1 TO maxE
140   IF ea(i)=0 THEN GO TO 240: REM Skip inactive
150   REM Move enemy
160   LET ex(i)=ex(i)+evx(i)
170   LET ey(i)=ey(i)+evy(i)
180   REM Boundary check (deactivate if off screen)
190   IF ey(i)>21 THEN LET ea(i)=0: LET numActive=numActive-1: GO TO 240
200   IF ex(i)<0 OR ex(i)>31 THEN LET ea(i)=0: LET numActive=numActive-1: GO TO 240
210   REM Draw enemy
220   INK 2: PRINT AT ey(i),ex(i);CHR$ 144
230   REM (In real game: erase previous position)
240 NEXT i
250 REM Spawn new enemy occasionally
260 IF numActive<5 AND RND>0.95 THEN GOSUB 1000
270 REM Frame delay
280 FOR d=1 TO 50: NEXT d
290 GO TO 120
1000 REM Spawn enemy subroutine
1010 REM Find empty slot
1020 FOR i=1 TO maxE
1030   IF ea(i)=0 THEN GO TO 1060
1040 NEXT i
1050 RETURN: REM No slots available
1060 REM Initialize enemy
1070 LET ex(i)=RND*30: LET ey(i)=1
1080 LET evx(i)=SGN(RND-0.5): LET evy(i)=1
1090 LET ea(i)=1: LET numActive=numActive+1
1100 RETURN
```

## Hardware
**Memory:**
- 10 entities × 5 variables × 2 bytes = 100 bytes
- 20 entities = 200 bytes (manageable)

**Performance:**
- Processing 10 entities: ~20-30ms per frame
- Processing 20 entities: ~40-60ms (still acceptable)
- ZX Spectrum can handle 10-15 moving sprites comfortably

## Common Pitfalls
1. **Processing inactive entities:** Always check active flag first
2. **Array bounds:** ZX BASIC crashes on out-of-bounds access
3. **Too many entities:** 20+ sprites causes visible slowdown
4. **Not reusing slots:** Memory waste and slower spawn

## Extension Ideas
- Different enemy types (different UDGs/behaviour)
- Wave spawner (spawn groups)
- Entity health system
- Formation flying

## Builds Toward
**In This Arc:**
- L24: Bullet patterns
- L25: Collision detection between entities
- L27: Complete arcade game

## Quick Reference
### Entity Management Pattern
```basic
REM Entity arrays
DIM ex(N), ey(N), evx(N), evy(N), ea(N)

REM Update loop
FOR i=1 TO N
  IF ea(i)=0 THEN NEXT i  REM Skip inactive
  REM Update entity i
  REM ...
  IF offScreen THEN LET ea(i)=0  REM Deactivate
NEXT i

REM Spawn new entity
REM Find empty slot: ea(i)=0
REM Initialize position/velocity
REM Set ea(i)=1
```

### Optimization
```basic
REM Track active count to skip loop when empty
IF numActive=0 THEN GO TO playerUpdate

REM Early exit from loop
IF ea(i)=0 THEN GO TO 500  REM Jump to NEXT
REM ... process entity ...
500 NEXT i
```

---

**Version:** 1.0
**Created:** 2025-10-27
