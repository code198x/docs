# Full Game Outline: NES Starweave (512 Units)

**Game:** Starweave (Game 4 — Capstone)
**Units:** 512 (16 phases × 32 units)
**Genre:** Multi-style action game with late-era NES polish
**Inspired by:** Kirby's Adventure, Batman: Return of the Joker, Shatterhand, Little Samson
**Target Quality:** Late-era NES showcase (1991–93 era)

---

## Premise

The sky-loom is broken. The constellations — once woven into patterns by the celestial weavers — are unravelling. Stars fall from the sky like loose threads. The world below darkens as the patterns dissolve.

You are a weaver's apprentice. Armed with a star-thread that can bind, pull, and mend, you climb through five realms from the surface to the sky-loom itself. Each realm has its own way of moving: surface forests demand platforming, underwater caverns require swimming physics, cloud kingdoms use wind currents, the mechanical orrery demands puzzle-solving, and the sky-loom itself is a vertical climb through star-thread constructions you weave as you go.

Five gameplay styles in one cartridge. The NES doing what Kirby's Adventure proved it could: varied, beautiful, and technically astonishing for 8-bit hardware.

---

## Why This Is the Capstone

Starweave requires every technique from Games 1-3 plus the production polish of the NES's final commercial years:

| From Game | Technique | Use in Starweave |
|-----------|-----------|-----------------|
| Dash | PPU fundamentals, scrolling, platforming | Core movement, forest realm |
| Dash | APU basics, NMI game loop | Sound engine foundation |
| Wyrdstone | Screen transitions, SRAM saves | Realm transitions, save system |
| Wyrdstone | Combat, item system, NPC text | Star-thread abilities, dialogue |
| Abyssal Gate | MMC3 bank switching | Multiple tilesets per realm |
| Abyssal Gate | Scanline counter HUD split | Fixed HUD above scrolling game |
| Abyssal Gate | Ability-gated world design | Star-thread upgrades open new paths |

**New in Starweave:**
- **CHR animation** — animated background tiles (waterfalls, machinery, star-thread shimmer) via mid-frame CHR bank swaps
- **Advanced DMC** — sampled bass, percussion, voice clips ("Level Clear!"), mixed with APU music
- **NTSC/PAL detection** — timing, speed, and music pitch adjusted automatically
- **Multiple gameplay styles** — platforming, swimming, wind-riding, puzzle, vertical climbing
- **Cinematic sequences** — nametable-animated cutscenes between realms
- **Attract mode with demo playback** — recorded input, title screen showcase
- **Professional ROM layout** — efficient bank organisation, minimal wasted space

---

## The Five Realms

| Realm | Setting | Gameplay Style | CHR Theme | Musical Feel |
|-------|---------|---------------|-----------|-------------|
| 1: Thornwood | Forest, ruins, rivers | Standard platforming | Green/brown natural | Pastoral, adventurous |
| 2: Deepwell | Underwater caverns, coral, currents | Swimming physics (buoyancy, drag) | Blue/cyan aquatic | Flowing, mysterious |
| 3: Cloudspire | Cloud platforms, wind currents, sky temples | Wind-affected movement, gliding | White/gold celestial | Soaring, bright |
| 4: The Orrery | Mechanical planetarium, gears, lenses | Puzzle-platforming (redirect beams, move gears) | Grey/bronze mechanical | Precise, rhythmic |
| 5: Sky-Loom | Woven star-thread constructions, void | Vertical climb, weave platforms as you go | Black/white/all colours | Triumphant, building |

Each realm has 3 stages + 1 boss. 15 stages + 5 bosses total.

### Gameplay Variety

The multi-style approach prevents the game from feeling like "another platformer." Each realm changes how the player interacts with the world:

- **Thornwood:** Run, jump, shoot star-thread. Standard platforming refined to perfection.
- **Deepwell:** Swimming inverts the physics model. Buoyancy replaces gravity. Currents push the player. Air meter limits exploration time.
- **Cloudspire:** Wind currents affect jump trajectory. The player can glide on updrafts. Platforms blow away if you stand too long.
- **The Orrery:** The star-thread can interact with machinery. Pull levers, redirect light beams through lenses, rotate gear assemblies. More puzzle than action.
- **Sky-Loom:** The star-thread weaves platforms into existence. The player creates the level as they climb. The ultimate expression of the game's central mechanic.

---

## Core Mechanics

### Star-Thread

The player's tool and weapon. A luminous thread that can:
- **Strike:** Short-range attack (like a whip). Defeats enemies, breaks obstacles.
- **Pull:** Latch onto grapple points. Swing or pull the player toward the anchor.
- **Bind:** Wrap enemies temporarily. Stun, not kill — the gentler option.
- **Weave:** In Realm 5, create temporary platforms from star-thread. Costs thread energy.

Thread energy replenishes from star fragments (collectibles) and save points.

### Star Fragments

Scattered throughout every realm. 100 per realm, 500 total. Collecting 80% of a realm's fragments reveals a hidden area with a thread upgrade. Completion percentage tracks fragments + upgrades + bosses.

### Thread Upgrades

| Upgrade | Found in | Effect |
|---------|----------|--------|
| Long Thread | Thornwood | Strike range doubles |
| Aqua Thread | Deepwell | Thread works underwater (normally it doesn't) |
| Gale Thread | Cloudspire | Thread pulls faster, can redirect wind |
| Gear Thread | Orrery | Thread interacts with machinery |
| Loom Thread | Sky-Loom | Thread can weave platforms |

Each upgrade is required to complete the next realm. Backtracking to previous realms with new upgrades reveals secrets.

---

## Phase Breakdown

### Phases 1-4: Engine and Realm 1 (Units 1–128)

**Phase 1 (Units 1-32): MMC3 Platform**

Build on Abyssal Gate's MMC3 foundation. Set up bank layout for 5 realms + shared code.

| Unit | You Add | NES Skill | Result |
|------|---------|-----------|--------|
| 1-8 | MMC3 bank layout for Starweave | PRG banks: engine, realms 1-5, music, shared data | Memory organised |
| 9-16 | Scrolling platformer on MMC3 | Horizontal scroll with scanline HUD (from Abyssal Gate) | Platform engine |
| 17-24 | Player: run, jump, star-thread strike | Animation system, thread as whip attack | Core mechanics |
| 25-32 | Thornwood Stage 1 | Forest tileset, platforms, first enemies, star fragments | **First playable stage** |

**Phase 2 (Units 33-64): Thornwood Complete**

| Unit | You Add | NES Skill | Result |
|------|---------|-----------|--------|
| 33-40 | Thread pull (grapple points) | Grapple anchor tiles, swing physics (sine table), release momentum | Movement expansion |
| 41-48 | Thread bind (stun enemies) | Enemy state: active/stunned/defeated. Stun timer. | Non-lethal option |
| 49-56 | Thornwood Stages 2-3 | Varied terrain, increasing challenge, mid-stage checkpoints | Three stages |
| 57-64 | Thornwood boss: The Thornwarden | Multi-sprite tree guardian. Phase 1: root attacks. Phase 2: branch sweep. Weak to thread-pull on exposed core. | **First boss** |

**Phase 3 (Units 65-96): CHR Animation and Deepwell**

| Unit | You Add | NES Skill | Result |
|------|---------|-----------|--------|
| 65-72 | CHR bank animation | Swap CHR banks every N frames for animated background tiles: waterfalls flow, torches flicker, star-thread shimmers | **Animated backgrounds** |
| 73-80 | Swimming physics | Buoyancy: player floats upward by default. D-pad swims. Air meter depletes. Surface to breathe. | New movement model |
| 81-88 | Deepwell Stages 1-3 | Underwater tileset (coral, caverns, currents). Current tiles push the player. Air pockets. | Three underwater stages |
| 89-96 | Deepwell boss: The Tideclaw | Giant crab in an underwater arena. Bubble projectiles. Weak to thread-bind on claws. | Second boss |

**Key Teaching Moment (Units 65-72):**
CHR bank animation is a late-era NES technique. Swap the CHR bank containing waterfall tiles every 4 frames: bank A has water frame 1, bank B has water frame 2, bank C has frame 3. The waterfall animates without any CPU cost — the PPU reads from whichever bank is currently switched in. Every tile using those CHR addresses animates simultaneously. Kirby's Adventure used this extensively.

**Phase 4 (Units 97-128): Cloudspire and Wind**

| Unit | You Add | NES Skill | Result |
|------|---------|-----------|--------|
| 97-104 | Wind physics | Per-room wind direction and strength. Affects player horizontal velocity during jumps. | Environmental force |
| 105-112 | Gliding | Hold jump button while airborne → slow descent + wind carries player. Horizontal distance. | Air traversal |
| 113-120 | Cloudspire Stages 1-3 | Cloud platforms (dissolve timer), wind tunnels, sky temple interiors. Bright palette. | Three cloud stages |
| 121-128 | Cloudspire boss: The Zephyr | Wind-based boss. Creates tornadoes. Must use thread-pull to anchor against wind, then strike during calm. | Third boss |

**End of Phase 4:** Three realms complete (Thornwood, Deepwell, Cloudspire). Three gameplay styles. CHR animation. The game already has impressive variety.

---

### Phases 5-8: Remaining Realms (Units 129–256)

**Phase 5 (Units 129-160): The Orrery (Puzzle Realm)**
- Mechanical tileset. Gears, lenses, mirrors, pistons.
- Thread interacts with machinery: pull a lever, rotate a gear, redirect a light beam through mirrors to unlock doors.
- Less combat, more puzzle. A change of pace.
- 3 stages + boss: The Clockwork (mechanical construct with gear-based weak points).

**Phase 6 (Units 161-192): Sky-Loom (Final Realm)**
- Vertical scrolling (new direction — upward climb).
- Thread weaves temporary platforms: press a button → a platform appears at the thread's endpoint, lasting 3 seconds.
- The player creates the level as they climb. Resource management: thread energy limits platform creation.
- Mixed enemies from all previous realms.
- 3 stages + final boss: The Unraveller (the entity tearing the sky-loom apart).

**Phase 7 (Units 193-224): Boss Polish and Variety**
- All 5 bosses refined: multi-phase patterns, visual telegraphs, satisfying defeats.
- 5 mini-bosses (one per realm, mid-stage encounters).
- Boss defeat animations: CHR-animated explosion, realm restoration cutscene.
- Boss health bars using scanline-timed HUD elements.

**Phase 8 (Units 225-256): Enemy and Stage Polish**
- 20+ enemy types (4 per realm). Region-specific designs.
- Sprite limit management: 8-per-scanline cycling, priority system.
- Stage checkpoints (restart mid-stage on death, not stage start).
- Star fragment placement: some require backtracking with later upgrades.
- Difficulty curve: Thornwood gentle, Sky-Loom demanding.

**End of Phase 8:** All 5 realms, 15 stages, 5 bosses, 5 mini-bosses, 20+ enemy types. Content-complete.

---

### Phases 9-12: Audio and Cinematics (Units 257–384)

**Phase 9 (Units 257-288): APU Music**
- Per-realm themes reflecting the realm's mood and pace.
- Boss theme (shared, intense), mini-boss variant.
- Title theme, realm-select theme, ending theme.
- NMI-driven sequencer with per-channel volume control.

**Phase 10 (Units 289-320): DMC and Advanced Audio**
- DMC bass drum in boss encounters and action peaks.
- DMC impact samples for thread attacks and explosions.
- DMC voice sample: brief "Level Clear!" or "Star Thread!" on key events (4-bit delta, ~4KB per sample).
- SFX: jump, land, thread-strike, thread-pull (with reel-in sound), thread-bind (shimmer), swim, glide, weave, collect, damage, boss hit.
- Music + SFX coexistence: SFX steal pulse 2, music continues on pulse 1 + triangle + noise + DMC.

**Phase 11 (Units 321-352): Cinematic Sequences**
- Between realms: brief cutscene showing the sky-loom's state. Stars falling, threads unravelling, then — as you restore each realm — threads reweaving.
- Implemented as nametable animations: pre-drawn frames loaded sequentially during VBlank. CHR bank swaps for frame-by-frame animation.
- Text overlays for narration: "The Thornwood stirs. The first thread holds."
- No separate "cutscene engine" — reuse existing nametable write and CHR swap tools.

**Phase 12 (Units 353-384): Audio Polish**
- Per-realm ambient variations (Deepwell: underwater filter effect on music via pulse duty cycle).
- Dynamic music: boss theme intensifies at boss phase 2 (tempo increase or additional channel activity).
- Audio balance across all realms, bosses, cutscenes.
- NTSC music tempo vs PAL: adjust note durations for correct pitch at both frame rates.

**End of Phase 12:** Full soundtrack with DMC, cinematic realm transitions, dynamic boss music. Professional audio.

---

### Phases 13-16: Production (Units 385–512)

**Phase 13 (Units 385-416): NTSC/PAL and Compatibility**
- NTSC: 60fps, ~29,780 CPU cycles per frame.
- PAL: 50fps, ~33,247 CPU cycles per frame.
- Detection via frame-counting timing difference.
- Adjustments: scroll speed, gravity strength, enemy speed, music tempo, DMC sample rate.
- Test on both systems: gameplay should feel equivalent despite timing difference.

**Phase 14 (Units 417-448): Save System and Completion**
- Battery SRAM: 3 save slots. Per-slot: realm progress, star fragments collected (bitfield), upgrades acquired, boss flags, play time.
- Completion percentage: (fragments + upgrades + bosses) / total. Displayed on save select and ending.
- Multiple endings:
  - Under 50%: the loom holds, but barely. Brief ending.
  - 50-89%: the loom is restored. Standard ending with credits.
  - 90%+: the loom shines. Extended ending with full constellation animation.

**Phase 15 (Units 449-480): Presentation**
- Title screen: "STARWEAVE" with animated star-thread pattern (CHR animation). Realm-select if save exists.
- Attract mode: recorded input playback of Thornwood Stage 1. Shows the game in action.
- Endings implemented with constellation CHR animations (stars reconnecting, patterns forming).
- Credits: scrolling text with realm-themed background cycling.

**Phase 16 (Units 481-512): Ship It**

| Unit | You Add | Result |
|------|---------|--------|
| 481-488 | Final ending: constellation fully woven, dawn breaks, the apprentice becomes a weaver | Narrative climax |
| 489-492 | All three endings tested and polished | Narrative reward |
| 493-496 | ROM bank audit: efficient use of PRG/CHR, no wasted space | Professional layout |
| 497-504 | Full testing: all realms, all bosses, NTSC/PAL, saves, completion %, endings | Release quality |
| 505-508 | iNES ROM image: mapper 4, correct bank count, valid header | Distribution |
| 509-512 | **Complete game** | **Ship it** |

---

## Technical Notes

### CHR Animation

```asm
; Animate waterfalls by cycling CHR banks every 4 frames
; Banks 0, 1, 2 contain waterfall tiles at frames 0, 1, 2

chr_anim_update:
    lda frame_counter
    and #$0C            ; Bits 2-3: 0, 4, 8 → divide by 4
    lsr
    lsr                 ; A = 0, 1, 2, 3 (wraps every 16 frames)
    cmp #3
    bcc :+
    lda #0              ; Wrap 3 → 0 (cycle through 0,1,2)
:   sta $8000           ; MMC3 bank register select (CHR bank 0)
    sta $8001           ; Set CHR bank for animated tiles
    rts
```

### Multi-Style Physics

```asm
; Physics mode selected per realm
; 0 = standard platformer (Thornwood, Orrery)
; 1 = swimming (Deepwell)
; 2 = wind-affected (Cloudspire)
; 3 = weaving/vertical (Sky-Loom)

apply_physics:
    lda physics_mode
    asl
    tax
    lda physics_table,x
    sta ptr_lo
    lda physics_table+1,x
    sta ptr_hi
    jmp (ptr_lo)        ; Jump to mode-specific physics routine

physics_table:
    .word physics_standard
    .word physics_swimming
    .word physics_wind
    .word physics_weaving
```

### ROM Layout (MMC3, 256KB PRG + 128KB CHR)

```
PRG (32 × 8KB banks):
  Banks 0-1: Game engine (movement, combat, thread mechanics, PPU routines)
  Banks 2-3: Thornwood (stage data, enemies)
  Banks 4-5: Deepwell (stage + swimming physics)
  Banks 6-7: Cloudspire (stage + wind physics)
  Banks 8-9: Orrery (stage + puzzle mechanics)
  Banks 10-11: Sky-Loom (stage + weaving + vertical scroll)
  Banks 12-13: Boss data, cutscene data
  Banks 14-15: Music engine + music data
  Banks 16-17: DMC samples
  Banks 18-19: Text, NPC data, save system
  Banks 30-31: Fixed bank (NMI, reset, IRQ, core tables)

CHR (16 × 8KB banks):
  Banks 0-2: Thornwood (3 frames for CHR animation)
  Banks 3-5: Deepwell (3 frames)
  Banks 6-8: Cloudspire (3 frames)
  Banks 9-10: Orrery (2 frames — less animation)
  Banks 11-13: Sky-Loom (3 frames)
  Bank 14: Shared (HUD, text, common elements)
  Bank 15: Sprites (player, enemies — shared across realms, specific per bank swap)
```

---

## The NES Arc

| Game | Mapper | Style | Scale | Emotion |
|------|--------|-------|-------|---------|
| Dash | NROM | Platformer | Linear levels | Momentum, discovery |
| Wyrdstone | NROM/UNROM | Top-down adventure | Open overworld + dungeons | Exploration, mystery |
| Abyssal Gate | MMC3 | Metroidvania | 200+ connected rooms | Isolation, mastery |
| Starweave | MMC3 | Multi-style showcase | 5 realms, 5 gameplay modes | Wonder, craftsmanship |

The learner starts with a character on a black screen. They end with animated backgrounds, sampled audio, cinematic cutscenes, and five distinct gameplay modes in one cartridge. The NES has been fully explored — from the VBlank warmup to the last CHR bank swap.

---

## Changelog

- **v1.0 (2026-03-09):** Initial outline. NES assembly capstone. Multi-style action game with CHR animation, DMC audio, NTSC/PAL support, and five gameplay modes.
