# Lesson 007: First Pixels

**Arc:** Character Graphics
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 15 lines of code

## Learning Objectives

- Use PLOT to draw individual pixels
- Understand Spectrum's coordinate system (0,0 to 255,175)
- Draw simple shapes with loops
- Experience instant graphics response

## Key Concepts Introduced

### PLOT Command
PLOT x,y turns on a pixel at coordinates (x,y). X is horizontal (0-255), Y is vertical (0-175, inverted - 0 at bottom).

### Graphics Coordinates
Unlike PRINT AT (character blocks), PLOT uses pixel coordinates for fine control.

### Drawing Loops
Use FOR loops to draw lines, boxes, or patterns pixel by pixel.

## Code Pattern

```basic
10 FOR x=0 TO 255
20 PLOT x,87
30 NEXT x
40 FOR y=0 TO 175
50 PLOT 128,y
60 NEXT y
```

## Quick Reference

- `PLOT x,y` - Draw pixel (x: 0-255, y: 0-175)
- `PLOT INK colour;x,y` - Draw in specific colour
- Y coordinates: 0=bottom, 175=top (inverted!)
- 256×176 pixels total

---

**Version:** 1.0
**Created:** 2025-10-24
