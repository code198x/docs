# Phase 1 Curriculum: 68000 Assembly + VDP Fundamentals (Lessons 1-256)

> **⚠️ STRUCTURED:** This curriculum uses granular documentation files for better organisation and context efficiency.

## Primary Documentation

**Start here:** [`phase-1/overview.md`](phase-1/overview.md)

This provides the Phase 1 overview with philosophy, structure, and learning outcomes for Genesis assembly development, emphasizing speed and arcade-quality gaming.

## Detailed Documentation

| What you need | Where to find it |
|---------------|------------------|
| **Tier 1 details** (Speed Runner, L1-32) | [`phase-1/tier-1/README.md`](phase-1/tier-1/README.md) |
| **Tier 2 details** (DMA Dash, L33-64) | [`phase-1/tier-2/README.md`](phase-1/tier-2/README.md) |
| **Tier 3 details** (Sprite Swarm, L65-96) | [`phase-1/tier-3/README.md`](phase-1/tier-3/README.md) |
| **Tier 4 details** (FM Soundscape, L97-128) | [`phase-1/tier-4/README.md`](phase-1/tier-4/README.md) |
| **Tier 5 details** (Button Brawler, L129-160) | [`phase-1/tier-5/README.md`](phase-1/tier-5/README.md) |
| **Tier 6 details** (Dual Plane Racer, L161-192) | [`phase-1/tier-6/README.md`](phase-1/tier-6/README.md) |
| **Tier 7 details** (Window Tactics, L193-224) | [`phase-1/tier-7/README.md`](phase-1/tier-7/README.md) |
| **Tier 8 details** (Scanline Shifter, L225-256) | [`phase-1/tier-8/README.md`](phase-1/tier-8/README.md) |
| **Individual lesson specs** | [`phase-1/tier-{1-8}/lesson-NNN.md`](phase-1/) |

## Why This Structure?

**Organised by tier and lesson**

**Benefits:**
- **60-70% less context** when working on specific lessons
- **Better organisation** with clear hierarchy (phase → tier → lesson)
- **Easier navigation** to find specific game or concept
- **Scalable** for future expansion

## Genesis-Specific Features

This curriculum showcases the Sega Genesis's powerhouse capabilities:

- **Motorola 68000 @ 7.67MHz** - 16-bit CPU, significantly more powerful than 6502/Z80
- **"Blast Processing"** - Marketing term, but Genesis IS fast with proper coding
- **VDP (Video Display Processor)** - Hardware sprites, tiles, scrolling, DMA
- **80 sprites, 20 per scanline** - More simultaneous sprites than NES or Game Boy
- **DMA transfers** - Hardware memory copying for blazing speed
- **Dual-plane scrolling** - Two independent scrolling backgrounds
- **FM synthesis (YM2612)** - Arcade-quality sound with 6 FM channels
- **Z80 sound CPU** - Dedicated processor for audio
- **6-button controller** - Complex fighting game inputs

## Curriculum Structure

### Phase 1: 68000 Assembly + VDP Fundamentals (256 lessons, 8 games)

**Total:** 256 lessons across 8 tiers
**Outcome:** 8 complete original games showcasing Genesis capabilities

### Tier Breakdown

**Tier 1 (L1-32):** Speed Runner - Lightning-fast action
- 68000 fundamentals (registers, addressing modes, basic instructions)
- Genesis ROM header and initialization
- VDP basics (registers, command port, data port)
- Tile loading to VRAM
- Sprite basics (running character)
- 3-button controller input (Run button!)
- Auto-scrolling at high speed
- **Playable:** Lesson 3 (run and jump at Genesis speed)
- **Complete:** Lesson 7 (obstacles, speed progression, 60fps smooth)
- **Pattern focus:** 68000 basics, VDP fundamentals, 60fps optimization
- **Genesis showcase:** 68000 power enabling smooth high-speed gameplay

**Tier 2 (L33-64):** DMA Dash - Instant updates
- VDP DMA transfers for blazing speed
- Collect items that disappear INSTANTLY (DMA clear)
- Background changes INSTANTLY via DMA
- Show DMA vs CPU speed difference
- PSG sound effects for DMA events
- **Playable:** Lesson 35 (collect items with instant DMA effects)
- **Complete:** Lesson 39 (full DMA mastery, visual effects)
- **Pattern focus:** DMA programming, ROM-to-VRAM, VRAM-to-VRAM
- **Genesis showcase:** "Blast Processing" DMA speed in action

**Tier 3 (L65-96):** Sprite Swarm - 80 sprites on screen
- Shooter with MASSIVE enemy counts (20-30 simultaneously)
- Player bullets, enemy bullets, explosions all on screen
- Showcase Genesis's 80-sprite capability
- Sprite attribute table management
- 60fps with all sprites moving
- **Playable:** Lesson 67 (shoot swarms of enemies, bullets everywhere)
- **Complete:** Lesson 71 (full 80-sprite usage, waves, smooth)
- **Pattern focus:** Sprite management, SAT updates, sprite limits
- **Genesis showcase:** 80 sprites - more than NES (64) or Game Boy (40)

**Tier 4 (L97-128):** FM Soundscape - Music-driven gameplay
- Simple shooter with FM synthesis soundtrack
- YM2612 FM programming for music
- Gameplay synced to music beats
- PCM drum samples
- Visual effects synchronized to music
- Simple Z80 sound driver
- **Playable:** Lesson 99 (shoot enemies with FM music playing)
- **Complete:** Lesson 103 (full FM soundtrack, music-synced effects)
- **Pattern focus:** YM2612 FM synthesis, Z80 communication, music sync
- **Genesis showcase:** Arcade-quality FM synthesis, 6-channel sound

**Tier 5 (L129-160):** Button Brawler - 6-button fighting
- Fighting game with 6-button controller inputs
- Complex move system (hadouken, shoryuken-style inputs)
- Input buffering for fighting game combos
- Frame-perfect move detection
- 6-button controller detection
- Arcade stick support
- **Playable:** Lesson 131 (perform special moves, 6-button works)
- **Complete:** Lesson 135 (full fighting system, combos, specials)
- **Pattern focus:** 6-button controller, input buffering, frame-perfect detection
- **Genesis showcase:** 6-button controller - fighting game inputs, arcade authenticity

**Tier 6 (L161-192):** Dual Plane Racer - Two scrolling layers
- Racing game with dual-plane parallax
- Plane A for track, Plane B for background
- Independent scroll speeds (parallax depth)
- Plane priority control
- Track + clouds/mountains scrolling independently
- **Playable:** Lesson 163 (dual planes scroll, parallax works)
- **Complete:** Lesson 167 (full racing game with parallax depth)
- **Pattern focus:** Dual-plane scrolling, Plane A/B management, parallax effects
- **Genesis showcase:** Dual-plane scrolling - two independent scrolling backgrounds

**Tier 7 (L193-224):** Window Tactics - Split-screen effects
- Strategy game with window plane HUD overlay
- Window plane for status bar (no sprite 0 hack!)
- Split-screen multiplayer
- Window plane positioning and scrolling
- Clean HUD without affecting gameplay area
- **Playable:** Lesson 195 (window plane splits screen, HUD works)
- **Complete:** Lesson 199 (full strategy game with window HUD)
- **Pattern focus:** Window plane, split-screen effects, HUD overlay
- **Genesis showcase:** Window plane - hardware split-screen, clean HUD overlay

**Tier 8 (L225-256):** Scanline Shifter - Per-line scrolling
- Pseudo-3D racing with per-line horizontal scrolling
- HBlank interrupt for scanline effects
- Each scanline scrolls differently (road perspective)
- Raster effects and color palette changes
- Mode 7-style pseudo-3D effect
- **Playable:** Lesson 227 (per-line scroll works, pseudo-3D racing)
- **Complete:** Lesson 231 (full pseudo-3D racer, smooth effects)
- **Pattern focus:** Per-line scrolling, HBlank interrupts, pseudo-3D techniques
- **Genesis showcase:** Per-line scrolling - hardware scanline manipulation, pseudo-3D effects

## Original Games for Phase 1

All games are 100% original concepts designed to showcase Genesis capabilities.

### 1. Speed Runner (Tier 1, L1-32)
**Genre:** High-speed auto-scroller
**Description:** Run at blazing speed, jump obstacles, feel the 68000 power! Smooth 60fps action.
**Technical focus:** 68000 basics, VDP fundamentals, 60fps optimization, smooth scrolling
**Genesis showcase:** 68000 CPU power enabling high-speed gameplay impossible on 8-bit systems
**Playable:** Lesson 3 | **Complete:** Lesson 7

### 2. DMA Dash (Tier 2, L33-64)
**Genre:** Collect-em-up with instant effects
**Description:** Items vanish INSTANTLY with DMA! Background changes INSTANTLY! See "Blast Processing" in action!
**Technical focus:** DMA transfers (ROM-to-VRAM, VRAM-to-VRAM, VRAM fill), speed comparison
**Genesis showcase:** DMA "Blast Processing" - instant graphics updates at hardware speed
**Playable:** Lesson 35 | **Complete:** Lesson 39

### 3. Sprite Swarm (Tier 3, L65-96)
**Genre:** Bullet-hell shooter
**Description:** 20-30 enemies on screen SIMULTANEOUSLY! Bullets everywhere! Shows Genesis's 80-sprite power!
**Technical focus:** 80-sprite management, SAT updates, 20-per-scanline limit, 60fps with many sprites
**Genesis showcase:** 80 sprites - more than NES (64) or Game Boy (40), arcade-style sprite capacity
**Playable:** Lesson 67 | **Complete:** Lesson 71

### 4. FM Soundscape (Tier 4, L97-128)
**Genre:** Music-driven shooter
**Description:** Arcade-quality FM soundtrack drives gameplay! Shoot in sync with beats! PCM drums!
**Technical focus:** YM2612 FM synthesis, Z80 sound driver, music synchronization, PCM samples
**Genesis showcase:** 6-channel FM synthesis, arcade-quality sound, music-gameplay integration
**Playable:** Lesson 99 | **Complete:** Lesson 103

### 5. Button Brawler (Tier 5, L129-160)
**Genre:** Fighting game with 6-button inputs
**Description:** Street Fighter-style fighting with 6-button controller! Hadouken, shoryuken-style inputs! Frame-perfect move detection and combos!
**Technical focus:** 6-button controller programming, input buffering, frame-perfect detection, combo system, special move inputs
**Genesis showcase:** 6-button controller - fighting game inputs, arcade stick support, authentic arcade fighting experience
**Playable:** Lesson 131 | **Complete:** Lesson 135

### 6. Dual Plane Racer (Tier 6, L161-192)
**Genre:** Racing game with parallax depth
**Description:** Racing with dual-plane parallax! Track on Plane A, mountains on Plane B scrolling independently. Feel the depth!
**Technical focus:** Dual-plane scrolling (Plane A, Plane B), independent scroll speeds, parallax effects, plane priority control
**Genesis showcase:** Dual-plane scrolling - two independent scrolling backgrounds for parallax depth
**Playable:** Lesson 163 | **Complete:** Lesson 167

### 7. Window Tactics (Tier 7, L193-224)
**Genre:** Strategy game with HUD overlay
**Description:** Strategy game with window plane HUD overlay - no sprite 0 hack needed! Clean split-screen without tricks. Hardware window plane!
**Technical focus:** Window plane programming, split-screen effects, HUD overlay, window positioning and scrolling
**Genesis showcase:** Window plane - hardware split-screen for clean HUD overlay without sprite hacks
**Playable:** Lesson 195 | **Complete:** Lesson 199

### 8. Scanline Shifter (Tier 8, L225-256)
**Genre:** Pseudo-3D racer with per-line scrolling
**Description:** Pseudo-3D racing using per-line horizontal scrolling! HBlank interrupts shift each scanline differently for Mode 7-style effect!
**Technical focus:** Per-line scrolling, HBlank interrupts, scanline manipulation, raster effects, pseudo-3D techniques
**Genesis showcase:** Per-line scrolling - hardware scanline manipulation for pseudo-3D road perspective
**Playable:** Lesson 227 | **Complete:** Lesson 231

## What Students Master

### Motorola 68000 Essentials
- Register set (D0-D7 data, A0-A7 address, PC, SR)
- Addressing modes (all 14 modes)
- Instruction set essentials (not comprehensive - see Amiga for that)
- 16-bit and 32-bit operations
- Efficient code patterns
- Stack frame usage

### Genesis Hardware
- **VDP (Video Display Processor):**
  - Control and data ports
  - Register configuration
  - VRAM layout and management
  - Tile format (4bpp, 8×8)
  - Sprite attribute table (SAT)
  - Dual-plane scrolling (Plane A, Plane B)
  - Window plane
  - Color palettes (4 palettes × 16 colors)
  - DMA operations (VRAM fill, copy, transfer)

- **Memory Map:**
  - ROM (cartridge space)
  - Work RAM (64KB)
  - VRAM (64KB)
  - Z80 RAM (8KB)
  - I/O registers

- **Controllers:**
  - 3-button controller reading
  - 6-button controller detection and reading
  - Input buffering for fighting games

- **Sound:**
  - YM2612 FM synthesis basics
  - PSG chip (legacy SMS sound)
  - Z80 sound driver basics
  - PCM sample playback

### VDP Mastery
- Sprite management (80 sprites, 20 per scanline)
- Tile loading and management
- Scrolling (horizontal, vertical, per-line)
- DMA transfers for speed
- VBlank and HBlank interrupts
- Raster effects
- Color palette manipulation

### DMA Programming
- VRAM to VRAM copy
- ROM to VRAM transfer
- VRAM fill
- Optimizing for "blast processing" speed
- Cycle-accurate DMA timing

### Advanced Techniques
- Sprite multiplexing strategies
- 60fps optimization
- Physics at high speed
- Pseudo-3D rendering
- Input buffering for fighting games
- Frame-perfect timing
- FM synthesis programming

## "Blast Processing" Explained

Sega's marketing term had basis in reality:

**DMA Advantage:**
- Genesis DMA can transfer data faster than CPU can write
- Allows CPU to work on game logic while DMA handles graphics
- Properly used, creates perception of speed

**Speed Techniques:**
- DMA for all bulk transfers
- VBlank-efficient code
- 68000's 16-bit power vs 8-bit competition
- Hardware scrolling at no CPU cost
- Sprite system handles 80 sprites automatically

Students learn to maximize Genesis speed capabilities.

## Transfer Knowledge

### From Amiga:
- 68000 instruction set (100% compatible)
- Similar memory management concepts
- Different custom chips (Amiga: Copper/Blitter, Genesis: VDP/DMA)
- Console constraints vs computer freedom

### From NES/Game Boy:
- Tile-based graphics concepts transfer
- Sprite management concepts transfer
- 68000 is MUCH more powerful than 6502/SM83
- More sprites, more colors, faster processing

### To Other Sega Platforms:
- Master System: 8-bit predecessor, Z80 CPU
- Game Gear: Portable Master System
- Mega CD: Genesis + CD-ROM
- 32X: Genesis + 32-bit processors

## Comparison with SNES and Other 16-bit Consoles

| Feature | Genesis | SNES | TurboGrafx-16 |
|---------|---------|------|---------------|
| **CPU** | 68000 @ 7.67MHz | 65C816 @ 3.58MHz | HuC6280 @ 7.16MHz |
| **Colors** | 512 on-screen (61 total palette) | 32,768 on-screen (256) | 482 on-screen |
| **Sprites** | 80 (20/line) | 128 (32/line) | 64 (16/line) |
| **Sound** | YM2612 FM + PSG | SPC700 sample | HuC6280 waveform |
| **Speed feel** | Fast, responsive | Mode 7, effects | Good balance |
| **Focus** | Arcade ports, speed | Nintendo polish | CD-ROM innovation |

Genesis excels at: fast action games, arcade ports, sports games, fighting games.

## Navigation

- **View all phases:** [`./`](./)
- **68000 references:** See Amiga curriculum for comprehensive 68000 docs
- **Hardware references:** Coming soon (VDP, YM2612, memory map)
- **Documentation index:** [`../START-HERE.md`](../START-HERE.md)

---

**Last updated:** 2025-11-04
**Version:** 1.0
**Status:** Overview complete, tier details and individual lessons to be created
