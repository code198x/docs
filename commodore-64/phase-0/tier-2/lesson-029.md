# Lesson 029: Smooth Movement

**Arc:** Physics & Movement
**Position:** Lesson 1 of 4 in arc
**Type:** Standard
**Estimated Completion:** 30 lines of code

## Learning Objectives

- Implement perfect 8-way joystick control
- Create smooth diagonal movement
- Handle simultaneous input directions
- Normalize movement speed for consistency

## Prerequisites

**From Previous Lessons:**
- Basic joystick control (L18)
- Sprite positioning (L17-23)

**BASIC Knowledge:**
- Joystick reading (PEEK 56320)
- Sprite movement
- Basic trigonometry concepts

## Key Concepts Introduced

### 8-Way Movement
Handle all 8 directions: up, down, left, right, and 4 diagonals (up-left, up-right, down-left, down-right).

### Diagonal Speed Problem
Moving diagonally (x+y) is ~1.4x faster than cardinal directions. Need to normalize or it feels wrong.

### Input Buffering
Check multiple direction bits simultaneously for smooth diagonal detection.

### Movement Feel
Speed, acceleration response make huge difference in how game feels. Small tweaks = major impact.

## Code Pattern

```basic
10 SX=160:SY=100:SP=2:REM Sprite X,Y,Speed
20 POKE 2040,13:POKE 53269,1:POKE 53287,1
30 REM Main loop
40 J=PEEK(56320)
50 DX=0:DY=0:REM Delta X, Delta Y
60 REM Check all directions
70 IF (J AND 1)=0 THEN DY=-SP:REM Up
80 IF (J AND 2)=0 THEN DY=SP:REM Down
90 IF (J AND 4)=0 THEN DX=-SP:REM Left
100 IF (J AND 8)=0 THEN DX=SP:REM Right
110 REM Diagonal normalization
120 IF DX<>0 AND DY<>0 THEN DX=DX*0.7:DY=DY*0.7
130 REM Apply movement
140 SX=SX+DX:SY=SY+DY
150 REM Bounds checking
160 IF SX<24 THEN SX=24
170 IF SX>320 THEN SX=320
180 IF SY<50 THEN SY=50
190 IF SY>229 THEN SY=229
200 REM Update sprite
210 POKE 53248,SX:POKE 53249,SY
220 GOTO 40
```

## Hardware Interaction

**Chips Involved:**
- **CIA** - Joystick reading
- **VIC-II** - Sprite positioning

**Memory Addresses:**
- 56320 ($DC00) - Joystick port 2
- 53248-53249 ($D000-$D001) - Sprite 0 position

## Common Pitfalls

1. **Diagonal too fast:** Without normalization, diagonal = √2 faster
2. **Wrong normalization:** Multiply by 0.707 (or 0.7 approximation) not 0.5
3. **Integer truncation:** DX*0.7 loses precision, accumulate error over time
4. **Input priority:** Checking up then down = up wins if both pressed
5. **Jittery movement:** Fractional positions need proper rounding

## Extension Ideas

- Add acceleration (gradual speed increase)
- Add deceleration (slide to stop)
- Add max speed cap
- Add different movement modes (walk/run)
- Add movement animation (facing direction)
- Add movement trails or effects

## Builds Toward

**In This Tier:**
- L30: Physics simulation builds on smooth movement
- L31-32: Asteroids game needs perfect 8-way control

## Quick Reference

**Perfect 8-Way Pattern:**
```basic
10 J=PEEK(56320)
20 DX=0:DY=0
30 IF (J AND 1)=0 THEN DY=-SP
40 IF (J AND 2)=0 THEN DY=SP
50 IF (J AND 4)=0 THEN DX=-SP
60 IF (J AND 8)=0 THEN DX=SP
70 IF DX<>0 AND DY<>0 THEN DX=DX*0.7:DY=DY*0.7
80 SX=SX+DX:SY=SY+DY
```

**Diagonal Speed Math:**
```
Cardinal movement: SP pixels/frame
Diagonal without fix: SP*√2 = SP*1.414
Diagonal with *0.707: SP*1.414*0.707 ≈ SP
```

**Movement Speeds:**
- 1 pixel/frame: Slow, precise
- 2 pixels/frame: Standard
- 3 pixels/frame: Fast
- 4+ pixels/frame: Very fast

**Feel Tuning:**
- Instant response: DX/DY = ±speed
- Acceleration: speed += 0.2 each frame (max cap)
- Inertia: speed -= 0.1 when no input
