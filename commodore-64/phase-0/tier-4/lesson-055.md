# Lesson 055: Unstable Colour Bars

**Arc:** Visual Limit - Raster Effects
**Position:** Lesson 2 of 6 in arc
**Type:** Standard
**Estimated Completion:** 70 lines

## Learning Objectives
- Attempt classic colour bar raster effect
- Experience visible wobble/jitter
- Measure timing instability
- Confirm BASIC cannot do stable rasters

## Key Concepts
- **Colour Bars:** Change border/background color every N raster lines
- **Wobble:** Bars move up/down 1-3 pixels each frame
- **Timing Variance:** 10-20 cycle execution variance per loop
- **Visual Failure:** Clearly visible instability

## Code Pattern
```basic
10 REM Unstable colour bars
20 POKE 53280,0:POKE 53281,0
30 REM Bar 1: Line 50
40 IF PEEK(53266)<>50 THEN 40
50 POKE 53280,2:REM Red
60 REM Bar 2: Line 100
70 IF PEEK(53266)<>100 THEN 70
80 POKE 53280,5:REM Green
90 REM Bar 3: Line 150
100 IF PEEK(53266)<>150 THEN 100
110 POKE 53280,6:REM Blue
120 REM Bar 4: Line 200
130 IF PEEK(53266)<>200 THEN 130
140 POKE 53280,4:REM Purple
150 REM Reset
160 IF PEEK(53266)<>250 THEN 160
170 POKE 53280,0:REM Black
180 GOTO 30
```

## Limit Demonstrated
**EXPLICIT FAILURE: Wobbling Bars**
"Colour bars wobble visibly (±2-3 pixels). BASIC's variable execution time prevents stable raster sync. Assembly uses raster IRQs → zero wobble."

## Quick Reference
**Expected:** Stable horizontal color bars
**Actual:** Bars wobble up/down each frame
**Cause:** 10-20 cycle timing variance
**Solution:** Assembly language raster interrupts

**Performance Note:** "Not a speed issue—a **timing precision issue**. BASIC cannot hit exact cycles needed for stable raster effects."
