# Game 05: Hop Island

**Track:** AMOS
**Genre:** Platformer
**Units:** 16
**BASIC Version:** AMOS Professional

---

## Overview

Full platformer with gravity, jumping, enemies, and collectibles. Major project using all AMOS features.

### What You Build

- Multi-screen levels
- Jump physics
- Platform collision
- Enemies with AI
- Collectibles
- Lives system

---

## Unit Breakdown

### Phase 1: Core (Units 1-4)

#### Unit 1: Level Display
**Concepts:** Tile maps, screen drawing

#### Unit 2: Player Character
**Concepts:** Bob, animation frames

#### Unit 3: Movement
**Concepts:** Left/right, acceleration

#### Unit 4: Gravity
**Concepts:** Falling, velocity

### Phase 2: Jumping (Units 5-8)

#### Unit 5: Jump Mechanics
**Concepts:** Jump power, arc

#### Unit 6: Platform Collision
**Concepts:** Landing detection

#### Unit 7: Animation
**Concepts:** Walk cycle, jump frames

#### Unit 8: Wall Collision
**Concepts:** Blocking, sliding

### Phase 3: Gameplay (Units 9-12)

#### Unit 9: Collectibles
**Concepts:** Coins, score

#### Unit 10: Enemies
**Concepts:** Enemy bobs, patterns

#### Unit 11: Enemy Collision
**Concepts:** Damage, death

#### Unit 12: Level Complete
**Concepts:** Exit, next level

### Phase 4: Polish (Units 13-16)

#### Unit 13: Multiple Levels
**Concepts:** Level loading

#### Unit 14: Sound
**Concepts:** Sam Play, effects

#### Unit 15: Title Screen
**Concepts:** Menu, options

#### Unit 16: Complete Game
**Concepts:** Polish, balance

---

## Platform Physics

```basic
' GRAVITY AND JUMPING
GRAVITY#=0.5
JUMPPOWER#=-8.0

Procedure PHYSICS
  ' Apply gravity
  Add VY#,GRAVITY#
  Add PY#,VY#

  ' Check floor
  If ONGROUND(PX,PY#)
    VY#=0
    PY#=SNAPTOFLOOR(PY#)
    GROUNDED=True
  Else
    GROUNDED=False
  End If

  ' Jump
  If Fire(1) And GROUNDED
    VY#=JUMPPOWER#
  End If
End Proc
```

---

## Skills Learned

- Complete platformer mechanics
- Gravity physics
- Animation systems
- Level management
- Sound integration
