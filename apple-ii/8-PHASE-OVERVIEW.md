# Apple II Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** Apple IIe (64KB) → Apple IIGS introduced Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Phase 0 - Applesoft BASIC

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare IIe vs IIGS implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Page flipping is page flipping" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master Apple IIe (64KB, 6502 @ 1MHz)
- Phase 3: **Apple IIGS introduced** - 65C816, advanced graphics/sound, revisit games
- Phase 4-6: Advanced techniques, pushing IIGS limits
- Phase 7: **IIGS advanced features** - maximum capabilities
- Phase 8: Modern Apple II development

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Apple IIe (64KB base)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 6502 instruction set fundamentals
- **Applesoft BASIC loader - Lesson 2-3, mandatory from Lesson 3**
- Screen memory addressing (text, lo-res, hi-res)
- Graphics modes (text 40×24, lo-res 40×48, hi-res 280×192)
- Page flipping (double buffering via soft switches)
- Software sprite rendering (no hardware sprites)
- Keyboard input (KBD register $C000)
- Speaker output (1-bit audio via $C030)
- Interrupt timing (60Hz NTSC)

**Autoload Requirement:**
All games from Lesson 3 onwards must use efficient loader:
```basic
10 PRINT CHR$(4);"BRUN GAME"
```
Or for Applesoft inline:
```basic
10 HIMEM: 8192
20 D$ = CHR$(4)
30 PRINT D$;"BLOAD GAME,A$2000"
40 CALL 8192
```
Professional presentation: RUN from DOS/ProDOS, game starts automatically. No manual CALL commands typed by user.

**Deliverables:** 16 complete, playable Apple IIe games with professional autoload

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** Apple IIe (64KB)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 6502 routines (zero-page, lookup tables)
- Software sprite optimization (pre-shifted, EOR/XOR techniques)
- Hi-res graphics programming (280×192 monochrome, or 6 colors)
- Double hi-res (if available - 140×192×16 colors)
- Page flipping techniques (smooth animation)
- Speaker music (Mockingboard alternative - creative 1-bit)
- Advanced collision detection
- Multi-screen game structures

**Deliverables:** 16 games with commercial-quality Apple IIe features

---

### Phase 3: Advanced Graphics & Sound (Apple IIGS)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **Apple IIGS introduced** - 65C816, advanced graphics/sound
**Complexity:** Direct IIe→IIGS comparison, professional optimization
**Games:** 5 revisited from Phases 1-2 with IIGS, 3 new showcasing features

**Key Learning:**
- **65C816 CPU programming** (16-bit, backward compatible with 6502)
- **Super Hi-Res graphics** (320×200×16 colors, 640×200×4 colors, 320×200×256 colors)
- **Ensoniq DOC sound** (32 oscillators, wavetable synthesis)
- **Direct comparison:** "Here's your IIe Snake. Now enhance it with IIGS graphics and sound"
- Mega II chip (IIe compatibility)
- Super Hi-Res addressing and palettes
- Wavetable audio programming
- Professional IIe optimization (for games staying on IIe)

**Deliverables:** 8 games - 5 IIGS versions of earlier games, 3 new showcasing IIGS

**Games Revisited with IIGS:**
1. Snake III (IIGS) - Super Hi-Res graphics, Ensoniq sound
2. Shooter III (IIGS) - 16-color graphics, wavetable music
3. Platformer III (IIGS) - Super Hi-Res scrolling, DOC audio
4. Breakout III (IIGS) - enhanced visuals, professional sound
5. One other from Phase 1-2

**New IIGS Games:**
6. Action RPG I (showcasing Super Hi-Res + DOC)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Apple IIGS (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced 65C816 programming (16-bit operations, long addressing)
- Super Hi-Res optimization (all modes)
- Advanced Ensoniq programming (32-channel mixing)
- Scrolling techniques (hardware limitations)
- GS/OS programming (file system)
- Disk I/O (ProDOS/GS/OS)
- Isometric projection
- Turn-based strategy mechanics

**Deliverables:** 8 games showcasing advanced IIGS techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Apple IIGS mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced Ensoniq music composition
- Disk-based save/load systems
- Multi-disk games

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Apple IIGS (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 32+ simultaneous software sprites
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 65C816 optimization
- Fast disk loaders (custom routines)
- Large-scale IIGS games (8MB RAM)
- Professional IIGS development

**Deliverables:** 4 games pushing absolute limits of Apple IIGS

---

### Phase 7: Enhanced Hardware Features
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** Apple IIGS (maximum capabilities) / TransWarp accelerators
**Complexity:** Large-scale games using all IIGS features
**Games:** 2 epic games (large RPG, grand strategy/adventure)

**Key Learning:**
- IIGS maximum RAM (8MB)
- TransWarp GS accelerator (16MHz 65C816)
- Advanced Super Hi-Res techniques
- Maximum Ensoniq capabilities
- AppleTalk networking (multiplayer)
- Large game worlds
- Advanced GS/OS programming
- Commercial IIGS development

**Deliverables:** 2 commercial-scale Apple IIGS games

---

### Phase 8: Pinnacle
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern Apple II development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern Apple II development workflow
- Emulator debugging (AppleWin, MAME, GSplus)
- Pushing IIGS absolute limits
- Modern storage (hard drives, SD cards, flash)
- Cross-development (modern assemblers)
- Commercial release preparation
- Portfolio capstone quality
- Modern Apple II community standards

**Deliverables:** 2 portfolio-ready commercial-quality Apple II games showcasing everything learned

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. Screen Mode Management**
- P1: Text/Lo-Res/Hi-Res basics (IIe)
- P2: Page flipping, double buffering
- P3: **Super Hi-Res (IIGS - 320×200×16/256 colors)**
- P4: Advanced SHR techniques
- P5+: Complex graphics systems

**2. Sprite Rendering**
- P1: Simple software sprites (IIe)
- P2: Pre-shifted sprites, EOR/XOR techniques
- P3: IIGS Super Hi-Res sprites (faster, more colors)
- P4: Optimized sprite systems
- P5+: Multi-sprite management (32+ sprites)

**3. Scrolling Systems**
- P1: Screen-aligned scrolling (page flipping)
- P2: Software pixel scrolling (limited on IIe)
- P3: IIGS Super Hi-Res scrolling
- P4: Advanced scrolling techniques
- P5+: Complex scrolling (parallax)

**4. Graphics Modes**
- P1: Hi-Res graphics (280×192, 6 colors)
- P2: Double Hi-Res (140×192×16 - if available)
- P3: **Super Hi-Res (IIGS - multiple modes)**
- P4: Advanced mode usage
- P5+: Complex graphics

**5. Sound Programming**
- P1: Speaker clicks (1-bit audio)
- P2: Speaker music (creative techniques)
- P3: **Ensoniq DOC (IIGS - wavetable)**
- P4: Advanced Ensoniq (32 oscillators)
- P5+: Professional audio (tracker format)

**6. Collision Detection**
- P1: Bounding box collision
- P2: Pixel-perfect (check screen memory)
- P3: IIGS optimized collision
- P5+: Multi-layer collision

**7. Memory Management**
- P1: Basic RAM usage (64KB IIe)
- P2: Efficient data structures
- P3: **IIGS bank switching** (256KB-8MB)
- P4: Complex banking strategies
- P5+: Large game data management

**8. Disk I/O**
- P3: ProDOS/GS/OS file operations
- P4: Advanced disk access
- P5: Disk-based game structure
- P6: Fast loaders
- P8: Modern storage (SD cards)

---

## Hardware Progression

### Apple IIe (Phases 1-2)
**Platform:** Apple IIe (1983), IIe Enhanced (1985)
**Characteristics:**
- 6502 CPU @ 1MHz (Enhanced: 65C02)
- 64KB RAM (IIe), 128KB RAM (Enhanced)
- Text: 40×24 (80×24 with 80-column card)
- Lo-Res: 40×48, 16 colors
- Hi-Res: 280×192, 6 colors (or monochrome)
- Double Hi-Res: 140×192×16 (with 128KB)
- Speaker: 1-bit audio (creative programming required)
- Optional: Mockingboard (6 voices, rare)
- DOS 3.3 or ProDOS
- 60Hz NTSC

**Focus:** Master Apple IIe fundamentals
- 6502 programming
- Hi-Res graphics techniques
- Page flipping (double buffering)
- Speaker audio creativity
- Software sprite rendering
- Creative solutions within constraints

### Apple IIGS (Phase 3+)
**Platform:** Apple IIGS (1986)
**Introduced Phase 3**
**Enhanced Features:**
- **65C816 CPU @ 2.8MHz** (16-bit, 6502-compatible)
- **Super Hi-Res graphics:**
  - 320×200, 16 colors (from 4096 palette)
  - 320×200, 256 colors (from 4096 palette)
  - 640×200, 4 colors (from 4096 palette)
  - Multiple fill modes
- **Ensoniq DOC sound chip** (32 oscillators, wavetable)
- 256KB-8MB RAM (bank switched)
- Mega II chip (full IIe hardware compatibility)
- GS/OS operating system (advanced)
- 3.5" floppy drive, hard drive support
- **Direct comparison:** IIe vs IIGS graphics/sound

**Focus:** Leverage IIGS enhancements
- 65C816 16-bit programming
- Super Hi-Res graphics (all modes)
- Ensoniq wavetable audio
- Bank switching (large games)
- Professional visuals/audio

### IIGS Enhanced (Phase 7)
**Additional capabilities:**
- Maximum 8MB RAM
- TransWarp GS accelerator (16MHz)
- AppleTalk networking
- Advanced GS/OS features

### Modern Development (Phase 8)
**Modern Tools:**
- Emulators (AppleWin, MAME, GSplus, Virtual II)
- Cross-assemblers (Merlin32, cc65, ca65)
- Modern storage (CF cards, SD cards, CFFA3000)
- Modern Apple II hardware (Laser 128, clones)

**Focus:** Modern workflow
- Commercial-quality games
- Modern development tools
- Portfolio showcase
- Community release

---

## Spiral Learning Example: Snake

**Phase 1: Snake I (Apple IIe)** (16 lessons)
- Basic grid movement (6502 fundamentals)
- Hi-Res graphics (280×192)
- Page flipping
- Speaker clicks
- 64KB RAM

**Phase 2: Snake II (IIe optimized)** (32 lessons)
- Optimized sprite routines
- Speaker music
- Double Hi-Res (if available)
- Multi-screen levels
- Optimized IIe

**Phase 3: Snake III (IIGS)** (64 lessons - REVISITED WITH IIGS)
- **Super Hi-Res graphics** (320×200×16 colors)
- **Ensoniq DOC sound** (wavetable music)
- **65C816 optimization**
- **Direct comparison:** "Here's your IIe Snake. Now enhance it with IIGS Super Hi-Res and Ensoniq"

**Phase 4: Snake IV (Advanced IIGS)** (64 lessons)
- Advanced Super Hi-Res techniques
- Multi-channel Ensoniq
- Bank-switched worlds
- Disk-based levels

**Phase 6: Snake V (IIGS limits)** (128 lessons)
- 32+ simultaneous AI snakes
- Extreme 65C816 optimization
- Commercial-quality
- Pushing IIGS limits

Students see evolution: IIe basics → IIe optimized → **IIGS enhanced** → Advanced → Professional

---

## Key Differences from Other Platforms

**Apple II Advantages:**
- Very influential platform (1977-1993 production)
- Excellent Applesoft BASIC (easy BASIC-to-assembly transition)
- IIGS: 65C816 (16-bit CPU, very capable)
- IIGS: Ensoniq DOC (excellent sound)
- Large software library and community
- Educational legacy

**Apple II Considerations:**
- IIe: Limited graphics (Hi-Res 6 colors, color clash)
- IIe: 1-bit speaker audio (very limited)
- No hardware sprites (software rendering)
- IIGS less common than IIe
- Color display needed (composite or RGB)

**Similar To:**
- Commodore 64 (6502 family, similar era)
- Atari 8-bit (6502 CPU)
- BBC Micro (6502 CPU)

**Unique Features:**
- IIGS 65C816 CPU (16-bit, powerful)
- IIGS Ensoniq DOC (32 oscillators)
- Page flipping via soft switches
- IIe longevity (very long production run)

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
- Expected output defined (IIe and IIGS where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 6502 Apple II games from scratch
- Understands Hi-Res graphics, page flipping, speaker audio
- Has 16 portfolio Apple IIe games

**Phase 3 Complete:**
- Student masters IIGS 65C816 and Super Hi-Res
- Can compare/contrast IIe vs IIGS implementations
- Has both IIe and IIGS versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games across all Apple II variants
- Masters IIe and IIGS
- Can create commercial-release quality games
- Ready for professional Apple II development

---

## Resources Required

**Development Tools:**
- Assembler: Merlin32, ca65, cc65
- BASIC: Applesoft BASIC
- Emulator: AppleWin (Windows), MAME, GSplus, Virtual II
- Graphics: Super Convert, various utilities
- Audio: SoundSmith (IIGS), tracker tools
- Utilities: CiderPress, ADTPro, disk image tools

**Reference Materials:**
- 6502/65C02/65C816 instruction set
- Apple II Reference Manual
- IIe Technical Reference
- IIGS Hardware Reference
- IIGS Firmware Reference
- Ensoniq DOC reference

**Testing:**
- Emulators (development)
- Real Apple II hardware (verification)
- Apple IIGS (Phase 3+)
- Modern storage interfaces

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - IIGS introduced Phase 3
**Note:** Apple II has Phase 0 (Applesoft BASIC)
**Next Steps:** Create Apple II 8-PHASE-GAME-PROGRESSION.md with specific game mapping
