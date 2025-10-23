# Lesson 056: Split-Screen HUD

**Arc:** Visual Limit - Raster Effects
**Position:** Lesson 3 of 6 in arc
**Type:** Standard
**Estimated Completion:** 80 lines

## Learning Objectives
- Attempt split-screen effect (different colors for HUD vs playfield)
- Experience screen tear at split point
- Measure split instability
- Confirm timing issues prevent clean splits

## Key Concepts
- **Split Screen:** Different colors for HUD area (top) vs game area (bottom)
- **Tear Line:** Visible wobble at split boundary
- **Timing Critical:** Must change color at exact line each frame
- **BASIC Fails:** Split position moves ±2-3 lines

## Code Pattern
```basic
10 REM Split-screen HUD attempt
20 SCORE=1000:LIVES=3
30 REM HUD area (lines 0-24): Dark colors
40 IF PEEK(53266)>5 THEN 40
50 POKE 53280,0:POKE 53281,11:REM Black border, gray BG
60 REM Display HUD
70 PRINT CHR$(19);"SCORE:";SCORE;" LIVES:";LIVES;"  ";
80 REM Wait for playfield split (line 25)
90 IF PEEK(53266)<>25 THEN 90
100 POKE 53280,6:POKE 53281,14:REM Blue border, lt blue BG
110 REM Wait for bottom (line 250)
120 IF PEEK(53266)<>250 THEN 120
130 GOTO 30
```

## Limit Demonstrated
**EXPLICIT FAILURE: Unstable Split**
"Split line wobbles. See 2-3 pixels of wrong color 'bleeding' across boundary. Clean split impossible in BASIC. Assembly uses raster IRQ → perfect split."

## Quick Reference
**Expected:** Clean horizontal split at line 25
**Actual:** Split wobbles, colors bleed
**Cause:** Cannot hit exact raster line consistently
**Solution:** Assembly raster interrupt at line 25

**Performance Note:** "Split-screen demos require ±1 cycle accuracy. BASIC has 10-20 cycles variance. **Visual result: wobbly tear line.**"
