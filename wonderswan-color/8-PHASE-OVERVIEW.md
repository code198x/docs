# WonderSwan Color Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** WonderSwan (1999, mono) → WonderSwan Color (2000) → SwanCrystal (2002) → Modern homebrew
**Approach:** Game-first, pattern library, x86 handheld mastery, dual-orientation design
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Designed by Gunpei Yokoi (Game Boy creator, his final project before death!), Bandai handheld (Japan-only, 1999-2003), NEC V30 CPU (x86 compatible! 16-bit!), ~3.5 million units sold, competed with Game Boy Color, extremely low power (single AA battery for 40 hours!), unique dual-orientation (vertical/horizontal), backward compatible across all models, strong RPG library (Squaresoft support!)

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** WonderSwan shipped without built-in BASIC. Curriculum begins directly with assembly, focused on x86 architecture and handheld optimization.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** V30 (x86) fundamentals, dual-orientation design, tile graphics, power management, 16KB RAM
**Professional Autoload:** From lesson 1, all programs professionally load from ROM

#### Pattern Library Established:
- **V30 CPU patterns** - NEC V30 @ 3.072 MHz (x86 compatible! 16-bit 8086 derivative)
- **x86 architecture** - Registers (AX, BX, CX, DX, SI, DI, BP, SP), segments (CS, DS, ES, SS)
- **Dual-orientation** - Vertical (224×144) or Horizontal (144×224) display
- **Tile graphics** - Background: 32×32 tiles, Sprites: 128 hardware sprites
- **Color palette** - WonderSwan Color: 4096 colors (12-bit RGB), 241 colors on-screen
- **Power management** - CRITICAL: Single AA battery (30-40 hours!), sleep modes
- **16KB RAM** - 64KB on WonderSwan Color (4× base!)
- **Sound** - 4-channel PCM (8-bit samples)
- **12-button control** - X1-X4 (top), Y1-Y4 (side), A, B, Start
- **Backward compatibility** - Color games work on mono WonderSwan (graceful degradation)

#### Example Tier 1 Lesson: "Your First Sprite (x86!)"
```asm
; WonderSwan Color Assembly - Lesson 001
; Display and move sprite using V30 (x86)
; NEC V30 @ 3.072 MHz

        .186                    ; V30 is 80186-compatible
        .MODEL  TINY            ; WonderSwan memory model

        .CODE
        ORG     $0000

START:  ; Initialize WonderSwan hardware
        cli                     ; Disable interrupts
        mov     ax,cs
        mov     ds,ax           ; DS = CS
        mov     es,ax           ; ES = CS
        mov     ss,ax           ; SS = CS
        mov     sp,2000h        ; Set stack

        ; Set display mode (vertical orientation, color)
        mov     al,80h          ; Color mode
        out     60h,al          ; Display control register

        ; Load sprite palette (16 colors for sprite 0)
        mov     si,OFFSET SPRITE_PALETTE
        mov     di,0FE00h       ; Sprite palette RAM
        mov     cx,16           ; 16 colors
        rep movsw               ; Copy palette

        ; Load sprite pattern (8×8 ball)
        mov     si,OFFSET SPRITE_DATA
        mov     di,2000h        ; Sprite pattern RAM
        mov     cx,8            ; 8 bytes (8×8, 1 byte per row)
        rep movsb

        ; Set sprite attributes
        mov     di,0800h        ; Sprite attribute RAM
        mov     ax,100          ; X position (center)
        stosw
        mov     ax,72           ; Y position (center)
        stosw
        mov     al,0            ; Sprite pattern #0
        stosb
        mov     al,0            ; Sprite palette #0
        stosb

MAIN_LOOP:
        ; Wait for vertical blank
        call    WAIT_VBL

        ; Read controller input
        in      al,0B5h         ; Read X buttons
        test    al,01h          ; X1 (right)
        jz      CHECK_LEFT
        mov     di,0800h        ; Sprite X address
        mov     ax,[di]
        inc     ax              ; Move right
        cmp     ax,224-8        ; Check boundary
        jl      UPDATE_X
        xor     ax,ax           ; Wrap to left
UPDATE_X:
        mov     [di],ax

CHECK_LEFT:
        in      al,0B5h
        test    al,02h          ; X2 (left)
        jz      MAIN_LOOP
        mov     di,0800h
        mov     ax,[di]
        dec     ax              ; Move left
        jns     UPDATE_X2
        mov     ax,224-8        ; Wrap to right
UPDATE_X2:
        mov     [di],ax

        jmp     MAIN_LOOP

WAIT_VBL:
        ; Wait for vertical blank interrupt
        in      al,0A4h         ; Read interrupt status
        test    al,40h          ; VBL flag
        jz      WAIT_VBL
        ret

SPRITE_PALETTE:
        ; 16-bit RGB444 colors (WonderSwan Color)
        dw      0000h           ; Transparent
        dw      0FFFh           ; White
        dw      0F00h           ; Red
        dw      00F0h           ; Green
        dw      000Fh           ; Blue
        dw      0FF0h           ; Yellow
        dw      0F0Fh           ; Magenta
        dw      00FFh           ; Cyan
        dw      0888h           ; Gray
        dw      0444h           ; Dark gray
        dw      0F80h           ; Orange
        dw      08F0h           ; Lime
        dw      080Fh           ; Purple
        dw      0088h           ; Dark blue
        dw      0800h           ; Dark red
        dw      0080h           ; Dark green

SPRITE_DATA:
        ; 8×8 ball sprite (1 bpp, palette applies colors)
        db      00111100b       ; ░░████░░
        db      01111110b       ; ░██████░
        db      11111111b       ; ████████
        db      11111111b       ; ████████
        db      11111111b       ; ████████
        db      11111111b       ; ████████
        db      01111110b       ; ░██████░
        db      00111100b       ; ░░████░░

        END     START
```

**Key teaching moment:** WonderSwan uses V30 CPU - this is x86 compatible! (8086 derivative). x86 architecture (AX/BX/CX/DX registers, segments). DUAL ORIENTATION (vertical 224×144 OR horizontal 144×224). 4096 colors (12-bit RGB). EXTREME power efficiency (single AA for 40 hours!). Designed by Gunpei Yokoi (Game Boy creator!). Japan-only but very successful (3.5M units). 128 hardware sprites, tile-based graphics.

**Tier progression:**
1. Sprite basics (128 sprites, 8×8 tiles)
2. Tile backgrounds (32×32 grid, scrolling)
3. Dual-orientation support (vertical/horizontal)
4. Color palettes (4096 colors, 241 on-screen)
5. Controller input (X1-X4, Y1-Y4, A, B, Start - 12 buttons!)
6. Sound basics (4-channel PCM samples)
7. Power management (sleep modes, battery optimization)
8. Backward compatibility (Color → Mono graceful degradation)
9. x86 optimization (V30 is 16-bit!)
10. RAM management (16KB base, 64KB Color)
11. Score display (tile-based text)
12. Animation patterns (sprite frame cycling)
13. Collision detection (hardware overlap detection)
14. Game state machines
15. Polish patterns (smooth 60 FPS on AA battery!)
16. Complete WonderSwan mini-games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced tile techniques, dual-orientation mastery, x86 optimization, power optimization, RPG patterns (WonderSwan strength!)

#### New Patterns:
- **Advanced tile graphics** - Multi-layer scrolling, parallax
- **Dual-orientation mastery** - Games playable both ways (unique!)
- **x86 optimization** - 16-bit x86 code optimization
- **Power optimization mastery** - Maximum battery life (40+ hours!)
- **RPG patterns** - WonderSwan known for RPGs (Final Fantasy, SaGa!)
- **Save data** - Internal SRAM or EEPROM (256 bytes-64KB)
- **Hardware scrolling** - Smooth tile scrolling
- **Sprite multiplexing** - >128 visible sprites via flickering
- **4-channel audio** - Complex PCM music
- **Compression** - Critical for 1-4MB ROM cartridges
- **Color + mono compatibility** - One ROM, two modes

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - WonderSwan Color (2000) + SwanCrystal (2002)
**Focus:** Color graphics, SwanCrystal TFT screen, 64KB RAM, enhanced features

#### Phase 3 Enhancement: WonderSwan Color + SwanCrystal
- **WonderSwan Color** (2000):
  - 4096 colors (12-bit RGB: 4-4-4)
  - 241 colors on-screen simultaneously
  - 64KB RAM (4× base WonderSwan!)
  - Backward compatible with mono WonderSwan
  - Same battery life (40 hours!)

- **SwanCrystal** (2002):
  - TFT screen (vs STN in WSC)
  - Better viewing angles, contrast
  - Same capabilities as WSC
  - Final WonderSwan model
  - Backward compatible

**Tier 40 Example - Color Detection and Adaptation:**
```asm
; Detect WonderSwan (mono) vs Color/Crystal and adapt

DetectColor:
        ; Check hardware version
        in      al,60h          ; Display control
        test    al,80h          ; Color bit
        jz      MONO_MODE

COLOR_MODE:
        ; WonderSwan Color/Crystal detected
        mov     byte ptr [ColorMode],1

        ; Enable color graphics
        mov     al,80h
        out     60h,al

        ; Load color palettes
        mov     si,OFFSET COLOR_PALETTES
        mov     di,0FE00h       ; Palette RAM
        mov     cx,256          ; 256 colors
        rep movsw

        ret

MONO_MODE:
        ; Original WonderSwan (mono) detected
        mov     byte ptr [ColorMode],0

        ; Use grayscale graphics
        mov     al,00h
        out     60h,al

        ; Load mono palettes (4 shades)
        mov     si,OFFSET MONO_PALETTES
        mov     di,0FE00h
        mov     cx,16           ; 16 grayscale entries
        rep movsw

        ret

ColorMode:      db      0
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional game architecture, x86 mastery, complex RPGs, dual-orientation design, power optimization

#### Advanced Techniques:
- **x86 assembly mastery** - Efficient 16-bit code
- **RPG engines** - Turn-based, menu systems (WonderSwan strength!)
- **Dual-orientation design** - Full support for both orientations
- **Power mastery** - 50+ hour battery life
- **Save systems** - SRAM/EEPROM for progress
- **Compression engines** - LZ variants for ROM space
- **Tile streaming** - Large worlds in limited ROM/RAM
- **Menu systems** - Complex RPG menus (WonderSwan has many buttons!)
- **4-channel music** - Complex compositions
- **Portrait/landscape UI** - Different UI layouts per orientation

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** RPGs (WonderSwan strength!), puzzle games, action games, dual-orientation showcases

#### Genre Specializations:
- **RPGs** - Final Fantasy, SaGa, Riviera (WonderSwan's killer apps!)
- **Puzzle games** - Gunpey (designed by Gunpei Yokoi!), Puzzle Bobble
- **Action games** - Mega Man, Rockman EXE
- **Fighting games** - Guilty Gear Petit (dual-orientation!)
- **Visual novels** - Text-heavy games (Japanese market)
- **Strategy games** - Turn-based tactics
- **Platformers** - Klonoa series
- **Sports games** - Baseball, soccer (compact designs)

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum color usage, complex RPGs, dual-orientation mastery, power efficiency

#### Limit-Pushing Techniques:
- **241 colors on-screen** - Maximum palette usage
- **128 sprite maximum** - Complex sprite multiplexing
- **Large RPG worlds** - Streaming from ROM
- **Dual-orientation showcase** - Perfect experience both ways
- **64KB RAM mastery** - Efficient use of Color's expanded RAM
- **Complex tile effects** - Multi-layer parallax, scrolling
- **Advanced audio** - 4-channel PCM music + sound effects
- **50+ hour battery** - Extreme power optimization

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial-quality RPGs, professional dual-orientation, showcase titles

#### Commercial Techniques:
- **Commercial RPGs** - Final Fantasy, SaGa quality
- **Gunpey** - Gunpei Yokoi's final game (puzzle masterpiece!)
- **Professional graphics** - Detailed tile art, smooth sprites
- **Complex music** - 4-channel compositions with PCM quality
- **Dual-orientation polish** - Perfect in both modes
- **Save systems** - Complex RPG progress tracking
- **Attract modes** - Demo playback, story teasers
- **Squaresoft quality** - Final Fantasy I, II, IV (WonderSwan remakes!)

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, flash cartridge features

#### Modern Development:
- **Mednafen / ares emulators** - WonderSwan emulation, debugging
- **Modern x86 assemblers** - NASM, YASM, FASM (x86 compatible!)
- **WonderSwan dev tools** - Modern toolchains
- **Flash cartridge development** - Benesse Pocket Challenge V2, flash carts
- **Modern graphics tools** - Tile editors, sprite tools
- **Community techniques** - Active WonderSwan homebrew scene (Japan + international)
- **Cross-platform x86** - x86 knowledge transfers to DOS, PC
- **Modern compression** - Better tools for ROM space

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 complex techniques
3. **Color/Crystal Patterns (Phase 3)** - 50 enhancement-specific
4. **Optimization Patterns (Phase 4-5)** - 100 x86 + power techniques
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns (RPG focus!)
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: WonderSwan (1999, Mono)**
- NEC V30 @ 3.072 MHz (x86 compatible, 16-bit!)
- 16KB RAM
- 224×144 pixels (STN LCD, 4 shades of gray)
- Dual-orientation (vertical 224×144 OR horizontal 144×224)
- 128 hardware sprites (8×8 tiles)
- 32×32 tile background (scrolling)
- 4-channel PCM audio (8-bit samples)
- 12-button controller (X1-X4, Y1-Y4, A, B, Start)
- Save RAM (256 bytes-64KB SRAM or EEPROM)
- Single AA battery (30-40 hours!)
- 1-4MB ROM cartridges

**Phase 3+: WonderSwan Color (2000) + SwanCrystal (2002)**
- All WonderSwan features
- +4096 colors (12-bit RGB: 4-4-4)
- +241 colors on-screen simultaneously
- +64KB RAM (4× base WonderSwan!)
- +SwanCrystal: TFT screen (better viewing)
- Backward compatible with mono WonderSwan
- Same battery life (40 hours!)

**Phase 7-8: Modern Homebrew**
- Flash cartridges (multi-game, save states)
- Modern development tools (Mednafen, ares, NASM)
- Modern graphics/audio tools

## Spiral Learning Example: RPG (WonderSwan's Strength!)

**Phase 1 (Tier 11):** Character sprite, tile map, movement (4 directions), simple menu. (~150 lines x86 assembly)

**Phase 2 (Tier 27):** Multiple maps, NPCs, dialogue system, save data (SRAM). (~500 lines)

**Phase 3 (Tier 39):** Color graphics (Color/Crystal), mono fallback, enhanced UI. (~800 lines)

**Phase 4 (Tier 47):** Battle system, inventory, equipment, status effects. (~1400 lines)

**Phase 5 (Tier 50):** Full RPG - world map, towns, dungeons, story. (~2200 lines)

**Phase 6 (Tier 54):** Large RPG world, complex battle system, dual-orientation UI. (~3000 lines)

**Phase 7 (Tier 57):** Final Fantasy I/II quality - professional RPG, complete story. (~4500 lines)

**Phase 8 (Tier 59):** Modern homebrew - expanded content, modern tools, flash cart. (~4500 lines + tooling)

## Key Differences from Other Platforms

1. **x86 Architecture!** - NEC V30 is x86 compatible (8086 derivative) - UNIQUE for handheld!
2. **Gunpei Yokoi's Final Project** - Designed by Game Boy creator before his death
3. **Dual-Orientation** - Vertical (224×144) OR horizontal (144×224) - unique design!
4. **Extreme Battery Life** - Single AA battery for 40 hours (best of era!)
5. **12-Button Controller** - X1-X4 + Y1-Y4 + A + B + Start (many games!)
6. **Japan-Only** - Never released in US/Europe (3.5M units in Japan)
7. **RPG Focus** - Strong Squaresoft support (Final Fantasy remakes!)
8. **Backward Compatible** - Color games work on mono WonderSwan
9. **4096 Colors** - WonderSwan Color (12-bit RGB, 241 on-screen)
10. **V30 @ 3MHz** - 16-bit x86 (faster than Game Boy's 8-bit)

## Assessment Strategy

**Formative Assessment:**
- Code challenges at end of each tier (e.g., "Add dual-orientation support")
- Pattern recognition exercises ("Identify the x86 optimization")
- Debugging challenges ("Fix the battery drain issue")
- Performance optimization tasks ("Extend battery life by 10%")

**Summative Assessment:**
- End of each phase: Complete WonderSwan game from scratch
- Must demonstrate all patterns learned in that phase
- Rubric covers: code structure, dual-orientation support, battery efficiency
- Peer review component (code sharing within cohort)

**Phase Milestones:**
- **Phase 1:** Complete working WonderSwan game (mono)
- **Phase 2:** Game with dual-orientation, advanced graphics
- **Phase 3:** Color game with mono fallback (backward compatible)
- **Phase 4:** Complex game (RPG preferred, WonderSwan strength!)
- **Phase 5:** Genre-mastery project (RPG/puzzle/action/fighting)
- **Phase 6:** Technical showcase (241 colors, dual-orientation perfect)
- **Phase 7:** Commercial-quality game (Final Fantasy-level RPG)
- **Phase 8:** Modern homebrew with community release

## Success Criteria

**By Phase 4, learners can:**
- Write x86 assembly fluently (V30 16-bit)
- Master dual-orientation design (vertical/horizontal)
- Program tile graphics (128 sprites, 32×32 background)
- Implement 4096-color graphics (WonderSwan Color)
- Optimize for battery life (40+ hours on AA!)
- Create save systems (SRAM/EEPROM)
- Design RPGs (WonderSwan's strength!)

**By Phase 8, learners can:**
- Develop commercial-quality WonderSwan games
- Master x86 optimization (transfers to DOS/PC!)
- Create perfect dual-orientation experiences
- Work with modern homebrew tools (Mednafen, ares)
- Contribute to WonderSwan homebrew community
- Design battery-efficient games (50+ hour goal!)
- Release and distribute homebrew titles

## Resources Required

**Phase 1-2:**
- Mednafen or ares emulator (WonderSwan support, free)
- NASM, YASM, or FASM (x86 assemblers)
- Text editor
- WonderSwan reference documentation (V30, graphics, sound)

**Phase 3+:**
- WonderSwan Color / SwanCrystal emulation

**Phase 7-8:**
- Flash cartridge (optional, for real hardware)
- WonderSwan Color / SwanCrystal (optional, collector's item!)
- Modern graphics tools (tile editors, sprite tools)
- Community resources (Japanese homebrew scene, international forums)

**All Phases:**
- Version control (Git)
- Bug tracking
- Community engagement (preservation efforts)

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study (assuming ~3 lessons per week)
**Unique Advantage:** x86 assembly mastery (unique for handheld! transfers to DOS/PC!), dual-orientation design expertise, extreme power optimization (40+ hours!), RPG development skills, Gunpei Yokoi design philosophy, understanding Japanese gaming market, 16-bit handheld programming
