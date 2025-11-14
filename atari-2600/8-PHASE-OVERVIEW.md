# Atari 2600 Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** 2600 base (4KB) → Bank switching introduced Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Direct assembly (no BASIC - console platform)
**Historical Note:** "1977 trinity" console (2600, Fairchild Channel F, Magnavox Odyssey²), 30M units sold
**Extreme Constraint:** Only 128 bytes of RAM (most constrained platform in curriculum!)

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare 4KB vs bank-switched implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "TIA racing the beam is TIA racing the beam" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres (within extreme constraints)
- Not recreating specific classic games (though students learn their techniques)
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master 2600 base (128B RAM, 4KB ROM, TIA racing the beam)
- Phase 3: **Bank switching introduced** - 8KB+ games, advanced techniques
- Phase 4-6: Advanced techniques, pushing 2600 limits
- Phase 7: **Maximum 2600** - all tricks, professional development
- Phase 8: Modern 2600 development (homebrew scene)

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Atari 2600 base (6507 @ 1.19MHz, 128B RAM, 4KB ROM)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 6507 instruction set fundamentals (6502 variant, 13-bit address bus)
- **Only 128 bytes of RAM** (extreme constraint - most constrained in curriculum!)
- **4KB ROM cartridge** (base game size)
- **TIA chip** (Television Interface Adapter - graphics/sound/input)
- **"Racing the beam"** (no frame buffer - must update display in real-time!)
- **2 player sprites** (8 pixels wide each)
- **2 missiles** (1 pixel wide)
- **1 ball** (1-4 pixels)
- **Playfield** (40 pixels wide, mirrored or repeated)
- **2-channel sound** (TIA audio)
- RIOT chip (128B RAM, timers, I/O)
- Joystick input (1 button + 4 directions)
- **No operating system** (direct hardware programming)
- 60Hz NTSC / 50Hz PAL

**No Autoload - Direct Boot:**
Cartridge inserted = game runs immediately. No loader required.

**Deliverables:** 16 complete, playable 2600 games (4KB each)

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** 2600 base (128B RAM, 4KB ROM)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 6507 code (extreme memory constraints)
- Advanced TIA techniques (racing the beam mastery)
- Sprite/playfield tricks (reuse, flicker, multiplexing)
- **Kernel development** (display kernel optimization)
- **Scanline timing** (cycle-perfect programming)
- Advanced collision detection (TIA hardware collision)
- Multi-screen game structures (within 128B RAM!)
- TIA audio programming (2-channel creative usage)
- **4KB optimization** (fitting games in tiny ROM)

**Deliverables:** 16 games with commercial-quality 2600 features (4KB)

---

### Phase 3: Bank Switching & Advanced Techniques
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** **Bank switching introduced** - 8KB, 16KB, 32KB games
**Complexity:** Direct 4KB→bank-switched comparison, advanced TIA mastery
**Games:** 5 revisited from Phases 1-2 with bank switching, 3 new showcasing techniques

**Key Learning:**
- **Bank switching** (F8, F6, F4 schemes - access more ROM)
- **8KB, 16KB, 32KB games** (vs 4KB base)
- **Direct comparison:** "Here's your 4KB game. Now expand it with bank switching"
- Advanced kernel techniques (more complex display routines)
- Advanced sprite tricks (sprite duplication, 6+ sprites)
- Advanced playfield manipulation
- Advanced TIA audio (all capabilities)
- Professional 4KB optimization (for games staying small)
- **Still only 128B RAM!** (bank switching doesn't add RAM)

**Deliverables:** 8 games - 5 enhanced bank-switched versions, 3 new showcasing mastery

**Games Revisited with Bank Switching:**
1. Snake III (Bank-switched) - more levels, better graphics
2. Shooter III (Bank-switched) - multiple stages, complex enemies
3. Platformer III (Bank-switched) - larger world, more detail
4. Breakout III (Bank-switched) - advanced effects, more levels
5. One other from Phase 1-2

**New Bank-Switched Games:**
6. Action RPG I (showcasing 16KB+ ROM, complex game logic)
7. Advanced game type
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** Bank-switched 2600 (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced bank switching (F4, F8, custom schemes)
- Maximum sprite techniques (6+ sprites, flicker minimization)
- Advanced kernel programming (cycle-perfect optimization)
- Complex playfield manipulation (asymmetric, scrolling)
- Advanced TIA audio (all channels, effects)
- Advanced collision detection (hardware + software hybrid)
- **Still 128B RAM!** (creative data management)
- Large game structures (16KB-32KB ROMs)

**Deliverables:** 8 games showcasing advanced 2600 techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** Bank-switched 2600 mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large adventure, shooter, platformer, puzzle)

**Key Learning:**
- Large-scale game architecture (within 128B RAM constraint!)
- Quest systems and narrative (Adventure-style games)
- Complex enemy AI (within constraints)
- Advanced visual techniques (all TIA tricks)
- Advanced audio composition (2-channel mastery)
- Multi-bank game structure (32KB+ games)
- **Creative 128B RAM usage** (every byte matters!)

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** Bank-switched 2600 (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 6+ simultaneous sprites (flicker optimization)
- Complex multi-character systems (within 128B RAM!)
- Advanced game mechanics (pushing what's possible)
- Commercial polish techniques
- Extreme 6507 optimization
- Pushing 2600 absolute limits
- Professional 2600 development
- **128B RAM mastery** (ultimate constraint programming)

**Deliverables:** 4 games pushing absolute limits of 2600

---

### Phase 7: Maximum 2600
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** 2600 (all capabilities, all tricks)
**Complexity:** Large-scale games with maximum techniques
**Games:** 2 epic games (large adventure, complex action game)

**Key Learning:**
- All TIA tricks (every technique mastered)
- All bank-switching schemes (custom mappers)
- Maximum 6507 efficiency
- Large game worlds (within 128B RAM constraint!)
- Commercial 2600 development
- Professional quality polish
- **Historical techniques** (learning from classic games)

**Deliverables:** 2 commercial-scale 2600 games

---

### Phase 8: Pinnacle (Modern Homebrew)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern 2600 development (homebrew scene)
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (shooter, platformer using all techniques)

**Key Learning:**
- Modern 2600 development workflow
- Emulator debugging (Stella, excellent 2600 emulator)
- Modern homebrew techniques (community innovations)
- Custom cartridge hardware (modern mappers, extra RAM - rare)
- Cross-development (modern assemblers: DASM, ca65)
- Commercial release preparation (AtariAge, homebrew market)
- Portfolio capstone quality
- **Historical significance:** Active homebrew scene, 30M units sold

**Deliverables:** 2 portfolio-ready commercial-quality 2600 games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 6507 Programming**
- P1: Basic instructions (6502 variant, 13-bit address)
- P2: Advanced 6507 techniques (extreme optimization)
- P3: Bank-switched 6507 (code in multiple banks)
- P4: Complex 6507 techniques
- P5+: Extreme optimization (cycle-counting critical!)

**2. TIA Programming (Racing the Beam)**
- P1: TIA basics (display kernel, racing the beam)
- P2: Advanced TIA (kernel optimization)
- P3: Bank-switched kernels (more complex displays)
- P4: Maximum TIA capabilities
- P5+: All TIA tricks (professional techniques)

**3. Sprite Management**
- P1: 2 player sprites (TIA hardware)
- P2: Sprite positioning, tricks
- P3: 6+ sprites (multiplexing, flicker)
- P4: Advanced sprite techniques
- P5+: Maximum sprites (minimizing flicker)

**4. Playfield Programming**
- P1: Basic playfield (40 pixels, mirrored/repeated)
- P2: Playfield manipulation (asymmetric, tricks)
- P3: Advanced playfield (scrolling, complex)
- P5+: All playfield techniques

**5. Sound Programming**
- P1: TIA audio basics (2-channel)
- P2: Music composition (creative 2-channel)
- P3: Advanced TIA audio (all effects)
- P5+: Professional audio (within limitations)

**6. Memory Management**
- P1: **128 bytes RAM** (extreme constraint!)
- P2: Efficient data structures (every byte counts)
- P3: **Still 128B RAM!** (bank switching adds ROM, not RAM)
- P4: Creative RAM usage (overlapping data, tricks)
- P5+: Ultimate 128B mastery (most constrained programming)

**7. Bank Switching**
- P3: **Bank switching introduction** (F8, F6 schemes)
- P4: Advanced bank switching (F4, custom)
- P5: Multi-bank game architecture
- P7: Custom mappers (ultimate control)

**8. Collision Detection**
- P1: TIA hardware collision (built-in)
- P2: Collision optimization
- P3: Advanced collision (software + hardware)
- P5+: Complex collision systems

---

## Hardware Progression

### Atari 2600 Base (Phases 1-2)
**Platform:** Atari 2600 (1977)
**Characteristics:**
- **6507 CPU @ 1.19MHz** (6502 variant, 13-bit address bus, 8KB address space)
- **128 bytes RAM** (RIOT chip - extreme constraint!)
- **4KB ROM cartridge** (base game size)
- **TIA chip** (Television Interface Adapter):
  - **2 player sprites** (8 pixels wide, single-color per scanline)
  - **2 missiles** (1 pixel wide)
  - **1 ball** (1-4 pixels)
  - **Playfield** (40 pixels wide, mirrored or repeated)
  - **2-channel sound** (limited but creative)
- **"Racing the beam"** (no frame buffer! Must update display in real-time)
- **Hardware collision detection** (TIA built-in)
- **RIOT chip** (RAM-I/O-Timer):
  - 128 bytes RAM
  - Timers
  - Joystick input (2 ports, 1 button + 4 directions)
- 160×192 resolution (NTSC)
- 128 colors (but limited per scanline)

**Focus:** Master extreme constraints
- 6507 programming (6502 variant)
- **128 bytes RAM** (ultimate constraint!)
- TIA racing the beam (no frame buffer)
- Cycle-perfect programming (timing critical)
- 4KB ROM limits (tiny games)

**Historical Context:**
- Console market pioneer (1977)
- Massive success (30 million units)
- "1977 trinity" console (2600, Channel F, Odyssey²)
- Video game crash 1983 (too many bad games)
- Discontinued 1992 (15-year lifespan!)
- Launched console gaming as industry
- Most constrained hardware (teaches extreme optimization)

**Why 128B RAM is Extreme:**
- Variables: ~20-40 bytes
- Stack: ~20 bytes
- Sprite positions: ~10 bytes
- Playfield data: ~20-40 bytes
- Game logic: Remaining bytes!
- **Every byte planned meticulously**

### Bank Switching (Phase 3+)
**Introduced Phase 3**
**Enhanced Features:**
- **8KB, 16KB, 32KB ROM** (vs 4KB)
- **Multiple ROM banks** (switched at runtime)
- **Common bank-switching schemes:**
  - F8 (8KB, two 4KB banks)
  - F6 (16KB, four 4KB banks)
  - F4 (32KB, eight 4KB banks)
- **Still only 128B RAM!** (bank switching adds ROM, not RAM)
- More complex games possible
- Multiple levels/stages
- Better graphics/audio data

**Focus:** Leverage more ROM
- Bank-switching techniques
- Multi-bank game structure
- More complex games (still 128B RAM!)
- Code organization across banks

**Why Bank Switching Matters:**
- Commercial games needed it (4KB too small)
- Classic games: Pitfall II, Adventure (later), many others
- Required for large games
- Still extremely constrained (vs other platforms)

### Modern 2600 (Phase 8)
**Modern enhancements:**
- **Stella emulator** (excellent, cycle-accurate)
- Modern assemblers (DASM, ca65)
- **Active homebrew scene** (AtariAge community)
- Custom cartridges (modern mappers, extra RAM - rare)
- Harmony/Melody carts (modern flash carts)

**Focus:** Modern workflow
- Homebrew development
- Modern tools
- Portfolio showcase
- Historical appreciation

---

## Spiral Learning Example: Breakout

**Phase 1: Breakout I (2600 base, 4KB)** (16 lessons)
- Basic ball physics (6507 fundamentals)
- Playfield bricks (TIA playfield)
- Paddle sprite (TIA player0)
- Ball sprite (TIA ball)
- **128 bytes RAM** (brick states, positions, score)

**Phase 2: Breakout II (2600 optimized, 4KB)** (32 lessons)
- Optimized kernel (racing the beam)
- Better collision detection (TIA hardware)
- Audio effects (TIA 2-channel)
- Multi-screen levels (within 128B RAM!)

**Phase 3: Breakout III (Bank-switched, 16KB)** (64 lessons - BANK SWITCHING)
- **16KB ROM** (vs 4KB)
- **Multiple level sets** (stored in ROM)
- **More complex brick patterns**
- **Better audio** (more sound data in ROM)
- **Direct comparison:** "Here's your 4KB Breakout. Now expand it with bank switching"
- **Still only 128B RAM!**

**Phase 4: Breakout IV (Advanced, 32KB)** (64 lessons)
- Advanced kernel (complex display)
- Power-ups (within RAM constraint!)
- Advanced collision (pixel-perfect)
- Professional polish

**Phase 6: Breakout V (2600 limits)** (128 lessons)
- All TIA tricks (maximum visual quality)
- Extreme optimization
- Commercial-quality
- Pushing 2600 limits

Students see evolution: 4KB basics → 4KB optimized → **Bank-switched expanded** → Advanced → Professional

---

## Key Differences from Other Platforms

**2600 Unique Challenges:**
- **128 bytes RAM** (vs 4KB+ on most platforms - extreme!)
- **Racing the beam** (no frame buffer - must draw in real-time)
- **Cycle-perfect timing** (display must be precise)
- **4KB base ROM** (vs 16KB-64KB typical)
- **No operating system** (direct hardware)
- **2 sprites** (vs 8-128 on other platforms)
- **40-pixel playfield** (vs full-screen graphics)

**2600 Advantages:**
- Hardware collision detection (TIA built-in)
- Simple architecture (easy to understand)
- Historical significance (launched console gaming)
- Active homebrew scene (still active today!)
- Forces extreme optimization skills
- Teaches constraint-based programming

**Learning Path:**
- 2600 → NES/SMS (see evolution)
- 6507 → 6502 (same instruction set, more address space)
- Constraint programming transfers everywhere

**Same Pattern Library Concepts:**
- 6502 assembly (6507 = 6502 variant)
- Collision detection algorithms
- Physics systems
- Game design patterns
- All transferable skills (with less constraints!)

---

## Assessment Strategy

**No self-directed work** - every tier is fully specified:
- Complete lesson breakdown (4-64 arcs × 4 lessons)
- Full code examples provided
- Expected output defined (4KB and bank-switched where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 6507 2600 games from scratch
- Understands TIA (racing the beam, sprites, playfield)
- **Masters 128B RAM constraint** (extreme optimization)
- Has 16 portfolio 2600 games (4KB)

**Phase 3 Complete:**
- Student masters bank switching (8KB-32KB games)
- Can compare/contrast 4KB vs bank-switched implementations
- Has both 4KB and bank-switched versions of key games
- **Still works within 128B RAM!**

**Phase 8 Complete:**
- Student has 60 portfolio games showcasing 2600
- Masters 6507 architecture (6502 variant)
- Masters TIA (all tricks, all techniques)
- **Ultimate 128B RAM mastery** (most constrained programming)
- Can create commercial-release quality games
- Ready for professional 2600 homebrew development
- **6502 expertise** transfers to NES, C64, Apple II, etc.

---

## Resources Required

**Development Tools:**
- Assembler: DASM (standard for 2600), ca65
- Emulator: Stella (excellent, cycle-accurate, debugger)
- Graphics: 2600 sprite/playfield editors
- Utilities: ROM builders, cartridge tools

**Reference Materials:**
- 6507 instruction set (6502 variant)
- TIA Programming Guide (racing the beam)
- Stella Programmer's Guide
- 2600 memory map
- Bank-switching schemes reference

**Testing:**
- Stella emulator (development, cycle-accurate)
- Real 2600 hardware (verification)
- Harmony/Melody cart (modern flash cart for testing)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Bank switching introduced Phase 3
**Note:** No Phase 0 (console - no BASIC, direct assembly)
**Historical Note:** "1977 trinity" console, 30M units sold, launched console gaming industry
**Extreme Constraint:** **Only 128 bytes RAM** (most constrained platform in entire curriculum!)
**Key Technique:** **Racing the beam** (no frame buffer - real-time display generation)
**Unique Learning:** Ultimate constraint programming - every byte matters, cycle-perfect timing
**Next Steps:** Create 2600 8-PHASE-GAME-PROGRESSION.md with specific game mapping
