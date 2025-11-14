# Sega Genesis/Mega Drive Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** Genesis base → Dual-CPU mastery Phase 3 → Sega CD/32X → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Direct assembly (no BASIC - console platform)
**Historical Note:** SNES competitor (1988-1997), 30.75M units sold, "Blast Processing!"
**Unique Feature:** **Dual-CPU architecture** (68000 + Z80, like Commodore 128!)

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare single-CPU vs dual-CPU implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Dual-CPU coordination is dual-CPU coordination" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games (though students learn their techniques)
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master Genesis base (68000, VDP, basic sound)
- Phase 3: **Dual-CPU mastery** - 68000+Z80 coordination, YM2612 FM synthesis
- Phase 4-6: Advanced techniques, pushing Genesis limits
- Phase 7: **Sega CD/32X** - enhanced hardware, maximum capabilities
- Phase 8: Modern Genesis development (homebrew scene)

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Sega Genesis base (68000 @ 7.6MHz, Z80 @ 3.58MHz)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 68000 instruction set fundamentals (16-bit CPU)
- **64KB main RAM** (vs 8-bit consoles' smaller RAM)
- **64KB VRAM** (video memory)
- **VDP** (Video Display Processor):
  - 320×224 resolution (40×28 tiles)
  - **80 sprites** (more than SMS's 32)
  - 64 colors on-screen (from palette of 512)
  - Tile-based graphics (8×8 tiles)
  - Hardware scrolling (smooth, multi-layer)
  - Plane A, Plane B, Window (3 layers)
- **Z80 sound CPU @ 3.58MHz** (secondary processor - like C128!)
- **YM2612 FM synthesis** (6-channel, arcade-quality - but complex!)
- **SN76489 PSG** (3-channel + noise, SMS backward compatibility)
- **8KB sound RAM** (Z80's RAM)
- Joystick/controller input (3 buttons + D-pad, 2 ports)
- **No operating system** (direct hardware programming)
- 60Hz NTSC / 50Hz PAL

**No Autoload - Direct Boot:**
Cartridge inserted = game runs immediately. No loader required.

**Deliverables:** 16 complete, playable Genesis games

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Genesis base (68000, basic Z80 usage)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 68000 code (7.6MHz efficiency)
- Advanced VDP programming (tiles, sprites, scrolling)
- **80 sprites optimization** (smooth movement)
- Sprite multiplexing (more than 80 visible)
- Advanced scrolling (plane A, B, window)
- **Basic Z80 usage** (sound playback, simple coordination)
- PSG audio programming (3-channel + noise)
- Advanced collision detection (software-based)
- Multi-screen game structures
- **64KB main RAM + 64KB VRAM management**

**Deliverables:** 16 games with commercial-quality Genesis features

---

### Phase 3: Dual-CPU Mastery (68000+Z80 Coordination)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** Genesis dual-CPU mastery, YM2612 FM synthesis
**Complexity:** Direct single-CPU→dual-CPU comparison, professional coordination
**Games:** 5 revisited from Phases 1-2 with dual-CPU, 3 new showcasing mastery

**Key Learning:**
- **Dual-CPU coordination** (68000 + Z80, like Commodore 128!)
- **68000** (main CPU, graphics, game logic) + **Z80** (sound CPU, music playback)
- **YM2612 FM synthesis** (6-channel, complex but powerful!)
- **Direct comparison:** "Here's your basic Genesis game. Now add Z80 sound coordination"
- Z80 sound driver development (music sequencing, sound effects)
- 68000↔Z80 communication (bus arbitration, shared RAM)
- Advanced VDP techniques (all capabilities)
- **FM synthesis programming** (YM2612 all channels)
- Professional dual-CPU architecture
- Comparing to single-CPU approach (when to use each)

**Deliverables:** 8 games - 5 dual-CPU versions, 3 new showcasing dual-CPU mastery

**Games Revisited with Dual-CPU:**
1. Snake III (Dual-CPU) - Z80 music sequencing, 68000 game logic
2. Shooter III (Dual-CPU) - Z80 audio driver, 68000 rendering
3. Platformer III (Dual-CPU) - Z80 sound, 68000 physics
4. Breakout III (Dual-CPU) - Z80 FM music, 68000 game logic
5. One other from Phase 1-2

**New Dual-CPU Games:**
6. Action RPG I (showcasing dual-CPU architecture, FM music)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Genesis dual-CPU (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced 68000 optimization (7.6MHz maximum efficiency)
- Advanced Z80 sound drivers (complex music, effects)
- Maximum VDP utilization (80 sprites + multiplexing)
- Advanced YM2612 programming (all FM channels, advanced techniques)
- Complex scrolling (parallax, smooth, multi-layer)
- DMA (Direct Memory Access - fast VRAM transfers)
- Advanced collision detection
- Isometric projection
- Turn-based strategy mechanics

**Deliverables:** 8 games showcasing advanced Genesis dual-CPU techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Genesis dual-CPU mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture (dual-CPU)
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced YM2612 music composition (FM mastery)
- Large game worlds (cartridge banking if needed)
- Multi-cartridge games (rare but possible)

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Genesis (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 80+ simultaneous sprites (multiplexing mastery)
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 68000 optimization
- Extreme Z80 sound driver optimization
- Pushing Genesis limits ("Blast Processing!")
- Professional Genesis development

**Deliverables:** 4 games pushing absolute limits of Genesis

---

### Phase 7: Enhanced Hardware (Sega CD/32X)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Sega CD (68000 @ 12.5MHz, CD-ROM) / 32X (dual SH-2)
**Complexity:** Large-scale games with enhanced hardware
**Games:** 2 epic games (large RPG with CD audio, grand strategy/adventure)

**Key Learning:**
- **Sega CD** (1991, CD-ROM add-on):
  - 68000 @ 12.5MHz (additional CPU!)
  - CD-ROM (700MB storage vs 4MB cartridge)
  - CD-DA audio (CD music, Red Book audio)
  - Scaling/rotation (hardware support)
  - FMV (full-motion video)
- **32X** (1994, 32-bit add-on):
  - Dual SH-2 @ 23MHz (32-bit CPUs!)
  - 256KB RAM
  - Enhanced graphics (32,768 colors)
- Advanced techniques (maximum Genesis capabilities)
- Commercial enhanced Genesis development

**Deliverables:** 2 commercial-scale enhanced Genesis games

---

### Phase 8: Pinnacle (Modern Homebrew)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern Genesis development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern Genesis development workflow
- Emulator debugging (BlastEm, Gens, Fusion)
- Modern homebrew techniques
- SGDK (Sega Genesis Development Kit - modern toolchain)
- Cross-development (modern assemblers: ASMX, SGDK)
- Commercial release preparation (homebrew market)
- Portfolio capstone quality
- **Historical significance:** SNES competitor, 30.75M units sold, "Blast Processing!"
- **Active homebrew scene** (still very active)

**Deliverables:** 2 portfolio-ready commercial-quality Genesis games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 68000 Programming**
- P1: Basic instructions (16-bit CPU)
- P2: Advanced 68000 techniques
- P3: **Dual-CPU coordination** (68000 + Z80)
- P4: Complex 68000 techniques
- P5+: Extreme optimization

**2. Dual-CPU Architecture**
- P3: **68000 + Z80 coordination** (like Commodore 128!)
- P4: Advanced dual-CPU techniques
- P5: Complex dual-CPU systems
- P6: Maximum dual-CPU efficiency

**3. VDP Programming**
- P1: VDP basics (tiles, sprites, scrolling)
- P2: Advanced VDP techniques
- P3: Maximum VDP capabilities
- P4: DMA mastery (fast transfers)
- P5+: Professional VDP programming

**4. Sprite Management**
- P1: **80 hardware sprites**
- P2: Sprite optimization (positioning, priority)
- P3: Advanced sprites (80+ via multiplexing)
- P4: Maximum sprite utilization
- P5+: Complex sprite systems (100+ sprites)

**5. Scrolling Systems**
- P1: **Hardware scrolling** (plane A, B, window)
- P2: Multi-layer scrolling (planes)
- P3: **Advanced scrolling** (parallax, smooth)
- P4: Complex scrolling effects
- P5+: Maximum scrolling techniques

**6. Sound Programming**
- P1: PSG basics (3-channel + noise, SMS compatible)
- P2: Basic Z80 sound coordination
- P3: **YM2612 FM synthesis** (6-channel, dual-CPU!)
- P4: Advanced FM synthesis (all channels)
- P5+: Professional audio (FM mastery)

**7. Z80 Sound Drivers**
- P3: **Z80 sound driver development** (dual-CPU!)
- P4: Complex sound drivers (music, effects)
- P5: Advanced sound drivers (all features)
- P6: Professional sound drivers

**8. Memory Management**
- P1: 64KB main RAM + 64KB VRAM + 8KB sound RAM
- P2: Efficient data structures
- P3: Dual-CPU memory management (shared RAM)
- P5+: Maximum memory efficiency

---

## Hardware Progression

### Sega Genesis/Mega Drive Base (Phases 1-2)
**Platform:** Sega Genesis / Mega Drive (1988)
**Characteristics:**
- **68000 CPU @ 7.6MHz** (main CPU, 16-bit)
- **Z80 CPU @ 3.58MHz** (sound CPU, 8-bit - dual-CPU!)
- **64KB main RAM** (68000's RAM)
- **8KB sound RAM** (Z80's RAM)
- **64KB VRAM** (video memory)
- **VDP** (Video Display Processor):
  - 320×224 resolution (40×28 tiles, 8×8 each)
  - **80 hardware sprites** (more than SMS's 32)
  - 64 colors on-screen (from palette of 512)
  - Tile-based graphics (8×8 tiles)
  - **Hardware scrolling** (plane A, B, window - 3 layers)
  - DMA (Direct Memory Access - fast VRAM transfers)
- **YM2612 FM synthesis** (6-channel, arcade-quality!)
- **SN76489 PSG** (3-channel + noise, SMS compatible)
- Controller input (3 buttons + D-pad, extendable to 6 buttons)
- Cartridge-based (512KB-4MB typical, up to 8MB with banking)

**Focus:** Master 68000 and dual-CPU basics
- 68000 programming (16-bit, same as Amiga, ST, X68000)
- VDP tile system (like SMS but enhanced)
- 80 hardware sprites (smooth movement)
- Hardware scrolling (3 planes)
- **Dual-CPU architecture** (68000 + Z80, like C128!)
- PSG audio (SMS compatible)

**Historical Context:**
- SNES main competitor (1988-1997)
- 30.75 million units sold (vs SNES's 49M)
- **"Blast Processing!"** (marketing, but Genesis was fast)
- Sonic the Hedgehog (mascot, 1991)
- **Dual-CPU architecture** (68000 + Z80, advanced for consoles)
- YM2612 FM synthesis (arcade-quality sound, complex)
- **16-bit console war** (Genesis vs SNES)
- More successful in North America/Europe than Japan

**Genesis vs SNES:**
- Faster CPU (68000 @ 7.6MHz vs 65816 @ 3.58MHz, but different architectures)
- **Dual-CPU** (68000 + Z80 vs single 65816 + coprocessors)
- Simpler scrolling (vs SNES's Mode 7, scaling/rotation)
- **FM synthesis** (vs SNES's sample-based audio - different strengths)
- Released earlier (1988 vs 1990)
- Different game libraries (Sonic vs Mario, etc.)

### Dual-CPU Mastery (Phase 3+)
**Introduced Phase 3**
**Enhanced Focus:**
- **Dual-CPU coordination** (68000 + Z80, like C128!)
- 68000: Main game logic, graphics, physics
- Z80: Sound driver, music sequencing, effects
- Bus arbitration (sharing access to sound hardware)
- **YM2612 FM synthesis** (6-channel, complex programming)
- Advanced VDP techniques (all capabilities)
- Professional dual-CPU architecture

**Focus:** Master dual-CPU coordination
- 68000↔Z80 communication
- Z80 sound driver development
- YM2612 FM synthesis (all channels)
- Optimizing dual-CPU workload
- Professional audio programming

**Why Dual-CPU Matters:**
- Z80 handles sound independently (68000 free for game logic)
- YM2612 FM synthesis (complex, benefits from dedicated CPU)
- Similar to Commodore 128 (8502 + Z80 coordination)
- Professional game architecture
- Classic Genesis games used this (Sonic, Streets of Rage, etc.)

### Enhanced Hardware (Phase 7)
**Sega CD (1991):**
- Additional 68000 @ 12.5MHz
- CD-ROM (700MB storage!)
- CD-DA audio (Red Book audio, CD music tracks)
- Scaling/rotation hardware
- FMV (full-motion video)

**32X (1994):**
- Dual SH-2 @ 23MHz (32-bit CPUs!)
- 256KB RAM
- 32,768 colors on-screen
- PWM audio (Pulse Width Modulation)
- Add-on for Genesis (pass-through)

### Modern Genesis (Phase 8)
**Modern enhancements:**
- BlastEm (cycle-accurate emulator)
- Gens, Fusion emulators
- SGDK (Sega Genesis Development Kit - modern, excellent!)
- Modern assemblers (ASMX, VASM)
- **Very active homebrew scene** (one of most active!)
- Everdrive (modern flash cart)

**Focus:** Modern workflow
- SGDK development (C + assembly hybrid)
- Homebrew development
- Modern tools
- Portfolio showcase

---

## Spiral Learning Example: Shooter

**Phase 1: Shooter I (Genesis base)** (16 lessons)
- Basic scrolling (68000 fundamentals, VDP scrolling)
- Tile-based backgrounds (8×8 tiles, planes)
- Player sprite (hardware sprite, 80 available)
- Enemy sprites (hardware sprites)
- PSG audio (3-channel, simple)

**Phase 2: Shooter II (Genesis optimized)** (32 lessons)
- Optimized 68000 code
- Smooth scrolling (plane A, B, parallax)
- More enemies (80 sprites)
- Basic Z80 sound coordination
- Multi-stage levels

**Phase 3: Shooter III (Dual-CPU + YM2612)** (64 lessons - DUAL-CPU MASTERY)
- **68000 + Z80 coordination** (dual-CPU, like C128!)
- **Z80 sound driver** (music sequencing, effects)
- **YM2612 FM synthesis** (6-channel arcade-quality music!)
- **Advanced VDP** (all capabilities)
- **Direct comparison:** "Here's your PSG game. Now add Z80+YM2612 dual-CPU audio"

**Phase 4: Shooter IV (Advanced dual-CPU)** (64 lessons)
- Complex Z80 sound driver (all features)
- Advanced YM2612 (all FM channels)
- DMA optimization (fast VRAM transfers)
- 80+ sprites (multiplexing)

**Phase 6: Shooter V (Genesis limits)** (128 lessons)
- Maximum sprites (100+ smooth)
- Extreme dual-CPU optimization
- Commercial-quality
- Pushing Genesis limits ("Blast Processing!")

Students see evolution: Genesis basics → Optimized → **Dual-CPU mastery** → Advanced → Professional

---

## Key Differences from Other Platforms

**Genesis vs SNES:**
- **Dual-CPU** (68000 + Z80) vs single 65816 + coprocessors
- 68000 @ 7.6MHz vs 65816 @ 3.58MHz (different architectures)
- **FM synthesis** (YM2612) vs sample-based (SNES APU)
- 64 colors on-screen vs 256 (SNES advantage)
- Earlier release (1988 vs 1990)
- Different strengths (speed vs effects)

**Genesis vs Master System:**
- 68000 vs Z80 (16-bit vs 8-bit)
- 80 sprites vs 32
- YM2612 FM vs PSG only
- **Dual-CPU** (68000 + Z80) vs single Z80
- 64KB RAM vs 8KB

**Genesis Advantages:**
- **Dual-CPU architecture** (68000 + Z80, advanced!)
- YM2612 FM synthesis (arcade-quality, 6-channel)
- Fast 68000 CPU (7.6MHz)
- 80 sprites (smooth games)
- Very active homebrew scene
- **Learning dual-CPU coordination** (like C128, transferable skill!)

**Learning Path:**
- Master System → Genesis (Sega evolution, see Z80 usage)
- Genesis → Saturn (Sega 32-bit evolution)
- 68000 skills transfer to Amiga, ST, X68000
- Dual-CPU skills transfer to other dual-CPU systems

**Same Pattern Library Concepts:**
- 68000 assembly (same as Amiga, ST, X68000)
- Dual-CPU coordination (like C128!)
- Collision detection algorithms
- AI pathfinding
- Physics systems
- Game design patterns
- All transferable skills

---

## Assessment Strategy

**No self-directed work** - every tier is fully specified:
- Complete lesson breakdown (4-64 arcs × 4 lessons)
- Full code examples provided
- Expected output defined (single-CPU and dual-CPU where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 68000 Genesis games from scratch
- Understands VDP (tiles, sprites, scrolling)
- Has 16 portfolio Genesis games

**Phase 3 Complete:**
- Student masters dual-CPU coordination (68000 + Z80)
- Can create Z80 sound drivers (YM2612 FM synthesis)
- Has both single-CPU and dual-CPU versions of key games
- **Dual-CPU architecture expertise** (like C128, transferable!)

**Phase 8 Complete:**
- Student has 60 portfolio games showcasing Genesis
- Masters 68000 architecture (transfers to Amiga, ST, X68000)
- Masters dual-CPU coordination (68000 + Z80)
- Masters YM2612 FM synthesis (6-channel)
- Can create commercial-release quality games
- Ready for professional Genesis homebrew development
- **68000 + dual-CPU expertise** transfers to other platforms

---

## Resources Required

**Development Tools:**
- Assembler: ASMX, VASM
- SGDK (Sega Genesis Development Kit - modern, excellent!)
- Emulator: BlastEm (cycle-accurate), Gens, Fusion
- Graphics: Tile/sprite editors (Genesis format)
- Audio: YM2612 trackers (DefleMask, etc.)
- Utilities: ROM builders

**Reference Materials:**
- 68000 instruction set
- Z80 instruction set (for sound driver)
- VDP Programming Guide (tiles, sprites, scrolling, DMA)
- YM2612 FM synthesis reference (complex!)
- Genesis Technical Reference
- Memory map (68000, Z80, shared areas)

**Testing:**
- Emulators (development - BlastEm recommended)
- Real Genesis hardware (verification)
- Everdrive (modern flash cart)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Dual-CPU mastery Phase 3
**Note:** No Phase 0 (console - no BASIC, direct assembly)
**Historical Note:** SNES competitor (1988-1997), 30.75M units sold, "Blast Processing!"
**Unique Feature:** **Dual-CPU architecture** (68000 + Z80, like Commodore 128!)
**Key Learning:** Dual-CPU coordination, YM2612 FM synthesis, professional game architecture
**68000 + Z80 Architecture:** Dual-CPU coordination skills transfer to other dual-CPU systems!
**Next Steps:** Create Genesis 8-PHASE-GAME-PROGRESSION.md with specific game mapping
