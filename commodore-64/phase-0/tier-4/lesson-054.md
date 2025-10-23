# Lesson 054: Understanding Rasters

**Arc:** Visual Limit - Raster Effects
**Position:** Lesson 1 of 6 in arc
**Type:** Standard
**Estimated Completion:** 60 lines of code

## Learning Objectives

- Understand raster beam concept (CRT display technology)
- Learn VIC-II raster register reading
- Discover timing requirements for raster effects
- Attempt basic raster wait loop
- Experience BASIC's timing instability

## Prerequisites

**From Previous Lessons:**
- Hardware interaction (VIC-II chip)
- Performance awareness from L49-53
- Timing concepts

**BASIC Knowledge:**
- PEEK for reading hardware registers
- WAIT statement
- Loop timing

## Key Concepts Introduced

### Raster Beam
CRT monitor draws screen line-by-line, top to bottom, 50 (PAL) or 60 (NTSC) times per second. VIC-II raster register ($D012) tracks current scan line.

### Raster Position
Register 53266 ($D012) contains current raster line (0-311 for PAL). Can wait for specific line to synchronize effects.

### Cycle-Perfect Timing
Raster effects need exact timing (±1 cycle accuracy). Change color at exact moment beam reaches position.

### BASIC's Timing Problem
BASIC's WAIT or polling loops have **variable execution time**. Can't hit exact cycles. Results in wobble/jitter.

## Code Pattern

```basic
10 REM Understanding rasters
20 REM VIC-II raster register: 53266 ($D012)
30 REM Border color: 53280 ($D020)
40 REM Background color: 53281 ($D021)
50 REM
60 REM Example 1: Read current raster position
70 PRINT CHR$(147)
80 PRINT "RASTER POSITION READER"
90 PRINT STRING$(40,"-")
100 FOR I=1 TO 100
110 RASTER=PEEK(53266)
120 PRINT CHR$(19);"CURRENT RASTER: ";RASTER;" ";
130 FOR J=1 TO 10:NEXT J:REM Slow down display
140 NEXT I
150 REM
160 REM Example 2: Wait for specific raster line
170 PRINT CHR$(147)
180 PRINT "WAITING FOR RASTER LINE 100..."
190 REM Wait for raster to reach line 100
200 IF PEEK(53266)<>100 THEN 200
210 PRINT "HIT LINE 100!"
220 REM
230 REM Example 3: Attempt color change at raster line
240 PRINT CHR$(147)
250 PRINT "ATTEMPTING RASTER COLOR CHANGE"
260 PRINT "(WATCH FOR WOBBLE)"
270 PRINT
280 PRINT "PRESS SPACE TO STOP"
290 REM Main loop
300 REM Wait for raster line 100
310 IF PEEK(53266)<>100 THEN 310
320 POKE 53280,2:REM Change border to red
330 REM Wait for raster line 150
340 IF PEEK(53266)<>150 THEN 340
350 POKE 53280,6:REM Change border to blue
360 REM Wait for raster line 200
370 IF PEEK(53266)<>200 THEN 370
380 POKE 53280,5:REM Change border to green
390 REM Check for space key
400 GET K$:IF K$<>" " THEN 300
410 POKE 53280,14:REM Reset border
420 REM
430 REM Example 4: Measure timing instability
440 PRINT CHR$(147)
450 PRINT "TIMING MEASUREMENT"
460 PRINT STRING$(40,"-")
470 PRINT
480 DIM HITTIME(20)
490 FOR I=1 TO 20
500 REM Wait for line 100
510 IF PEEK(53266)<>100 THEN 510
520 REM Record when we hit it
530 HITTIME(I)=TI
540 REM Wait for next frame
550 FOR J=1 TO 100:NEXT J
560 NEXT I
570 REM Show variance
580 PRINT "HIT TIMES (JIFFIES):"
590 MINTIME=HITTIME(1):MAXTIME=HITTIME(1)
600 FOR I=1 TO 20
610 PRINT HITTIME(I);
620 IF HITTIME(I)<MINTIME THEN MINTIME=HITTIME(I)
630 IF HITTIME(I)>MAXTIME THEN MAXTIME=HITTIME(I)
640 NEXT I
650 PRINT:PRINT
660 PRINT "VARIANCE: ";MAXTIME-MINTIME;" jiffies"
670 PRINT "(Should be 0 for stable timing)"
680 PRINT
690 PRINT "BASIC CANNOT HIT EXACT CYCLES"
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Raster register reading, color changes

**Memory Addresses:**
- 53266 ($D012) - Raster counter (0-311 for PAL)
- 53265 ($D011) - Raster bit 8 (for lines > 255)
- 53280 ($D020) - Border color
- 53281 ($D021) - Background color

## Timing Problem Discovered

**BASIC Cannot Hit Exact Cycles:**

"When attempting to change color at specific raster line, you'll see **wobble and jitter**.

**Why BASIC fails:**
1. **Variable loop time:** IF PEEK(53266)<>100 THEN 310
   - PEEK: Variable time
   - Comparison: Variable time
   - Branch: Variable time
   - Each iteration: 10-20 cycles variance

2. **No cycle control:** Can't specify "wait exactly N cycles"

3. **Interpreter overhead:** Parsing line numbers adds random delays

**Assembly language:**
- Can wait exact cycles
- Can use hardware interrupts (raster IRQ)
- Can poll register with precise timing
- Result: Rock-solid raster effects (zero wobble)

**Visual result:** Color bars wobble up/down by 1-3 pixels. Unacceptable for professional effects.

Next lessons attempt various raster effects—all will show instability."

## Common Pitfalls

1. **Not accounting for raster wrap:** Line 311 → 0 (need to handle)
2. **Forgetting bit 8:** Lines 256+ need checking $D011
3. **Too many effects:** Multiple raster waits compound timing errors
4. **Blocking input:** Raster loops prevent joystick reading
5. **PAL vs NTSC:** Different raster line counts (311 vs 262)

## Builds Toward

**In This Arc:**
- L55: Unstable colour bars (wobble demonstrated)
- L56: Split-screen HUD (timing issues visible)
- L57: Sprite multiplexing attempt (flicker)
- L58: Fine scrolling attempt (tearing)
- L59: Complete raster demo (all effects unstable)

## Quick Reference

**Raster Register Reading:**
```basic
10 RASTER=PEEK(53266):REM Lines 0-255
20 REM For lines 256-311:
30 RASTER=PEEK(53266)
40 IF PEEK(53265) AND 128 THEN RASTER=RASTER+256
```

**Wait for Raster Line:**
```basic
10 REM Wait for line 100
20 IF PEEK(53266)<>100 THEN 20
30 REM Execute code here (but timing is unstable)
```

**Raster Positions:**
```
Line 0-49: Top border
Line 50-249: Visible screen (200 lines)
Line 250-311: Bottom border + vblank
```

**Timing Requirements:**
```
VIC-II clock: 1.023 MHz (PAL)
Cycles per raster line: 63 cycles
For stable effect: Must hit ±1 cycle

BASIC variance: 10-20 cycles (unstable)
Assembly: 0 cycles variance (stable)
```

**Visual Effects Requiring Stable Rasters:**
```
- Color bars (L55)
- Split screen (L56)
- Sprite multiplexing (L57)
- Smooth scrolling (L58)
- FLD (flexible line distance)
- Sprite stretching

All impossible in BASIC due to timing variance.
```

**Performance Note:**
"Raster effects demonstrate a **different failure mode** than speed (L49-53). Not too slow—too **imprecise**. BASIC's variable execution time means color changes happen at slightly different raster lines each frame (±2-3 lines of wobble). This creates visible instability. Raster effects need ±1 cycle accuracy. BASIC has 10-20 cycles variance. **Assembly language can use raster interrupts** (hardware-triggered exact timing) → rock-solid effects."
