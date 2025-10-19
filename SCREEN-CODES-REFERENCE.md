# C64 Screen Display Codes Reference

**For: Commodore 64 Programming**
**Updated:** 2025-01-18
**Source:** Official Commodore 64 Programmer's Reference Guide, Appendix B

---

## Overview

Screen display codes are the values you **POKE into screen memory** (locations 1024-2023) to display characters. These are **different from PETSCII codes** used with PRINT and CHR$().

**Critical:** This document shows **screen codes** (for POKE), not PETSCII codes (for PRINT).

---

## Quick Start

```basic
REM Display a solid circle (●) at screen position 1504
POKE 1504,81    : REM Screen code 81 = circle

REM Set its color to yellow (color code 7)
POKE 55776,7    : REM Color memory offset matches screen memory
```

**Memory Layout:**
- **Screen Memory:** 1024-2023 (1000 locations for 40×25 screen)
- **Color Memory:** 55296-56295 (1000 locations, one per character)

---

## Character Sets

The C64 has **two character sets**, but only one can be active at a time:

### Set 1: Uppercase/Graphics (Default)
- Uppercase letters A-Z
- Numbers, punctuation
- Graphics characters (boxes, symbols)

### Set 2: Uppercase/Lowercase
- Uppercase letters A-Z
- Lowercase letters a-z
- Some graphics replaced with lowercase

**Switching Character Sets:**
```basic
POKE 53272,21  : REM Set 1 (uppercase/graphics) - DEFAULT
POKE 53272,23  : REM Set 2 (uppercase/lowercase)
```

**Keyboard:** Hold SHIFT + Commodore key to toggle sets

---

## Reverse Characters

**Any character can be displayed in reverse video** by adding 128 to its screen code.

```basic
POKE 1024,1    : REM Normal "A"
POKE 1024,129  : REM Reversed "A" (1 + 128)

POKE 1024,81   : REM Normal circle
POKE 1024,209  : REM Reversed circle (81 + 128)
```

**Range:** Codes 128-255 are reversed versions of codes 0-127.

---

## Complete Screen Code Table

### Letters (Set 1 = Uppercase, Set 2 = Lowercase)

| Code | Set 1 | Set 2 | Code | Set 1 | Set 2 | Code | Set 1 | Set 2 |
|------|-------|-------|------|-------|-------|------|-------|-------|
| 0 | @ | @ | 9 | I | i | 18 | R | r |
| 1 | A | a | 10 | J | j | 19 | S | s |
| 2 | B | b | 11 | K | k | 20 | T | t |
| 3 | C | c | 12 | L | l | 21 | U | u |
| 4 | D | d | 13 | M | m | 22 | V | v |
| 5 | E | e | 14 | N | n | 23 | W | w |
| 6 | F | f | 15 | O | o | 24 | X | x |
| 7 | G | g | 16 | P | p | 25 | Y | y |
| 8 | H | h | 17 | Q | q | 26 | Z | z |

### Special Characters & Symbols

| Code | Set 1 | Set 2 | Description |
|------|-------|-------|-------------|
| 27 | [ | [ | Left bracket |
| 28 | £ | £ | Pound sign |
| 29 | ] | ] | Right bracket |
| 30 | ↑ | ↑ | Up arrow |
| 31 | ← | ← | Left arrow |
| 32 | SPACE | SPACE | Space character |

### Numbers & Punctuation

| Code | Char | Code | Char | Code | Char |
|------|------|------|------|------|------|
| 33 | ! | 44 | , | 55 | 7 |
| 34 | " | 45 | - | 56 | 8 |
| 35 | # | 46 | . | 57 | 9 |
| 36 | $ | 47 | / | 58 | : |
| 37 | % | 48 | 0 | 59 | ; |
| 38 | & | 49 | 1 | 60 | < |
| 39 | ' | 50 | 2 | 61 | = |
| 40 | ( | 51 | 3 | 62 | > |
| 41 | ) | 52 | 4 | 63 | ? |
| 42 | * | 53 | 5 | 64 | ─ |
| 43 | + | 54 | 6 |  |  |

### Graphics Characters (Set 1 Only)

**Common Box-Drawing Characters:**

| Code | Char | Description | Code | Char | Description |
|------|------|-------------|------|------|-------------|
| 66 | ▕ | Vertical line (right) | 76 | ▏ | Vertical line (left) |
| 67 | ─ | Horizontal line | 77 | ╲ | Diagonal line |
| 68 | ═ | Double horizontal | 78 | ╱ | Diagonal line |
| 69 | ═ | Double horizontal (thick) | 79 | ╲ | Corner piece |
| 70 | ═ | Triple horizontal | 80 | ▕ | Vertical line |
| 71 | ▕ | Vertical bar | 81 | ● | Filled circle |
| 72 | ▕ | Vertical bar (thick) | 82 | ▔ | Horizontal line (top) |
| 73 | ╮ | Top-right corner | 83 | ♥ | Heart |
| 74 | ╰ | Bottom-left corner | 84 | ▏ | Vertical line |
| 75 | ╯ | Bottom-right corner | 85 | ╭ | Top-left corner |

**Additional Graphics:**

| Code | Char | Description | Code | Char | Description |
|------|------|-------------|------|------|-------------|
| 86 | ╳ | Diagonal cross | 97 | ▕ | Vertical bar |
| 87 | ○ | Open circle | 98 | ▔ | Horizontal bar |
| 88 | ♣ | Club | 99-104 | Various | Box pieces |
| 89 | ▏ | Vertical line | 105 | ◢ | Triangle (Set 2: ◣) |
| 90 | ♦ | Diamond | 106-121 | Various | Box/line pieces |
| 91 | ┼ | Cross | 122 | ▄ | Lower half block (Set 2: ✓) |
| 92 | ▌ | Left half | 123-127 | Various | Box pieces |
| 93 | │ | Vertical line |  |  |  |
| 94 | ▓ | Checkerboard (Set 2: ░) |  |  |  |
| 95 | ▒ | Checkerboard pattern (Set 2: ▒) |  |  |  |
| 96 | SPACE | Blank space |  |  |  |

**Note:** Codes 128-255 display the same characters in **reverse video** (add 128 to any code above).

---

## Common Graphics for Games

### Essential Box Drawing

```basic
REM Complete box outline codes
10 TL=85  : REM ╭ Top-left corner
20 TR=73  : REM ╮ Top-right corner
30 BL=74  : REM ╰ Bottom-left corner
40 BR=75  : REM ╯ Bottom-right corner
50 HZ=67  : REM ─ Horizontal line
60 VT=93  : REM │ Vertical line
```

### Game Symbols

```basic
REM Common game graphics
10 PLAYER=81   : REM ● Player character
20 ENEMY=90    : REM ♦ Enemy
30 HEART=83    : REM ♥ Lives/health
40 CLUB=88     : REM ♣ Item/pickup
50 BULLET=46   : REM . Projectile
60 WALL=160    : REM █ Solid wall (reverse space = 32+128)
```

### Block Characters

```basic
REM Half-block characters for terrain
10 TOPBLOCK=163    : REM ▀ Upper half
20 BOTTOMBLOCK=164 : REM ▄ Lower half
30 LEFTBLOCK=161   : REM ▌ Left half
40 RIGHTBLOCK=162  : REM ▐ Right half
50 FULLBLOCK=160   : REM █ Full block (reverse space)
```

---

## Color Memory

Each screen position (1024-2023) has a corresponding color memory location (55296-56295).

**Formula:**
```
Color Address = Screen Address - 1024 + 55296
```

**Example:**
```basic
REM Display red "A" at top-left of screen
POKE 1024,1     : REM Screen code 1 = "A"
POKE 55296,2    : REM Color code 2 = red
```

**Color Codes (0-15):**
| Code | Color | Code | Color |
|------|-------|------|-------|
| 0 | Black | 8 | Orange |
| 1 | White | 9 | Brown |
| 2 | Red | 10 | Light Red |
| 3 | Cyan | 11 | Dark Gray |
| 4 | Purple | 12 | Medium Gray |
| 5 | Green | 13 | Light Green |
| 6 | Blue | 14 | Light Blue |
| 7 | Yellow | 15 | Light Gray |

---

## Important Notes

### Characters That Are the Same in Both Sets

The following codes display **identical characters** in Set 1 and Set 2:
- Code 1 (always different: @ vs a)
- Codes 27-64 (symbols and numbers)
- Codes 91-93 (brackets, arrows)
- Codes 96-104 (graphics)
- Codes 106-121 (graphics)
- Codes 123-127 (graphics)

### Common Mistakes

❌ **Using PETSCII codes with POKE**
```basic
POKE 1024,65  : REM Displays @ (not A!)
```

✅ **Using screen codes with POKE**
```basic
POKE 1024,1   : REM Displays A (correct)
```

❌ **Forgetting color memory**
```basic
POKE 1024,81  : REM Circle appears in last color used
```

✅ **Setting color and character**
```basic
POKE 1024,81   : REM Screen code (circle)
POKE 55296,7   : REM Color code (yellow)
```

---

## Practical Examples

### Display Text Using Screen Codes

```basic
10 REM "HELLO" using screen codes
20 DATA 8,5,12,12,15
30 FOR I=0 TO 4
40 READ C
50 POKE 1024+I,C
60 NEXT I
```

### Draw a Simple Box

```basic
10 REM Draw 10x5 box at top-left
20 POKE 1024,85       : REM Top-left corner
30 FOR I=1 TO 8
40 POKE 1024+I,67     : REM Horizontal line
50 NEXT I
60 POKE 1024+9,73     : REM Top-right corner
70 FOR R=1 TO 3
80 POKE 1024+(R*40),93    : REM Left side
90 POKE 1024+(R*40)+9,93  : REM Right side
100 NEXT R
110 POKE 1024+(4*40),74   : REM Bottom-left
120 FOR I=1 TO 8
130 POKE 1024+(4*40)+I,67 : REM Bottom line
140 NEXT I
150 POKE 1024+(4*40)+9,75 : REM Bottom-right
```

### Fill Screen with Pattern

```basic
10 REM Checkerboard pattern
20 FOR I=1024 TO 2023
30 POKE I,102         : REM Checkerboard character
40 POKE I+54272,1     : REM White color
50 NEXT I
```

### Create Reverse Video Text

```basic
10 REM "GAME OVER" in reverse
20 FOR I=0 TO 8
30 READ C
40 POKE 1024+480+I,C+128  : REM Add 128 for reverse
50 POKE 55296+480+I,1     : REM White
60 NEXT I
70 DATA 7,1,13,5,32,15,22,5,18
REM     G A M  E    O  V  E R
```

---

## Converting PETSCII to Screen Codes

If you need to convert PETSCII (from ASC() or user input) to screen codes:

```basic
10 REM PETSCII TO SCREEN CODE CONVERTER
20 INPUT "CHARACTER"; C$
30 P=ASC(C$)           : REM Get PETSCII code
40 REM Convert to screen code
50 IF P>=64 AND P<=95 THEN S=P-64:GOTO 100
60 IF P>=96 AND P<=127 THEN S=P-32:GOTO 100
70 IF P>=192 AND P<=223 THEN S=P-128:GOTO 100
80 S=P : REM Unchanged
100 PRINT "SCREEN CODE: ";S
110 POKE 1024,S        : REM Display it
```

---

## Screen Memory Layout

**40 columns × 25 rows = 1000 characters**

| Row | Start Address | Calculation |
|-----|---------------|-------------|
| 0 (top) | 1024 | 1024 + (0 × 40) |
| 1 | 1064 | 1024 + (1 × 40) |
| 2 | 1104 | 1024 + (2 × 40) |
| ... | ... | ... |
| 12 (middle) | 1504 | 1024 + (12 × 40) |
| ... | ... | ... |
| 24 (bottom) | 1984 | 1024 + (24 × 40) |

**Formula for position:**
```
Address = 1024 + (Row × 40) + Column
```

**Example - Row 10, Column 15:**
```basic
10 ROW=10:COL=15
20 ADDR=1024+(ROW*40)+COL
30 POKE ADDR,81      : REM Display circle
40 POKE ADDR+54272,7 : REM Yellow color
```

---

## Quick Reference Card

```
Screen Memory:    1024 - 2023   (1000 bytes)
Color Memory:     55296 - 56295 (1000 bytes)

Character Sets:
  POKE 53272,21   Uppercase/Graphics (Set 1)
  POKE 53272,23   Uppercase/Lowercase (Set 2)

Common Screen Codes:
  Space    = 32       Circle ● = 81
  @ (Set1) = 0        Heart ♥  = 83
  A-Z      = 1-26     Diamond ♦= 90
  a-z      = 1-26 (Set 2 only)
  0-9      = 48-57    Horizontal ─ = 67
  Box TL ╭ = 85       Vertical │ = 93
  Box TR ╮ = 73       Full block █ = 160 (reverse space)
  Box BL ╰ = 74
  Box BR ╯ = 75

Reverse Video: Add 128 to any code (0-127 → 128-255)

Position Formula: 1024 + (Row × 40) + Column
Color Formula:    55296 + (Row × 40) + Column
```

---

## References

- **Official Documentation:** Commodore 64 Programmer's Reference Guide, Appendix B
- **Related:** See PETSCII-SCREEN-CODES.md for PETSCII vs Screen Code conversion
- **Screen Layout:** Appendix D (Screen and Color Memory Maps)

---

**Document Version:** 1.0
**Last Updated:** 2025-01-18
**Based on:** Official Commodore Technical Specifications
