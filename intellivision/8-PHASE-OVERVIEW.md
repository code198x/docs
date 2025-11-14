# Intellivision Assembly: Complete 8-Phase Curriculum Overview

**Total:** 60 tiers = 4,096 lessons across 8 phases
**Pedagogy:** Spiral learning through ~25-30 games revisited at increasing complexity
**Hardware:** Intellivision (base, 1979) → Intellivision II (1983) → Modern (ECS expansion)
**Approach:** Game-first, pattern library, genre technique mastery
**Gateway:** Direct to assembly (no BASIC interpreter)
**Historical Note:** First 16-bit home console (1979), revolutionary controller with numeric keypad + disc + action buttons, 3 million units sold, competed with Atari 2600, known for sports games and advanced AI

## 8-Phase Structure

### Phase 0: N/A
**No BASIC gateway.** Intellivision shipped without a built-in programming language (though Keyboard Component with BASIC was planned but cancelled). The curriculum begins directly with assembly.

### Phase 1: Foundation (Tiers 1-16, 256 lessons)
**Spiral:** First exposure to all ~25-30 games
**Focus:** CP1610 fundamentals, STIC graphics chip, PSG sound, controller input, 1456 bytes RAM constraint mastery
**Professional Autoload:** From lesson 1, all programs professionally load from ROM

#### Pattern Library Established:
- **CP1610 CPU patterns** - 16-bit General Instrument architecture (unusual instruction set: no flags register, SDBD prefix for 16-bit immediate data)
- **STIC video patterns** - Sprite Multiplexed Object Graphics (MOBs): 8 hardware sprites, 20×12 background cards
- **PSG sound patterns** - General Instrument AY-3-8914 (3 channels, noise, envelope)
- **Controller patterns** - 16-direction disc + 12-button keypad + 4 side action buttons (revolutionary for 1979!)
- **Extreme RAM constraint patterns** - 1456 bytes total RAM (240 bytes system + 1216 bytes available)
- **ROM banking patterns** - 8KB segments (games typically 4KB-16KB)
- **Background card patterns** - 20×12 playfield (160×96 resolution equivalent), 16 colors
- **Collision detection patterns** - Hardware sprite collision detection (STIC provides flags)
- **Memory-mapped I/O** - All hardware at $0000-$01FF (256 words)
- **16-bit word addressing** - All addresses are 16-bit words (not bytes!)

#### Example Tier 1 Lesson: "Your First Sprite"
```asm
; Intellivision Assembly - Lesson 001
; Display bouncing ball sprite (MOB 0)
; CP1610 @ 894.886 kHz (1.79 MHz / 2)

        ORG     $5000

INIT:   MVII    #$0080,R0       ; X position (center)
        MVO     R0,MOBX         ; Set MOB 0 X
        MVII    #$0050,R0       ; Y position
        MVO     R0,MOBY         ; Set MOB 0 Y
        MVII    #$0800,R0       ; Card #8 (ball graphic)
        MVO     R0,MOBA         ; Set MOB 0 attribute
        MVII    #$0007,R0       ; White color
        MVO     R0,MOBC         ; Set MOB 0 color

LOOP:   MVI     MOBX,R0         ; Read current X
        ADDI    #1,R0           ; Move right
        CMPI    #$00A0,R0       ; At edge?
        BLE     CONT            ; No, continue
        MVII    #$0020,R0       ; Yes, wrap to left
CONT:   MVO     R0,MOBX         ; Update position

        CALL    WAITVB          ; Wait for vertical blank
        B       LOOP            ; Repeat

; Memory-mapped hardware addresses
MOBX    EQU     $0000           ; MOB 0 X position
MOBY    EQU     $0001           ; MOB 0 Y position
MOBA    EQU     $0002           ; MOB 0 attribute (card #)
MOBC    EQU     $0003           ; MOB 0 color
WAITVB  EQU     $1014           ; System routine
```

**Key teaching moment:** CP1610 has NO FLAGS REGISTER! Comparison sets result in register. Also, all addresses are 16-bit WORDS (unusual for the era). Notice SDBD prefix for 16-bit immediate data.

**Tier progression:**
1. Single sprite basics (MOB display, color, position)
2. Multiple sprites (8 MOBs management)
3. Background cards (20×12 playfield, GRAM/GROM)
4. Controller input (disc + keypad + action buttons)
5. Sound basics (PSG 3-channel)
6. Collision detection (hardware flags)
7. RAM conservation (1456 bytes total!)
8. Simple AI (sports game opponents)
9. Score display (GRAM custom fonts)
10. Title screens (GRAM animation)
11. Game state machines
12. Difficulty progression
13. Multi-level structures
14. Save-state patterns (no battery backup!)
15. Polish patterns (sound effects, animations)
16. Complete mini-games (integration)

### Phase 2: Expansion (Tiers 17-32, 512 lessons)
**Spiral:** Second pass through all games
**Focus:** Advanced STIC techniques, complex AI, GRAM animation, multi-direction scrolling challenges (non-trivial on STIC), ROM banking strategies

#### New Patterns:
- **GRAM programming** - 64 user-definable cards (8×8 pixels each, animation!)
- **MOB doubling** - 2×2 or 2×4 sprite combinations for large objects
- **MOB priority** - Sprite layering and depth
- **Smooth scrolling simulation** - Challenging due to 20×12 card grid (not pixel-based)
- **ROM banking** - 8KB segments switched at $5000 boundaries
- **BACKTAB manipulation** - 20×12 background card table reprogramming
- **Envelope synthesis** - PSG envelope generator for complex sounds
- **Keypad overlays** - Game-specific controller templates
- **AI pathfinding** - Grid-based movement for sports/strategy
- **Multiplayer coordination** - Two controller support patterns
- **Data compression** - Critical for 4KB-16KB ROMs
- **GROM sharing** - Efficient use of built-in graphics

### Phase 3: Enhanced Hardware (Tiers 33-40, 512 lessons)
**Spiral:** Third pass - introducing Intellivision II (1983) + ECS (Entertainment Computer System, 1983)
**Focus:** ECS keyboard, ECS extra PSG, Intellivision II compatibility, 2KB extra RAM (ECS)

#### Phase 3 Enhancement: ECS Expansion
- **ECS keyboard** - Full QWERTY keyboard (49 keys)
- **Second PSG** - 3 additional sound channels (6 total!)
- **2KB extra RAM** - Total 3.5KB available (from 1.2KB)
- **Serial port** - Computer Link cable (network play potential!)
- **BASIC cartridge** - Optional (but not focus of curriculum)
- **Cassette support** - Data storage (49-button keyboard makes this viable)

**Tier 40 Example - ECS Dual-PSG Music:**
```asm
; 6-channel music using both PSGs
; Base PSG at $01F0-$01F2, ECS PSG at $00F0-$00F2

MUSIC:  MVII    #$0800,R0       ; Note data
        MVO     R0,$01F0        ; Channel A (base PSG)
        MVO     R0,$00F0        ; Channel A (ECS PSG)
        MVII    #$0A00,R0       ; Harmony
        MVO     R0,$01F1        ; Channel B (base)
        MVO     R0,$00F1        ; Channel B (ECS)
        ; ... pattern continues
```

### Phase 4: Advanced Fundamentals (Tiers 41-48, 512 lessons)
**Spiral:** Fourth pass
**Focus:** Professional game architecture, ROM banking mastery, data compression, procedural content generation, complex AI systems, network play patterns (ECS serial)

#### Advanced Techniques:
- **Procedural level generation** - Critical for ROM space conservation
- **AI opponent strategies** - Sports games, strategy games
- **Network protocol** - ECS serial port multiplayer
- **Advanced ROM banking** - 16KB+ games (banking choreography)
- **Hardware sprite limits** - 8 MOB multiplexing strategies
- **Card animation systems** - GRAM cycling for effects
- **Music engines** - Complex 6-channel compositions (ECS)
- **Text adventure engines** - ECS keyboard integration
- **Save/load systems** - Cassette tape via ECS
- **Voice synthesis simulation** - PSG noise channel tricks

### Phase 5: Specialized Systems (Tiers 49-52, 512 lessons)
**Spiral:** Fifth pass through genre specializations
**Focus:** Sports game mastery, strategy game complexity, action game speed optimization, adventure game depth

#### Genre Specializations:
- **Sports AI** - Baseball (pitch prediction), Football (play calling), Basketball (shot selection)
- **Strategy games** - Turn-based engines, hex maps, unit AI
- **Action games** - Fast-paced MOB movement, smooth scrolling tricks
- **Adventure games** - Parser engines (ECS keyboard), inventory systems
- **Educational games** - Keyboard typing tutors, math challenges
- **Board game conversions** - Chess, checkers, poker

### Phase 6: Platform Limits (Tiers 53-56, 512 lessons)
**Spiral:** Sixth pass - pushing boundaries
**Focus:** Maximum sprite counts (MOB multiplexing), complex background effects, data compression mastery, RAM usage minimization

#### Limit-Pushing Techniques:
- **MOB multiplexing** - 16+ visible sprites (8 hardware limit overcome!)
- **GRAM animation banks** - Rapid card switching for effects
- **ROM size maximization** - 24KB+ games with banking
- **Raster effects** - Timing-based color changes
- **Pseudo-3D** - Scaling tricks with MOB doubling
- **Advanced physics** - Ball trajectories, realistic movement
- **Complex audio** - 6-channel orchestration + noise effects

### Phase 7: Maximum Capabilities (Tiers 57-58, 512 lessons)
**Spiral:** Seventh pass - commercial-quality
**Focus:** Full-featured games, advanced graphics tricks, professional music, polished UI, speed optimization

#### Commercial Techniques:
- **Professional sprite art** - MOB design patterns, animation cycles
- **Orchestral music** - Full 6-channel scores with dynamics
- **Advanced AI** - Commercial sports game intelligence
- **Polish effects** - Screen transitions, particle effects (card-based)
- **Difficulty curves** - Progressive challenge systems
- **Replay systems** - RAM-efficient playback
- **Hidden content** - Easter eggs, unlockables

### Phase 8: Modern Homebrew (Tiers 59-60, 512 lessons)
**Spiral:** Final pass - cutting-edge homebrew techniques
**Focus:** 2020s homebrew tools, modern development workflows, emulator-specific optimizations, flash cartridge features

#### Modern Development:
- **jzIntv emulator integration** - Debugging, development cycle
- **AS1600 assembler** - Modern toolchain
- **SDK-1600** - Full development environment
- **Flash cartridge development** - LTO Flash! (unlimited ROM space via flash)
- **Modern tools** - IntyBASIC (higher-level option), graphics editors
- **Community techniques** - AtariAge homebrew scene patterns
- **Cross-platform patterns** - Techniques from other retro platforms
- **Preservation** - ROM archiving, documentation

## Pattern Library Structure

The curriculum builds a comprehensive library of reusable patterns:

1. **Core Patterns (Phase 1)** - 50 foundational patterns
2. **Advanced Patterns (Phase 2)** - 75 complex techniques
3. **ECS Patterns (Phase 3)** - 50 expansion-specific
4. **Optimization Patterns (Phase 4-5)** - 100 performance techniques
5. **Genre Patterns (Phase 5-6)** - 150 game-specific patterns
6. **Polish Patterns (Phase 7)** - 75 professional touches
7. **Modern Patterns (Phase 8)** - 50 contemporary techniques

**Total:** ~550 reusable patterns across 8 phases

## Hardware Progression

**Phase 1-2: Base Intellivision**
- CP1610 @ 894.886 kHz (16-bit)
- 1456 bytes RAM (1216 available)
- STIC graphics: 8 MOBs, 20×12 background, 16 colors
- PSG: 3 channels + noise
- Controller: 16-dir disc + 12 keypad + 4 action buttons
- 4KB-8KB ROM typical

**Phase 3+: Enhanced (ECS)**
- +2KB RAM (total 3.5KB available)
- +Second PSG (6 audio channels total)
- +49-key keyboard
- +Serial port (network play)
- +Cassette interface (data storage)
- 16KB-24KB ROM typical

**Phase 7-8: Modern Homebrew**
- LTO Flash! cartridge (unlimited ROM via flash memory)
- Modern development tools (jzIntv, SDK-1600)
- Emulator debugging features
- Cross-platform development techniques

## Spiral Learning Example: Breakout

**Phase 1 (Tier 3):** Basic paddle, ball, single row of bricks. Teaches MOB movement, collision, controller input. 1 screen. (~50 lines assembly)

**Phase 2 (Tier 19):** Multiple brick rows, score display, GRAM animation for brick destruction. Introduces GRAM programming, multi-level structures. (~200 lines)

**Phase 3 (Tier 35):** ECS dual-PSG music, keyboard support for controls, enhanced sound effects. Network play via serial port (2-player cooperative). (~400 lines)

**Phase 4 (Tier 43):** Power-ups (multi-ball, paddle extend), procedurally generated levels, advanced physics (ball spin). (~600 lines)

**Phase 5 (Tier 50):** Boss battles (moving brick formations), complex scoring, difficulty progression. (~800 lines)

**Phase 6 (Tier 54):** Pseudo-3D brick walls, raster effects, MOB multiplexing for particles. (~1000 lines)

**Phase 7 (Tier 57):** Commercial polish, orchestral music, advanced particle effects, replay system. (~1500 lines)

**Phase 8 (Tier 59):** Modern homebrew release, flash cartridge optimization, community integration. (~1500 lines + modern tooling)

## Key Differences from Other Platforms

1. **16-bit Architecture (1979!)** - First home console with 16-bit CPU, unusual instruction set with no flags register
2. **Extreme RAM Constraint** - Only 1456 bytes total (1216 available) - second smallest in curriculum after Atari 2600!
3. **Unique Controller** - 16-direction disc + 12-button keypad + 4 side buttons (revolutionary for era)
4. **Word Addressing** - All memory addresses are 16-bit words, not bytes (unusual)
5. **GRAM System** - 64 user-definable 8×8 cards for animation and custom graphics
6. **Card-Based Display** - 20×12 background cards (not pixel-based), makes smooth scrolling challenging
7. **ECS Expansion** - Keyboard, second PSG, extra RAM, serial port (network play!)
8. **CP1610 Quirks** - SDBD prefix for 16-bit immediate data, no flags register (comparisons set register values)
9. **Sports Game Focus** - Platform known for advanced sports games (baseball, football, basketball) with complex AI
10. **STIC Video Chip** - Sprite Multiplexed Object Graphics (MOBs) with hardware collision detection

## Assessment Strategy

**Formative Assessment:**
- Code challenges at end of each tier (e.g., "Add power-ups to your game")
- Pattern recognition exercises ("Identify the MOB doubling pattern")
- Debugging challenges ("Fix the collision detection")
- Performance optimization tasks ("Reduce RAM usage by 100 bytes")

**Summative Assessment:**
- End of each phase: Complete game from scratch in chosen genre
- Must demonstrate all patterns learned in that phase
- Rubric covers: code structure, RAM efficiency, visual polish, gameplay feel
- Peer review component (code sharing within cohort)

**Phase Milestones:**
- **Phase 1:** Complete working game (simple, one screen)
- **Phase 2:** Multi-level game with GRAM animation
- **Phase 3:** ECS-enhanced game (dual-PSG + keyboard/serial)
- **Phase 4:** Professional-architecture game (ROM banking, compression)
- **Phase 5:** Genre-mastery project (sports/strategy/action/adventure)
- **Phase 6:** Technical showcase (pushing hardware limits)
- **Phase 7:** Commercial-quality release
- **Phase 8:** Modern homebrew with community release

## Success Criteria

**By Phase 4, learners can:**
- Write CP1610 assembly fluently (understand 16-bit word addressing, SDBD prefix, no flags quirks)
- Manage extreme RAM constraints (1456 bytes efficiently)
- Program STIC graphics (8 MOBs, GRAM, 20×12 background)
- Implement complex AI (sports game opponents)
- Create multi-channel music (PSG programming)
- Handle controller input (disc + keypad + action buttons)
- Use ECS expansion (keyboard, second PSG, serial port)

**By Phase 8, learners can:**
- Develop commercial-quality Intellivision games
- Push hardware to absolute limits (MOB multiplexing, raster effects)
- Work with modern homebrew tools (jzIntv, SDK-1600, LTO Flash!)
- Contribute to active Intellivision homebrew community
- Port techniques from other platforms
- Release and distribute homebrew titles

## Resources Required

**Phase 1-2:**
- jzIntv emulator (cross-platform, accurate, free)
- AS1600 assembler (or SDK-1600)
- Text editor
- Intellivision reference documentation (CP1610, STIC, PSG)
- Controller overlay templates (PDF)

**Phase 3+:**
- ECS ROM images (for testing ECS features)
- Network testing setup (for serial port development)
- Multiple controller profiles (keyboard + disc configurations)

**Phase 7-8:**
- LTO Flash! cartridge (optional, for real hardware)
- Original Intellivision or Intellivision II (optional)
- Modern development tools (IntyBASIC for prototyping, graphics editors)
- Community resources (AtariAge forums, homebrew scene)

**All Phases:**
- Version control (Git)
- Bug tracking
- Community engagement (for feedback and collaboration)

---

**Total Lesson Count:** 4,096 assembly lessons across 60 tiers
**Estimated Time:** 2-4 years of dedicated study (assuming ~3 lessons per week)
**Unique Advantage:** Most extreme RAM constraint curriculum (after 2600), unique 16-bit 1979 architecture, revolutionary controller, strong sports game focus
