# Atari 8-bit Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** Atari 400/800/XL/XE → VBXE → Modern (Ultimate Cart, FPGA)
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - Atari BASIC

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare basic vs optimized vs advanced display list implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Display lists are display lists" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master base Atari (ANTIC, GTIA, POKEY, PMG)
- Phase 3: **Advanced ANTIC/GTIA techniques** - display list interrupts, mode mixing
- Phase 4-6: Professional techniques, pushing XL/XE limits
- Phase 7: **VBXE (Video Board XE)** - 256 colors, enhanced graphics
- Phase 8: Modern hardware (Ultimate Cart, FPGA recreations)

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Atari 400/800/XL/XE base
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 6502 instruction set fundamentals (stock 6502, no illegal opcodes)
- **Binary load autoload (.XEX format) - Lesson 2-3, mandatory from Lesson 3**
- ANTIC basics (display lists, screen modes)
- GTIA basics (colors, player-missile graphics)
- Player-Missile Graphics (PMG) - 4 players + 4 missiles
- POKEY basics (sound effects, keyboard I/O)
- Display list fundamentals
- Joystick input (PORTA/STICK0)
- Vertical blank interrupt (VBI)

**Autoload Requirement:**
All games from Lesson 3 onwards must use efficient .XEX binary load format:
- Binary file header with load address
- Optional run address for auto-execution
- DOS automatically loads and runs
- Professional presentation: LOAD from DOS menu, game starts automatically
- No manual memory addresses typed by user

**Deliverables:** 16 complete, playable games with professional .XEX autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Atari 400/800/XL/XE
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized routines (zero-page, lookup tables)
- PMG multiplexing (>8 sprites on screen)
- Advanced display lists (mixed modes, scrolling)
- Horizontal/vertical scrolling (fine scroll registers)
- POKEY music sequencing (4 channels)
- Display List Interrupts (DLI) basics
- Advanced collision detection (PMG hardware collision)
- Multi-screen game structures

**Deliverables:** 16 games with commercial-quality features

---

### Phase 3: Advanced Display List Techniques
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** Atari XL/XE
**Complexity:** Professional optimization, complex display lists
**Games:** 5 revisited with advanced DLI, 3 new showcasing techniques

**Key Learning:**
- **Advanced Display List Interrupts (DLI)** - multiple per frame
- **Mode mixing** (text + graphics modes in single display)
- **Direct comparison:** "Here's your basic Snake. Now enhance with DLI color changes"
- GTIA advanced modes (9-16 color modes, 256 shades)
- Advanced PMG (5th player tricks, reuse)
- Complex scrolling (split-screen, parallax via DLI)
- Professional display list optimization
- Advanced POKEY (all 4 channels, music composition)

**Deliverables:** 8 games - 5 enhanced with DLI, 3 new showcasing advanced techniques

**Games Revisited with Advanced DLI:**
1. Snake III (DLI) - color cycling, status bar
2. Shooter III (DLI) - raster effects, parallax
3. Platformer III (DLI) - split-screen, smooth scrolling
4. Breakout III (DLI) - color bars, effects
5. One other from Phase 1-2

**New Advanced Games:**
6. Action RPG I (showcasing mixed modes)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Atari XL/XE (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Extreme PMG optimization (16+ sprites smooth)
- Complex display list chains
- Advanced scrolling techniques (coarse + fine scroll)
- POKEY music trackers integration
- Page flipping (double buffering)
- Disk I/O (SIO bus programming)
- Isometric projection
- Turn-based strategy mechanics

**Deliverables:** 8 games showcasing advanced Atari techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Atari XL/XE mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced POKEY music (tracker format)
- Disk-based save/load systems
- Multi-disk games

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Atari XL/XE (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous PMG sprites (extreme optimization)
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Advanced display list tricks
- Fast disk loaders (custom SIO routines)
- Cartridge-based games (memory banking)
- Professional Atari 8-bit development

**Deliverables:** 4 games pushing absolute limits of Atari 8-bit

---

### Phase 7: Enhanced Hardware (VBXE)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** VBXE (Video Board XE) expansion
**Complexity:** Large-scale games with enhanced graphics
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- VBXE programming (256 colors, enhanced graphics)
- Blitter operations (fast graphics)
- Hardware sprites (beyond PMG)
- Large frame buffers
- Enhanced display modes
- Backward compatibility (XL/XE vs VBXE)
- Large game worlds with enhanced graphics
- Commercial VBXE development

**Deliverables:** 2 commercial-scale VBXE-enhanced games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern (Ultimate Cart, FPGA recreations)
**Complexity:** Modern enhanced development, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Ultimate Cart features (SD card, USB)
- Modern development workflow
- FPGA recreations (cycle-accurate)
- Pushing Atari 8-bit absolute limits
- Modern storage (SD cards)
- Enhanced audio capabilities (where available)
- Commercial release preparation
- Portfolio capstone quality

**Deliverables:** 2 portfolio-ready commercial-quality games showcasing everything learned

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. Display List Programming**
- P1: Basic display lists (single mode screens)
- P2: Advanced display lists (mixed modes, scrolling)
- P3: **Display List Interrupts (DLI)** - color changes, effects
- P4: Complex DLI chains, extreme timing
- P5+: Professional display list techniques
- P7: VBXE display programming

**2. Player-Missile Graphics (PMG)**
- P1: Basic PMG (4 players + 4 missiles)
- P2: PMG multiplexing (>8 sprites)
- P3: Advanced PMG (5th player tricks, reuse)
- P4: Extreme multiplexing (16+ sprites)
- P5+: Maximum optimization (32+ sprites)
- P7: VBXE hardware sprites

**3. Scrolling Systems**
- P1: Character scrolling (coarse scroll)
- P2: Smooth scrolling (fine scroll registers)
- P3: Parallax via DLI, split-screen
- P4+: Complex scrolling systems
- P7: VBXE enhanced scrolling

**4. POKEY Programming**
- P1: Simple sound effects
- P2: Music sequencing (4 channels)
- P3: Advanced music composition
- P4: Music trackers integration
- P5+: Professional audio techniques

**5. Collision Detection**
- P1: PMG hardware collision ($D00C-$D00F)
- P2: Bounding box refinement
- P3: Advanced collision techniques
- P5+: Pixel-perfect collision

**6. Graphics Modes**
- P1: Basic ANTIC modes (text, basic graphics)
- P2: Mixed mode displays
- P3: GTIA advanced modes (9-16 colors, 256 shades)
- P4+: Complex mode combinations
- P7: **VBXE 256-color modes**

---

## Hardware Progression

### Atari 400/800/XL/XE Base (Phases 1-6)
**Characteristics:**
- 6502 CPU @ 1.79MHz (stock 6502, no illegal opcodes)
- 16KB-64KB RAM (XL/XE typically 64KB)
- ANTIC: Display list processor, screen modes
- GTIA: Graphics/color chip, player-missile graphics
- POKEY: 4-channel sound, keyboard/joystick I/O
- 4 players (PMG sprites, 8 pixels wide)
- 4 missiles (PMG sprites, 2 pixels wide)
- 128 colors (16 hues × 8 luminances)
- Display list system (programmable display)

**Model progression:**
- Atari 400 (1979): 8KB/16KB RAM, membrane keyboard
- Atari 800 (1979): 8KB-48KB RAM, full keyboard
- Atari 800XL (1983): 64KB RAM, built-in BASIC
- Atari 130XE (1985): 128KB RAM (64KB base + 64KB extended)

**Focus:** Master Atari 8-bit fundamentals
- ANTIC display list programming
- GTIA PMG system
- POKEY sound and I/O
- Display List Interrupts (DLI)
- Creative solutions within constraints

### VBXE - Video Board XE (Phase 7)
**Additional Features:**
- 512KB video RAM
- 256 colors on-screen (from 24-bit palette)
- Blitter (fast graphics operations)
- Hardware sprites (beyond PMG)
- Enhanced display modes
- Backward compatible with ANTIC/GTIA

**Focus:** Enhanced graphics capabilities
- 256-color graphics
- Blitter operations
- Large frame buffers
- Hardware sprite systems
- Professional visuals

### Modern Hardware (Phase 8)
**Ultimate Cart:**
- Cartridge emulation
- SD card storage
- USB connectivity

**FPGA Recreations:**
- Cycle-accurate Atari 8-bit cores
- Modern I/O
- Enhanced features

**Focus:** Modern development
- Commercial-quality games
- Modern storage and I/O
- Portfolio showcase

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (Basic)** (16 lessons)
- Basic grid movement (6502 fundamentals)
- Simple display list
- PMG for snake segments
- POKEY sound effects
- Basic colors

**Phase 2: Snake II (Optimized)** (32 lessons)
- PMG multiplexing (longer snake)
- Smooth scrolling playfield
- Multi-screen levels
- POKEY music
- Optimized routines

**Phase 3: Snake III (DLI Enhanced)** (64 lessons - REVISITED WITH DLI)
- **Display List Interrupts for color cycling**
- **Status bar via DLI**
- **Advanced GTIA modes**
- **Direct comparison:** "Here's your basic Snake. Now enhance with DLI effects."

**Phase 4: Snake IV (Advanced)** (64 lessons)
- Complex display list effects
- Advanced PMG techniques
- Page flipping
- Disk-based level sets

**Phase 6: Snake V** (128 lessons)
- 32+ simultaneous AI snakes
- Extreme optimization
- Commercial-quality

**Phase 7: Snake Ultimate (VBXE)** (if applicable)
- 256 colors
- Blitter graphics
- Hardware sprites

Students see evolution: Basic → Optimized → **DLI Enhanced** → Advanced → Professional → VBXE

---

## Key Differences from Other Platforms

**Atari 8-bit Advantages:**
- Display list system (programmable display)
- ANTIC (dedicated display processor)
- Player-Missile Graphics (hardware sprites)
- POKEY sound (4 channels)
- 6502 CPU (same family as C64, NES)

**Atari 8-bit Considerations:**
- PMG sprites limited (4 players + 4 missiles)
- Display list timing synchronization
- GTIA color limitations (128 colors standard)
- 6502 slightly slower than C64 (1.79MHz vs C64's effective speed)

**Similar To:**
- C64 (6502 CPU, BASIC gateway, custom chips)
- NES (6502 CPU, display list concept similar to PPU)

**Unique Features:**
- Display List Interrupts (powerful raster effects)
- ANTIC/GTIA architecture (different from VIC-II)
- POKEY sound (different from SID)

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
- Expected output defined
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 6502 Atari games from scratch
- Understands ANTIC, GTIA, POKEY, PMG
- Has 16 portfolio games

**Phase 3 Complete:**
- Student masters Display List Interrupts
- Can compare/contrast basic vs DLI-enhanced implementations
- Has both basic and DLI versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all hardware variants
- Masters Atari 8-bit through modern enhancements
- Can create commercial-release quality games
- Ready for professional Atari 8-bit development

---

## Resources Required

**Development Tools:**
- Assembler: MADS, ca65, MAC/65
- Emulator: Altirra (excellent debugging), Atari800
- Graphics: Graphics Explorer, Envision PC
- Audio: Raster Music Tracker (RMT), Chaos Music Composer
- Utilities: Various disk tools

**Reference Materials:**
- 6502 instruction set
- ANTIC reference (display lists, modes)
- GTIA reference (PMG, colors)
- POKEY reference (sound, I/O)
- Hardware documentation

**Testing:**
- Altirra/Atari800 emulators (development)
- Real hardware (verification)
- VBXE hardware (Phase 7)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - DLI introduced Phase 3
**Note:** Atari 8-bit has Phase 0 (Atari BASIC)
**Next Steps:** Create Atari 8-bit 8-PHASE-GAME-PROGRESSION.md with specific game mapping
