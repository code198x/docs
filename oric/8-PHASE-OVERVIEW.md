# Oric-1/Atmos Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** Oric-1 (16KB) → Oric Atmos introduced Phase 3 (48KB) → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - Oric BASIC
**Note:** UK/French competitor to Spectrum, 6502-based with AY sound chip

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare Oric-1 vs Oric Atmos implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "6502 addressing modes are 6502 addressing modes" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master Oric-1 (16KB RAM, 6502 @ 1MHz)
- Phase 3: **Oric Atmos introduced** - 48KB RAM, better keyboard, revisit games
- Phase 4-6: Advanced techniques, pushing Atmos limits
- Phase 7: **Oric Telestrat** (rare, enhanced model) / modern expansions
- Phase 8: Modern Oric development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Oric-1 (16KB RAM, 6502 @ 1MHz)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 6502 instruction set fundamentals
- **Oric BASIC loader - Lesson 2-3, mandatory from Lesson 3**
- ULA chip basics (graphics, sound, color)
- TEXT mode (40×28 characters, 8 colors)
- HIRES mode (240×200 pixels, 2 colors per 6-pixel cell)
- AY-3-8912 PSG (3-voice sound, same as Spectrum 128K/CPC)
- Software sprite rendering
- Keyboard input
- Cassette tape storage
- Interrupt timing (50Hz PAL / 60Hz NTSC)

**Autoload Requirement:**
All games from Lesson 3 onwards must use Oric BASIC loader:
```basic
10 HIMEM #9FFF
20 CALL #A000
```
Or inline assembly. Professional presentation: LOAD from tape, game starts automatically.

**Deliverables:** 16 complete, playable Oric-1 games with professional autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Oric-1 (16KB RAM)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 6502 routines (zero-page, lookup tables)
- Software sprite optimization (HIRES mode)
- Advanced ULA programming
- AY PSG music sequencing (3 voices)
- Character set customization
- Advanced collision detection
- Multi-screen game structures
- Memory management (16KB efficiently)

**Deliverables:** 16 games with commercial-quality Oric-1 features

---

### Phase 3: Enhanced Model (Oric Atmos)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **Oric Atmos introduced** - 48KB RAM, better keyboard
**Complexity:** Direct Oric-1→Atmos comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with Atmos, 3 new showcasing 48KB

**Key Learning:**
- **Oric Atmos** (48KB RAM, 3× more memory)
- **Better keyboard** (proper keyboard vs Oric-1's less reliable one)
- **Direct comparison:** "Here's your 16KB Snake. Now expand it with Atmos's 48KB"
- Larger game worlds (more RAM for data)
- Better graphics (room for sprite libraries)
- Music and sound effects simultaneously
- Advanced sprite systems
- Professional Oric-1 optimization (for games staying on 16KB)

**Deliverables:** 8 games - 5 enhanced Atmos versions, 3 new showcasing 48KB

**Games Revisited with Oric Atmos:**
1. Snake III (Atmos) - larger worlds, better graphics
2. Shooter III (Atmos) - multiple stages, music
3. Platformer III (Atmos) - larger world, animations
4. Breakout III (Atmos) - more levels, effects
5. One other from Phase 1-2

**New Atmos Games:**
6. Action RPG I (showcasing 48KB RAM)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Oric Atmos (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced ULA programming (HIRES tricks, attributes)
- Complex sprite systems (48KB allows data)
- Advanced AY PSG programming (all 3 voices, envelopes)
- Scrolling techniques (character and pixel-based)
- Disk I/O (Microdisc system - 3" floppy)
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced Oric Atmos techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Oric Atmos mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced AY music composition
- Disk-based save/load systems (Microdisc)
- Multi-disk games

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Oric Atmos (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous software sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 6502 optimization
- Fast disk loaders (Microdisc)
- Pushing Oric Atmos limits
- Professional Oric development

**Deliverables:** 4 games pushing absolute limits of Oric Atmos

---

### Phase 7: Oric Telestrat & Enhancements
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Oric Telestrat (rare) / modern Oric enhancements
**Complexity:** Large-scale games with enhanced capabilities
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- **Oric Telestrat** (1986, 64KB RAM, cartridge slot)
- Banking system (Telestrat)
- Cartridge games
- Modern Oric expansions (Cumulus, Twilighte Board)
- Large game worlds
- Advanced ULA/AY techniques
- Commercial Oric development

**Deliverables:** 2 commercial-scale Oric games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern Oric development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern Oric development workflow
- Emulator debugging (Oricutron, MAME)
- Modern expansions (Cumulus, Twilighte Board, microSD)
- Pushing Oric absolute limits
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- Modern Oric community standards

**Deliverables:** 2 portfolio-ready commercial-quality Oric games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 6502 Programming**
- P1: Basic instructions (same as C64, Apple II, etc.)
- P2: Advanced 6502 techniques
- P3: Atmos optimization (more RAM)
- P4: Complex 6502 techniques
- P5+: Extreme optimization

**2. Graphics Programming**
- P1: TEXT and HIRES modes
- P2: Advanced HIRES techniques
- P3: Atmos graphics (48KB allows more)
- P4: Advanced ULA tricks
- P5+: Complex graphics systems

**3. Sprite Rendering**
- P1: Software sprites (HIRES mode)
- P2: Optimized sprites (6502)
- P3: Atmos sprites (48KB allows data)
- P4: Advanced sprite systems
- P5+: Multi-sprite management (32+ sprites)

**4. Scrolling Systems**
- P1: Screen-aligned scrolling
- P2: Character scrolling
- P3: Pixel scrolling (Atmos)
- P4: Complex scrolling
- P5+: Advanced scrolling

**5. Sound Programming**
- P1: AY PSG basics (3 voices)
- P2: Music sequencing
- P3: Advanced AY programming (Atmos)
- P4: Envelopes, complex music
- P5+: Professional audio

**6. Memory Management**
- P1: Basic RAM (16KB Oric-1)
- P2: Efficient data structures
- P3: **Atmos (48KB RAM)**
- P4: Efficient use of 48KB
- P5+: Telestrat banking

**7. Collision Detection**
- P1: Bounding box collision
- P2: Pixel-perfect collision
- P3: Atmos optimized collision
- P5+: Multi-layer collision

**8. Disk I/O**
- P3: Microdisc basics
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders
- P8: Modern storage (Cumulus, microSD)

---

## Hardware Progression

### Oric-1 (Phases 1-2)
**Platform:** Oric-1 (1983)
**Characteristics:**
- 6502 CPU @ 1MHz
- 16KB RAM
- ULA chip (graphics, color)
- TEXT mode: 40×28 characters, 8 colors
- HIRES mode: 240×200 pixels, 2 colors per 6-pixel cell
- **AY-3-8912 PSG** (3-voice sound, same as Spectrum 128K/CPC)
- 8 colors (black, red, green, yellow, blue, magenta, cyan, white)
- Cassette tape storage
- 50Hz PAL / 60Hz NTSC

**Focus:** Master Oric-1 fundamentals
- 6502 programming
- ULA graphics (TEXT and HIRES)
- AY PSG sound (3 voices)
- Software sprite rendering

**Historical Context:**
- UK/French market
- Competed with Spectrum
- Cult following (quality sound chip)
- Sold ~200,000 units

### Oric Atmos (Phase 3+)
**Platform:** Oric Atmos (1984)
**Introduced Phase 3**
**Enhanced Features:**
- **48KB RAM** (3× more than Oric-1)
- **Better keyboard** (more reliable)
- Same 6502 @ 1MHz
- Same ULA and AY PSG
- **Direct comparison:** 16KB vs 48KB RAM

**Focus:** Leverage memory expansion
- More room for graphics/sprites
- Larger game worlds
- Music + effects simultaneously
- Professional game development

### Oric Telestrat (Phase 7)
**Platform:** Oric Telestrat (1986, rare)
**Enhanced Features:**
- 64KB RAM
- Banking system
- Cartridge slot
- Better keyboard
- Rare (primarily France)

### Modern Oric (Phase 8)
**Modern enhancements:**
- Cumulus (microSD interface)
- Twilighte Board (modern expansion)
- Oricutron emulator (excellent)
- Modern assemblers

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (Oric-1)** (16 lessons)
- Basic grid movement (6502 fundamentals)
- HIRES graphics (240×200)
- Software sprites
- AY PSG sound
- 16KB RAM

**Phase 2: Snake II (Oric-1 optimized)** (32 lessons)
- Optimized 6502 code
- Better HIRES graphics
- AY music
- Multi-screen levels
- Optimized Oric-1

**Phase 3: Snake III (Oric Atmos)** (64 lessons - REVISITED WITH ATMOS)
- **48KB RAM** (3× more memory)
- **Larger playfield**
- **Music + effects**
- **Better graphics**
- **Direct comparison:** "Here's your 16KB Snake. Now expand it with Atmos"

**Phase 4: Snake IV (Advanced Atmos)** (64 lessons)
- Advanced HIRES tricks
- Complex AY music
- Scrolling playfield
- Disk-based levels

**Phase 6: Snake V (Atmos limits)** (128 lessons)
- 32+ simultaneous AI snakes
- Extreme optimization
- Commercial-quality
- Pushing Atmos limits

Students see evolution: Oric-1 basics → Oric-1 optimized → **Atmos expanded** → Advanced → Professional

---

## Key Differences from Other Platforms

**Oric Advantages:**
- **AY-3-8912 PSG** (excellent 3-voice sound, same as Spectrum 128K/CPC)
- 6502 CPU (well-documented, same as C64/Apple II)
- 8 colors (more than Spectrum's 2 per character block)
- HIRES mode (240×200)
- Cult following (quality hardware)

**Oric Considerations:**
- Less common than Spectrum/C64
- Smaller software library
- HIRES mode has attribute limitations
- Primarily UK/France market

**Similar To:**
- C64 (6502 CPU)
- Apple II (6502 CPU)
- Amstrad CPC (AY PSG sound)
- Spectrum (UK competitor)

**Same Pattern Library Concepts:**
- 6502 assembly (same as C64, Apple II, VIC-20)
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
- Expected output defined (Oric-1 and Atmos where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 6502 Oric games from scratch
- Understands ULA graphics (TEXT and HIRES)
- Understands AY PSG sound
- Has 16 portfolio Oric-1 games

**Phase 3 Complete:**
- Student masters Oric Atmos
- Can compare/contrast Oric-1 vs Atmos implementations
- Has both Oric-1 and Atmos versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all Oric variants
- Masters 6502 architecture
- Masters ULA and AY PSG programming
- Can create commercial-release quality games
- Ready for professional Oric development
- **6502 expertise** transfers to C64, Apple II, VIC-20

---

## Resources Required

**Development Tools:**
- Assembler: xa, 6502 cross-assemblers
- Emulator: Oricutron (excellent), MAME
- Graphics: Oric graphics editors
- Audio: AY tracker tools
- Utilities: Tape/disk image tools

**Reference Materials:**
- 6502 instruction set
- ULA reference
- AY-3-8912 PSG reference
- Oric Technical Manual
- Oric BASIC reference

**Testing:**
- Emulators (development)
- Real Oric hardware (verification)
- Oric Atmos (Phase 3+)
- Modern expansions (Cumulus, etc.)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Oric Atmos introduced Phase 3
**Note:** Oric has Phase 0 (Oric BASIC)
**Historical Note:** UK/French competitor to Spectrum, 6502-based with excellent AY sound chip
**Next Steps:** Create Oric 8-PHASE-GAME-PROGRESSION.md with specific game mapping
