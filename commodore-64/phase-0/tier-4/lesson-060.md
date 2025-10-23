# Lesson 060: Multi-System Game Start

**Arc:** Complexity Limit - System Depth
**Position:** Lesson 1 of 5 in arc
**Type:** Standard
**Estimated Completion:** 160 lines

## Learning Objectives
- Combine all Phase 0 systems in one game
- Attempt simultaneous music, sprites, scrolling, rasters
- Measure performance collapse (5-6 fps)
- Experience system integration overhead

## Key Concepts
- **All Systems Active:** Music (3 voices) + sprites (8) + scrolling + collision + AI
- **Performance Collapse:** FPS drops from 6-8 to 5-6
- **Mutual Exclusivity:** Can have music OR smooth gameplay, not both
- **Complexity Ceiling:** Interpreter overhead compounds with system count

## Code Pattern
```basic
10 REM Multi-system game
20 REM ALL FEATURES ENABLED
30 REM Player + sprites + music + scrolling + rasters
40 DIM NOTES(32):REM Music notes
50 DIM EX(7),EY(7),EACTIVE(7):REM Enemies
60 NOTEPOS=0:MUSICENABLED=1
70 FC=0:FPS=0:LASTFPS=TI
80 REM Initialize
90 GOSUB 9000:REM Load music
100 GOSUB 9100:REM Init sprites
110 REM Main loop
120 FC=FC+1
130 REM Music update (expensive!)
140 IF MUSICENABLED=1 AND TI-LASTNOTE>5 THEN GOSUB 1000
150 REM Scrolling
160 IF FC MOD 3=0 THEN GOSUB 2000
170 REM Raster color bars
180 GOSUB 3000
190 REM Input
200 GOSUB 4000
210 REM Enemies
220 GOSUB 5000
230 REM Collision
240 GOSUB 6000
250 REM Sprites
260 GOSUB 7000
270 REM HUD
280 GOSUB 8000
290 GOTO 120
8000 REM HUD
8010 PRINT CHR$(19);
8020 PRINT "FPS:";FPS;" MUSIC:";
8030 IF MUSICENABLED=1 THEN PRINT "ON ";
8040 IF MUSICENABLED=0 THEN PRINT "OFF";
8050 PRINT:PRINT "PRESS M TO TOGGLE MUSIC"
8060 RETURN
```

## Performance Measurement
**All Systems Active:**
```
FPS: 5-6 (down from 6-8 without music)
Frame time: ~166-200ms
Music adds: ~30-40ms overhead per frame
```

## Limit Discovery
**System Trade-offs: Music OR Smoothness**

"With all systems active, FPS drops to **5-6 fps** (barely playable). Disabling music: **6-8 fps**. Disabling scrolling: **8-10 fps**.

**You cannot have everything simultaneously in BASIC:**
- Music + scrolling + sprites = 5-6 fps
- Scrolling + sprites (no music) = 6-8 fps
- Just sprites (no music, no scroll) = 12-15 fps

**Mutual exclusivity demonstrated.** Assembly can do all simultaneously at 50-60 fps."

## Performance Note
"Multi-system integration shows **complexity ceiling**. Each system adds overhead. BASIC's interpreter makes them mutually exclusive. Assembly has CPU headroom for all systems."
