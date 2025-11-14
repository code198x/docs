# Sam Coupe Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** Sam Coupe base → Advanced features Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - SAM BASIC
**Historical Note:** British "super Spectrum" (1989-1992), sophisticated hardware, cult following
**Relationship:** Spectrum spiritual successor (Z80-compatible, better hardware)

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare basic vs advanced implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Z80 addressing modes are Z80 addressing modes" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master Sam Coupe base hardware (Z80B @ 6MHz, 256KB RAM)
- Phase 3: **Advanced features mastery** - disk systems, hardware sprites optimization
- Phase 4-6: Advanced techniques, pushing Sam Coupe limits
- Phase 7: **Maximum Sam Coupe** - all capabilities, professional development
- Phase 8: Modern Sam Coupe development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Sam Coupe base (Z80B @ 6MHz, 256KB RAM)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- Z80 instruction set fundamentals (same as Spectrum, but faster)
- **SAM BASIC loader - Lesson 2-3, mandatory from Lesson 3**
- ASIC (Application Specific Integrated Circuit) - custom chip
- Screen modes (multiple resolutions: 256×192, 512×192)
- Palette system (128 colours from 4096 palette)
- **Hardware sprites** (unlike Spectrum - no character clash!)
- 6-channel stereo sound (SAA1099 chip - much better than Spectrum beeper)
- Memory paging (256KB in 16KB pages)
- Keyboard/joystick input
- Interrupt timing (50Hz PAL)
- Disk drive (built-in 3.5" floppy)

**Autoload Requirement:**
All games from Lesson 3 onwards must use SAM BASIC loader:
```basic
10 LOAD "game" CODE 32768
20 RANDOMIZE USR 32768
```
Professional presentation: LOAD from disk, RUN, game starts automatically.

**Deliverables:** 16 complete, playable Sam Coupe games with professional autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Sam Coupe base (Z80B @ 6MHz, 256KB RAM)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized Z80 code (6MHz vs Spectrum's 3.5MHz - nearly 2× faster)
- Hardware sprite optimization (no clash, smooth movement)
- Palette manipulation (128 colours available)
- Multi-screen mode techniques
- SAA1099 music programming (6-channel stereo)
- Advanced memory paging (256KB efficiently)
- Scrolling systems (hardware support)
- Disk I/O (3.5" floppy drive)
- Advanced collision detection

**Deliverables:** 16 games with commercial-quality Sam Coupe features

---

### Phase 3: Advanced Features Mastery
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** Sam Coupe advanced features
**Complexity:** Direct basic→advanced comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with advanced features, 3 new showcasing mastery

**Key Learning:**
- **Advanced sprite techniques** (all hardware capabilities)
- **Disk-based game systems** (multi-level loading)
- **Direct comparison:** "Here's your basic game. Now enhance it with advanced features"
- Advanced palette effects (128 colours, dynamic changes)
- Advanced SAA1099 programming (all 6 channels, stereo effects)
- Memory banking mastery (256KB efficiently)
- Professional screen mode usage
- Hardware scrolling optimization
- Comparing to Spectrum (Z80 skills transfer)

**Deliverables:** 8 games - 5 enhanced advanced versions, 3 new showcasing mastery

**Games Revisited with Advanced Features:**
1. Snake III (Advanced) - hardware sprites, smooth scrolling
2. Shooter III (Advanced) - multi-level disk loading, all colours
3. Platformer III (Advanced) - advanced sprites, parallax scrolling
4. Breakout III (Advanced) - palette effects, stereo sound
5. One other from Phase 1-2

**New Advanced Games:**
6. Action RPG I (showcasing disk systems, 256KB RAM)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Sam Coupe (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced ASIC programming (all capabilities)
- Maximum sprite utilization (smooth, no flicker)
- Advanced SAA1099 (6-channel stereo mastery)
- Complex palette effects (128 colours)
- Advanced scrolling (hardware + software hybrid)
- Disk I/O optimization (fast loading)
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced Sam Coupe techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Sam Coupe mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced SAA1099 music composition
- Disk-based multi-level games
- Multi-disk games (if applicable)
- Memory management (256KB efficiently)

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Sam Coupe (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing many simultaneous sprites (all hardware sprites)
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme Z80 optimization (6MHz maximum efficiency)
- Fast disk loaders (custom routines)
- Pushing Sam Coupe limits
- Professional Sam Coupe development

**Deliverables:** 4 games pushing absolute limits of Sam Coupe

---

### Phase 7: Maximum Sam Coupe
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Sam Coupe (maximum capabilities)
**Complexity:** Large-scale games with maximum features
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- Maximum 256KB RAM usage
- All ASIC capabilities (graphics, sprites, everything)
- All SAA1099 capabilities (6-channel stereo perfection)
- Large game worlds (disk-based)
- Advanced graphics techniques (all screen modes)
- Commercial Sam Coupe development
- Professional quality polish

**Deliverables:** 2 commercial-scale Sam Coupe games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern Sam Coupe development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern Sam Coupe development workflow
- Emulator debugging (SimCoupe, SAM Coupe emulators)
- Modern expansions (rare but exist)
- Pushing Sam Coupe absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- **Historical significance:** "Super Spectrum", cult following, sophisticated hardware

**Deliverables:** 2 portfolio-ready commercial-quality Sam Coupe games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. Z80 Programming**
- P1: Basic instructions (same as Spectrum, CPC, MSX, TRS-80)
- P2: Advanced Z80 techniques (6MHz optimization)
- P3: Sam Coupe hardware mastery (ASIC, sprites)
- P4: Complex Z80 techniques
- P5+: Extreme optimization

**2. Graphics Programming**
- P1: ASIC basics (screen modes, palette)
- P2: Multiple screen modes (256×192, 512×192)
- P3: Advanced screen techniques (all modes)
- P4: Maximum ASIC capabilities
- P5+: Complex graphics systems

**3. Sprite Management**
- P1: **Hardware sprites** (no clash - unlike Spectrum!)
- P2: Sprite optimization (smooth movement)
- P3: Advanced sprite techniques (all hardware)
- P4: Maximum sprite utilization
- P5+: Complex sprite systems

**4. Scrolling Systems**
- P1: Hardware scrolling basics
- P2: Multi-directional scrolling
- P3: Advanced scrolling (hardware + software)
- P4: Parallax scrolling
- P5+: Complex scrolling effects

**5. Sound Programming**
- P1: SAA1099 basics (6-channel stereo)
- P2: Music composition (multi-channel)
- P3: Advanced SAA1099 (all channels, stereo)
- P4: Professional audio
- P5+: Commercial-quality sound

**6. Memory Management**
- P1: Basic paging (256KB in 16KB pages)
- P2: Efficient memory usage
- P3: Advanced paging techniques
- P4: Complex banking strategies
- P5+: Maximum 256KB efficiency

**7. Palette Programming**
- P1: Basic palette (128 colours from 4096)
- P2: Colour cycling, palette effects
- P3: Advanced palette manipulation
- P5+: Complex colour effects

**8. Disk I/O**
- P1: Basic disk operations (3.5" floppy)
- P2: Multi-file loading
- P3: Disk-based game structure
- P4: Advanced disk access
- P5: Multi-level disk systems
- P6: Fast loaders

---

## Hardware Progression

### Sam Coupe Base (Phases 1-2)
**Platform:** Sam Coupe (1989)
**Characteristics:**
- **Z80B CPU @ 6MHz** (nearly 2× faster than Spectrum's 3.5MHz)
- **256KB RAM** (vs Spectrum's 48KB/128KB)
- **ASIC custom chip** (Application Specific Integrated Circuit)
- Multiple screen modes (256×192, 512×192, various)
- **128 colours available** from 4096 palette (vs Spectrum's 16 bright/8 normal)
- **Hardware sprites** (Spectrum has none - no character clash!)
- **SAA1099 sound chip** (6-channel stereo vs Spectrum's beeper)
- Memory paging (256KB in 16KB pages)
- Built-in 3.5" floppy disk drive
- Keyboard/joystick input
- 50Hz PAL

**Focus:** Master superior Sam Coupe hardware
- Z80B programming (faster than Spectrum)
- Hardware sprites (no clash!)
- Palette system (128 colours)
- 6-channel stereo sound
- 256KB RAM management

**Historical Context:**
- British computer (MGT - Miles Gordon Technology)
- "What the Spectrum should have been"
- Released 1989 (late in 8-bit era)
- Short-lived (1989-1992)
- Spectrum spiritual successor (Z80-compatible)
- Cult following (still active today)
- ~12,000 units sold (commercial failure but technical success)

**Relationship to Spectrum:**
- Z80-compatible (same instruction set)
- Can run modified Spectrum software
- Similar market positioning (British home computer)
- Much more powerful hardware
- "Super Spectrum" design philosophy

### Sam Coupe Advanced (Phase 3+)
**Introduced Phase 3**
**Enhanced Focus:**
- Advanced sprite techniques
- Disk-based game systems
- All 256KB RAM efficiently
- Advanced palette effects
- Advanced SAA1099 programming
- Professional optimization

**Focus:** Master all capabilities
- All hardware features
- Disk systems mastery
- Professional development techniques

### Modern Sam Coupe (Phase 7-8)
**Modern enhancements:**
- SimCoupe emulator (excellent)
- Modern assemblers
- Active community (still exists!)
- Modern storage solutions

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (Sam Coupe base)** (16 lessons)
- Basic grid movement (Z80 fundamentals)
- Hardware sprites (no clash!)
- Palette colours (128 available)
- SAA1099 sound (6-channel)
- 256KB RAM

**Phase 2: Snake II (Sam Coupe optimized)** (32 lessons)
- Optimized Z80 code (6MHz)
- Better sprite usage
- Palette effects
- Multi-channel music
- Multi-screen levels

**Phase 3: Snake III (Advanced features)** (64 lessons - REVISITED WITH ADVANCED FEATURES)
- **Disk-based levels** (multi-level loading)
- **Advanced sprites** (all hardware)
- **Advanced palette** (colour cycling)
- **Advanced sound** (all 6 channels)
- **Direct comparison:** "Here's your basic Snake. Now enhance it with advanced features"

**Phase 4: Snake IV (Advanced)** (64 lessons)
- Advanced scrolling
- Complex palette effects
- Professional audio
- Disk optimization

**Phase 6: Snake V (Sam Coupe limits)** (128 lessons)
- Maximum sprite usage
- Extreme optimization
- Commercial-quality
- Pushing Sam Coupe limits

Students see evolution: Sam Coupe basics → Sam Coupe optimized → **Advanced features** → Maximum capabilities → Professional

---

## Key Differences from Spectrum

**Sam Coupe vs ZX Spectrum:**
- **Same Z80 CPU family** (Z80B @ 6MHz vs Z80 @ 3.5MHz - nearly 2× faster)
- **More RAM:** 256KB (vs Spectrum's 48KB/128KB)
- **Hardware sprites:** Yes (vs Spectrum's none - no character clash!)
- **Better graphics:** 128 colours from 4096 palette (vs 16 bright/8 normal)
- **Better sound:** SAA1099 6-channel stereo (vs Spectrum's beeper)
- **Better storage:** Built-in 3.5" floppy (vs Spectrum's cassette/Microdrive)
- **Later release:** 1989 (vs Spectrum 1982)

**Sam Coupe Advantages:**
- Hardware sprites (no clash!)
- Much better sound (6-channel stereo)
- More colours (128 vs ~16)
- More RAM (256KB vs 48/128KB)
- Faster CPU (6MHz vs 3.5MHz)
- Built-in disk drive

**Sam Coupe Considerations:**
- Small user base (~12,000 units)
- Short commercial lifespan (1989-1992)
- Less software library than Spectrum
- British market primarily

**Learning Path:**
- Spectrum → Sam Coupe (natural upgrade path)
- Z80 skills transfer directly
- Understanding British home computer evolution

**Same Pattern Library Concepts:**
- Z80 assembly (identical to Spectrum)
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
- Expected output defined
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete Z80 Sam Coupe games from scratch
- Understands hardware sprites (no clash!)
- Understands SAA1099 (6-channel stereo)
- Has 16 portfolio Sam Coupe games

**Phase 3 Complete:**
- Student masters advanced Sam Coupe features
- Can create disk-based multi-level games
- Masters all hardware capabilities
- Has advanced versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games showcasing Sam Coupe
- Masters Z80 architecture (6MHz optimization)
- Masters Sam Coupe custom chips (ASIC, SAA1099)
- Can create commercial-release quality games
- Ready for professional Sam Coupe development
- **Z80 expertise** transfers to Spectrum, CPC, MSX, TRS-80

---

## Resources Required

**Development Tools:**
- Assembler: pyz80.py, modern Z80 cross-assemblers
- Emulator: SimCoupe (excellent Sam Coupe emulation)
- Graphics: Sam Coupe graphics tools
- Audio: SAA1099 trackers
- Utilities: Disk image tools

**Reference Materials:**
- Z80 instruction set
- ASIC reference (custom chip documentation)
- SAA1099 sound chip reference
- SAM BASIC reference
- Memory map documentation

**Testing:**
- SimCoupe emulator (development)
- Real Sam Coupe hardware (verification, if accessible)
- Active community resources

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined
**Note:** Sam Coupe has Phase 0 (SAM BASIC)
**Historical Note:** British "super Spectrum" (1989-1992), sophisticated hardware, cult following
**Relationship:** Spectrum spiritual successor - Z80-compatible, much better hardware
**Key Feature:** **Hardware sprites** (no character clash - major Spectrum improvement!)
**Next Steps:** Create Sam Coupe 8-PHASE-GAME-PROGRESSION.md with specific game mapping
