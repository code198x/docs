# VIC-II Chip Technical Reference

**For: Commodore 64 Programming**
**Updated:** 2025-01-18
**Source:** Official Commodore 64 Programmer's Reference Guide, Appendix G

---

## Overview

The VIC-II (Video Interface Chip II) is the graphics display chip in the Commodore 64, responsible for sprites, scrolling, character/bitmap graphics, collision detection, and screen layout. It provides 8 hardware sprites, smooth scrolling, multiple graphics modes, and hardware collision detection.

---

## Memory Map

**Base Address:** 53248 ($D000)
**Address Range:** 53248 - 53294 ($D000 - $D01E)

### Complete Register Map

| Register | Decimal | Hex | Bits Used | Description |
|----------|---------|-----|-----------|-------------|
| 0 | 53248 | $D000 | 0-7 | Sprite 0 X Position (low 8 bits) |
| 1 | 53249 | $D001 | 0-7 | Sprite 0 Y Position |
| 2 | 53250 | $D002 | 0-7 | Sprite 1 X Position |
| 3 | 53251 | $D003 | 0-7 | Sprite 1 Y Position |
| 4 | 53252 | $D004 | 0-7 | Sprite 2 X Position |
| 5 | 53253 | $D005 | 0-7 | Sprite 2 Y Position |
| 6 | 53254 | $D006 | 0-7 | Sprite 3 X Position |
| 7 | 53255 | $D007 | 0-7 | Sprite 3 Y Position |
| 8 | 53256 | $D008 | 0-7 | Sprite 4 X Position |
| 9 | 53257 | $D009 | 0-7 | Sprite 4 Y Position |
| 10 | 53258 | $D00A | 0-7 | Sprite 5 X Position |
| 11 | 53259 | $D00B | 0-7 | Sprite 5 Y Position |
| 12 | 53260 | $D00C | 0-7 | Sprite 6 X Position |
| 13 | 53261 | $D00D | 0-7 | Sprite 6 Y Position |
| 14 | 53262 | $D00E | 0-7 | Sprite 7 X Position |
| 15 | 53263 | $D00F | 0-7 | Sprite 7 Y Position |
| 16 | 53264 | $D010 | 0-7 | Sprite X MSB (9th bit for horizontal position) |
| 17 | 53265 | $D011 | 0-7 | Vertical scroll & screen mode control |
| 18 | 53266 | $D012 | 0-7 | Raster counter (read/write) |
| 19 | 53267 | $D013 | 0-7 | Light pen X position (read-only) |
| 20 | 53268 | $D014 | 0-7 | Light pen Y position (read-only) |
| 21 | 53269 | $D015 | 0-7 | Sprite enable (on/off) |
| 22 | 53270 | $D016 | 0-7 | Horizontal scroll & screen mode control |
| 23 | 53271 | $D017 | 0-7 | Sprite vertical expansion (double height) |
| 24 | 53272 | $D018 | 1-7 | Memory pointers (screen & character) |
| 25 | 53273 | $D019 | 0, 3-7 | Interrupt request register |
| 26 | 53274 | $D01A | 0-3 | Interrupt request masks (enable) |
| 27 | 53275 | $D01B | 0-7 | Sprite-to-background priority |
| 28 | 53276 | $D01C | 0-7 | Sprite multicolor mode select |
| 29 | 53277 | $D01D | 0-7 | Sprite horizontal expansion (double width) |
| 30 | 53278 | $D01E | 0-7 | Sprite-to-sprite collision (read-only) |
| 31 | 53279 | $D01F | 0-7 | Sprite-to-background collision (read-only) |
| 32 | 53280 | $D020 | 0-3 | Border color |
| 33 | 53281 | $D021 | 0-3 | Background color 0 (main background) |

---

## Sprite Control

### Sprite Position (Registers 0-16)

The C64 has 8 hardware sprites (also called MOBs - Movable Object Blocks), each 24×21 pixels.

**Position Registers:**
- **X Position:** Registers 0-15 (even = X low byte, odd = Y)
- **X MSB:** Register 16 (bits 0-7 = 9th bit for sprites 0-7)

**X Coordinate Range:** 0-511 (9 bits total)
- Bits 0-7: Stored in sprite's X register (53248 + sprite*2)
- Bit 8: Stored in register 16 (53264)

**Y Coordinate Range:** 0-255 (8 bits)
- Stored in sprite's Y register (53249 + sprite*2)

**Example - Position Sprite 0:**
```basic
REM Sprite 0 at X=100, Y=50
POKE 53248,100  : REM X low byte
POKE 53249,50   : REM Y
REM Bit 8 of X is 0, so no change to register 16
```

**Example - Position Sprite 0 beyond X=255:**
```basic
REM Sprite 0 at X=300, Y=100
POKE 53248,44   : REM 300-256=44
POKE 53249,100  : REM Y
POKE 53264,1    : REM Set bit 0 (sprite 0's 9th X bit)
```

### Sprite Enable (Register 21 / $D015)

Each bit enables one sprite:
- Bit 0 = Sprite 0
- Bit 1 = Sprite 1
- ...
- Bit 7 = Sprite 7

**Common Values:**
- `1` = Enable sprite 0 only
- `3` = Enable sprites 0 and 1 (binary 00000011)
- `255` = Enable all 8 sprites (binary 11111111)

```basic
POKE 53269,1   : REM Enable sprite 0
POKE 53269,7   : REM Enable sprites 0, 1, 2
POKE 53269,255 : REM Enable all sprites
```

### Sprite Expansion (Registers 23, 29)

**Register 23 ($D017):** Vertical expansion (double height)
**Register 29 ($D01D):** Horizontal expansion (double width)

Each bit controls one sprite (bit 0 = sprite 0, etc.)

```basic
POKE 53271,1  : REM Double height for sprite 0
POKE 53277,1  : REM Double width for sprite 0
POKE 53271,255: REM Double height for all sprites
```

### Sprite Priority (Register 27 / $D01B)

Controls whether sprites appear in front or behind background graphics.

- Bit = 0: Sprite appears in FRONT of background
- Bit = 1: Sprite appears BEHIND background

```basic
POKE 53275,0   : REM All sprites in front
POKE 53275,1   : REM Sprite 0 behind background
POKE 53275,255 : REM All sprites behind background
```

### Sprite Multicolor Mode (Register 28 / $D01C)

Enables multicolor mode for individual sprites (4 colors instead of 2).

- Bit = 0: Hi-res sprite (2 colors: transparent + 1 color)
- Bit = 1: Multicolor sprite (4 colors: transparent + 3 colors)

```basic
POKE 53276,1   : REM Sprite 0 multicolor
POKE 53276,255 : REM All sprites multicolor
```

---

## Collision Detection

### Sprite-to-Sprite Collision (Register 30 / $D01E)

**Read-only register.** Each bit indicates which sprites have collided with each other.

- Bit 0 = Sprite 0 collided
- Bit 1 = Sprite 1 collided
- ...
- Bit 7 = Sprite 7 collided

**Reading clears the register**, so save the value immediately.

```basic
10 C=PEEK(53278)  : REM Read collision register
20 IF C AND 1 THEN PRINT "SPRITE 0 HIT!"
30 IF C AND 2 THEN PRINT "SPRITE 1 HIT!"
```

### Sprite-to-Background Collision (Register 31 / $D01F)

**Read-only register.** Each bit indicates which sprites have collided with background graphics.

```basic
10 C=PEEK(53279)  : REM Read background collision
20 IF C AND 1 THEN PRINT "SPRITE 0 HIT BACKGROUND!"
```

**Important:** Reading the register clears it, so always store in a variable first.

---

## Screen Control

### Vertical Scroll & Mode Control (Register 17 / $D011)

| Bit | Name | Description |
|-----|------|-------------|
| 0-2 | YSCL0-2 | Vertical fine scroll (0-7 pixels) |
| 3 | RSEL | Screen height: 0=24 rows, 1=25 rows |
| 4 | BLNK | Screen blanking: 0=blank, 1=display |
| 5 | BMM | Bitmap mode: 0=text, 1=bitmap |
| 6 | ECM | Extended color mode: 0=off, 1=on |
| 7 | RC8 | 9th bit of raster counter |

**Common Values:**
- `27` ($1B): Normal text mode, 25 rows, screen on
- `59` ($3B): Bitmap mode, 25 rows, screen on

```basic
POKE 53265,27  : REM Standard text mode
POKE 53265,59  : REM Bitmap graphics mode
```

### Horizontal Scroll & Mode Control (Register 22 / $D016)

| Bit | Name | Description |
|-----|------|-------------|
| 0-2 | XSCL0-2 | Horizontal fine scroll (0-7 pixels) |
| 3 | CSEL | Screen width: 0=38 columns, 1=40 columns |
| 4 | MCM | Multicolor mode: 0=off, 1=on |
| 5 | RST | Reset (unused in normal operation) |
| 6-7 | N.C. | Not connected |

**Common Values:**
- `8` ($08): Normal 40-column mode
- `24` ($18): Multicolor character mode

```basic
POKE 53270,8   : REM Standard 40-column mode
POKE 53270,24  : REM Multicolor text mode
```

### Memory Pointers (Register 24 / $D018)

Controls where the VIC-II reads screen and character data from.

| Bits | Name | Description |
|------|------|-------------|
| 1-3 | CB11-13 | Character memory location (8 possible banks) |
| 4-7 | VS10-13 | Screen memory location (16 possible locations) |
| 0 | N.C. | Not connected (always 0) |

**Screen Memory Formula:**
```
Screen Address = (PEEK(53272) AND 240) * 64
```

**Character Memory Formula:**
```
Character Address = (PEEK(53272) AND 14) * 1024
```

**Common Values:**
- `20` ($14): Screen at 1024, characters at 4096 (default)
- `21` ($15): Screen at 1024, characters at 6144

```basic
POKE 53272,20  : REM Default screen/char setup
POKE 53272,21  : REM Uppercase/lowercase charset
```

---

## Raster Control

### Raster Counter (Register 18 / $D012)

Current raster line being drawn (0-312 for PAL, 0-262 for NTSC).

**9-bit value:**
- Bits 0-7: Register 18 (53266)
- Bit 8: Bit 7 of register 17 (53265)

**Reading the current raster line:**
```basic
10 R=PEEK(53266)  : REM Get raster line
20 IF R=100 THEN PRINT "RASTER AT 100"
```

**Common use:** Raster interrupts for timing-sensitive graphics.

---

## Interrupts

### Interrupt Request (Register 25 / $D019)

**Read:** Shows which interrupt sources are active
**Write:** Clear interrupt flags (write 1 to clear)

| Bit | Name | Description |
|-----|------|-------------|
| 0 | RIRQ | Raster interrupt occurred |
| 1 | ISBC | Sprite-background collision interrupt |
| 2 | ISSC | Sprite-sprite collision interrupt |
| 3 | LPIRQ | Light pen interrupt |
| 7 | IRQ | Any VIC interrupt (OR of bits 0-3) |

```basic
REM Clear raster interrupt
POKE 53273,1
```

### Interrupt Masks (Register 26 / $D01A)

**Enable/disable interrupt sources** (1=enabled, 0=disabled)

| Bit | Name | Description |
|-----|------|-------------|
| 0 | MRIRQ | Enable raster interrupt |
| 1 | MISBC | Enable sprite-background collision interrupt |
| 2 | MISSC | Enable sprite-sprite collision interrupt |
| 3 | MLPI | Enable light pen interrupt |

```basic
POKE 53274,1  : REM Enable raster interrupts
POKE 53274,0  : REM Disable all VIC interrupts
```

---

## Light Pen

### Light Pen Position (Registers 19-20)

**Read-only registers** that latch X/Y coordinates when light pen triggers.

- Register 19 ($D013): Light pen X position (0-255)
- Register 20 ($D014): Light pen Y position (0-255)

```basic
10 LPX=PEEK(53267)  : REM Light pen X
20 LPY=PEEK(53268)  : REM Light pen Y
30 PRINT "LIGHT PEN AT";LPX;",";LPY
```

---

## Graphics Modes

### Text Mode (Default)

- 40×25 characters (or 38×25 with CSEL=0)
- Screen memory: 1000 bytes (character codes)
- Color memory: 55296-56295 ($D800-$DBE7) - 1000 bytes

```basic
POKE 53265,27  : REM Bit 5=0 (text mode)
POKE 53270,8   : REM 40 columns
```

### Multicolor Text Mode

- 40×25 characters with 4-color characters
- Reduced horizontal resolution (4×8 pixels per char)

```basic
POKE 53265,27  : REM Text mode
POKE 53270,24  : REM Bit 4=1 (multicolor)
```

### Bitmap Mode

- 320×200 pixels (hi-res) or 160×200 (multicolor)
- 8000 bytes of bitmap data

```basic
POKE 53265,59  : REM Bit 5=1 (bitmap mode)
POKE 53270,8   : REM Hi-res bitmap
```

### Extended Color Mode

- 40×25 characters
- 4 background colors selectable per character
- Only 64 unique character shapes (instead of 256)

```basic
POKE 53265,91  : REM Bit 6=1 (extended color)
POKE 53270,8   : REM 40 columns
```

---

## Common Operations

### Enable a Sprite

```basic
10 REM Enable sprite 0 at position 100,100
20 POKE 2040,13        : REM Sprite pointer (sprite data at 832)
30 POKE 53248,100      : REM X position
40 POKE 53249,100      : REM Y position
50 POKE 53287,1        : REM Sprite 0 color (white)
60 POKE 53269,1        : REM Enable sprite 0
```

### Detect Sprite Collision

```basic
10 REM Check if sprite 0 hit anything
20 C=PEEK(53278)       : REM Sprite-sprite collision
30 B=PEEK(53279)       : REM Sprite-background collision
40 IF C AND 1 THEN PRINT "HIT ANOTHER SPRITE!"
50 IF B AND 1 THEN PRINT "HIT BACKGROUND!"
```

### Smooth Scrolling

```basic
10 REM Scroll screen right
20 FOR X=0 TO 7
30 POKE 53270,8+X      : REM Increase X scroll
40 FOR D=1 TO 50:NEXT  : REM Delay
50 NEXT X
```

### Change Screen Colors

```basic
POKE 53280,0  : REM Border = black
POKE 53281,6  : REM Background = blue
```

---

## Register Quick Reference

```
VIC-II Base: 53248 ($D000)

Sprite Positions: 53248-53263 (X/Y for sprites 0-7)
Sprite X MSB:     53264 (9th bit for X coords)
Sprite Enable:    53269
Sprite Expand Y:  53271
Sprite Expand X:  53277
Sprite Priority:  53275
Sprite Multicolor:53276
Sprite Colors:    53287-53294

Screen Control:   53265 (vertical), 53270 (horizontal)
Memory Pointers:  53272
Raster Counter:   53266
Interrupts:       53273 (status), 53274 (masks)

Collisions:       53278 (sprite-sprite), 53279 (sprite-background)

Border Color:     53280
Background Color: 53281

Light Pen:        53267 (X), 53268 (Y)
```

---

## Common Pitfalls

### Sprite Not Appearing

1. **Sprite not enabled** - Set bit in register 53269
2. **Sprite pointer not set** - POKE 2040-2047 with sprite data location
3. **Sprite data not defined** - Create 63 bytes of sprite shape data
4. **Sprite color is 0** - Sprite is black on black background
5. **X position > 255** - Remember to set bit in register 53264

### Collision Detection Not Working

1. **Not reading fast enough** - Collision registers clear when read
2. **Sprites not overlapping** - Check X/Y positions
3. **Sprite behind background** - Check register 53275 (priority)

### Screen Memory Wrong Location

1. **Wrong bank selected** - VIC-II can only see 16K banks
2. **Register 53272 not set** - Screen memory pointer not configured
3. **Forgot to multiply by 64** - Screen address = (value AND 240) * 64

---

## Hardware Specifications

- **Chip:** MOS 6567 (NTSC) / 6569 (PAL)
- **Display:** 320×200 pixels maximum (hi-res bitmap)
- **Text Mode:** 40×25 characters (1000 screen positions)
- **Colors:** 16 colors
- **Sprites:** 8 hardware sprites, 24×21 pixels each
- **Raster Lines:** 312 (PAL) / 262 (NTSC)
- **Memory Access:** 16K banks (4 banks selectable)

---

## Color Codes

| Value | Color | Value | Color |
|-------|-------|-------|-------|
| 0 | Black | 8 | Orange |
| 1 | White | 9 | Brown |
| 2 | Red | 10 | Light Red |
| 3 | Cyan | 11 | Dark Gray |
| 4 | Purple | 12 | Medium Gray |
| 5 | Green | 13 | Light Green |
| 6 | Blue | 14 | Light Blue |
| 7 | Yellow | 15 | Light Gray |

---

## References

- **Official Documentation:** Commodore 64 Programmer's Reference Guide, Appendix G
- **VIC-II Chip:** MOS Technology 6567/6569
- **Additional Reading:** "Mapping the Commodore 64" (Compute! Publications)

---

**Document Version:** 1.0
**Last Updated:** 2025-01-18
**Based on:** Official Commodore Technical Specifications
