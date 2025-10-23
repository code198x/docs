# Lesson 033: Platform Basics

**Arc:** Platform Adventure
**Position:** Lesson 1 of 7 in arc
**Type:** Standard
**Estimated Completion:** 45 lines of code

## Learning Objectives

- Implement gravity and jumping mechanics
- Create platform collision detection
- Build foundation for platformer games
- Handle ground detection and landing

## Prerequisites

**From Previous Lessons:**
- Physics simulation (L30)
- Sprite control (L17-23)
- Collision detection (L19)

**BASIC Knowledge:**
- Velocity and acceleration
- Sprite positioning
- Collision checking

## Key Concepts Introduced

### Constant Gravity
Apply downward acceleration every frame (VY += GRAV). Creates realistic falling motion.

### Jump Mechanic
When on ground + jump button: set VY to negative value (upward velocity). Gravity brings back down.

### Platform Collision
Check if player sprite overlaps platform. If landing from above, stop at platform top.

### Ground State
Track whether player is on ground (GR flag). Can only jump when GR=1.

## Code Pattern

```basic
10 SX=160:SY=150:VX=0:VY=0:GR=0:REM Position, velocity, grounded
20 GRAV=0.2:JMP=-3:REM Gravity, jump strength
30 DIM PX(5),PY(5),PW(5):REM Platform X, Y, width
40 REM Define platforms
50 PX(1)=100:PY(1)=180:PW(1)=80
60 PX(2)=200:PY(2)=140:PW(2)=60
70 POKE 53269,1:POKE 53287,1:POKE 2040,13
80 REM Main loop
90 J=PEEK(56320)
100 REM Horizontal movement
110 IF (J AND 4)=0 THEN VX=-2
120 IF (J AND 8)=0 THEN VX=2
130 IF (J AND 12)=12 THEN VX=VX*0.8:REM Friction when no input
140 REM Jumping
150 IF (J AND 16)=0 AND GR=1 THEN VY=JMP:GR=0
160 REM Apply gravity
170 VY=VY+GRAV
180 REM Apply velocity
190 SX=SX+VX:SY=SY+VY
200 REM Platform collision
210 GR=0
220 FOR I=1 TO 2
230 IF SX>PX(I)-12 AND SX<PX(I)+PW(I)+12 THEN
240 IF SY>PY(I)-21 AND SY<PY(I) AND VY>0 THEN SY=PY(I)-21:VY=0:GR=1
250 NEXT I
260 REM Ground collision
270 IF SY>200 THEN SY=200:VY=0:GR=1
280 REM Update sprite
290 POKE 53248,SX:POKE 53249,SY
300 GOTO 90
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Sprite for player
- **CIA** - Joystick input

**Memory Addresses:**
- Standard sprite and joystick registers

## Common Pitfalls

1. **Gravity too strong:** VY accelerates too fast, feels floaty or heavy
2. **Can't jump:** Forgetting to check GR=1 allows mid-air jumps
3. **Platform detection wrong:** Must check sprite bounds not just center point
4. **Falling through platforms:** Collision must set VY=0 and position
5. **No terminal velocity:** VY grows infinitely if no cap

## Extension Ideas

- Add variable jump height (hold button = higher)
- Add double-jump mechanic
- Add platforms that move
- Add one-way platforms (can jump through from below)
- Add ladders (disable gravity)
- Add wall-jump mechanic

## Builds Toward

**In This Tier:**
- L34: Multi-state character animation (idle, walk, jump, fall)
- L35: Multiple level screens with data-driven design
- L36-37: Enemies and collectibles in platformer
- L39: Complete platformer game

## Quick Reference

**Gravity Pattern:**
```basic
10 GRAV=0.2  :REM Gravity constant
20 VY=VY+GRAV  :REM Apply every frame
30 IF VY>5 THEN VY=5  :REM Terminal velocity
```

**Jump Pattern:**
```basic
10 IF FIRE AND GR=1 THEN VY=JMP_STRENGTH:GR=0
20 JMP_STRENGTH=-2 to -4 (negative = upward)
```

**Platform Collision:**
```basic
100 REM Check if player above platform
110 IF SX in platform X range AND
120 SY near platform top AND
130 VY>0 THEN
140 SY=PLATFORM_TOP:VY=0:GR=1
```

**Sprite Bounds:**
```
Player sprite 24×21 pixels
Center point: SX, SY
Left edge: SX-12
Right edge: SX+12
Top edge: SY-21
Bottom edge: SY
```

**Feel Tuning:**
- Gravity: 0.15-0.25 (lower = floaty, higher = heavy)
- Jump: -2 to -4 (lower = short hop, higher = big jump)
- Friction: 0.7-0.9 when no input (responsive vs slide)
- Terminal velocity: 4-6 pixels/frame

**Performance Note:**
"Platformer calculations (gravity, collision) are lightweight. Performance depends on number of animated sprites and enemies (discovered in L36)."
