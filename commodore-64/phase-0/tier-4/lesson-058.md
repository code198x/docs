# Lesson 058: Fine Scrolling Attempt

**Arc:** Visual Limit - Raster Effects
**Position:** Lesson 5 of 6 in arc
**Type:** Standard
**Estimated Completion:** 85 lines

## Learning Objectives
- Attempt hardware fine scrolling (smooth pixel scrolling)
- Experience jerky/tearing scrolling
- Understand VIC-II scrolling registers
- Confirm BASIC cannot sync with raster properly

## Key Concepts
- **Fine Scrolling:** VIC-II has hardware registers for smooth 8-pixel scrolling
- **$D016:** Horizontal scroll register (bits 0-2)
- **Synchronization:** Must update scroll register during vblank to avoid tearing
- **BASIC Problem:** Can't reliably hit vblank window → visible tearing

## Code Pattern
```basic
10 REM Hardware fine scrolling attempt
20 SCROLL=0:DIR=1
30 REM Main loop
40 REM Attempt to wait for vblank (line 250+)
50 IF PEEK(53266)<250 THEN 50
60 REM Update scroll register
70 POKE 53270,(PEEK(53270) AND 248) OR (SCROLL AND 7)
80 REM Update scroll position
90 SCROLL=SCROLL+DIR
100 IF SCROLL=0 OR SCROLL=7 THEN DIR=-DIR
110 REM Display
120 PRINT CHR$(19);"SCROLL: ";SCROLL;" ";
130 GOTO 40
```

## Limit Demonstrated
**EXPLICIT FAILURE: Jerky Scrolling with Tears**
"Scrolling jerks and tears. Sometimes updates mid-screen (visible split). BASIC can't reliably hit vblank window. Assembly uses vblank IRQ → butter-smooth scrolling."

## Quick Reference
**Expected:** Smooth pixel-by-pixel scrolling
**Actual:** Jerky motion with occasional screen tears
**Cause:** Can't reliably update during vblank
**Solution:** Assembly vblank interrupt

**Performance Note:** "Fine scrolling needs exact vblank timing. BASIC's timing variance causes mid-screen updates → **visible tearing.**"
