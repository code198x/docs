# Game 08: Artillery Duel

**Track:** Blitz Basic
**Genre:** Worms-Style Artillery
**Units:** 16
**BASIC Version:** Blitz Basic 2

---

## Overview

**Capstone project** - Worms-style artillery game. This is THE genre that proved Blitz Basic could make commercial games (Worms itself was made in Blitz).

### What You Build

- Destructible terrain
- Angle/power shooting
- Projectile physics
- Multiple weapons
- Turn-based multiplayer
- Wind effects

---

## Unit Breakdown

### Phase 1: Terrain (Units 1-4)

#### Unit 1: Terrain Generation
**Concepts:** Procedural landscape

#### Unit 2: Terrain Display
**Concepts:** Bitmap drawing

#### Unit 3: Terrain Destruction
**Concepts:** Pixel removal, circles

#### Unit 4: Collision Detection
**Concepts:** Pixel checking

### Phase 2: Shooting (Units 5-8)

#### Unit 5: Aiming
**Concepts:** Angle selection

#### Unit 6: Power
**Concepts:** Power bar, charging

#### Unit 7: Projectile Physics
**Concepts:** Gravity, arc

#### Unit 8: Impact
**Concepts:** Explosion, damage

### Phase 3: Weapons (Units 9-12)

#### Unit 9: Weapon Types
**Concepts:** Different projectiles

#### Unit 10: Blast Radius
**Concepts:** Damage falloff

#### Unit 11: Special Weapons
**Concepts:** Cluster, homing

#### Unit 12: Weapon Selection
**Concepts:** Limited ammo

### Phase 4: Multiplayer (Units 13-16)

#### Unit 13: Turn System
**Concepts:** Player switching

#### Unit 14: Wind
**Concepts:** Affecting trajectories

#### Unit 15: Victory
**Concepts:** Win conditions

#### Unit 16: Complete Game
**Concepts:** Polish, balance

---

## Destructible Terrain

```blitz
; TERRAIN AS BITMAP
DEFTYPE .w

; Create terrain bitmap
terrainBM = 1
BitMap terrainBM, 640, 400, 4

; Generate landscape
Statement GenerateTerrain{}
  Use BitMap terrainBM
  Cls 0

  ; Procedural hills
  height.w = 200
  For x = 0 To 639
    height = height + Rnd(5) - 2
    If height < 100 Then height = 100
    If height > 300 Then height = 300

    Line x, 399, x, 399 - height, 2  ; Green terrain
  Next x
End Statement

; Destroy terrain (explosion)
Statement DestroyTerrain{cx.w, cy.w, radius.w}
  Use BitMap terrainBM
  Circlef cx, cy, radius, 0  ; Draw black circle (remove terrain)
End Statement

; Check if point is terrain
Function IsTerrain{x.w, y.w}
  Use BitMap terrainBM
  c.w = Point(x, y)
  Function Return c > 0
End Function
```

---

## Projectile Physics

```blitz
; WORMS-STYLE PROJECTILE
DEFTYPE .q

Statement FireProjectile{x.q, y.q, angle.w, power.w}
  ; Convert angle to radians
  rad.q = angle * Pi / 180

  ; Initial velocity
  projVX.q = Cos(rad) * power / 10
  projVY.q = -Sin(rad) * power / 10  ; Negative because Y increases downward

  ; Projectile loop
  While projY < 400 And projX > 0 And projX < 640
    ; Apply gravity
    projVY = projVY + gravity

    ; Apply wind
    projVX = projVX + wind / 100

    ; Move
    projX = projX + projVX
    projY = projY + projVY

    ; Check terrain collision
    If IsTerrain{projX, projY}
      Explode{projX, projY, blastRadius}
      Pop While  ; Exit loop
    End If

    ; Draw
    Plot projX, projY, 1
    VWait 1
  Wend
End Statement
```

---

## Why This Game Matters

**Worms** (1995) was created in Blitz Basic by Andy Davidson for Team17. It became one of the most successful game franchises ever, spawning dozens of sequels across every platform.

This proves that Blitz Basic wasn't just for hobbyists - it was capable of producing commercial hits.

---

## Skills Learned

- Bitmap manipulation
- Destructible terrain
- Projectile physics
- Wind effects
- Turn-based multiplayer
- Complete game design
- Everything Blitz Basic offers
