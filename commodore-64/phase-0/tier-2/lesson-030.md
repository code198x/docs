# Lesson 030: Physics Simulation

**Arc:** Physics & Movement
**Position:** Lesson 2 of 4 in arc
**Type:** Standard
**Estimated Completion:** 45 lines of code

## Learning Objectives

- Implement momentum and inertia
- Create acceleration and deceleration
- Add friction and bounce mechanics
- Understand velocity vs position

## Prerequisites

**From Previous Lessons:**
- Smooth movement (L29)
- Sprite control (L17-23)

**BASIC Knowledge:**
- Variables for state tracking
- Velocity concepts
- Basic physics

## Key Concepts Introduced

### Velocity Variables
Position (SX,SY) changes by velocity (VX,VY) each frame. Velocity persists, creating momentum.

### Acceleration
Input doesn't change position directly - it changes velocity. Velocity changes position. Two-step process feels natural.

### Friction/Damping
Multiply velocity by 0.95 each frame to simulate friction. Object gradually stops without input.

### Bounce Mechanics
When hitting wall, reverse velocity (VX = -VX). Optionally reduce magnitude (energy loss).

## Code Pattern

```basic
10 SX=160:SY=100:VX=0:VY=0:REM Position and velocity
20 AC=0.3:FR=0.95:REM Acceleration, friction
30 POKE 2040,13:POKE 53269,1
40 REM Main loop
50 J=PEEK(56320)
60 REM Apply acceleration from input
70 IF (J AND 1)=0 THEN VY=VY-AC:REM Up
80 IF (J AND 2)=0 THEN VY=VY+AC:REM Down
90 IF (J AND 4)=0 THEN VX=VX-AC:REM Left
100 IF (J AND 8)=0 THEN VX=VX+AC:REM Right
110 REM Apply friction
120 VX=VX*FR:VY=VY*FR
130 REM Speed cap
140 IF VX>3 THEN VX=3
150 IF VX<-3 THEN VX=-3
160 IF VY>3 THEN VY=3
170 IF VY<-3 THEN VY=-3
180 REM Apply velocity to position
190 SX=SX+VX:SY=SY+VY
200 REM Bounce off walls
210 IF SX<24 OR SX>320 THEN VX=-VX*0.8
220 IF SY<50 OR SY>229 THEN VY=-VY*0.8
230 REM Update sprite
240 POKE 53248,SX:POKE 53249,SY
250 GOTO 50
```

## Hardware Interaction

**Chips Involved:**
- **CIA** - Input
- **VIC-II** - Sprite display

**Memory Addresses:**
- Standard sprite and joystick registers

## Common Pitfalls

1. **Velocity explosion:** Without speed cap, velocity grows infinitely
2. **Too much friction:** FR=0.5 stops too fast, FR=0.98 barely slows
3. **Integer velocity:** Velocity needs fractional precision or jitters
4. **Bounce direction wrong:** Must check which wall hit (X vs Y)
5. **No minimum velocity:** Objects drift forever at tiny speeds

## Extension Ideas

- Add gravity (VY += 0.1 each frame)
- Add air resistance (different friction for X vs Y)
- Add elastic vs inelastic collisions
- Add rotation physics
- Add object-object collision with momentum transfer
- Add launch/throw mechanics

## Builds Toward

**In This Tier:**
- L31: Asteroids-style rotation and momentum
- L32: Complete physics-based game

## Quick Reference

**Physics Variables:**
```basic
10 SX,SY = Position
20 VX,VY = Velocity
30 AC = Acceleration rate
40 FR = Friction multiplier (0.9-0.99)
50 MV = Max velocity cap
```

**Physics Update Loop:**
```basic
100 REM Apply forces (input, gravity)
110 VX=VX+[acceleration]
120 VY=VY+[acceleration]
130 REM Apply friction
140 VX=VX*FR:VY=VY*FR
150 REM Cap speed
160 IF ABS(VX)>MV THEN VX=SGN(VX)*MV
170 REM Apply velocity
180 SX=SX+VX:SY=SY+VY
```

**Friction Values:**
- 1.0 = No friction (space)
- 0.98 = Very low (ice)
- 0.95 = Medium (normal)
- 0.90 = High (mud)
- 0.80 = Very high (sand)

**Bounce Formula:**
```basic
10 IF SX<WALL THEN VX=-VX*BOUNCE
20 BOUNCE=1.0 :REM Perfect elastic
30 BOUNCE=0.8 :REM Energy loss
40 BOUNCE=0.5 :REM High energy loss
```

**Gravity Simulation:**
```basic
10 VY=VY+0.2  :REM Constant downward acceleration
20 IF SY>GROUND AND VY>0 THEN VY=-VY*0.7:REM Bounce
```

**Physics Feels:**
- Spaceship: AC=0.2, FR=1.0 (no friction)
- Car: AC=0.5, FR=0.95
- Ball: AC=0, FR=0.98, VY+=0.2 (gravity)
- Character: AC=1.0, FR=0.85 (responsive)
