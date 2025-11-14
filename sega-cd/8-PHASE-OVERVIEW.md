# Sega CD Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Sega CD / Mega-CD (1991-1996) → Genesis + Sega CD dual-68000 architecture
**Approach:** Game-first, pattern library, dual-68000 coordination, CD-ROM mastery
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Genesis add-on (1991), adds second 68000 @ 12.5MHz + CD-ROM + CD-DA audio + 6× more RAM, pioneered console CD-ROM gaming, FMV (full-motion video) games, 2.24 million units sold (Japan/US), competed with TurboGrafx-CD, paved way for PlayStation/Saturn CD-ROM era

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Sega CD is a Genesis add-on, no BASIC interpreter. Curriculum begins directly with assembly, building on Genesis knowledge while focusing on CD-specific features.

**Prerequisite Knowledge:** Genesis/Mega Drive assembly programming (68000, VDP, Z80). This curriculum focuses on SEGA CD-SPECIFIC features: second 68000, CD-ROM, scaling/rotation chip, additional RAM.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** Second 68000 fundamentals, dual-68000 coordination, CD-ROM access, CD-DA audio, scaling/rotation chip, 6× more RAM (768KB total!)
**Professional Autoload:** From lesson 1, all programs professionally load from CD-ROM

#### Pattern Library Established:
- **Dual-68000 patterns** - Main 68000 @ 7.67MHz (Genesis) + Sub 68000 @ 12.5MHz (Sega CD)
- **CD-ROM access** - 150KB/s (1× speed), sector reading, streaming
- **CD-DA audio** - Redbook audio tracks (44.1kHz stereo, full quality!)
- **Scaling/rotation chip** - Hardware sprite/background scaling and rotation (revolutionary!)
- **6× more RAM** - Genesis 64KB + Sega CD 512KB PRG-RAM + 256KB Word RAM = 832KB total!
- **Communication** - Main CPU ↔ Sub CPU via shared Word RAM and registers
- **ASIC graphics** - Custom chip for scaling/rotation (like SNES Mode 7!)
- **PCM audio** - 8-channel PCM samples (in addition to Genesis YM2612/PSG!)
- **Backup RAM** - Battery-backed save RAM (revolutionary for 1991!)
- **FMV playback** - Cinepak codec for full-motion video

#### Example Tier 1 Lesson: "Your First CD-ROM Read"
```asm
; Sega CD Assembly - Lesson 001
; Read sector from CD-ROM and display
; Sub CPU (68000 @ 12.5 MHz) handles CD

;-------------------------------------------------
; SUB CPU CODE (runs on Sega CD 68000 @ 12.5MHz)
;-------------------------------------------------
        .ORG    $00000000

SUB_ENTRY:
        ; Initialize Sub CPU
        move.w  #$2700,sr       ; Disable interrupts
        move.l  #$00006000,sp   ; Set stack

        ; Initialize CD-ROM drive
        jsr     CD_INIT

        ; Read sector 150 (first data sector, 2 seconds in)
        move.l  #150,d0         ; Sector number
        move.l  #$00020000,a0   ; Destination in PRG-RAM
        jsr     CD_READ_SECTOR

        ; Tell main CPU data is ready
        move.w  #$0001,$FFFF800A ; Set flag in comms register

WAIT_MAIN:
        ; Wait for main CPU to process
        move.w  $FFFF800C,d0    ; Read main CPU flag
        beq     WAIT_MAIN

        ; Main CPU done, we can continue
        bra     SUB_ENTRY       ; Loop

CD_INIT:
        ; Initialize CD-ROM BIOS
        move.w  #$0000,$FFF802  ; CD command: INIT
        rts

CD_READ_SECTOR:
        ; Read single sector from CD
        ; d0.l = sector number
        ; a0   = destination address
        move.l  d0,$FFF804      ; Set sector number
        move.l  a0,$FFF808      ; Set destination
        move.w  #$0001,$FFF802  ; CD command: READ
.WAIT:  move.w  $FFF802,d1      ; Check status
        bne     .WAIT           ; Wait for completion
        rts

;-------------------------------------------------
; MAIN CPU CODE (runs on Genesis 68000 @ 7.67MHz)
;-------------------------------------------------
        .ORG    $00000000       ; Genesis ROM space

MAIN_ENTRY:
        ; Standard Genesis initialization
        move.w  #$2700,sr
        move.l  #$00FF0000,sp

        ; Initialize Genesis VDP
        jsr     VDP_INIT

        ; Wait for Sub CPU to load data
WAIT_SUB:
        move.w  $A12000,d0      ; Read comms register (Sub→Main)
        beq     WAIT_SUB        ; Wait for flag from Sub CPU

        ; Sub CPU has loaded data!
        ; Access data via Word RAM (bank-switched)
        move.w  #$0001,$A12002  ; Request Word RAM access
.WAIT_RAM:
        move.w  $A12002,d0
        beq     .WAIT_RAM       ; Wait for Word RAM ownership

        ; Copy data from Word RAM to Genesis RAM
        lea     $200000,a0      ; Word RAM (from Main CPU perspective)
        lea     $FF0000,a1      ; Genesis RAM
        move.w  #2048-1,d0      ; 2048 bytes (one sector)
.COPY:  move.b  (a0)+,(a1)+
        dbf     d0,.COPY

        ; Display "DATA LOADED" message on screen
        ; (VDP code omitted for brevity)

        ; Tell Sub CPU we're done
        move.w  #$0001,$A12004  ; Set flag (Main→Sub)

        ; Return Word RAM to Sub CPU
        move.w  #$0000,$A12002

        bra     WAIT_SUB        ; Loop

VDP_INIT:
        ; Standard Genesis VDP initialization
        ; (Code omitted for brevity)
        rts
```

**Key teaching moment:** Sega CD has TWO 68000 CPUs! Main CPU (Genesis 7.67MHz) handles display/control, Sub CPU (Sega CD 12.5MHz) handles CD-ROM/audio. They communicate via Word RAM (bank-switched) and comms registers. This is CRITICAL pattern! CD-ROM is slow (150KB/s), must stream carefully. CD-DA audio is CD-quality (revolutionary for 1991!). Scaling/rotation chip provides SNES Mode 7-like effects!

**Tier progression:**
1. CD-ROM sector reading (Sub CPU controls CD)
2. Main/Sub CPU communication (Word RAM, comms registers)
3. CD-DA audio playback (Redbook audio tracks)
4. Scaling chip basics (sprite scaling/rotation)
5. PCM audio (8-channel samples on Sub CPU)
6. Word RAM bank switching (2×128KB banks)
7. CD streaming (continuous data loading)
8. Backup RAM (save games - revolutionary!)
9. FMV basics (Cinepak playback)
10. Dual-68000 coordination patterns
11. Genesis VDP (same as Genesis curriculum)
12. Large game assets (CD holds 650MB!)
13. Multi-track audio (CD-DA + PCM + YM2612)
14. Load time optimization (hide loading!)
15. Polish patterns (CD features showcase)
16. Complete Sega CD mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced dual-68000 techniques, CD streaming mastery, FMV integration, scaling/rotation effects, massive game assets

#### New Patterns:
- **Dual-68000 optimization** - Load balancing (Main: display, Sub: CD/audio/processing)
- **CD streaming engines** - Continuous level loading, zero visible loading
- **FMV integration** - Cinepak decoding, video playback in gameplay
- **Scaling/rotation mastery** - ASIC chip for Mode 7-like effects
- **Multi-track audio** - CD-DA music + PCM effects + Genesis YM2612/PSG
- **Large level data** - 650MB CD capacity (vs 4MB Genesis cartridge!)
- **Word RAM choreography** - Efficient bank switching, DMA transfers
- **Backup RAM patterns** - Save systems, progress tracking
- **Mixed-mode CDs** - Audio tracks + data tracks
- **Pre-rendered graphics** - Large sprite sheets from CD
- **Voice acting** - PCM voice samples from CD
- **Dynamic loading** - Load assets based on player location

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Sega CD Model 2 (1993) + 32X compatibility
**Focus:** Model 2 cost reduction (same capabilities), 32X pass-through (Genesis + Sega CD + 32X = triple-processor!), optimization for all models

#### Phase 3 Enhancement: Model 2 & 32X Compatibility
- **Sega CD Model 2** (1993) - Smaller, cheaper, same capabilities as Model 1
- **32X pass-through** - Genesis + Sega CD + 32X = 5 processors total! (2×68000 + Z80 + 2×SH-2)
- **Triple-platform games** - Games that run on Genesis, enhanced on Sega CD, further enhanced on CD+32X
- **Backward compatibility** - All Sega CD Model 1 games work on Model 2

**Note:** 32X + Sega CD combination was rare (only ~10 games). Phase 3 focuses on Model 2 optimization and understanding the 32X compatibility layer.

**Tier 40 Example - Triple-Platform Enhancement Detection:**
```asm
; Detect Genesis / Sega CD / Sega CD+32X and enable features

DETECT_HARDWARE:
        ; Check if running on Sega CD (vs Genesis)
        move.b  $A10001,d0      ; Read version register
        andi.b  #$0F,d0
        cmpi.b  #$00,d0         ; Japan Genesis
        beq     .GENESIS_ONLY
        ; More checks... (omitted for brevity)

        ; We're on Sega CD! Enable CD features
        move.w  #1,SEGA_CD_FLAG

        ; Check for 32X
        move.l  $A130EC,d0      ; 32X signature
        cmpi.l  #'MARS',d0      ; '32X' signature
        bne     .NO_32X

        ; 32X detected! Enable triple-platform features
        move.w  #1,SEGA_32X_FLAG
        jsr     ENABLE_32X_GRAPHICS
        jsr     ENABLE_32X_AUDIO
        bra     .DONE

.NO_32X:
        ; Sega CD only - use CD features
        jsr     ENABLE_CD_FMV
        jsr     ENABLE_SCALING_CHIP
        bra     .DONE

.GENESIS_ONLY:
        ; No Sega CD - fallback mode
        move.w  #0,SEGA_CD_FLAG
        ; Disable CD-dependent features

.DONE:  rts

SEGA_CD_FLAG:   dc.w 0
SEGA_32X_FLAG:  dc.w 0
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional dual-68000 architecture, advanced CD streaming, FMV mastery, complex audio mixing, large-scale games

#### Advanced Techniques:
- **Dual-CPU pipelines** - Main (display/input) → Sub (CD/audio/processing)
- **Zero-load streaming** - No loading screens (continuous CD streaming)
- **FMV/gameplay integration** - Video playback during gameplay (not just cutscenes)
- **Scaling/rotation 3D** - Pseudo-3D using ASIC chip (racing games!)
- **Multi-layer audio** - CD-DA + 8 PCM channels + YM2612 + PSG = complex mixes
- **Massive game worlds** - 650MB games with streaming
- **Backup RAM mastery** - Complex save systems
- **Word RAM DMA** - Hardware-accelerated transfers
- **CD file systems** - Efficient data organization on CD
- **Pre-rendered 3D** - Store pre-rendered frames on CD, stream for "3D"

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** FMV adventures, CD-DA RPGs, scaling/rotation racing games, large-scale action games

#### Genre Specializations:
- **FMV adventures** - Interactive movies (Sega CD known for this!)
- **RPGs** - Large game worlds, CD-DA music, voice acting
- **Racing games** - Scaling/rotation for Mode 7-like roads
- **Action/adventure** - Large levels streaming from CD
- **Fighting games** - CD-DA music, voice samples
- **Shoot-em-ups** - Pre-rendered graphics, scaling bosses
- **Platformers** - CD-DA soundtracks, large level data
- **Arcade ports** - More accurate (650MB for graphics/audio!)

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum CD streaming, complex FMV, scaling/rotation mastery, dual-68000 optimization

#### Limit-Pushing Techniques:
- **Maximum CD streaming** - Full 150KB/s utilization, zero gaps
- **FMV quality** - Best possible Cinepak encoding
- **Scaling/rotation showcase** - Complex pseudo-3D scenes
- **Dual-68000 efficiency** - Perfect load balancing
- **Full CD capacity** - 650MB games with massive content
- **Multi-track complexity** - All audio systems simultaneously
- **Backup RAM maximization** - Complex save data
- **Pre-rendered showcase** - Near-3D quality via pre-rendered frames

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial-quality CD games, professional FMV integration, showcase titles

#### Commercial Techniques:
- **Commercial FMV games** - Night Trap, Sewer Shark quality
- **CD-DA RPGs** - Lunar: The Silver Star, Final Fantasy quality
- **Racing showcases** - Road Rash CD, Sega Rally quality
- **Professional audio** - Full CD-DA soundtracks, voice acting
- **Large-scale adventures** - Snatcher, Rise of the Dragon quality
- **Arcade-perfect ports** - Using 650MB for perfect accuracy
- **Attract modes** - FMV attract sequences
- **Multi-platform optimization** - Games that run on all models

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, CD burning, emulation

#### Modern Development:
- **Kega Fusion / Gens emulators** - Sega CD emulation, debugging
- **SGDK (Sega Genesis Development Kit)** - Modern toolchain with Sega CD support
- **Modern 68000 assemblers** - VASM, AS, cross-platform
- **CD mastering tools** - ISO creation, Cue/Bin format
- **FMV encoding** - Modern Cinepak encoders
- **Audio mastering** - CD-DA track creation, PCM conversion
- **Community techniques** - Active Sega CD homebrew scene
- **Flash cartridge + CD** - Combined development (MODE + Mega EverDrive Pro)
- **Modern compression** - Better than 1990s tools (more content!)
- **32X compatibility** - Modern triple-platform development

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 complex techniques
3. **Multi-platform Patterns (Phase 3)** - 50 Model 2 + 32X-specific
4. **Optimization Patterns (Phase 4-5)** - 100 dual-68000 + CD streaming
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Sega CD Model 1 (1991)**
- Main 68000 @ 7.67MHz (Genesis CPU)
- Sub 68000 @ 12.5MHz (Sega CD CPU)
- Z80 @ 3.58MHz (sound co-processor, from Genesis)
- 64KB Genesis RAM + 512KB PRG-RAM + 256KB Word RAM = 832KB total (6× Genesis!)
- CD-ROM drive (1× speed, 150KB/s)
- CD-DA audio (Redbook, 44.1kHz stereo)
- ASIC scaling/rotation chip (hardware sprite/BG scaling and rotation)
- PCM audio (8 channels, 8-bit samples)
- Backup RAM (battery-backed saves)
- Cinepak FMV codec support
- Genesis VDP (same as Genesis)
- Genesis YM2612 + PSG (same as Genesis)

**Phase 3+: Sega CD Model 2 (1993) + 32X Compatibility**
- Same specs as Model 1 (cost-reduced design)
- 32X pass-through (optional, adds 2×SH-2 @ 23MHz)
- Smaller, lighter form factor
- Backward compatible with Model 1 games

**Phase 7-8: Modern Homebrew**
- CD-R burning (create custom Sega CD games)
- Modern development tools (SGDK, Kega Fusion, Gens)
- Flash cartridge + CD hybrid development
- Modern compression (more content in 650MB)

## Spiral Learning Example: Racing Game (Sega CD's Strength!)

**Phase 1 (Tier 4):** Simple road (scaling chip!), player car, CD-DA music. Revolutionary scaling! (~150 lines assembly)

**Phase 2 (Tier 20):** Multiple opponent cars (streaming from CD), track variations, PCM engine sounds. (~400 lines)

**Phase 3 (Tier 36):** Model 2 optimization, 32X detection (enhanced graphics if present). (~600 lines)

**Phase 4 (Tier 44):** Multiple tracks (streaming), FMV intro, voice announcer (PCM), Backup RAM saving. (~900 lines)

**Phase 5 (Tier 50):** Full racing game - championship mode, many tracks, complex opponent AI. (~1300 lines)

**Phase 6 (Tier 54):** Maximum scaling effects, pre-rendered track scenery from CD, full CD-DA soundtrack. (~1800 lines)

**Phase 7 (Tier 57):** Road Rash CD / Sega Rally quality - professional polish, FMV cutscenes. (~2500 lines)

**Phase 8 (Tier 59):** Modern homebrew - additional tracks, modern tools, CD-R burning. (~2500 lines + tooling)

## Key Differences from Other Platforms

1. **Genesis Add-On** - Requires Genesis, extends capabilities (not standalone)
2. **Dual-68000 Architecture** - Main (7.67MHz) + Sub (12.5MHz) coordination critical
3. **CD-ROM Pioneer** - One of first console CD-ROM systems (with TurboGrafx-CD)
4. **CD-DA Audio** - Full quality CD audio (44.1kHz stereo)
5. **6× More RAM** - 832KB total (vs Genesis 64KB)
6. **Scaling/Rotation Chip** - Hardware sprite/BG scaling (like SNES Mode 7!)
7. **FMV Capability** - Cinepak full-motion video (pioneered console FMV)
8. **650MB Capacity** - Huge vs 4MB Genesis cartridges
9. **Backup RAM** - Battery-backed saves (revolutionary for 1991)
10. **8-Channel PCM** - High-quality sample playback (in addition to Genesis sound)

## Assessment Strategy

**Formative Assessment:**
- Code challenges at end of each tier (e.g., "Add CD streaming to your game")
- Pattern recognition exercises ("Identify the dual-68000 sync pattern")
- Debugging challenges ("Fix the Word RAM bank-switching")
- Performance optimization tasks ("Reduce CD load time by 50%")

**Summative Assessment:**
- End of each phase: Complete Sega CD game from scratch
- Must demonstrate all patterns learned in that phase
- Rubric covers: code structure, CD utilization, dual-CPU coordination
- Peer review component (code sharing within cohort)

**Phase Milestones:**
- **Phase 1:** Complete working Sega CD game (CD-ROM, CD-DA, dual-68000)
- **Phase 2:** Game with CD streaming, FMV, scaling effects
- **Phase 3:** Multi-platform game (Model 1/2 + optional 32X)
- **Phase 4:** Advanced CD game (zero-load streaming, complex FMV)
- **Phase 5:** Genre-mastery project (FMV adventure/RPG/racer/action)
- **Phase 6:** Technical showcase (maximum CD/FMV/scaling usage)
- **Phase 7:** Commercial-quality CD game
- **Phase 8:** Modern homebrew with community release (CD-R)

## Success Criteria

**By Phase 4, learners can:**
- Program dual-68000 systems fluently (Main + Sub coordination)
- Master CD-ROM access (sector reading, streaming, file systems)
- Implement CD-DA audio (Redbook track playback)
- Program scaling/rotation chip (ASIC hardware)
- Work with large RAM (832KB efficiently)
- Create FMV sequences (Cinepak encoding/playback)
- Implement backup RAM saves

**By Phase 8, learners can:**
- Develop commercial-quality Sega CD games
- Push dual-68000 to limits (perfect load balancing)
- Master CD streaming (zero visible loading)
- Work with modern homebrew tools (SGDK, emulators)
- Create custom CD-Rs (burn homebrew games)
- Contribute to Sega CD homebrew community
- Release and distribute CD-ROM titles

## Resources Required

**Phase 1-2:**
- Kega Fusion or Gens emulator (Sega CD support, free)
- SGDK or 68000 assembler (VASM, AS)
- Text editor
- Sega CD reference documentation (dual-68000, CD-ROM, ASIC)
- Genesis reference (VDP, Z80, YM2612) - see Genesis curriculum

**Phase 3+:**
- Model 2 testing (emulator support)
- 32X emulation (for triple-platform testing)

**Phase 7-8:**
- CD burning software (ISO/Cue/Bin creation)
- Sega CD hardware (optional, for real CD-R testing)
- MODE or Mega EverDrive Pro (flash cart with CD-ROM emulation)
- FMV encoding tools (Cinepak encoders)
- Audio mastering tools (CD-DA track creation)
- Community resources (Sega Retro, homebrew scene)

**All Phases:**
- Version control (Git)
- Bug tracking
- Community engagement (for feedback and collaboration)

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study (assuming ~3 lessons per week)
**Unique Advantage:** Dual-68000 coordination mastery, CD-ROM streaming expertise, FMV integration, scaling/rotation chip programming, CD-DA audio, massive game assets (650MB!), understanding CD-ROM gaming transition era
