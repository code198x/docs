# Phase 7: The Gauntlet

**Game:** Dash (NES Game 1)
**Units:** 97-112
**Theme:** Enemies, combat, and boss fights
**6502 Focus:** Object pools, complex state machines, OAM cycling, metasprite entities, multi-phase patterns
**Hardware:** OAM cycling for 8-per-scanline management
**Status:** Planned

---

## Overview

Phase 7 fills the levels with danger. Walking enemies patrol platforms. Flying enemies trace sine wave paths. Shooting enemies fire projectiles. The player can stomp enemies (jump on their heads) or throw projectiles with the B button.

Boss fights are the phase highlight: large metasprite entities (4x4 tiles) with health bars, telegraphed attack patterns, and phase transitions at 50% health. Managing sprites becomes critical -- player metasprite + enemy metasprites + projectiles can exceed 8 sprites per scanline. OAM cycling distributes the flicker fairly.

Level design integrates enemies with terrain. Enemies are scroll-aware: they activate when the camera brings their position on screen. Placements are designed encounters, not random spawns.

---

## Prerequisites from Phase 6

- Music engine running in NMI
- SFX priority system
- Complete visual system with metasprites
- Scrolling with nametable seam loading

---

## Unit Progression

| Unit | Title | New 6502 Concept | Game Addition |
|------|-------|------------------|---------------|
| 97 | Walking Enemy (Patrol) | Object pool with state table, direction toggle | Moving threat |
| 98 | Enemy-Player Collision | Bounding box per enemy, damage on contact | **Danger** |
| 99 | Stomp Mechanic | Player falling onto enemy top = defeat, bounce up | Jump attack |
| 100 | Stomp Sound + Score | APU noise burst, score increment | Satisfying |
| 101 | Flying Enemy (Sine Wave) | Lookup table for Y offset, horizontal drift | Aerial threat |
| 102 | Shooting Enemy | Enemy fires toward player, aimed projectile | Ranged danger |
| 103 | Player Projectile | B button throws, limited cooldown | Offensive option |
| 104 | Multiple Enemy Types | Type field, behaviour dispatch via jump table | Varied challenge |
| 105 | OAM Cycling | Rotate starting OAM index per frame | Fair flicker distribution |
| 106 | Boss: Large Metasprite | 4x4 tile entity (32x32 pixels), coordinated movement | **Imposing** |
| 107 | Boss Movement Pattern | State machine: idle -> telegraph -> attack -> recover | Learnable fight |
| 108 | Boss Health Bar | Background tiles in HUD, deplete on hits | Visible progress |
| 109 | Boss Phase 2 | Pattern change at 50% health, faster attacks | Escalation |
| 110 | Boss Defeat Sequence | Explosion metasprites, victory jingle, door opens | Triumph |
| 111 | Scroll-Triggered Enemies | Enemies activate when camera reaches their world X | Designed encounters |
| 112 | Integration + Combat Balance | Hit boxes, damage values, placement | Challenging but fair |

---

## Key Teaching Moments

### The Stomp (Unit 99)

The stomp distinguishes platformer combat from other genres. The check:

```asm
; Is this a stomp? Player must be:
; 1. Falling (velocity_y > 0)
; 2. Above the enemy (player bottom near enemy top)
    lda velocity_y
    bmi @not_stomp      ; Moving up = not a stomp
    beq @not_stomp      ; Stationary = not a stomp

    ; Check vertical overlap
    lda player_y
    clc
    adc #PLAYER_HEIGHT
    sec
    sbc enemy_y         ; player_bottom - enemy_top
    cmp #$08            ; Within 8 pixels of enemy top?
    bcs @not_stomp      ; Too deep = side hit

    ; It's a stomp! Bounce and defeat
    lda #BOUNCE_VEL
    sta velocity_y      ; Bounce upward
    ; ... defeat enemy
```

If the overlap is horizontal instead of above, it's contact damage. The distinction is a few comparisons -- simple code, iconic mechanic.

### OAM Cycling (Unit 105)

The NES renders sprites in OAM order. With 8 per scanline, sprites later in OAM disappear when the line is full. OAM cycling rotates which sprites get priority: each frame, the starting index advances by 4 (one sprite). Over successive frames, different sprites get dropped, creating even flicker instead of permanent invisibility. Every commercial NES game does this.

### Boss State Machine (Unit 107)

The boss cycles through states on a timer:

1. **Idle** (60 frames) -- boss drifts slowly, safe to approach
2. **Telegraph** (30 frames) -- boss flashes, sprite palette change, warning
3. **Attack** (45 frames) -- boss charges, projectiles, danger zone
4. **Recover** (30 frames) -- boss is vulnerable, takes extra damage

Telegraphing is the design key: the player sees the attack coming and has time to react. Tense but fair. Phase 2 (at 50% health) accelerates the timers and adds a new attack -- same structure, higher stakes.

---

## 6502 Concepts Introduced

1. Object pool -- fixed-size array of enemy slots, active/inactive flag (Unit 97)
2. Bounding box collision -- 4-comparison overlap test (Unit 98)
3. Jump table dispatch -- `LDA type : ASL : TAX : LDA table,X` (Unit 104)
4. OAM rotation -- advance starting index by 4 each frame (Unit 105)
5. Large metasprite -- 16-sprite entity from table data (Unit 106)
6. State machine with timers -- state + frame counter + transition table (Unit 107)
7. Scroll-aware activation -- compare enemy world X to camera position (Unit 111)

---

## Hardware

### New in Phase 7

| Resource | Purpose | Introduced |
|----------|---------|------------|
| OAM cycling pattern | Rotate sprite priority to distribute 8-per-scanline flicker | Unit 105 |

Phase 7 is primarily about game logic. The hardware skills from Phases 1-6 provide everything needed.

---

## Game State at Phase End

After Unit 112:

- **Walking enemies** -- patrol platforms, reverse at edges
- **Flying enemies** -- sine wave paths through the air
- **Shooting enemies** -- fire aimed projectiles at the player
- **Stomp mechanic** -- jump on enemies to defeat them
- **Player projectile** -- B button attack with cooldown
- **OAM cycling** -- fair flicker when many sprites share scanlines
- **Boss fights** -- large metasprite, health bar, telegraph, two phases
- **Boss defeat** -- explosion sequence, victory jingle, progression
- **Scroll-triggered spawns** -- enemies activate as camera reaches them
- **Designed encounters** -- enemy placement integrated with level terrain

The gauntlet is complete. Every level is a designed challenge.

---

## What Carries to Phase 8

- **Object pool** -- reused for attract mode entities
- **State machines** -- menu navigation, demo playback
- **OAM cycling** -- permanent, runs every frame
- **Combat balance** -- difficulty select adjusts damage and speed values

---

**Version:** 1.0
**Last Updated:** 2026-02-06
