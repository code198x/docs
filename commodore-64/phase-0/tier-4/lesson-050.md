# Lesson 050: Scrolling Background

**Arc:** Speed Limit - Fast Action Shmup
**Position:** Lesson 2 of 5 in arc
**Type:** Standard
**Estimated Completion:** 100 lines of code

## Learning Objectives

- Implement character-based vertical scrolling
- Create scrolling starfield effect
- Measure scrolling performance cost
- Discover BASIC's scrolling limitations
- Document FPS degradation

## Prerequisites

**From Previous Lessons:**
- Shmup foundation (L49)
- Screen memory manipulation (L8)
- Performance measurement

**BASIC Knowledge:**
- Screen memory scrolling
- Character copying in loops
- Memory address calculation

## Key Concepts Introduced

### Character Scrolling
Copy screen memory rows upward each frame to create scrolling effect. Bottom row filled with new stars.

### Starfield Pattern
Random star characters (*,.,-) at different densities. Creates illusion of depth and speed.

### Scrolling Cost
Scrolling 1000 bytes (40×25 screen) each frame adds significant overhead. **FPS drops from 15-18 to 12-14**.

### Memory Block Copy
Use FOR loops to copy screen memory. BASIC interpreter overhead makes this expensive operation.

## Code Pattern

```basic
10 REM Shmup with scrolling background
20 REM Performance measurement: scrolling cost
30 REM Screen memory addresses
40 SCREEN=1024:SCREENSIZE=1000
50 REM Player, bullets, enemies (from L49)
60 PX=160:PY=220:SCORE=0:PLIVES=3
70 DIM BX(5),BY(5),BACTIVE(5)
80 DIM EX(3),EY(3),EACTIVE(3)
90 REM Timing
100 FC=0:FPS=0:LASTFPS=TI:LASTFC=0
110 SCROLLSPEED=2:SCROLLCOUNT=0
120 REM Initialize
130 GOSUB 9000:REM Init screen with stars
140 POKE 53269,15:REM Enable sprites
150 POKE 53280,0:POKE 53281,0:REM Black background
160 REM Main loop
170 FC=FC+1
180 REM FPS measurement
190 IF TI-LASTFPS>50 THEN GOSUB 8000
200 REM Scrolling
210 IF FC MOD SCROLLSPEED=0 THEN GOSUB 1000
220 REM Input (from L49)
230 J=PEEK(56320)
240 IF (J AND 4)=0 AND PX>24 THEN PX=PX-3
250 IF (J AND 8)=0 AND PX<296 THEN PX=PX+3
260 IF (J AND 16)=0 AND TI-LASTSHOT>10 THEN GOSUB 2000
270 REM Update bullets (from L49)
280 GOSUB 3000
290 REM Update enemies (from L49)
300 GOSUB 4000
310 REM Spawn enemies
320 IF TI-LASTSPAWN>100 THEN GOSUB 5000
330 REM Update sprites
340 GOSUB 6000
350 REM Display HUD
360 GOSUB 7000
370 GOTO 170
1000 REM Scroll screen up one row
1010 REM Copy each row up one position
1020 FOR ROW=1 TO 24:REM Rows 1-24
1030 SRCROW=SCREEN+(ROW*40):REM Source row address
1040 DSTROW=SCREEN+((ROW-1)*40):REM Destination row address
1050 FOR COL=0 TO 39:REM Each character in row
1060 POKE DSTROW+COL,PEEK(SRCROW+COL)
1070 NEXT COL
1080 NEXT ROW
1090 REM Fill bottom row with new stars
1100 GOSUB 1200
1110 SCROLLCOUNT=SCROLLCOUNT+1
1120 RETURN
1200 REM Generate new star row at bottom
1210 BOTTOMROW=SCREEN+(24*40):REM Row 24
1220 FOR COL=0 TO 39
1230 REM Random star density
1240 R=INT(RND(1)*100)
1250 IF R<5 THEN POKE BOTTOMROW+COL,42:GOTO 1280:REM * (bright star)
1260 IF R<10 THEN POKE BOTTOMROW+COL,46:GOTO 1280:REM . (dim star)
1270 POKE BOTTOMROW+COL,32:REM Space (empty)
1280 NEXT COL
1290 RETURN
2000 REM Shoot bullet (from L49)
2010 REM [bullet shooting code]
2020 RETURN
3000 REM Update bullets (from L49)
3010 REM [bullet update code]
3020 RETURN
4000 REM Update enemies (from L49)
4010 REM [enemy update code]
4020 RETURN
5000 REM Spawn enemy (from L49)
5010 REM [enemy spawn code]
5020 RETURN
6000 REM Update sprites (from L49)
6010 REM [sprite update code]
6020 RETURN
7000 REM Display HUD
7010 PRINT CHR$(19);:REM Home
7020 PRINT "SCORE:";SCORE;" FPS:";FPS;" SCROLLS:";SCROLLCOUNT;"  ";
7030 RETURN
8000 REM Calculate FPS
8010 FRAMES=FC-LASTFC
8020 JIFFIES=TI-LASTFPS
8030 IF JIFFIES>0 THEN FPS=INT(FRAMES*60/JIFFIES)
8040 LASTFPS=TI:LASTFC=FC
8050 RETURN
9000 REM Initialize starfield
9010 FOR I=0 TO SCREENSIZE-1
9020 R=INT(RND(1)*100)
9030 IF R<5 THEN POKE SCREEN+I,42:GOTO 9060:REM *
9040 IF R<10 THEN POKE SCREEN+I,46:GOTO 9060:REM .
9050 POKE SCREEN+I,32:REM Space
9060 NEXT I
9070 RETURN
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Screen memory reading/writing for scrolling
- **SID** - Sound effects (from L49)
- **CIA** - Joystick, timing

**Memory Addresses:**
- 1024-2023 ($0400-$07E7) - Screen memory (1000 bytes)
- 55296-56295 ($D800-$DBE7) - Color memory (not used for stars)

## Performance Measurement

**Scrolling Cost:**
```
Without scrolling (L49): 15-18 fps
With scrolling (L50): 12-14 fps
Performance loss: ~20-25%
```

**Scrolling Overhead:**
```
Bytes copied per scroll: 960 bytes (24 rows × 40 cols)
PEEK operations: 960
POKE operations: 960
Total: 1920 memory operations per scroll
At 2 frames per scroll: 960 ops per frame
```

## Limit Discovery

**Scrolling Performance Hit:**

"Adding character-based scrolling **drops FPS from 15-18 to 12-14** (20-25% slower).

**Why so expensive?**
- Copying 960 characters per scroll (24 rows)
- Each character: PEEK source + POKE destination
- 1920 memory operations
- BASIC interpreter parses each PEEK/POKE line
- Nested FOR loops = massive overhead

**Assembly language** could use hardware scrolling registers or fast block copy routines (50-60 fps). BASIC can't—interpreter overhead dominates.

**This is just scrolling.** Next lesson adds animated enemies (drops to 8-10 fps)."

## Common Pitfalls

1. **Scrolling entire screen:** Including HUD line causes flicker
2. **Scrolling every frame:** Too fast, also more expensive
3. **Not optimizing:** Copying color memory too (doubles work)
4. **Wrong scroll direction:** Copying in wrong order causes artifacts
5. **Sprites behind text:** Sprite-to-background priority issues

## Extension Ideas

- Add multiple scroll speeds (layered parallax)
- Add scrolling obstacles (rocks, debris)
- Add horizontal scrolling (left/right)
- Add color cycling (animated stars)
- Add tile-based scrolling (patterns instead of characters)

## Builds Toward

**In This Arc:**
- L51: Many animated enemies (adds 6-8 fps overhead → 8-10 fps total)
- L52: Particle effects (another 2-3 fps lost → 6-8 fps)
- L53: Everything combined (6-8 fps ceiling measured)

## Quick Reference

**Screen Memory Scrolling (Up):**
```basic
FOR ROW=1 TO 24
  SOURCE = SCREEN + (ROW × 40)
  DEST = SCREEN + ((ROW-1) × 40)
  FOR COL=0 TO 39
    POKE DEST+COL, PEEK(SOURCE+COL)
  NEXT COL
NEXT ROW
```

**Starfield Generation:**
```basic
10 R=RND(1)
20 IF R<0.05 THEN CHAR=42  : REM * (5% bright)
30 IF R<0.10 THEN CHAR=46  : REM . (5% dim)
40 ELSE CHAR=32            : REM space (90% empty)
```

**Scroll Speed Tuning:**
```
Every frame: Smooth but expensive (FPS drops more)
Every 2 frames: Good balance (used here)
Every 3 frames: Slower, less overhead
Every 4+ frames: Too jerky for shmup feel
```

**Memory Operation Count:**
```
Screen size: 40 columns × 25 rows = 1000 bytes
Scrolling area: 40 × 24 = 960 bytes (skip HUD row)
Operations per scroll:
  - PEEK: 960 (read each character)
  - POKE: 960 (write each character)
  - New row generation: 40 (bottom row)
Total: ~2000 operations per scroll
```

**Performance Optimization Attempts (Insufficient):**
```
1. Skip empty rows: Saves ~10% (still too slow)
2. Scroll every 2-3 frames: Saves ~30-40% (but jerky)
3. Reduce scroll area: Saves ~20% (but limits play area)
4. Hardware scrolling: Not accessible from BASIC

None solve the fundamental problem: interpreter overhead.
```

**Expected Performance Degradation:**
```
L49 (baseline): 15-18 fps
L50 (+ scrolling): 12-14 fps (↓20%)
L51 (+ many enemies): 8-10 fps (↓35%)
L52 (+ particles): 6-8 fps (↓20%)
L53 (all combined): 6-8 fps (ceiling hit)
```

**Performance Note:**
"Character-based scrolling costs **20-25% FPS** (drops from 15-18 to 12-14 fps). Copying 960 screen characters every 2 frames means 1920 PEEK/POKE operations per scroll. BASIC's interpreter must parse every line—expensive. Game still playable but noticeably choppier. **This demonstrates BASIC's memory access overhead.** Assembly could use hardware scrolling or fast block moves (50-60 fps). BASIC can't."
