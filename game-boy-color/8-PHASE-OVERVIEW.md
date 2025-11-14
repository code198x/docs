# Game Boy Color Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Game Boy Color (1998-2003) → Color handheld that extended Game Boy dynasty
**Approach:** Game-first, pattern library, Sharp SM83 (Z80-like) mastery, color graphics, Game Boy backward compatibility
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Nintendo's color Game Boy (1998), Sharp SM83 @ 8MHz (Z80-like, 2× faster than original GB!), 160×144 LCD with 32,768 colors (56 on-screen!), 32KB RAM (4× original GB!), fully backward compatible with GB/SGB games, infrared port for wireless link, ~920 GBC-exclusive games + all GB games (~1000 total GB library!), 118.7M units sold (massive success!), dominated handheld market with Pokemon Gold/Silver/Crystal, Link's Awakening DX, Oracle games, continued GB dynasty, Game Boy Advance successor (2001), discontinued 2003, last GB-compatible handheld

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Game Boy Color had no BASIC. Curriculum begins directly with assembly, focused on Sharp SM83 architecture and color graphics while maintaining Game Boy compatibility.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** SM83 fundamentals, color LCD programming, 32KB RAM, infrared communication, GB backward compatibility
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **Sharp SM83 patterns** - Sharp SM83 @ 8MHz (Z80-like, 2× faster than GB!)
- **160×144 color LCD** - 32,768 colors total, 56 on-screen!
- **32KB RAM** - 4× original Game Boy!
- **Color palettes** - 8 background palettes + 8 sprite palettes
- **Infrared port** - Wireless communication!
- **GB backward compatible** - Plays all GB/SGB games!
- **Link cable** - 2-player multiplayer
- **8KB VRAM** - 2× original GB!
- **Cartridge ROM** - Up to 8MB with MBC
- **RTC** - Real-Time Clock (Pokemon Crystal!)

#### Example Tier 1 Lesson: "Your First GBC Color Sprite"
```asm
; Game Boy Color Assembly - Lesson 001
; Color sprite on 160×144 LCD
; Sharp SM83 @ 8 MHz (2× faster than original GB!)

; Sharp SM83 architecture (Z80-like):
; - 8-bit CPU, Z80-compatible
; - 8-bit accumulator (A)
; - Register pairs BC, DE, HL
; - Stack pointer SP
; - Flags: ZNHC (Zero, Negative, Half-carry, Carry)
; - Similar to Z80, some differences
; - GBC runs at 8MHz (original GB was 4MHz!)

        SECTION "Header",ROM0[$0100]
        nop
        jp      START

        ; GB/GBC ROM header (required!)
        db      $CE,$ED,$66,$66,$CC,$0D,$00,$0B ; Nintendo logo
        db      "GBC GAME    "  ; Title (11 chars)
        db      $80             ; GBC flag ($80 = GBC exclusive, $C0 = GBC enhanced)
        db      0,0             ; Licensee code
        db      0               ; SGB flag
        db      $1B             ; Cart type (MBC5+RAM+BATTERY)
        db      0               ; ROM size
        db      0               ; RAM size
        db      1               ; Destination (non-Japan)
        db      $33             ; Old licensee
        db      0               ; Version
        db      0               ; Header checksum
        dw      0               ; Global checksum

SECTION "GameCode",ROM0[$0150]

; Game Boy Color memory map
ROM0            EQU $0000       ; ROM bank 0 (16KB)
ROM1            EQU $4000       ; ROM bank 1+ (16KB switchable)
VRAM            EQU $8000       ; VRAM (8KB, 2 banks on GBC!)
SRAM            EQU $A000       ; External RAM
WRAM0           EQU $C000       ; Work RAM bank 0 (4KB)
WRAM1           EQU $D000       ; Work RAM bank 1+ (4KB, 7 banks on GBC!)
OAM             EQU $FE00       ; Sprite attribute table
HRAM            EQU $FF80       ; High RAM (127 bytes)

; GBC-specific registers
BCPS            EQU $FF68       ; Background color palette specification
BCPD            EQU $FF69       ; Background color palette data
OCPS            EQU $FF6A       ; Object color palette specification
OCPD            EQU $FF6B       ; Object color palette data
SVBK            EQU $FF70       ; WRAM bank select (GBC only!)
VBK             EQU $FF4F       ; VRAM bank select (GBC only!)
KEY1            EQU $FF4D       ; Speed switch (4MHz ↔ 8MHz!)

; LCD registers (same as GB)
LCDC            EQU $FF40       ; LCD control
STAT            EQU $FF41       ; LCD status
SCY             EQU $FF42       ; Scroll Y
SCX             EQU $FF43       ; Scroll X
LY              EQU $FF44       ; LCD Y coordinate
LYC             EQU $FF45       ; LCD Y compare
DMA             EQU $FF46       ; DMA transfer
BGP             EQU $FF47       ; BG palette (GB mode)
OBP0            EQU $FF48       ; Object palette 0 (GB mode)
OBP1            EQU $FF49       ; Object palette 1 (GB mode)

START:
        ; Wait for VBlank before init
        call    WaitVBlank

        ; Turn off LCD during setup
        xor     a
        ld      [LCDC],a

        ; Check if we're on GBC
        cp      $11             ; GBC sets A=$11 at boot
        jr      z,.is_gbc

        ; Running on original GB (backward compatibility!)
        ; Set up GB-compatible mode
        jr      .gb_mode

.is_gbc:
        ; GBC exclusive features available!

        ; Switch to double-speed mode (8MHz!)
        ld      a,$01
        ld      [KEY1],a
        stop                    ; Execute speed switch

        ; Set up GBC color palettes
        call    InitGBCPalettes

        ; Select VRAM bank 1 (GBC has 2 VRAM banks!)
        ld      a,1
        ld      [VBK],a

.gb_mode:
        ; Load tile data
        ld      hl,TILE_DATA
        ld      de,VRAM
        ld      bc,16           ; One 8×8 tile
        call    MemCopy

        ; Set up sprite in OAM
        ld      a,80            ; Y = 80
        ld      [OAM],a
        ld      a,80            ; X = 80
        ld      [OAM+1],a
        ld      a,0             ; Tile 0
        ld      [OAM+2],a
        ld      a,%00000000     ; Attributes (palette 0 on GBC)
        ld      [OAM+3],a

        ; Turn on LCD
        ld      a,%10010011     ; LCD on, BG on, Sprites on
        ld      [LCDC],a

MAIN_LOOP:
        ; Wait for VBlank
        call    WaitVBlank

        ; Read buttons
        call    ReadButtons
        ld      b,a             ; Save input

        ; Check right
        bit     0,b
        jr      z,.check_left
        ld      a,[OAM+1]       ; X position
        inc     a
        cp      160
        jr      c,.update_x
        xor     a
.update_x:
        ld      [OAM+1],a

.check_left:
        bit     1,b
        jr      z,.check_down
        ld      a,[OAM+1]
        dec     a
        jr      nc,.update_x2
        ld      a,159
.update_x2:
        ld      [OAM+1],a

.check_down:
        bit     2,b
        jr      z,.check_up
        ld      a,[OAM]         ; Y position
        inc     a
        cp      144
        jr      c,.update_y
        xor     a
.update_y:
        ld      [OAM],a

.check_up:
        bit     3,b
        jr      z,.check_a
        ld      a,[OAM]
        dec     a
        jr      nc,.update_y2
        ld      a,143
.update_y2:
        ld      [OAM],a

.check_a:
        ; Check A button
        bit     4,b
        jr      z,MAIN_LOOP

        ; Play sound
        ; (GBC has same sound as GB: 4 channels)

        jr      MAIN_LOOP

; Initialize GBC color palettes
InitGBCPalettes:
        ; Set background palette 0
        ld      a,$00           ; Palette 0, color 0
        ld      [BCPS],a

        ; Color 0: White (RGB555: 31,31,31)
        ld      a,$FF
        ld      [BCPD],a        ; Low byte
        ld      a,$7F
        ld      [BCPD],a        ; High byte

        ; Color 1: Light gray
        ld      a,$AD
        ld      [BCPD],a
        ld      a,$55
        ld      [BCPD],a

        ; Color 2: Dark gray
        ld      a,$52
        ld      [BCPD],a
        ld      a,$2A
        ld      [BCPD],a

        ; Color 3: Black
        ld      a,$00
        ld      [BCPD],a
        ld      a,$00
        ld      [BCPD],a

        ; Set sprite palette 0 (similar)
        ld      a,$00
        ld      [OCPS],a
        ; (Load sprite colors similarly)

        ret

WaitVBlank:
        ld      a,[LY]
        cp      144
        jr      c,WaitVBlank
        ret

ReadButtons:
        ; Read D-pad
        ld      a,$20           ; Select D-pad
        ld      [$FF00],a
        ld      a,[$FF00]
        ld      a,[$FF00]       ; Read twice for stability
        cpl                     ; Invert (pressed = 1)
        and     $0F
        swap    a
        ld      b,a

        ; Read buttons
        ld      a,$10           ; Select buttons
        ld      [$FF00],a
        ld      a,[$FF00]
        ld      a,[$FF00]
        cpl
        and     $0F
        or      b

        ret

MemCopy:
        ; HL = source, DE = dest, BC = length
        ld      a,[hl+]
        ld      [de],a
        inc     de
        dec     bc
        ld      a,b
        or      c
        jr      nz,MemCopy
        ret

; Tile data
TILE_DATA:
        db      $3C,$3C,$7E,$7E,$FF,$FF,$FF,$FF
        db      $FF,$FF,$7E,$7E,$3C,$3C,$00,$00
```

**Key teaching moment:** Game Boy Color uses Sharp SM83 @ 8MHz - 2× faster than original GB! 160×144 LCD with 32,768 colors (56 on-screen!). 32KB RAM (4× original GB!). 8KB VRAM with 2 banks! Infrared port for wireless communication! FULLY backward compatible with all GB/SGB games! ~920 GBC games + ~1000 GB games = massive library! 118.7M units sold! Pokemon Gold/Silver/Crystal! Link's Awakening DX! Dominated handheld market! GBA successor (2001). Discontinued 2003. Last GB-compatible handheld!

**Tier progression:**
1. SM83 basics (Z80-like, A/BC/DE/HL registers)
2. Color LCD (32,768 colors, 56 on-screen)
3. Color palettes (8 BG + 8 sprite palettes, RGB555)
4. 32KB RAM management (4× original GB!)
5. 2 VRAM banks (8KB each, GBC only!)
6. 7 WRAM banks (4KB each, GBC only!)
7. Speed switch (4MHz GB mode ↔ 8MHz GBC mode!)
8. Infrared port (wireless communication!)
9. Link cable (2-player multiplayer)
10. GB backward compatibility (detecting GB vs GBC)
11. RTC (Real-Time Clock, Pokemon!)
12. Sound (same 4 channels as GB)
13. DMA transfers
14. Sprites (40 sprites, 8×8 or 8×16)
15. Background/window layers
16. Complete GBC color games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced color techniques, infrared mastery, GB compatibility optimization, 32KB RAM mastery

#### New Patterns:
- **Color mastery** - 56 on-screen color optimization
- **Palette animation** - Color cycling effects
- **VRAM banking** - 2 banks for double tile data!
- **WRAM banking** - 7 banks for large game states!
- **Speed switching** - Dynamic 4MHz/8MHz switching
- **Infrared protocols** - Wireless 2-player!
- **GB compatibility** - Games that work on both GB and GBC
- **RTC usage** - Day/night cycles, time-based events
- **32KB RAM efficiency** - Large game states
- **Battery optimization** - Long play sessions (2× AA)

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - GBC-exclusive vs GB-compatible modes
**Focus:** Maximizing GBC features, understanding GB compatibility

#### Phase 3 Enhancement: GBC Modes
- **GBC exclusive** - ($80 flag) GBC-only, won't boot on GB
- **GBC enhanced** - ($C0 flag) Works on GB, better on GBC!
- **Speed modes** - 4MHz (GB compat) vs 8MHz (GBC full speed)
- **VRAM/WRAM banks** - GBC-only features
- **Color palettes** - GBC colors vs GB grayscale

**Tier 40 Example - GBC Enhanced Mode:**
```asm
; GBC enhanced game (works on both GB and GBC!)

DetectHardware:
        ; Check if GBC at boot
        cp      $11             ; A=$11 on GBC
        jr      z,on_gbc

on_gb:
        ; Running on original GB
        ; Use GB-compatible mode
        ld      a,0
        ld      [GBC_MODE],a
        ; Set up GB palettes
        call    SetupGBPalettes
        ret

on_gbc:
        ; Running on GBC!
        ld      a,1
        ld      [GBC_MODE],a
        ; Enable double-speed mode
        ld      a,$01
        ld      [KEY1],a
        stop
        ; Set up GBC color palettes
        call    SetupGBCPalettes
        ret

GBC_MODE:       db 0
```

### Phase 4-8 Summary:

**Phase 4:** Professional SM83 programming, color mastery, infrared depth, Pokemon-style features

**Phase 5:** Genre specializations - RPGs (Pokemon!), action-adventure (Zelda!), puzzles, platformers

**Phase 6:** Maximum GBC performance, 56-color showcase, complex games in 32KB RAM

**Phase 7:** Commercial AAA quality - Pokemon Gold/Silver, Zelda Oracle games level!

**Phase 8:** Modern homebrew - GBDK-2020 (modern SDK!), GB Studio, flash carts (EverDrive), active scene!

## Key Differences from Other Platforms

1. **2× Faster** - 8MHz vs 4MHz original GB!
2. **32,768 Colors** - 56 on-screen from 32K palette!
3. **4× RAM** - 32KB vs 8KB original GB!
4. **2 VRAM Banks** - 16KB total vs 8KB GB!
5. **7 WRAM Banks** - 32KB total banked RAM!
6. **Infrared Port** - Wireless communication!
7. **Full GB Compatibility** - All ~1000 GB games work!
8. **118.7M Units Sold** - Massive success!
9. **Pokemon Era** - Gold/Silver/Crystal dominated!
10. **Active Homebrew** - GBDK-2020, GB Studio, EverDrive!

---

**Total:** 4,096 lessons | **Time:** 2-4 years
**Unique Advantage:** SM83/Z80-like mastery, color handheld programming, GB backward compatibility, infrared wireless, Pokemon-era gaming, 118.7M units success story, active homebrew (GBDK-2020!), GB Studio visual development!
