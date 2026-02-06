# Phase 3: Momentum

**Game:** Dash (NES Game 1)
**Units:** 33-48
**Theme:** Jump feel refined to commercial quality, hazards, and checkpoints
**6502 Focus:** Signed arithmetic, bit manipulation (AND/ORA/EOR), comparison chains (CMP/BCS/BCC)
**Hardware:** OAM cycling for flicker management, PPU palette writes
**Status:** Planned

---

## Overview

Phase 3 is about feel. Variable-height jumping -- hold the button longer, jump higher -- is the single mechanic that separates amateur platformers from professional ones. Coyote time (grace frames after leaving a platform edge) and jump buffering (queue a jump just before landing) make controls feel responsive when they should feel frustrating.

Moving platforms, crumbling platforms, springs, conveyors, and water create environmental variety. Checkpoints and a health system add forgiveness. By the end of Phase 3, the jump feel matches commercial quality -- the game feels right before it looks or sounds complete.

---

## Prerequisites from Phase 2

- Metatile system with collision types
- Player animation state machine
- One-way platforms and ladders
- Multiple levels with transitions

---

## Unit Progression

| Unit | Title | New 6502 Concept | Game Addition |
|------|-------|------------------|---------------|
| 33 | Variable-Height Jump | Check button held, reduce velocity on release | **Professional jump** |
| 34 | Jump Apex Hang | Reduced gravity near peak | Floaty-good feel |
| 35 | Coyote Time | Grace frames after leaving edge, `INC` timer | Forgiving controls |
| 36 | Jump Buffering | Buffer A press before landing | Responsive |
| 37 | Moving Platforms (Horizontal) | Platform object with velocity, carry player | Dynamic level |
| 38 | Moving Platforms (Vertical) | Carry upward, detach on jump | Elevators |
| 39 | Crumbling Platforms | Timer on contact, collapse after delay | Urgency |
| 40 | Pit Death and Respawn | Y boundary, life lost, respawn at checkpoint | Consequence |
| 41 | Checkpoint Flag | Metatile trigger, save respawn position | Fairness |
| 42 | Invincibility Frames | Damage cooldown, sprite flicker via OAM cycling | Brief immunity |
| 43 | Health System (3 Hits) | Health variable, HUD hearts display | Forgiveness |
| 44 | Heal Item | Heart pickup restores one point | Recovery |
| 45 | Spring Tile | Upward boost on contact | Vertical traversal |
| 46 | Conveyor Belt | Horizontal force while standing | Movement hazard |
| 47 | Water Tiles | Reduced gravity and speed when submerged | Environment variety |
| 48 | Integration + Feel Tuning | Constants for gravity, jump force, speeds | **Feels right** |

---

## Key Teaching Moments

### Variable-Height Jump (Unit 33)

The mechanic: while the A button is held and the player is moving upward, gravity applies normally. When the button is released early, the remaining upward velocity is halved. The player peaks sooner, producing a shorter jump. One `LSR` instruction halves the velocity. Simple code, transformative feel.

```asm
; Variable-height jump: cut velocity if button released
    lda buttons
    and #BUTTON_A
    bne @held           ; A still held, normal gravity
    lda velocity_y
    bpl @held           ; Already falling, don't modify
    lsr a               ; Halve upward velocity
    sta velocity_y
@held:
```

### Coyote Time (Unit 35)

A counter tracks frames since the player was last grounded. Each frame on solid ground, reset to zero. Each frame in the air, increment. When the player presses jump, check: if `coyote_timer` < 6, allow the jump even though they're airborne. Without this, walking off a ledge and pressing jump immediately feels like a bug. With it, the player feels skilled.

### Invincibility Frames (Unit 42)

After taking damage, the player is invincible for ~60 frames (1 second). During this time, the sprite flickers by skipping OAM writes every other frame. The OAM buffer position for the player alternates between valid Y coordinates and Y=$EF (off-screen). The damage cooldown prevents rapid multi-hit kills from single hazard contact.

---

## 6502 Concepts Introduced

1. Signed comparison -- `BPL`/`BMI` for positive/negative velocity (Unit 33)
2. `LSR` for fast division by 2 -- halving velocity (Unit 33)
3. Timer patterns -- `INC` counter, `CMP` threshold, reset (Unit 35)
4. Input buffering -- save button press, consume on valid state (Unit 36)
5. Object velocity -- platform movement applied to rider (Unit 37)
6. Frame-based timers -- `DEC` countdown, trigger at zero (Unit 39)
7. OAM cycling -- alternate sprite visibility for flicker effect (Unit 42)
8. Bit flags -- health display using tile indices per heart (Unit 43)
9. Environmental modifiers -- different physics constants per tile type (Unit 47)

---

## Hardware

### New in Phase 3

| Resource | Purpose | Introduced |
|----------|---------|------------|
| OAM Y coordinate $EF | Hide sprites off-screen (below visible area) | Unit 42 |

Phase 3 is primarily about game logic, not new hardware. The PPU and APU skills from Phases 1-2 are sufficient.

---

## Game State at Phase End

After Unit 48:

- **Variable-height jump** -- hold longer for higher, release for short hop
- **Jump apex hang** -- reduced gravity at peak for satisfying arc
- **Coyote time** -- 6-frame grace period after leaving edges
- **Jump buffering** -- queue jump before landing for responsive feel
- **Moving platforms** -- horizontal and vertical, carry the player
- **Crumbling platforms** -- collapse after standing on them briefly
- **Checkpoints** -- respawn at last flag on death
- **Health system** -- 3 hits before death, HUD hearts
- **Springs** -- upward boost tile for vertical level design
- **Conveyors** -- horizontal force tiles
- **Water** -- reduced gravity and speed zones

The jump feels professional. Controls are responsive and forgiving. Hazards create varied gameplay.

---

## What Carries to Phase 4

- **Refined physics** -- the constants tuned here define the game's identity
- **Platform object system** -- reused for enemy movement
- **Checkpoint system** -- works across scrolling levels
- **Environmental tiles** -- water and conveyor physics apply in scrolling sections

---

**Version:** 1.0
**Last Updated:** 2026-02-06
