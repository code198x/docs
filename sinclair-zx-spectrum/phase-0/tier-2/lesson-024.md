# Lesson 024: Simple Bullet Patterns

**Arc:** Arcade Action
**Position:** Lesson 3 of 6 in arc
**Type:** Standard
**Estimated Completion:** 100 lines of code

## Learning Objectives
- Implement player shooting mechanism
- Manage bullet entity pool
- Create simple enemy bullet patterns
- Handle bullet lifecycle efficiently

## Prerequisites
- Multiple moving objects (L23)
- Entity management (L23)
- Fast sprite movement (L22)

## Key Concepts
**Bullet Pool** - Dedicated array for bullets (typically 5-10)
**Spawn on Fire** - Create bullet at player position when firing
**Straight Line Movement** - Simple velocity patterns
**Auto-Deactivate** - Remove bullets when off-screen

## Code Pattern
```basic
10 REM Player shooting demo
20 DIM bx(10): DIM by(10): DIM bvx(10): DIM bvy(10): DIM ba(10)
30 LET maxB=10
40 LET px=15: LET py=18: REM Player position
50 REM Main loop
60 REM Input
70 LET k$=INKEY$
80 IF k$="q" THEN LET px=px-1
90 IF k$="w" THEN LET px=px+1
100 IF k$=" " THEN GOSUB 1000: REM Fire bullet
110 REM Update bullets
120 FOR i=1 TO maxB
130   IF ba(i)=0 THEN GO TO 200
140   REM Move bullet
150   LET bx(i)=bx(i)+bvx(i)
160   LET by(i)=by(i)+bvy(i)
170   REM Off screen check
180   IF by(i)<0 OR by(i)>21 THEN LET ba(i)=0: GO TO 200
190   REM Draw bullet
195   INK 6: PRINT AT by(i),bx(i);CHR$ 144
200 NEXT i
210 REM Draw player
220 INK 2: PRINT AT py,px;CHR$ 145
230 REM Frame delay
240 FOR d=1 TO 30: NEXT d
250 GO TO 60
1000 REM Fire bullet subroutine
1010 REM Find empty slot
1020 FOR i=1 TO maxB
1030   IF ba(i)=0 THEN GO TO 1060
1040 NEXT i
1050 RETURN: REM No slots (player can't fire)
1060 REM Spawn bullet at player position
1070 LET bx(i)=px: LET by(i)=py-1
1080 LET bvx(i)=0: LET bvy(i)=-2: REM Upward velocity
1090 LET ba(i)=1
1100 RETURN
```

## Hardware
**Memory:** 10 bullets × 5 vars × 2 bytes = 100 bytes
**Performance:** 10 bullets adds ~10ms per frame

## Common Pitfalls
1. **Fire rate too fast:** Add cooldown timer between shots
2. **Bullets spawn inside enemy:** Offset spawn position
3. **Running out of slots:** Limit fire rate or increase pool size

## Extension Ideas
- Fire rate cooldown (timer)
- Spread shot (3 bullets at angles)
- Enemy return fire
- Bullet UDG variations

## Builds Toward
- L25: Collision between bullets and enemies
- L27: Complete shooter game

## Quick Reference
### Fire Rate Limiting
```basic
LET fireCooldown=0
REM In main loop:
IF fireCooldown>0 THEN LET fireCooldown=fireCooldown-1
IF k$=" " AND fireCooldown=0 THEN GOSUB 1000: LET fireCooldown=10
```

### Spread Shot
```basic
REM Fire 3 bullets (left, center, right)
GOSUB 1000: LET bvx(i)=-1: REM Left
GOSUB 1000: LET bvx(i)=0: REM Center
GOSUB 1000: LET bvx(i)=1: REM Right
```

---

**Version:** 1.0
**Created:** 2025-10-27
