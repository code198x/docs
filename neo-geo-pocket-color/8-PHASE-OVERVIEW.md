# Neo Geo Pocket Color Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Neo Geo Pocket Color (1998-2001) → SNK's 16-bit color handheld powerhouse
**Approach:** Game-first, pattern library, TLCS-900H mastery, 4096-color graphics, clicky thumbstick
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** SNK's 16-bit color handheld (1998), Toshiba TLCS-900H @ 6.144MHz (16-bit CPU!), 160×152 LCD with 4,096 colors (146 on-screen!), 12KB RAM + 64KB VRAM, cartridge-based, clicky thumbstick innovation (best handheld d-pad!), 40-hour battery life (2× AA!), backward compatible with Neo Geo Pocket (B&W), ~82 games (fighting game excellence!), competed with Game Boy Color, commercial failure (~2M units vs GBC's 118.7M), discontinued 2001 after SNK bankruptcy, cult following, VERY active homebrew scene!, historically significant for SNK's last handheld and incredible game library quality

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Neo Geo Pocket Color had no BASIC. Curriculum begins directly with assembly, focused on Toshiba TLCS-900H architecture and efficient 16-bit handheld programming.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** TLCS-900H fundamentals, 4096-color LCD programming, clicky thumbstick input, 12KB RAM efficiency, cartridge optimization
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **TLCS-900H patterns** - Toshiba TLCS-900H @ 6.144MHz (16-bit!)
- **160×152 LCD** - 4,096 colors total, 146 on-screen!
- **12KB RAM** - Efficient memory management critical!
- **64KB VRAM** - Video memory for sprites/tiles
- **Clicky thumbstick** - Best handheld control!
- **40-hour battery** - 2× AA, incredible efficiency!
- **Cartridge ROM** - Up to 16MB
- **NGP backward compatible** - Plays B&W Neo Geo Pocket games!
- **16-bit sprites** - Hardware sprite support
- **Z80 sound** - Z80 @ 3.072MHz for audio!

#### Example Tier 1 Lesson: "Your First NGPC Color Sprite"
```asm
; Neo Geo Pocket Color Assembly - Lesson 001
; Color sprite on 160×152 LCD
; Toshiba TLCS-900H @ 6.144 MHz

; Toshiba TLCS-900H architecture (16-bit):
; - 16-bit CPU (8-bit/16-bit/32-bit operations)
; - Registers: XWA, XBC, XDE, XHL (32-bit extended registers)
; - Also: WA, BC, DE, HL (16-bit)
; - Also: A, B, C, D, E, H, L (8-bit)
; - Stack pointer: XSP (32-bit)
; - 256-level interrupts (sophisticated!)
; - NGPC has separate Z80 for sound!

        .org    $00000000

; Neo Geo Pocket Color memory map
ROM_BANK0       EQU $00000000   ; ROM bank 0 (32KB)
ROM_BANK1       EQU $00008000   ; ROM bank 1+ (32KB switchable)
RAM             EQU $00004000   ; Main RAM (12KB)
VRAM            EQU $0000A000   ; VRAM (64KB)
HARDWARE        EQU $00008000   ; Hardware registers

; Hardware registers (NGPC-specific)
LCD_CONTROL     EQU $8000       ; LCD control
LCD_HWIDTH      EQU $8002       ; Horizontal width
LCD_VHEIGHT     EQU $8003       ; Vertical height
LCD_PALETTE     EQU $8100       ; Palette RAM (512 bytes, 256 colors!)
SPRITE_RAM      EQU $8800       ; Sprite attribute RAM
TILE_RAM        EQU $9000       ; Tile data RAM
BG_SCROLL_X     EQU $8020       ; Background scroll X
BG_SCROLL_Y     EQU $8021       ; Background scroll Y

; Input registers
INPUT_PORT      EQU $8010       ; Input port (thumbstick + buttons)

; Interrupt registers
INT_ENABLE      EQU $8080       ; Interrupt enable
INT_PRIORITY    EQU $8081       ; Interrupt priority

; Z80 sound CPU registers
Z80_CONTROL     EQU $8090       ; Z80 control
Z80_COMM        EQU $8091       ; Z80 communication

START:
        ; Disable interrupts during init
        di

        ; Set up stack pointer
        ld      xsp,RAM+$3000   ; Stack near top of 12KB RAM

        ; Initialize LCD
        ld      a,$C0           ; LCD on, color mode
        ld      (LCD_CONTROL),a
        ld      a,160           ; Horizontal width
        ld      (LCD_HWIDTH),a
        ld      a,152           ; Vertical height
        ld      (LCD_VHEIGHT),a

        ; Check if we're on NGPC vs NGP (B&W)
        ld      a,(LCD_CONTROL)
        and     $40             ; Color mode bit
        jr      z,ngp_bw_mode

ngpc_color_mode:
        ; NGPC color mode available!

        ; Set up color palette (4096 colors, RGB444!)
        ld      hl,LCD_PALETTE
        ld      bc,PALETTE_DATA
        ld      de,16           ; Load 16 colors

.load_palette:
        ld      a,(bc)          ; Low byte
        ld      (hl),a
        inc     hl
        inc     bc
        ld      a,(bc)          ; High byte
        ld      (hl),a
        inc     hl
        inc     bc
        dec     de
        jr      nz,.load_palette

ngp_bw_mode:
        ; Running on original NGP (backward compatibility!)
        ; Set up grayscale mode
        ; (NGPC code still works, just in grayscale)

        ; Load tile data to VRAM
        ld      hl,TILE_DATA
        ld      de,TILE_RAM
        ld      bc,128          ; One 8×8 tile (8 bytes/plane × 2 planes × 8)
        call    MemCopy

        ; Set up sprite in sprite RAM
        ld      hl,SPRITE_RAM

        ; Sprite 0: X position (80)
        ld      a,80
        ld      (hl),a
        inc     hl

        ; Sprite 0: Y position (76)
        ld      a,76
        ld      (hl),a
        inc     hl

        ; Sprite 0: Tile number (0)
        ld      a,0
        ld      (hl),a
        inc     hl

        ; Sprite 0: Attributes (palette 0, priority, no flip)
        ld      a,$00
        ld      (hl),a

        ; Enable VBlank interrupt
        ld      a,$01
        ld      (INT_ENABLE),a
        ei                      ; Enable interrupts

MAIN_LOOP:
        ; Wait for VBlank
        halt                    ; Wait for interrupt (battery efficient!)

        ; Read thumbstick input (NGPC's best feature!)
        ld      a,(INPUT_PORT)
        ld      b,a             ; Save input

        ; Check right
        bit     0,b
        jr      z,.check_left
        ld      hl,SPRITE_RAM   ; Sprite 0 X position
        ld      a,(hl)
        inc     a
        cp      160
        jr      c,.update_x
        xor     a
.update_x:
        ld      (hl),a

.check_left:
        bit     1,b
        jr      z,.check_down
        ld      hl,SPRITE_RAM
        ld      a,(hl)
        dec     a
        jr      nc,.update_x2
        ld      a,159
.update_x2:
        ld      (hl),a

.check_down:
        bit     2,b
        jr      z,.check_up
        ld      hl,SPRITE_RAM+1 ; Sprite 0 Y position
        ld      a,(hl)
        inc     a
        cp      152
        jr      c,.update_y
        xor     a
.update_y:
        ld      (hl),a

.check_up:
        bit     3,b
        jr      z,.check_a
        ld      hl,SPRITE_RAM+1
        ld      a,(hl)
        dec     a
        jr      nc,.update_y2
        ld      a,151
.update_y2:
        ld      (hl),a

.check_a:
        ; Check A button (clicky!)
        bit     4,b
        jr      z,.check_b

        ; Play sound via Z80
        ld      a,$01           ; Sound command
        ld      (Z80_COMM),a

.check_b:
        ; Check B button
        bit     5,b
        jr      z,MAIN_LOOP

        ; Option button - change palette
        ld      a,(SPRITE_RAM+3)
        add     a,$10           ; Next palette
        and     $F0
        ld      (SPRITE_RAM+3),a

        jr      MAIN_LOOP

; VBlank interrupt handler
VBlank:
        ; VBlank processing here
        ; Battery efficient: only update during VBlank!
        reti

MemCopy:
        ; HL = source, DE = dest, BC = length
        ld      a,(hl)
        ld      (de),a
        inc     hl
        inc     de
        dec     bc
        ld      a,b
        or      c
        jr      nz,MemCopy
        ret

; Palette data (RGB444 format, 4096 colors!)
PALETTE_DATA:
        ; Color 0: White (RGB444: F,F,F)
        dw      $0FFF
        ; Color 1: Light gray
        dw      $0AAA
        ; Color 2: Dark gray
        dw      $0555
        ; Color 3: Black
        dw      $0000
        ; Color 4: Red
        dw      $0F00
        ; Color 5: Green
        dw      $00F0
        ; Color 6: Blue
        dw      $000F
        ; Color 7: Yellow
        dw      $0FF0
        ; Colors 8-15: More colors
        dw      $0F0F,$00FF,$0F88,$0888
        dw      $0CCC,$0F44,$044F,$0080

; Tile data (8×8, 2 bitplanes)
TILE_DATA:
        ; Bitplane 0
        db      $3C,$7E,$FF,$FF,$FF,$FF,$7E,$3C
        ; Bitplane 1
        db      $00,$42,$81,$81,$81,$81,$42,$00

; Interrupt vector table (TLCS-900H uses vectors)
        .org    $0000FFF8
        dw      VBlank          ; VBlank vector
```

**Key teaching moment:** Neo Geo Pocket Color uses Toshiba TLCS-900H @ 6.144MHz - 16-bit CPU with sophisticated 256-level interrupts! 160×152 LCD with 4,096 colors (146 on-screen!). 12KB RAM (efficient programming essential!). 64KB VRAM. Clicky thumbstick (BEST handheld control ever!). 40-hour battery life (2× AA!). Backward compatible with B&W Neo Geo Pocket! Separate Z80 @ 3.072MHz for sound! ~82 games (incredible fighting game library!). Commercial failure (~2M units) vs GBC but CULT FOLLOWING! SNK bankruptcy 2001. VERY active homebrew scene! Incredible game quality despite small library!

**Tier progression:**
1. TLCS-900H basics (16-bit, XWA/XBC/XDE/XHL registers)
2. 4096-color LCD (RGB444, 146 on-screen)
3. Palette programming (256 colors, RGB444)
4. 12KB RAM management (efficiency critical!)
5. 64KB VRAM management
6. Sprite system (hardware sprites)
7. Tile system (background tiles)
8. Clicky thumbstick input (8-way + buttons)
9. VBlank interrupts (256-level system)
10. Z80 sound CPU (communication protocol)
11. NGP backward compatibility (detecting NGP vs NGPC)
12. Battery optimization (40-hour target!)
13. Cartridge banking (up to 16MB)
14. Background scrolling
15. Sprite/background priority
16. Complete NGPC color games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced color techniques, thumbstick mastery, Z80 sound depth, 12KB RAM efficiency optimization

#### New Patterns:
- **146-color optimization** - Maximum on-screen color usage
- **Palette animation** - Color cycling effects
- **Advanced scrolling** - Parallax, smooth scrolling
- **Z80 sound mastery** - Music, sound effects, PCM
- **Sprite multiplexing** - More sprites than hardware limit
- **Battery optimization** - Hitting 40-hour target
- **12KB RAM techniques** - Working within tight memory
- **Thumbstick precision** - Leveraging clicky feedback
- **NGP compatibility** - Games that work on both NGP and NGPC
- **Fast cartridge access** - Banking optimization

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - NGPC-exclusive vs NGP-compatible modes
**Focus:** Maximizing NGPC features, understanding NGP compatibility

#### Phase 3 Enhancement: NGPC Modes
- **NGPC exclusive** - Full color, won't boot on NGP
- **NGP compatible** - Works on both, color on NGPC
- **Color vs grayscale** - Detecting hardware
- **Palette modes** - 4096 colors vs 4 grays
- **Battery modes** - Power consumption optimization

**Tier 40 Example - NGP Compatible Mode:**
```asm
; NGPC enhanced game (works on both NGP and NGPC!)

DetectHardware:
        ; Check if NGPC color mode available
        ld      a,(LCD_CONTROL)
        and     $40             ; Color mode bit
        jr      z,on_ngp

on_ngpc:
        ; Running on NGPC!
        ld      a,1
        ld      (COLOR_MODE),a
        ; Set up color palettes
        call    SetupNGPCPalettes
        ret

on_ngp:
        ; Running on original NGP (B&W)
        ld      a,0
        ld      (COLOR_MODE),a
        ; Set up grayscale palettes
        call    SetupNGPPalettes
        ret

COLOR_MODE:     db 0
```

### Phase 4-8 Summary:

**Phase 4:** Professional TLCS-900H programming, color mastery, Z80 audio depth, SNK Neo Geo fighting game techniques

**Phase 5:** Genre specializations - Fighting games (SNK excellence!), puzzle games, action games, card battles

**Phase 6:** Maximum NGPC performance, 146-color showcase, complex games in 12KB RAM

**Phase 7:** Commercial AAA quality - SNK vs. Capcom, Metal Slug, King of Fighters level!

**Phase 8:** Modern homebrew - NGPC SDK, NGDevKit, active homebrew scene (VERY active!), flash carts

## Key Differences from Other Platforms

1. **16-bit CPU** - TLCS-900H @ 6.144MHz vs 8-bit GBC!
2. **4,096 Colors** - 146 on-screen from 4K palette (RGB444)!
3. **Clicky Thumbstick** - Best handheld control ever made!
4. **40-Hour Battery** - 2× AA, incredible efficiency!
5. **12KB RAM Only** - Efficient programming essential!
6. **Z80 Sound CPU** - Separate processor @ 3.072MHz!
7. **NGP Backward Compatible** - All B&W NGP games work!
8. **~82 Games** - Small but INCREDIBLE quality library!
9. **Cult Following** - ~2M units but passionate fans!
10. **Very Active Homebrew** - NGDevKit, modern scene!

---

**Total:** 4,096 lessons | **Time:** 2-4 years
**Unique Advantage:** TLCS-900H 16-bit mastery, 4096-color handheld programming, clicky thumbstick techniques, 12KB RAM efficiency, Z80 sound CPU coordination, NGP backward compatibility, SNK fighting game study, cult classic status, VERY active homebrew (NGDevKit!), best handheld d-pad ever!
