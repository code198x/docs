# TurboGrafx-16 / PC Engine Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** TurboGrafx-16 base → SuperGrafx + CD-ROM² Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Direct assembly (no BASIC - console platform)
**Historical Note:** First 16-bit console (Japan 1987), 10M units sold, "16-bit" marketing (8-bit data bus!)
**Unique Feature:** CD-ROM² (first console CD-ROM add-on), HuCard format (credit card sized)

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare base TurboGrafx vs SuperGrafx implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "VDP sprite management is VDP sprite management" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games (though students learn their techniques)
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master TurboGrafx-16 base (HuC6280, VDP, PSG)
- Phase 3: **SuperGrafx + CD-ROM² mastery** - enhanced hardware, CD-ROM games
- Phase 4-6: Advanced techniques, pushing TurboGrafx limits
- Phase 7: **Maximum TurboGrafx** - all capabilities, CD-ROM mastery
- Phase 8: Modern TurboGrafx development (homebrew scene)

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** TurboGrafx-16 / PC Engine base (HuC6280 @ 7.16MHz, 8KB RAM)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- HuC6280 instruction set fundamentals (6502-based with enhancements!)
- **8KB main RAM** (vs Genesis 64KB, SNES 128KB - limited!)
- **64KB VRAM** (video memory)
- **VDP** (Video Display Processor - HuC6270):
  - 256×224 or 512×224 resolution
  - **64 hardware sprites** (16×16, 16×32, 16×64, 32×16, 32×32, 32×64 - flexible!)
  - 482 colors on-screen (from palette of 512)
  - Tile-based graphics (8×8 tiles)
  - Hardware scrolling (smooth)
  - 2 background layers (BAT - Background Attribute Table)
- **6-channel PSG** (HuC6280 integrated - 5 waveform + 1 noise/DDA)
- **HuCard format** (credit card sized cartridges - compact!)
- Joystick/controller input (2 buttons + D-pad, expandable to 5 players)
- **No operating system** (direct hardware programming)
- 60Hz NTSC (Japan/North America) / 50Hz PAL (Europe, rare)

**No Autoload - Direct Boot:**
HuCard inserted = game runs immediately. No loader required.

**Deliverables:** 16 complete, playable TurboGrafx-16 games

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** TurboGrafx-16 base (HuC6280 @ 7.16MHz, 8KB RAM)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized HuC6280 code (6502-based optimization, 7.16MHz)
- Advanced VDP programming (sprites, backgrounds, scrolling)
- **64 sprites optimization** (flexible sizes)
- Sprite multiplexing (more than 64 visible)
- Advanced scrolling (smooth, multi-layer)
- **6-channel PSG** programming (waveform + DDA samples)
- Advanced collision detection (software-based)
- Multi-screen game structures
- **8KB RAM management** (creative usage - limited RAM!)
- **64KB VRAM** efficiency

**Deliverables:** 16 games with commercial-quality TurboGrafx-16 features

---

### Phase 3: SuperGrafx & CD-ROM² Mastery
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **SuperGrafx** (enhanced) + **CD-ROM²** (CD-ROM add-on)
**Complexity:** Direct base→SuperGrafx/CD-ROM² comparison, mastery
**Games:** 5 revisited from Phases 1-2 with SuperGrafx, 3 new showcasing CD-ROM²

**Key Learning:**
- **SuperGrafx** (1989, enhanced TurboGrafx):
  - Second VDP (HuC6270 × 2 - dual video chips!)
  - Second VCE (HuC6260 × 2 - dual video encoders!)
  - **4 background layers** (vs base's 2 - doubled!)
  - **128 sprites** (vs base's 64 - doubled!)
  - Better parallax scrolling (4 layers)
  - Rare (5 games released!) but interesting hardware
- **CD-ROM²** (1988, first console CD-ROM add-on!):
  - CD-ROM drive (540MB storage vs HuCard's 2.5MB max!)
  - **CD-DA audio** (Red Book audio - CD music tracks!)
  - ADPCM audio (CD-quality voice/samples)
  - 64KB additional RAM (Super System Card)
  - 192KB additional RAM (Arcade Card - later)
  - FMV (full-motion video - limited)
  - Large game worlds (CD storage)
- **Direct comparison:** "Here's your HuCard game. Now expand it with CD-ROM²"
- Advanced VDP techniques (all capabilities)
- Professional TurboGrafx development

**Deliverables:** 8 games - 5 SuperGrafx versions, 3 new showcasing CD-ROM²

**Games Revisited with SuperGrafx:**
1. Snake III (SuperGrafx) - 4 backgrounds, 128 sprites
2. Shooter III (SuperGrafx) - parallax scrolling (4 layers)
3. Platformer III (SuperGrafx) - better graphics, more sprites
4. Breakout III (SuperGrafx) - enhanced effects
5. One other from Phase 1-2

**New CD-ROM² Games:**
6. Action RPG I (CD-ROM² - CD-DA music, large world, voice)
7. Adventure I (CD-ROM² - FMV, voice acting, CD audio)
8. Shooter I (CD-ROM² - CD audio, large stages)

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** TurboGrafx-16/SuperGrafx (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced HuC6280 optimization (7.16MHz maximum efficiency, 6502-based)
- Maximum VDP utilization (64-128 sprites, SuperGrafx 4 layers)
- Advanced scrolling (parallax, smooth)
- Advanced PSG programming (6-channel mastery, DDA samples)
- CD-ROM² optimization (streaming, CD-DA + ADPCM)
- Advanced collision detection
- Isometric projection
- Turn-based strategy mechanics
- **8KB RAM creative usage** (base TurboGrafx constraint)

**Deliverables:** 8 games showcasing advanced TurboGrafx techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** TurboGrafx/SuperGrafx mastery, CD-ROM² mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large CD-ROM² RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture (CD-ROM² storage)
- Quest systems and narrative (CD-ROM² voice, FMV)
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- CD-DA audio mastery (CD music tracks)
- ADPCM voice/samples (CD-quality audio)
- Large game worlds (CD-ROM² multi-disc if needed)
- FMV integration (full-motion video)

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** TurboGrafx/SuperGrafx (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 64-128 simultaneous sprites (multiplexing mastery)
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme HuC6280 optimization (6502-based)
- Pushing TurboGrafx limits
- Professional TurboGrafx development
- CD-ROM² maximum capabilities (streaming, audio, FMV)

**Deliverables:** 4 games pushing absolute limits of TurboGrafx

---

### Phase 7: Maximum TurboGrafx & CD-ROM²
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** TurboGrafx (all capabilities) + CD-ROM² mastery
**Complexity:** Large-scale games with maximum features
**Games:** 2 epic games (large CD-ROM² RPG, grand strategy/adventure)

**Key Learning:**
- All VDP capabilities (SuperGrafx 4 layers, 128 sprites)
- All PSG capabilities (6-channel mastery)
- CD-ROM² maximum (CD-DA, ADPCM, streaming, FMV)
- Large game worlds (CD-ROM² multi-disc)
- Advanced graphics techniques
- Commercial TurboGrafx development
- Professional quality polish

**Deliverables:** 2 commercial-scale TurboGrafx games (CD-ROM² mastery)

---

### Phase 8: Pinnacle (Modern Homebrew)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern TurboGrafx development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (CD-ROM² shooter, SuperGrafx platformer)

**Key Learning:**
- Modern TurboGrafx development workflow
- Emulator debugging (Mednafen, Magic Engine, Ootake)
- Modern homebrew techniques
- Modern assemblers (WLA-DX, HuC - C compiler for TurboGrafx!)
- Cross-development (modern tools)
- Commercial release preparation (homebrew market)
- Portfolio capstone quality
- **Historical significance:** First 16-bit console (Japan 1987), first CD-ROM add-on
- **Active homebrew scene** (still active)

**Deliverables:** 2 portfolio-ready commercial-quality TurboGrafx games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. HuC6280 Programming**
- P1: Basic instructions (6502-based with enhancements)
- P2: Advanced HuC6280 techniques (6502 optimization)
- P3: SuperGrafx/CD-ROM² optimization
- P4: Complex HuC6280 techniques
- P5+: Extreme optimization

**2. VDP Programming**
- P1: VDP basics (tiles, sprites, 2 backgrounds)
- P2: Advanced VDP techniques
- P3: **SuperGrafx VDP** (dual chips, 4 backgrounds, 128 sprites)
- P4: All VDP capabilities
- P5+: Professional VDP programming

**3. Sprite Management**
- P1: **64 hardware sprites** (flexible sizes)
- P2: Sprite optimization (positioning, sizes)
- P3: **SuperGrafx 128 sprites** (vs base 64)
- P4: Maximum sprite utilization
- P5+: Complex sprite systems

**4. Scrolling Systems**
- P1: **Hardware scrolling** (2 backgrounds)
- P2: Multi-layer scrolling
- P3: **SuperGrafx 4-layer scrolling** (parallax)
- P4: Complex scrolling effects
- P5+: Maximum scrolling techniques

**5. Sound Programming**
- P1: PSG basics (6-channel - 5 waveform + 1 noise/DDA)
- P2: PSG music composition
- P3: **CD-ROM² audio** (CD-DA + ADPCM)
- P4: Professional audio (PSG + CD mastery)
- P5+: Maximum audio capabilities

**6. CD-ROM² Development**
- P3: **CD-ROM² introduction** (CD-DA, ADPCM, storage)
- P4: CD-ROM² optimization (streaming, loading)
- P5: Large CD-ROM² games (multi-disc)
- P6: FMV integration (full-motion video)
- P7: CD-ROM² maximum capabilities

**7. Memory Management**
- P1: **8KB main RAM** (vs Genesis 64KB, SNES 128KB - limited!)
- P2: Efficient data structures (creative RAM usage)
- P3: CD-ROM² additional RAM (64KB-192KB Arcade Card)
- P5+: Maximum memory efficiency

**8. Collision Detection**
- P1: Software collision (no hardware collision)
- P2: Bounding box optimization
- P3: Optimized collision
- P5+: Complex collision systems

---

## Hardware Progression

### TurboGrafx-16 / PC Engine Base (Phases 1-2)
**Platform:** TurboGrafx-16 (US) / PC Engine (Japan) (1987)
**Characteristics:**
- **HuC6280 CPU @ 7.16MHz** (6502-based with enhancements!)
  - 6502 core with added instructions
  - Built-in timer
  - Built-in I/O ports
  - Built-in PSG (6-channel audio)
  - 8-bit data bus, 21-bit address bus
- **8KB main RAM** (vs Genesis 64KB, SNES 128KB - limited!)
- **64KB VRAM** (video memory - VDC, Video Display Controller)
- **VDP** (HuC6270 Video Display Processor):
  - 256×224 or 512×224 resolution
  - **64 hardware sprites** (sizes: 16×16, 16×32, 16×64, 32×16, 32×32, 32×64 - flexible!)
  - **482 colors on-screen** (from palette of 512)
  - Tile-based graphics (8×8 tiles)
  - **2 background layers** (BAT - Background Attribute Table)
  - Hardware scrolling (smooth, per-pixel)
  - Sprite priority system
- **VCE** (HuC6260 Video Color Encoder):
  - Color palette control
  - 512 color palette (9-bit color - 3 bits each R/G/B)
- **6-channel PSG** (HuC6280 integrated):
  - 5 waveform channels (32-sample waveforms)
  - 1 noise channel / DDA channel (sample playback!)
  - Integrated into CPU (unusual!)
- **HuCard format** (credit card sized cartridges, 2.5MB max)
- Controller input (2 buttons + D-pad, TurboTap for 5 players)

**Focus:** Master HuC6280 and VDP
- HuC6280 programming (6502-based, enhanced)
- VDP tile system (2 backgrounds, 64 sprites)
- 64 hardware sprites (flexible sizes)
- Hardware scrolling (smooth)
- 6-channel PSG (waveform + DDA)
- **8KB RAM creative usage** (major constraint!)

**Historical Context:**
- **First "16-bit" console** (Japan 1987, US 1989)
  - "16-bit" marketing (16-bit graphics chip, 8-bit data bus!)
  - Actually hybrid 8/16-bit architecture
- 10 million units sold (mostly Japan)
- **HuCard format** (credit card sized - compact!)
- **CD-ROM² add-on** (1988 - first console CD-ROM!)
- Strong in Japan, weak in US (marketing issues)
- Many excellent shooters (shmups) - genre strength
- Released before Genesis (1987 vs 1988) and SNES (1990)

**TurboGrafx vs Genesis/SNES:**
- **Less RAM:** 8KB (vs Genesis 64KB, SNES 128KB - major constraint!)
- **More colors:** 482 on-screen (vs Genesis 64, less than SNES 256)
- **Fewer sprites:** 64 (vs Genesis 80, SNES 128)
- **6502-based CPU:** HuC6280 @ 7.16MHz (vs Genesis 68000 @ 7.6MHz, SNES 65816 @ 3.58MHz)
- **Earlier release:** 1987 (vs Genesis 1988, SNES 1990)
- **First CD-ROM:** CD-ROM² 1988 (vs Sega CD 1991)
- **Smaller in US:** 2.5M US vs 10M worldwide (Japan-focused)

**TurboGrafx Advantages:**
- More colors (482 on-screen)
- Flexible sprite sizes (16×16 to 32×64)
- **First CD-ROM** (CD-ROM² 1988)
- Earlier release (1987)
- HuCard format (compact, fast loading)
- Excellent shooters (shmup strength)

**TurboGrafx Constraints:**
- **Only 8KB main RAM** (major limitation vs Genesis/SNES!)
- Only 2 background layers (vs SNES's 4)
- Fewer sprites than SNES (64 vs 128)
- Weaker US marketing (vs Nintendo/Sega)

### SuperGrafx (Phase 3+)
**Platform:** SuperGrafx (1989, Japan only)
**Introduced Phase 3**
**Enhanced Features:**
- **Dual VDP** (HuC6270 × 2 - two video chips!)
- **Dual VCE** (HuC6260 × 2 - two video encoders!)
- **4 background layers** (vs base's 2 - doubled!)
- **128 sprites** (vs base's 64 - doubled!)
- Better parallax scrolling (4 independent layers)
- Same HuC6280 CPU (7.16MHz)
- Same 8KB main RAM (still limited!)
- **Rare:** Only 5 games released (commercial failure)
- Backward compatible with TurboGrafx-16/PC Engine

**Focus:** SuperGrafx mastery
- Dual VDP programming (4 backgrounds)
- 128 sprites (doubled)
- 4-layer parallax scrolling
- Professional multi-layer effects

**Why SuperGrafx Matters:**
- Enhanced TurboGrafx (4 backgrounds, 128 sprites)
- Shows hardware potential
- Rare (5 games) but interesting
- Learning value (multi-chip coordination)

### CD-ROM² (Phase 3+)
**Platform:** CD-ROM² System (1988, Japan) / TurboGrafx-CD (1989, US)
**Introduced Phase 3**
**Enhanced Features:**
- **CD-ROM drive** (540MB storage vs HuCard 2.5MB max!)
- **CD-DA audio** (Red Book audio - CD music tracks, high quality!)
- **ADPCM audio** (CD-quality voice/samples)
- **Additional RAM:**
  - Base System Card: 64KB (2.0/3.0)
  - **Arcade Card:** 192KB additional RAM (total 200KB!)
- **First console CD-ROM** (1988 - before Sega CD 1991!)
- Large game worlds (CD storage)
- FMV (full-motion video - limited but present)
- Voice acting (ADPCM)

**Focus:** CD-ROM² mastery
- CD-ROM programming (streaming, loading)
- CD-DA audio (Red Book audio tracks)
- ADPCM audio (voice, samples)
- Large game worlds (CD storage)
- FMV integration (full-motion video)

**Why CD-ROM² Matters:**
- **First console CD-ROM** (1988 - pioneering!)
- CD-DA audio (CD-quality music)
- Large storage (540MB vs 2.5MB HuCard)
- Voice acting (ADPCM)
- Many classic CD-ROM² games (Ys I-IV, Rondo of Blood, etc.)
- Historical significance (console CD-ROM pioneer)

### Modern TurboGrafx (Phase 8)
**Modern enhancements:**
- Mednafen (cycle-accurate emulator)
- Magic Engine, Ootake emulators
- HuC (C compiler for TurboGrafx!)
- Modern assemblers (WLA-DX)
- **Active homebrew scene** (still active)
- TurboEverdrive (modern flash cart)

**Focus:** Modern workflow
- Modern emulators with debugging
- HuC C development (or assembly)
- Homebrew development
- Portfolio showcase

---

## Spiral Learning Example: Shooter

**Phase 1: Shooter I (TurboGrafx base)** (16 lessons)
- Basic scrolling (HuC6280 fundamentals, 6502-based)
- Tile-based backgrounds (2 layers)
- Player sprite (hardware sprite, flexible size)
- Enemy sprites (64 sprites available)
- 6-channel PSG audio (music + effects)

**Phase 2: Shooter II (TurboGrafx optimized)** (32 lessons)
- Optimized HuC6280 code (6502-based optimization)
- Smooth scrolling (2 layers, parallax)
- More enemies (64 sprites)
- PSG music (6-channel composition)
- Multi-stage levels

**Phase 3: Shooter III (SuperGrafx + CD-ROM²)** (64 lessons - ENHANCED HARDWARE)
- **SuperGrafx:** 4 backgrounds (vs 2), 128 sprites (vs 64), 4-layer parallax!
- **CD-ROM²:** CD-DA music (CD audio tracks!), ADPCM voice, large stages!
- **Direct comparison:** "Here's your base TurboGrafx. Now enhance with SuperGrafx/CD-ROM²"
- Professional audio (CD-DA + ADPCM)
- Large game (CD storage)

**Phase 4: Shooter IV (Advanced)** (64 lessons)
- Advanced VDP (4 layers mastery)
- 128 sprites smooth
- CD-ROM² streaming (large levels)
- Professional CD audio

**Phase 6: Shooter V (TurboGrafx limits)** (128 lessons)
- Maximum sprites (128 smooth)
- Extreme optimization
- Commercial-quality (Blazing Lazers, Gate of Thunder level)
- Pushing TurboGrafx limits

Students see evolution: TurboGrafx basics → Optimized → **SuperGrafx/CD-ROM² enhanced** → Advanced → Professional

---

## Key Differences from Other Platforms

**TurboGrafx vs Genesis/SNES:**
- **Less RAM:** 8KB (vs Genesis 64KB, SNES 128KB - major constraint!)
- **More colors:** 482 on-screen (vs Genesis 64, SNES 256)
- **Earlier release:** 1987 (vs Genesis 1988, SNES 1990)
- **First CD-ROM:** CD-ROM² 1988 (vs Sega CD 1991)
- **6502-based CPU:** HuC6280 (vs Genesis 68000, SNES 65816)
- **Fewer sprites:** 64 base (vs Genesis 80, SNES 128)
- **Smaller in US:** 2.5M units (vs Genesis 30M, SNES 49M)

**TurboGrafx Advantages:**
- More colors (482 on-screen)
- **First CD-ROM** (CD-ROM² 1988 - pioneering!)
- CD-DA audio (CD-quality music)
- Earlier release (1987)
- HuCard format (compact, fast)
- Excellent shooters (genre strength)

**TurboGrafx Constraints:**
- **Only 8KB main RAM** (vs 64-128KB on Genesis/SNES!)
- Only 2 background layers base (vs SNES 4)
- Weaker US presence (vs Nintendo/Sega)
- 8-bit data bus ("16-bit" marketing)

**Learning Path:**
- TurboGrafx → Genesis/SNES (console generation comparison)
- HuC6280 → 6502 family (skills transfer to NES, C64, 2600, 7800)
- CD-ROM² → Sega CD/Saturn (CD-ROM console evolution)

**Same Pattern Library Concepts:**
- 6502 assembly (HuC6280 = 6502-based)
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
- Expected output defined (base, SuperGrafx, CD-ROM² where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete HuC6280 TurboGrafx games from scratch
- Understands VDP (2 backgrounds, 64 sprites, tile system)
- Understands 6-channel PSG (waveform + DDA)
- **Masters 8KB RAM constraint** (creative programming!)
- Has 16 portfolio TurboGrafx games

**Phase 3 Complete:**
- Student masters SuperGrafx (4 backgrounds, 128 sprites)
- Masters CD-ROM² (CD-DA audio, ADPCM, CD storage)
- Can compare/contrast base vs SuperGrafx vs CD-ROM² implementations
- Has base, SuperGrafx, and CD-ROM² versions of key games
- **CD-ROM pioneer understanding** (first console CD-ROM!)

**Phase 8 Complete:**
- Student has 60 portfolio games showcasing TurboGrafx
- Masters HuC6280 (6502-based, skills transfer to 6502 family)
- Masters VDP (all capabilities, SuperGrafx dual chips)
- Masters CD-ROM² (CD-DA, ADPCM, streaming, FMV)
- Masters 8KB RAM constraint (creative optimization)
- Can create commercial-release quality games
- Ready for professional TurboGrafx homebrew development
- **6502 expertise** transfers to NES, C64, 2600, 7800, Apple II

---

## Resources Required

**Development Tools:**
- Assembler: WLA-DX, NESASM (6502-based)
- HuC (C compiler for TurboGrafx!)
- Emulator: Mednafen (cycle-accurate, excellent debugger), Magic Engine, Ootake
- Graphics: Tile/sprite editors (TurboGrafx format)
- Audio: PSG trackers
- CD-ROM tools: ISO builders, CD-DA/ADPCM tools
- Utilities: HuCard/CD-ROM builders

**Reference Materials:**
- HuC6280 instruction set (6502-based with enhancements)
- VDP Programming Guide (HuC6270 - tiles, sprites, scrolling)
- PSG reference (6-channel waveform + DDA)
- CD-ROM² reference (CD-DA, ADPCM, System/Arcade Cards)
- SuperGrafx reference (dual VDP/VCE)
- TurboGrafx Technical Reference
- Memory map (8KB main RAM, VRAM, registers)

**Testing:**
- Emulators (development - Mednafen recommended)
- Real TurboGrafx-16 hardware (verification)
- TurboEverdrive (modern flash cart)
- CD-ROM² System (for CD games)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - SuperGrafx + CD-ROM² Phase 3
**Note:** No Phase 0 (console - no BASIC, direct assembly)
**Historical Note:** First "16-bit" console (Japan 1987), first CD-ROM add-on (1988), 10M units sold
**Unique Features:** **CD-ROM² (first console CD-ROM!), SuperGrafx (dual VDP), HuCard format**
**CPU:** HuC6280 @ 7.16MHz (6502-based) - skills transfer to 6502 family!
**Major Constraint:** **Only 8KB main RAM** (vs Genesis 64KB, SNES 128KB - teaches efficient programming!)
**Next Steps:** Create TurboGrafx-16 8-PHASE-GAME-PROGRESSION.md with specific game mapping
