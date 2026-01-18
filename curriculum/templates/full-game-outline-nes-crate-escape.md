# Full Game Outline: NES Crate Escape (128 Units)

**Game:** Crate Escape (Game 2)
**Platform:** Nintendo Entertainment System
**Units:** 128 (8 phases × 16 units)
**Prerequisite:** Stellar Barrage (Game 1) - PPU, sprites, OAM, controller, APU basics
**Target Quality:** Polished single-screen platformer (Donkey Kong / Lode Runner quality)

---

## What Carries Over from Game 1

Learners already know:
- PPU setup (pattern tables, nametables, palettes)
- Sprites via OAM
- Controller reading
- APU sound effects
- Basic collision detection (sprite-to-sprite)
- Game loop structure (NMI-driven)

**What's NEW in this game:**
- Gravity and acceleration
- Jump physics (impulse, arc, landing)
- Tile-based collision (background as platforms)
- Metatile concept for level design
- Animation state machines
- Level data in CHR/PRG ROM

---

## Design Philosophy

- **Gravity from Unit 1** — the defining new mechanic
- **Jumping by Unit 4** — playable platformer early
- **Tile collision is fundamental** — the NES way
- **Debugging inline** — platform collision bugs explained
- **Polish by Unit 128** — a complete NES platformer

---

## Phase 1: Basic Platforming (Units 1-16)

**Goal:** Player can run, jump, and land on platforms.

| Unit | You Add | Result |
|------|---------|--------|
| 1 | Player sprite + gravity | Falls to bottom |
| 2 | Floor tile collision | Stops on floor |
| 3 | Left/right movement | Walk around |
| 4 | Jump (impulse) | **Can jump!** |
| 5 | Jump arc (gravity applied) | Natural arc |
| 6 | Landing detection | Smooth landing |
| 7 | Platform tiles in nametable | Level geometry |
| 8 | Platform collision | **Land on platforms** |
| 9 | Walk off edge = fall | Correct behaviour |
| 10 | Jump sound (APU) | Feedback |
| 11 | Land sound | Polish |
| 12 | Simple level layout | One screen |
| 13 | Exit door tile | Goal |
| 14 | Reach door = complete | **Playable game** |
| 15 | Level complete sound | Celebration |
| 16 | Integration + edge cases | Solid foundation |

**NES-Specific Unit 1:**
```asm
; Gravity - applied every frame to player velocity
; Using 4.4 fixed-point for sub-pixel precision

GRAVITY = $08       ; 0.5 pixels per frame (in 4.4)
MAX_FALL = $40      ; 4 pixels per frame maximum

update_gravity:
    lda player_vel_y
    clc
    adc #GRAVITY
    cmp #MAX_FALL
    bcc @no_cap
    lda #MAX_FALL
@no_cap:
    sta player_vel_y
    rts

apply_velocity:
    ; Add velocity to position (sub-pixel)
    lda player_y_sub
    clc
    adc player_vel_y
    sta player_y_sub
    lda player_y
    adc #0              ; Carry from sub-pixel
    sta player_y
    rts
```

**Tile Collision Basics:**
```asm
; Check tile at player's feet
; Tiles $01-$0F = solid platforms

check_floor:
    ; Calculate nametable address from player position
    lda player_y
    clc
    adc #16             ; Check below sprite (feet)
    lsr
    lsr
    lsr                 ; /8 = tile row
    ; ... calculate nametable address ...

    lda (tile_ptr),y    ; Read tile
    cmp #$10            ; Solid if < $10
    bcc @solid
    ; Not solid - player falls
    rts
@solid:
    ; Stop falling, snap to tile top
    lda #0
    sta player_vel_y
    rts
```

**If it doesn't work (Phase 1):**
- **Player falls through floor?** Check tile collision BEFORE moving, not after
- **Player stuck in tiles?** Push player out of collision, don't just stop velocity
- **Jumping feels floaty?** Increase gravity or reduce initial jump velocity
- **Can't reach platforms?** Check jump height vs. platform spacing
- **Collision offset wrong?** Remember: sprite position is top-left, feet are +16 pixels

**End of Phase 1:** Basic platforming works. Jump, land, reach goal.

---

## Phase 2: Level Design (Units 17-32)

**Goal:** Multiple levels stored in ROM.

| Unit | You Add | Result |
|------|---------|--------|
| 17 | Level data format (metatiles) | Efficient storage |
| 18 | Metatile to tile expansion | Data-driven levels |
| 19 | Load level to nametable | System works |
| 20 | Level 2 | Variety |
| 21 | Level 3 | Progression |
| 22 | Lives system | Stakes |
| 23 | Fall off screen = death | Consequence |
| 24 | Death animation | Feedback |
| 25 | Respawn at level start | Try again |
| 26 | Game over screen | End state |
| 27 | Level 4 (harder jumps) | Challenge |
| 28 | Level 5 (precision) | Skill test |
| 29 | Level counter display | Progress |
| 30 | Score display | Competition |
| 31 | Points for completing | Reward |
| 32 | Integration + balance | 5 solid levels |

**NES-Specific:**
- Metatiles: 2×2 tiles grouped (16×16 pixels) for easier level design
- Level data: 16×12 metatiles = 192 bytes per level (very compact)
- Attribute table: set per metatile for consistent colouring
- Levels stored in PRG ROM, copied to nametable

**Metatile Example:**
```asm
; Metatile definitions (4 tiles each)
metatile_empty:   .byte $00, $00, $00, $00  ; Air
metatile_brick:   .byte $01, $02, $03, $04  ; Solid brick
metatile_crate:   .byte $05, $06, $07, $08  ; Crate platform
metatile_ladder:  .byte $09, $0A, $09, $0A  ; Ladder

; Level 1 data (16 wide × 12 tall metatiles)
level_1:
    .byte $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
    ; ... etc
```

**If it doesn't work (Phase 2):**
- **Level looks wrong?** Check metatile expansion order (top-left, top-right, bottom-left, bottom-right)
- **Attributes wrong?** Each attribute byte covers 4×4 tiles (2×2 metatiles)
- **Level doesn't load?** Ensure PPU is disabled during nametable writes

**End of Phase 2:** 5 levels, lives, death, game over.

---

## Phase 3: Hazards and Enemies (Units 33-48)

**Goal:** Dangers beyond falling.

| Unit | You Add | Result |
|------|---------|--------|
| 33 | Hazard tile (spikes) | Danger zone |
| 34 | Touch hazard = death | Consequence |
| 35 | Hazard graphics | Visual clarity |
| 36 | Moving platform (sprite) | Dynamic |
| 37 | Ride moving platform | New mechanic |
| 38 | Moving platform (vertical) | Variety |
| 39 | Enemy sprite | Active threat |
| 40 | Enemy patrol (back/forth) | Predictable |
| 41 | Touch enemy = death | Danger |
| 42 | Enemy hit sound | Feedback |
| 43 | Conveyor belt tile | Movement modifier |
| 44 | Conveyor affects player | New mechanic |
| 45 | Collapsing platform | Timing element |
| 46 | Collapse animation | Visual warning |
| 47 | Levels 6-8 with hazards | Application |
| 48 | Integration + balance | Fair challenge |

**NES-Specific:**
- Enemies: additional sprites, managed in OAM
- Moving platforms: can be sprites or animated tiles
- Conveyor: modify player velocity when standing on specific tiles
- Collapse: swap nametable tiles over time using buffered updates

**If it doesn't work (Phase 3):**
- **Player clips through moving platform?** Update platform BEFORE player collision
- **Enemy sprite limit?** NES allows 64 sprites, 8 per scanline - plan placement
- **Tile animation stutters?** Buffer nametable writes, apply during vblank

**End of Phase 3:** 8 levels with varied hazards and enemies.

---

## Phase 4: Player Abilities (Units 49-64)

**Goal:** More things the player can do.

| Unit | You Add | Result |
|------|---------|--------|
| 49 | Walk animation (2 frames) | Life |
| 50 | Walk animation (4 frames) | Smooth |
| 51 | Jump animation | Polish |
| 52 | Fall animation | Distinction |
| 53 | Direction facing (flip) | Responsiveness |
| 54 | Collectible items | Goals |
| 55 | Collect = points | Reward |
| 56 | Collect sound | Feedback |
| 57 | All items = bonus | Incentive |
| 58 | Ladder tile | New traversal |
| 59 | Climb ladder | Vertical movement |
| 60 | Ladder animation | Polish |
| 61 | Variable jump height | Skill expression |
| 62 | Coyote time | Forgiveness |
| 63 | Levels 9-12 | Application |
| 64 | Integration + feel | Tight controls |

**NES-Specific:**
```asm
; Variable jump - cut velocity when button released
check_jump_release:
    lda controller
    and #BUTTON_A
    bne @still_held

    ; Button released - cut upward velocity
    lda player_vel_y
    bpl @done           ; Already falling
    lsr                 ; Halve upward velocity
    ora #$80            ; Keep negative (upward)
    sta player_vel_y
@still_held:
@done:
    rts

; Coyote time - allow jump briefly after walking off edge
COYOTE_FRAMES = 6

update_coyote:
    lda on_ground
    bne @reset
    ; Not on ground - count down
    lda coyote_timer
    beq @done
    dec coyote_timer
    rts
@reset:
    lda #COYOTE_FRAMES
    sta coyote_timer
@done:
    rts
```

**If it doesn't work (Phase 4):**
- **Animation wrong frame?** Check animation counter and state transitions
- **Sprite flip doesn't work?** Set OAM attribute bit 6 for horizontal flip
- **Coyote time too generous?** Reduce frame count
- **Variable jump not working?** Ensure velocity check distinguishes rising vs falling

**End of Phase 4:** 12 levels, animated player, ladders, tight controls.

---

## Phase 5: Audio Polish (Units 65-80)

**Goal:** Full APU soundtrack.

| Unit | You Add | Result |
|------|---------|--------|
| 65 | Title music | Atmosphere |
| 66 | In-game music | Energy |
| 67 | Music engine basics | System |
| 68 | Death jingle | Punctuation |
| 69 | Level complete jingle | Celebration |
| 70 | Game over music | Finality |
| 71 | Jump sound variety | Interest |
| 72 | Enemy sounds | Presence |
| 73 | Hazard sounds | Warning |
| 74 | Collectible sounds | Reward |
| 75 | Low lives warning | Tension |
| 76 | SFX during music | Mixing |
| 77 | Music per level set | Variety |
| 78 | Sound options | Accessibility |
| 79 | Audio mixing | Balance |
| 80 | Integration | Cohesive |

**NES-Specific:**
- APU: 2 pulse, 1 triangle, 1 noise, 1 DMC
- Typical: music uses pulse 1+2 and triangle, SFX steals pulse 2 or uses noise
- Music engine: simple note table, duration counter, pattern playback
- Consider using established formats (FamiTracker) for music data

**End of Phase 5:** Full music and sound effects.

---

## Phase 6: Visual Polish (Units 81-96)

**Goal:** Look like a commercial NES game.

| Unit | You Add | Result |
|------|---------|--------|
| 81 | CHR design pass | Unique look |
| 82 | Player sprite detail | Character |
| 83 | Enemy sprite variety | Interest |
| 84 | Background decoration | Depth |
| 85 | Animated tiles (water, etc.) | Life |
| 86 | Palette optimisation | Colour |
| 87 | Death effect | Impact |
| 88 | Level complete effect | Celebration |
| 89 | Screen transitions | Flow |
| 90 | UI design | Clean |
| 91 | Status bar | Information |
| 92 | Theme per level set | Variety |
| 93 | Title screen art | Presentation |
| 94 | Sprite priorities | Depth |
| 95 | Flicker management | Professional |
| 96 | Integration | Cohesive |

**NES-Specific:**
- CHR ROM: 8KB for sprites, 8KB for background (typical NROM)
- Palettes: 4 background + 4 sprite palettes, 3 colours each + shared background
- Animated tiles: update CHR RAM if using CHR RAM, or swap pattern table pointers
- Sprite 0 hit for status bar split (optional advanced technique)

**End of Phase 6:** Looks like a real NES game.

---

## Phase 7: Advanced Features (Units 97-112)

**Goal:** Features beyond basics.

| Unit | You Add | Result |
|------|---------|--------|
| 97 | High score table | Competition |
| 98 | Initials entry | Ownership |
| 99 | Scores in RAM | Persistence (session) |
| 100 | Title animation | Polish |
| 101 | Attract mode | Showcase |
| 102 | Two-player alternating | Multiplayer |
| 103 | Bonus level | Variety |
| 104 | Secret areas | Exploration |
| 105 | Warp zones | Speedrun |
| 106 | Difficulty settings | Accessibility |
| 107 | Password system | Progress save |
| 108 | Boss level | Milestone |
| 109 | Boss pattern | Challenge |
| 110 | Boss defeated | Payoff |
| 111 | Enemy variety | Fresh |
| 112 | Integration + balance | Complete |

**NES-Specific:**
- Passwords: encode level + score + lives into 8-16 characters (like Metroid)
- High scores: stored in RAM, lost on power off (battery backup in later games)
- Two-player: read controller 2, alternate on death

**End of Phase 7:** Full-featured platformer.

---

## Phase 8: Final Polish (Units 113-128)

**Goal:** ROM-ready quality.

| Unit | You Add | Result |
|------|---------|--------|
| 113 | Levels 13-16 | More content |
| 114 | Levels 17-20 | Full game |
| 115 | Difficulty curve | Fair |
| 116 | Control tuning | Responsive |
| 117 | Bug hunting | Stable |
| 118 | Edge cases | Robust |
| 119 | PRG/CHR optimisation | Efficient |
| 120 | iNES header | Standard format |
| 121 | ROM file creation | Distribution |
| 122 | Emulator testing | Compatibility |
| 123 | Ending sequence | Reward |
| 124 | Credits | Attribution |
| 125 | Final testing | Quality |
| 126 | Documentation | Homebrew ready |
| 127 | Performance pass | Smooth |
| 128 | **Complete game** | Ship it! |

**End of Phase 8:** A complete NES platformer ROM.

---

## Crate Escape Debugging Guide

**Tile Collision Issues:**
- Player falls through floors → Check collision point is at feet, not sprite origin
- Player stuck in walls → Separate X and Y collision, resolve each axis
- Player vibrates on slopes → Snap to surface, don't just reverse velocity
- Collision inconsistent → Use consistent fixed-point math

**Jump Issues:**
- Can jump in mid-air → Check ground flag before allowing jump
- Jump height varies → Ensure consistent frame timing (NMI-driven)
- Can't reach platforms → Adjust jump velocity or level design

**Sprite Issues:**
- Sprites don't appear → Check OAM DMA is happening each frame
- Wrong sprites shown → Verify OAM tile indices match CHR data
- Flickering → Rotate sprite priority when near 8-per-scanline limit

**NES-Specific Issues:**
- Game crashes → Check for stack overflow, infinite loops
- Graphics corrupt → Ensure PPU writes only during vblank
- Music glitches → APU updates must be consistent

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 8 (Unit 128) |
|--------|-------------------|---------------------|
| Levels | 1 screen | 20 varied levels |
| Player | Walk + jump | Full animation, abilities |
| Hazards | None | Enemies, spikes, conveyors |
| Audio | Jump sound | Full music + SFX |
| Visuals | Basic tiles | Polished, themed |
| Features | Reach door | High scores, passwords, boss |

---

## The NES Platformer Context

The NES defined the platformer genre. This game teaches:
- **Tile-based thinking** — everything is 8×8 or 16×16
- **Constraint creativity** — 4 palettes, 8 sprites per line
- **Feel over features** — Mario's jump feel took months to perfect
- **The NES way** — vblank-driven, OAM DMA, pattern tables

This is the foundation for scrolling platformers (Game 8) and run'n'gun games (Game 12).

---

**Version:** 1.0
**Last Updated:** 2026-01-18
