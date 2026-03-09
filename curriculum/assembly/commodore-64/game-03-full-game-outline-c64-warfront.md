# Full Game Outline: C64 Warfront (512 Units)

**Game:** Warfront (Game 3)
**Units:** 512 (16 phases × 32 units)
**Genre:** Run 'n' gun
**Inspired by:** Turrican, Turrican II, Contra, Metal Warrior
**Target Quality:** Commercial-grade action game (1990–92 era)

---

## Premise

The war machine has awakened. Five worlds lie between you and its core: jungle canopy, frozen fortress, molten foundry, machine city, and the living core itself. You run, jump, shoot in all directions, grapple across chasms, and transform into a rolling assault vehicle to blast through barriers. Hundreds of enemies. Massive bosses. Parallax scrolling that fills every pixel. The SID screaming.

This is the game that requires everything the C64 can do. 8-directional scrolling. Sprite multiplexing to put 20+ objects on screen. Raster effects for visual polish. SID music that drives the action. It's Turrican: the game that proved the C64 could match 16-bit machines in ambition, if not resolution.

---

## Why This Game

Turrican is the peak of C64 game development. Factor 5 pushed the hardware beyond what anyone thought possible: smooth multi-directional scrolling, dozens of sprites via multiplexing, parallax backgrounds, and a Chris Hülsbeck soundtrack that's still celebrated. Building a Turrican-scale game teaches the learner every advanced C64 technique.

Warfront teaches:
- **8-directional scrolling** — horizontal AND vertical, combined
- **Sprite multiplexing** — 16-32 sprites from 8 hardware slots, the definitive C64 technique
- **Parallax scrolling** — background layers at different speeds via raster splits
- **Grappling physics** — rope simulation with sine table swing
- **Vehicle transformation** — different physics model, different sprite set
- **Level streaming** — worlds too large for memory, loaded progressively
- **Advanced SID** — multi-speed music, filter sweeps, digi-drums
- **Boss state machines** — multi-phase encounters with weak points

---

## 6510 Progression

| Phase | 6510 Focus |
|-------|-----------|
| 1-2 | 8-way scrolling: combined H+V fine/coarse scroll, tile streaming |
| 3-4 | Sprite multiplexing: Y-sorted allocation, raster chain, flicker management |
| 5-6 | Player mechanics: 8-way shooting, grappling hook (sine table), vehicle mode |
| 7-8 | Enemy systems: wave spawning, AI types, bullet patterns |
| 9-10 | 5 worlds: level data, streaming, themes, bosses |
| 11-12 | Advanced SID: multi-speed music, digi-drums, filter automation |
| 13-14 | Parallax, visual effects, polish |
| 15-16 | Production: fast loader, PAL/NTSC, distribution |

---

## Phase 1-2: The Scroll Engine (Units 1–64)

**Goal:** 8-directional scrolling with tile-based terrain.

**Phase 1 (Units 1-32):** Horizontal scrolling — the same fine/coarse technique from Coldframe, but faster and optimised. The scroll speed must support running-speed gameplay, not the deliberate pace of a stealth game. Character set tiles for terrain. Tile map wider and taller than the screen.

**Phase 2 (Units 33-64):** Add vertical scrolling. Combined H+V scroll: the screen can move in any of 8 directions depending on player movement. The tile map is a 2D grid; the viewport slides across it. Column streaming (horizontal) and row streaming (vertical) feed new tiles at the scroll edges.

Key techniques:
- **Fine scroll:** $D016 (horizontal bits 0-2) and $D011 (vertical bits 0-2) updated per frame
- **Coarse scroll:** Screen RAM shifted by one character column or row when fine scroll wraps
- **Tile streaming:** New column/row drawn at the leading edge, just off-screen
- **Double-width screen:** VIC displays 40 columns; the buffer is 42 columns wide, giving 2 columns of off-screen margin for smooth tile insertion
- **Raster-stable scroll:** IRQ ensures scroll registers update during vertical blank

```asm
; Combined fine scroll update
scroll_update:
    ; Horizontal
    lda scroll_hfine
    clc
    adc scroll_hdelta
    cmp #8
    bcc .no_hcoarse
    sbc #8
    pha
    jsr coarse_scroll_h     ; Shift screen data horizontally
    pla
.no_hcoarse:
    sta scroll_hfine

    ; Vertical
    lda scroll_vfine
    clc
    adc scroll_vdelta
    cmp #8
    bcc .no_vcoarse
    sbc #8
    pha
    jsr coarse_scroll_v     ; Shift screen data vertically
    pla
.no_vcoarse:
    sta scroll_vfine

    ; Apply to VIC-II
    lda $d016
    and #$f8
    ora scroll_hfine
    sta $d016

    lda $d011
    and #$f8
    ora scroll_vfine
    sta $d011
    rts
```

**End of Phase 2:** Smooth 8-directional scrolling with tile streaming. The world is larger than the screen in both dimensions.

---

## Phase 3-4: Sprite Multiplexing (Units 65–128)

**Goal:** Display 16-32 sprites using 8 hardware slots.

**Phase 3 (Units 65-96):** The multiplexer algorithm.
- Sort all active sprites by Y position
- Assign sprites to hardware slots top-to-bottom
- Set up a chain of raster interrupts: each fires just below a sprite's last scanline
- Each interrupt handler repositions that slot's X/Y, data pointer, and colour for its next assignment
- Handle the "crunch bug" (VIC-II glitch when sprite Y = raster line during bad-line)

**Phase 4 (Units 97-128):** Multiplexer integration with gameplay.
- Player sprite(s) always allocated (never flickered away)
- Bullets as multiplexed sprites
- Enemies as multiplexed sprites
- Priority: player > bullets > nearest enemies > distant enemies
- Flicker management: if more sprites than slots at a Y position, rotate which ones are visible
- Performance profiling: how many sprites before the raster chain can't keep up?

```asm
; Simplified multiplexer concept
; After sorting sprites by Y:
;
; For each hardware slot (0-7):
;   Find the next unassigned virtual sprite
;   Set the raster IRQ to fire at that sprite's Y - 1
;   In the IRQ handler:
;     Set slot's X, Y, data pointer, colour
;     Set the next raster IRQ for the next sprite assigned to this slot

multiplex_irq:
    ; Acknowledge IRQ
    lda #$01
    sta $d019

    ; Get next sprite assignment for this slot
    ldx current_slot
    ldy sprite_assignment,x

    ; Position the sprite
    lda sprite_x,y
    sta $d000,x            ; Even registers = X positions
    lda sprite_y,y
    sta $d001,x            ; Odd registers = Y positions
    lda sprite_ptr,y
    sta $07f8,x            ; Data pointer

    ; Set next raster line for this slot
    lda next_raster,x
    sta $d012

    rti
```

**Key Teaching Moment:**
Sprite multiplexing is the single technique that separates amateur C64 games from professional ones. Katakis, Armalyte, Turrican, IO — they all use it. The concept is simple: once the electron beam passes a sprite, that hardware slot is free to be reused further down the screen. The implementation is hard: sorting, timing, raster chains, edge cases. This is the C64's deepest technique, and Warfront is where the learner masters it.

**End of Phase 4:** 16-32 multiplexed sprites. Player, bullets, and enemies all rendered from 8 hardware slots. The screen fills with action.

---

## Phase 5-6: Player Mechanics (Units 129–192)

**Phase 5 (Units 129-160):** Core player.
- 8-directional movement with momentum
- Jump with variable height
- 8-directional shooting (aim with joystick direction, fire button shoots)
- Weapon types: standard shot, spread, laser, bounce. Power-up items switch weapon.
- Player animation: walk (8 directions × 4 frames), jump, fall, crouch, shoot (per direction)

**Phase 6 (Units 161-192):** Advanced player.
- **Grappling hook:** Fire upward, rope attaches to ceiling. Player swings on a pendulum (sine table for arc). Release to fly in the swing direction. The signature Turrican move.
- **Vehicle mode:** Press down while crouched → transform into a rolling ball/vehicle. Different physics (faster, lower, fits through gaps, has a different weapon). Press jump to revert.
- **Shield:** Limited-use energy shield absorbs hits. Depletes over time when active.

The grappling hook uses a pre-computed sine table for the swing arc. The rope is drawn as a line of characters or sprites between the player and the anchor point.

**End of Phase 6:** Full player moveset — run, jump, shoot in 8 directions, grapple, transform, shield. The player is as capable as Turrican's protagonist.

---

## Phase 7-8: Enemies and Combat (Units 193–256)

**Phase 7 (Units 193-224):** Enemy variety.
- Walkers (patrol platforms), flyers (sine-wave or chase), turrets (fixed, fire at player), spawners (create enemies until destroyed), bombers (drop projectiles)
- Enemy bullet patterns: aimed, spread, stream
- Enemy health varies by type (1-hit fodder to 5-hit tanks)
- Destruction effects: explosion sprite, score popup, power-up drop chance

**Phase 8 (Units 225-256):** Boss encounters.
- One boss per world (5 total). Multi-sprite constructions (4-8 sprites per boss).
- Boss state machines: idle → telegraph → attack → recover. Multiple phases (pattern change at 50% health).
- Weak points: only specific parts take damage. Destructible armour sections.
- Boss arenas: scrolling stops, arena boundaries set.

**End of Phase 8:** 8+ enemy types, bullet patterns, and 5 multi-phase boss encounters. Combat is intense and varied.

---

## Phase 9-10: The Five Worlds (Units 257–320)

**Phase 9 (Units 257-288):** Worlds 1-3.
- **World 1: Canopy** — jungle terrain, vine platforms, organic enemies. Green/brown palette.
- **World 2: Fortress** — ice and stone, sliding surfaces, mechanical enemies. White/cyan palette.
- **World 3: Foundry** — lava, conveyor belts, fire hazards, armoured enemies. Red/orange palette.

Each world: 3-4 scrolling areas + boss arena. Distinct tile sets, enemy rosters, and colour palettes. Level data streamed from compressed storage.

**Phase 10 (Units 289-320):** Worlds 4-5.
- **World 4: Machine City** — metallic terrain, complex platform arrangements, turret-heavy. Grey/blue palette.
- **World 5: The Core** — organic-mechanical hybrid, pulsing walls, the final boss. Dark with accent colours.

**End of Phase 10:** 5 complete worlds with distinct themes, enemies, and bosses. The game is content-complete.

---

## Phase 11-12: Sound (Units 321–384)

**Phase 11 (Units 321-352):** SID music.
- Multi-speed music engine (play at 2× or 4× the normal rate for more notes per frame — used by Chris Hülsbeck in Turrican)
- Per-world themes: epic, driving, atmospheric
- Boss music: intense, different from level themes
- CIA timer-driven playback at stable tempo

**Phase 12 (Units 353-384):** SID effects and advanced techniques.
- Digi-drums: 4-bit samples played via $D418 volume register, interleaved with music
- Filter automation: cutoff sweeps synced to gameplay events
- Ring modulation for alien/mechanical sounds
- Sound priority: gameplay SFX steal voices briefly, music continues underneath

**End of Phase 12:** A Hülsbeck-quality SID soundtrack. Multi-speed playback, digi-drums, filter sweeps. The SID at its absolute peak.

---

## Phase 13-14: Visual Polish (Units 385–448)

**Phase 13 (Units 385-416):** Parallax scrolling.
- Raster split: different scroll offset in the background area vs. foreground
- Background layer uses colour RAM manipulation (attribute-based parallax) or a second character set
- Distant mountains/sky scroll at half speed. Foreground at full speed.
- Per-world parallax configuration (jungle has tree canopy layers, fortress has snowfall, foundry has heat shimmer)

**Phase 14 (Units 417-448):** Visual effects.
- Screen shake on explosions (VIC-II scroll register jitter)
- Raster colour bars in borders (C64 signature)
- Colour cycling for lava, water, energy effects
- Particle-like explosion debris (multiplexed micro-sprites)
- Player damage flash (sprite colour strobe)

**End of Phase 14:** Parallax depth, screen shake, raster effects. Visually competitive with late-era C64 releases.

---

## Phase 15-16: Production (Units 449–512)

**Phase 15 (Units 449-480):** Distribution technology.
- **Fast loader:** Custom tape loading routine (3000+ baud vs. 1500 standard)
- **IRQ loader:** Continue loading data while the game runs (load next world during current world)
- **Direct 1541 drive programming:** Send a fast-load routine to the drive's own 6502, controlling the read head directly
- **Multi-load architecture:** Title + world 1 load first. Worlds 2-5 load on demand.
- **D64 disk image creation**

**Phase 16 (Units 481-512):** Ship it.

| Unit | You Add | Result |
|------|---------|--------|
| 481-484 | Title screen with demo-scene effects: raster bars, colour cycling, DYCP scroller for credits | Impressive opening |
| 485-488 | High scores, difficulty select, attract mode | Professional package |
| 489-492 | PAL/NTSC detection, 6581/8580 SID detection | Universal compatibility |
| 493-496 | Ending sequence: core destroyed, escape, world saved, credits roll | Narrative closure |
| 497-504 | Final testing: all 5 worlds, all difficulties, PAL+NTSC, 6581+8580 | Release quality |
| 505-508 | D64 (disk) + TAP (tape) distribution. Loading screen. Fast loader. | Dual format |
| 509-512 | **Complete game** | **Ship it** |

---

## Technical Notes

### Sprite Multiplexer Performance

With a Y-sorted raster chain:
- 8 sprites displayed without multiplexing: always works
- 12-16 sprites: comfortable, 1-2 raster IRQs per slot
- 20-24 sprites: achievable, requires tight IRQ handlers (~40 cycles each)
- 28-32 sprites: maximum practical limit, requires cycle-exact handlers and careful Y-spacing

The "crunch bug" (VIC-II DMA timing conflict) occurs when a sprite's Y position equals the current raster line during a bad-line. Avoid by ensuring multiplexed sprites are repositioned at least 2 lines below the current display position.

### 8-Way Scroll Performance

Combined horizontal + vertical scrolling requires:
- Fine scroll update: ~20 cycles (register writes)
- Coarse scroll H: ~800 cycles (shift 1000 bytes of screen RAM, or use self-modifying scroll)
- Coarse scroll V: ~800 cycles (shift 1000 bytes vertically)
- Tile streaming: ~200-400 cycles (draw new column or row)
- Colour RAM sync: ~800 cycles (if scrolling, shift colour RAM too)

Total worst case (diagonal coarse scroll): ~2,800 cycles. At ~19,656 cycles per frame (PAL), this leaves ~16,000 cycles for everything else. Tight but achievable with optimisation.

### Level Data

Each world is ~4-6 screens wide × 3-4 screens tall. At 42×27 tiles per screen, that's ~170×100 tiles = ~17,000 bytes uncompressed per world. With RLE: ~3-5KB per world. All 5 worlds: ~15-25KB. Fits in memory with bank switching or multi-load.

### Memory Map

```
$0400-$07FF: Screen RAM (VIC bank 0)
$0800-$0FFF: Screen RAM 2 (double-buffer)
$1000-$1FFF: Character set (terrain tiles)
$2000-$3FFF: Sprite data (player, enemies, bullets, bosses, effects)
$4000-$9FFF: Game code (~24KB)
$A000-$BFFF: Music + sound engine (~8KB)
$C000-$CFFF: Current world data (decompressed tile map, ~4KB)
$D000-$DFFF: I/O
$E000-$FFFF: World data bank / Kernal (switch as needed)
```

---

## The C64 Arc (So Far)

| Game | Focus | Scale |
|------|-------|-------|
| Nova Storm | Sprites + SID + raster basics | Fixed screen, 8 sprites |
| Coldframe | Scrolling + large sprites + atmosphere | Scrolling rooms, stealth |
| Warfront | Everything at maximum | 8-way scroll, 20+ multiplexed sprites, 5 worlds |

Each game doubles the ambition. Nova Storm is "here's a sprite." Coldframe is "here's a scrolling room." Warfront is "here's Turrican."

---

## Changelog

- **v1.0 (2026-03-09):** Initial outline. New Game 3 for the restructured C64 assembly track. Run 'n' gun with sprite multiplexing, 8-way scrolling, and advanced SID.
