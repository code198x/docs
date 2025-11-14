# Sega Mega Jet Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Sega Mega Jet (1994) → Portable Genesis for airlines!
**Approach:** Game-first, pattern library, 68000 mastery, Genesis compatibility
**Gateway:** Direct to assembly (Genesis/Mega Drive development)
**Historical Note:** Sega portable (1994, Japan-only), 68000 @ 7.67MHz (SAME as Genesis!), 100% Genesis/Mega Drive cartridge compatible, designed for airline in-flight entertainment (Japan Airlines!), also available retail (limited, rare), 320×240 resolution, battery powered or AC adapter, small built-in screen, full Genesis hardware, released AFTER Sega CD but BEFORE Sega Saturn/Nomad, precursor to Sega Nomad (1995), very rare and expensive, commercial obscurity but historical significance, MAME emulation available

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Sega Mega Jet (portable Genesis) has no BASIC. Uses standard Genesis/Mega Drive development (assembly or C via SGDK). Curriculum begins with assembly.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** 68000 fundamentals, Genesis VDP, portable optimization, battery efficiency, airline usage context
**Professional Autoload:** From lesson 1, all programs professionally load from Genesis cartridge

#### Pattern Library Established:
- **68000 patterns** - Motorola 68000 @ 7.67MHz (SAME as Genesis!)
- **Genesis VDP** - Video Display Processor (same as home console!)
- **320×240 resolution** - Genesis resolution
- **64 colors on-screen** - From 512-color palette
- **64KB RAM** - Genesis RAM
- **64KB VRAM** - Genesis VRAM
- **Z80 sound co-processor** - 8KB RAM, PSG + YM2612 FM
- **Genesis cartridge compatible** - 100% compatible!
- **Portable design** - Battery powered, built-in screen
- **Airline usage** - In-flight entertainment context
- **D-pad + 3 buttons** - A, B, C (Genesis controls)

#### Example Tier 1 Lesson: "Your First Mega Jet Game"
```asm
; Sega Mega Jet Assembly - Lesson 001
; Portable Genesis game
; 68000 @ 7.67 MHz (SAME as Genesis!)

; Motorola 68000 architecture:
; - 32-bit registers (D0-D7 data, A0-A7 address)
; - 16-bit data bus
; - 24-bit address bus
; - Big-endian
; - No hardware multiply/divide (unlike 68020+)

; Mega Jet is 100% Genesis hardware!
; ALL Genesis programming techniques apply!

        .org    $00000000

; Genesis/Mega Jet memory map (SAME!)
ROM_START       = $00000000     ; ROM base
RAM_START       = $00FF0000     ; 64KB RAM
VDP_DATA        = $00C00000     ; VDP data port
VDP_CTRL        = $00C00004     ; VDP control port
Z80_RAM         = $00A00000     ; Z80 sound RAM (8KB)
CTRL_DATA1      = $00A10003     ; Controller 1 data
CTRL_DATA2      = $00A10005     ; Controller 2 data
VERSION         = $00A10001     ; Version register

; Entry point (Genesis standard)
START:  ; Initialize
        move.w  #$2700,sr       ; Disable interrupts
        move.l  #$00FFFE00,sp   ; Set stack pointer

        ; Initialize Genesis VDP (standard)
        jsr     InitVDP

        ; Clear VRAM
        jsr     ClearVRAM

        ; Load tiles
        lea     TILE_DATA,a0
        move.l  #$40000000,d0   ; VRAM address $0000
        jsr     LoadToVRAM

        ; Set palette
        lea     PALETTE_DATA,a0
        move.l  #$C0000000,d0   ; CRAM address
        jsr     LoadPalette

        ; Initialize sprite
        move.w  #160,d0         ; X = 160 (center)
        move.w  #120,d1         ; Y = 120 (center)
        jsr     SetSpritePos

MAIN_LOOP:
        ; Wait for VBlank
        jsr     WaitVBlank

        ; MEGA JET SPECIFIC: Check battery level
        ; (Important for portable use!)
        jsr     CheckBattery

        ; Read controller (Genesis standard)
        jsr     ReadController
        move.b  d0,d7           ; Save input

        ; Check right
        btst    #0,d7
        beq     .check_left
        ; Move sprite right
        move.w  SPRITE_X,d0
        addq.w  #1,d0
        cmp.w   #320,d0
        blt     .update_x
        moveq   #0,d0
.update_x:
        move.w  d0,SPRITE_X

.check_left:
        btst    #1,d7
        beq     .check_down
        ; Move sprite left
        move.w  SPRITE_X,d0
        subq.w  #1,d0
        bge     .update_x2
        move.w  #319,d0
.update_x2:
        move.w  d0,SPRITE_X

.check_down:
        btst    #2,d7
        beq     .check_up
        ; Move sprite down
        move.w  SPRITE_Y,d1
        addq.w  #1,d1
        cmp.w   #240,d1
        blt     .update_y
        moveq   #0,d1
.update_y:
        move.w  d1,SPRITE_Y

.check_up:
        btst    #3,d7
        beq     .check_button

        ; Move sprite up
        move.w  SPRITE_Y,d1
        subq.w  #1,d1
        bge     .update_y2
        move.w  #239,d1
.update_y2:
        move.w  d1,SPRITE_Y

.check_button:
        ; Check A button (play sound)
        btst    #4,d7
        beq     .no_sound
        jsr     PlaySound

.no_sound:
        ; Update sprite on screen
        move.w  SPRITE_X,d0
        move.w  SPRITE_Y,d1
        jsr     SetSpritePos

        bra     MAIN_LOOP

; Initialize VDP (Genesis standard)
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

; MEGA JET SPECIFIC: Check battery level
CheckBattery:
        ; Mega Jet has battery status register
        ; (Portable-specific feature)
        move.b  $A14001,d0      ; Battery status
        andi.b  #$0F,d0
        cmpi.b  #$02,d0
        bgt     .battery_ok
        ; Low battery - could show warning
.battery_ok:
        rts

; Other routines (standard Genesis code)
ClearVRAM:
        move.l  #$40000000,VDP_CTRL
        move.w  #$7FFF,d0
.loop:  move.w  #$0000,VDP_DATA
        dbra    d0,.loop
        rts

LoadToVRAM:
        ; a0 = source, d0 = VDP command
        move.l  d0,VDP_CTRL
        move.w  #511,d1
.loop:  move.l  (a0)+,VDP_DATA
        dbra    d1,.loop
        rts

LoadPalette:
        ; a0 = palette, d0 = CRAM command
        move.l  d0,VDP_CTRL
        move.w  #15,d1
.loop:  move.w  (a0)+,VDP_DATA
        dbra    d1,.loop
        rts

SetSpritePos:
        ; d0 = X, d1 = Y
        ; (Write to sprite attribute table)
        rts

WaitVBlank:
        move.w  VDP_CTRL,d0
.wait:  move.w  VDP_CTRL,d0
        andi.w  #$0008,d0
        beq     .wait
        rts

ReadController:
        ; Read Genesis controller
        move.b  #$40,CTRL_DATA1
        nop
        nop
        move.b  CTRL_DATA1,d0
        andi.b  #$3F,d0
        rts

PlaySound:
        ; Use Z80 sound processor (Genesis standard)
        rts

; Data
SPRITE_X:       dc.w    160
SPRITE_Y:       dc.w    120
TILE_DATA:      incbin  "tiles.bin"
PALETTE_DATA:
        dc.w    $0000,$000E,$00E0,$0E00,$000E,$0E0E,$00EE,$0EEE
        dc.w    $0000,$0006,$0060,$0600,$0066,$0606,$0666,$0666

; Genesis ROM header (standard)
        .org    $000100
        dc.b    "SEGA MEGA DRIVE "
        dc.b    "(C)SEGA 1994.JAN"
        dc.b    "MEGA JET GAME                           "
        dc.b    "MEGA JET GAME                           "
        dc.b    "GM XXXXXXXX-XX"
        dc.w    $0000
        dc.b    "J               "  ; Japan only!
        dc.l    $00000000,$003FFFFF
        dc.l    $00FF0000,$00FFFFFF
        dc.b    "RA",$F820,$0020
        dc.l    $00000000,$00000000
        dc.b    "               "
        dc.b    "               "
        dc.b    "               "
        dc.b    "JUE             "  ; Japan, USA, Europe
```

**Key teaching moment:** Sega Mega Jet is portable GENESIS with 100% cartridge compatibility! Same 68000 @ 7.67MHz as home console! Designed for Japan Airlines in-flight entertainment (unique market!). Released in 1994 (AFTER Sega CD, BEFORE Saturn/Nomad!). Battery powered with built-in screen. Full Genesis hardware (VDP, Z80, PSG + YM2612 FM). Precursor to Sega Nomad (1995, worldwide). Very rare and expensive. All Genesis programming techniques apply! Japan-only. Commercial obscurity but historical significance!

**Tier progression:**
1. 68000 basics (same as Genesis!)
2. Genesis VDP (Video Display Processor)
3. 320×240 graphics (Genesis resolution)
4. 64 colors on-screen (Genesis palette)
5. Sprite system (Genesis sprites)
6. Controller input (Genesis pad)
7. Z80 sound processor (PSG + YM2612 FM)
8. Battery optimization (portable-specific!)
9. Built-in screen (portable display)
10. Genesis cartridge compatibility (100%!)
11. Portable design patterns (battery life!)
12. Airline usage context (in-flight entertainment)
13. VBlank timing (Genesis standard)
14. DMA transfers (Genesis optimization)
15. Genesis game techniques (all apply!)
16. Complete Mega Jet/Genesis games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced Genesis techniques, portable optimization, battery efficiency, airline entertainment design

#### New Patterns:
- **Genesis mastery** - All Genesis techniques applicable!
- **VDP optimization** - Fast graphics updates
- **Sprite coordination** - 64 sprites, 8×8 or 16×16
- **Z80 sound mastery** - PSG + YM2612 FM synthesis
- **DMA efficiency** - Fast VRAM transfers
- **Battery profiling** - Portable power optimization!
- **Screen size** - Designing for small built-in screen
- **Airline context** - In-flight entertainment design
- **64KB RAM mastery** - Genesis memory management
- **Controller precision** - Genesis 3-button (or 6-button)
- **Genesis compatibility** - 100% cartridge support!

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Understanding Mega Jet vs Nomad
**Focus:** Mega Jet (1994) vs Nomad (1995) differences

#### Phase 3 Enhancement: Mega Jet vs Nomad
- **Mega Jet** (1994, Japan) - Airline/limited retail
- **Sega Nomad** (1995, worldwide) - Retail handheld
- **Same Genesis hardware** - Both 100% compatible!
- **Different form factors** - Mega Jet more compact
- **Different markets** - Airline vs consumer retail
- **Nomad improvements** - Better ergonomics, TV out

**Note:** Mega Jet preceded Nomad by 1 year. Mega Jet was Japan-only airline/limited retail. Nomad was worldwide consumer release with better design.

**Tier 40 Example - Battery Optimization:**
```asm
; Battery optimization for Mega Jet portable use

OptimizeBattery:
        ; Reduce VDP updates when battery low
        jsr     CheckBattery
        cmpi.b  #$03,d0
        bgt     .normal

low_battery_mode:
        ; Reduce frame rate to save power
        move.b  #$01,LOW_POWER
        ; Dim display (if supported)
        move.b  #$80,VDP_BRIGHTNESS
        rts

.normal:
        move.b  #$00,LOW_POWER
        move.b  #$FF,VDP_BRIGHTNESS
        rts

LOW_POWER:      dc.b    0
VDP_BRIGHTNESS: equ     $A14002 ; Mega Jet specific
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional Genesis programming, portable game design, airline entertainment

#### Advanced Techniques:
- **68000 mastery** - Efficient Genesis code
- **VDP depth** - Advanced graphics techniques
- **Sprite mastery** - Complex sprite usage (64 sprites!)
- **Z80 sound depth** - Complex FM synthesis
- **DMA mastery** - Optimal VRAM transfers
- **Battery excellence** - Maximum portable play time!
- **Genesis optimization** - Fast, smooth games
- **64KB RAM efficiency** - Complex game states
- **Portable design** - Screen size considerations
- **Airline suitability** - In-flight entertainment design

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Genesis games optimized for portable/airline use

#### Genre Specializations:
- **Action games** - Sonic, platformers
- **RPGs** - Phantasy Star-style
- **Puzzle games** - Columns, Dr. Robotnik
- **Fighting games** - Streets of Rage
- **Sports games** - NHL, FIFA
- **Shooters** - Thunder Force, R-Type
- **Strategy games** - Shining Force
- **Arcade ports** - Golden Axe, Altered Beast

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing Genesis boundaries
**Focus:** Maximum Genesis performance on portable hardware

#### Limit-Pushing Techniques:
- **68000 maximum** - Cycle-perfect code
- **VDP showcase** - Advanced graphics effects
- **Sprite flickering** - >64 objects via flicker
- **Z80 sound showcase** - Complex FM + PSG
- **DMA showcase** - Fast graphics updates
- **Battery perfection** - Maximum play time!
- **Genesis limits** - Blast processing!
- **Portable excellence** - Best handheld Genesis experience

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial Genesis games on Mega Jet

#### Commercial Techniques:
- **Commercial quality** - Sonic 2, Shinobi III level!
- **Graphics polish** - Beautiful Genesis art
- **Sprite excellence** - Smooth 60 FPS animation
- **FM synthesis mastery** - Professional Genesis sound
- **Portable polish** - Perfect for airline/handheld
- **Genesis showcase** - Best Genesis capabilities
- **Battery optimization** - Long play sessions
- **Professional standards** - 1994 Genesis quality

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s Genesis/Mega Jet homebrew, modern tools

#### Modern Development:
- **MAME/Fusion emulation** - Mega Jet emulation
- **SGDK (Sega Genesis Dev Kit)** - Modern Genesis toolchain
- **GCC 68000** - Modern compiler
- **Flash cartridges** - Everdrive, homebrew
- **Genesis community** - Active homebrew scene!
- **Modern Genesis tools** - Debuggers, graphics editors
- **Cross-platform 68000** - Amiga, Atari ST, Mac knowledge transfer
- **Mega Jet/Nomad support** - Portable Genesis development

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 Genesis fundamentals
2. **Advanced Patterns (Phase 2)** - 75 Genesis optimization
3. **Portable Patterns (Phase 3)** - 50 battery + Mega Jet specific
4. **Mastery Patterns (Phase 4-5)** - 100 68000 + Genesis depth
5. **Genre Patterns (Phase 5-6)** - 150 Genesis game patterns
6. **Polish Patterns (Phase 7)** - 75 professional Genesis techniques
7. **Modern Patterns (Phase 8)** - 50 contemporary homebrew

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-8: Sega Mega Jet (1994, Japan-only)**
- Motorola 68000 @ 7.67MHz (SAME as Genesis!)
- 64KB RAM (Genesis RAM)
- 64KB VRAM (Genesis VRAM)
- Z80 @ 3.58MHz (sound co-processor)
- 8KB Z80 RAM
- 320×240 resolution (Genesis!)
- 64 colors on-screen (from 512-color palette)
- VDP (Genesis Video Display Processor)
- PSG + YM2612 FM synthesis (Genesis sound!)
- 100% Genesis cartridge compatible!
- Battery powered (4× AA) or AC adapter
- Built-in small screen
- D-pad + 3 buttons (A, B, C)
- Airline in-flight entertainment use
- Limited retail (Japan only)

**Relationship to Nomad (1995):**
- Mega Jet → Nomad evolution
- Same Genesis hardware
- Different form factors
- Mega Jet: Japan, airline
- Nomad: worldwide, retail

**Phase 7-8: Modern Homebrew**
- Everdrive flash cartridges
- SGDK (Sega Genesis Dev Kit)
- Modern Genesis homebrew scene (very active!)
- MAME/Fusion emulation

## Spiral Learning Example: Action Game (Genesis/Portable!)

**Phase 1 (Tier 12):** Simple platformer, Genesis sprites, portable battery. (~200 lines)

**Phase 2 (Tier 28):** Advanced platformer, Genesis VDP, FM audio. (~500 lines)

**Phase 3 (Tier 36):** Battery optimization, portable design. (~650 lines)

**Phase 4 (Tier 44):** Complex platformer, Genesis mastery. (~850 lines)

**Phase 5 (Tier 49):** Complete Genesis-quality platformer! (~1100 lines)

**Phase 6 (Tier 53):** Maximum Genesis performance, portable polish. (~1350 lines)

**Phase 7 (Tier 57):** Sonic-quality game for Mega Jet! (~1600 lines)

**Phase 8 (Tier 59):** Modern homebrew, flash cart, SGDK. (~1600 lines + tooling)

## Key Differences from Other Platforms

1. **Portable Genesis** - 100% cartridge compatible!
2. **Airline Design** - Japan Airlines in-flight entertainment!
3. **68000 @ 7.67MHz** - SAME as Genesis home console!
4. **Full Genesis Hardware** - VDP, Z80, PSG + YM2612!
5. **Preceded Nomad** - 1994 (Nomad was 1995)
6. **Japan-Only** - Limited retail + airline use
7. **Very Rare** - Commercial obscurity
8. **Historical Significance** - Precursor to Nomad
9. **Battery Powered** - Portable design
10. **Genesis Knowledge Transfer** - All techniques apply!

## Success Criteria

**By Phase 4, learners can:**
- Write 68000 assembly fluently (Genesis!)
- Master Genesis VDP programming
- Program Genesis sprites (64 sprites!)
- Use Z80 sound processor (PSG + YM2612 FM)
- Optimize for portable battery life
- Create Genesis-compatible games
- Design for small built-in screen
- Understand airline entertainment context

**By Phase 8, learners can:**
- Develop commercial-quality Genesis/Mega Jet games
- Master 68000 architecture (transfers to Amiga, Atari ST, Mac!)
- Work with modern Genesis homebrew tools (SGDK!)
- Create Sonic-quality games
- Contribute to active Genesis homebrew scene
- Release flash cart games (Everdrive!)
- Apply Genesis knowledge to Mega Jet/Nomad

## Resources Required

**Phase 1-2:**
- MAME or Fusion emulator (Mega Jet/Genesis support)
- SGDK (Sega Genesis Dev Kit) - modern!
- GCC 68000 or assembler
- Text editor
- Genesis programming documentation

**Phase 7-8:**
- Everdrive flash cartridge
- Sega Mega Jet hardware (optional, very rare!)
- Sega Genesis/Mega Drive (more common alternative)
- Modern development tools (SGDK, debuggers)

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** 68000 mastery (transfers to Genesis, Nomad, Amiga, Atari ST, Mac!), full Genesis programming (100% compatible!), portable game design, battery optimization, airline entertainment context, understanding Mega Jet → Nomad evolution, Genesis homebrew scene (very active!), rare platform study, precursor to Nomad, historical significance!
