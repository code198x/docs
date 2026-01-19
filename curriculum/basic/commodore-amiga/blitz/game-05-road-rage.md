# Game 05: Road Rage

**Track:** Blitz Basic
**Genre:** Top-Down Racing
**Units:** 16
**BASIC Version:** Blitz Basic 2

---

## Overview

Skidmarks-style racing - the genre that made Blitz Basic famous. Full car physics with skidding, drifting, and split-screen multiplayer.

### What You Build

- Advanced car physics
- Skid/drift mechanics
- Track system
- 2-player split screen
- Lap timing
- Championship mode

---

## Unit Breakdown

### Phase 1: Physics (Units 1-4)

#### Unit 1: Car Basics
**Concepts:** Position, rotation

#### Unit 2: Acceleration
**Concepts:** Speed, friction

#### Unit 3: Steering
**Concepts:** Turn rate, grip

#### Unit 4: Skidding
**Concepts:** Drift physics

### Phase 2: Track (Units 5-8)

#### Unit 5: Track Tiles
**Concepts:** Tile map, surfaces

#### Unit 6: Track Collision
**Concepts:** Surface detection

#### Unit 7: Checkpoints
**Concepts:** Lap system

#### Unit 8: Multiple Tracks
**Concepts:** Track loading

### Phase 3: Multiplayer (Units 9-12)

#### Unit 9: Split Screen
**Concepts:** ViewPort, dual view

#### Unit 10: Two Cars
**Concepts:** Independent physics

#### Unit 11: Position Tracking
**Concepts:** Who's winning

#### Unit 12: Race Structure
**Concepts:** Countdown, finish

### Phase 4: Polish (Units 13-16)

#### Unit 13: Sound
**Concepts:** Engine, skid sounds

#### Unit 14: AI Opponent
**Concepts:** Waypoint driving

#### Unit 15: Championship
**Concepts:** Points, standings

#### Unit 16: Complete Game
**Concepts:** Polish, balance

---

## Skid Physics

```blitz
; SKIDMARKS-STYLE CAR PHYSICS
DEFTYPE .q

Statement CarPhysics{car.w}
  ; Get input
  If Joyx(car) < 0 Then steer.q = -turnSpeed Else If Joyx(car) > 0 Then steer.q = turnSpeed Else steer.q = 0
  accel.q = 0
  If Joyy(car) < 0 Then accel = acceleration
  If Joyy(car) > 0 Then accel = -braking

  ; Apply steering (reduced at high speed)
  angle(car) = angle(car) + steer * (1 - speed(car) / maxSpeed * 0.5)

  ; Calculate velocity components
  targetVX.q = Cos(angle(car)) * speed(car)
  targetVY.q = Sin(angle(car)) * speed(car)

  ; Lerp actual velocity toward target (grip)
  grip.q = GetGrip(carX(car), carY(car))  ; Surface dependent
  vx(car) = vx(car) + (targetVX - vx(car)) * grip
  vy(car) = vy(car) + (targetVY - vy(car)) * grip

  ; Apply acceleration
  speed(car) = speed(car) + accel
  speed(car) = speed(car) * friction

  ; Move car
  carX(car) = carX(car) + vx(car)
  carY(car) = carY(car) + vy(car)
End Statement
```

---

## Split Screen

```blitz
; SPLIT SCREEN SETUP
BitMap 0, 320, 512, 4  ; Double height for both views

; Player 1 view (top half)
VPort 0, 0, 0, 320, 128
; Player 2 view (bottom half)
VPort 1, 0, 128, 320, 128

; RENDER LOOP
Cls 0
RenderView{0, carX(1), carY(1)}  ; P1 camera
RenderView{1, carX(2), carY(2)}  ; P2 camera
```

---

## Skills Learned

- Advanced car physics
- Drift/skid mechanics
- Split-screen rendering
- Surface-based grip
- Multiplayer design
