# Lesson 035: Level Design

**Arc:** Platform Adventure
**Position:** Lesson 3 of 7 in arc
**Type:** Standard
**Estimated Completion:** 80 lines of code

## Learning Objectives

- Design multiple level screens using data-driven approach
- Implement level loading from DATA statements
- Create screen transitions and boundaries
- Build reusable level architecture for platformers

## Prerequisites

**From Previous Lessons:**
- Platform mechanics with animation (L33-34)
- Data-driven design concepts (L6)
- Array usage for game data

**BASIC Knowledge:**
- DATA/READ statements
- Multi-dimensional arrays
- Screen boundary detection

## Key Concepts Introduced

### Data-Driven Levels
Store level data in DATA statements (platform X, Y, width for each level). READ into arrays at level start, enabling easy level creation.

### Level Transitions
Detect when player exits screen boundaries (SX<0, SX>319, SY>229). Load next level data, reset player position.

### Platform Arrays
Use 2D arrays: PX(level, platform), PY(level, platform), PW(level, platform). Supports multiple platforms per level.

### Level Count Management
Track current level (LV), maximum levels (MAXLV). Handle level progression and wrap-around.

## Code Pattern

```basic
10 REM Level system variables
20 LV=1:MAXLV=4:PMAX=5:REM Current level, max levels, max platforms
30 DIM PX(4,5),PY(4,5),PW(4,5):REM Platform X, Y, Width per level
40 SX=20:SY=150:VX=0:VY=0:GR=0:ST=0:FC=0
50 GRAV=0.2:JMP=-3
60 REM Load all level data
70 GOSUB 1000
80 REM Setup sprite
90 POKE 53269,1:POKE 53287,1:POKE 2040,13
100 REM Main loop
110 J=PEEK(56320):FC=FC+1
120 REM Movement
130 VX=0
140 IF (J AND 4)=0 THEN VX=-2
150 IF (J AND 8)=0 THEN VX=2
160 IF (J AND 16)=0 AND GR=1 THEN VY=JMP:GR=0
170 REM Physics
180 VY=VY+GRAV
190 SX=SX+VX:SY=SY+VY
200 REM Platform collision
210 GR=0
220 FOR I=1 TO PMAX
230 IF PX(LV,I)=0 THEN NEXT I:GOTO 270
240 IF SX>PX(LV,I)-12 AND SX<PX(LV,I)+PW(LV,I)+12 THEN
250 IF SY>PY(LV,I)-21 AND SY<PY(LV,I) AND VY>0 THEN SY=PY(LV,I)-21:VY=0:GR=1
260 NEXT I
270 IF SY>229 THEN SY=229:VY=0:GR=1
280 REM Level boundaries and transitions
290 IF SX<0 THEN LV=LV-1:IF LV<1 THEN LV=MAXLV
300 IF LV<>LV THEN SX=300:GOSUB 2000:REM Left exit
310 IF SX>319 THEN LV=LV+1:IF LV>MAXLV THEN LV=1
320 IF LV<>LV THEN SX=20:GOSUB 2000:REM Right exit
330 REM Animation state
340 IF GR=0 AND VY<0 THEN ST=2
350 IF GR=0 AND VY>0 THEN ST=3
360 IF GR=1 AND VX<>0 THEN ST=1
370 IF GR=1 AND VX=0 THEN ST=0
380 REM Update sprite
390 IF ST=0 THEN SP=13+(FC/10) AND 1
400 IF ST=1 THEN SP=15+(FC/5) AND 3
410 IF ST=2 THEN SP=19
420 IF ST=3 THEN SP=20
430 POKE 2040,SP
440 POKE 53248,SX:POKE 53249,SY
450 GOTO 110
1000 REM Load level data
1010 FOR L=1 TO MAXLV
1020 FOR P=1 TO PMAX
1030 READ PX(L,P),PY(L,P),PW(L,P)
1040 NEXT P
1050 NEXT L
1060 RETURN
1100 REM Level 1 data (tutorial level)
1110 DATA 50,200,100, 200,180,80, 280,140,40, 0,0,0, 0,0,0
1120 REM Level 2 data (stepping stones)
1130 DATA 40,200,60, 120,180,50, 200,160,50, 280,140,40, 0,0,0
1140 REM Level 3 data (vertical challenge)
1150 DATA 20,220,50, 120,200,40, 180,170,40, 240,140,50, 0,0,0
1160 REM Level 4 data (gap jumping)
1170 DATA 20,200,80, 180,200,80, 0,0,0, 0,0,0, 0,0,0
2000 REM Level transition
2010 PRINT CHR$(147):REM Clear screen
2020 PRINT "LEVEL ";LV
2030 FOR I=1 TO 50:NEXT I:REM Brief pause
2040 RETURN
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Sprite rendering, screen boundaries
- **CIA** - Joystick input

**Memory Addresses:**
- Standard sprite and joystick registers
- Screen memory for level transition messages

## Common Pitfalls

1. **Wrong level transition logic:** Using IF LV<>LV (always false) instead of tracking old level
2. **Array bounds errors:** Forgetting to check if platform exists (PX=0 means no platform)
3. **Player stuck in wall:** Transition spawning player inside platform geometry
4. **No wrap-around:** Level 1 left exit goes to invalid level -1
5. **DATA count mismatch:** Not enough DATA values for all levels and platforms

## Extension Ideas

- Add visual differences per level (background colors)
- Add moving platforms (PX value changes over time)
- Add hazards (spikes at certain Y positions)
- Add collectibles placed per level
- Add locked doors requiring keys from previous levels
- Add vertical scrolling (levels taller than one screen)

## Builds Toward

**In This Tier:**
- L36: Enemies placed per level using same data-driven approach
- L37: Collectibles and goals distributed across levels
- L38: Level-specific music and visual themes
- L39: Complete 4-level platformer game

## Quick Reference

**Level Data Structure:**
```basic
10 DIM PX(levels, platforms), PY(levels, platforms), PW(levels, platforms)
20 REM Example: PX(2,3) = X position of platform 3 in level 2
30 REM Use 0 to mark "no platform" in unused slots
```

**DATA Organization Pattern:**
```basic
100 REM Level N: platform1_x, platform1_y, platform1_w, platform2_x...
110 DATA 50,200,100, 150,180,80, 0,0,0, 0,0,0, 0,0,0
```

**Level Transition Detection:**
```basic
10 OLDLV=LV
20 IF SX<0 THEN LV=LV-1:SX=300
30 IF SX>319 THEN LV=LV+1:SX=20
40 IF LV<1 THEN LV=MAXLV
50 IF LV>MAXLV THEN LV=1
60 IF LV<>OLDLV THEN GOSUB [transition routine]
```

**Platform Loop Pattern:**
```basic
100 FOR I=1 TO PMAX
110 IF PX(LV,I)=0 THEN NEXT I:GOTO [after loop]
120 REM Check collision with platform I
130 NEXT I
```

**Level Design Guidelines:**
- **Level 1:** Tutorial (easy jumps, clear path)
- **Level 2:** Introduce mechanics (longer jumps, moving)
- **Level 3:** Challenge (vertical sections, precision)
- **Level 4:** Mastery (combines all techniques)

**Platform Layout Tips:**
- Leave 50-80 pixel gaps for jumpable distances
- Platform width 40-100 pixels (too narrow = frustrating)
- Vertical spacing 50-80 pixels (one jump height)
- Always provide a "safe path" (don't force pixel-perfect jumps)

**Performance Note:**
"Level transitions are instant (DATA already in memory). Collision checking scales with platforms per level (5 platforms = negligible overhead). With 4 levels of 5 platforms each, performance remains smooth (12-15 fps)."
