# Sega Pico Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Sega Pico (1993-2005) → Educational console for children ages 3-7
**Approach:** Game-first, pattern library, 68000 mastery, educational software focus
**Gateway:** Direct to assembly (though C development common via Genesis SDK)
**Historical Note:** Sega educational console (1993), 68000 @ 7.6MHz (SAME as Genesis!), "Storyware" cartridges (book + cartridge hybrid!), drawing tablet + pen input (innovative!), page-turning mechanism (physical pages), educational focus (ages 3-7), 320×224 resolution, 64 colors on-screen, 3.4 million units sold (success!), worldwide release (Japan, USA, Europe), long lifespan (1993-2005, 12 years!), Advanced Pico (1998, upgraded), Beena successor (2005), ~350 titles, unique input methods

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Sega Pico shipped without BASIC. Most commercial development used C (Genesis SDK adapted), but assembly programming possible and powerful. Curriculum begins with assembly.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** 68000 fundamentals, drawing tablet input, page-turning mechanics, educational software design, child-friendly interfaces
**Professional Autoload:** From lesson 1, all programs professionally load from Storyware cartridge

#### Pattern Library Established:
- **68000 patterns** - Motorola 68000 @ 7.6MHz (SAME as Genesis!)
- **Drawing tablet** - Pen input, touch detection (innovative!)
- **Page-turning** - Physical page mechanism on cartridge
- **Storyware cartridges** - Book pages + ROM chip hybrid
- **320×224 graphics** - Genesis-like resolution
- **64 colors on-screen** - From 512-color palette
- **Educational focus** - Ages 3-7 content design
- **Child-friendly UI** - Simple, intuitive interfaces
- **VDP (Video Display Processor)** - Genesis VDP
- **PSG audio** - TI SN76489 (3 channels + noise)
- **Speech synthesis** - Voice samples for education

#### Example Tier 1 Lesson: "Your First Pico Drawing"
```asm
; Sega Pico Assembly - Lesson 001
; Drawing program using 68000 + tablet
; 68000 @ 7.6 MHz (SAME as Genesis!)

; Motorola 68000 architecture:
; - 32-bit registers (D0-D7 data, A0-A7 address)
; - 16-bit data bus
; - 24-bit address bus (16MB addressing)
; - No hardware multiply/divide (unlike 68020+)
; - Big-endian

        .org    $00000000

; Sega Pico memory map (similar to Genesis)
ROM_START       = $00000000     ; ROM base
RAM_START       = $00FF0000     ; 64KB RAM
VDP_DATA        = $00C00000     ; VDP data port
VDP_CTRL        = $00C00004     ; VDP control port
TABLET_X        = $00800000     ; Tablet X coordinate
TABLET_Y        = $00800002     ; Tablet Y coordinate
TABLET_PEN      = $00800004     ; Pen down status
PAGE_NUM        = $00800006     ; Current page number

; Entry point
START:  ; Initialize
        move.w  #$2700,sr       ; Disable interrupts
        move.l  #$00FFFE00,sp   ; Set stack pointer

        ; Initialize VDP (Genesis-compatible)
        jsr     InitVDP

        ; Clear VRAM
        jsr     ClearVRAM

        ; Load drawing character set
        lea     CHAR_DATA,a0
        move.l  #$40000000,d0   ; VRAM address $0000
        jsr     LoadToVRAM

        ; Set background color
        move.l  #$C0000000,VDP_CTRL     ; CRAM address
        move.w  #$0000,VDP_DATA         ; Black background

        ; Display title
        lea     TITLE_TEXT,a0
        move.w  #2,d0           ; Row 2
        move.w  #8,d1           ; Column 8
        jsr     DrawText

MAIN_LOOP:
        ; Wait for VBlank
        jsr     WaitVBlank

        ; Read tablet input
        move.w  TABLET_PEN,d0   ; Check if pen is down
        andi.w  #$0001,d0
        beq     NO_DRAW         ; Skip if pen up

        ; Pen is down - read coordinates
        move.w  TABLET_X,d2     ; X coordinate
        move.w  TABLET_Y,d3     ; Y coordinate

        ; Convert to screen position (320×224)
        lsr.w   #2,d2           ; Scale X (tablet is higher res)
        lsr.w   #2,d3           ; Scale Y

        ; Draw pixel/dot at position
        move.w  d2,d0           ; X
        move.w  d3,d1           ; Y
        move.w  #$000E,d4       ; Color (yellow)
        jsr     DrawPixel

NO_DRAW:
        ; Check if page was turned
        move.w  PAGE_NUM,d5     ; Current page
        cmp.w   OLD_PAGE,d5
        beq     SAME_PAGE

        ; Page changed - update display
        jsr     ClearVRAM
        lea     PAGE_TEXT,a0
        move.w  #10,d0          ; Row
        move.w  #5,d1           ; Column
        jsr     DrawText

SAME_PAGE:
        move.w  d5,OLD_PAGE

        ; Play sound on pen touch
        move.w  TABLET_PEN,d0
        andi.w  #$0001,d0
        beq     NO_SOUND
        jsr     PlayBeep

NO_SOUND:
        bra     MAIN_LOOP

; Initialize VDP (Genesis-compatible)
InitVDP:
        move.l  #$8004,VDP_CTRL         ; Mode register 1
        move.l  #$8174,VDP_CTRL         ; Mode register 2
        move.l  #$8230,VDP_CTRL         ; Plane A address
        move.l  #$8407,VDP_CTRL         ; Plane B address
        move.l  #$857C,VDP_CTRL         ; Sprite table
        move.l  #$8700,VDP_CTRL         ; Background color
        move.l  #$8B00,VDP_CTRL         ; H-int register
        move.l  #$8C81,VDP_CTRL         ; Mode register 3
        move.l  #$8D3F,VDP_CTRL         ; HScroll address
        move.l  #$8F02,VDP_CTRL         ; Auto-increment
        rts

; Clear VRAM
ClearVRAM:
        move.l  #$40000000,VDP_CTRL     ; VRAM write
        move.w  #$7FFF,d0               ; 64KB
.loop:  move.w  #$0000,VDP_DATA
        dbra    d0,.loop
        rts

; Load data to VRAM
; a0 = source, d0 = VDP command
LoadToVRAM:
        move.l  d0,VDP_CTRL
        move.w  #511,d1                 ; 512 transfers
.loop:  move.l  (a0)+,VDP_DATA
        dbra    d1,.loop
        rts

; Draw text
; a0 = text, d0 = row, d1 = column
DrawText:
        ; Calculate VRAM address
        mulu    #64,d0          ; Row × 64
        add.w   d1,d0           ; + column
        lsl.l   #1,d0           ; × 2 (word per character)
        swap    d0
        ori.l   #$40000003,d0   ; VRAM write command
        move.l  d0,VDP_CTRL

.loop:  move.b  (a0)+,d2
        beq     .done
        ext.w   d2
        move.w  d2,VDP_DATA
        bra     .loop
.done:  rts

; Draw pixel (simplified)
DrawPixel:
        ; d0 = X, d1 = Y, d4 = color
        ; (Real implementation would use sprites or VRAM)
        rts

; Wait for VBlank
WaitVBlank:
        move.w  VDP_CTRL,d0
.wait:  move.w  VDP_CTRL,d0
        andi.w  #$0008,d0       ; VBlank flag
        beq     .wait
        rts

; Play beep
PlayBeep:
        ; Simple PSG tone
        move.b  #$90,PSG_PORT   ; Channel 0 frequency
        move.b  #$0F,PSG_PORT   ; Volume
        rts

; Data
TITLE_TEXT:     dc.b    "DRAW WITH PEN!",0
PAGE_TEXT:      dc.b    "NEW PAGE!",0
OLD_PAGE:       dc.w    0
CHAR_DATA:      incbin  "font.bin"

PSG_PORT        = $00C00011
```

**Key teaching moment:** Sega Pico uses 68000 @ 7.6MHz - SAME CPU as Genesis! Knowledge transfers directly to Genesis programming! "Storyware" cartridges are books with physical pages + ROM chip (innovative!). Drawing tablet + pen input (touchscreen-like in 1993!). Page-turning mechanism (physical pages on cart). Educational focus (ages 3-7). 3.4 million units sold (success!). Long lifespan (1993-2005, 12 years!). Worldwide release. ~350 educational titles. Advanced Pico (1998, upgraded). Unique input methods.

**Tier progression:**
1. 68000 basics (32-bit registers, addressing modes)
2. VDP programming (Genesis-compatible video)
3. Drawing tablet input (pen X/Y coordinates, pen down)
4. Page-turning detection (physical pages on cartridge!)
5. Child-friendly graphics (simple, colorful, large)
6. Text rendering (educational content)
7. PSG audio (3-channel + noise)
8. Speech samples (voice for education)
9. Educational UI patterns (ages 3-7 design)
10. Touch-based interaction (pen input)
11. Animation (simple, child-friendly)
12. Color choice (64 on-screen, bright palettes)
13. Drawing programs (pen-based art)
14. Educational mini-games (learning focus)
15. Storyware integration (book + game hybrid)
16. Complete Pico educational apps

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced educational software, complex tablet interactions, multi-page stories, speech synthesis

#### New Patterns:
- **Advanced tablet handling** - Handwriting recognition (simple)
- **Multi-page stories** - Narratives across physical pages
- **Educational game design** - Learning objectives (math, reading, etc.)
- **Speech synthesis** - Voice samples for instruction
- **Child UI design** - Age 3-7 interface guidelines
- **Drawing applications** - Paint programs, coloring books
- **Interactive stories** - Page-based adventures
- **Simple animations** - Child-friendly movement
- **Bright colors** - High-contrast, appealing palettes
- **PSG music** - Educational songs
- **Reward systems** - Positive reinforcement
- **Progress tracking** - Learning metrics

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Advanced Pico (1998) improvements
**Focus:** Advanced Pico features, enhanced capabilities

#### Phase 3 Enhancement: Advanced Pico (1998)
- **Advanced Pico** (1998, Japan) - Upgraded Pico
- **Same 68000 CPU** - Compatible with original
- **Enhanced software** - More educational titles
- **Backward compatible** - All Pico Storyware works
- **Better build quality** - Improved construction
- **Longer lifespan** - Supported until 2005

**Tier 40 Example - Detect Advanced Pico:**
```asm
; Detect original Pico vs Advanced Pico

DetectPicoVariant:
        ; Check ROM header for variant ID
        move.l  #$00000100,a0   ; Header location
        move.b  (a0),d0
        andi.b  #$F0,d0
        cmpi.b  #$A0,d0         ; Advanced Pico marker
        beq     is_advanced

is_original:
        ; Original Pico (1993)
        move.w  #0,variant
        rts

is_advanced:
        ; Advanced Pico (1998)
        move.w  #1,variant
        rts

variant:        dc.w    0       ; 0=original, 1=advanced
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional educational software, complex interactive stories, advanced tablet usage

#### Advanced Techniques:
- **68000 mastery** - Efficient code for Genesis-class CPU
- **Educational pedagogy** - Learning theory integration
- **Complex tablet apps** - Advanced drawing, handwriting
- **Multi-page narratives** - Long-form stories
- **Speech integration** - Voice-guided instruction
- **VDP mastery** - Genesis-level graphics
- **PSG composition** - Educational music
- **Progress systems** - Learning analytics
- **Child psychology** - Age-appropriate design
- **Interactive storytelling** - Branching narratives
- **Reward mechanics** - Motivation systems

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Educational genres (reading, math, art, music)

#### Genre Specializations:
- **Reading education** - Phonics, sight words, stories
- **Math education** - Counting, addition, subtraction
- **Art applications** - Drawing, coloring, creativity
- **Music education** - Rhythm, melodies, instruments
- **Science education** - Nature, animals, experiments
- **Language learning** - Vocabulary, basic language
- **Logic puzzles** - Pattern recognition, problem-solving
- **Interactive stories** - Read-along adventures

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum educational value, complex tablet interactions

#### Limit-Pushing Techniques:
- **Complex handwriting recognition** - Letter/number recognition
- **Multi-page epics** - Long-form educational content
- **Advanced drawing tools** - Paint program features
- **Speech showcase** - Extensive voice instruction
- **VDP maximum** - Best possible graphics
- **PSG music complexity** - Educational songs
- **Progress analytics** - Detailed learning metrics
- **Branching education** - Adaptive difficulty

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial educational software quality

#### Commercial Techniques:
- **Commercial quality** - Professional educational apps
- **Pedagogical depth** - Research-based learning
- **Interactive excellence** - Engaging tablet usage
- **Voice acting** - Professional speech samples
- **Graphics polish** - Child-appealing art
- **Music production** - Educational soundtracks
- **Long-form content** - Comprehensive curricula
- **Parent features** - Progress reports, settings

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development, emulation

#### Modern Development:
- **MAME emulation** - Sega Pico emulation
- **Genesis toolchains** - GCC 68000, SGDK (Sega Genesis Dev Kit)
- **Flash cartridges** - Homebrew Storyware development
- **Modern educational design** - Contemporary pedagogy
- **Community techniques** - Pico preservation scene
- **Cross-platform 68000** - Genesis/Pico shared knowledge
- **Modern tools** - Emulator debugging

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Educational Patterns (Phase 2)** - 75 learning design techniques
3. **Advanced Pico Patterns (Phase 3)** - 50 upgraded hardware
4. **Pedagogy Patterns (Phase 4-5)** - 100 educational theory
5. **Genre Patterns (Phase 5-6)** - 150 subject specializations
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Sega Pico (1993)**
- Motorola 68000 @ 7.6MHz (SAME as Genesis!)
- 64KB RAM
- VDP (Genesis video chip)
- 320×224 resolution
- 64 colors on-screen (from 512-color palette)
- Drawing tablet + pen (touch input!)
- Physical page-turning mechanism
- "Storyware" cartridges (book + ROM)
- PSG audio (TI SN76489, 3 channels + noise)
- Speech synthesis samples
- Educational focus (ages 3-7)

**Phase 3+: Advanced Pico (1998)**
- Same 68000 CPU
- Enhanced build quality
- Backward compatible
- Supported until 2005

**Phase 7-8: Modern Homebrew**
- Flash Storyware cartridges (homebrew)
- Modern development tools (MAME, SGDK, GCC 68000)
- Educational software development

## Spiral Learning Example: Reading Education App (Pico Strength!)

**Phase 1 (Tier 16):** Simple word game, pen input, page turning. (~300 lines)

**Phase 2 (Tier 32):** Phonics lessons, voice samples, multi-page story. (~800 lines)

**Phase 3 (Tier 40):** Advanced Pico support, enhanced content. (~1000 lines)

**Phase 4 (Tier 48):** Comprehensive reading curriculum, progress tracking. (~1500 lines)

**Phase 5 (Tier 50):** Full reading platform - many lessons, stories. (~2200 lines)

**Phase 6 (Tier 54):** Handwriting recognition, adaptive difficulty. (~2800 lines)

**Phase 7 (Tier 57):** Professional educational software - commercial quality. (~3500 lines)

**Phase 8 (Tier 59):** Modern homebrew - updated pedagogy, modern tools. (~3500 lines + tooling)

## Key Differences from Other Platforms

1. **Educational Focus** - Ages 3-7 (unique positioning!)
2. **Drawing Tablet + Pen** - Touch input (innovative 1993!)
3. **Storyware Cartridges** - Book + ROM hybrid (unique!)
4. **Page-Turning Mechanism** - Physical pages on cart
5. **68000 @ 7.6MHz** - SAME as Genesis (knowledge transfer!)
6. **Long Lifespan** - 1993-2005 (12 years!)
7. **3.4M Units Sold** - Success story!
8. **~350 Titles** - Large educational library
9. **Worldwide Release** - Japan, USA, Europe
10. **Advanced Pico** - Upgraded 1998 version

## Success Criteria

**By Phase 4, learners can:**
- Write 68000 assembly fluently (Genesis-compatible!)
- Design educational software (ages 3-7)
- Program drawing tablet input
- Implement page-turning mechanics
- Create child-friendly interfaces
- Use VDP graphics (Genesis skills!)
- Program PSG audio
- Integrate speech samples

**By Phase 8, learners can:**
- Develop commercial-quality Pico educational software
- Master 68000 architecture (transfers to Genesis!)
- Work with modern homebrew tools (MAME, SGDK)
- Apply educational theory to game design
- Contribute to Pico preservation
- Release custom Storyware cartridges

## Resources Required

**Phase 1-2:**
- MAME emulator (Sega Pico support)
- SGDK (Sega Genesis Dev Kit) - works for Pico!
- GCC 68000 assembler
- Text editor
- Sega Pico reference documentation

**Phase 7-8:**
- Flash Storyware cartridges (homebrew)
- Sega Pico hardware (optional)
- Modern development tools
- Educational software design resources

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** 68000 mastery (transfers to Genesis, Amiga, Atari ST!), educational software design, tablet/pen input programming, child UI design, pedagogical theory, Storyware development, long-lived platform study (1993-2005), understanding educational gaming market, unique input methods
