# Game Boy Advance Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning - games revisited at increasing complexity
**Hardware:** GBA base → Advanced techniques Phase 3 → Modern
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Direct assembly (no BASIC - console platform)
**Historical Note:** 32-bit portable (2001-2008), 81.51M units sold, Game Boy backward compatible
**Unique Feature:** **ARM7TDMI 32-bit CPU** (first ARM in curriculum!), Mode 7-like scaling/rotation

---

## Curriculum Philosophy

### Core Principles

**1. Game-First Development**
- Every lesson improves an actual, playable game
- No abstract exercises or theoretical concepts in isolation
- Milestones: Playable → Complete → Polished → Professional

**2. Spiral Learning**
- Games revisited multiple times across phases at increasing complexity
- Students directly compare basic vs advanced GBA techniques
- Clear progression shows growth and mastery

**3. Pattern Library**
- Core techniques taught once, documented, then reused
- "ARM addressing modes are ARM addressing modes" - same concept, increasingly optimized
- Avoid teaching from scratch every time

**4. Genre Techniques, Not Recreations**
- Teach techniques applicable to game genres
- Not recreating specific classic games (though students learn their techniques)
- Students learn transferable skills

**5. Progressive Hardware Mastery**
- Phase 1-2: Master GBA base (ARM7TDMI, LCD, DMA, 32-bit power)
- Phase 3: **Advanced GBA mastery** - rotation/scaling, all modes, DMA optimization
- Phase 4-6: Advanced techniques, pushing GBA limits
- Phase 7: **Maximum GBA** - all capabilities, professional development
- Phase 8: Modern GBA development (homebrew scene)

---

## 8-Phase Structure

### Phase 1: Foundation
**Tiers:** 16 × 16 lessons = 256 lessons (Lessons 1-256)
**Hardware:** Game Boy Advance base (ARM7TDMI @ 16.78MHz, 288KB RAM)
**Complexity:** Simple techniques, focused scope
**Games:** 16 unique games introducing core concepts

**Key Learning:**
- ARM7TDMI instruction set fundamentals (32-bit RISC - first ARM in curriculum!)
- **288KB RAM** (256KB WRAM + 32KB IRAM + 96KB VRAM)
- **96KB video RAM** (VRAM)
- **LCD Controller**:
  - 240×160 resolution (30×20 tiles, 8×8 each)
  - **32,768 colors** (15-bit color - 5 bits each R/G/B)
  - **Tile-based backgrounds** (4 background layers)
  - **128 hardware sprites** (OAM - Object Attribute Memory)
  - **6 graphics modes** (Mode 0-5):
    - Mode 0-2: Tile-based (like SNES)
    - **Mode 3-5: Bitmap modes** (direct pixel access!)
    - **Mode 1-2: Affine backgrounds** (rotation/scaling - like SNES Mode 7!)
  - Hardware scrolling, rotation, scaling
- **DMA** (Direct Memory Access - 4 channels, very powerful!)
- **2-channel sample audio** (Direct Sound - high quality samples!)
- **Game Boy backward compatible** (plays GB/GBC games!)
- **Portable:** Rechargeable battery (2 AA batteries, 15 hours typical)
- D-pad + A/B + L/R buttons + Select/Start
- **No operating system** (direct hardware programming)
- 59.73Hz refresh rate

**No Autoload - Direct Boot:**
Cartridge inserted = game runs immediately. No loader required.

**Deliverables:** 16 complete, playable GBA games

---

### Phase 2: Expansion
**Tiers:** 16 × 32 lessons = 512 lessons (Lessons 257-768)
**Hardware:** GBA base (ARM7TDMI @ 16.78MHz, 288KB RAM)
**Complexity:** Optimization, more features
**Games:** 8 revisited (optimized), 8 new genres

**Key Learning:**
- Optimized ARM7TDMI code (32-bit RISC, 16.78MHz)
- **THUMB mode** (16-bit instructions - denser code, faster from ROM!)
- Advanced LCD programming (4 backgrounds, 6 modes)
- **128 sprites optimization** (smooth movement)
- Sprite multiplexing (more than 128 visible)
- Advanced scrolling (per-layer, rotation/scaling)
- **DMA optimization** (4 channels - HBlank, VBlank, FIFO)
- **2-channel Direct Sound** (sample-based audio, high quality)
- Advanced collision detection (software-based)
- Multi-screen game structures
- **288KB RAM management** (256KB WRAM + 32KB IRAM fast)

**Deliverables:** 16 games with commercial-quality GBA features

---

### Phase 3: Advanced GBA Mastery (Rotation/Scaling/Bitmap)
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 769-1280)
**Hardware:** GBA advanced techniques
**Complexity:** Direct basic→advanced comparison, rotation/scaling/bitmap mastery
**Games:** 5 revisited from Phases 1-2 with advanced techniques, 3 new showcasing mastery

**Key Learning:**
- **Affine backgrounds** (rotation/scaling - Mode 1-2, like SNES Mode 7!):
  - 2D matrix transformations (rotate, scale, shear)
  - Pseudo-3D effects (racing games, mode 7-style)
  - Background rotation/scaling (affine transformations)
- **Bitmap modes** (Mode 3-5 - direct pixel access!):
  - Mode 3: 240×160, 32,768 colors (full screen bitmap)
  - Mode 4: 240×160, 256 colors (double-buffered bitmap, page flipping!)
  - Mode 5: 160×128, 32,768 colors (smaller bitmap)
  - Direct pixel manipulation
  - Software 3D rendering possible (framebuffer access)
- **All 6 graphics modes** (Mode 0-5 mastery):
  - Tile-based (Mode 0-2)
  - Bitmap (Mode 3-5)
  - Affine (Mode 1-2)
- **Direct comparison:** "Here's your tile game. Now add rotation/scaling with affine mode"
- **DMA mastery** (4 channels, all techniques)
- **THUMB/ARM mode switching** (optimization)
- Professional GBA development

**Deliverables:** 8 games - 5 affine/bitmap versions, 3 new showcasing advanced techniques

**Games Revisited with Advanced Techniques:**
1. Snake III (Affine) - rotating playfield (Mode 7-style)
2. Shooter III (Affine/Bitmap) - pseudo-3D backgrounds, Mode 4 effects
3. Platformer III (Affine) - rotation effects, scaling
4. Racer I (Affine) - Mode 7-style racing (like SNES F-Zero!)
5. One other from Phase 1-2

**New Advanced Games:**
6. 3D Action I (Bitmap Mode 4 - software 3D rendering, page flipping!)
7. Puzzle I (Bitmap Mode 3 - direct pixel manipulation)
8. Advanced game type

---

### Phase 4: Advanced Fundamentals
**Tiers:** 8 × 64 lessons = 512 lessons (Lessons 1281-1792)
**Hardware:** GBA (pushing limits)
**Complexity:** Advanced techniques, large games
**Games:** 4 revisited (advanced), 4 new

**Key Learning:**
- Advanced ARM7TDMI optimization (32-bit RISC, 16.78MHz maximum)
- **THUMB mode mastery** (16-bit instructions, ROM efficiency)
- Maximum LCD utilization (128 sprites, all 6 modes)
- Advanced affine transformations (rotation, scaling, shear, all)
- Advanced bitmap modes (software 3D, effects)
- **DMA extreme optimization** (4 channels, HBlank/VBlank tricks)
- Advanced audio (2-channel Direct Sound, sample streaming)
- Advanced collision detection
- Isometric projection
- Turn-based strategy mechanics
- **32KB IRAM usage** (fast work RAM for critical code)

**Deliverables:** 8 games showcasing advanced GBA techniques

---

### Phase 5: Specialized Systems
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 1793-2304)
**Hardware:** GBA mastery
**Complexity:** Genre-specific deep dives, large-scale games
**Games:** 4 genre-mastery games (large RPG, Metroidvania, full shmup, adventure)

**Key Learning:**
- Large-scale game architecture
- Quest systems and narrative
- Interconnected world design
- Advanced enemy AI and bosses
- Power-up progression systems
- Advanced audio composition (2-channel Direct Sound mastery)
- Large game worlds (cartridge ROM, save SRAM/Flash)
- Software 3D rendering (bitmap modes, polygon fill)

**Deliverables:** 4 large-scale genre-defining games

---

### Phase 6: Platform Limits
**Tiers:** 4 × 128 lessons = 512 lessons (Lessons 2305-2816)
**Hardware:** GBA (absolute limits)
**Complexity:** Ambitious projects pushing boundaries
**Games:** 4 extreme games (ultimate versions, complex systems)

**Key Learning:**
- Managing 128+ simultaneous sprites (multiplexing mastery)
- Complex multi-character systems
- Real-time strategy mechanics
- Commercial polish techniques
- Extreme ARM7TDMI optimization (32-bit RISC)
- Software 3D engines (bitmap modes, z-buffer, textures)
- Pushing GBA limits
- Professional GBA development

**Deliverables:** 4 games pushing absolute limits of GBA

---

### Phase 7: Maximum GBA
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 2817-3328)
**Hardware:** GBA (all capabilities)
**Complexity:** Large-scale games with maximum features
**Games:** 2 epic games (large RPG, 3D action/racer)

**Key Learning:**
- All LCD capabilities (all 6 modes, affine, bitmap)
- All audio capabilities (2-channel Direct Sound mastery)
- Software 3D mastery (bitmap rendering, polygon engines)
- Large game worlds
- Advanced graphics techniques (all modes, effects)
- Commercial GBA development
- Professional quality polish
- **Game Boy backward compatibility** (GB/GBC mode understanding)

**Deliverables:** 2 commercial-scale GBA games

---

### Phase 8: Pinnacle (Modern Homebrew)
**Tiers:** 2 × 256 lessons = 512 lessons (Lessons 3329-3840)
**Hardware:** Modern GBA development
**Complexity:** Modern enhanced platform, portfolio capstone
**Games:** 2 ultimate showcase games (3D racer, advanced platformer)

**Key Learning:**
- Modern GBA development workflow
- Emulator debugging (mGBA, No$GBA, VisualBoyAdvance-M)
- Modern homebrew techniques
- Modern assemblers/toolchains (devkitARM - standard GBA toolchain!)
- Cross-development (modern tools, C + ARM assembly)
- Commercial release preparation (homebrew market, physical carts)
- Portfolio capstone quality
- **Historical significance:** 81.51M units sold, 32-bit portable, ARM architecture
- **Active homebrew scene** (very active, physical cart releases!)

**Deliverables:** 2 portfolio-ready commercial-quality GBA games

---

## Pattern Library Structure

The curriculum builds a **reusable pattern library** taught once and enhanced progressively:

### Core Patterns

**1. ARM7TDMI Programming**
- P1: Basic instructions (32-bit RISC - first ARM!)
- P2: **THUMB mode** (16-bit instructions, ROM efficiency)
- P3: Advanced ARM/THUMB (mode switching optimization)
- P4: Complex ARM7TDMI techniques
- P5+: Extreme optimization

**2. LCD Programming**
- P1: LCD basics (tiles, sprites, 4 backgrounds)
- P2: Advanced LCD (6 modes, scrolling)
- P3: **Affine backgrounds** (rotation/scaling - Mode 7-like!)
- P3: **Bitmap modes** (Mode 3-5, direct pixels)
- P4: All LCD capabilities
- P5+: Professional LCD programming

**3. Affine Transformations**
- P3: **Affine backgrounds** (rotation, scaling, shear)
- P4: Advanced affine (pseudo-3D, Mode 7-style)
- P5: Affine mastery (all transformations)
- P6: Maximum affine techniques

**4. Bitmap Programming**
- P3: **Bitmap Mode 3** (240×160, 32,768 colors)
- P3: **Bitmap Mode 4** (240×160, 256 colors, page flipping!)
- P3: **Bitmap Mode 5** (160×128, 32,768 colors)
- P5: Software 3D rendering (polygons, z-buffer)
- P6: 3D engines (full polygon rendering)

**5. Sprite Management**
- P1: **128 hardware sprites** (various sizes)
- P2: Sprite optimization (positioning, priority)
- P3: Advanced sprites (128+ via multiplexing)
- P5+: Complex sprite systems

**6. DMA Programming**
- P2: **DMA basics** (4 channels)
- P3: **DMA optimization** (HBlank, VBlank, FIFO)
- P4: DMA mastery (all channels, all techniques)
- P5+: Extreme DMA techniques

**7. Sound Programming**
- P1: 2-channel Direct Sound basics (sample-based)
- P2: Sample streaming (audio playback)
- P3: Advanced audio (all capabilities)
- P5+: Professional audio

**8. Memory Management**
- P1: 288KB RAM (256KB WRAM + 32KB IRAM + 96KB VRAM)
- P2: **32KB IRAM usage** (fast work RAM for critical code)
- P3: Efficient data structures
- P5+: Maximum memory efficiency

---

## Hardware Progression

### Game Boy Advance Base (Phases 1-2)
**Platform:** Game Boy Advance (2001)
**Characteristics:**
- **ARM7TDMI CPU @ 16.78MHz** (32-bit RISC - first ARM in curriculum!)
  - ARM instruction set (32-bit instructions)
  - **THUMB instruction set** (16-bit instructions - denser, faster from ROM!)
  - 3-stage pipeline
  - High-performance RISC
- **288KB RAM total:**
  - 256KB WRAM (work RAM - external, slower)
  - **32KB IRAM** (internal RAM - on-chip, fast!)
  - 96KB VRAM (video RAM)
- **LCD Controller**:
  - 240×160 resolution (30×20 tiles, 8×8 each)
  - **32,768 colors** (15-bit color - 5 bits each R/G/B)
  - **4 background layers** (BG0, BG1, BG2, BG3)
  - **128 hardware sprites** (OAM - Object Attribute Memory)
  - Various sizes (8×8 to 64×64)
  - **6 graphics modes:**
    - **Mode 0:** 4 tile backgrounds (no rotation)
    - **Mode 1:** 2 tile backgrounds + 1 affine background (rotation/scaling!)
    - **Mode 2:** 2 affine backgrounds (rotation/scaling!)
    - **Mode 3:** Bitmap 240×160, 32,768 colors (full screen)
    - **Mode 4:** Bitmap 240×160, 256 colors (page flipping!)
    - **Mode 5:** Bitmap 160×128, 32,768 colors
  - Hardware scrolling, rotation, scaling (affine)
  - Priority system, alpha blending
- **DMA** (Direct Memory Access - 4 channels):
  - Fast memory copies (VRAM, OAM, etc.)
  - HBlank DMA (per-scanline effects!)
  - VBlank DMA (per-frame effects)
  - FIFO DMA (audio streaming)
- **2-channel Direct Sound** (sample-based audio):
  - High-quality sample playback
  - Mixing, volume control
  - Much better than GB/GBC (4-channel simple vs 2-channel samples)
- **Game Boy backward compatible** (plays GB/GBC games!)
- **Portable:** 2 AA batteries or rechargeable (15 hours typical)
- **Reflective LCD** (backlit on later models - SP)
- D-pad + A/B + L/R + Select/Start

**Focus:** Master ARM7TDMI and GBA hardware
- ARM7TDMI programming (32-bit RISC)
- THUMB mode (16-bit instructions, efficiency)
- LCD tile system (4 backgrounds, 128 sprites)
- 6 graphics modes (tile + bitmap + affine)
- DMA (4 channels, powerful!)
- 2-channel Direct Sound (sample audio)
- **32-bit portable power** (vs 8-bit GB/GBC)

**Historical Context:**
- 32-bit portable (2001-2008)
- 81.51 million units sold (very successful!)
- Game Boy successor (backward compatible!)
- ARM architecture (first mainstream ARM handheld)
- More powerful than SNES (32-bit vs 16-bit)
- Affine graphics (rotation/scaling like SNES Mode 7)
- Bitmap modes (direct pixel access, 3D possible)
- Pokémon Ruby/Sapphire (2002 - major success)
- Game Boy Advance SP (2003 - backlit, rechargeable, clamshell)
- Game Boy Micro (2005 - tiny)

**GBA vs Game Boy/GBC:**
- **32-bit ARM** vs 8-bit SM83 (Z80-like)
- **32,768 colors** vs 4-shade monochrome / 56 colors
- **128 sprites** vs 40
- **Affine graphics** (rotation/scaling vs none)
- **Bitmap modes** (direct pixels vs tiles only)
- **Sample audio** (Direct Sound vs 4-channel simple)
- **More RAM:** 288KB vs 8-32KB
- **Backward compatible** (plays GB/GBC!)

**GBA vs SNES:**
- Similar graphics power (both have rotation/scaling!)
- More portable (vs home console)
- ARM vs 65816 (different architectures)
- Sample audio vs SNES's sample audio (similar approach)

**GBA Advantages:**
- **32-bit ARM** (powerful RISC CPU)
- **Affine graphics** (rotation/scaling - Mode 7-style!)
- **Bitmap modes** (software 3D possible!)
- **DMA** (4 channels, very powerful)
- **Portable** (vs home consoles)
- **Backward compatible** (entire GB/GBC library!)
- **Very active homebrew scene**

### Advanced GBA (Phase 3+)
**Introduced Phase 3**
**Enhanced Focus:**
- **Affine backgrounds** (rotation/scaling mastery)
- **Bitmap modes** (Mode 3-5 mastery, software 3D)
- **All 6 graphics modes** (tile + bitmap + affine)
- **DMA mastery** (4 channels, all techniques)
- **THUMB/ARM optimization** (mode switching)
- Professional GBA development

**Focus:** Affine + Bitmap mastery
- Mode 1-2 affine (rotation/scaling)
- Mode 3-5 bitmap (direct pixels, 3D)
- Software 3D engines (polygon fill, textures)
- DMA extreme optimization
- All LCD capabilities

**Why Affine/Bitmap Matter:**
- **Affine:** Rotation/scaling (F-Zero, racing games, Mode 7-style effects!)
- **Bitmap:** Direct pixel access (3D games, effects, framebuffer!)
- Software 3D possible (bitmap + ARM speed)
- Commercial games used these (many GBA games)

### Modern GBA (Phase 8)
**Modern enhancements:**
- **mGBA** (excellent emulator + debugger, cycle-accurate!)
- No$GBA, VisualBoyAdvance-M emulators
- **devkitARM** (standard GBA toolchain - C + ARM assembly!)
- Modern toolchains (GBA development kits)
- **Very active homebrew scene** (physical cart releases!)
- EZ-Flash, Everdrive GBA (modern flash carts)
- Analogue Pocket (modern FPGA hardware, plays GBA)

**Focus:** Modern workflow
- devkitARM development (standard)
- mGBA debugging (excellent!)
- C + ARM assembly hybrid
- Homebrew development
- Physical cart releases (active market!)
- Portfolio showcase

---

## Spiral Learning Example: Racer

**Phase 1: Racer I (GBA base, tile mode)** (16 lessons)
- Basic top-down racing (ARM7TDMI fundamentals)
- Tile-based track (Mode 0, 4 backgrounds)
- Player/opponent sprites (128 sprites)
- 2-channel Direct Sound (engine samples)

**Phase 2: Racer II (GBA optimized)** (32 lessons)
- Optimized ARM/THUMB code (16-bit instructions from ROM)
- Smooth scrolling (4 backgrounds)
- More opponents (128 sprites)
- DMA optimization (VBlank transfers)
- Advanced audio (sample streaming)

**Phase 3: Racer III (Affine mode - Mode 7 style!)** (64 lessons - AFFINE INTRODUCED)
- **Mode 1 affine background** (rotation/scaling - F-Zero/Mario Kart style!)
- **Pseudo-3D racing** (perspective projection, like SNES Mode 7!)
- **DMA HBlank** (per-scanline road transformation)
- **Sprite scaling simulation** (opponents appear 3D)
- **Direct comparison:** "Here's your top-down racer. Now make it pseudo-3D with affine mode!"

**Phase 4: Racer IV (Advanced affine + bitmap)** (64 lessons)
- Advanced affine (all transformations, complex tracks)
- **Bitmap Mode 4** (3D dashboard, page flipping)
- DMA mastery (HBlank effects)
- Professional audio (sample streaming)

**Phase 6: Racer V (GBA limits)** (128 lessons)
- Software 3D (polygon road, texture mapping)
- Extreme optimization (ARM7TDMI maximum)
- Commercial-quality (F-Zero style)
- Pushing GBA limits

Students see evolution: GBA tile basics → Optimized → **Affine pseudo-3D** → Advanced → Professional

---

## Key Differences from Other Platforms

**GBA vs Game Boy/GBC:**
- **32-bit ARM** vs 8-bit SM83 (huge leap!)
- **32,768 colors** vs 4-shade / 56 colors
- **128 sprites** vs 40
- **Affine graphics** (rotation/scaling)
- **Bitmap modes** (direct pixels, 3D possible)
- **Sample audio** vs simple waveform
- **Backward compatible** (plays GB/GBC!)

**GBA vs SNES:**
- **Portable** vs home console
- **ARM vs 65816** (different architectures)
- **Similar graphics:** Both have rotation/scaling (affine vs Mode 7)
- **Bitmap modes** (GBA advantage for 3D)
- **Sample audio** (both use samples)

**GBA Advantages:**
- **32-bit ARM RISC** (powerful, modern architecture)
- **Affine + Bitmap** (rotation/scaling + direct pixels)
- **DMA** (4 channels, very powerful)
- **Portable** (play anywhere!)
- **Backward compatible** (GB/GBC library)
- **Very active homebrew scene**
- **ARM architecture** (first ARM learning - valuable skill!)

**Learning Path:**
- Game Boy → GBA (Nintendo portable evolution)
- GBA → Nintendo DS (ARM evolution, dual ARM CPUs)
- **ARM7TDMI → ARM family** (valuable modern skill!)
- Affine graphics → rotation/scaling understanding

**Same Pattern Library Concepts:**
- Collision detection algorithms
- AI pathfinding
- Physics systems
- Software 3D rendering (if bitmap modes)
- Game design patterns
- All transferable skills

---

## Assessment Strategy

**No self-directed work** - every tier is fully specified:
- Complete lesson breakdown (4-64 arcs × 4 lessons)
- Full code examples provided
- Expected output defined (tile, affine, bitmap modes where applicable)
- Verification steps included

**Progressive verification:**
- Lesson 4 (arc 1): Must be playable
- Lesson 8 (arc 2): Must be complete game
- Lesson 16/32/64/128/256: Must meet final specification

---

## Success Criteria

**Phase 1 Complete:**
- Student can write complete ARM7TDMI GBA games from scratch
- Understands LCD (4 backgrounds, 128 sprites, 6 modes)
- Understands DMA (4 channels)
- **Masters ARM architecture** (first ARM in curriculum!)
- Has 16 portfolio GBA games

**Phase 3 Complete:**
- Student masters affine graphics (rotation/scaling, Mode 7-style)
- Masters bitmap modes (Mode 3-5, direct pixels, software 3D)
- Masters all 6 graphics modes (tile + affine + bitmap)
- Can compare/contrast tile vs affine vs bitmap implementations
- Has tile, affine, and bitmap versions of key games

**Phase 8 Complete:**
- Student has 60 portfolio games showcasing GBA
- Masters ARM7TDMI (32-bit RISC, THUMB mode)
- Masters LCD (all 6 modes, affine, bitmap)
- Masters DMA (4 channels, all techniques)
- Masters 2-channel Direct Sound
- Can create commercial-release quality games
- Ready for professional GBA homebrew development
- **ARM architecture expertise** (valuable modern skill - ARM everywhere!)

---

## Resources Required

**Development Tools:**
- Toolchain: **devkitARM** (standard GBA toolchain - C + ARM assembly!)
- Emulator: **mGBA** (excellent debugger, cycle-accurate!), No$GBA, VBA-M
- Graphics: Tile/sprite/bitmap editors (GBA format)
- Audio: Sample converters, audio tools
- Utilities: ROM builders, GBA tools

**Reference Materials:**
- ARM7TDMI instruction set (32-bit RISC + THUMB 16-bit)
- GBATEK (comprehensive GBA technical reference)
- LCD reference (6 modes, affine, bitmap, DMA)
- DMA reference (4 channels, HBlank/VBlank/FIFO)
- Direct Sound reference (2-channel sample audio)
- Memory map (288KB RAM, VRAM, registers)

**Testing:**
- Emulators (development - mGBA highly recommended!)
- Real GBA hardware (verification)
- GBA SP (backlit screen)
- EZ-Flash, Everdrive GBA (modern flash carts)
- Analogue Pocket (modern FPGA hardware)

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Status:** Complete 8-phase curriculum structure defined - Affine + Bitmap mastery Phase 3
**Note:** No Phase 0 (console - no BASIC, direct assembly)
**Historical Note:** 32-bit portable (2001-2008), 81.51M units sold, Game Boy backward compatible
**Signature Features:** **ARM7TDMI 32-bit, Affine graphics (rotation/scaling), Bitmap modes (3D!)**
**CPU:** ARM7TDMI @ 16.78MHz (32-bit RISC) - **first ARM in curriculum, valuable modern skill!**
**Unique Advantage:** **Software 3D possible** (bitmap modes + ARM speed = polygon engines!)
**Next Steps:** Create GBA 8-PHASE-GAME-PROGRESSION.md with specific game mapping
