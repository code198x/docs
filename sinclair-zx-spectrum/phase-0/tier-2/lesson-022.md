# Lesson 022: Fast Sprite Movement

**Arc:** Arcade Action
**Position:** Lesson 1 of 6 in arc
**Type:** Standard
**Estimated Completion:** 90 lines of code

## Learning Objectives
- Achieve smooth sprite movement on ZX Spectrum
- Use PRINT AT for fast character positioning
- Implement velocity-based movement
- Handle screen boundaries efficiently

## Prerequisites
- UDG graphics (L17-18)
- PRINT AT positioning (Tier 1)
- Basic game loops (Tier 1)

## Key Concepts
**Character-Based Sprites** - UDGs as sprites (faster than PLOT/DRAW)
**Velocity System** - Separate velocity from position for smooth motion
**Double Buffering Trick** - Erase-move-draw pattern
**Frame Timing** - Consistent speed across different Spectrums

## Code Pattern
```basic
10 REM Fast sprite movement demo
20 LET base=USR "a"
30 REM Define sprite (ship)
40 FOR n=0 TO 7
50   READ byte
60   POKE base+n,byte
70 NEXT n
80 DATA 24,60,126,255,126,60,24,24
90 REM Position and velocity (integer math)
100 LET x=15: LET y=10
110 LET vx=0: LET vy=0
120 LET speed=1: REM Move 1 character per update
130 REM Main loop
140 LET k$=INKEY$
150 LET vx=0: LET vy=0
160 IF k$="q" THEN LET vx=-speed
170 IF k$="w" THEN LET vx=speed
180 IF k$="a" THEN LET vy=-speed
190 IF k$="z" THEN LET vy=speed
200 REM Calculate new position
210 LET nx=x+vx: LET ny=y+vy
220 REM Boundary check
230 IF nx<1 THEN LET nx=1
240 IF nx>30 THEN LET nx=30
250 IF ny<1 THEN LET ny=1
260 IF ny>20 THEN LET ny=20
270 REM Erase old position (if moved)
280 IF nx<>x OR ny<>y THEN PRINT AT y,x;" "
290 REM Update position
300 LET x=nx: LET y=ny
310 REM Draw new position
320 INK 6: PRINT AT y,x;CHR$ 144
330 REM Frame delay (adjust for speed)
340 FOR d=1 TO 100: NEXT d
350 GO TO 140
```

## Hardware
**Z80 CPU:** 3.5 MHz, slower than Amiga but sufficient for character-based sprites
**ULA:** Generates video, no hardware sprites (unlike C64/Amiga)
**Screen Memory:** 16384-22527, character-based access via PRINT AT

**Performance:**
- PRINT AT: ~1-2ms per character (very fast)
- PLOT: ~10-20ms (avoid for real-time games)
- DRAW: ~50-100ms (avoid for real-time games)
- Character sprites can achieve 25-30 FPS easily

## Common Pitfalls
1. **Using PLOT/DRAW:** Far too slow for moving sprites
2. **No erase before draw:** Leaves trails
3. **Integer-only math:** No sub-character precision (8-pixel jumps)
4. **Frame rate varies:** 48K vs 128K vs +2/+3 timing differences

## Extension Ideas
- Sub-character movement (track pixel position separately)
- Diagonal movement normalization
- Acceleration/deceleration
- Inertia and momentum

## Builds Toward
**In This Arc:**
- L23: Multiple moving objects
- L24: Simple bullet patterns
- L25: Collision detection
- L26: Enemy AI patterns
- L27: Space Invaders-style game (deliverable)

## Quick Reference
### Speed Control
```basic
REM Slow (every frame)
LET x=x+vx

REM Fast (skip frames)
LET frameCount=frameCount+1
IF frameCount MOD 2=0 THEN LET x=x+vx

REM Very slow (delay between moves)
FOR delay=1 TO 200: NEXT delay
```

### Smooth Boundaries
```basic
REM Wrap around
IF x<0 THEN LET x=31
IF x>31 THEN LET x=0

REM Bounce
IF x<0 OR x>31 THEN LET vx=-vx
```

---

**Version:** 1.0
**Created:** 2025-10-27
