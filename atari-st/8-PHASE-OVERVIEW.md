# Atari ST Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** ST (520ST/1040ST) → STe introduced Phase 3 → Falcon030 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - GFA BASIC

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare ST vs STe implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Blitter operations are blitter operations" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master base ST (520ST/1040ST, 68000 @ 8MHz)
- Phase 3: **STe introduced** - Blitter, DMA sound, enhanced palette, revisit games
- Phase 4-6: Advanced techniques, pushing STe limits
- Phase 7: **Falcon030** - DSP, true color, enhanced audio
- Phase 8: Modern ST development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Atari ST base (520ST/1040ST)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 68000 instruction set fundamentals
- **GFA BASIC inline assembly - Lesson 2-3, mandatory from Lesson 3**
- BIOS/XBIOS/GEMDOS basics (TOS operating system)
- Screen modes (320×200×16 colors, 640×200×4 colors)
- Shifter chip basics (video control)
- Software sprite rendering (no hardware sprites on ST)
- PSG sound (YM2149, 3 voices like Amiga/CPC)
- Joystick/mouse input (IKBD intelligent keyboard)
- VBL interrupt (50Hz PAL / 60Hz NTSC)

**Autoload Requirement:**
All games from Lesson 3 onwards must be standalone executables:
- .PRG format (GEM executable)
- Professional presentation: double-click from desktop, game starts
- Can use GFA BASIC compiled programs or pure assembly .PRG
- No manual commands in CLI

**Deliverables:** 16 complete, playable ST games with professional .PRG format

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Base ST (520ST/1040ST)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 68000 routines (address registers, efficient moves)
- Software sprite optimization (pre-shifted, masked)
- Screen double buffering (page flipping)
- Hardware scrolling techniques (limited on base ST)
- PSG music sequencing (3 voices)
- Advanced collision detection
- Multi-screen game structures
- Memory management (512KB/1MB efficiently)

**Deliverables:** 16 games with commercial-quality ST features

---

### Phase 3: Enhanced Hardware (STe)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **Atari STe introduced** - Blitter, DMA sound, enhanced palette
**Complexity:** Direct ST→STe comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with STe, 3 new showcasing features

**Key Learning:**
- **Blitter chip programming** (fast graphics like Amiga)
- **DMA sound** (stereo 8-bit sample playback)
- **Extended palette** (4096 colors from 24-bit palette)
- **Hardware scrolling** (horizontal offset registers)
- **Direct comparison:** "Here's your ST Snake. Now enhance it with STe features"
- Blitter operations (fast copies, fills, line drawing)
- Sample playback vs PSG
- Professional ST optimization (for games staying on base ST)

**Deliverables:** 8 games - 5 STe versions of earlier games, 3 new showcasing STe

**Games Revisited with STe:**
1. Snake III (STe) - Blitter graphics, DMA sound
2. Shooter III (STe) - hardware scrolling, 4096 colors
3. Platformer III (STe) - Blitter optimization, samples
4. Breakout III (STe) - enhanced palette, DMA audio
5. One other from Phase 1-2

**New STe Games:**
6. Action RPG I (showcasing Blitter + palette)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** STe (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced Blitter programming (complex operations)
- DMA sound mixing (multi-channel playback)
- Advanced palette techniques (copper-like raster effects)
- Hardware scrolling optimization
- Disk I/O (GEMDOS, custom loaders)
- Isometric projection
- Turn-based strategy mechanics
- Complex game state management

**Deliverables:** 8 games showcasing advanced STe techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** STe mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced DMA sound (tracker format)
- Disk-based save/load systems
- Multi-disk games

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** STe (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous sprites (Blitter optimization)
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme Blitter techniques
- Fast disk loaders (custom routines)
- Large-scale STe games
- Professional ST development

**Deliverables:** 4 games pushing absolute limits of STe

---

### Phase 7: Enhanced Audio/Graphics (Falcon030)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Atari Falcon030 - DSP, true color, enhanced features
**Complexity:** Large-scale games with enhanced audio/graphics
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- **Falcon030 68030 CPU** (16MHz, faster than STe)
- **DSP (Motorola 56001)** - Digital Signal Processor
- **True color modes** (65,536 colors)
- **Enhanced Videl chip** (programmable video)
- **Professional audio** (16-bit stereo, DSP effects)
- Large game worlds
- DSP programming basics
- Commercial Falcon development

**Deliverables:** 2 commercial-scale Falcon030 games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern ST development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern ST development workflow
- Emulator debugging (Hatari, Steem)
- Pushing ST/STe/Falcon limits
- Modern storage (SD cards, hard drives)
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- Modern ST community standards

**Deliverables:** 2 portfolio-ready commercial-quality ST games showcasing everything learned

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. Screen Management**
- P1: Basic screen modes (320×200×16, 640×200×4)
- P2: Double buffering (page flipping)
- P3: STe hardware scrolling, extended palette
- P4: Advanced screen techniques
- P5+: Complex display systems
- P7: Falcon true color modes

**2. Graphics Rendering**
- P1: Software sprite rendering (no hardware sprites)
- P2: Optimized software sprites (pre-shifted)
- P3: **Blitter sprites (STe - hardware acceleration)**
- P4: Advanced Blitter techniques
- P5+: Complex sprite systems (32+ sprites)
- P7: Falcon enhanced graphics

**3. Scrolling Systems**
- P1: Screen-aligned scrolling (page flipping)
- P2: Software pixel scrolling
- P3: **STe hardware scrolling** (horizontal offset)
- P4: Complex scrolling (parallax, multi-directional)
- P5+: Advanced scrolling techniques
- P7: Falcon Videl scrolling

**4. Sound Programming**
- P1: PSG basics (YM2149, 3 voices)
- P2: PSG music sequencing
- P3: **DMA sound (STe - 8-bit stereo samples)**
- P4: DMA mixing, multi-channel
- P5+: Advanced audio (tracker format)
- P7: **Falcon DSP audio** (16-bit, effects)

**5. Palette Management**
- P1: Basic 16-color palette (512 colors available)
- P2: Palette cycling, effects
- P3: **STe extended palette** (4096 colors from 24-bit)
- P4: Raster palette changes
- P5+: Complex palette effects
- P7: **Falcon true color** (65,536 colors)

**6. Collision Detection**
- P1: Bounding box collision
- P2: Pixel-perfect (check screen memory)
- P3: Blitter-assisted collision
- P5+: Multi-layer collision

**7. Memory Management**
- P1: Basic RAM usage (512KB/1MB)
- P2: Efficient data structures
- P3: STe 4MB RAM support
- P4: Large data management
- P5+: Complex memory systems
- P7: Falcon extended RAM

**8. Disk I/O**
- P3: Basic GEMDOS file operations
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders, custom routines
- P8: Modern storage (SD cards)

---

## Hardware Progression

### Base ST (Phases 1-2)
**Platform:** Atari 520ST/1040ST (1985-1986)
**Characteristics:**
- 68000 CPU @ 8MHz
- 512KB (520ST) or 1MB (1040ST) RAM
- TOS operating system (GEM desktop)
- Shifter chip (video - 320×200×16 or 640×200×4)
- No hardware sprites (software rendering)
- YM2149 PSG (3 voices, like Amstrad CPC)
- IKBD intelligent keyboard (mouse/joystick)
- Blitter: **None on base ST**
- 512 colors available (16 on-screen from 512)

**Focus:** Master base ST fundamentals
- 68000 programming
- TOS/BIOS/XBIOS calls
- Software sprite techniques
- PSG sound
- Screen double buffering
- Creative solutions without Blitter

### Atari STe (Phase 3+)
**Platform:** Atari STe (1989)
**Introduced Phase 3**
**Enhanced Features:**
- **Blitter chip** (fast graphics operations like Amiga)
- **DMA sound** (stereo 8-bit sample playback, 50KHz)
- **Extended palette** (4096 colors from 24-bit palette)
- **Hardware scrolling** (horizontal fine scroll)
- 512KB-4MB RAM (expandable)
- Joystick ports enhanced (analog support)
- **Direct comparison:** ST vs STe implementations

**Focus:** Leverage STe enhancements
- Blitter operations (fills, copies, line drawing)
- DMA sample playback (music + effects)
- 4096-color palette
- Hardware scrolling
- Professional visuals/audio

### Atari Falcon030 (Phase 7)
**Platform:** Atari Falcon030 (1992)
**Enhanced Features:**
- **68030 CPU @ 16MHz** (faster than STe)
- **Motorola 56001 DSP** @ 32MHz (audio/graphics processing)
- **Videl chip** (programmable video, true color)
- **True color modes** (256 colors, 65,536 colors)
- **16-bit stereo audio** via DSP
- IDE hard drive interface
- Up to 14MB RAM

**Focus:** Advanced audio/graphics
- DSP programming
- True color graphics
- Professional audio synthesis
- Large-scale games

### Modern Development (Phase 8)
**Modern Tools:**
- Emulators (Hatari - excellent debugger, Steem)
- Cross-assemblers (vasm, DevPac on modern systems)
- Modern ST hardware (FireBee, MiST FPGA)
- SD card interfaces
- Modern development workflow

**Focus:** Modern workflow
- Commercial-quality games
- Modern tools and debugging
- Portfolio showcase
- Community release

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (Base ST)** (16 lessons)
- Basic grid movement (68000 fundamentals)
- 320×200×16 color display
- Software sprite rendering
- PSG sound effects
- 512KB/1MB RAM

**Phase 2: Snake II (ST optimized)** (32 lessons)
- Optimized software sprites
- Double buffering
- PSG music sequencing
- Multi-screen levels
- Optimized ST

**Phase 3: Snake III (STe)** (64 lessons - REVISITED WITH STe)
- **Blitter graphics** (hardware acceleration)
- **DMA sound** (sample playback)
- **4096-color palette**
- **Hardware scrolling**
- **Direct comparison:** "Here's your ST Snake. Now enhance it with STe Blitter and DMA sound"

**Phase 4: Snake IV (Advanced STe)** (64 lessons)
- Advanced Blitter techniques
- Multi-channel DMA mixing
- Complex scrolling
- Disk-based levels

**Phase 6: Snake V (STe limits)** (128 lessons)
- 32+ simultaneous AI snakes (Blitter optimization)
- Extreme optimization
- Commercial-quality
- Pushing STe limits

**Phase 7: Snake Ultimate (Falcon030)** (if applicable)
- DSP audio
- True color graphics
- 68030 optimization

Students see evolution: ST basics → ST optimized → **STe enhanced** → Advanced → Professional → Falcon

---

## Key Differences from Other Platforms

**Atari ST Advantages:**
- 68000 CPU @ 8MHz (same family as Amiga, faster than 8-bit)
- TOS/GEM operating system (file system, desktop)
- MIDI ports (music production standard)
- Good development tools (GFA BASIC, DevPac, etc.)
- STe: Blitter + DMA sound (closer to Amiga)

**Atari ST Considerations:**
- No hardware sprites on base ST (unlike Amiga)
- Limited colors on-screen (16 from 512 on base ST)
- No custom chips like Amiga (simpler but less capable)
- STe less common than base ST
- Blitter only on STe (not base ST)

**Similar To:**
- Amiga (68000 CPU, similar era, competitor)
- Atari 8-bit (same company, different architecture)

**Unique Features:**
- MIDI ports built-in (industry standard)
- TOS/GEM (intuitive desktop OS)
- STe Blitter (fast graphics)
- Falcon DSP (powerful audio)

**Same Pattern Library Concepts:**
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
- Expected output defined (ST and STe where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 68000 ST games from scratch
- Understands TOS, screen modes, PSG sound
- Has 16 portfolio base ST games

**Phase 3 Complete:**
- Student masters STe Blitter and DMA sound
- Can compare/contrast ST vs STe implementations
- Has both ST and STe versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all ST variants
- Masters base ST, STe, and Falcon030
- Can create commercial-release quality games
- Ready for professional Atari ST development

---

## Resources Required

**Development Tools:**
- Assembler: vasm, DevPac, Turbo Assembler
- BASIC: GFA BASIC, STOS BASIC, Omikron BASIC
- Emulator: Hatari (best debugger), Steem, Saint
- Graphics: Degas Elite, NeoChrome
- Audio: MaxYMiser (YM2149), sample editors
- Utilities: Disk image tools

**Reference Materials:**
- 68000 instruction set
- TOS/BIOS/XBIOS reference
- Shifter chip reference
- Blitter reference (STe)
- DMA sound reference (STe)
- Videl/DSP reference (Falcon)

**Testing:**
- Emulators (development)
- Real ST hardware (verification)
- STe (Phase 3+)
- Falcon030 (Phase 7)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - STe introduced Phase 3
**Note:** Atari ST has Phase 0 (GFA BASIC - very popular on ST)
**Next Steps:** Create Atari ST 8-PHASE-GAME-PROGRESSION.md with specific game mapping
