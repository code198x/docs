# Lesson 017: User-Defined Graphics Basics

**Arc:** UDG Graphics System
**Position:** Lesson 1 of 5 in arc
**Type:** Standard
**Estimated Completion:** 50 lines of code

## Learning Objectives

- Understand UDG (User-Defined Graphics) system
- Define custom characters in memory
- Use CHR$ to display UDGs
- Create simple tile graphics

## Prerequisites

**From Previous Lessons:**
- PRINT AT positioning (L1-3)
- POKE command (L7-9)
- String manipulation (all Tier 1)

**Sinclair BASIC Knowledge:**
- CHR$ function
- USR function for address access
- FOR loops for data entry

## Key Concepts Introduced

### UDG Address Space
Characters 144-164 (21 chars) can be redefined. Each is 8 bytes (8×8 pixels). UDG data starts at address 65368 (USR "a" gives address).

### Binary to Byte Pattern
Each byte defines one pixel row. Binary 10000001 = decimal 129 = pixel pattern ⬛⚫⚫⚫⚫⚫⚫⬛.

### CHR$ Display
`CHR$ 144` prints first UDG. PRINT AT positions it on screen.

### Character-Based Maps
UDGs displayed as normal text. No slow PLOT/DRAW - instant PRINT AT. Perfect for tile-based games.

## Code Pattern

```basic
10 REM UDG Demo - Custom Character Graphics
20 REM Define UDG "a" (CHR$ 144) as smiley face
30
40 REM Get UDG base address
50 LET udg=USR "a"
60
70 REM Define character: 8 bytes for 8×8 pixels
80 REM Binary -> Decimal for each row
90 DATA 60,66,165,129,165,153,66,60
100
110 REM Load UDG data into memory
120 RESTORE 90
130 FOR n=0 TO 7
140   READ byte
150   POKE udg+n,byte
160 NEXT n
170
180 REM Display the UDG
190 CLS
200 PRINT AT 10,15;CHR$ 144
210
220 PAUSE 0
```

## Hardware Interaction

**Z80 CPU:**
- UDG memory at 65368-65535 (168 bytes for 21 chars)
- Screen memory 16384-22527 (6144 pixels + 768 attributes)
- ULA reads UDG patterns when rendering characters

**ULA (Uncommitted Logic Array):**
- Generates video signal
- Looks up character patterns from ROM or UDG RAM
- Characters 0-127 in ROM, 128-143 block graphics, 144-164 UDGs

**Performance:**
- PRINT AT + UDG = instant (< 1ms)
- PLOT/DRAW much slower (~10-20ms)
- UDG perfect for fast tile-based graphics

## Common Pitfalls

1. **Wrong address:** USR "a" not USR "A" (lowercase!)
2. **Binary confusion:** 11111111 is decimal 255, not 11111111
3. **Off-by-one:** Characters 144-164, not 144-165 (21 total)
4. **Forgetting RESTORE:** Reading wrong DATA if not reset
5. **Overwriting UDGs:** POKEing beyond 168 bytes crashes

## Extension Ideas

- Create full alphabet in UDG style
- Design tile set (wall, floor, door, key)
- Animated UDG (redefine same character)
- Inverse video tiles (swap INK/PAPER)
- Multi-character sprites (4 UDGs = 16×16)

## Builds Toward

**In This Tier:**
- L18: Complete tile sets
- L19: Character-based maps
- L20: Attribute management with UDGs
- L21: Maze game synthesis

## Quick Reference

### UDG Addresses
```basic
USR "a" = 65368  (CHR$ 144, first UDG)
USR "b" = 65376  (CHR$ 145)
...
USR "u" = 65528  (CHR$ 164, last UDG)
```

### Binary to Decimal Conversion
```
Binary      Decimal  Pattern
--------    -------  -------------
00000000  =    0    ⚫⚫⚫⚫⚫⚫⚫⚫
11111111  =  255    ⬛⬛⬛⬛⬛⬛⬛⬛
10000001  =  129    ⬛⚫⚫⚫⚫⚫⚫⬛
01000010  =   66    ⚫⬛⚫⚫⚫⚫⬛⚫
00111100  =   60    ⚫⚫⬛⬛⬛⬛⚫⚫
```

### Defining UDGs
```basic
REM Get character address
LET addr=USR "a"  : REM CHR$ 144

REM Define 8 bytes (8 rows)
FOR n=0 TO 7
  READ byte
  POKE addr+n,byte
NEXT n

REM DATA: 8 bytes for 8×8 pattern
DATA 60,66,165,129,165,153,66,60
```

### Displaying UDGs
```basic
REM Single character
PRINT AT 10,15;CHR$ 144

REM Multiple characters (string)
PRINT AT 5,0;CHR$ 144;CHR$ 145;CHR$ 146

REM Loop for tiles
FOR y=0 TO 10
  FOR x=0 TO 20
    PRINT AT y,x;CHR$ 144
  NEXT x
NEXT y
```

### Creating Tile Patterns

**Solid wall:**
```basic
DATA 255,255,255,255,255,255,255,255
```

**Brick pattern:**
```basic
DATA 255,129,129,129,255,132,132,132
```

**Checkerboard:**
```basic
DATA 170,85,170,85,170,85,170,85
```

**Circle:**
```basic
DATA 60,66,129,129,129,129,66,60
```

### Multi-Character Sprites

**16×16 sprite = 4 UDGs:**
```basic
REM Top-left, top-right
REM Bottom-left, bottom-right

PRINT AT y,x;CHR$ 144;CHR$ 145
PRINT AT y+1,x;CHR$ 146;CHR$ 147
```

### Calculating Binary Values

**Quick reference:**
```
Bit:  7 6 5 4 3 2 1 0
Val: 128 64 32 16 8 4 2 1

Examples:
10000001 = 128 + 1 = 129
11000011 = 128 + 64 + 2 + 1 = 195
00111100 = 32 + 16 + 8 + 4 = 60
```

### Animating UDGs
```basic
10 REM Redefine same UDG for animation
20 LET udg=USR "a"
30 FOR frame=1 TO 4
40   RESTORE frame*10+100
50   FOR n=0 TO 7
60     READ byte
70     POKE udg+n,byte
80   NEXT n
90   PAUSE 10
100 NEXT frame
110 GO TO 30
120
130 REM Frame 1
140 DATA 60,66,129,129,129,129,66,60
150 REM Frame 2
160 DATA 24,36,66,66,66,66,36,24
```

---

**Version:** 1.0
**Created:** 2025-10-27
