# FM Towns Marty Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** FM Towns Marty (1993-1995, Japan-only) → Fujitsu's 32-bit multimedia console
**Approach:** Game-first, pattern library, i386 mastery, multimedia/CD-ROM focus
**Gateway:** Direct to assembly (no BASIC, though C development common via Towns OS SDK)
**Historical Note:** Fujitsu's home console (1993), based on FM Towns computer line, i386SX @ 16MHz, claims "world's first 32-bit home console" (debatable vs Jaguar!), CD-ROM only (no cartridge slot), expensive (¥98,000 = ~$740 USD!), keyboard + mouse included, multimedia focus (games + education + karaoke!), Japan-only, ~45,000 units sold (commercial failure), Towns OS (custom OS, MS-DOS-like), ~184 games, discontinued 1995

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** FM Towns Marty shipped without BASIC. Most commercial development used C via Towns OS SDK, but assembly programming possible and powerful. Curriculum begins with assembly.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** i386 fundamentals, CD-ROM access, VGA-like graphics, FM synthesis audio, Towns OS integration, multimedia capabilities
**Professional Autoload:** From lesson 1, all programs professionally load from CD-ROM

#### Pattern Library Established:
- **i386SX patterns** - Intel i386SX @ 16MHz (32-bit x86 architecture!)
- **CD-ROM access** - 1× speed (150KB/s), later 2× models
- **VGA-like graphics** - 640×480 resolution, 32,768 colors on-screen (from 16.7M palette)
- **FM synthesis** - Yamaha YM3438 (6-channel FM synthesis)
- **PCM audio** - 8-channel PCM samples
- **2MB RAM** - Expandable to 6MB (large for 1993!)
- **Towns OS** - Custom operating system (MS-DOS-like interface)
- **Keyboard + mouse** - Full PC-style peripherals included
- **SCSI CD-ROM** - Professional-grade drive
- **Multimedia focus** - Games, education software, karaoke applications

#### Example Tier 1 Lesson: "Your First i386 Sprite"
```asm
; FM Towns Marty Assembly - Lesson 001
; Display sprite using i386 architecture
; i386SX @ 16 MHz

        .386                    ; i386 mode
        .model flat, stdcall    ; Flat memory model

        .code

        public  _start

_start: ; Initialize
        cli                     ; Disable interrupts
        mov     esp, 100000h    ; Set stack pointer

        ; Initialize video mode (640×480, 256 colors)
        mov     ah, 00h
        mov     al, 12h         ; VGA mode
        int     10h             ; BIOS video interrupt

        ; Set up Towns video controller
        mov     dx, 440h        ; Towns video port
        mov     al, 01h         ; Enable graphics
        out     dx, al

        ; Load sprite data to video RAM
        mov     edi, 0C0000000h ; Video RAM base
        mov     esi, offset SPRITE_DATA
        mov     ecx, 1024       ; 32×32 sprite
        rep movsb               ; Copy to VRAM

        ; Set sprite position
        mov     dword ptr [SPRITE_X], 320  ; Center X
        mov     dword ptr [SPRITE_Y], 240  ; Center Y

LOOP:   ; Main game loop
        call    WaitVSync

        ; Read keyboard
        in      al, 60h         ; Keyboard port
        cmp     al, 4Dh         ; Right arrow?
        jne     CHECK_LEFT

        ; Move sprite right
        inc     dword ptr [SPRITE_X]
        cmp     dword ptr [SPRITE_X], 640
        jl      UPDATE_POS
        mov     dword ptr [SPRITE_X], 0

UPDATE_POS:
        ; Update sprite on screen
        mov     eax, [SPRITE_Y]
        imul    eax, 640        ; Y * width
        add     eax, [SPRITE_X] ; + X
        add     eax, 0C0000000h ; + VRAM base
        mov     edi, eax

        ; Draw sprite
        mov     esi, offset SPRITE_DATA
        mov     ecx, 32         ; Height
.ROW:   push    ecx
        mov     ecx, 32         ; Width
        rep movsb
        add     edi, 640-32     ; Next row
        pop     ecx
        loop    .ROW

CHECK_LEFT:
        ; ... (similar for other directions)

        jmp     LOOP

WaitVSync:
        ; Wait for vertical sync
        mov     dx, 3DAh        ; VGA status port
.WAIT:  in      al, dx
        test    al, 08h         ; VSync bit
        jz      .WAIT
        ret

SPRITE_X:   dd  320
SPRITE_Y:   dd  240

SPRITE_DATA:
        ; 32×32 sprite data (8-bit indexed color)
        .incbin "sprite32x32.bin"

        end     _start
```

**Key teaching moment:** FM Towns Marty uses i386SX - real x86 architecture! 32-bit programming (knowledge transfers to PC!). Claims "first 32-bit home console" (1993, same year as Jaguar - debatable!). CD-ROM only. VGA-like 640×480 graphics. Multimedia focus (games + education + karaoke!). Keyboard + mouse included. Towns OS (custom OS, MS-DOS-like). Very expensive ($740!). Japan-only. Commercial failure (~45K units) but technically impressive.

**Tier progression:**
1. i386 basics (32-bit x86 registers, addressing modes)
2. VGA graphics (640×480, palette programming)
3. CD-ROM access (SCSI drive, file I/O)
4. Sprite rendering (software sprites, no hardware)
5. Keyboard input (PC-style scan codes)
6. Mouse input (PS/2 protocol)
7. FM synthesis (Yamaha YM3438, 6 channels)
8. PCM audio (8-channel sample playback)
9. Towns OS integration (system calls, API)
10. CD-DA audio (Redbook playback)
11. Multimedia formats (video, audio codecs)
12. 2MB RAM management (expandable to 6MB)
13. SCSI CD-ROM optimization
14. Education software patterns
15. Karaoke application patterns (unique!)
16. Complete FM Towns Marty mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced i386 techniques, multimedia applications, CD-ROM streaming, professional graphics

#### New Patterns:
- **Protected mode** - i386 protected mode programming
- **CD-ROM streaming** - Continuous data loading
- **VGA effects** - Mode X (320×240), hardware scrolling
- **FM synthesis mastery** - Complex YM3438 programming
- **PCM mixing** - 8-channel audio mixing
- **Multimedia codecs** - Video/audio compression
- **Towns OS SDK** - System calls, libraries
- **Karaoke systems** - Lyrics display, audio synchronization (Marty known for this!)
- **Education software** - Interactive learning applications
- **CD-DA + PCM hybrid** - Music + sound effects
- **Mouse-driven UI** - Point-and-click interfaces
- **Keyboard shortcuts** - PC-style key combinations

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Marty II (1994) and memory expansions
**Focus:** Marty II improvements, RAM expansion, 2× CD-ROM drive

#### Phase 3 Enhancement: Marty II + Expansions
- **Marty II** (1994) - 2× CD-ROM drive (300KB/s, 2× faster!)
- **RAM expansion** - Up to 6MB total (from 2MB base)
- **Improved cooling** - Better thermal design
- **Lower price** - ¥66,000 (still expensive!)
- **Backward compatible** - All Marty games work

**Tier 40 Example - Memory Expansion Detection:**
```asm
; Detect RAM expansion and adjust features

DetectRAM:
        ; Probe memory to detect installed RAM
        mov     edi, 200000h    ; Start of expansion RAM
        mov     eax, 12345678h  ; Test pattern
        mov     [edi], eax
        cmp     [edi], eax
        jne     .NO_EXPANSION

        ; Expansion RAM detected
        ; Try 4MB
        mov     edi, 400000h
        mov     [edi], eax
        cmp     [edi], eax
        je      .FOUND_4MB

        ; 2MB expansion only
        mov     dword ptr [TOTAL_RAM], 4
        ret

.FOUND_4MB:
        ; Try 6MB
        mov     edi, 600000h
        mov     [edi], eax
        cmp     [edi], eax
        jne     .STOP_4MB

        ; 6MB total!
        mov     dword ptr [TOTAL_RAM], 6
        ret

.STOP_4MB:
        mov     dword ptr [TOTAL_RAM], 4
        ret

.NO_EXPANSION:
        ; Base 2MB only
        mov     dword ptr [TOTAL_RAM], 2
        ret

TOTAL_RAM: dd 2
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional i386 programming, multimedia mastery, CD-ROM optimization, Towns OS proficiency

#### Advanced Techniques:
- **i386 protected mode mastery** - Segmentation, paging
- **DMA transfers** - Hardware-accelerated data movement
- **CD-ROM buffering** - Efficient streaming from SCSI drive
- **VGA mode mastery** - All modes, smooth scrolling
- **FM synthesis complexity** - 6-channel orchestration
- **8-channel PCM mixing** - Professional audio engine
- **Multimedia codecs** - Efficient video/audio compression
- **Towns OS API mastery** - System integration
- **Large RAM utilization** - Using 6MB efficiently
- **Multi-disc games** - Games spanning multiple CDs
- **Education software** - Professional teaching applications
- **Karaoke production** - Full karaoke system (Marty specialty!)

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Games, education software, multimedia applications, karaoke (Marty's unique strengths!)

#### Genre Specializations:
- **RPGs** - CD-ROM capacity enables large games
- **Adventure games** - Point-and-click with mouse
- **Education software** - Interactive learning (Marty strength!)
- **Karaoke applications** - Lyrics + music + scoring (unique to Marty!)
- **Puzzle games** - Mouse-driven puzzle games
- **Board games** - Digital versions with mouse control
- **Multimedia encyclopedias** - Educational references
- **Music creation** - FM synthesis tools

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum i386 performance, multimedia mastery, CD-ROM optimization

#### Limit-Pushing Techniques:
- **i386 optimization** - Cycle-perfect code
- **VGA maximum performance** - Fast graphics routines
- **CD-ROM streaming mastery** - Zero-load continuous streaming
- **6MB RAM utilization** - Complex games in expanded RAM
- **FM + PCM showcase** - 6 FM + 8 PCM = 14 channels total!
- **Multimedia compression** - Maximum quality in CD space
- **Karaoke perfection** - Professional karaoke system
- **Education software depth** - Comprehensive learning suites

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial multimedia applications, professional karaoke, educational software

#### Commercial Techniques:
- **Commercial games** - RPGs, adventures (professional quality)
- **Karaoke showcases** - Full karaoke production (Marty known for this!)
- **Educational software** - Professional teaching applications
- **Multimedia encyclopedias** - Interactive references
- **Professional graphics** - VGA art, smooth animation
- **Complex audio** - 14-channel compositions
- **Multi-disc production** - Large-scale applications
- **Towns OS integration** - Seamless system integration

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, emulation

#### Modern Development:
- **MAME** - FM Towns Marty emulation
- **Tsugaru emulator** - Dedicated Towns emulator (excellent!)
- **Modern i386 toolchains** - GCC, NASM, FASM
- **CD-ROM mastering** - Burning Marty CD-Rs
- **Modern multimedia tools** - Video/audio encoding
- **Community techniques** - Towns preservation scene
- **Cross-platform i386** - Knowledge transfers to PC/DOS!
- **ODE solutions** - Flash storage for CD drive

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 multimedia techniques
3. **Expansion Patterns (Phase 3)** - 50 Marty II/RAM expansion
4. **Optimization Patterns (Phase 4-5)** - 100 i386 + CD-ROM
5. **Genre Patterns (Phase 5-6)** - 150 game/education/karaoke patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: FM Towns Marty (1993)**
- i386SX @ 16MHz (32-bit x86!)
- 2MB RAM (expandable to 6MB)
- CD-ROM 1× speed (150KB/s, SCSI)
- 640×480 resolution, 32,768 colors on-screen (from 16.7M palette)
- Yamaha YM3438 FM synthesis (6 channels)
- 8-channel PCM audio
- Keyboard + mouse (PS/2)
- Towns OS (custom OS, MS-DOS-like)
- SCSI interface
- ¥98,000 (~$740 USD)

**Phase 3+: Marty II (1994) + Expansions**
- 2× CD-ROM drive (300KB/s)
- Same CPU/RAM/graphics
- Improved cooling
- Lower price (¥66,000)
- RAM expansion to 6MB total
- Backward compatible

**Phase 7-8: Modern Homebrew**
- CD-R burning (create custom Marty discs)
- ODE (Optical Disc Emulator)
- Modern development tools (MAME, Tsugaru, GCC i386)
- Modern multimedia tools

## Spiral Learning Example: Educational Software (Marty Strength!)

**Phase 1 (Tier 15):** Simple education app, text + images, keyboard/mouse input. (~300 lines)

**Phase 2 (Tier 31):** Interactive lessons, CD-ROM assets, audio narration. (~800 lines)

**Phase 3 (Tier 39):** Advanced app using 6MB RAM for complex content. (~1200 lines)

**Phase 4 (Tier 47):** Comprehensive learning suite, multiple subjects, progress tracking. (~1800 lines)

**Phase 5 (Tier 50):** Full educational platform - many lessons, multimedia. (~2500 lines)

**Phase 6 (Tier 54):** Maximum multimedia, video lessons, interactive exercises. (~3200 lines)

**Phase 7 (Tier 57):** Professional educational software - commercial quality. (~4000 lines)

**Phase 8 (Tier 59):** Modern homebrew - updated content, modern tools. (~4000 lines + tooling)

## Key Differences from Other Platforms

1. **i386SX 32-bit** - Real x86 architecture (knowledge transfers to PC!)
2. **"First 32-bit Console" Claim** - Debatable (vs Jaguar, same year)
3. **CD-ROM Only** - No cartridge slot
4. **Keyboard + Mouse** - PC peripherals included
5. **Towns OS** - Custom operating system (MS-DOS-like)
6. **$740 Launch** - Very expensive!
7. **Multimedia Focus** - Games + education + karaoke!
8. **Japan-Only** - Never exported
9. **Karaoke Strength** - Unique application focus
10. **Commercial Failure** - ~45K units, discontinued 1995

## Success Criteria

**By Phase 4, learners can:**
- Write i386 assembly fluently (32-bit x86)
- Program VGA graphics (640×480, palettes)
- Master CD-ROM access (SCSI, streaming)
- Create multimedia applications
- Program FM synthesis (YM3438)
- Mix 8-channel PCM audio
- Integrate with Towns OS
- Design education software

**By Phase 8, learners can:**
- Develop commercial-quality FM Towns Marty applications
- Master i386 architecture (transfers to PC programming!)
- Work with modern homebrew tools (MAME, Tsugaru)
- Create professional multimedia software
- Contribute to Towns preservation
- Release custom CD-ROM titles

## Resources Required

**Phase 1-2:**
- MAME or Tsugaru emulator
- GCC i386 or NASM/FASM assembler
- Text editor
- FM Towns Marty reference documentation
- Towns OS documentation

**Phase 7-8:**
- CD burning software
- FM Towns Marty hardware (optional, rare!)
- ODE (Optical Disc Emulator)
- Modern multimedia tools
- Community resources (preservation scene)

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** i386 x86 mastery (transfers to PC!), "first 32-bit console" claim, multimedia applications, karaoke development, education software, Towns OS, understanding Japan multimedia market, rare architecture study
