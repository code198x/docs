# PC-FX Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** PC-FX (1994-1998, Japan-only) → NEC's 32-bit successor to PC Engine
**Approach:** Game-first, pattern library, 32-bit RISC mastery, anime/FMV focus
**Gateway:** Direct to assembly (no BASIC, though C development common)
**Historical Note:** NEC's final console (1994), successor to PC Engine/TurboGrafx-16, V810 32-bit RISC @ 21.5MHz, CD-ROM only (no cartridge slot), tower design (vertical!), anime/dating sim/visual novel focus, expensive (¥49,800/$500 equivalent), Japan-only, ~400K units sold, 62 games total, competed with Saturn/PlayStation but focused on 2D anime + FMV niche, commercial failure but cult following, NEC exited console market after this

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** PC-FX shipped without BASIC. Most commercial development used C (PC-FX SDK), but assembly programming possible and educational. Curriculum begins with assembly.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** V810 RISC fundamentals, CD-ROM access, 2D sprite system, MJPEG FMV, ADPCM audio, anime-style graphics
**Professional Autoload:** From lesson 1, all programs professionally load from CD-ROM

#### Pattern Library Established:
- **V810 patterns** - NEC V810 @ 21.5MHz (32-bit RISC, rare architecture!)
- **2D sprite system** - Hardware sprites, scrolling layers
- **MJPEG decoder** - Hardware FMV playback (revolutionary for 1994!)
- **CD-ROM patterns** - 2× speed (300KB/s), streaming
- **ADPCM audio** - 32-channel sample playback
- **2MB main RAM** - Large for 1994
- **1.25MB VRAM** - Dedicated video memory
- **256×240 / 341×240** - High-resolution 2D (341 wider than TV!)
- **16.7 million colors** - 24-bit true color
- **Anime graphics focus** - Platform designed for anime-style games

#### Example Tier 1 Lesson: "Your First V810 Sprite"
```asm
; PC-FX Assembly - Lesson 001
; Display sprite using V810 RISC
; V810 @ 21.5 MHz

; V810 is 32-bit RISC with unusual architecture
; 32 general-purpose registers (r0-r31)
; Load/store architecture
; Big-endian

        .v810                   ; V810 mode

        .org    $00000000

; PC-FX boot process
START:  ; Initialize V810
        movhi   hi(stack_top),r0,sp
        movea   lo(stack_top),sp,sp

        ; Initialize video hardware
        jal     InitVideo

        ; Load sprite data to VRAM
        movhi   hi(SPRITE_DATA),r0,r6
        movea   lo(SPRITE_DATA),r6,r6
        mov     0x80000,r7      ; VRAM address
        mov     1024,r8         ; Size (32×32 sprite)
        jal     LoadVRAM

        ; Set sprite position
        mov     160,r6          ; X = 160 (center)
        mov     120,r7          ; Y = 120 (center)
        mov     0,r8            ; Sprite index
        jal     SetSpritePos

        ; Set sprite attributes
        mov     0,r6            ; Sprite index
        mov     1,r7            ; Visible
        mov     0,r8            ; Palette
        jal     SetSpriteAttr

LOOP:   ; Main game loop
        jal     WaitVSync

        ; Read controller
        jal     ReadPad
        ; r10 now contains button state

        ; Check right
        andi    r10,r10,0x0001
        be      CHECK_LEFT
        ; Move right
        ld.w    0[r31],r6       ; Load X pos
        addi    1,r6,r6
        cmp     320,r6
        bl      .UPDATE
        mov     0,r6            ; Wrap
.UPDATE:
        st.w    r6,0[r31]       ; Store X pos
        mov     0,r7            ; Sprite index
        jal     SetSpritePos

CHECK_LEFT:
        ; ... (similar for other directions)

        br      LOOP

; V810 Routines
InitVideo:
        ; Initialize PC-FX video hardware
        ; Set resolution, enable sprites
        mov     0x80000000,r6   ; Video control base
        mov     0x0001,r7       ; Enable display
        st.w    r7,0[r6]
        jmp     [r31]

LoadVRAM:
        ; Load data to VRAM
        ; r6 = source, r7 = dest, r8 = size
.LOOP:  ld.b    0[r6],r9
        st.b    r9,0[r7]
        addi    1,r6,r6
        addi    1,r7,r7
        addi    -1,r8,r8
        bne     .LOOP
        jmp     [r31]

SetSpritePos:
        ; Set sprite X,Y position
        ; r6 = X, r7 = Y, r8 = sprite index
        mov     0x80010000,r9   ; Sprite attr base
        shl     4,r8            ; Index * 16
        add     r8,r9
        st.h    r6,0[r9]        ; X pos
        st.h    r7,2[r9]        ; Y pos
        jmp     [r31]

SetSpriteAttr:
        ; Set sprite attributes
        ; r6 = index, r7 = visible, r8 = palette
        ; ... (implementation)
        jmp     [r31]

WaitVSync:
        ; Wait for vertical sync
        mov     0x80000004,r6
.WAIT:  ld.w    0[r6],r7
        andi    r7,r7,0x8000
        be      .WAIT
        jmp     [r31]

ReadPad:
        ; Read controller
        ; Returns button state in r10
        mov     0x80000008,r6
        ld.w    0[r6],r10
        jmp     [r31]

SPRITE_DATA:
        .incbin "sprite32x32.bin"

        .align  4
stack_top:
        .space  4096
```

**Key teaching moment:** V810 is 32-bit RISC with unusual architecture! 32 general-purpose registers, load/store architecture, big-endian. PC-FX focuses on 2D anime-style games + FMV. MJPEG hardware decoder for video. 2× CD-ROM. High resolution (341×240 wider than TV!). Japan-only, niche market (anime games, visual novels, dating sims). NEC's final console.

**Tier progression:**
1. V810 RISC basics (32 registers, load/store)
2. Sprite system (hardware sprites, attributes)
3. CD-ROM loading (2× speed, file systems)
4. MJPEG FMV playback (hardware decoder!)
5. ADPCM audio (32-channel samples)
6. Controller input (standard PC Engine-style pad)
7. High-resolution modes (341×240 for anime graphics)
8. True color graphics (24-bit, 16.7M colors)
9. Scrolling layers (multi-layer backgrounds)
10. CD streaming (continuous data loading)
11. Save data (256KB backup RAM)
12. Anime graphics techniques (cel-shading style)
13. Visual novel patterns (text, choices, branches)
14. Dating sim mechanics (relationship stats)
15. Polish patterns (FMV integration, transitions)
16. Complete PC-FX mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced 2D techniques, FMV/gameplay integration, visual novel engines, anime production values

#### New Patterns:
- **Multi-layer scrolling** - Parallax backgrounds (anime style)
- **MJPEG mastery** - Full-screen FMV, video compression
- **CD streaming engines** - Loading during FMV playback
- **32-channel audio mixing** - ADPCM samples + CD-DA
- **Visual novel engines** - Text rendering, choices, save points
- **Dating sim mechanics** - Stat systems, multiple endings
- **Anime graphics** - Cel-shading, gradients, high-res sprites
- **Save/load systems** - 256KB backup RAM (progress, multiple saves)
- **341×240 optimization** - Using full wide resolution
- **FMV/gameplay transitions** - Seamless video to gameplay

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - PC Engine backward compatibility adapter
**Focus:** PC Engine adapter, comparing PC-FX vs PC Engine capabilities

#### Phase 3 Enhancement: PC Engine Backward Compatibility
- **PC Engine adapter** - Limited release accessory
- **Plays HuCard games** - Original PC Engine/TurboGrafx-16 games
- **Enhanced features** - Potential for enhancements (not commonly used)
- **Rare accessory** - Not widely available

**Tier 40 Example - PC Engine Compatibility Mode:**
```asm
; Detect PC Engine adapter and enable compatibility

DetectPCEAdapter:
        ; Check for PC Engine adapter presence
        mov     0x80000010,r6   ; Adapter detection
        ld.w    0[r6],r7
        andi    r7,r7,0x0001
        be      .NO_ADAPTER

        ; PC Engine adapter detected
        mov     1,r6
        movhi   hi(PCEAdapter),r0,r7
        movea   lo(PCEAdapter),r7,r7
        st.w    r6,0[r7]

        ; Enable PC Engine compatibility mode
        jal     EnablePCEMode
        jmp     [r31]

.NO_ADAPTER:
        ; No adapter
        mov     0,r6
        movhi   hi(PCEAdapter),r0,r7
        movea   lo(PCEAdapter),r7,r7
        st.w    r6,0[r7]
        jmp     [r31]

EnablePCEMode:
        ; Switch to PC Engine compatibility mode
        ; (Implementation for running HuCard games)
        jmp     [r31]

PCEAdapter: .word 0
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional anime game architecture, complex visual novels, FMV production mastery

#### Advanced Techniques:
- **Branching story engines** - Complex narratives, multiple paths
- **Relationship systems** - Dating sim stat tracking
- **FMV quality optimization** - Best MJPEG encoding for CD
- **Multi-disc games** - Large games spanning 2-3 CDs
- **Voice acting integration** - ADPCM voice samples + lip sync
- **Anime animation** - Frame-by-frame cel animation
- **Save system complexity** - Multiple save slots, autosave
- **CD-DA + ADPCM hybrid** - Music + voice simultaneously
- **V810 optimization** - Efficient RISC code
- **High-res UI design** - 341×240 interface layouts

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Anime fighters, visual novels, RPGs, FMV adventures (PC-FX's focus genres!)

#### Genre Specializations:
- **Anime fighting games** - 2D fighters with FMV sequences
- **Visual novels** - Text-heavy, branching narratives
- **Dating sims** - Relationship management, multiple endings
- **RPGs** - Turn-based with anime cutscenes
- **FMV adventures** - Interactive movie games
- **Mahjong/card games** - Popular in Japanese market
- **Board games** - Anime-themed adaptations
- **Quiz games** - Anime trivia with FMV hosts

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum 2D quality, complex FMV, CD streaming mastery

#### Limit-Pushing Techniques:
- **Maximum sprite counts** - Complex anime scenes
- **Full-screen FMV** - Best possible MJPEG quality
- **Zero-load streaming** - Seamless CD data flow
- **32-channel audio showcase** - Complex sound mixing
- **Multi-disc epics** - Large-scale games
- **Branching complexity** - Dozens of story paths
- **Save data maximization** - Using full 256KB backup RAM
- **341×240 mastery** - Full use of wide resolution

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial anime game quality, professional FMV production

#### Commercial Techniques:
- **Commercial visual novels** - Tokimeki Memorial quality
- **Professional FMV** - Anime cutscenes, full production
- **Complex dating sims** - Multiple heroines, many endings
- **Anime fighters** - Highly detailed sprites, FMV supers
- **RPG epics** - Long games with voice acting
- **Multi-disc showcases** - Games using 2-3 CDs fully
- **Attract modes** - FMV attract sequences
- **Professional voice acting** - Full ADPCM cast

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development, emulation

#### Modern Development:
- **Mednafen emulator** - Excellent PC-FX emulation
- **MAME** - PC-FX support
- **Modern V810 toolchains** - GCC V810, assemblers
- **CD mastering** - Burning PC-FX CD-Rs
- **FMV encoding** - Modern MJPEG tools
- **Community techniques** - PC-FX homebrew preservation
- **Flash solutions** - ODE (Optical Disc Emulator)
- **Cross-platform V810** - Rare architecture expertise

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 anime/FMV techniques
3. **Compatibility Patterns (Phase 3)** - 50 PC Engine adapter
4. **Optimization Patterns (Phase 4-5)** - 100 V810 RISC + FMV
5. **Genre Patterns (Phase 5-6)** - 150 visual novel/dating sim/anime
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: PC-FX (1994, Japan-only)**
- V810 @ 21.5MHz (32-bit NEC RISC)
- 2MB main RAM + 1.25MB VRAM + 256KB backup RAM
- CD-ROM 2× speed (300KB/s)
- 256×240 or 341×240 resolution (wide!)
- 16.7 million colors (24-bit true color)
- Hardware sprites + scrolling layers
- MJPEG hardware decoder (FMV!)
- 32-channel ADPCM audio
- PC Engine backward compatible (adapter required)
- Tower design (vertical console)

**Phase 3+: PC Engine Adapter**
- Plays PC Engine/TurboGrafx-16 HuCards
- Limited release accessory
- Rare but functional

**Phase 7-8: Modern Homebrew**
- CD-R burning (create custom PC-FX games)
- ODE (Optical Disc Emulator)
- Modern development tools (Mednafen, GCC V810)
- Modern FMV encoding tools

## Spiral Learning Example: Visual Novel (PC-FX Strength!)

**Phase 1 (Tier 13):** Simple visual novel, text display, choices, basic branches. (~200 lines)

**Phase 2 (Tier 29):** Complex visual novel, FMV sequences, voice acting, multiple endings. (~600 lines)

**Phase 3 (Tier 39):** PC Engine adapter support for legacy content. (~800 lines)

**Phase 4 (Tier 47):** Dating sim mechanics, relationship stats, many endings, save system. (~1200 lines)

**Phase 5 (Tier 50):** Full visual novel - dozens of scenes, voice acting, FMV cutscenes. (~1800 lines)

**Phase 6 (Tier 54):** Maximum branching, complex relationship system, multi-disc. (~2400 lines)

**Phase 7 (Tier 57):** Tokimeki Memorial quality - professional visual novel. (~3200 lines)

**Phase 8 (Tier 59):** Modern homebrew - CD-R, modern tools, ODE support. (~3200 lines + tooling)

## Key Differences from Other Platforms

1. **V810 32-bit RISC** - Rare architecture (educational value!)
2. **Japan-Only** - Never released outside Japan
3. **NEC's Final Console** - Ended NEC's console presence
4. **Anime/Visual Novel Focus** - Niche market positioning
5. **MJPEG Hardware** - FMV decoder (advanced for 1994)
6. **Tower Design** - Vertical console (unique form factor)
7. **341×240 Resolution** - Wider than standard TV
8. **CD-ROM Only** - No cartridge slot
9. **PC Engine Backward Compatible** - Via adapter
10. **62 Games Total** - Very small library, cult following

## Success Criteria

**By Phase 4, learners can:**
- Write V810 assembly fluently (32-bit RISC)
- Master MJPEG FMV integration
- Create visual novel engines
- Implement dating sim mechanics
- Program 32-channel ADPCM audio
- Use 341×240 high-resolution modes
- Manage CD-ROM streaming

**By Phase 8, learners can:**
- Develop commercial-quality PC-FX games
- Master V810 RISC architecture
- Work with modern homebrew tools (Mednafen, ODE)
- Create professional FMV sequences
- Contribute to PC-FX preservation
- Release custom CD-ROM titles

## Resources Required

**Phase 1-2:**
- Mednafen or MAME emulator
- GCC V810 or assembler
- Text editor
- PC-FX reference documentation

**Phase 7-8:**
- CD burning software
- PC-FX hardware (optional, rare!)
- ODE (Optical Disc Emulator)
- FMV encoding tools
- Community resources

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** V810 32-bit RISC mastery, anime game development, FMV integration, visual novel engines, understanding Japanese niche markets, NEC's console history closure
