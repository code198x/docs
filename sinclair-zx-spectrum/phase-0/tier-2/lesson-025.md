# Lesson 025: Collision Detection

**Arc:** Arcade Action
**Position:** Lesson 4 of 6 in arc
**Type:** Standard
**Estimated Completion:** 110 lines of code

## Learning Objectives
- Implement character-based collision detection
- Check bullet-enemy collisions
- Handle player-enemy collisions
- Optimize collision checks for performance

## Prerequisites
- Multiple entities (L23)
- Bullet patterns (L24)
- Arrays and nested loops (Tier 1)

## Key Concepts
**Character Grid Collision** - Simple x,y position comparison
**Nested Loop Pattern** - Check every bullet against every enemy
**Early Exit** - Stop checking once collision found
**Performance Trade-off** - 10 bullets × 10 enemies = 100 checks per frame

## Code Pattern
```basic
10 REM Collision detection demo
20 REM (Assume bullets and enemies from L23-24)
30 REM Player: px, py
40 REM Bullets: bx(), by(), ba()
50 REM Enemies: ex(), ey(), ea()
60 LET score=0: LET lives=3
70 REM Main loop (after updates)
80 REM Check bullet-enemy collisions
90 FOR b=1 TO maxB
100   IF ba(b)=0 THEN GO TO 200: REM Skip inactive bullet
110   FOR e=1 TO maxE
120     IF ea(e)=0 THEN GO TO 190: REM Skip inactive enemy
130     REM Check if bullet and enemy at same position
140     IF bx(b)=ex(e) AND by(b)=ey(e) THEN GOSUB 2000
150     REM (GOSUB 2000 handles hit - deactivates both, adds score)
160   190 NEXT e
170 200 NEXT b
180 REM Check player-enemy collisions
190 FOR e=1 TO maxE
200   IF ea(e)=0 THEN GO TO 270
210   IF ex(e)=px AND ey(e)=py THEN GOSUB 3000
220   REM (GOSUB 3000 handles player hit - deactivates enemy, loses life)
230 270 NEXT e
240 REM ... rest of game loop ...
250 GO TO 80
2000 REM Bullet-enemy collision handler
2010 LET ba(b)=0: REM Deactivate bullet
2020 LET ea(e)=0: REM Deactivate enemy
2030 LET score=score+10
2040 REM Explosion effect (optional)
2050 INK 4: PRINT AT ey(e),ex(e);CHR$ 148: REM Flash UDG
2060 RETURN
3000 REM Player-enemy collision handler
3010 LET ea(e)=0: REM Deactivate enemy
3020 LET lives=lives-1
3030 IF lives<=0 THEN GO TO 9000: REM Game over
3040 REM Flash player (invulnerability effect)
3050 FOR f=1 TO 5
3060   INVERSE 1: PRINT AT py,px;CHR$ 145
3070   FOR d=1 TO 50: NEXT d
3080   INVERSE 0: PRINT AT py,px;CHR$ 145
3090 NEXT f
3100 RETURN
9000 REM Game over
9010 CLS
9020 PRINT AT 10,10;"GAME OVER"
9030 PRINT AT 12,8;"Score: ";score
9040 STOP
```

## Hardware
**Performance:**
- 10 bullets × 10 enemies = 100 comparisons
- Each comparison: ~0.1ms
- Total collision checks: ~10ms per frame (acceptable)

**Optimization:**
- Skip inactive entities (ba(i)=0, ea(i)=0)
- Early exit on collision found
- Spatial partitioning for 20+ entities (advanced)

## Common Pitfalls
1. **Checking inactive entities:** Wastes CPU time
2. **No collision response:** Detecting but not handling
3. **Instant death:** No invulnerability after hit (frustrating)
4. **Double-hit:** Same bullet hits multiple enemies (fix by deactivating immediately)

## Extension Ideas
- Explosion animation on hit
- Different scores per enemy type
- Power-ups (larger collision radius)
- Shield system (absorbs one hit)

## Builds Toward
- L26: Enemy AI with collision awareness
- L27: Complete arcade game with scoring

## Quick Reference
### Basic Collision Check
```basic
REM Character-based (exact position)
IF x1=x2 AND y1=y2 THEN collision

REM With tolerance (adjacent cells)
IF ABS(x1-x2)<=1 AND ABS(y1-y2)<=1 THEN collision
```

### Optimized Nested Loop
```basic
FOR b=1 TO maxB
  IF ba(b)=0 THEN GO TO 300  REM Skip to NEXT b
  FOR e=1 TO maxE
    IF ea(e)=0 THEN GO TO 290  REM Skip to NEXT e
    REM Check collision
    IF bx(b)=ex(e) AND by(b)=ey(e) THEN GOSUB handleHit: GO TO 300  REM Exit both loops
  290 NEXT e
300 NEXT b
```

---

**Version:** 1.0
**Created:** 2025-10-27
