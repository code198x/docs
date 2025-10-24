# Lesson 008: Vector Artist

**Arc:** Character Graphics
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 20 lines of code

## Learning Objectives

- Use DRAW to create lines from current position
- Master CIRCLE for round shapes
- Understand INK, PAPER, BORDER for colours
- Learn BRIGHT and FLASH attributes

## Key Concepts Introduced

### DRAW Command
DRAW x,y draws a line from the last plot/draw position by x pixels horizontally and y pixels vertically (relative movement).

### CIRCLE Command
CIRCLE x,y,radius draws a circle centered at (x,y). Faster than plotting individual pixels.

### Colour Attributes
INK (foreground), PAPER (background), BORDER (screen edge) set colours. Each character block (8×8 pixels) has one INK and one PAPER colour.

### BRIGHT and FLASH
BRIGHT 1 makes colours more vivid. FLASH 1 makes them alternate between INK and PAPER.

## Code Pattern

```basic
10 PAPER 0: INK 2: BORDER 0: CLS
20 PLOT 128,88
30 DRAW 50,0
40 DRAW 0,50
50 DRAW -50,0
60 DRAW 0,-50
70 CIRCLE 128,88,30
80 BRIGHT 1: CIRCLE 128,88,40
```

## Quick Reference

- `DRAW x,y` - Relative line from last position
- `CIRCLE x,y,radius` - Draw circle
- `INK n` - Set foreground colour (0-7)
- `PAPER n` - Set background colour (0-7)
- `BORDER n` - Set border colour (0-7)
- `BRIGHT 0/1` - Normal/bright colours
- `FLASH 0/1` - Static/flashing

**Spectrum Colours:** 0=Black, 1=Blue, 2=Red, 3=Magenta, 4=Green, 5=Cyan, 6=Yellow, 7=White

---

**Version:** 1.0
**Created:** 2025-10-24
