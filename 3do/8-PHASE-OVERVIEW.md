# 3DO Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** 3DO Interactive Multiplayer (1993-1996) → Multiple manufacturers (Panasonic FZ-1, GoldStar, Sanyo)
**Approach:** Game-first, pattern library, ARM/CEL mastery, CD-ROM multimedia
**Gateway:** Direct to assembly (no BASIC, though some development used C)
**Historical Note:** First "open standard" console (multiple manufacturers!), very powerful for 1993 (ARM60 + dual custom chips), expensive ($699 launch!), CD-ROM multimedia focus, 2 million units sold, competed with Saturn/PlayStation, commercial failure despite advanced hardware, pioneered licensing model that influenced PlayStation

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** 3DO shipped without built-in BASIC. Most commercial development used C (3DO SDK), but assembly programming possible and powerful. Curriculum begins with assembly, acknowledging C hybrid development in later phases.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** ARM60 fundamentals, CEL engine (2D graphics), CLIO (I/O), MADAM (math accelerator), CD-ROM access, 2MB RAM, true color graphics
**Professional Autoload:** From lesson 1, all programs professionally load from CD-ROM

#### Pattern Library Established:
- **ARM60 patterns** - 32-bit RISC ARM @ 12.5MHz (powerful for 1993!)
- **CEL engine patterns** - Hardware 2D graphics (sprite scaling, transparency, blending)
- **CLIO patterns** - I/O processor (CD-ROM, controllers, expansion)
- **MADAM patterns** - Math accelerator (16.6MHz, matrix operations, 3D support)
- **True color graphics** - 24-bit RGB (16.7 million colors!), 320×240 / 640×480 resolution
- **CD-ROM access** - 2× speed (300KB/s), streaming
- **2MB RAM** - Huge for 1993 (unified memory architecture)
- **CEL animation** - Hardware cel blending, scaling, rotation
- **CD-DA audio** - Redbook audio + compressed audio
- **32-bit architecture** - First pure 32-bit home console (vs Saturn/PS1 hybrid designs)

#### Example Tier 1 Lesson: "Your First CEL Sprite"
```asm
; 3DO Assembly - Lesson 001
; Display and move a CEL sprite
; ARM60 @ 12.5 MHz

; 3DO uses CEL engine for all graphics
; CELs are hardware-accelerated 2D sprites with scaling/rotation/blending

        .ARM                    ; ARM mode (32-bit)
        .GLOBAL _start

_start:
        ; Initialize 3DO hardware
        BL      Init3DO

        ; Create CEL for sprite (ball)
        LDR     R0,=SPRITE_DATA ; Sprite pixel data
        MOV     R1,#32          ; Width 32 pixels
        MOV     R2,#32          ; Height 32 pixels
        MOV     R3,#160         ; X position (center)
        MOV     R4,#120         ; Y position (center)
        BL      CreateCEL
        MOV     R5,R0           ; Save CEL handle

MainLoop:
        ; Wait for vertical blank
        BL      WaitVBL

        ; Read controller input
        BL      ReadController
        TST     R0,#BUTTON_RIGHT
        BLNE    MoveRight
        TST     R0,#BUTTON_LEFT
        BLNE    MoveLeft

        ; Update CEL position
        MOV     R0,R5           ; CEL handle
        LDR     R1,=XPos
        LDR     R1,[R1]
        LDR     R2,=YPos
        LDR     R2,[R2]
        BL      SetCELPosition

        ; Render frame
        BL      RenderFrame

        B       MainLoop

MoveRight:
        LDR     R0,=XPos
        LDR     R1,[R0]
        ADD     R1,R1,#1        ; Move right
        CMP     R1,#320-32      ; Check boundary
        MOVGE   R1,#0           ; Wrap
        STR     R1,[R0]
        MOV     PC,LR

MoveLeft:
        LDR     R0,=XPos
        LDR     R1,[R0]
        SUB     R1,R1,#1        ; Move left
        CMP     R1,#0
        MOVLT   R1,#320-32      ; Wrap
        STR     R1,[R0]
        MOV     PC,LR

Init3DO:
        ; Initialize 3DO system
        ; - Set up frame buffer
        ; - Initialize CEL engine
        ; - Initialize CLIO (I/O)
        ; (Calls to 3DO BIOS routines)
        LDR     R0,=BIOSInitVideo
        MOV     LR,PC
        MOV     PC,R0
        MOV     PC,LR

CreateCEL:
        ; Create hardware CEL
        ; R0 = pixel data, R1 = width, R2 = height, R3 = X, R4 = Y
        ; Returns CEL handle in R0
        ; (Calls to 3DO CEL engine)
        STMFD   SP!,{R1-R4,LR}
        LDR     R5,=BIOSCreateCEL
        MOV     LR,PC
        MOV     PC,R5
        LDMFD   SP!,{R1-R4,PC}

SetCELPosition:
        ; Update CEL position
        ; R0 = CEL handle, R1 = X, R2 = Y
        STMFD   SP!,{R0-R2,LR}
        LDR     R3,=BIOSSetCELPos
        MOV     LR,PC
        MOV     PC,R3
        LDMFD   SP!,{R0-R2,PC}

RenderFrame:
        ; Render all CELs to frame buffer
        LDR     R0,=BIOSRender
        MOV     LR,PC
        MOV     PC,R0
        MOV     PC,LR

ReadController:
        ; Read controller state, return in R0
        LDR     R1,=BIOSReadPad
        MOV     LR,PC
        MOV     PC,R1
        MOV     PC,LR

WaitVBL:
        ; Wait for vertical blank
        LDR     R0,=BIOSWaitVBL
        MOV     LR,PC
        MOV     PC,R0
        MOV     PC,LR

; Data
XPos:           .WORD   160
YPos:           .WORD   120

SPRITE_DATA:
        ; 32×32 16-bit RGB565 sprite data (ball)
        .INCBIN "ball32x32.rgb"

; 3DO BIOS function addresses (example addresses)
BIOSInitVideo:  .WORD   0x00300000
BIOSCreateCEL:  .WORD   0x00300100
BIOSSetCELPos:  .WORD   0x00300200
BIOSRender:     .WORD   0x00300300
BIOSReadPad:    .WORD   0x00300400
BIOSWaitVBL:    .WORD   0x00300500

BUTTON_RIGHT:   .EQU    0x0001
BUTTON_LEFT:    .EQU    0x0002
```

**Key teaching moment:** 3DO uses CEL ENGINE for all graphics - hardware-accelerated 2D sprites with scaling, rotation, transparency, blending. ARM60 is 32-bit RISC (very powerful for 1993!). MADAM math accelerator helps with 3D. TRUE COLOR graphics (16.7 million colors!). 2MB unified RAM (huge!). CD-ROM 2× speed. First "open standard" console (multiple manufacturers).

**Tier progression:**
1. CEL sprite basics (hardware 2D engine)
2. Multiple CELs (sprite layering, priority)
3. CEL scaling (hardware zoom)
4. CEL rotation (hardware rotation)
5. CEL transparency (alpha blending)
6. Controller input (3DO gamepad, 8-way + buttons)
7. CD-ROM access (2× speed, 300KB/s)
8. Audio playback (CD-DA, compressed audio)
9. MADAM basics (math accelerator, matrix operations)
10. 2MB RAM management (unified memory)
11. True color graphics (24-bit RGB)
12. Frame buffer access (320×240 / 640×480)
13. CD streaming (continuous data loading)
14. Save data (NVRAM)
15. Polish patterns (CEL effects, audio)
16. Complete 3DO mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced CEL techniques, MADAM 3D, CD streaming, FMV integration, complex audio mixing, large-scale games

#### New Patterns:
- **Advanced CEL effects** - Multi-layer blending, complex scaling/rotation
- **MADAM 3D** - Matrix operations for 3D rendering (software + hardware assist)
- **CD streaming mastery** - 300KB/s utilization, zero loading
- **FMV integration** - Cinepak/Duckling video codecs
- **Multi-channel audio** - CD-DA + compressed samples + sound effects
- **Large game assets** - 650MB CD capacity
- **NVRAM patterns** - Save game data
- **Multi-player** - Link cable for 2-8 players (rare feature!)
- **3D rendering** - Software 3D with MADAM acceleration
- **Texture mapping** - Affine texture mapping
- **Lighting effects** - CEL blending for dynamic lighting
- **Particle systems** - Many scaled/rotated CELs

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Multiple manufacturer models + M2 (cancelled)
**Focus:** FZ-1 (Panasonic), FZ-10 (Panasonic), GoldStar model, Sanyo TRY, cross-compatibility

#### Phase 3 Enhancement: Multiple Manufacturers
- **Panasonic FZ-1** (1993) - Original "REAL" 3DO
- **Panasonic FZ-10** (1994) - Front-loading, cheaper ($399)
- **GoldStar 3DO** (1994) - Third-party manufacturer
- **Sanyo TRY** (1994) - Japanese market
- **Goldstar Alive II** (1995) - Korea
- **All 100% compatible** - Same hardware, different cases/features
- **M2 (cancelled 1997)** - Planned successor, never released (PowerPC 602!)

**Note:** All 3DO models have identical capabilities. Phase 3 focuses on optimization for all models and understanding the "open standard" concept.

**Tier 40 Example - Model Detection (for logging/statistics):**
```asm
; Detect specific 3DO model (purely informational)

DetectModel:
        ; Read 3DO ROM version
        LDR     R0,=0x03000000  ; ROM base
        LDR     R1,[R0,#0x10]   ; Version string offset
        ADD     R1,R0,R1
        ; R1 now points to version string
        ; "PANASONIC FZ-1", "PANASONIC FZ-10", "GOLDSTAR", etc.
        MOV     PC,LR

; All models have identical capabilities, detection is for
; informational purposes only (logging, statistics)
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional game architecture, 3D engine development, complex CEL effects, CD optimization, FMV mastery

#### Advanced Techniques:
- **3D game engines** - Software 3D with MADAM acceleration
- **CEL optimization** - Maximum sprites, efficient rendering
- **CD streaming engines** - Zero-load continuous streaming
- **FMV/gameplay hybrid** - Video during gameplay (not just cutscenes)
- **Complex audio mixing** - CD-DA + multiple compressed streams
- **Texture mapping** - Perspective-correct via MADAM
- **Z-buffering** - Software depth sorting with hardware assist
- **Lighting** - Dynamic lighting via CEL blending
- **Physics engines** - ARM60 processing power
- **AI systems** - Complex game AI (plenty of CPU!)

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** FMV games, 3D action, fighting games, multimedia titles, CD-DA RPGs

#### Genre Specializations:
- **FMV interactive movies** - 3DO known for these (Mad Dog McCree, etc.)
- **3D action/adventure** - Gex, Crash 'N Burn (3DO's strength!)
- **Fighting games** - Super Street Fighter II Turbo (arcade perfect!)
- **RPGs** - CD-DA music, voice acting, large worlds
- **Shooters** - Arcade ports (Star Control II, etc.)
- **Sports games** - FIFA, Madden (EA supported 3DO!)
- **Puzzle games** - Tetris, puzzle collections
- **Multimedia** - Educational, reference (CD-ROM multimedia era!)

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum 3D polygon counts, complex CEL layering, FMV quality, CD streaming optimization

#### Limit-Pushing Techniques:
- **Maximum polygons** - Software 3D + MADAM: 50,000-80,000 polys/sec
- **CEL showcase** - Hundreds of scaled/rotated/blended CELs
- **FMV quality** - Best possible Cinepak encoding
- **CD streaming perfection** - Full 300KB/s utilization
- **Audio complexity** - All channels simultaneously
- **Texture mapping** - High-resolution textures from CD
- **Dynamic lighting** - Complex CEL blending
- **Particle effects** - Thousands of particles via CELs

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial-quality 3D games, professional FMV, showcase titles

#### Commercial Techniques:
- **Commercial 3D** - Need for Speed, Crash 'N Burn quality
- **FMV showcases** - Mad Dog McCree, Sewer Shark quality
- **Fighting game polish** - Super Street Fighter II Turbo quality
- **RPG production** - Lucienne's Quest, Guardian War quality
- **Professional audio** - Full CD-DA soundtracks, voice acting
- **Attract modes** - FMV attract sequences
- **Multimedia integration** - Interactive multimedia (CD-ROM era!)
- **EA sports titles** - FIFA, Madden, NHL (3DO had strong EA support!)

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, CD burning, emulation

#### Modern Development:
- **4DO / FreeDO emulators** - 3DO emulation, debugging
- **Modern ARM assemblers** - GNU AS, modern toolchains
- **3DO SDK modern ports** - Updated development kits
- **CD mastering tools** - ISO creation for 3DO
- **FMV encoding** - Modern Cinepak encoders
- **Community techniques** - Active 3DO homebrew preservation
- **Cross-platform ARM** - ARM knowledge transfers to many platforms
- **Modern compression** - Better tools than 1990s
- **ODE (Optical Disc Emulator)** - Flash storage replacement for CD drive

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 complex techniques
3. **Multi-manufacturer Patterns (Phase 3)** - 50 cross-compatibility
4. **Optimization Patterns (Phase 4-5)** - 100 ARM + CEL + MADAM techniques
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: 3DO (1993, all models)**
- ARM60 @ 12.5MHz (32-bit RISC)
- CLIO @ 25MHz (I/O processor: CD, controllers, expansion)
- MADAM @ 16.6MHz (math accelerator: matrix ops, 3D assist)
- 2MB DRAM + 1MB VRAM = 3MB total
- CEL engine: hardware 2D (sprites, scaling, rotation, transparency, blending)
- 320×240 or 640×480 resolution
- True color: 24-bit RGB (16.7 million colors!)
- CD-ROM 2× speed (300KB/s)
- CD-DA audio (Redbook) + compressed audio
- NVRAM (32KB save memory)
- Expansion port (link cable for multiplayer)

**Phase 3+: Multiple Manufacturers (all identical capabilities)**
- Panasonic FZ-1, FZ-10
- GoldStar 3DO
- Sanyo TRY
- 100% hardware compatible

**Phase 7-8: Modern Homebrew**
- CD-R burning (create custom 3DO games)
- ODE (Optical Disc Emulator) flash storage
- Modern development tools (4DO, FreeDO, ARM toolchains)
- Modern compression (more content in 650MB)

## Spiral Learning Example: 3D Racing Game

**Phase 1 (Tier 5):** Simple 3D road (MADAM-assisted), player car (CEL), forward movement. (~200 lines assembly + 3D math)

**Phase 2 (Tier 22):** Opponent cars, track curves, collision, CD-DA music. (~500 lines)

**Phase 3 (Tier 37):** Cross-model testing (FZ-1, FZ-10, GoldStar), optimization. (~700 lines)

**Phase 4 (Tier 46):** Multiple tracks (streaming from CD), texture-mapped road, FMV intro. (~1100 lines)

**Phase 5 (Tier 50):** Full racing game - championship, many tracks, complex AI. (~1500 lines)

**Phase 6 (Tier 54):** Maximum 3D detail, advanced lighting (CEL blending), high-res textures. (~2000 lines)

**Phase 7 (Tier 57):** Need for Speed quality - professional 3D, FMV, CD-DA soundtrack. (~2800 lines)

**Phase 8 (Tier 59):** Modern homebrew - additional content, modern tools, ODE support. (~2800 lines + tooling)

## Key Differences from Other Platforms

1. **First "Open Standard"** - Multiple manufacturers (Panasonic, GoldStar, Sanyo), all compatible
2. **Pure 32-bit RISC** - ARM60 @ 12.5MHz (vs Saturn/PS1 hybrid designs)
3. **CEL Engine** - Hardware 2D sprites with scaling, rotation, transparency, blending
4. **MADAM Math Accelerator** - Dedicated 3D assist chip (16.6MHz)
5. **True Color** - 24-bit RGB (16.7 million colors) vs 16-bit on most platforms
6. **2MB Unified RAM** - Large for 1993, unified memory architecture
7. **CD-ROM 2× Speed** - 300KB/s (2× faster than Sega CD, same as PS1)
8. **Expensive Launch** - $699 (vs PS1 $299, Saturn $399) - major commercial problem
9. **Strong EA Support** - FIFA, Madden, NHL (EA was early supporter)
10. **Multimedia Focus** - CD-ROM multimedia era (games, education, reference)

## Assessment Strategy

**Formative Assessment:**
- Code challenges at end of each tier (e.g., "Add 3D rendering with MADAM")
- Pattern recognition exercises ("Identify the CEL optimization")
- Debugging challenges ("Fix the CD streaming buffer underrun")
- Performance optimization tasks ("Increase polygon count by 20%")

**Summative Assessment:**
- End of each phase: Complete 3DO game from scratch
- Must demonstrate all patterns learned in that phase
- Rubric covers: code structure, CEL/MADAM utilization, CD streaming
- Peer review component (code sharing within cohort)

**Phase Milestones:**
- **Phase 1:** Complete working 3DO game (CELs, CD-ROM, audio)
- **Phase 2:** Game with 3D rendering (MADAM), advanced CEL effects
- **Phase 3:** Cross-model compatible game (all manufacturers)
- **Phase 4:** Advanced 3D game (texture mapping, lighting)
- **Phase 5:** Genre-mastery project (FMV/3D/fighting/RPG)
- **Phase 6:** Technical showcase (maximum 3D/CEL usage)
- **Phase 7:** Commercial-quality 3D or FMV game
- **Phase 8:** Modern homebrew with community release (CD-R/ODE)

## Success Criteria

**By Phase 4, learners can:**
- Program ARM60 assembly fluently (32-bit RISC)
- Master CEL engine (hardware 2D with scaling/rotation/blending)
- Program MADAM (math accelerator for 3D)
- Implement CD-ROM streaming (2× speed, 300KB/s)
- Create 3D games (software + hardware assist)
- Work with 2MB unified RAM efficiently
- Implement true color graphics (24-bit RGB)

**By Phase 8, learners can:**
- Develop commercial-quality 3DO games
- Push ARM/CEL/MADAM to limits (maximum 3D polygons, CEL effects)
- Work with modern homebrew tools (4DO, FreeDO, ODE)
- Contribute to 3DO preservation and homebrew
- Create CD-Rs for real hardware
- Understand "open standard" console model
- Release and distribute homebrew titles

## Resources Required

**Phase 1-2:**
- 4DO or FreeDO emulator (cross-platform, accurate, free)
- GNU ARM assembler (or modern ARM toolchain)
- Text editor
- 3DO reference documentation (ARM60, CEL, CLIO, MADAM)
- 3DO SDK documentation (even for assembly, understanding APIs helps)

**Phase 3+:**
- Multiple model testing (FZ-1, FZ-10 emulation)

**Phase 7-8:**
- CD burning software (ISO creation for 3DO)
- 3DO hardware (optional, for real testing)
- ODE (Optical Disc Emulator, modern replacement for CD drive)
- FMV encoding tools (Cinepak encoders)
- Community resources (3DO forums, preservation groups)

**All Phases:**
- Version control (Git)
- Bug tracking
- Community engagement (preservation efforts)

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study (assuming ~3 lessons per week)
**Unique Advantage:** ARM assembly mastery (32-bit RISC!), CEL engine expertise (hardware 2D effects), MADAM 3D acceleration, true color graphics, understanding "open standard" console model, CD-ROM multimedia era, ARM knowledge transfers to many modern platforms (smartphones, Raspberry Pi, etc.)
