# Lesson 018: Player Control

**Arc:** Space Shooter Evolution
**Position:** Lesson 2 of 7 in arc
**Type:** Standard
**Estimated Completion:** 30 lines of code

## Learning Objectives

- Read joystick input from CIA chip
- Control sprite position with joystick
- Implement smooth 8-direction movement
- Add bounds checking for sprite movement

## Prerequisites

**From Previous Lessons:**
- Sprite creation and positioning (L17)
- Input handling concepts (GET from L9, L12)
- Bounds checking (L9, L12)

**BASIC Knowledge:**
- PEEK for reading hardware
- Sprite position registers
- Bitwise operations (AND)

## Key Concepts Introduced

### Joystick Reading
Joystick state is read from CIA chip at memory address 56320 (port 2) or 56321 (port 1). Each bit represents one direction or fire button.

### Bitwise AND Operation
Use AND to test individual bits: `J AND 1` tests up, `J AND 2` tests down, etc. This decodes the joystick byte.

### 8-Direction Movement
Check multiple bits simultaneously for diagonal movement (up+left, down+right, etc.).

### Smooth Movement Speed
Update position by small increments (1-2 pixels) per frame for smooth control. Larger values = faster but less precise.

## Code Pattern

```basic
10 SX=160:SY=100:REM Sprite position
20 POKE 2040,13:POKE 53269,1:POKE 53287,1
30 REM Main loop
40 J=PEEK(56320):REM Read joystick port 2
50 IF (J AND 1)=0 THEN SY=SY-2:REM Up
60 IF (J AND 2)=0 THEN SY=SY+2:REM Down
70 IF (J AND 4)=0 THEN SX=SX-2:REM Left
80 IF (J AND 8)=0 THEN SX=SX+2:REM Right
90 REM Bounds check
100 IF SX<24 THEN SX=24
110 IF SX>320 THEN SX=320
120 IF SY<50 THEN SY=50
130 IF SY>229 THEN SY=229
140 REM Update sprite position
150 POKE 53248,SX:POKE 53249,SY
160 GOTO 40
```

## Hardware Interaction

**Chips Involved:**
- **CIA** - Joystick port reading
- **VIC-II** - Sprite positioning

**Memory Addresses:**
- `56320` ($DC00) - Joystick port 2 (standard game port)
- `56321` ($DC01) - Joystick port 1
- `53248` ($D000) - Sprite 0 X position
- `53249` ($D001) - Sprite 0 Y position

**Joystick Bit Values:**
```
Bit 0 (AND 1)  = Up
Bit 1 (AND 2)  = Down
Bit 2 (AND 4)  = Left
Bit 3 (AND 8)  = Right
Bit 4 (AND 16) = Fire button
```
Note: Bits are 0 when active (pressed)

## Common Pitfalls

1. **Inverted logic:** Bits are 0 when pressed, 1 when not pressed
2. **Wrong port:** Port 2 (56320) is standard, port 1 less common
3. **No bounds checking:** Sprite can move off-screen (visual glitches)
4. **Too fast movement:** SX=SX+10 makes control too sensitive
5. **X position >255:** Need high-bit register (53264) for right edge

## Extension Ideas

- Add fire button detection (bit 4)
- Implement acceleration (speed increases with hold)
- Add movement inertia (slide to stop)
- Restrict movement to play area only
- Add visual feedback (exhaust sprite when moving)
- Support keyboard fallback (WASD from L12)

## Builds Toward

**In This Tier:**
- L19: Fire bullets with button press
- L20: Enemy AI responds to player position
- L23: Complete shooter with full joystick control

**In Next Tier:**
- All sprite-based games use joystick input

## Quick Reference

**Joystick Reading Pattern:**
```basic
10 J=PEEK(56320)           :REM Port 2
20 IF (J AND 1)=0 THEN UP
30 IF (J AND 2)=0 THEN DOWN
40 IF (J AND 4)=0 THEN LEFT
50 IF (J AND 8)=0 THEN RIGHT
60 IF (J AND 16)=0 THEN FIRE
```

**8-Direction Movement:**
```basic
REM Diagonal up-left
IF (J AND 1)=0 AND (J AND 4)=0 THEN SX=SX-2:SY=SY-2
```

**Sprite Bounds (Typical):**
```
X: 24 to 320  (visible screen area)
Y: 50 to 229  (visible screen area)
```

**Movement Speed Guidelines:**
- 1 pixel/frame: Very slow, precise
- 2 pixels/frame: Standard game speed
- 3-4 pixels/frame: Fast action
- 5+ pixels/frame: Very fast, hard to control

**See Reference:**
`/docs/CIA-QUICK-REFERENCE.md` for complete joystick details
