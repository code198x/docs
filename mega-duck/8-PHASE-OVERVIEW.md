# Mega Duck Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Mega Duck / Cougar Boy (1993) → Game Boy clone
**Approach:** Game-first, pattern library, Z80 mastery, Game Boy-like development
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Hong Kong handheld (1993), Welback Holdings/Timlex manufacturer, Z80-like CPU @ 4MHz, 160×144 resolution (SAME as Game Boy!), 4 shades grayscale, budget GB competitor, incompatible cartridges (different pinout!), marketed in Europe/South America, also sold as Cougar Boy (Brazil), ~50 games (many GB ports), similar hardware to GB but legally distinct, ~$40-50 price (cheaper than GB!), limited commercial success, discontinued mid-1990s, interesting GB alternative study

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Mega Duck shipped without BASIC. Curriculum begins directly with assembly, focused on the Z80-like architecture and Game Boy-like hardware.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** Z80 fundamentals, 160×144 LCD, 4-shade grayscale, portable optimization, GB-like techniques
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **Z80 patterns** - Z80-like CPU @ 4MHz (similar to GB's Sharp LR35902!)
- **160×144 LCD** - Same resolution as Game Boy!
- **4 shades grayscale** - White, light gray, dark gray, black
- **8KB RAM** - Similar to GB
- **8KB VRAM** - Dedicated video memory
- **Hardware sprites** - 8×8 tiles, like GB
- **Background tiles** - Character-based background
- **Simple audio** - 4-channel PSG (GB-style!)
- **D-pad + 2 buttons** - A, B (GB-compatible controls!)
- **Portable optimization** - Battery life (4× AA)

#### Example Tier 1 Lesson: "Your First Mega Duck Sprite"
```asm
; Mega Duck Assembly - Lesson 001
; Display sprite on 160×144 LCD
; Z80 @ 4 MHz

; Mega Duck CPU (Z80-like, similar to GB's Sharp LR35902):
; - 8-bit accumulator (A)
; - Register pairs BC, DE, HL
; - Stack pointer SP
; - Flags: SZHC (Sign, Zero, Half-carry, Carry)
; - Similar to Z80 and Game Boy CPU

        .org    $0000

; Mega Duck memory map (similar to Game Boy!)
ROM_BASE        = $0000         ; ROM at $0000-$7FFF
VRAM_BASE       = $8000         ; 8KB VRAM at $8000-$9FFF
RAM_BASE        = $C000         ; 8KB RAM at $C000-$DFFF
LCD_CTRL        = $FF40         ; LCD control (like GB!)
LCD_STAT        = $FF41         ; LCD status
SCY             = $FF42         ; Scroll Y
SCX             = $FF43         ; Scroll X
LY              = $FF44         ; LCD Y coordinate
BGP             = $FF47         ; Background palette
OBP0            = $FF48         ; Sprite palette 0
OBP1            = $FF49         ; Sprite palette 1
BUTTONS         = $FF00         ; Button input (like GB!)
SOUND_CH1       = $FF10         ; Sound channel 1
SOUND_CH2       = $FF15         ; Sound channel 2
SOUND_CH3       = $FF1A         ; Sound channel 3
SOUND_CH4       = $FF1F         ; Sound channel 4

; Sprite OAM (Object Attribute Memory) at $FE00-$FE9F (like GB!)
OAM_BASE        = $FE00

START:  ; Initialize
        di                      ; Disable interrupts
        ld      sp,$FFFE        ; Set stack pointer

        ; Wait for VBlank
        call    WaitVBlank

        ; Turn off LCD during setup (like GB!)
        ld      a,$00
        ld      (LCD_CTRL),a

        ; Clear VRAM
        ld      hl,VRAM_BASE
        ld      bc,$2000        ; 8KB
        xor     a
.clear: ld      (hl),a
        inc     hl
        dec     bc
        ld      a,b
        or      c
        jr      nz,.clear

        ; Load tile data
        ld      hl,TILE_DATA
        ld      de,VRAM_BASE
        ld      bc,16           ; One 8×8 tile (16 bytes)
        call    MemCopy

        ; Set background palette (4 shades)
        ld      a,%11100100     ; Palette: dark -> light
        ld      (BGP),a
        ld      (OBP0),a

        ; Initialize sprite in OAM
        ld      hl,OAM_BASE
        ld      a,80            ; Y position
        ld      (hl+),a
        ld      a,80            ; X position
        ld      (hl+),a
        ld      a,0             ; Tile number
        ld      (hl+),a
        ld      a,%00000000     ; Attributes (palette 0, no flip)
        ld      (hl),a

        ; Turn on LCD with sprites and background (like GB!)
        ld      a,%10010011     ; LCD on, BG on, Sprites on
        ld      (LCD_CTRL),a

MAIN_LOOP:
        ; Wait for VBlank
        call    WaitVBlank

        ; Read buttons (like GB!)
        ld      a,$20           ; Select D-pad
        ld      (BUTTONS),a
        ld      a,(BUTTONS)
        cpl                     ; Invert (pressed = 0)
        and     $0F
        ld      b,a             ; Save D-pad state

        ; Check right
        bit     0,b
        jr      z,.check_left
        ; Move sprite right
        ld      hl,OAM_BASE+1   ; X position
        ld      a,(hl)
        inc     a
        cp      160
        jr      c,.update_x
        xor     a               ; Wrap
.update_x:
        ld      (hl),a

.check_left:
        bit     1,b
        jr      z,.check_down
        ; Move sprite left
        ld      hl,OAM_BASE+1
        ld      a,(hl)
        dec     a
        jr      nc,.update_x2
        ld      a,159           ; Wrap
.update_x2:
        ld      (hl),a

.check_down:
        bit     3,b
        jr      z,.check_up
        ; Move sprite down
        ld      hl,OAM_BASE     ; Y position
        ld      a,(hl)
        inc     a
        cp      144
        jr      c,.update_y
        xor     a
.update_y:
        ld      (hl),a

.check_up:
        bit     2,b
        jr      z,.check_buttons
        ; Move sprite up
        ld      hl,OAM_BASE
        ld      a,(hl)
        dec     a
        jr      nc,.update_y2
        ld      a,143
.update_y2:
        ld      (hl),a

.check_buttons:
        ; Check A/B buttons
        ld      a,$10           ; Select buttons
        ld      (BUTTONS),a
        ld      a,(BUTTONS)
        cpl
        and     $0F
        ld      c,a

        bit     0,c             ; A button?
        jr      z,.no_sound
        ; Play beep
        call    PlayBeep

.no_sound:
        jr      MAIN_LOOP

; Wait for VBlank (like GB!)
WaitVBlank:
        ld      a,(LY)
        cp      144             ; VBlank starts at line 144
        jr      c,WaitVBlank
        ret

; Memory copy routine
; HL = source, DE = dest, BC = length
MemCopy:
        ld      a,(hl+)
        ld      (de),a
        inc     de
        dec     bc
        ld      a,b
        or      c
        jr      nz,MemCopy
        ret

; Play beep (simple tone on channel 1)
PlayBeep:
        ld      a,$80
        ld      (SOUND_CH1),a
        ld      a,$F0
        ld      (SOUND_CH1+1),a
        ret

; Tile data (8×8 sprite, 2 bits per pixel)
TILE_DATA:
        .db     $3C,$3C,$7E,$7E,$FF,$FF,$FF,$FF
        .db     $FF,$FF,$7E,$7E,$3C,$3C,$00,$00
```

**Key teaching moment:** Mega Duck is Game Boy CLONE with SAME resolution (160×144)! Z80-like CPU similar to GB's Sharp LR35902. 4 shades grayscale (like GB). Hardware sprites and tiles (GB-like!). 4-channel PSG audio (GB-style!). D-pad + A/B (GB controls). Incompatible cartridges (different pinout, legal distinction!). $40-50 price (cheaper than GB!). ~50 games (many GB ports). Sold in Europe/South America. Also called Cougar Boy (Brazil). Knowledge transfers directly to Game Boy development!

**Tier progression:**
1. Z80 basics (accumulator, registers, flags)
2. 160×144 LCD (same as GB!)
3. 4-shade grayscale (palette programming)
4. VRAM tiles (8×8 character data)
5. Hardware sprites (OAM, like GB!)
6. Background tiles (character-based BG)
7. D-pad input (GB-style button reading)
8. A/B button input (action buttons)
9. 4-channel PSG (GB-style audio!)
10. Scrolling (SCX, SCY registers)
11. VBlank timing (like GB!)
12. Collision detection (software)
13. Animation (sprite/tile cycling)
14. Simple games (GB-style!)
15. ROM banking (cartridge memory management)
16. Complete Mega Duck mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced Z80 techniques, GB-like optimization, 4-shade art mastery, audio depth

#### New Patterns:
- **Z80 optimization** - Efficient assembly code
- **GB-like techniques** - Leveraging GB knowledge
- **4-shade art mastery** - Beautiful grayscale graphics
- **Sprite coordination** - Multiple sprites (flickering for >40)
- **Tile art** - Creative 8×8 tile designs
- **Background scrolling** - Smooth scrolling techniques
- **4-channel PSG mastery** - Music and effects
- **Button precision** - Responsive D-pad + A/B
- **VBlank efficiency** - Optimal update timing
- **ROM banking** - Larger games (128KB+ carts)
- **Battery optimization** - Long play sessions (4× AA)
- **GB port adaptation** - Converting GB games

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Understanding Mega Duck variants
**Focus:** Cougar Boy (Brazil) and European variants

#### Phase 3 Enhancement: Regional Variants
- **Mega Duck** (Europe) - Original branding
- **Cougar Boy** (Brazil) - Brazilian market variant
- **Same hardware** - Identical electronics
- **Different packaging** - Regional branding
- **Compatible cartridges** - All Mega Duck games work

**Note:** Mega Duck had no hardware enhancements. Phase 3 focuses on advanced GB-like techniques and understanding the clone market.

**Tier 40 Example - Advanced Sprite Flickering:**
```asm
; Display >40 sprites via flickering (like GB!)

MAX_OBJECTS     = 80            ; Want 80 objects, have 40 sprites
FRAME_COUNT     = $C000

FlickerSprites:
        ; Alternate which 40 objects are visible each frame
        ld      a,(FRAME_COUNT)
        and     $01             ; Even/odd frame?
        jr      nz,show_odd

show_even:
        ; Show objects 0-39
        ld      hl,objects
        ld      de,OAM_BASE
        ld      b,40
.loop_even:
        ; Copy object to OAM (4 bytes per sprite)
        ld      a,(hl+)         ; Y
        ld      (de),a
        inc     de
        ld      a,(hl+)         ; X
        ld      (de),a
        inc     de
        ld      a,(hl+)         ; Tile
        ld      (de),a
        inc     de
        ld      a,(hl+)         ; Attr
        ld      (de),a
        inc     de
        inc     hl              ; Skip to next even object
        inc     hl
        inc     hl
        inc     hl
        dec     b
        jr      nz,.loop_even
        ret

show_odd:
        ; Show objects 40-79
        ; (Similar logic for odd objects)
        ret

objects:        .space  320     ; 80 objects × 4 bytes
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional Z80 programming, GB-like mastery, advanced graphics/audio

#### Advanced Techniques:
- **Z80 mastery** - Cycle-perfect code
- **GB techniques** - Advanced GB-like patterns
- **4-shade showcase** - Beautiful grayscale art
- **Sprite flickering** - Many objects on-screen
- **Tile art mastery** - Complex 8×8 designs
- **Scrolling mastery** - Smooth, parallax scrolling
- **PSG composition** - 4-channel music
- **VBlank optimization** - Maximum updates
- **ROM banking mastery** - Large games (256KB+)
- **Battery excellence** - 40+ hour optimization

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** GB-style games adapted for Mega Duck

#### Genre Specializations:
- **Platformers** - Mario, Sonic-style
- **Puzzle games** - Tetris, Dr. Mario
- **Action games** - Shooters, beat-em-ups
- **RPGs** - Turn-based adventures
- **Sports games** - Soccer, tennis
- **Arcade ports** - Space Invaders, Pac-Man
- **Adventure games** - Zelda-style
- **Racing games** - Top-down racers

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum GB-like performance

#### Limit-Pushing Techniques:
- **Z80 maximum** - Every cycle optimized
- **4-shade showcase** - Best possible grayscale
- **Sprite flickering mastery** - 100+ objects via flicker
- **Tile complexity** - Advanced 8×8 art
- **Scrolling showcase** - Multi-layer parallax
- **PSG depth** - Complex 4-channel compositions
- **VBlank mastery** - Maximum update efficiency
- **ROM showcase** - Large-scale games
- **Battery perfection** - 50+ hours!

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Best possible Mega Duck games (GB-quality!)

#### Commercial Techniques:
- **Commercial quality** - GB-level games
- **Grayscale polish** - Beautiful 4-shade art
- **Sprite excellence** - Smooth animation
- **GB port perfection** - High-quality conversions
- **Audio polish** - Engaging PSG music
- **Portable excellence** - Ideal handheld experience
- **Battery optimization** - Long play sessions
- **Professional polish** - Commercial standards

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development, emulation

#### Modern Development:
- **MAME emulation** - Mega Duck emulation support
- **GB development tools** - GBDK, Rednex GameBoy Development System (adaptable!)
- **Modern Z80 toolchains** - z88dk, modern assemblers
- **Flash cartridges** - Homebrew development (rare!)
- **Community techniques** - Mega Duck preservation
- **GB knowledge transfer** - Using GB skills for Mega Duck
- **Modern tools** - Emulator debugging

## Pattern Library Structure

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **GB-like Patterns (Phase 2)** - 75 Game Boy techniques
3. **Advanced Patterns (Phase 3-4)** - 100 Z80 + GB mastery
4. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
5. **Polish Patterns (Phase 7)** - 75 professional touches
6. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~500 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-8: Mega Duck / Cougar Boy (1993)**
- Z80-like CPU @ 4MHz (similar to GB!)
- 8KB RAM
- 8KB VRAM
- 160×144 LCD (SAME as Game Boy!)
- 4 shades grayscale
- Hardware sprites (8×8 tiles, 40 sprites, like GB!)
- Background tiles (character-based)
- 4-channel PSG audio (GB-style!)
- D-pad + A, B buttons (GB controls!)
- 4× AA batteries (20-40 hours)
- Cartridge slot (incompatible with GB cartridges!)
- $40-50 price (cheaper than GB!)

**Regional Variants (same hardware):**
- Mega Duck (Europe)
- Cougar Boy (Brazil)

**Phase 7-8: Modern Homebrew**
- Flash cartridges (rare, homebrew)
- Modern development tools (MAME, GBDK adaptable)
- Homebrew community (very small)

## Spiral Learning Example: Platformer (GB-Style!)

**Phase 1 (Tier 12):** Simple platformer, player sprite, tiles, jumping. (~120 lines)

**Phase 2 (Tier 28):** Advanced platformer, enemies, scrolling, PSG music. (~300 lines)

**Phase 3 (Tier 36):** Multi-level platformer, sprite flickering. (~400 lines)

**Phase 4 (Tier 44):** Complex platformer, ROM banking, many levels. (~550 lines)

**Phase 5 (Tier 49):** Complete platformer - GB quality! (~700 lines)

**Phase 6 (Tier 53):** Advanced platformer, parallax scrolling. (~850 lines)

**Phase 7 (Tier 57):** Commercial quality platformer. (~1000 lines)

**Phase 8 (Tier 59):** Modern homebrew, flash cart support. (~1000 lines + tooling)

## Key Differences from Other Platforms

1. **Game Boy Clone** - SAME resolution (160×144!)
2. **Z80-like CPU** - Similar to GB's Sharp LR35902
3. **GB-Compatible Controls** - D-pad + A/B
4. **Incompatible Cartridges** - Different pinout (legal distinction!)
5. **$40-50 Price** - Cheaper than Game Boy!
6. **4-Channel PSG** - GB-style audio
7. **~50 Games** - Many GB ports
8. **Europe/South America** - Regional focus
9. **Cougar Boy** - Brazilian variant
10. **GB Knowledge Transfer** - Direct application of GB skills!

## Success Criteria

**By Phase 4, learners can:**
- Write Z80 assembly fluently (GB-compatible skills!)
- Design for 160×144 LCD (same as GB!)
- Create 4-shade grayscale graphics
- Program hardware sprites (GB-style!)
- Use 4-channel PSG audio
- Optimize for battery life
- Implement VBlank timing
- Port/adapt Game Boy games

**By Phase 8, learners can:**
- Develop commercial-quality Mega Duck games
- Master Z80 architecture (transfers to GB, MSX, etc!)
- Work with modern homebrew tools (MAME, GBDK)
- Create GB-quality games
- Contribute to Mega Duck preservation
- Release homebrew cartridges
- Understand clone console market

## Resources Required

**Phase 1-2:**
- MAME emulator (Mega Duck support)
- GBDK (adaptable for Mega Duck!)
- Z80 assembler (z88dk, etc.)
- Text editor
- Mega Duck reference documentation
- Game Boy development guides (very applicable!)

**Phase 7-8:**
- Flash cartridge (rare, homebrew)
- Mega Duck hardware (optional, collector's item!)
- Modern development tools
- Community resources

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study
**Unique Advantage:** Z80 mastery (transfers to GB, MSX, ZX Spectrum!), Game Boy-compatible skills (direct transfer!), understanding clone console market, 160×144 portable game design, 4-shade grayscale art, GB porting techniques, legal clone study (incompatible cartridges), budget handheld development, GB/Mega Duck dual-platform knowledge!
