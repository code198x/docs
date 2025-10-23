# Lesson 031: Asteroid Clone Part 1

**Arc:** Physics & Movement
**Position:** Lesson 3 of 4 in arc
**Type:** Standard
**Estimated Completion:** 70 lines of code

## Learning Objectives

- Implement rotation mechanics
- Create momentum-based spaceship control
- Add thrust and inertia for Asteroids-style movement
- Combine rotation with velocity

## Prerequisites

**From Previous Lessons:**
- Physics simulation (L30)
- Smooth movement (L29)
- Sprite control and collision (L17-23)

**BASIC Knowledge:**
- Physics variables (velocity, acceleration)
- Trigonometry basics (sine, cosine)
- Sprite animation for rotation

## Key Concepts Introduced

### Rotation Angle
Track ship angle (0-360 degrees). Rotate left/right changes angle, not position directly.

### Thrust Vector
Thrust applies acceleration in direction ship faces. Use SIN/COS to convert angle to X/Y acceleration.

### Momentum Persistence
Ship continues moving in current direction even when rotating. Thrust changes velocity, not erases it.

### Rotation Sprites
Need multiple sprite frames showing ship at different angles (8-16 directions).

## Code Pattern

```basic
10 SX=160:SY=100:VX=0:VY=0:A=0:REM Position, velocity, angle
20 SP=2:TR=0.1:FR=0.99:REM Rotation speed, thrust, friction
30 DIM SA(8):REM Sprite angles (8 rotation frames)
40 FOR I=0 TO 7:SA(I)=13+I:NEXT I:REM Sprite blocks
50 POKE 53269,1:POKE 53287,1
60 REM Main loop
70 J=PEEK(56320)
80 REM Rotation
90 IF (J AND 4)=0 THEN A=A-SP:REM Rotate left
100 IF (J AND 8)=0 THEN A=A+SP:REM Rotate right
110 IF A<0 THEN A=A+360
120 IF A>=360 THEN A=A-360
130 REM Thrust (fire button)
140 IF (J AND 16)=0 THEN VX=VX+SIN(A*0.0174)*TR:VY=VY-COS(A*0.0174)*TR
150 REM Apply physics
160 VX=VX*FR:VY=VY*FR:REM Friction
170 SX=SX+VX:SY=SY+VY
180 REM Screen wrap
190 IF SX<0 THEN SX=320
200 IF SX>320 THEN SX=0
210 IF SY<0 THEN SY=229
220 IF SY>229 THEN SY=0
230 REM Update sprite
240 SF=INT(A/45):POKE 2040,SA(SF):REM Select rotated sprite frame
250 POKE 53248,SX:POKE 53249,SY
260 GOTO 70
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Multiple sprite frames for rotation
- **CIA** - Joystick input

**Memory Addresses:**
- Sprite data: Need 8 frames (8×64 = 512 bytes)
- Sprite pointer: 2040
- Position registers: 53248-53249

## Common Pitfalls

1. **Angle overflow:** Angle goes negative or >360, needs wrapping
2. **Radians vs degrees:** SIN/COS need radians (degrees × 0.0174)
3. **Y-axis inverted:** Screen Y increases downward, need -COS for up
4. **Too many rotation frames:** 8 is enough, 16 is smoother but more memory
5. **Thrust without friction:** Ship accelerates infinitely

## Extension Ideas

- Add rotation inertia (angular velocity)
- Add hyperspace (random teleport)
- Add shield sprite (ring around ship)
- Add exhaust animation when thrusting
- Add sound effects (thrust, rotate)
- Add rotation damping (gradual stop)

## Builds Toward

**In This Tier:**
- L32: Complete Asteroids with rocks, shooting, collision

## Quick Reference

**Rotation Pattern:**
```basic
10 A=0  :REM Angle (0-360)
20 IF LEFT THEN A=A-5
30 IF RIGHT THEN A=A+5
40 IF A<0 THEN A=A+360
50 IF A>=360 THEN A=A-360
```

**Thrust Vector:**
```basic
10 R=A*0.0174  :REM Convert degrees to radians
20 VX=VX+SIN(R)*THRUST
30 VY=VY-COS(R)*THRUST  :REM Negative because Y inverted
```

**Sprite Frame Selection:**
```basic
10 SF=INT(A/45)  :REM 8 frames, 360÷8=45 degrees each
20 POKE 2040,13+SF  :REM Sprite frames at blocks 13-20
```

**Screen Wrap:**
```basic
10 IF SX<0 THEN SX=320
20 IF SX>320 THEN SX=0
30 IF SY<0 THEN SY=229
40 IF SY>229 THEN SY=0
```

**8-Direction Sprite Frames:**
```
Frame 0: 0° (up)
Frame 1: 45° (up-right)
Frame 2: 90° (right)
Frame 3: 135° (down-right)
Frame 4: 180° (down)
Frame 5: 225° (down-left)
Frame 6: 270° (left)
Frame 7: 315° (up-left)
```

**Physics Constants:**
- Rotation speed: 2-5 degrees/frame
- Thrust: 0.05-0.15 acceleration
- Friction: 0.98-0.995 (very low for space)
- Max speed: 3-5 pixels/frame
