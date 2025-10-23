# Lesson 063: System Integration Struggles

**Arc:** Complexity Limit - System Depth
**Position:** Lesson 4 of 5 in arc
**Type:** Standard
**Estimated Completion:** 140 lines

## Learning Objectives
- Demonstrate mutual exclusivity of systems
- Document feature trade-offs required
- Measure FPS with different system combinations
- Confirm complexity ceiling

## Key Concepts
- **Mutual Exclusivity:** Can't have music AND scrolling AND sprites simultaneously
- **Feature Trade-offs:** Must choose which systems to enable
- **Performance Budget:** Limited CPU time forces choices
- **Assembly Advantage:** Can do all systems simultaneously

## Code Pattern
```basic
10 REM System integration tester
20 MUSIC=1:SCROLL=1:SPRITES=7:RASTERS=1
30 REM Toggle features
40 PRINT CHR$(147)
50 PRINT "SYSTEM INTEGRATION TEST"
60 PRINT STRING$(40,"-")
70 PRINT "1. MUSIC: ";:IF MUSIC THEN PRINT "ON" ELSE PRINT "OFF"
80 PRINT "2. SCROLLING: ";:IF SCROLL THEN PRINT "ON" ELSE PRINT "OFF"
90 PRINT "3. SPRITES: ";SPRITES
100 PRINT "4. RASTERS: ";:IF RASTERS THEN PRINT "ON" ELSE PRINT "OFF"
110 PRINT
120 PRINT "M=MUSIC, S=SCROLL, P=SPRITES, R=RASTERS"
130 PRINT "SPACE=RUN TEST"
140 GET K$:IF K$="" THEN 140
150 IF K$="M" THEN MUSIC=1-MUSIC:GOTO 40
160 IF K$="S" THEN SCROLL=1-SCROLL:GOTO 40
170 IF K$="P" THEN INPUT "SPRITES (0-7)";SPRITES:GOTO 40
180 IF K$="R" THEN RASTERS=1-RASTERS:GOTO 40
190 IF K$<>" " THEN 140
200 REM Run test
210 GOSUB 1000
300 GOTO 40
1000 REM Performance test
1010 PRINT CHR$(147);"TESTING..."
1020 FC=0:STARTTIME=TI
1030 FOR I=1 TO 300:REM 300 frames
1040 FC=FC+1
1050 IF MUSIC THEN GOSUB 2000
1060 IF SCROLL THEN GOSUB 3000
1070 FOR S=1 TO SPRITES:GOSUB 4000:NEXT S
1080 IF RASTERS THEN GOSUB 5000
1090 NEXT I
1100 ELAPSED=TI-STARTTIME
1110 FPS=INT(300*60/ELAPSED)
1120 PRINT CHR$(147)
1130 PRINT "RESULTS:"
1140 PRINT "FPS: ";FPS
1150 PRINT:PRINT "PRESS ANY KEY";
1160 GET K$:IF K$="" THEN 1160
1170 RETURN
```

## Performance Measurement
**System Combinations:**
```
All systems (music+scroll+7 sprites+rasters): 5-6 fps
No music (scroll+7 sprites+rasters): 6-8 fps
No scroll (music+7 sprites+rasters): 7-9 fps
No rasters (music+scroll+7 sprites): 8-10 fps
Just sprites (3 sprites only): 15-18 fps
```

## Limit Demonstrated
**Feature Trade-offs Required**

"**You must choose which systems to include:**

**Option A:** Music + sprites (no scrolling) = 8-10 fps
**Option B:** Scrolling + sprites (no music) = 6-8 fps
**Option C:** Simple game (3 sprites, no music, no scroll) = 15-18 fps

**Cannot have professional game with all features in BASIC.**

**Commercial C64 games (assembly):**
- Music (3 voices)
- Scrolling (smooth hardware scrolling)
- 20+ sprites (multiplexed)
- Raster effects
- All at 50-60 fps simultaneously

**BASIC forces mutual exclusivity. Assembly doesn't.**"

## Quick Reference
**Performance Budget (BASIC):**
```
Music: ~30-40ms per frame
Scrolling: ~40-50ms per frame
7 sprites + AI: ~50-60ms per frame
Rasters: ~10-15ms per frame
Total if all enabled: ~150-180ms = 5-6 fps

Target frame time: 16-20ms (50-60 fps)
Overage: 8-10× too slow
```

**Assembly Budget:**
```
Music (IRQ): ~2-3ms
Scrolling (hardware): ~1ms
20 sprites (multiplexed): ~3-4ms
Rasters (IRQ): ~1-2ms
Total: ~8-10ms = 50-60 fps achievable
```

**Performance Note:**
"System integration demonstrates **mutual exclusivity**. Must choose music OR scrolling OR many sprites—can't have all. BASIC's interpreter overhead makes complex games impossible. **Assembly can do all systems simultaneously at 50-60 fps.**"
