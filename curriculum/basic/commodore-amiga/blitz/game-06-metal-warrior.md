# Game 06: Metal Warrior

**Track:** Blitz Basic
**Genre:** Run and Gun
**Units:** 16
**BASIC Version:** Blitz Basic 2

---

## Overview

Turrican-style action platformer with large scrolling levels, multiple weapons, and boss battles.

### What You Build

- Large scrolling levels
- 8-way shooting
- Multiple weapons
- Power-ups
- Boss battles
- Lives/continues

---

## Unit Breakdown

### Phase 1: Core (Units 1-4)

#### Unit 1: Level System
**Concepts:** Large tile maps

#### Unit 2: Scrolling
**Concepts:** Smooth scroll, camera

#### Unit 3: Player Movement
**Concepts:** Run, jump, crouch

#### Unit 4: Basic Shooting
**Concepts:** 8-way aiming

### Phase 2: Weapons (Units 5-8)

#### Unit 5: Weapon Types
**Concepts:** Different projectiles

#### Unit 6: Weapon Switching
**Concepts:** Inventory, selection

#### Unit 7: Power-ups
**Concepts:** Weapon pickups

#### Unit 8: Special Weapons
**Concepts:** Bombs, beams

### Phase 3: Enemies (Units 9-12)

#### Unit 9: Basic Enemies
**Concepts:** Spawning, AI

#### Unit 10: Enemy Variety
**Concepts:** Different types

#### Unit 11: Enemy Attacks
**Concepts:** Shooting back

#### Unit 12: Boss Design
**Concepts:** Patterns, health

### Phase 4: Polish (Units 13-16)

#### Unit 13: Scrolling Optimisation
**Concepts:** Performance

#### Unit 14: Sound and Music
**Concepts:** Effects, tracker

#### Unit 15: Lives System
**Concepts:** Continues, checkpoints

#### Unit 16: Complete Game
**Concepts:** Balance, testing

---

## Large Level Scrolling

```blitz
; EFFICIENT SCROLLING FOR LARGE LEVELS
DEFTYPE .w

levelWidth = 256   ; Tiles
levelHeight = 64
tileSize = 16

Dim levelData.b(levelWidth, levelHeight)

Statement RenderLevel{camX.w, camY.w}
  ; Only draw visible tiles
  startX.w = camX / tileSize
  startY.w = camY / tileSize
  endX.w = startX + 21  ; Screen width in tiles + 1
  endY.w = startY + 17  ; Screen height in tiles + 1

  For ty = startY To endY
    For tx = startX To endX
      tile.b = levelData(tx, ty)
      If tile > 0
        screenX.w = tx * tileSize - camX
        screenY.w = ty * tileSize - camY
        Blit tile, screenX, screenY
      End If
    Next tx
  Next ty
End Statement
```

---

## Skills Learned

- Large level management
- Efficient scrolling
- Weapon systems
- Boss design
- Performance optimisation
