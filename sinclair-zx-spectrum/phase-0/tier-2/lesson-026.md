# Lesson 026: Enemy AI Patterns

**Arc:** Arcade Action
**Position:** Lesson 5 of 6 in arc
**Type:** Standard
**Estimated Completion:** 130 lines of code

## Learning Objectives
- Create simple enemy movement patterns
- Implement different enemy types with distinct behaviors
- Use timers for pattern changes
- Balance difficulty with variety

## Prerequisites
- Multiple entities (L23)
- Collision detection (L25)
- Basic trigonometry (SIN/COS) for patterns

## Key Concepts
**Pattern Types** - Straight down, zigzag, sine wave, dive attack
**State Machines** - Enemy behavior changes over time
**Timer-Based AI** - Use frame counter for pattern transitions
**Enemy Types** - Store behavior type per entity

## Code Pattern
```basic
10 REM Enemy AI patterns demo
20 DIM ex(10),ey(10),evx(10),evy(10),ea(10),et(10),etimer(10)
30 REM et=type (1=straight, 2=zigzag, 3=sine, 4=dive)
40 REM etimer=internal timer for pattern
50 LET maxE=10
60 REM Spawn enemies with different types
70 FOR i=1 TO 5
80   LET ex(i)=RND*30: LET ey(i)=1
90   LET et(i)=INT(RND*4)+1: REM Random type 1-4
100   LET ea(i)=1: LET etimer(i)=0
110 NEXT i
120 REM Main loop - update enemies
130 FOR i=1 TO maxE
140   IF ea(i)=0 THEN GO TO 400
150   LET etimer(i)=etimer(i)+1
160   LET typ=et(i)
170   REM Type 1: Straight down
180   IF typ=1 THEN LET evy(i)=1: LET evx(i)=0
190   REM Type 2: Zigzag
200   IF typ=2 THEN GOSUB 1000
210   REM Type 3: Sine wave
220   IF typ=3 THEN GOSUB 2000
230   REM Type 4: Dive at player
240   IF typ=4 THEN GOSUB 3000
250   REM Apply velocity
260   LET ex(i)=ex(i)+evx(i)
270   LET ey(i)=ey(i)+evy(i)
280   REM Boundary/deactivate
290   IF ey(i)>21 THEN LET ea(i)=0: GO TO 400
300   REM Draw enemy
310   INK 2: PRINT AT ey(i),ex(i);CHR$ (143+typ): REM Different UDG per type
320 400 NEXT i
330 REM ... rest of game loop ...
340 GO TO 130
1000 REM Zigzag pattern (type 2)
1010 LET evy(i)=1
1020 IF etimer(i) MOD 20<10 THEN LET evx(i)=1 ELSE LET evx(i)=-1
1030 RETURN
2000 REM Sine wave pattern (type 3)
2010 LET evy(i)=1
2020 LET evx(i)=INT(2*SIN(etimer(i)/5))
2030 RETURN
3000 REM Dive at player (type 4)
3010 LET evy(i)=1
3020 IF ey(i)>5 AND etimer(i) MOD 60=0 THEN GOSUB 3100: REM Dive every 60 frames
3030 RETURN
3100 REM Calculate dive velocity toward player
3110 LET dx=px-ex(i): LET dy=py-ey(i)
3120 LET dist=SQR(dx*dx+dy*dy)
3130 IF dist>0 THEN LET evx(i)=SGN(dx): LET evy(i)=SGN(dy)
3140 RETURN
```

## Hardware
**Performance:** AI calculations add ~5-10ms per frame for 10 enemies
**Memory:** Extra variables (type, timer) = +40 bytes per 10 enemies

## Common Pitfalls
1. **Too complex patterns:** ZX Spectrum CPU can't handle 10+ entities with heavy math
2. **No randomness:** Predictable patterns become boring
3. **Pattern never changes:** Static behavior lacks challenge
4. **Dive attack too accurate:** Make slightly off-target for fairness

## Extension Ideas
- Formation flying (enemies move as group)
- Boss patterns (multi-phase)
- Spawn mini-enemies
- Different speeds per type

## Builds Toward
- L27: Complete arcade game combining all patterns

## Quick Reference
### Pattern Types
```basic
REM 1. Straight down
LET evx=0: LET evy=1

REM 2. Zigzag (change direction periodically)
IF timer MOD 20 < 10 THEN LET evx=1 ELSE LET evx=-1

REM 3. Sine wave
LET evx=INT(2*SIN(timer/5))

REM 4. Circle
LET evx=INT(3*COS(timer/10))
LET evy=INT(3*SIN(timer/10))

REM 5. Toward player (simple chase)
LET evx=SGN(px-ex)
LET evy=SGN(py-ey)
```

---

**Version:** 1.0
**Created:** 2025-10-27
