# Lesson 057: Sprite Multiplexing Attempt

**Arc:** Visual Limit - Raster Effects
**Position:** Lesson 4 of 6 in arc
**Type:** Standard
**Estimated Completion:** 100 lines

## Learning Objectives
- Attempt sprite multiplexing (reuse sprites across screen)
- Experience massive flicker
- Understand timing requirements for multiplexing
- Confirm BASIC too slow for sprite reuse

## Key Concepts
- **Multiplexing:** Reuse same hardware sprite at multiple Y positions
- **Timing:** Must update sprite position between raster lines
- **8-Sprite Limit:** Hardware only has 8 sprites; multiplexing shows more
- **BASIC Failure:** Too slow to update positions → massive flicker

## Code Pattern
```basic
10 REM Sprite multiplexing attempt
20 REM Try to show 12 sprites (only 8 hardware sprites)
30 DIM SY(12):REM Y positions
40 FOR I=1 TO 12:SY(I)=40+(I*15):NEXT I
50 POKE 53269,255:REM Enable sprites 0-7
60 REM Main loop
70 FOR S=1 TO 12
80 REM Determine which hardware sprite to use
90 HW=S MOD 8
100 REM Wait for raster past previous position
110 IF S>1 THEN
120 WAITLINE=SY(S-1)+25
130 IF PEEK(53266)<WAITLINE THEN 130
140 REM Update hardware sprite
150 POKE 2040+HW,13:REM Sprite pointer
160 POKE 53248+HW*2,160:REM X position
170 POKE 53249+HW*2,SY(S):REM Y position
180 NEXT S
190 GOTO 70
```

## Limit Demonstrated
**EXPLICIT FAILURE: Massive Flicker**
"Sprites flicker wildly. BASIC too slow to update positions between raster lines. See 3-4 sprites instead of 12. Assembly can do clean multiplexing → 20+ stable sprites."

## Quick Reference
**Expected:** 12 visible sprites via multiplexing
**Actual:** 3-4 sprites with massive flicker
**Cause:** BASIC too slow to update sprite positions in time
**Solution:** Assembly with raster IRQs

**Performance Note:** "Multiplexing needs sprite updates in ~500 cycles between positions. BASIC takes 2000-3000 cycles. **Result: Flicker city.**"
