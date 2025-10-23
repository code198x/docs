# Lesson 017: First Sprite

**Arc:** Space Shooter Evolution
**Position:** Lesson 1 of 7 in arc
**Type:** Standard
**Estimated Completion:** 25 lines of code

## Learning Objectives

- Introduction to hardware sprites via VIC-II chip
- Create and define custom sprite shapes
- Position and display a sprite on screen
- Understand sprite data format (24×21 pixels)

## Prerequisites

**From Previous Lessons:**
- POKE command for hardware control (L7-8, L10-11)
- DATA statements for structured information (L6)
- Screen positioning concepts (L8)

**BASIC Knowledge:**
- POKE to memory addresses
- DATA/READ for sprite data
- Loops for data loading

## Key Concepts Introduced

### Hardware Sprites
Unlike screen characters, sprites are hardware-accelerated graphics that move independently of the text screen. The VIC-II chip handles 8 sprites (numbered 0-7).

### Sprite Data Format
Each sprite is 24×21 pixels, stored as 63 bytes (3 bytes per row × 21 rows). Each bit represents one pixel (1=on, 0=off).

### Sprite Pointers
Sprite shape data lives in memory, and sprite pointers (at 2040-2047) tell VIC-II where to find each sprite's shape.

### Sprite Control Registers
Enable sprites, set positions, set colours - all through POKE to VIC-II registers.

## Code Pattern

```basic
10 REM Define sprite shape at 13*64=832
20 FOR I=0 TO 62:READ B:POKE 832+I,B:NEXT I
30 POKE 2040,13:REM Point sprite 0 to block 13
40 POKE 53269,1:REM Enable sprite 0
50 POKE 53287,1:REM Set sprite 0 colour to white
60 REM Position sprite
70 POKE 53248,100:REM X position (low byte)
80 POKE 53249,100:REM Y position
90 END
1000 DATA 0,126,0,1,255,128,3,255,192
1010 DATA 7,231,224,7,255,224,15,255,240
1020 DATA [sprite data continues...]
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Complete sprite system control

**Memory Addresses:**
- `832-894` (example) - Sprite shape data (63 bytes per sprite)
- `2040-2047` ($07F8-$07FF) - Sprite pointers
- `53248-53264` ($D000-$D010) - Sprite position registers
- `53269` ($D015) - Sprite enable register
- `53287-53294` ($D027-$D02E) - Sprite colours

## Common Pitfalls

1. **Sprite memory location:** Must be on 64-byte boundary (832, 896, 960, etc.)
2. **Sprite pointer calculation:** Divide memory address by 64 (832÷64=13)
3. **Wrong data format:** Each row needs 3 bytes, total 63 bytes
4. **Forgetting to enable:** POKE 53269,1 required or sprite invisible
5. **Position registers:** Separate X and Y registers for each sprite

## Extension Ideas

- Design different sprite shapes (rocket, player character, enemy)
- Animate sprite position in a loop (move across screen)
- Create multiple sprites (use sprites 1-7)
- Experiment with sprite colours
- Create sprite editor tool (like L9 but for sprites)

## Builds Toward

**In This Tier:**
- L18: Joystick control for sprite movement
- L19: Multiple sprites (bullets and targets)
- L20-21: Enemy sprites with AI and animation
- L22-23: Complete shooter with all sprite features

**In Next Tier:**
- Advanced sprite techniques throughout

## Quick Reference

**Sprite Memory Layout:**
- 63 bytes per sprite
- 24 pixels wide × 21 pixels tall
- 3 bytes per row (24 bits = 24 pixels)
- Must align to 64-byte boundary

**Sprite Block Calculation:**
```
Memory Address ÷ 64 = Sprite Block Number
832 ÷ 64 = 13
896 ÷ 64 = 14
```

**Enable Sprite N:**
```basic
POKE 53269,2^N  :REM Single sprite
POKE 53269,255  :REM All 8 sprites
```

**Position Sprite 0:**
```basic
POKE 53248,X  :REM X position (0-255)
POKE 53249,Y  :REM Y position (0-255)
REM For X>255, need to set bit in 53264
```

**Sprite Control Registers:**
```
53248 ($D000) - Sprite 0 X position
53249 ($D001) - Sprite 0 Y position
53250 ($D002) - Sprite 1 X position
...every 2 bytes per sprite...
53264 ($D010) - High bits for X>255
53269 ($D015) - Sprite enable (bit per sprite)
53287 ($D027) - Sprite 0 colour
```

**Sprite Data Creation:**
- Use sprite editor tools
- Draw on graph paper (24×21 grid)
- Convert binary to decimal for DATA
- See `/docs/VIC-II-QUICK-REFERENCE.md` for complete sprite reference

**Simple Rocket Sprite:**
```
   XXX
  XXXXX
  XXXXX
  XX XX
  XX XX
```
Convert to bytes and store in DATA
