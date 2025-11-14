# Atari Jaguar Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Atari Jaguar (1993-1996) → Jaguar CD (1995) → Modern homebrew (2000s+)
**Approach:** Game-first, pattern library, multi-processor coordination mastery
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Atari's last console (1993), claimed "64-bit" (actually 32-bit with 64-bit data paths), complex multi-processor architecture (68000 + 2 custom RISC chips: Tom & Jerry), notoriously difficult to program, commercial failure (~250K units sold), competed with Saturn/PlayStation/N64, cult following and active homebrew scene decades later

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Atari Jaguar shipped without a built-in programming language. The curriculum begins directly with assembly, focused on multi-processor coordination and RISC programming.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** 68000 basics, Tom (GPU) graphics processor, Jerry (DSP) audio processor, Object Processor, Blitter, multi-processor coordination
**Professional Autoload:** From lesson 1, all programs professionally load from ROM

#### Pattern Library Established:
- **68000 CPU patterns** - Motorola 68000 @ 13.295 MHz (general control, system management)
- **Tom GPU patterns** - 32-bit RISC @ 26.6 MHz (graphics processing, main workhorse!)
- **Jerry DSP patterns** - 32-bit RISC @ 26.6 MHz (audio processing, can also do graphics!)
- **Object Processor** - Hardware display list (like Amiga copper, but more complex)
- **Blitter patterns** - Hardware bitmap copying, scaling, transparency
- **Multi-processor sync** - Coordinating 68000 + GPU + DSP (CRITICAL challenge!)
- **2MB RAM** - Split: 2MB main RAM (huge for 1993!)
- **16-bit RGB565 color** - 65,536 colors on screen simultaneously
- **24-bit true color** - RGB888 in RAM (downsampled to RGB565 for display)
- **Object list programming** - Display controlled via linked list of objects

#### Example Tier 1 Lesson: "Your First Object (68000 Control)"
```asm
; Atari Jaguar Assembly - Lesson 001
; Display a bitmap object using Object Processor
; Start with 68000, hand off to GPU later
; 68000 @ 13.295 MHz

        .include "jaguar.inc"

        .text

START:  move.w  #$2700,sr       ; Disable interrupts
        move.l  #$00100000,sp   ; Set stack pointer

        ; Stop Tom (GPU) and Jerry (DSP) initially
        move.l  #0,G_CTRL       ; Stop GPU
        move.l  #0,D_CTRL       ; Stop DSP

        ; Initialize Object Processor
        move.l  #OBJLIST,OLP    ; Set Object List Pointer

        ; Enable video output
        move.w  #$1F,VMODE      ; NTSC, RGB16, enable

LOOP:   ; Main loop (68000 handles control)
        move.w  VI,d0           ; Read Video Interrupt (wait for vblank)
        btst    #0,d0
        beq     LOOP

        ; Update game logic here
        bsr     UPDATE_GAME

        bra     LOOP

UPDATE_GAME:
        ; Simple animation: move sprite
        move.w  XPOS,d0
        addq    #1,d0           ; Move right
        cmp.w   #320,d0         ; Check boundary
        blt     .DONE
        moveq   #0,d0           ; Wrap to left
.DONE:  move.w  d0,XPOS
        move.w  d0,OBJLIST+8    ; Update object X position
        rts

XPOS:   dc.w    160             ; Sprite X position

; Object List (controls what Object Processor displays)
OBJLIST:
        ; Bitmap object (64×64 pixel sprite)
        dc.l    BRANCH_OBJ      ; Object type (bitmap)
        dc.l    OBJLIST         ; Link (points to self = last object)
        dc.w    160,100         ; X, Y position
        dc.w    64,64           ; Width, Height
        dc.l    SPRDATA         ; Bitmap data address
        dc.w    0               ; Index (unused)
        dc.w    $0001           ; Flags (enable)
        dc.l    0               ; Link to next (0 = end)

; Sprite bitmap data (64×64 pixels, RGB565)
SPRDATA:
        .rept   64*64
        dc.w    $F800           ; Red pixel (RGB565: 11111 000000 00000)
        .endr

        .include "jaguar_regs.inc"
```

**Key teaching moment:** Jaguar has THREE processors! 68000 for control, Tom GPU for graphics (where real power is!), Jerry DSP for audio. Object Processor displays things via linked list (NOT raster or tile system). Programming this architecture is NOTORIOUSLY DIFFICULT - coordination is the challenge.

**Tier progression:**
1. 68000 basics (system control, Object Processor)
2. Object List programming (display list concepts)
3. Bitmap objects (RGB565, RGB888)
4. Scaled bitmap objects (Blitter usage)
5. Controller input (3-button pad, numeric keypad)
6. GPU basics (loading code to GPU, execution)
7. Simple GPU graphics (pixel plotting, lines)
8. Jerry DSP basics (audio samples)
9. Multi-processor sync (68000↔GPU↔DSP communication)
10. Collision detection (software-based)
11. Score display (bitmap fonts)
12. Game state machines
13. Lives/continues systems
14. Difficulty progression
15. Polish patterns (screen transitions)
16. Complete multi-processor mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced GPU programming, Blitter mastery, Jerry DSP audio, multi-processor optimization, texture mapping

#### New Patterns:
- **GPU as main processor** - Most games run primarily on GPU (faster than 68000!)
- **Blitter techniques** - Hardware scaling, rotation, transparency
- **GPU 3D** - Software 3D rendering on GPU (no hardware 3D!)
- **Jerry audio engine** - Sample playback, mixing, effects
- **Object Processor mastery** - Complex display lists, priorities
- **RISC optimization** - Tom/Jerry have RISC instruction sets (different from 68000!)
- **Texture mapping** - Affine texture mapping via GPU
- **Z-buffering** - Software depth sorting for 3D
- **Multi-processor load balancing** - Distributing work efficiently
- **68000 as coordinator** - Using 68000 for I/O, GPU/DSP for processing

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - introducing Jaguar CD (1995)
**Focus:** CD-ROM access, CD-DA audio, full-motion video (FMV), larger game assets

#### Phase 3 Enhancement: Jaguar CD
- **CD-ROM drive** - 2× speed (300 KB/s, slow by 1995 standards)
- **CD-DA audio** - Redbook audio tracks (full quality music!)
- **Full-motion video** - Cinepak codec support
- **Larger games** - 650MB vs 6MB cartridge
- **Memory management** - Streaming from CD (careful buffering!)
- **VLM (Virtual Light Machine)** - Visualization engine for CD audio

**Tier 40 Example - Streaming CD Data to GPU:**
```asm
; Load texture data from CD-ROM and send to GPU

CD_LOAD_TEXTURE:
        ; Position CD to texture data sector
        move.l  #TEXTURE_SECTOR,d0
        bsr     CD_SEEK

        ; Read texture data (64KB)
        move.l  #TEXTURE_BUFFER,a0
        move.l  #65536,d0
        bsr     CD_READ

        ; Wait for GPU to be idle
.WAIT:  move.l  G_CTRL,d0
        btst    #0,d0           ; Check GPU busy bit
        bne     .WAIT

        ; Send texture to GPU RAM
        move.l  #GPU_TEX_ADDR,a1
        move.l  #TEXTURE_BUFFER,a0
        move.l  #65536,d0
.COPY:  move.l  (a0)+,(a1)+
        subq.l  #4,d0
        bne     .COPY

        ; Tell GPU texture is ready
        move.l  #1,GPU_MSG
        move.l  #$00000001,G_CTRL ; Start GPU
        rts

TEXTURE_SECTOR: dc.l 100        ; CD sector number
TEXTURE_BUFFER: ds.b 65536      ; RAM buffer
```

**Jaguar CD Games:** Only 13 commercial titles released. Homebrew scene has created more CD titles than Atari did!

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional multi-processor architecture, advanced 3D (GPU), complex audio (DSP), load balancing, optimization

#### Advanced Techniques:
- **GPU 3D engines** - Textured polygons, Gouraud shading
- **Jerry 3D audio** - Positional audio, doppler effects
- **Multi-processor pipelines** - 68000 (control) → GPU (graphics) → DSP (audio)
- **Object Processor tricks** - Mid-screen palette changes, sprite multiplexing
- **Blitter chaining** - Multiple operations queued
- **Fixed-point math** - Fast 3D without FPU (none of the processors have FPU!)
- **Texture caching** - Managing 2MB RAM for large textures
- **CD streaming** - Continuous data loading (music, levels)
- **RISC assembly mastery** - Tom/Jerry have different instruction sets than 68000
- **VLM programming** - Music visualizations (Jaguar CD)

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** 3D action games, fighting games, platformers, racing games, FMV adventures (CD)

#### Genre Specializations:
- **3D shooters** - Doom-style (Jaguar had native Doom port!), Wolfenstein 3D
- **Fighting games** - 2D sprite-based (Blitter scaling for zoom)
- **Platformers** - 2D scrolling (Object Processor layers)
- **Racing games** - 3D perspective, texture-mapped roads
- **FMV adventures** - Cinepak playback (Jaguar CD)
- **Sports games** - Cybermorph-style (polygon 3D)
- **Puzzle games** - Tetris-style with Blitter effects
- **Shooters** - Tempest 2000 (Jaguar's killer app!)

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum polygon counts, complex multi-processor coordination, advanced 3D techniques, CD streaming mastery

#### Limit-Pushing Techniques:
- **Maximum polygons** - 10,000+ polygons/sec (GPU optimized)
- **Advanced texturing** - Perspective-correct texture mapping
- **Particle systems** - GPU-accelerated particles
- **Complex object lists** - 1000+ objects via Object Processor
- **Multi-DSP audio** - All audio processing on Jerry (free up GPU)
- **CD streaming mastery** - Zero loading times (continuous streaming)
- **Blitter fill-rate** - Full-screen effects at 60 FPS
- **RISC optimization** - Cycle-perfect GPU/DSP code

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial-quality 3D games, professional multi-processor architecture, showcase titles

#### Commercial Techniques:
- **Commercial 3D** - Alien vs Predator, Wolfenstein 3D quality
- **Tempest 2000** - Vector graphics emulation, complex effects
- **Professional audio** - Multi-channel DSP mixing, music
- **Polish effects** - Screen transitions, particle effects, dynamic lighting
- **CD production** - Full CD titles with FMV, CD-DA audio
- **Attract modes** - Demo playback, high score tables
- **Save systems** - EEPROM cartridge saves
- **Multi-tap support** - 4-player games via Team Tap

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, flash cartridge features, community collaboration

#### Modern Development:
- **Virtual Jaguar emulator** - Cross-platform, debugging features
- **RMAC/RASM assemblers** - Modern Jaguar toolchain
- **Jaguar Development Tools** - BJL (Jaguar Boot Loader), Skunkboard
- **Flash cartridge development** - Skunkboard, GameDrive (large ROMs)
- **Modern C compilers** - GCC 6502 port for Jaguar
- **Graphics tools** - Texture converters, 3D model exporters
- **Audio tools** - Sample converters, MOD trackers
- **Community techniques** - AtariAge homebrew scene, annual competitions
- **Cross-platform patterns** - Techniques from other 32-bit systems
- **Modern compression** - LZ4, ZX0 for larger games

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 complex techniques
3. **CD Patterns (Phase 3)** - 50 CD-ROM-specific
4. **Optimization Patterns (Phase 4-5)** - 100 multi-processor techniques
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Base Jaguar (1993)**
- 68000 @ 13.295 MHz (general control)
- Tom (GPU): 32-bit RISC @ 26.6 MHz (graphics workhorse)
- Jerry (DSP): 32-bit RISC @ 26.6 MHz (audio, can do graphics)
- Object Processor: hardware display list
- Blitter: hardware bitmap operations
- 2MB RAM (huge for 1993!)
- 16-bit RGB565 color (65,536 simultaneous)
- 32-bit cartridge ROM bus
- 6MB typical cartridge size
- Controller: 3-button + numeric keypad + Option/Pause

**Phase 3+: Jaguar CD (1995)**
- +CD-ROM drive (2× speed, 300 KB/s)
- +CD-DA audio (Redbook audio)
- +FMV support (Cinepak codec)
- +VLM (Virtual Light Machine) visualization
- +128KB extra RAM
- +650MB storage (vs 6MB cartridge)
- All base features unchanged

**Phase 7-8: Modern Homebrew**
- Skunkboard or GameDrive (flash cartridge, debugging)
- Modern development tools (Virtual Jaguar, RMAC, BJL)
- Flash cartridge features (save states, debugging)
- Modern compression (larger games)
- 32MB+ ROMs possible (banking)

## Spiral Learning Example: 3D Shooter (Jaguar's Strength!)

**Phase 1 (Tier 8):** Simple 3D room (4 walls, textured), player movement, GPU rendering. (~150 lines assembly)

**Phase 2 (Tier 24):** Multiple rooms, doors, enemies (sprites), collision detection. GPU + DSP coordination. (~500 lines)

**Phase 3 (Tier 38):** CD version - streaming music (CD-DA), FMV intro, larger levels. (~800 lines)

**Phase 4 (Tier 46):** Advanced 3D - multiple floors, stairs, complex geometry, AI pathfinding. (~1200 lines)

**Phase 5 (Tier 50):** Weapons, power-ups, complex enemy AI, DSP positional audio. (~1600 lines)

**Phase 6 (Tier 54):** Doom-quality - many enemies, particle effects, dynamic lighting. (~2000 lines)

**Phase 7 (Tier 57):** Alien vs Predator quality - professional 3D, complex levels, polish. (~3000 lines)

**Phase 8 (Tier 59):** Modern homebrew - additional features, debug tools, GameDrive support. (~3000 lines + tooling)

## Key Differences from Other Platforms

1. **Three Processors!** - 68000 (control) + Tom GPU (graphics) + Jerry DSP (audio) - coordination is the CHALLENGE
2. **"64-bit" Marketing** - Actually 32-bit processors with 64-bit data paths (misleading marketing)
3. **Object Processor** - Hardware display list (unique architecture, like Amiga but more complex)
4. **No Dedicated Tilemap** - Everything via Object Processor or GPU rendering
5. **RISC Graphics** - Tom GPU is 32-bit RISC @ 26.6 MHz (unusual for 1993)
6. **Notoriously Difficult** - Multi-processor coordination makes programming very challenging
7. **2MB RAM** - Huge for 1993 (but needed for complex 3D)
8. **65,536 Simultaneous Colors** - RGB565 (more than SNES/Genesis)
9. **Jaguar CD** - CD-ROM with FMV support (competed with Sega CD, 3DO)
10. **Commercial Failure** - Only 250K units sold, but cult following and active homebrew

## Assessment Strategy

**Formative Assessment:**
- Code challenges at end of each tier (e.g., "Add GPU-rendered particles")
- Pattern recognition exercises ("Identify the multi-processor sync pattern")
- Debugging challenges ("Fix the GPU/DSP coordination issue")
- Performance optimization tasks ("Move rendering from 68000 to GPU")

**Summative Assessment:**
- End of each phase: Complete multi-processor game from scratch
- Must demonstrate all patterns learned in that phase
- Rubric covers: code structure, processor utilization, visual quality, performance
- Peer review component (code sharing within cohort)

**Phase Milestones:**
- **Phase 1:** Complete working game (68000 + Object Processor)
- **Phase 2:** Game with GPU graphics, DSP audio (multi-processor)
- **Phase 3:** Jaguar CD title (streaming, CD-DA, FMV)
- **Phase 4:** Advanced 3D game (textured polygons, complex scenes)
- **Phase 5:** Genre-mastery project (3D shooter/racer/fighting/platformer)
- **Phase 6:** Technical showcase (10,000+ polygons, complex audio)
- **Phase 7:** Commercial-quality 3D game (AvP/Doom quality)
- **Phase 8:** Modern homebrew with community release

## Success Criteria

**By Phase 4, learners can:**
- Write 68000 assembly fluently (Motorola 68K)
- Program Tom GPU (32-bit RISC graphics processor)
- Program Jerry DSP (32-bit RISC audio processor)
- Coordinate three processors efficiently (68000↔GPU↔DSP)
- Master Object Processor (display list programming)
- Implement 3D graphics (GPU-rendered polygons, textures)
- Create complex audio (DSP sample mixing)

**By Phase 8, learners can:**
- Develop commercial-quality Jaguar games
- Push multi-processor architecture to limits (10,000+ polygons)
- Work with modern homebrew tools (Virtual Jaguar, RMAC, Skunkboard)
- Contribute to active Jaguar homebrew community
- Master Jaguar CD development (streaming, FMV)
- Implement advanced 3D techniques (perspective textures, lighting)
- Release and distribute homebrew titles

## Resources Required

**Phase 1-2:**
- Virtual Jaguar emulator (cross-platform, accurate, free)
- RMAC/RASM assemblers
- Text editor
- Atari Jaguar reference documentation (68000, Tom, Jerry, Object Processor)
- Skunkboard or BJL (for real hardware testing)

**Phase 3+:**
- Jaguar CD emulation/hardware (for CD development)
- CD burning tools (for CD-ROM creation)
- Cinepak encoder (for FMV)

**Phase 7-8:**
- Skunkboard or GameDrive (flash cartridge, debugging)
- Original Atari Jaguar (optional)
- GCC compiler (for C programming option)
- Modern graphics tools (3D modelers, texture converters)
- Audio tools (sample converters, MOD trackers)
- Community resources (AtariAge forums, homebrew scene)

**All Phases:**
- Version control (Git)
- Bug tracking
- Community engagement (for feedback and collaboration)

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study (assuming ~3 lessons per week)
**Unique Advantage:** Multi-processor coordination mastery (3 processors!), RISC graphics/audio programming, Object Processor display list expertise, advanced 3D techniques, notoriously challenging architecture (builds expertise in complex systems)
