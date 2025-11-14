# Turbo Express Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Turbo Express / PC Engine GT (1990-1994) → Portable TurboGrafx-16
**Approach:** Game-first, pattern library, portable optimization mastery
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** Portable TurboGrafx-16 (1990), plays ALL HuCard games!, FIRST full-color backlit handheld (400×270 active matrix TFT!), revolutionary display for 1990, 6× AA batteries (3 hours typical), expensive ($249 launch, same as home console!), 1.5 million units sold, praised for display quality, competed with Game Boy (but color + backlight!), TV tuner accessory available

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Turbo Express is a portable TurboGrafx-16, no BASIC interpreter. Curriculum begins directly with assembly.

**Prerequisite Knowledge:** TurboGrafx-16 assembly programming (HuC6280, VDC, PSG). This curriculum focuses on TURBO EXPRESS-SPECIFIC aspects: battery optimization, portable ergonomics, smaller screen adaptation.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** HuC6280 fundamentals (SAME as TurboGrafx-16!), battery optimization, 400×270 display adaptation, portable ergonomics
**Professional Autoload:** From lesson 1, all programs professionally load from HuCard

#### Pattern Library Established:
- **HuC6280 patterns** - 8-bit CPU @ 7.16 MHz (6502-based, SAME as TurboGrafx-16!)
- **VDC graphics patterns** - SAME as TurboGrafx-16: 482 colors, 64 sprites
- **Battery optimization** - CRITICAL: 6× AA batteries = ~3 hours typical
- **Display adaptation** - 400×270 active matrix TFT (2.6" diagonal)
- **Portable ergonomics** - D-pad, I/II buttons, Run/Select
- **Power management** - Sleep modes, brightness control, auto-shutoff
- **8KB main RAM** - SAME as TurboGrafx-16
- **64KB VRAM** - SAME as TurboGrafx-16
- **PSG audio** - 6-channel (SAME), but through small speaker (mono)
- **100% compatibility** - ALL TurboGrafx-16 HuCard games work!

#### Example Tier 1 Lesson: "Your First Portable Sprite"
```asm
; Turbo Express Assembly - Lesson 001
; Display sprite with battery-efficient code
; HuC6280 @ 7.16 MHz (SAME as TurboGrafx-16!)

; NOTE: Code is IDENTICAL to TurboGrafx-16!
; Key difference: Optimize for battery life

        .include "pce.inc"

        .org    $E000

START:  ; Initialize (standard PCE init)
        sei                     ; Disable interrupts
        cld                     ; Clear decimal mode
        ldx     #$FF
        txs                     ; Set stack

        ; Initialize VDC (SAME as TurboGrafx-16)
        jsr     VDC_Init

        ; TURBO EXPRESS SPECIFIC: Check battery level
        jsr     CheckBattery

        ; TURBO EXPRESS SPECIFIC: Set brightness (user preference)
        lda     #$02            ; Medium brightness (save battery)
        jsr     SetBrightness

        ; Load sprite data (SAME as TurboGrafx-16)
        lda     #$00
        sta     <VDC_MAWR
        lda     #$20
        sta     <VDC_MAWR+1

        ldx     #0
.LOAD:  lda     SPRITE_DATA,x
        sta     VDC_WRITE
        lda     #0
        sta     VDC_WRITE
        inx
        cpx     #64             ; 8×8 sprite = 64 bytes
        bne     .LOAD

        ; Set sprite position
        lda     #200            ; X = 200 (center for 400px width)
        sta     VDC_SATB
        lda     #135            ; Y = 135 (center for 270px height)
        sta     VDC_SATB+1

LOOP:   ; Main loop
        jsr     WaitVSync

        ; TURBO EXPRESS SPECIFIC: Check for power button
        jsr     CheckPowerButton
        bcs     SHUTDOWN

        ; Read joypad (SAME as TurboGrafx-16)
        jsr     ReadJoypad
        ; ... (move sprite based on input)

        bra     LOOP

SHUTDOWN:
        ; TURBO EXPRESS SPECIFIC: Graceful shutdown
        jsr     SaveState
        ; Power down

; TURBO EXPRESS SPECIFIC ROUTINES
CheckBattery:
        ; Check battery voltage
        ; (Hardware-specific I/O)
        ; Return: A = battery level (0-3)
        ; Display warning if low
        rts

SetBrightness:
        ; Set LCD brightness
        ; A = level (0-3): 0=lowest, 3=highest
        ; Lower = better battery life
        sta     $1FE4           ; Turbo Express brightness register
        rts

CheckPowerButton:
        ; Check if power/sleep button pressed
        ; Return: Carry set if shutdown requested
        clc
        rts

SaveState:
        ; Save game state before shutdown
        ; (Use RAM persistence if available)
        rts

; Standard TurboGrafx-16 routines (unchanged)
VDC_Init:
        ; Initialize VDC (SAME as TurboGrafx-16)
        rts

WaitVSync:
        ; Wait for vertical sync (SAME)
        rts

ReadJoypad:
        ; Read controller (SAME)
        rts

SPRITE_DATA:
        ; 8×8 sprite data (SAME as TurboGrafx-16)
        .incbin "sprite.bin"
```

**Key teaching moment:** Turbo Express uses IDENTICAL hardware to TurboGrafx-16! HuC6280, VDC, PSG - all SAME. Games work perfectly! Key differences: (1) Battery optimization critical (3 hours!), (2) Smaller screen (400×270 vs 512×242), (3) Portable ergonomics. Display is REVOLUTIONARY for 1990 - full color, backlit TFT! First handheld with color + backlight (9 years before Game Boy Color!).

**Tier progression:**
1. Sprite basics (SAME as TurboGrafx-16)
2. Background tiles (SAME)
3. Battery optimization (Turbo Express-specific!)
4. Display adaptation (400×270 screen)
5. Controller input (portable ergonomics)
6. Sound optimization (mono speaker vs stereo)
7. Brightness control (battery life)
8. Power management (sleep, auto-shutoff)
9. Save state patterns (prepare for shutdown)
10. Portable UI design (readable on 2.6" screen)
11. Frame rate optimization (maintain 60 FPS while saving battery)
12. Joypad optimization (different form factor)
13. TV tuner accessory (optional)
14. Link cable (multiplayer, rare)
15. Polish patterns (battery-efficient effects)
16. Complete Turbo Express-optimized games

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced battery optimization, portable-specific UI, HuCard compatibility testing, TV tuner integration

#### New Patterns:
- **Battery profiling** - Measuring power consumption per feature
- **Adaptive brightness** - Auto-adjust based on ambient light
- **Portable UI design** - Readable text on 2.6" screen
- **Power-efficient effects** - Same visual impact, less battery drain
- **Sleep mode integration** - Instant sleep/wake
- **TV tuner patterns** - TV accessory programming (watch TV on handheld!)
- **HuCard compatibility** - Testing all TurboGrafx-16 games
- **Mono audio optimization** - Mixing stereo to mono effectively
- **Save state systems** - Quick save before battery dies
- **Link cable multiplayer** - Rare but possible

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - TV Tuner accessory + SuperGrafx compatibility
**Focus:** TV Tuner integration, SuperGrafx game compatibility, battery life maximization

#### Phase 3 Enhancement: TV Tuner + SuperGrafx
- **TV Tuner accessory** - Watch TV on Turbo Express! (analog TV)
- **SuperGrafx games** - Most work, some compatibility issues
- **Extended battery packs** - Third-party solutions
- **Car adapter** - Play while traveling (eliminates battery concern)

**Tier 40 Example - TV Tuner Integration:**
```asm
; Detect and use TV Tuner accessory

DetectTVTuner:
        ; Check for TV Tuner presence
        lda     $1FE8           ; TV Tuner detection register
        and     #$01
        beq     .NO_TUNER

        ; TV Tuner detected
        lda     #1
        sta     TVTunerPresent
        ; Enable TV mode option in menu
        rts

.NO_TUNER:
        ; No TV Tuner
        lda     #0
        sta     TVTunerPresent
        rts

SwitchToTV:
        ; Switch from game to TV mode
        ; (User presses TV button)
        lda     TVTunerPresent
        beq     .NO_TV

        ; Save game state
        jsr     SaveState

        ; Switch to TV input
        lda     #$01
        sta     $1FE8

        ; Display TV controls
        jsr     ShowTVControls

.NO_TV: rts

TVTunerPresent: .db 0
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional portable game design, battery optimization mastery, 100% HuCard compatibility

#### Advanced Techniques:
- **5+ hour battery life** - Extreme optimization techniques
- **Portable game design patterns** - Short sessions, instant sleep/wake
- **HuCard catalog mastery** - Testing with entire TurboGrafx-16 library
- **Mono audio mastery** - Effective stereo→mono mixing
- **Power consumption profiling** - Per-feature battery usage
- **Adaptive gameplay** - Adjust difficulty based on remaining battery
- **Save state sophistication** - Multiple quick-save slots
- **Brightness algorithms** - Auto-adjust for different game scenes

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Portable-optimized games across genres

#### Genre Specializations:
- **Portable action games** - Short bursts, instant suspend
- **Puzzle games** - Perfect for portable (low power, long play)
- **Shoot-em-ups** - Turbo Express strength (arcade-perfect on the go!)
- **Platformers** - Bonk, Adventure Island (portable classics)
- **RPGs** - Long sessions, need save state support
- **Sports games** - Quick matches
- **Card/board games** - Minimal power consumption
- **TV tuner showcases** - Picture-in-picture game + TV

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum battery efficiency, portable ergonomics mastery

#### Limit-Pushing Techniques:
- **10+ hour battery** - Extreme optimization (if possible!)
- **Perfect HuCard compatibility** - All 600+ games work flawlessly
- **Advanced portable UI** - Optimal readability on 2.6" screen
- **Mono audio perfection** - Best possible sound from small speaker
- **Sleep/wake instant** - <1 second resume
- **Battery prediction** - Accurate remaining play time
- **Power-efficient effects** - Maximum visual impact, minimum drain
- **TV tuner mastery** - Perfect game + TV integration

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Commercial-quality portable games, perfect battery optimization

#### Commercial Techniques:
- **Commercial portable games** - Games designed for Turbo Express
- **Battery life showcase** - 5+ hours on single set of batteries
- **Professional portable UI** - Perfect for 2.6" TFT display
- **Mono audio polish** - Professional sound mixing
- **TV tuner integration** - Games that leverage TV accessory
- **Perfect compatibility** - Works with all TurboGrafx-16 HuCards
- **Portable ergonomics** - Comfortable for extended play
- **Save state mastery** - Instant save/resume perfection

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, flash cartridge features

#### Modern Development:
- **Mednafen / Beetle PCE emulators** - Turbo Express emulation
- **Modern HuC6280 toolchains** - PCEAS, HuC compiler
- **Flash HuCard development** - Everdrives
- **Modern graphics tools** - Tile/sprite editors
- **Community techniques** - Active PCE/Turbo Express homebrew
- **Battery simulation** - Testing battery optimization in emulators
- **Cross-platform patterns** - HuC6280 techniques
- **Preservation** - Documenting Turbo Express's revolutionary display

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns (mostly TurboGrafx-16)
2. **Portable Patterns (Phase 2)** - 75 battery/ergonomics techniques
3. **Accessory Patterns (Phase 3)** - 50 TV Tuner-specific
4. **Optimization Patterns (Phase 4-5)** - 100 battery efficiency techniques
5. **Genre Patterns (Phase 5-6)** - 150 portable-optimized game patterns
6. **Polish Patterns (Phase 7)** - 75 professional portable touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Turbo Express / PC Engine GT (1990)**
- HuC6280 @ 7.16 MHz (SAME as TurboGrafx-16!)
- 8KB main RAM, 64KB VRAM (SAME)
- 400×270 active matrix TFT (2.6" diagonal, 66mm)
- 482 colors on-screen from 512 palette (SAME)
- 64 sprites, 16×16 or 16×32 (SAME)
- PSG: 6-channel (SAME, but mono speaker)
- Controller: D-pad + I + II + Run + Select
- 6× AA batteries (~3 hours typical)
- TV tuner accessory (optional)
- Stereo headphone jack
- 100% HuCard compatible (ALL TurboGrafx-16 games!)

**Phase 3+: Accessories**
- TV Tuner (watch analog TV!)
- Car adapter (unlimited play)
- Extended battery packs (third-party)
- Link cable (multiplayer, rare)

**Phase 7-8: Modern Homebrew**
- Flash HuCard (Everdrive)
- Modern development tools (Mednafen, PCEAS)
- Rechargeable battery solutions

## Spiral Learning Example: Shoot-em-up (Turbo Express Strength!)

**Phase 1 (Tier 1):** Simple shmup, battery-efficient code, portable UI. SAME as TurboGrafx-16 code! (~150 lines)

**Phase 2 (Tier 19):** Advanced shmup, power-ups, boss, optimized for 3-hour battery. (~400 lines)

**Phase 3 (Tier 37):** TV tuner integration (watch TV between levels!), extended battery support. (~600 lines)

**Phase 4 (Tier 45):** Complex shmup, many enemies, 5-hour battery life achieved. (~900 lines)

**Phase 5 (Tier 50):** Full shmup - multiple stages, varied enemies, perfect portable design. (~1300 lines)

**Phase 6 (Tier 54):** Maximum enemies, complex patterns, optimal battery efficiency. (~1700 lines)

**Phase 7 (Tier 57):** Commercial quality - arcade-perfect on portable, 5+ hour battery. (~2200 lines)

**Phase 8 (Tier 59):** Modern homebrew - flash HuCard, modern tools. (~2200 lines + tooling)

## Key Differences from Other Platforms

1. **100% TurboGrafx-16 Compatible** - Plays ALL HuCard games perfectly!
2. **First Color Backlit Handheld** - Revolutionary 400×270 TFT display (1990!)
3. **Identical Hardware** - Same HuC6280, VDC, PSG as home console
4. **Battery Life Challenge** - 3 hours typical (optimization critical!)
5. **TV Tuner Accessory** - Watch analog TV on handheld (unique!)
6. **Active Matrix TFT** - Superior to Game Boy's passive LCD
7. **Expensive** - $249 launch (same as home console!)
8. **Portable Ergonomics** - Smaller screen adaptation required
9. **Mono Speaker** - Stereo via headphones only
10. **1.5 Million Units** - Successful for such an expensive portable

## Assessment Strategy

**Formative Assessment:**
- Code challenges at end of each tier (e.g., "Extend battery life by 30 minutes")
- Pattern recognition exercises ("Identify the battery drain source")
- Debugging challenges ("Fix the display flicker on low battery")
- Performance optimization tasks ("Maintain 60 FPS while reducing power")

**Summative Assessment:**
- End of each phase: Complete Turbo Express-optimized game
- Must demonstrate all patterns learned in that phase
- Rubric covers: code structure, battery efficiency, portable UI design
- Peer review component (code sharing within cohort)

**Phase Milestones:**
- **Phase 1:** Complete working portable game (3-hour battery target)
- **Phase 2:** Game with advanced battery optimization (4-hour target)
- **Phase 3:** Game with TV Tuner support (if available)
- **Phase 4:** Complex game with 5-hour battery life
- **Phase 5:** Genre-mastery portable game (optimized for handheld play)
- **Phase 6:** Technical showcase (maximum battery efficiency)
- **Phase 7:** Commercial-quality portable title
- **Phase 8:** Modern homebrew with flash HuCard support

## Success Criteria

**By Phase 4, learners can:**
- Write HuC6280 assembly fluently (SAME as TurboGrafx-16)
- Optimize for battery life (5+ hours achievable)
- Design portable-friendly UI (readable on 2.6" screen)
- Mix stereo to mono effectively
- Implement sleep/wake states
- Test across entire HuCard library
- Use TV Tuner accessory (if available)

**By Phase 8, learners can:**
- Develop commercial-quality Turbo Express games
- Achieve maximum battery efficiency (5+ hours)
- Work with modern homebrew tools (Mednafen, flash HuCards)
- Contribute to TurboGrafx-16/PCE homebrew community
- Create portable-optimized experiences
- Master HuC6280 (knowledge transfers to TurboGrafx-16!)
- Release and distribute homebrew titles

## Resources Required

**Phase 1-2:**
- Mednafen or Beetle PCE emulator (Turbo Express mode)
- PCEAS assembler or HuC compiler
- Text editor
- TurboGrafx-16 reference documentation (hardware is SAME!)
- Battery profiling tools (emulator or hardware)

**Phase 3+:**
- TV Tuner documentation (for accessory support)
- SuperGrafx compatibility testing

**Phase 7-8:**
- Flash HuCard (TurboEverdrive, etc.)
- Turbo Express hardware (optional, rare/expensive collector's item!)
- Modern development tools
- Community resources (PCE homebrew scene)

**All Phases:**
- Version control (Git)
- Bug tracking
- Community engagement

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study (assuming ~3 lessons per week)
**Unique Advantage:** HuC6280 mastery (transfers to TurboGrafx-16!), battery optimization expertise, portable game design, first color backlit handheld display, 100% HuCard compatibility, TV Tuner integration, understanding revolutionary 1990 technology, portable ergonomics
