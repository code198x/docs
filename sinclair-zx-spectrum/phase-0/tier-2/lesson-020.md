# Lesson 020: Attribute Management with UDGs

**Arc:** UDG Graphics System
**Position:** Lesson 4 of 5 in arc
**Type:** Standard
**Estimated Completion:** 80 lines of code

## Learning Objectives
- Understand attribute memory and colour clash
- Set INK/PAPER/BRIGHT/FLASH for UDG tiles
- Work around colour limitations
- Create colourful game graphics within constraints

## Prerequisites
- UDG system (L17-18)
- Character maps (L19)
- PRINT AT and attributes (Tier 1)

## Key Concepts
**Attribute Blocks** - 8×8 pixel blocks share one colour
**Colour Clash** - Limitation where multiple sprites in same 8×8 block conflict
**Design Around Limitations** - Use attributes strategically
**ATTR Function** - Read/write attribute memory directly

## Code Pattern
```basic
10 REM Attribute control with UDGs
20 LET base=USR "a"
30 REM Define wall tile
40 FOR n=0 TO 7
50   READ byte
60   POKE base+n,byte
70 NEXT n
80 DATA 255,255,255,255,255,255,255,255
90 REM Draw with attributes
100 FOR y=0 TO 5
110   FOR x=0 TO 10
120     INK 2: PAPER 7: BRIGHT 1
130     PRINT AT y,x;CHR$ 144
140   NEXT x
150 NEXT y
160 REM Change attributes without redrawing
170 LET addr=22528+(5*32)+5: REM Attribute at row 5, col 5
180 POKE addr,71: REM INK 7, PAPER 0, BRIGHT 1
```

## Hardware
**Attribute Memory:** 22528-23295 (768 bytes)
**Format:** Bits 0-2=INK, 3-5=PAPER, 6=BRIGHT, 7=FLASH
**Formula:** `22528 + (row * 32) + col`

**Colour Clash:**
- ULA limitation: one attribute per 8×8 block
- Games work around this with careful sprite placement
- Use monochrome sprites or align to 8×8 grid

## Quick Reference
### Attribute Bits
```
Bit 7: FLASH (0=off, 1=on)
Bit 6: BRIGHT (0=normal, 1=bright)
Bits 5-3: PAPER colour (0-7)
Bits 2-0: INK colour (0-7)
```

### Colour Values
```
0=Black   4=Green
1=Blue    5=Cyan
2=Red     6=Yellow
3=Magenta 7=White
```

### Direct Attribute Access
```basic
REM Read attribute at row Y, col X
LET a=PEEK(22528+Y*32+X)

REM Write attribute
POKE 22528+Y*32+X,value

REM Decode attribute
LET ink=a-INT(a/8)*8
LET paper=INT(a/8)-INT(a/64)*8
LET bright=(a>=64 AND a<128)
LET flash=(a>=128)
```

---

**Version:** 1.0
**Created:** 2025-10-27
