# Lesson 028: Gravity and Jumping

**Arc:** Platform Game
**Position:** Lesson 1 of 5 in arc
**Type:** Standard
**Estimated Completion:** 100 lines of code

## Learning Objectives
- Implement gravity physics in BASIC
- Create responsive jump mechanics
- Handle ground detection
- Achieve smooth vertical movement

## Prerequisites
- Fast sprite movement (L22)
- UDG graphics (L17)
- Integer math and velocity (L22)

## Key Concepts
**Gravity Constant** - Acceleration downward each frame
**Jump Velocity** - Initial upward velocity when jumping
**Terminal Velocity** - Maximum falling speed
**Ground State** - Boolean tracking if player on ground

## Code Pattern
```basic
10 REM Gravity and jumping demo
20 REM Player sprite
30 LET base=USR "a"
40 FOR n=0 TO 7
50   READ byte
60   POKE base+n,byte
70 NEXT n
80 DATA 60,126,255,255,126,60,60,24: REM Player character
90 REM Physics variables
100 LET py=10: REM Y position (row)
110 LET vy=0: REM Y velocity
120 LET gravity=1: REM Gravity acceleration
130 LET jumpSpeed=-5: REM Jump velocity (negative=up)
140 LET groundY=20: REM Ground level
150 LET onGround=1: REM Boolean: on ground?
160 REM Horizontal movement
170 LET px=15: LET vx=0
180 REM Main loop
190 REM Input
200 LET k$=INKEY$
210 LET vx=0
220 IF k$="q" THEN LET vx=-1
230 IF k$="w" THEN LET vx=1
240 REM Jump (only when on ground)
250 IF k$=" " AND onGround=1 THEN LET vy=jumpSpeed: LET onGround=0: BEEP 0.01,20
260 REM Apply gravity
270 IF onGround=0 THEN LET vy=vy+gravity
280 REM Terminal velocity (max fall speed)
290 IF vy>3 THEN LET vy=3
300 REM Horizontal movement
310 LET px=px+vx
320 IF px<1 THEN LET px=1
330 IF px>30 THEN LET px=30
340 REM Vertical movement
350 LET py=py+vy
360 REM Ground collision
370 IF py>=groundY THEN LET py=groundY: LET vy=0: LET onGround=1
380 REM Render
390 CLS
400 REM Draw ground
410 FOR x=0 TO 31
420   PRINT AT groundY,x;CHR$ 145: REM Ground tiles
430 NEXT x
440 REM Draw player
450 INK 6: PRINT AT py,px;CHR$ 144
460 REM Debug info
470 PRINT AT 0,0;"Y:";py;" VY:";vy;" Ground:";onGround
480 REM Frame delay
490 FOR d=1 TO 15: NEXT d
500 GO TO 190
```

## Hardware
**Performance:**
- Gravity calculations: ~1ms per frame
- Character-based movement: very fast (no pixel plotting)
- 48K and 128K Spectrum handle equally well

**Limitations:**
- Character grid (8-pixel jumps) not smooth like Amiga
- No sub-character precision without complex tracking
- Still playable and responsive for platformers

## Common Pitfalls
1. **Gravity too strong:** Player falls instantly (feels bad)
2. **Jump too weak:** Can't reach platforms
3. **No terminal velocity:** Acceleration continues forever
4. **Forgetting ground check:** Can double-jump mid-air

## Extension Ideas
- Variable jump height (hold longer = higher)
- Coyote time (grace period after walking off edge)
- Double jump power-up
- Different gravity zones

## Builds Toward
**In This Arc:**
- L29: Collision with platforms/walls
- L30: Moving platforms
- L31: Level data and scrolling
- L32: Complete platformer synthesis

## Quick Reference
### Physics Pattern
```basic
REM Constants
LET gravity=1
LET jumpSpeed=-5
LET terminalVel=3

REM Each frame:
IF onGround=0 THEN LET vy=vy+gravity
IF vy>terminalVel THEN LET vy=terminalVel
LET py=py+vy
IF py>=groundY THEN LET py=groundY: LET vy=0: LET onGround=1
```

### Variable Jump Height
```basic
REM When button pressed:
IF k$=" " AND onGround=1 THEN LET vy=jumpSpeed: LET jumpHeld=1

REM Each frame while holding:
IF k$=" " AND jumpHeld=1 AND vy<0 THEN LET vy=vy-1: REM Extra boost

REM When button released:
IF k$<>" " THEN LET jumpHeld=0
```

---

**Version:** 1.0
**Created:** 2025-10-27
