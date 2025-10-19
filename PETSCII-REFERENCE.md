# PETSCII Character Codes Reference

**For: Commodore 64 Programming**
**Updated:** 2025-01-18
**Source:** Official Commodore 64 Programmer's Reference Guide, Appendix C

---

## Overview

PETSCII (PET Standard Code of Information Interchange) is the character encoding used by Commodore computers. These are the codes used with:
- `PRINT CHR$(X)` - Print a character
- `ASC("x")` - Get the code for a character
- `GET A$` - Read keyboard input

**Important:** PETSCII codes are **different from screen codes** used with POKE to screen memory.

---

## Quick Start

```basic
PRINT CHR$(147)  : REM Clear screen
PRINT CHR$(5)    : REM White text color
PRINT CHR$(65)   : REM Print "A"
A=ASC("A")       : REM A=65
GET A$:IF A$<>"" THEN PRINT ASC(A$)  : REM Show key code
```

---

## Complete PETSCII Code Table

### Control Characters (0-31)

| Code | Function | Code | Function |
|------|----------|------|----------|
| 0 | CRSR ↓ (Cursor Down) | 17 | CRSR → (Cursor Right) |
| 1 | RVS ON (Reverse On) | 18 | RVS ON |
| 2 | CLR/HOME (Clear Screen) | 19 | CLR/HOME |
| 3 | INST/DEL | 20 | INST/DEL |
| 4 | (undefined) | 21 | (undefined) |
| 5 | WHT (White color) | 22 | (undefined) |
| 6 | (undefined) | 23 | (undefined) |
| 7 | (undefined) | 24 | (undefined) |
| 8 | Disable SHIFT+Commodore | 25 | (undefined) |
| 9 | Enable SHIFT+Commodore | 26 | (undefined) |
| 10 | (undefined) | 27 | (undefined) |
| 11 | RED (Red color) | 28 | RED |
| 12 | (undefined) | 29 | CRSR → (Right) |
| 13 | RETURN (Carriage Return) | 30 | GRN (Green color) |
| 14 | Switch to Lowercase | 31 | BLU (Blue color) |
| 15 | (undefined) | | |
| 16 | (undefined) | | |

### Printable Characters (32-95)

| Code | Char | Code | Char | Code | Char | Code | Char |
|------|------|------|------|------|------|------|------|
| 32 | SPACE | 48 | 0 | 64 | @ | 80 | P |
| 33 | ! | 49 | 1 | 65 | A | 81 | Q |
| 34 | " | 50 | 2 | 66 | B | 82 | R |
| 35 | # | 51 | 3 | 67 | C | 83 | S |
| 36 | $ | 52 | 4 | 68 | D | 84 | T |
| 37 | % | 53 | 5 | 69 | E | 85 | U |
| 38 | & | 54 | 6 | 70 | F | 86 | V |
| 39 | ' | 55 | 7 | 71 | G | 87 | W |
| 40 | ( | 56 | 8 | 72 | H | 88 | X |
| 41 | ) | 57 | 9 | 73 | I | 89 | Y |
| 42 | * | 58 | : | 74 | J | 90 | Z |
| 43 | + | 59 | ; | 75 | K | 91 | [ |
| 44 | , | 60 | < | 76 | L | 92 | £ |
| 45 | - | 61 | = | 77 | M | 93 | ] |
| 46 | . | 62 | > | 78 | N | 94 | ↑ |
| 47 | / | 63 | ? | 79 | O | 95 | ← |

### Graphics Characters (96-127)

| Code | Char | Code | Char | Code | Char | Code | Char |
|------|------|------|------|------|------|------|------|
| 96 | ▂ | 104 | ▕ | 112 | ▔ | 120 | ▀ |
| 97 | ♠ | 105 | ╮ | 113 | ● | 121 | ▔ |
| 98 | │ | 106 | ╰ | 114 | ─ | 122 | ♦ |
| 99 | ─ | 107 | ╯ | 115 | ♥ | 123 | ┼ |
| 100 | ─ | 108 | ◤ | 116 | │ | 124 | ╱ |
| 101 | ─ | 109 | ◥ | 117 | ◢ | 125 | │ |
| 102 | ─ | 110 | ╱ | 118 | ╳ | 126 | π |
| 103 | ▕ | 111 | ◣ | 119 | ○ | 127 | ◥ |

### Control & Color Characters (128-159)

| Code | Function | Code | Function |
|------|----------|------|----------|
| 128 | (undefined) | 145 | CRSR ↑ (Cursor Up) |
| 129 | Orange color | 146 | RVS OFF (Reverse Off) |
| 130 | (undefined) | 147 | CLR/HOME |
| 131 | (undefined) | 148 | INST/DEL |
| 132 | (undefined) | 149 | Brown color |
| 133 | F1 key | 150 | Light Red color |
| 134 | F3 key | 151 | Gray 1 color |
| 135 | F5 key | 152 | Gray 2 color |
| 136 | F7 key | 153 | Light Green color |
| 137 | F2 key | 154 | Light Blue color |
| 138 | F4 key | 155 | Gray 3 color |
| 139 | F6 key | 156 | Purple color |
| 140 | F8 key | 157 | ← CRSR (Cursor Left) |
| 141 | SHIFT+RETURN | 158 | Yellow color |
| 142 | Switch to Uppercase | 159 | Cyan color |
| 143 | (undefined) | | |
| 144 | Black color | | |

### Graphics Characters (160-191)

| Code | Char | Code | Char | Code | Char | Code | Char |
|------|------|------|------|------|------|------|------|
| 160 | SPACE | 168 | ▃ | 176 | ▄ | 184 | ▌ |
| 161 | ▌ | 169 | ▔ | 177 | ▀ | 185 | ▐ |
| 162 | ▄ | 170 | ▃ | 178 | ▀ | 186 | ▄ |
| 163 | ▔ | 171 | ▂ | 179 | ▃ | 187 | ▌ |
| 164 | ▁ | 172 | ▌ | 180 | ▂ | 188 | ▀ |
| 165 | ▕ | 173 | ◣ | 181 | ▔ | 189 | ▔ |
| 166 | ▒ | 174 | ▃ | 182 | ▁ | 190 | ▀ |
| 167 | ▃ | 175 | ▀ | 183 | ▔ | 191 | ▀ |

### Important Notes

**Codes 192-223:** Same as codes 96-127
**Codes 224-254:** Same as codes 160-190
**Code 255:** Same as code 126

---

## Color Control Codes

### Text Colors (Use with PRINT CHR$)

| Code | Color | Code | Color |
|------|-------|------|-------|
| 5 | White | 149 | Brown |
| 28 | Red | 150 | Light Red |
| 30 | Green | 151 | Gray 1 (Dark Gray) |
| 31 | Blue | 152 | Gray 2 (Medium Gray) |
| 129 | Orange | 153 | Light Green |
| 144 | Black | 154 | Light Blue |
| 156 | Purple | 155 | Gray 3 (Light Gray) |
| 158 | Yellow | | |
| 159 | Cyan | | |

**Example:**
```basic
PRINT CHR$(28);"RED TEXT";CHR$(30);"GREEN TEXT"
```

---

## Cursor Control Codes

| Code | Function | Code | Function |
|------|----------|------|----------|
| 0 | Cursor Down | 145 | Cursor Up |
| 17 | Cursor Right | 157 | Cursor Left |
| 19 | HOME (move to top-left) | 147 | CLR/HOME (clear screen) |

**Example - Position Cursor:**
```basic
10 PRINT CHR$(147);  : REM Clear screen
20 FOR I=1 TO 10
30 PRINT CHR$(17);   : REM Move right 10 spaces
40 NEXT I
50 PRINT "CENTERED"
```

---

## Character Set Control

| Code | Function |
|------|----------|
| 14 | Switch to lowercase/uppercase mode |
| 142 | Switch to uppercase/graphics mode (default) |

**Example:**
```basic
PRINT CHR$(14)  : REM Enable lowercase
PRINT "Hello World"
PRINT CHR$(142) : REM Back to uppercase
```

---

## Reverse Video

| Code | Function |
|------|----------|
| 18 | Reverse On (inverted colors) |
| 146 | Reverse Off (normal colors) |

**Example:**
```basic
PRINT CHR$(18);"REVERSED";CHR$(146);"NORMAL"
```

---

## Function Keys (F1-F8)

When read with GET, function keys return these codes:

| Key | Code | Key | Code |
|-----|------|-----|------|
| F1 | 133 | F2 | 137 |
| F3 | 134 | F4 | 138 |
| F5 | 135 | F6 | 139 |
| F7 | 136 | F8 | 140 |

**Example - Function Key Detection:**
```basic
10 GET A$:IF A$="" THEN 10
20 C=ASC(A$)
30 IF C=133 THEN PRINT "F1 PRESSED"
40 IF C=134 THEN PRINT "F3 PRESSED"
```

---

## Practical Examples

### Example 1: Clear Screen and Set Color

```basic
10 PRINT CHR$(147);    : REM Clear screen
20 PRINT CHR$(30);     : REM Green text
30 PRINT "HELLO WORLD"
```

### Example 2: Print Centered Text

```basic
10 T$="GAME OVER"
20 L=LEN(T$)
30 SP=(40-L)/2        : REM Calculate spaces
40 PRINT CHR$(147);   : REM Clear
50 FOR I=1 TO 12
60 PRINT             : REM Move down
70 NEXT I
80 FOR I=1 TO SP
90 PRINT CHR$(17);   : REM Move right
100 NEXT I
110 PRINT CHR$(28);T$ : REM Red text
```

### Example 3: Menu with Function Keys

```basic
10 PRINT CHR$(147);CHR$(5)
20 PRINT "MAIN MENU"
30 PRINT
40 PRINT "F1 - START GAME"
50 PRINT "F3 - LOAD GAME"
60 PRINT "F5 - QUIT"
70 GET A$:IF A$="" THEN 70
80 C=ASC(A$)
90 IF C=133 THEN PRINT "STARTING...":END
100 IF C=134 THEN PRINT "LOADING...":END
110 IF C=135 THEN PRINT "GOODBYE":END
120 GOTO 70
```

### Example 4: Print Colored Border

```basic
10 PRINT CHR$(147)
20 FOR I=1 TO 40
30 PRINT CHR$(28);CHR$(67);  : REM Red horizontal line
40 NEXT I
50 PRINT
```

### Example 5: Animated Text Colors

```basic
10 PRINT CHR$(147)
20 FOR C=5 TO 159 STEP 10
30 PRINT CHR$(19);       : REM Home cursor
40 PRINT CHR$(C);"RAINBOW TEXT"
50 FOR D=1 TO 100:NEXT D : REM Delay
60 NEXT C
70 GOTO 20
```

### Example 6: Reverse Video Effect

```basic
10 T$="FLASH!"
20 FOR F=1 TO 10
30 PRINT CHR$(19);       : REM Home
40 PRINT CHR$(18);T$;    : REM Reverse on
50 FOR D=1 TO 100:NEXT D
60 PRINT CHR$(19);       : REM Home
70 PRINT CHR$(146);T$;   : REM Reverse off
80 FOR D=1 TO 100:NEXT D
90 NEXT F
```

### Example 7: GET Character and Display Code

```basic
10 PRINT CHR$(147);"PRESS ANY KEY"
20 GET A$:IF A$="" THEN 20
30 C=ASC(A$)
40 PRINT "PETSCII CODE:";C
50 PRINT "CHARACTER: ";A$
60 GOTO 10
```

### Example 8: Print Box with Graphics

```basic
10 PRINT CHR$(147);CHR$(5)
20 PRINT CHR$(176);      : REM Top-left corner
30 FOR I=1 TO 10
40 PRINT CHR$(67);       : REM Horizontal
50 NEXT I
60 PRINT CHR$(174)       : REM Top-right corner
```

### Example 9: Convert Uppercase to Lowercase

```basic
10 INPUT "ENTER TEXT"; T$
20 PRINT CHR$(14);       : REM Switch to lowercase mode
30 FOR I=1 TO LEN(T$)
40 C=ASC(MID$(T$,I,1))
50 IF C>=65 AND C<=90 THEN C=C+32  : REM Convert
60 PRINT CHR$(C);
70 NEXT I
80 PRINT CHR$(142)       : REM Back to uppercase
```

### Example 10: Screen Saver Effect

```basic
10 PRINT CHR$(147);CHR$(144)  : REM Clear, black text
20 X=INT(RND(1)*40)
30 Y=INT(RND(1)*25)
40 C=INT(RND(1)*15)+129       : REM Random color
50 PRINT CHR$(19);            : REM Home
60 FOR I=1 TO Y:PRINT:NEXT I  : REM Move down
70 FOR I=1 TO X
80 PRINT CHR$(17);            : REM Move right
90 NEXT I
100 PRINT CHR$(C);CHR$(113)   : REM Colored circle
110 FOR D=1 TO 50:NEXT D
120 GOTO 20
```

---

## PETSCII vs Screen Codes

**Critical Difference:**

| Operation | Code Type | Example |
|-----------|-----------|---------|
| `PRINT CHR$(65)` | PETSCII | Displays "A" |
| `POKE 1024,65` | Screen Code | Displays "A" (but code 65 = "A" in screen, 1 in PETSCII) |
| `ASC("A")` | Returns PETSCII | Returns 65 |
| `PEEK(1024)` | Returns Screen Code | Returns 1 if "A" is displayed |

**Conversion Example:**
```basic
10 REM Print "A" using POKE
20 P=ASC("A")        : REM PETSCII code = 65
30 S=P-64            : REM Convert to screen code = 1
40 POKE 1024,S       : REM Display at top-left
```

---

## GET Statement and PETSCII

The GET statement returns PETSCII codes:

```basic
10 GET A$
20 IF A$="" THEN 10              : REM No key pressed
30 C=ASC(A$)                     : REM Get PETSCII code
40 IF C=13 THEN PRINT "RETURN"   : REM Return key
50 IF C=32 THEN PRINT "SPACE"    : REM Space bar
60 IF C>=65 AND C<=90 THEN PRINT "LETTER" : REM A-Z
```

---

## Common Character Ranges

### Uppercase Letters (A-Z)
- **PETSCII:** 65-90
- **Screen Code:** 1-26

### Lowercase Letters (a-z)
- **PETSCII:** 97-122 (in lowercase mode)
- **Screen Code:** 1-26 (Set 2)

### Numbers (0-9)
- **PETSCII:** 48-57
- **Screen Code:** 48-57 (same)

### Punctuation (!-/)
- **PETSCII:** 33-47
- **Screen Code:** 33-47 (same)

### Graphics Characters
- **PETSCII:** 96-127, 160-191, 192-223, 224-254
- **Screen Code:** Different mapping (see SCREEN-CODES-REFERENCE.md)

---

## Special Character Notes

### Commodore-Specific Characters

- **£ (Pound Sign):** PETSCII 92, Screen Code 28
- **↑ (Up Arrow):** PETSCII 94, Screen Code 30
- **← (Left Arrow):** PETSCII 95, Screen Code 31
- **π (Pi):** PETSCII 126, Screen Code 94

### Shifted Characters

When SHIFT is held, many keys produce graphics characters (PETSCII 96-127).

---

## Quick Reference Card

```
CONTROL CODES
Clear Screen:  CHR$(147)
Home:          CHR$(19)
Cursor Down:   CHR$(0)   or CHR$(17)
Cursor Right:  CHR$(17)  or CHR$(29)
Cursor Up:     CHR$(145)
Cursor Left:   CHR$(157)
Return:        CHR$(13)

COLOR CODES
White:      CHR$(5)     Cyan:      CHR$(159)
Red:        CHR$(28)    Purple:    CHR$(156)
Green:      CHR$(30)    Yellow:    CHR$(158)
Blue:       CHR$(31)    Orange:    CHR$(129)
Black:      CHR$(144)   Brown:     CHR$(149)

REVERSE VIDEO
On:  CHR$(18)
Off: CHR$(146)

CHARACTER SET
Lowercase Mode:  CHR$(14)
Uppercase Mode:  CHR$(142)

LETTERS (PETSCII)
A-Z: 65-90
a-z: 97-122 (lowercase mode)

NUMBERS: 48-57 (0-9)
SPACE: 32
```

---

## References

- **Official Documentation:** Commodore 64 Programmer's Reference Guide, Appendix C
- **Related:** See SCREEN-CODES-REFERENCE.md for screen memory codes
- **Related:** See PETSCII-SCREEN-CODES.md for conversion between systems

---

**Document Version:** 1.0
**Last Updated:** 2025-01-18
**Based on:** Official Commodore Technical Specifications
