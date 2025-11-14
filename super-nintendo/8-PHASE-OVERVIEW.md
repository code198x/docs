# Super Nintendo (SNES) Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** SNES base → Mode 7 + Enhancement chips Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Direct assembly (no BASIC - console platform)
**Historical Note:** Genesis competitor (1990-2003), 49M units sold, winner of 16-bit console war
**Signature Feature:** **Mode 7** (scaling/rotation), **Enhancement chips**, **HDMA**

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare basic vs Mode 7 vs Enhancement chip implementations
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "Mode 7 transformations are Mode 7 transformations" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games (though students learn their techniques)
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master SNES base (65816, PPU, 8-channel audio)
- Phase 3: **Mode 7 + Enhancement chips mastery** - scaling/rotation, coprocessors
- Phase 4-6: Advanced techniques, pushing SNES limits
- Phase 7: **Maximum SNES** - all capabilities, all enhancement chips
- Phase 8: Modern SNES development (homebrew scene)

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Super Nintendo base (65816 @ 3.58MHz, 128KB RAM)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- 65816 instruction set fundamentals (16-bit, WDC 65C816 - 6502 evolution!)
- **128KB main RAM** (vs Genesis's 64KB, vs 8-bit consoles' much less)
- **64KB VRAM** (video memory)
- **PPU** (Picture Processing Unit - sophisticated graphics chip):
  - 256×224 resolution (32×28 tiles, 8×8 or 16×16 tiles)
  - **128 hardware sprites** (64 large + 64 small, vs Genesis's 80)
  - **256 colors on-screen** (from palette of 32,768 - vs Genesis's 64 from 512!)
  - **4 background layers** (BG1, BG2, BG3, BG4 - independent scrolling)
  - 8 graphics modes (Mode 0-7, including signature Mode 7!)
  - Tile-based graphics (8×8 or 16×16 tiles)
  - Hardware scrolling (per-layer, smooth)
  - Priority system (layering control)
- **DMA** (Direct Memory Access - fast transfers)
- **HDMA** (Horizontal DMA - per-scanline effects, SNES exclusive!)
- **8-channel sample-based audio** (S-SMP @ 1.024MHz + S-DSP):
  - 64KB audio RAM
  - BRR sample format (compressed samples)
  - High-quality audio (vs Genesis's FM synthesis - different approach)
- Controller input (4-6 buttons + D-pad, 2 ports, expandable to 5 players)
- **No operating system** (direct hardware programming)
- 60Hz NTSC / 50Hz PAL

**No Autoload - Direct Boot:**
Cartridge inserted = game runs immediately. No loader required.

**Deliverables:** 16 complete, playable SNES games

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** SNES base (65816 @ 3.58MHz, 128KB RAM)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized 65816 code (16-bit/8-bit mode switching, efficient)
- Advanced PPU programming (4 backgrounds, all capabilities)
- **128 sprites optimization** (smooth movement, priority)
- Sprite multiplexing (more than 128 visible)
- Advanced scrolling (per-layer, independent, smooth)
- **HDMA basics** (per-scanline effects - powerful!)
- **8-channel sample audio** (S-SMP programming, BRR samples)
- Advanced collision detection (software-based)
- Multi-screen game structures
- **128KB main RAM + 64KB VRAM + 64KB audio RAM management**
- Graphics modes (Mode 0-6, preparing for Mode 7)

**Deliverables:** 16 games with commercial-quality SNES features

---

### Phase 3: Mode 7 & Enhancement Chips Mastery
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** SNES Mode 7 + Enhancement chips (Super FX, SA-1, DSP, etc.)
**Complexity:** Direct basic→Mode 7/Enhancement comparison, mastery
**Games:** 5 revisited from Phases 1-2 with Mode 7, 3 new showcasing enhancement chips

**Key Learning:**
- **Mode 7** (signature SNES feature - scaling/rotation graphics!):
  - Affine transformations (rotate, scale, shear, perspective)
  - Background scaling/rotation (single layer)
  - Pseudo-3D effects (F-Zero, Mario Kart, Pilotwings style)
  - Mode 7 + sprites (simulating 3D)
  - HDMA + Mode 7 (per-scanline transformations, advanced effects)
  - All Mode 7 capabilities
- **Enhancement chips** (cartridge-based coprocessors - SNES unique!):
  - **Super FX** (GSU - Graphics Support Unit):
    - 10.5-21.4MHz RISC processor
    - 3D polygon rendering (Star Fox, Yoshi's Island)
    - Custom instruction set
  - **SA-1** (65816 @ 10.74MHz):
    - 3× faster CPU!
    - 2KB I-RAM (fast work RAM)
    - MMC (Memory Management Controller)
    - DMA controller
    - Super Mario RPG, Kirby's Dream Land 3
  - **DSP** chips (DSP-1 to DSP-4):
    - Math coprocessor (multiply, divide, matrix operations)
    - NEC µPD77C25 (DSP-1)
    - Pilotwings, Super Mario Kart
  - **S-DD1** (compression chip):
    - Graphics decompression
    - Star Ocean, Street Fighter Alpha 2
  - **SPC7110** (decompression + RTC):
    - Data decompression
    - Real-time clock
    - Far East of Eden Zero, Tengai Makyou Zero
  - **CX4** (Hitachi HG51B169):
    - Wireframe 3D (Mega Man X2, X3)
  - **OBC1** (sprite protection/positioning)
- **Direct comparison:** "Here's your basic game. Now add Mode 7 scaling/rotation"
- Advanced HDMA (per-scanline Mode 7 modifications, wave effects)
- Professional SNES development (enhancement chips, Mode 7)
- Comparing basic SNES vs Mode 7 vs Enhancement chips

**Deliverables:** 8 games - 5 Mode 7 versions, 3 new showcasing enhancement chips

**Games Revisited with Mode 7:**
1. Snake III (Mode 7) - rotating playfield, perspective effects
2. Shooter III (Mode 7) - pseudo-3D backgrounds (Space Harrier style)
3. Platformer III (Mode 7) - rotation effects, pseudo-3D sections
4. Racer I (Mode 7) - F-Zero/Mario Kart style racing (signature Mode 7!)
5. One other from Phase 1-2

**New Enhancement Chip Games:**
6. 3D Action I (Super FX - Star Fox style polygon 3D)
7. Advanced RPG I (SA-1 - enhanced CPU, complex systems)
8. Advanced game type (DSP - math coprocessor usage)

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** SNES (pushing limits, all features)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced 65816 optimization (3.58MHz maximum efficiency, 16-bit/8-bit switching)
- Maximum PPU utilization (4 backgrounds, all 8 modes)
- Advanced Mode 7 (all transformations, HDMA combination)
- Advanced enhancement chips (Super FX, SA-1, DSP mastery)
- Maximum sprite utilization (128 sprites + multiplexing)
- **HDMA mastery** (per-scanline effects, complex transformations)
- Advanced audio (8 channels, BRR samples, all S-DSP features)
- DMA optimization (fast VRAM/audio RAM transfers)
- Advanced collision detection
- Isometric projection
- Turn-based strategy mechanics

**Deliverables:** 8 games showcasing advanced SNES techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** SNES mastery (all capabilities)
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative (RPG systems)
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced audio composition (8-channel, BRR samples mastery)
- Mode 7 game worlds (pseudo-3D environments)
- Enhancement chip optimization (Super FX 3D, SA-1 speed)
- Large game worlds (cartridge ROM banking if needed)
- Multi-cartridge games (rare but possible)

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** SNES (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 128+ simultaneous sprites (multiplexing mastery)
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme 65816 optimization
- Extreme enhancement chip optimization (Super FX, SA-1 maximum)
- HDMA maximum capabilities (complex per-scanline effects)
- Mode 7 maximum capabilities (all transformations perfected)
- Pushing SNES limits
- Professional SNES development

**Deliverables:** 4 games pushing absolute limits of SNES

---

### Phase 7: Maximum SNES
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** SNES (all capabilities, all enhancement chips)
**Complexity:** Large-scale games with maximum features
**Games:** 2 epic games (large RPG with SA-1, 3D action with Super FX)

**Key Learning:**
- All PPU capabilities (4 backgrounds, all 8 modes, Mode 7 mastery)
- All enhancement chips (Super FX, SA-1, DSP, S-DD1, all types)
- All HDMA capabilities (maximum per-scanline effects)
- All audio capabilities (8 channels, BRR mastery)
- Large game worlds (Mode 7 + enhancement chips)
- Advanced graphics techniques (all PPU features)
- Commercial SNES development (professional quality)
- Maximum SNES capabilities

**Deliverables:** 2 commercial-scale SNES games (maximum capabilities)

---

### Phase 8: Pinnacle (Modern Homebrew)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern SNES development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (Mode 7 racer, Super FX shooter)

**Key Learning:**
- Modern SNES development workflow
- Emulator debugging (bsnes-plus, Mesen-S, Snes9x, higan/ares)
- Modern homebrew techniques
- Modern assemblers (WLA-DX, bass, ca65)
- Modern toolchains (SNES development kits)
- Cross-development (modern tools)
- Commercial release preparation (homebrew market)
- Portfolio capstone quality
- **Historical significance:** 49M units sold, 16-bit console war winner
- **Active homebrew scene** (still very active)
- Mode 7 + enhancement chip mastery (signature SNES features)

**Deliverables:** 2 portfolio-ready commercial-quality SNES games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. 65816 Programming**
- P1: Basic instructions (16-bit, 6502 evolution)
- P2: Advanced 65816 techniques (16-bit/8-bit mode switching)
- P3: Enhancement chip optimization (SA-1, Super FX)
- P4: Complex 65816 techniques
- P5+: Extreme optimization

**2. PPU Programming**
- P1: PPU basics (tiles, sprites, 4 backgrounds)
- P2: Advanced PPU (all modes 0-6)
- P3: **Mode 7 mastery** (scaling/rotation, pseudo-3D)
- P4: All PPU capabilities (all 8 modes)
- P5+: Professional PPU programming

**3. Mode 7 Graphics**
- P3: **Mode 7 introduction** (scaling, rotation)
- P3: Mode 7 + HDMA (per-scanline transformations)
- P4: Mode 7 + sprites (pseudo-3D games)
- P5: Advanced Mode 7 (F-Zero, Mario Kart techniques)
- P6: Maximum Mode 7 capabilities

**4. Enhancement Chips**
- P3: **Super FX** (3D polygons, Star Fox style)
- P3: **SA-1** (faster 65816, 10.74MHz)
- P3: **DSP** chips (math coprocessor)
- P3: **Other chips** (S-DD1, SPC7110, CX4, etc.)
- P4: Enhancement chip mastery (all types)
- P5+: Professional enhancement chip usage

**5. Sprite Management**
- P1: **128 hardware sprites** (64 large + 64 small)
- P2: Sprite optimization (positioning, priority)
- P3: Advanced sprites (128+ via multiplexing)
- P4: Maximum sprite utilization
- P5+: Complex sprite systems

**6. HDMA (Horizontal DMA)**
- P2: **HDMA basics** (per-scanline effects)
- P3: **HDMA + Mode 7** (per-scanline transformations)
- P4: Advanced HDMA (wave effects, complex)
- P5: HDMA mastery (all capabilities)
- P6: Maximum HDMA (extreme effects)

**7. Sound Programming**
- P1: S-SMP/S-DSP basics (8-channel sample-based)
- P2: BRR sample format (compressed samples)
- P3: Advanced audio (all 8 channels, effects)
- P4: Professional audio (S-DSP all features)
- P5+: Audio mastery (commercial quality)

**8. Memory Management**
- P1: 128KB main RAM + 64KB VRAM + 64KB audio RAM
- P2: Efficient data structures
- P3: Enhancement chip RAM (SA-1 I-RAM, etc.)
- P5+: Maximum memory efficiency

---

## Hardware Progression

### Super Nintendo Base (Phases 1-2)
**Platform:** Super Nintendo / Super Famicom (1990)
**Characteristics:**
- **65816 CPU @ 3.58MHz** (WDC 65C816 - 16-bit, 6502 evolution!)
- **128KB main RAM** (vs Genesis's 64KB)
- **64KB VRAM** (video memory)
- **64KB audio RAM** (S-SMP's RAM)
- **PPU** (Picture Processing Unit - sophisticated graphics):
  - 256×224 resolution (32×28 tiles, 8×8 or 16×16)
  - **128 hardware sprites** (64 large 64×64, 64 small 32×32, vs Genesis's 80)
  - **256 colors on-screen** from 32,768 palette (vs Genesis's 64 from 512!)
  - **4 background layers** (BG1, BG2, BG3, BG4 - independent scrolling)
  - **8 graphics modes** (Mode 0-7):
    - Mode 0: 4 backgrounds, 4 colors each
    - Mode 1: 2 backgrounds (16 colors) + 1 background (4 colors)
    - Mode 2: 2 backgrounds (16 colors) + offset-per-tile
    - Mode 3: 2 backgrounds (256/16 colors) + direct color
    - Mode 4: 2 backgrounds (256/4 colors) + offset-per-tile
    - Mode 5: 1 background (16 colors) + 512×224 hi-res
    - Mode 6: 1 background (16 colors) + 512×224 hi-res + offset
    - **Mode 7: Scaling/rotation (signature SNES feature!)**
  - Priority system (layering)
  - Hardware scrolling (per-layer)
- **DMA** (Direct Memory Access - fast transfers to VRAM/audio RAM)
- **HDMA** (Horizontal DMA - per-scanline effects, SNES exclusive!)
- **8-channel sample-based audio**:
  - **S-SMP** (Sony SPC700 @ 1.024MHz - sound CPU)
  - **S-DSP** (Digital Signal Processor - audio chip)
  - 64KB audio RAM
  - **BRR sample format** (Bit Rate Reduction - compressed samples)
  - High-quality sample-based audio (vs Genesis's FM synthesis)
  - 8 independent channels (ADSR envelope, pitch, pan, echo)
- Controller input (4-6 buttons + D-pad, 2 ports)
- Cartridge-based (256KB-6MB typical, enhancement chips possible)

**Focus:** Master 65816 and PPU
- 65816 programming (16-bit, 6502 evolution)
- PPU tile system (4 backgrounds, 8 modes)
- 128 hardware sprites (smooth movement)
- Hardware scrolling (per-layer, independent)
- HDMA (per-scanline effects - powerful!)
- 8-channel sample audio (S-SMP/S-DSP)

**Historical Context:**
- Genesis main competitor (1990-2003, 13 years)
- **49 million units sold** (vs Genesis's 30.75M - winner of 16-bit console war!)
- Released later (1990 vs Genesis's 1988)
- Super Mario World (pack-in), Mario, Zelda, Metroid, Final Fantasy, Chrono Trigger
- **Mode 7** (scaling/rotation - signature feature)
- **Enhancement chips** (Super FX, SA-1, DSP - pushed capabilities)
- Longer lifespan (1990-2003 vs Genesis's 1988-1997)
- More RPGs (Final Fantasy, Dragon Quest, Chrono Trigger, etc.)

**SNES vs Genesis:**
- **More colors:** 256 on-screen (vs Genesis's 64)
- **Mode 7:** Scaling/rotation (vs Genesis's limited effects)
- **Enhancement chips:** Super FX, SA-1, DSP (vs Genesis's standard hardware)
- **HDMA:** Per-scanline effects (vs Genesis's standard DMA)
- **Sample-based audio:** 8 channels (vs Genesis's FM synthesis) - different approaches
- **Slower CPU:** 65816 @ 3.58MHz (vs Genesis's 68000 @ 7.6MHz - but different architectures)
- **More sprites:** 128 (vs Genesis's 80)
- **More RAM:** 128KB main (vs Genesis's 64KB)
- **Later release:** 1990 (vs Genesis's 1988)
- **Winner:** 49M units (vs Genesis's 30.75M)

**SNES Advantages:**
- More colors (256 vs 64 on-screen)
- Mode 7 (scaling/rotation - unique!)
- Enhancement chips (Super FX 3D, SA-1 speed, etc.)
- HDMA (per-scanline effects)
- More RAM (128KB vs 64KB)
- More sprites (128 vs 80)
- Sample-based audio (high quality, different from FM)

**SNES vs Genesis - Different Strengths:**
- **SNES:** Mode 7, colors, effects, enhancement chips, sample audio, RPGs
- **Genesis:** Faster CPU, "Blast Processing!", FM synthesis, action games, sports

### Mode 7 & Enhancement Chips (Phase 3+)
**Introduced Phase 3**
**Enhanced Features:**

**Mode 7 (Scaling/Rotation):**
- Single background layer with affine transformations
- Rotate, scale, shear, perspective
- Pseudo-3D effects (F-Zero, Mario Kart, Pilotwings)
- Combined with sprites (simulate 3D)
- HDMA + Mode 7 (per-scanline transformations - advanced!)
- Signature SNES feature (games: F-Zero, Mario Kart, Pilotwings, etc.)

**Enhancement Chips (Cartridge-based coprocessors):**

**Super FX (GSU - Graphics Support Unit):**
- 10.5-21.4MHz RISC processor (faster than main CPU!)
- 3D polygon rendering
- Custom instruction set
- 512 bytes cache RAM
- Games: Star Fox (polygons!), Yoshi's Island (effects), Stunt Race FX

**SA-1 (Super Accelerator):**
- 65816 @ 10.74MHz (3× faster than main CPU!)
- 2KB I-RAM (fast work RAM)
- Memory mapping (MMC)
- DMA controller
- Math acceleration
- Games: Super Mario RPG, Kirby's Dream Land 3, Kirby Super Star

**DSP Chips (Digital Signal Processor):**
- Math coprocessor (multiply, divide, matrix operations)
- NEC µPD77C25 (DSP-1, most common)
- DSP-2, DSP-3, DSP-4 variants
- Games: Pilotwings (DSP-1), Super Mario Kart (DSP-1), Dungeon Master (DSP-2)

**Other Enhancement Chips:**
- **S-DD1:** Graphics decompression (Star Ocean, Street Fighter Alpha 2)
- **SPC7110:** Data decompression + RTC (Far East of Eden Zero)
- **CX4:** Wireframe 3D (Mega Man X2, X3)
- **OBC1:** Sprite positioning (Metal Combat: Falcon's Revenge)
- **ST010/ST011:** Math coprocessor (F1 Race of Champions II)

**Focus:** Mode 7 + Enhancement chips mastery
- Mode 7 transformations (all capabilities)
- HDMA + Mode 7 (per-scanline effects)
- Super FX 3D programming (polygons)
- SA-1 enhanced CPU (10.74MHz 65816)
- DSP math coprocessor usage
- All enhancement chip types
- Professional SNES development

**Why Mode 7 & Enhancement Chips Matter:**
- **Mode 7:** Signature SNES feature (F-Zero, Mario Kart - couldn't be done on Genesis without special tricks)
- **Enhancement chips:** Extended SNES capabilities (3D, speed, math)
- **Competitive advantage:** SNES vs Genesis differentiation
- **Classic games:** Star Fox (Super FX), Super Mario RPG (SA-1), Pilotwings (DSP-1)
- **Learning value:** Understanding coprocessor architecture, hardware acceleration

### Modern SNES (Phase 8)
**Modern enhancements:**
- **bsnes-plus** (cycle-accurate emulator with excellent debugger)
- **Mesen-S** (cycle-accurate, excellent debugger)
- **Snes9x** (popular emulator)
- **higan/ares** (multi-system, cycle-accurate)
- Modern assemblers (WLA-DX, bass, ca65)
- Modern toolchains (SNES development kits)
- **Very active homebrew scene** (one of most active!)
- SD2SNES/FXPak Pro (modern flash cart, enhancement chip support)

**Focus:** Modern workflow
- Modern emulators with debugging
- Modern assemblers and toolchains
- Homebrew development
- Portfolio showcase

---

## Spiral Learning Example: Racer

**Phase 1: Racer I (SNES base)** (16 lessons)
- Basic top-down racing (65816 fundamentals)
- Tile-based track (PPU backgrounds)
- Player sprite (hardware sprite)
- Opponent sprites (hardware sprites)
- 8-channel sample audio (engine sounds)

**Phase 2: Racer II (SNES optimized)** (32 lessons)
- Optimized 65816 code (16-bit/8-bit switching)
- Smooth scrolling (PPU backgrounds)
- More opponents (128 sprites available)
- HDMA effects (road effects)
- Multi-track game

**Phase 3: Racer III (Mode 7!)** (64 lessons - MODE 7 INTRODUCED)
- **Mode 7 scaling/rotation** (pseudo-3D racing - F-Zero/Mario Kart style!)
- **Perspective projection** (road scaling towards horizon)
- **HDMA + Mode 7** (per-scanline road transformation)
- **Sprite scaling simulation** (opponents appear to move in 3D)
- **Direct comparison:** "Here's your top-down racer. Now make it pseudo-3D with Mode 7!"
- Signature SNES racing (like Mario Kart, F-Zero)

**Phase 4: Racer IV (Advanced Mode 7)** (64 lessons)
- Advanced Mode 7 (all transformations, complex tracks)
- HDMA mastery (complex road effects)
- 128 sprites (many opponents)
- Professional audio (8-channel music, samples)

**Phase 6: Racer V (SNES limits)** (128 lessons)
- Maximum Mode 7 (extreme effects)
- Extreme optimization
- Commercial-quality (F-Zero/Mario Kart level)
- Pushing SNES limits

Students see evolution: SNES basics → Optimized → **Mode 7 pseudo-3D** → Advanced → Professional

---

## Key Differences from Other Platforms

**SNES vs Genesis:**
- **Mode 7:** Yes (vs Genesis no - signature SNES feature!)
- **Enhancement chips:** Yes (Super FX, SA-1, DSP vs Genesis standard)
- **More colors:** 256 on-screen (vs Genesis 64)
- **HDMA:** Per-scanline effects (vs Genesis standard DMA)
- **Sample audio:** 8-channel (vs Genesis FM synthesis) - different approaches
- **Slower CPU:** 65816 @ 3.58MHz (vs Genesis 68000 @ 7.6MHz)
- **More sprites:** 128 (vs Genesis 80)
- **More RAM:** 128KB (vs Genesis 64KB)
- **Winner:** 49M units (vs Genesis 30.75M)

**SNES vs NES:**
- 65816 vs 6502 (16-bit evolution)
- 256 colors vs 25 (huge improvement!)
- 128 sprites vs 64
- Mode 7 (vs NES no scaling/rotation)
- 8-channel sample vs 5-channel waveform
- Enhancement chips (vs NES mappers)

**SNES Advantages:**
- **Mode 7** (scaling/rotation - F-Zero, Mario Kart, Pilotwings)
- **Enhancement chips** (Super FX 3D, SA-1 speed, DSP math)
- **HDMA** (per-scanline effects - unique!)
- **More colors** (256 vs Genesis 64)
- **Sample-based audio** (8-channel, high quality)
- **Winner of 16-bit console war** (49M units)

**SNES Considerations:**
- Slower CPU than Genesis (but enhancement chips compensate)
- Sample audio vs FM (different, not clearly better/worse)
- Later release than Genesis (1990 vs 1988)
- More expensive (vs Genesis)

**Learning Path:**
- NES → SNES (Nintendo evolution, 6502 → 65816)
- SNES → N64 (Nintendo 16-bit → 64-bit)
- 65816 skills transfer to 6502 family (NES, C64, 2600, 7800, Apple II)

**Same Pattern Library Concepts:**
- 65816 assembly (6502 evolution - skills transfer!)
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
- Expected output defined (basic, Mode 7, enhancement chips where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete 65816 SNES games from scratch
- Understands PPU (4 backgrounds, 128 sprites, graphics modes)
- Understands 8-channel sample audio (S-SMP/S-DSP)
- Has 16 portfolio SNES games

**Phase 3 Complete:**
- Student masters Mode 7 (scaling/rotation, pseudo-3D)
- Masters enhancement chips (Super FX, SA-1, DSP)
- Masters HDMA + Mode 7 (per-scanline transformations)
- Can compare/contrast basic vs Mode 7 vs enhancement chip implementations
- Has basic, Mode 7, and enhancement chip versions of key games
- **Signature SNES features mastered**

**Phase 8 Complete:**
- Student has 60 portfolio games showcasing SNES
- Masters 65816 architecture (16-bit 6502 evolution)
- Masters Mode 7 (all transformations, pseudo-3D)
- Masters enhancement chips (Super FX, SA-1, DSP, all types)
- Masters HDMA (per-scanline effects, all capabilities)
- Masters PPU (all 8 modes, all features)
- Masters 8-channel sample audio (S-SMP/S-DSP mastery)
- Can create commercial-release quality games
- Ready for professional SNES homebrew development
- **65816 expertise** transfers to 6502 family (NES, C64, 2600, 7800)

---

## Resources Required

**Development Tools:**
- Assembler: WLA-DX (standard for SNES), bass, ca65
- Emulator: bsnes-plus (cycle-accurate, debugger), Mesen-S, Snes9x
- Graphics: Tile/sprite editors (SNES format)
- Audio: BRR sample converters, S-SMP/S-DSP trackers
- Mode 7 tools: Mode 7 calculators, transformation tools
- Enhancement chip tools: Super FX assemblers, SA-1 tools
- Utilities: ROM builders

**Reference Materials:**
- 65816 instruction set (16-bit, 6502 evolution)
- PPU Programming Guide (tiles, sprites, 8 modes, Mode 7, HDMA)
- S-SMP/S-DSP reference (8-channel audio, BRR format)
- Mode 7 reference (affine transformations, HDMA combination)
- Enhancement chip references:
  - Super FX instruction set (GSU programming)
  - SA-1 reference (10.74MHz 65816, I-RAM, MMC)
  - DSP chip references (math coprocessor operations)
- SNES Technical Reference
- Memory map (main RAM, VRAM, audio RAM, registers)

**Testing:**
- Emulators (development - bsnes-plus/Mesen-S recommended)
- Real SNES hardware (verification)
- SD2SNES/FXPak Pro (modern flash cart, enhancement chip support!)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Mode 7 + Enhancement chips Phase 3
**Note:** No Phase 0 (console - no BASIC, direct assembly)
**Historical Note:** Genesis competitor (1990-2003), 49M units sold, winner of 16-bit console war
**Signature Features:** **Mode 7 scaling/rotation, Enhancement chips (Super FX, SA-1, DSP), HDMA**
**CPU:** 65816 @ 3.58MHz (16-bit 6502 evolution) - skills transfer to 6502 family!
**Winner:** 49M units sold vs Genesis's 30.75M - 16-bit console war champion
**Next Steps:** Create SNES 8-PHASE-GAME-PROGRESSION.md with specific game mapping
