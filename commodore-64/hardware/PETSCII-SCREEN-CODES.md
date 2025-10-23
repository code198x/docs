# C64 PETSCII & Screen Code Reference

**Quick Reference Guide for Commodore 64 Character Codes**

## Understanding the Different Code Systems

The C64 uses three different character encoding systems:

1. **PETSCII** - What you use with PRINT, CHR$(), and ASC()
2. **Screen Codes** - What you POKE to screen memory (1024-2023)
3. **ASCII** - For reference (differs from both PETSCII and screen codes)

## Critical Differences

- `PRINT "A"` uses PETSCII code 65
- `POKE 1024,1` uses screen code 1 (displays "A")
- Screen codes 0-63 are the SAME characters as PETSCII 64-127 (uppercase/graphics)
- Screen codes 128-255 are the SAME characters as PETSCII 192-255 (shifted/graphics)

## Common Characters (Uppercase Mode)

| Character | PETSCII | Screen Code | Notes |
|-----------|---------|-------------|-------|
| Space | 32 | 32 | Same in both |
| ! | 33 | 33 | Same in both |
| " | 34 | 34 | Same in both |
| # | 35 | 35 | Same in both |
| $ | 36 | 36 | Same in both |
| % | 37 | 37 | Same in both |
| & | 38 | 38 | Same in both |
| ' | 39 | 39 | Same in both |
| ( | 40 | 40 | Same in both |
| ) | 41 | 41 | Same in both |
| * | 42 | 42 | Same in both |
| + | 43 | 43 | Same in both |
| , | 44 | 44 | Same in both |
| - | 45 | 45 | Same in both |
| . | 46 | 46 | Same in both |
| / | 47 | 47 | Same in both |
| 0-9 | 48-57 | 48-57 | Same in both |
| : | 58 | 58 | Same in both |
| ; | 59 | 59 | Same in both |
| < | 60 | 60 | Same in both |
| = | 61 | 61 | Same in both |
| > | 62 | 62 | Same in both |
| ? | 63 | 63 | Same in both |

## Alphabetic Characters (Uppercase Mode)

| Character | PETSCII | Screen Code | Notes |
|-----------|---------|-------------|-------|
| @ | 64 | 0 | **Different!** |
| A | 65 | 1 | **Different!** |
| B | 66 | 2 | **Different!** |
| C | 67 | 3 | **Different!** |
| D | 68 | 4 | **Different!** |
| E | 69 | 5 | **Different!** |
| F | 70 | 6 | **Different!** |
| G | 71 | 7 | **Different!** |
| H | 72 | 8 | **Different!** |
| I | 73 | 9 | **Different!** |
| J | 74 | 10 | **Different!** |
| K | 75 | 11 | **Different!** |
| L | 76 | 12 | **Different!** |
| M | 77 | 13 | **Different!** |
| N | 78 | 14 | **Different!** |
| O | 79 | 15 | **Different!** |
| P | 80 | 16 | **Different!** |
| Q | 81 | 17 | **Different!** |
| R | 82 | 18 | **Different!** |
| S | 83 | 19 | **Different!** |
| T | 84 | 20 | **Different!** |
| U | 85 | 21 | **Different!** |
| V | 86 | 22 | **Different!** |
| W | 87 | 23 | **Different!** |
| X | 88 | 24 | **Different!** |
| Y | 89 | 25 | **Different!** |
| Z | 90 | 26 | **Different!** |

## Graphic Characters (Critical for Games)

**IMPORTANT**: Box-drawing characters require SHIFTED PETSCII codes (letter + 128)

| Character | PETSCII | Screen Code | Description |
|-----------|---------|-------------|-------------|
| ● | 81 | 81 | Filled circle (same) |
| ○ | 87 | 87 | Open circle (same) |
| ♥ | 83 | 83 | Heart (same) |
| ♦ | 90 | 90 | Diamond |
| ♣ | 88 | 88 | Club (same) |
| ♠ | 65 | 65 | Spade |
| █ | 160 | 160 | Solid block (same) |
| ▌ | 161 | 161 | Left half block |
| ▐ | 162 | 162 | Right half block |
| ▄ | 163 | 163 | Lower half block |
| ▀ | 164 | 164 | Upper half block |
| ╭ | 213 | 85 | Top-left corner (SHIFT+U) |
| ╮ | 201 | 73 | Top-right corner (SHIFT+I) |
| ╯ | 203 | 75 | Bottom-right corner (SHIFT+K) |
| ╰ | 202 | 74 | Bottom-left corner (SHIFT+J) |
| ─ | 195 | 67 | Horizontal line (SHIFT+C) |
| │ | 221 | 93 | Vertical line (SHIFT+]) |
| ┼ | 219 | 91 | Cross (SHIFT+[) |
| ╳ | 214 | 86 | Diagonal cross (SHIFT+V) |
| ░ | 230 | 102 | Checkerboard |
| ▒ | 246 | 230 | Dense checkerboard |

## Conversion Rules

### PETSCII to Screen Code (Uppercase Mode)
```basic
IF P >= 0 AND P <= 31 THEN S = P + 128
IF P >= 32 AND P <= 63 THEN S = P
IF P >= 64 AND P <= 95 THEN S = P - 64
IF P >= 96 AND P <= 127 THEN S = P - 32
IF P >= 128 AND P <= 159 THEN S = P + 64
IF P >= 160 AND P <= 191 THEN S = P - 64
IF P >= 192 AND P <= 223 THEN S = P - 128
IF P >= 224 AND P <= 254 THEN S = P - 128
```

### Screen Code to PETSCII (Uppercase Mode)
```basic
IF S >= 0 AND S <= 31 THEN P = S + 64
IF S >= 32 AND S <= 63 THEN P = S
IF S >= 64 AND S <= 95 THEN P = S + 128
IF S >= 96 AND S <= 127 THEN P = S + 64
IF S >= 128 AND S <= 159 THEN P = S + 64
IF S >= 160 AND S <= 191 THEN P = S - 64
IF S >= 192 AND S <= 223 THEN P = S - 128
IF S >= 224 AND S <= 254 THEN P = S - 128
```

## Quick Reference Functions

### Convert PETSCII to Screen Code
```basic
10 REM PETSCII TO SCREEN CODE
20 INPUT "PETSCII CODE"; P
30 IF P>=64 AND P<=95 THEN S=P-64:GOTO 80
40 IF P>=96 AND P<=127 THEN S=P-32:GOTO 80
50 IF P>=192 AND P<=223 THEN S=P-128:GOTO 80
60 S=P
80 PRINT "SCREEN CODE: ";S
```

### Convert Screen Code to Character
```basic
10 REM SCREEN CODE TO CHARACTER
20 INPUT "SCREEN CODE"; S
30 IF S>=0 AND S<=31 THEN P=S+64:GOTO 70
40 IF S>=32 AND S<=63 THEN P=S:GOTO 70
50 P=S+128
70 PRINT CHR$(P);
```

## Common Mistakes

1. **Using PETSCII codes with POKE** - Won't work as expected
   - ❌ `POKE 1024,65` displays @ (not A)
   - ✅ `POKE 1024,1` displays A

2. **Using ASC() for screen codes** - ASC returns PETSCII, not screen codes
   - ❌ `POKE 1024,ASC("A")` displays @
   - ✅ `POKE 1024,ASC("A")-64` displays A

3. **Mixing code systems** - Keep them separate
   - `PRINT` = PETSCII
   - `POKE screen memory` = Screen codes
   - `POKE colour memory` = Colour values (0-15)

## Practical Examples

### Display "HELLO" using screen codes
```basic
10 DATA 8,5,12,12,15
20 FOR I=0 TO 4
30 READ C
40 POKE 1024+I,C
50 NEXT I
```

### Display "HELLO" using PETSCII conversion
```basic
10 A$="HELLO"
20 FOR I=1 TO 5
30 P=ASC(MID$(A$,I,1))
40 S=P-64
50 POKE 1024+I-1,S
60 NEXT I
```

### Draw a box using graphics characters
```basic
10 REM TOP-LEFT TO TOP-RIGHT
20 POKE 1024,85:REM TOP-LEFT CORNER
30 FOR I=1 TO 38:POKE 1024+I,67:NEXT:REM HORIZONTAL
40 POKE 1024+39,73:REM TOP-RIGHT CORNER
50 REM SIDES
60 FOR R=1 TO 23
70 POKE 1024+(R*40),93:REM LEFT SIDE
80 POKE 1024+(R*40)+39,93:REM RIGHT SIDE
90 NEXT R
100 REM BOTTOM
110 POKE 1024+(24*40),74:REM BOTTOM-LEFT
120 FOR I=1 TO 38:POKE 1024+(24*40)+I,67:NEXT
130 POKE 1024+(24*40)+39,75:REM BOTTOM-RIGHT
```

## Notes

- This reference covers **Uppercase/Graphics mode** (default C64 mode)
- Lowercase/Uppercase mode has different character mappings
- Switch modes with `POKE 53272,23` (uppercase/graphics) or `POKE 53272,21` (lowercase/uppercase)
- Colour memory (55296+) always uses values 0-15, not character codes

## References

- [C64 Wiki: PETSCII](https://www.c64-wiki.com/wiki/PETSCII)
- [C64 Wiki: Screen Code](https://www.c64-wiki.com/wiki/Screen_code)
- Original Commodore 64 Programmer's Reference Guide

---

**Last Updated:** 2025-01-18
**Version:** 1.0
