# Lesson 008: Screen Artist

**Arc:** BOB Graphics
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 40 lines of code

## Learning Objectives

- Master Plot, Draw, Circle, Bar commands
- Use Ink, Paper, Cls for colours
- Understand Amiga's colour palette
- Create graphics for BOB capture

## Key Concepts Introduced

### Drawing Commands
Plot (point), Draw (line), Circle, Bar (filled rectangle), Box (outline). Hardware-accelerated.

### Colour System
Ink (foreground), Paper (background). 32 colours in low-res (0-31). Each colour is RGB value.

### Palette Programming
Colour command sets RGB values. `Colour 1,$F00` = red (R=15, G=0, B=0, range 0-15).

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Flash Off: Curs Off: Cls 0

' Set custom colours
Colour 1,$F00  ' Red
Colour 2,$0F0  ' Green
Colour 3,$00F  ' Blue

' Draw shapes
Ink 1: Bar 50,50 To 100,100
Ink 2: Circle 150,80,30
Ink 3: Box 200,50 To 250,100
Draw 0,0 To 319,255

Wait Key
```

## Quick Reference

- `Plot x,y` - Draw pixel
- `Draw x,y` - Line from last position
- `Circle x,y,radius` - Circle
- `Bar x1,y1 To x2,y2` - Filled rectangle
- `Box x1,y1 To x2,y2` - Outline rectangle
- `Colour index,$RGB` - Set palette (R,G,B: 0-F hex)

---

**Version:** 1.0
**Created:** 2025-10-24
