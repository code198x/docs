# Philips CD-i Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Philips CD-i (1991-1998) → Multimedia interactive CD console
**Approach:** Game-first, pattern library, 68070 mastery, CD-ROM multimedia focus
**Gateway:** CD-i BASIC available (some models/software) → Direct to assembly for performance
**Historical Note:** Philips multimedia console (1991), 68070 @ 15.5MHz (16-bit Motorola variant with integrated peripherals), CD-ROM only (no cartridges!), multimedia focus (games + education + movies + karaoke), expensive ($700 launch!), keyboard + mouse support, full-motion video (FMV) capable, Digital Video cartridge (MPEG-1 add-on), ~570 titles (many non-games!), infamous Nintendo games (Zelda CDi, Mario!), commercial failure as game console, better success as multimedia player, discontinued 1998, historically significant for CD-ROM era

## 8-Phase Structure

### Phase 0: CD-i BASIC Gateway (Optional)
**Some CD-i models/software included BASIC:**
- **CD-i BASIC** - Programming environment on some CD-i titles
- **Multimedia BASIC** - Create interactive presentations
- **Educational use** - Learning programming on CD-i
- **Limited availability** - Not all CD-i units had BASIC

**Note:** CD-i BASIC was rare and limited. Most development used C/C++ via professional SDK. Assembly was used for performance-critical code.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** 68070 fundamentals, CD-ROM access, FMV playback, multimedia applications, keyboard/mouse support
**Professional Autoload:** From lesson 1, all programs professionally load from CD-ROM

#### Pattern Library Established:
- **68070 patterns** - Philips/Signetics 68070 @ 15.5MHz (68000 variant with integrated peripherals!)
- **CD-ROM access** - CD-i format, Green Book standard
- **FMV playback** - Full-motion video, MPEG-1 with cartridge
- **384×280 resolution** - Interlaced display (PAL), 384×240 (NTSC)
- **16.7M colors** - 24-bit true color support!
- **1-2MB RAM** - Varies by model (expandable)
- **Multimedia focus** - Games + education + movies + karaoke
- **Keyboard + mouse** - PC-style peripherals
- **RTOS** - CD-i OS (real-time operating system)
- **Audio CD playback** - CD-DA audio support

#### Example Tier 1 Lesson: "Your First CD-i Multimedia App"
```asm
; Philips CD-i Assembly - Lesson 001
; Multimedia application on CD-i
; 68070 @ 15.5 MHz

; Philips 68070 architecture:
; - Based on 68000, but 16-bit with integrated peripherals!
; - 32-bit internal registers (D0-D7, A0-A7)
; - 16-bit external data bus
; - Integrated timers, DMA, I²C, UART
; - Big-endian
; - CD-i specific hardware integration

        .org    $00000000

; CD-i memory map
ROM_BASE        = $00000000     ; CD-i BIOS ROM
RAM_BASE        = $00200000     ; RAM (1-2MB depending on model)
VIDEO_BASE      = $00300000     ; Video processor
AUDIO_BASE      = $00301000     ; Audio processor (CD-DA + ADPCM)
CDIC_BASE       = $00303000     ; CD controller
SLAVE_BASE      = $00303400     ; Slave processor
NVRAM_BASE      = $00400000     ; Non-volatile RAM

; CD-i OS services (RTOS)
OS_OPENFILE     = $00000100     ; Open CD file
OS_READFILE     = $00000104     ; Read CD file
OS_DRAWIMAGE    = $00000108     ; Draw image
OS_PLAYVIDEO    = $0000010C     ; Play FMV
OS_PLAYAUDIO    = $00000110     ; Play CD-DA/ADPCM

START:  ; Initialize
        move.w  #$2700,sr       ; Disable interrupts
        move.l  #RAM_BASE+$100000,sp ; Set stack (top of 1MB RAM)

        ; Initialize CD-i OS
        jsr     InitCDiOS

        ; Set video mode (384×280 interlaced PAL)
        move.w  #$0001,VIDEO_BASE       ; Enable video
        move.w  #384,VIDEO_BASE+2       ; Width
        move.w  #280,VIDEO_BASE+4       ; Height
        move.w  #$8000,VIDEO_BASE+6     ; Interlaced mode

        ; Clear screen to black
        lea     SCREEN_BUFFER,a0
        move.l  #384*280,d0
        moveq   #0,d1
.clear: move.b  d1,(a0)+
        subq.l  #1,d0
        bne     .clear

        ; Load image from CD-ROM
        lea     IMAGE_PATH,a0           ; "/CD-i/IMAGE.RGB"
        move.l  #OS_OPENFILE,a1
        jsr     CallCDiOS               ; Open file
        move.l  d0,d7                   ; Save file handle

        ; Read image data
        move.l  d7,d0                   ; File handle
        lea     IMAGE_BUFFER,a0         ; Destination
        move.l  #100000,d1              ; Max size (100KB)
        move.l  #OS_READFILE,a1
        jsr     CallCDiOS

        ; Display image
        lea     IMAGE_BUFFER,a0
        move.w  #0,d0                   ; X = 0
        move.w  #0,d1                   ; Y = 0
        move.w  #384,d2                 ; Width
        move.w  #280,d3                 ; Height
        move.l  #OS_DRAWIMAGE,a1
        jsr     CallCDiOS

        ; Display title text
        lea     TITLE_TEXT,a0
        move.w  #100,d0                 ; X
        move.w  #50,d1                  ; Y
        jsr     DrawText

MAIN_LOOP:
        ; Check mouse input (CD-i supports mouse!)
        jsr     ReadMouse
        move.w  d0,MOUSE_X
        move.w  d1,MOUSE_Y
        move.b  d2,MOUSE_BUTTONS

        ; Check if left button clicked
        btst    #0,MOUSE_BUTTONS
        beq     .no_click

        ; Play CD-DA audio track
        move.w  #1,d0                   ; Track 1
        move.l  #OS_PLAYAUDIO,a1
        jsr     CallCDiOS

.no_click:
        ; Check keyboard (CD-i supports keyboard!)
        jsr     ReadKeyboard
        tst.b   d0
        beq     .no_key

        ; Key pressed - could play FMV video
        cmpi.b  #$20,d0                 ; Space key?
        bne     .no_key

        ; Play full-motion video
        lea     VIDEO_PATH,a0           ; "/CD-i/VIDEO.MPG"
        move.l  #OS_PLAYVIDEO,a1
        jsr     CallCDiOS

.no_key:
        ; Delay
        move.w  #$FFFF,d0
.delay: subq.w  #1,d0
        bne     .delay

        bra     MAIN_LOOP

; Initialize CD-i OS
InitCDiOS:
        ; CD-i RTOS initialization
        ; (Simplified - real implementation complex)
        rts

; Call CD-i OS service
CallCDiOS:
        ; a1 = service address
        jsr     (a1)
        rts

; Read mouse position and buttons
ReadMouse:
        ; CD-i mouse reading
        move.w  SLAVE_BASE+$10,d0       ; X position
        move.w  SLAVE_BASE+$12,d1       ; Y position
        move.b  SLAVE_BASE+$14,d2       ; Button state
        rts

; Read keyboard
ReadKeyboard:
        ; CD-i keyboard reading
        move.b  SLAVE_BASE+$20,d0       ; Key code
        rts

; Draw text
DrawText:
        ; a0 = text, d0 = X, d1 = Y
        ; (Simplified text rendering)
        rts

; Data
TITLE_TEXT:     dc.b    "Philips CD-i Multimedia!",0
IMAGE_PATH:     dc.b    "/CD-i/IMAGE.RGB",0
VIDEO_PATH:     dc.b    "/CD-i/VIDEO.MPG",0
MOUSE_X:        dc.w    0
MOUSE_Y:        dc.w    0
MOUSE_BUTTONS:  dc.b    0

; Buffers
        .align  4
IMAGE_BUFFER:   ds.b    100000          ; 100KB image buffer
SCREEN_BUFFER:  ds.b    384*280         ; Screen buffer
```

**Key teaching moment:** Philips CD-i uses 68070 @ 15.5MHz - 68000 variant with integrated peripherals! CD-ROM only (no cartridges). Multimedia focus (games + education + movies + karaoke!). $700 launch price (very expensive!). 384×280 resolution (PAL), 16.7M colors (24-bit!). Keyboard + mouse support. FMV capable (MPEG-1 with Digital Video cartridge). Infamous Nintendo games (Zelda CDi!). ~570 titles (many non-games). Commercial failure as game console, better as multimedia player. CD-i OS (RTOS). Green Book CD standard. Discontinued 1998.

**Tier progression:**
1. 68070 basics (68000 variant, integrated peripherals)
2. CD-ROM access (Green Book, CD-i format)
3. 384×280 graphics (interlaced, PAL/NTSC)
4. 16.7M color support (24-bit true color!)
5. Mouse input (PC-style pointing device)
6. Keyboard input (full QWERTY)
7. CD-DA audio (audio CD playback)
8. ADPCM audio (compressed voice/sound)
9. FMV playback (full-motion video, MPEG-1)
10. CD-i OS integration (RTOS services)
11. Multimedia applications (games + education + movies)
12. Non-volatile RAM (save data)
13. Digital Video cartridge (MPEG-1 hardware)
14. Karaoke applications (unique CD-i feature!)
15. Interactive movies (Dragon's Lair-style)
16. Complete CD-i multimedia apps

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced 68070 techniques, FMV mastery, multimedia integration, CD-ROM optimization

#### New Patterns:
- **68070 optimization** - Efficient 68000-family code
- **CD-ROM streaming** - Continuous data loading
- **FMV integration** - Gameplay + video seamless
- **MPEG-1 mastery** - Digital Video cartridge usage
- **CD-DA + ADPCM hybrid** - Music + voice simultaneously
- **Mouse-driven UI** - Point-and-click interfaces
- **Keyboard integration** - Text input, shortcuts
- **24-bit graphics** - True color art (16.7M colors!)
- **Multimedia authoring** - Interactive presentations
- **Karaoke systems** - Lyrics + music + scoring
- **Educational software** - Interactive learning
- **CD-i OS mastery** - Deep RTOS integration

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Digital Video cartridge (MPEG-1)
**Focus:** MPEG-1 video playback, enhanced multimedia

#### Phase 3 Enhancement: Digital Video Cartridge (1993)
- **Digital Video cartridge** - MPEG-1 hardware decoder!
- **Full-screen video** - 352×240 MPEG-1 playback
- **VideoCD support** - Play VideoCD discs
- **Better video quality** - Hardware acceleration
- **Photo CD support** - View Photo CD images
- **Optional accessory** - Not included with console

**Tier 40 Example - MPEG-1 Hardware Detection:**
```asm
; Detect Digital Video cartridge presence

DetectDigitalVideo:
        ; Check for MPEG decoder hardware
        move.l  #$00304000,a0   ; MPEG decoder address
        move.w  #$5555,(a0)     ; Test pattern
        cmp.w   #$5555,(a0)
        bne     no_mpeg

has_mpeg:
        ; Digital Video cartridge present!
        move.w  #1,MPEG_AVAILABLE
        ; Can play MPEG-1 video, VideoCD, Photo CD
        rts

no_mpeg:
        ; No Digital Video cartridge
        move.w  #0,MPEG_AVAILABLE
        ; Fall back to software video playback
        rts

MPEG_AVAILABLE: dc.w    0
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional multimedia development, FMV mastery, CD-i OS proficiency

#### Advanced Techniques:
- **68070 mastery** - Cycle-perfect code
- **CD-ROM optimization** - Fast streaming from CD
- **MPEG-1 showcase** - Professional video quality
- **24-bit graphics mastery** - Beautiful true color art
- **Mouse UI excellence** - Professional interfaces
- **Keyboard input mastery** - Text adventures, typing tutors
- **CD-DA mastery** - High-quality audio CD playback
- **ADPCM depth** - Compressed voice acting
- **Multimedia authoring** - Complex interactive titles
- **Karaoke production** - Full karaoke systems
- **Educational depth** - Comprehensive learning software
- **CD-i OS depth** - Advanced RTOS usage

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Multimedia genres (education, karaoke, interactive movies, games)

#### Genre Specializations:
- **Interactive movies** - Dragon's Lair, full FMV games
- **Educational software** - Learning applications (CD-i strength!)
- **Karaoke applications** - Music + lyrics + scoring
- **Point-and-click adventures** - Mouse-driven games
- **Photo CD viewers** - Image browsing applications
- **VideoCD players** - Movie playback software
- **Multimedia encyclopedias** - Interactive references
- **Training software** - Corporate/industrial training

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum multimedia capability, FMV mastery

#### Limit-Pushing Techniques:
- **68070 maximum** - Every cycle optimized
- **CD-ROM streaming mastery** - Zero-load continuous streaming
- **MPEG-1 showcase** - Professional video quality
- **24-bit graphics showcase** - Beautiful true color
- **Mouse UI mastery** - Complex interfaces
- **CD-DA excellence** - High-quality audio
- **ADPCM showcase** - Extensive voice acting
- **Multimedia depth** - Complex interactive titles
- **Karaoke perfection** - Professional karaoke systems
- **Educational excellence** - Comprehensive learning

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial multimedia titles, professional FMV games

#### Commercial Techniques:
- **Commercial quality** - Professional CD-i titles
- **FMV excellence** - Seamless video integration
- **Multimedia mastery** - Games + education + movies
- **24-bit polish** - Beautiful true color graphics
- **Mouse UI perfection** - Professional interfaces
- **Karaoke showcases** - Full-featured systems
- **Educational showcases** - Comprehensive learning
- **Interactive movie quality** - Dragon's Lair level!

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development, emulation

#### Modern Development:
- **MAME/MESS emulation** - CD-i emulation support
- **Modern 68000 toolchains** - GCC, cross-compilers
- **CD-i homebrew** - CD-R burning for CD-i
- **Community techniques** - CD-i preservation scene
- **68070/68000 knowledge** - Transfers to Amiga, Atari ST!
- **Multimedia expertise** - Interactive CD development
- **Historical research** - Understanding CD-i's niche

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Multimedia Patterns (Phase 2)** - 75 FMV + CD techniques
3. **MPEG Patterns (Phase 3)** - 50 Digital Video cartridge
4. **Advanced Patterns (Phase 4-5)** - 100 68070 + multimedia
5. **Genre Patterns (Phase 5-6)** - 150 specialized applications
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Philips CD-i (1991-1998)**
- Philips/Signetics 68070 @ 15.5MHz (68000 variant!)
- 1-2MB RAM (varies by model, expandable)
- 384×280 resolution (PAL interlaced), 384×240 (NTSC)
- 16.7 million colors (24-bit true color!)
- CD-ROM drive (Green Book standard)
- CD-DA audio (audio CD playback)
- ADPCM audio (compressed voice/sound)
- Keyboard support (full QWERTY)
- Mouse support (PC-style pointing device)
- CD-i OS (real-time operating system)
- Non-volatile RAM (save data)
- $700 launch price (very expensive!)

**Phase 3+: Digital Video Cartridge (1993)**
- MPEG-1 hardware decoder
- 352×240 video playback
- VideoCD support
- Photo CD support
- Optional accessory

**Phase 7-8: Modern Homebrew**
- CD-R burning (create CD-i discs)
- Modern development tools (MAME, GCC 68000)
- CD-i homebrew scene (small)

## Spiral Learning Example: Interactive Educational Title (CD-i Strength!)

**Phase 1 (Tier 14):** Simple education app, CD-ROM assets, mouse UI. (~400 lines)

**Phase 2 (Tier 30):** Interactive lessons, FMV instruction, CD-DA audio. (~1000 lines)

**Phase 3 (Tier 38):** MPEG-1 video lessons, Digital Video cartridge. (~1400 lines)

**Phase 4 (Tier 46):** Comprehensive learning system, progress tracking. (~2000 lines)

**Phase 5 (Tier 50):** Full educational platform, many subjects. (~2800 lines)

**Phase 6 (Tier 54):** Maximum multimedia, FMV showcase. (~3600 lines)

**Phase 7 (Tier 57):** Commercial educational software - professional quality. (~4500 lines)

**Phase 8 (Tier 59):** Modern homebrew, CD-R mastering. (~4500 lines + tooling)

## Key Differences from Other Platforms

1. **68070 CPU** - 68000 variant with integrated peripherals!
2. **CD-ROM Only** - No cartridge slot!
3. **Multimedia Focus** - Games + education + movies + karaoke!
4. **$700 Launch** - Very expensive!
5. **24-bit True Color** - 16.7M colors!
6. **Keyboard + Mouse** - PC-style peripherals
7. **FMV Capable** - Full-motion video, MPEG-1
8. **Infamous Nintendo Games** - Zelda CDi, Mario!
9. **~570 Titles** - Many non-games
10. **Commercial Failure** - As game console, better as multimedia player

## Success Criteria

**By Phase 4, learners can:**
- Write 68070 assembly fluently (68000 family!)
- Access CD-ROM efficiently (Green Book)
- Program 24-bit graphics (true color!)
- Integrate FMV seamlessly (MPEG-1)
- Create mouse-driven interfaces
- Support keyboard input
- Play CD-DA and ADPCM audio
- Integrate with CD-i OS (RTOS)
- Design multimedia applications

**By Phase 8, learners can:**
- Develop commercial-quality CD-i software
- Master 68070/68000 architecture (transfers to Amiga, Atari ST!)
- Work with modern homebrew tools (MAME, CD-R)
- Create professional multimedia titles
- Contribute to CD-i preservation
- Release custom CD-i discs

## Resources Required

**Phase 1-2:**
- MAME or MESS emulator (CD-i support)
- GCC 68000 or assembler
- Text editor
- CD-i reference documentation
- Green Book CD-i specification

**Phase 7-8:**
- CD-R burner (create CD-i discs)
- Philips CD-i hardware (optional, collector's item!)
- Modern development tools
- CD-i homebrew resources

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** 68070/68000 mastery (transfers to Amiga, Atari ST, Mac!), CD-ROM multimedia development, FMV integration, MPEG-1 video, 24-bit true color graphics, interactive multimedia, understanding CD-based gaming transition, Green Book CD-i format, multimedia authoring, karaoke systems, educational software development, infamous Nintendo games study!
