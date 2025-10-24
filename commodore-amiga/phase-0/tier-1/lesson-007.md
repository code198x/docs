# Lesson 007: First BOB

**Arc:** BOB Graphics
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 30 lines of code

## Learning Objectives

- Understand BOBs (Blitter OBjects)
- Create and display sprite graphics
- Master Screen Open and screen modes
- Experience hardware-accelerated graphics

## Key Concepts Introduced

### BOBs (Blitter OBjects)
BOBs are AMOS's sprite system using the Amiga's hardware blitter for fast graphics. Not the same as Amiga's 8 hardware sprites.

### Screen Modes
Screen Open creates display. Common modes: Low-res (320×256, 32 colours), High-res (640×256, 16 colours).

### Get Bob / Paste Bob
Get Bob captures screen area as BOB image. Paste Bob displays it at coordinates.

### Double Buffering
Screen Swap and Autoback for flicker-free animation (built into AMOS).

## Code Pattern

```amos
' Open screen and create BOB
Screen Open 0,320,256,32,Lowres
Curs Off: Cls 0: Flash Off

' Draw a simple shape
Ink 2: Bar 0,0 To 15,15
Ink 3: Circle 8,8,6

' Capture as BOB #1
Get Bob 1,0,0 To 16,16

' Display the BOB
Paste Bob 100,100,1

Wait Key
```

## Quick Reference

- `Screen Open id,width,height,colours,mode` - Create screen
- `Get Bob number,x1,y1 To x2,y2` - Capture BOB
- `Paste Bob x,y,number` - Display BOB
- `Curs Off` - Hide text cursor
- `Flash Off` - Disable cursor flash

**Chips Used:** Blitter (hardware copy), Agnus (memory management)

---

**Version:** 1.0
**Created:** 2025-10-24
