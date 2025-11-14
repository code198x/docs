# Sega Nomad Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Sega Nomad (1995-1999, US-only) → Portable Genesis/Mega Drive
**Approach:** Game-first, pattern library, portable optimization mastery
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Portable Genesis (1995), plays ALL Genesis cartridges!, 320×224 backlit color LCD (3.25" diagonal), 6× AA batteries (3 hours typical), US-only release ($179 launch), ~1 million units sold, praised for portability of 16-bit library, competed with Game Gear, released late in Genesis lifecycle (1995, after Saturn!), "last hurrah" for Genesis, TV tuner accessory available

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Sega Nomad is a portable Genesis, no BASIC interpreter. Curriculum begins directly with assembly.

**Prerequisite Knowledge:** Genesis/Mega Drive assembly programming (68000, VDP, Z80). This curriculum focuses on NOMAD-SPECIFIC aspects: battery optimization, portable ergonomics, smaller screen adaptation.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** 68000 fundamentals (SAME as Genesis!), battery optimization, 320×224 display adaptation, portable ergonomics
**Professional Autoload:** From lesson 1, all programs professionally load from cartridge

#### Pattern Library Established:
- **68000 patterns** - Motorola 68000 @ 7.67 MHz (SAME as Genesis!)
- **VDP graphics patterns** - SAME as Genesis: 512 colors, 64-80 sprites
- **Battery optimization** - CRITICAL: 6× AA batteries = ~3 hours typical
- **Display adaptation** - 320×224 backlit TFT LCD (3.25" diagonal)
- **Portable ergonomics** - D-pad, A/B/C, Start, portable grip
- **Power management** - Sleep modes, brightness control, auto-shutoff
- **64KB main RAM** - SAME as Genesis
- **64KB VRAM** - SAME as Genesis
- **Z80 + YM2612 + PSG audio** - SAME, but through small speaker (mono)
- **100% compatibility** - ALL Genesis cartridges work!

#### Example Tier 1 Lesson: "Your First Portable Sprite"
```asm
; Sega Nomad Assembly - Lesson 001
; Display sprite with battery-efficient code
; 68000 @ 7.67 MHz (SAME as Genesis!)

; NOTE: Code is IDENTICAL to Genesis!
; Key difference: Optimize for battery life

        .include "genesis.inc"

        .org    $00000000

; Cartridge header (SAME as Genesis)
        dc.l    $00FFFE00       ; Stack pointer
        dc.l    START           ; Entry point
        ; ... (standard Genesis header)

START:  ; Initialize (standard Genesis init)
        move.w  #$2700,sr       ; Disable interrupts
        move.l  #$00FFFE00,sp   ; Set stack

        ; Initialize VDP (SAME as Genesis)
        jsr     VDP_Init

        ; NOMAD SPECIFIC: Check battery level
        jsr     CheckBattery

        ; NOMAD SPECIFIC: Set brightness (user preference)
        move.w  #2,d0           ; Medium brightness (save battery)
        jsr     SetBrightness

        ; Load sprite data (SAME as Genesis)
        lea     SPRITE_DATA,a0
        move.l  #$20000000,d0   ; VRAM address
        jsr     LoadVRAM

        ; Set sprite attributes in SAT
        move.l  #$C0000000,d0   ; SAT address
        move.w  #$0080,VDP_DATA ; Y position (center)
        move.w  #$0108,VDP_DATA ; Size + link
        move.w  #$0000,VDP_DATA ; Tile + flags
        move.w  #$00A0,VDP_DATA ; X position (center)

LOOP:   ; Main loop
        jsr     WaitVSync

        ; NOMAD SPECIFIC: Check for power button
        jsr     CheckPowerButton
        beq     SHUTDOWN

        ; Read joypad (SAME as Genesis)
        jsr     ReadJoypad
        ; ... (move sprite based on input)

        bra     LOOP

SHUTDOWN:
        ; NOMAD SPECIFIC: Graceful shutdown
        jsr     SaveState
        ; Power down
        stop    #$2700

; NOMAD SPECIFIC ROUTINES
CheckBattery:
        ; Check battery voltage
        ; Note: Nomad doesn't have direct battery check in hardware
        ; This would need to track time or use external hardware
        ; Display warning if usage time suggests low battery
        rts

SetBrightness:
        ; Set LCD brightness
        ; d0.w = level (0-3): 0=lowest, 3=highest
        ; Note: Nomad brightness may be hardware dial, not software
        ; This represents optimization patterns
        rts

CheckPowerButton:
        ; Check if power/sleep button pressed
        ; Return: Z flag clear if running, set if shutdown
        ; Nomad has hardware power switch
        moveq   #0,d0           ; Assume running
        rts

SaveState:
        ; Save game state before shutdown
        ; Use cartridge SRAM if available
        rts

; Standard Genesis routines (unchanged)
VDP_Init:
        ; Initialize VDP (SAME as Genesis)
        rts

LoadVRAM:
        ; Load data to VRAM (SAME as Genesis)
        rts

WaitVSync:
        ; Wait for vertical sync (SAME)
        rts

ReadJoypad:
        ; Read controller (SAME)
        rts

SPRITE_DATA:
        ; 8×8 sprite tiles (SAME as Genesis)
        .incbin "sprite.bin"
```

**Key teaching moment:** Nomad uses IDENTICAL hardware to Genesis! 68000, VDP, Z80, YM2612, PSG - all SAME. Games work perfectly! Key differences: (1) Battery optimization critical (3 hours!), (2) Smaller screen (3.25" LCD vs TV), (3) Portable ergonomics. Display is backlit color LCD (320×224). Released LATE (1995, after Saturn launch!) but praised for portable 16-bit gaming.

**Tier progression:**
1. Sprite basics (SAME as Genesis)
2. Background tiles (SAME)
3. Battery optimization (Nomad-specific!)
4. Display adaptation (3.25" LCD vs TV)
5. Controller input (portable ergonomics)
6. Sound optimization (mono speaker vs stereo)
7. Brightness control (if hardware supports)
8. Power management (efficient gameplay loops)
9. Save state patterns (prepare for shutdown)
10. Portable UI design (readable on small screen)
11. Frame rate optimization (maintain 60 FPS while saving battery)
12. Joypad optimization (different form factor)
13. TV tuner accessory (optional, rare)
14. Link cable (6-player support via accessories!)
15. Polish patterns (battery-efficient effects)
16. Complete Nomad-optimized games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced battery optimization, portable-specific UI, cartridge compatibility testing, accessory integration

#### New Patterns:
- **Battery profiling** - Measuring power consumption per feature
- **Portable UI design** - Readable text on 3.25" LCD
- **Power-efficient effects** - Same visual impact, less battery drain
- **Sleep mode integration** - Manual power-off patterns
- **TV tuner patterns** - TV accessory programming (rare)
- **Genesis compatibility** - Testing entire Genesis library (700+ games!)
- **Mono audio optimization** - Mixing stereo to mono effectively
- **Save state systems** - Quick save via cartridge SRAM
- **Link cable multiplayer** - 6-player via accessories
- **Sega CD integration** - Nomad cannot use Sega CD (cart-only)

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - Accessories and compatibility edge cases
**Focus:** TV tuner, link cable multiplayer, battery packs, Genesis compatibility mastery

#### Phase 3 Enhancement: Accessories + Battery Solutions
- **TV tuner accessory** - Watch TV on Nomad (rare)
- **6-player adapter** - Via link cable port
- **Extended battery packs** - Third-party solutions
- **Car adapter** - Play while traveling (eliminates battery concern)
- **Master System converter** - Some Genesis converters work!

**Tier 40 Example - Multi-Player via Link Cable:**
```asm
; Support 6-player adapter via link cable port

DetectMultiTap:
        ; Check for 6-player adapter
        ; (Link cable port used for this)
        move.b  $A10003,d0      ; Version register
        andi.b  #$0F,d0
        cmpi.b  #$00,d0
        beq     .MULTITAP

        ; Standard 1 controller
        move.w  #1,PlayerCount
        rts

.MULTITAP:
        ; 6-player adapter detected
        move.w  #6,PlayerCount
        rts

ReadAllControllers:
        ; Read all connected controllers
        move.w  PlayerCount,d7
        subq.w  #1,d7           ; Count-1 for dbf
        lea     JoyData,a0

.LOOP:  jsr     ReadJoypad
        move.w  d0,(a0)+
        dbf     d7,.LOOP
        rts

PlayerCount:    dc.w    1
JoyData:        ds.w    6       ; Up to 6 controllers
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional portable game design, battery optimization mastery, 100% Genesis compatibility

#### Advanced Techniques:
- **5+ hour battery life** - Extreme optimization techniques
- **Portable game design patterns** - Short sessions, instant pause
- **Genesis catalog mastery** - Testing with entire 700+ game library
- **Mono audio mastery** - Effective stereo→mono mixing
- **Power consumption profiling** - Per-feature battery usage
- **Adaptive gameplay** - Adjust based on remaining battery
- **Save state sophistication** - Multiple quick-save via SRAM
- **Screen adaptation** - Optimal use of 320×224 LCD

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Portable-optimized Genesis games across genres

#### Genre Specializations:
- **Portable action games** - Sonic, Streets of Rage (portable classics!)
- **Puzzle games** - Perfect for portable (Columns, Dr. Robotnik)
- **Fighting games** - Mortal Kombat, Street Fighter II portable
- **Platformers** - Sonic series, Vectorman (portable)
- **RPGs** - Phantasy Star, Shining Force (long sessions, need saves)
- **Sports games** - NBA Jam, FIFA (quick matches)
- **Shoot-em-ups** - Thunder Force, Gunstar Heroes
- **Strategy games** - Shining Force, Herzog Zwei

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum battery efficiency, portable ergonomics mastery

#### Limit-Pushing Techniques:
- **8+ hour battery** - Extreme optimization (if possible!)
- **Perfect Genesis compatibility** - All 700+ cartridges work flawlessly
- **Advanced portable UI** - Optimal readability on 3.25" LCD
- **Mono audio perfection** - Best possible sound from small speaker
- **Instant pause/resume** - <1 second via SRAM save
- **Battery prediction** - Accurate remaining play time
- **Power-efficient effects** - Maximum visual impact, minimum drain
- **Multi-player mastery** - 6-player games via adapter

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial-quality portable games, perfect battery optimization

#### Commercial Techniques:
- **Commercial portable games** - Games optimized for Nomad
- **Battery life showcase** - 5+ hours on single set of batteries
- **Professional portable UI** - Perfect for 3.25" LCD
- **Mono audio polish** - Professional sound mixing
- **Perfect compatibility** - Works with all Genesis cartridges
- **Portable ergonomics** - Comfortable for extended play
- **Save state mastery** - Instant save/resume via SRAM
- **Multi-player polish** - 6-player games work perfectly

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, flash cartridge features

#### Modern Development:
- **Kega Fusion / Gens emulators** - Nomad emulation mode
- **SGDK (Sega Genesis Development Kit)** - Modern toolchain
- **Modern 68000 assemblers** - VASM, AS, cross-platform
- **Flash cartridge development** - Everdrive (works in Nomad!)
- **Modern graphics tools** - Tile/sprite editors
- **Community techniques** - Active Genesis/Nomad homebrew
- **Battery simulation** - Testing battery optimization
- **Cross-platform patterns** - 68000 techniques
- **Preservation** - Documenting Nomad as final Genesis evolution

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns (mostly Genesis)
2. **Portable Patterns (Phase 2)** - 75 battery/ergonomics techniques
3. **Accessory Patterns (Phase 3)** - 50 multi-player/TV Tuner-specific
4. **Optimization Patterns (Phase 4-5)** - 100 battery efficiency techniques
5. **Genre Patterns (Phase 5-6)** - 150 portable-optimized game patterns
6. **Polish Patterns (Phase 7)** - 75 professional portable touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Sega Nomad (1995, US-only)**
- 68000 @ 7.67 MHz (SAME as Genesis!)
- Z80 @ 3.58 MHz (sound co-processor, SAME)
- 64KB main RAM, 64KB VRAM (SAME)
- 320×224 backlit TFT LCD (3.25" diagonal)
- 512 colors on-screen from 512 palette (SAME)
- 64-80 sprites (SAME)
- YM2612 (6-channel FM) + SN76489 PSG (SAME, but mono speaker)
- Controller: D-pad + A + B + C + Start + Mode
- 6× AA batteries (~3 hours typical)
- Link cable port (6-player adapter, TV tuner)
- Stereo headphone jack
- 100% Genesis cartridge compatible (ALL games work!)

**Phase 3+: Accessories**
- TV Tuner (watch analog TV, rare)
- 6-player adapter (via link cable)
- Car adapter (unlimited play)
- Extended battery packs (third-party)
- Master System converter (some work)

**Phase 7-8: Modern Homebrew**
- Flash cartridge (Everdrive, works in Nomad!)
- Modern development tools (Kega Fusion, SGDK)
- Rechargeable battery solutions

## Spiral Learning Example: Sonic (Nomad Perfect!)

**Phase 1 (Tier 1):** Sonic running, battery-efficient code, portable UI. SAME as Genesis code! (~200 lines)

**Phase 2 (Tier 19):** Full Sonic level, optimized for 3-hour battery. (~600 lines)

**Phase 3 (Tier 37):** 6-player multiplayer mode (via adapter), extended battery support. (~900 lines)

**Phase 4 (Tier 45):** Complex Sonic gameplay, 5-hour battery life achieved. (~1200 lines)

**Phase 5 (Tier 50):** Full Sonic game - multiple zones, perfect portable design. (~1800 lines)

**Phase 6 (Tier 54):** Maximum speed, complex patterns, optimal battery efficiency. (~2400 lines)

**Phase 7 (Tier 57):** Commercial quality - Sonic 3 & Knuckles portable, 5+ hour battery. (~3200 lines)

**Phase 8 (Tier 59):** Modern homebrew - flash cart, modern tools. (~3200 lines + tooling)

## Key Differences from Other Platforms

1. **100% Genesis Compatible** - Plays ALL Genesis cartridges perfectly!
2. **Released AFTER Saturn** - 1995 launch (late in Genesis lifecycle!)
3. **Identical Hardware** - Same 68000, VDP, Z80, YM2612, PSG as Genesis
4. **Battery Life Challenge** - 3 hours typical (optimization critical!)
5. **US-Only Release** - Never released in Japan or Europe
6. **3.25" LCD** - Backlit color TFT (good for 1995)
7. **6-Player Support** - Via link cable adapter
8. **TV Tuner Available** - Watch TV on handheld (rare accessory)
9. **Mono Speaker** - Stereo via headphones only
10. **~1 Million Units** - "Last hurrah" for Genesis hardware

## Assessment Strategy

**Formative Assessment:**
- Code challenges at end of each tier (e.g., "Extend battery life by 30 minutes")
- Pattern recognition exercises ("Identify the battery drain source")
- Debugging challenges ("Fix the display on low battery")
- Performance optimization tasks ("Maintain 60 FPS while reducing power")

**Summative Assessment:**
- End of each phase: Complete Nomad-optimized game
- Must demonstrate all patterns learned in that phase
- Rubric covers: code structure, battery efficiency, portable UI design
- Peer review component (code sharing within cohort)

**Phase Milestones:**
- **Phase 1:** Complete working portable game (3-hour battery target)
- **Phase 2:** Game with advanced battery optimization (4-hour target)
- **Phase 3:** Game with 6-player support (if adapter available)
- **Phase 4:** Complex game with 5-hour battery life
- **Phase 5:** Genre-mastery portable game (optimized for handheld)
- **Phase 6:** Technical showcase (maximum battery efficiency)
- **Phase 7:** Commercial-quality portable title
- **Phase 8:** Modern homebrew with flash cart support

## Success Criteria

**By Phase 4, learners can:**
- Write 68000 assembly fluently (SAME as Genesis)
- Optimize for battery life (5+ hours achievable)
- Design portable-friendly UI (readable on 3.25" LCD)
- Mix stereo to mono effectively
- Implement save states via SRAM
- Test across entire Genesis library (700+ games!)
- Use 6-player adapter (if available)

**By Phase 8, learners can:**
- Develop commercial-quality Nomad games
- Achieve maximum battery efficiency (5+ hours)
- Work with modern homebrew tools (Kega Fusion, SGDK, flash carts)
- Contribute to Genesis homebrew community
- Create portable-optimized experiences
- Master 68000 (knowledge transfers to Genesis!)
- Release and distribute homebrew titles

## Resources Required

**Phase 1-2:**
- Kega Fusion or Gens emulator (Nomad mode)
- SGDK or 68000 assembler (VASM, AS)
- Text editor
- Genesis reference documentation (hardware is SAME!)
- Battery profiling tools

**Phase 3+:**
- 6-player adapter documentation
- TV Tuner documentation (for accessory support)

**Phase 7-8:**
- Flash cartridge (Everdrive, works in Nomad!)
- Sega Nomad hardware (optional, collector's item!)
- Modern development tools
- Community resources (Genesis/Nomad homebrew scene)

**All Phases:**
- Version control (Git)
- Bug tracking
- Community engagement

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study (assuming ~3 lessons per week)
**Unique Advantage:** 68000 mastery (transfers to Genesis!), battery optimization expertise, portable game design, 100% Genesis cartridge compatibility, 6-player support, understanding late-lifecycle hardware evolution, portable ergonomics, released after 32-bit transition (historical context)
