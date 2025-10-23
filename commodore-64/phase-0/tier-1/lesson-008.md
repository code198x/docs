# Lesson 008: Screen Painter

**Arc:** Visual Creation
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 20 lines of code

## Learning Objectives

- Directly manipulate screen memory
- Understand screen memory layout (1000 bytes, 40×25)
- Create patterns by POKEing character codes
- Learn the relationship between screen position and memory address

## Prerequisites

**From Previous Lessons:**
- POKE command basics (L7)
- Loops and variables (L1-3)
- Hardware control concepts (L7)

**BASIC Knowledge:**
- FOR/NEXT loops
- POKE command
- Arithmetic for address calculation

## Key Concepts Introduced

### Screen Memory
Screen memory starts at address 1024. Each byte controls one screen character. 40 columns × 25 rows = 1000 bytes total (1024-2023).

### Character Codes
Each number represents a character: 1=A, 2=B, 32=space, 42=asterisk, 81=filled block. PETSCII defines these mappings.

### Position to Address Calculation
To POKE position (X,Y): `ADDR = 1024 + (Y * 40) + X`. This converts row/column to memory address.

### Direct Screen Drawing
Unlike PRINT (which uses the operating system), POKEing screen memory is instant and gives pixel-level control.

## Code Pattern

```basic
10 REM Draw horizontal line
20 FOR X=0 TO 39
30 POKE 1024+X,42
40 NEXT X
50 REM Draw vertical line
60 FOR Y=0 TO 24
70 POKE 1024+(Y*40),42
80 NEXT Y
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Reads screen memory and displays characters

**Memory Addresses:**
- `1024-2023` ($0400-$07E7) - Screen memory (1000 bytes)
- `55296-56295` ($D800-$DBE7) - Colour memory (1000 bytes)

**Screen Layout:**
```
Row 0: 1024-1063   (40 characters)
Row 1: 1064-1103   (40 characters)
Row 2: 1104-1143   (40 characters)
...
Row 24: 1984-2023  (40 characters)
```

## Common Pitfalls

1. **Address calculation errors:** Row 5 is NOT 1024+5, it's 1024+(5*40)=1224
2. **Out of bounds:** POKEing beyond 2023 writes to other memory (potential crash)
3. **Wrong character codes:** Need PETSCII reference for character numbers
4. **Colour memory separate:** POKEing 1024 changes character, not colour

## Extension Ideas

- Draw different patterns (checkerboard, diagonal lines, boxes)
- Fill entire screen with one character
- Create animated patterns (changing characters over time)
- Draw simple graphics (smiley face, house)
- Combine with L7's colour control for coloured patterns

## Builds Toward

**In This Tier:**
- L9: Interactive PETSCII tool with GET input
- L12-14: Screen-based character movement

**In Next Tier:**
- Sprites will replace screen characters for smooth animation
- But understanding screen memory helps with backgrounds and HUDs

## Quick Reference

**Screen Memory Formulas:**
- Address for position (X,Y): `1024 + (Y * 40) + X`
- Address for row Y: `1024 + (Y * 40)`
- Entire screen: FOR I=1024 TO 2023

**Useful Character Codes:**
- `32` - Space (blank)
- `42` - Asterisk
- `81` - Filled block (█)
- `160` - Solid block (different reverse video)
- `65-90` - Letters (but shifted in PETSCII)

**Common Patterns:**
```basic
REM Horizontal line at row Y
100 FOR X=0 TO 39
110 POKE 1024+(Y*40)+X,C
120 NEXT X

REM Vertical line at column X
200 FOR Y=0 TO 24
210 POKE 1024+(Y*40)+X,C
220 NEXT Y

REM Fill entire screen with character C
300 FOR I=1024 TO 2023
310 POKE I,C
320 NEXT I
```

**See Reference:**
`/docs/PETSCII-AND-SCREEN-CODES.md` for complete character code table
