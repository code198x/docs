# Full Game Outline: C64 Starfield (128 Units)

**Game:** Starfield (Game 1)
**Units:** 128 (8 phases × 16 units)
**Target Quality:** Commercial-grade fixed-screen shooter (1985-86 era)
**Comparable To:** Arcadia, Gridrunner → evolving to Armalyte, Delta-level polish by completion

---

## What Makes This "C64"

The Commodore 64 has:
- **8 hardware sprites** — real movable objects from the start, no software rendering needed
- **SID sound chip** — 3 voices with ADSR envelopes, a resonant filter, and waveform control
- **VIC-II video** — sprites, custom character sets, raster interrupts, 16 colours
- **CIA chips** — joystick input, keyboard scanning, precision timers
- **Zero page** — 256 bytes of fast variable storage (the 6510's secret weapon)
- **64KB RAM with ROM banking** — a generous playground with hidden complexity

This shooter showcases the hardware sprite system and the SID. Player and enemies are hardware sprites from Unit 1. SID voices provide punchy sound effects immediately, building toward a full three-voice soundtrack. Raster interrupts — the C64 programmer's most powerful tool — unlock colour effects and sprite multiplexing. The result is unmistakably C64.

---

## Design Philosophy

- **One concept per unit** — never overwhelming
- **Always playable** — from Unit 2 onwards
- **Debugging inline** — every unit includes "if it doesn't work"
- **6510 skill per unit** — assembly concepts build alongside the game
- **Hardware sprites from Unit 1** — the C64's advantage, used immediately
- **SID sound from Unit 4** — not silent until late game
- **Raster interrupts from Phase 4** — the technique that unlocks everything
- **Commercial quality by Unit 128** — a real game

---

## 6510 Assembly Progression

| Phase | 6510 Focus |
|-------|-----------|
| 1 (Ignition) | Registers (A/X/Y), zero page, LDA/STA, addressing modes, CMP, branches, JSR/RTS |
| 2 (The Fleet) | Indexed addressing, lookup tables, indirect addressing, comparison chains |
| 3 (Firepower) | Bit manipulation (AND/ORA/EOR), 16-bit arithmetic (ADC/SBC), stack operations |
| 4 (Incoming) | Interrupts (SEI/CLI), IRQ vector, raster register ($D012), hardware timing |
| 5 (Stardust) | Custom character sets, VIC bank switching, colour RAM, self-modifying code |
| 6 (Waveform) | SID register architecture, ADSR envelopes, filter control, timer-driven music |
| 7 (Command) | Raster-precise timing, sprite multiplexing, complex state machines |
| 8 (Launch) | Code optimisation, memory management, I/O routines, PAL/NTSC detection |

By Unit 128, learners have a working knowledge of the 6510 instruction set, VIC-II graphics, SID audio, and the raster interrupt techniques that define C64 programming.

---

## Phase 1: Ignition (Units 1-16)

**Goal:** Complete game loop — shoot enemies, score points, die, restart.
**6510 Focus:** Registers, addressing modes, zero page, branches, subroutines.
**Graphics:** Hardware sprites. The C64 gives you real sprites from the start — no rendering code needed.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 1 | BASIC stub + ship sprite on screen | `LDA`/`STA`, memory addresses, VIC-II sprite registers | See your ship |
| 2 | Joystick moves ship | `LDA $DC00`, `AND` bit mask, `BEQ`/`BNE` branches | **Control something** |
| 3 | Fire button shoots | Zero-page variables, `INC`/`DEC` | Bullet flies up |
| 4 | Laser sound (SID voice 1) | `STA $D4xx`, waveform + gate bit concept | Satisfying "pew" |
| 5 | One enemy sprite | Sprite enable bits (`ORA`), sprite positions | Target exists |
| 6 | Bullet hits enemy | `CMP` comparisons, coordinate distance check | **It dies!** |
| 7 | Explosion sound + sprite flash | SID noise channel, sprite colour register change | Feedback |
| 8 | Score display | 16-bit `ADC` with carry, BCD or hex→decimal conversion | See your points |
| 9 | Enemies spawn continuously | `JSR`/`RTS` subroutines, SID voice 3 oscillator for random | Challenge |
| 10 | Enemy touches ship = death | Bounding box collision (or hardware collision `$D01E`) | You can die |
| 11 | Game over screen | Game states, screen RAM text output | End state |
| 12 | Press fire to restart | State machine reset, initialisation routine | **Complete loop** |
| 13 | Title screen | Screen RAM + colour RAM fills, character output | Feels real |
| 14 | Three lives | Game state in zero page, display update | Forgiveness |
| 15 | Life lost flash/sound | Border flash (`$D020`), SID death sound | Feedback |
| 16 | Integration + edge cases | Screen boundaries, sprite X bit 8 (`$D010`) | Solid foundation |

**C64-Specific Unit 1:**
```asm
; BASIC stub: 10 SYS 2061 (launches machine code)
*= $0801
    !byte $0c,$08,$0a,$00,$9e,$32,$30,$36,$31,$00,$00,$00

*= $080d
    ; Enable sprite 0
    lda #%00000001
    sta $d015           ; Sprite enable register

    ; Position sprite 0 (centre-bottom)
    lda #172
    sta $d000           ; Sprite 0 X
    lda #220
    sta $d001           ; Sprite 0 Y

    ; Set sprite colour (white)
    lda #1
    sta $d027           ; Sprite 0 colour

    ; Point sprite 0 to data at $2000 (block 128)
    lda #128
    sta $07f8           ; Sprite 0 data pointer

    jmp *               ; Infinite loop (for now)

*= $2000               ; Sprite data (64 bytes per sprite)
    ; ... 24 rows × 3 bytes = ship graphic
```

**If it doesn't work (Unit 1):**
- **No sprite?** Check `$D015` has the right bit set. Check `$07F8` points to the right 64-byte block.
- **Wrong position?** X positions >255 need the corresponding bit in `$D010` (MSB register).
- **Wrong colour?** Sprite colour registers are `$D027`-`$D02E`. Values 0-15 only.
- **Garbled sprite?** Sprite data must be 64 bytes aligned. Block number = address ÷ 64.

**End of Phase 1:** Playable shooter with hardware sprites. Simple, but a complete game you'd recognise as C64.

---

## Phase 2: The Fleet (Units 17-32)

**Goal:** Multiple enemy types with distinct behaviours. VIC-II sprite system mastery.
**6510 Focus:** Indexed addressing, lookup tables, indirect addressing.
**Sprites:** All 8 sprite slots managed. Understanding VIC-II priority, collision, and X-expansion.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 17 | Enemy data table (type, x, y, speed, alive) | Tables with `LDA table,X`, stride access | Organised enemies |
| 18 | Multiple enemies from table | Loop with index offset, zero-page pointer | Several on screen |
| 19 | Fast enemy (dives straight down) | Speed as data field, parameterised update | Variety begins |
| 20 | Slow enemy (drifts sideways) | Combined X+Y movement from table | Pacing contrast |
| 21 | Zigzag enemy (weaves as it falls) | Direction toggle or sine table lookup | Movement patterns |
| 22 | Different sprite graphics per type | Sprite pointer table (`$07F8`+), indirect load | Visual distinction |
| 23 | Different colours per type | Colour as data field → `$D027`+ register | Instant recognition |
| 24 | Different point values per type | Score lookup table, indexed access | Risk/reward |
| 25 | Wave system (clear all = next wave) | Enemy alive counter, state transitions | Structure |
| 26 | Wave composition tables | Data-driven wave definitions (which types, how many) | Varied challenge |
| 27 | Faster spawning each wave | Timer adjustment per wave, difficulty ramping | Escalation |
| 28 | Wave number display | HUD updates via screen RAM writes | Progress visible |
| 29 | Sprite priority and ordering | `$D01B` (sprite-background priority) | Visual correctness |
| 30 | Sprite X high bit management | `$D010` bit manipulation for full screen width | No X-position bugs |
| 31 | Hardware collision detection | `$D01E` sprite-sprite, `$D01F` sprite-background | C64 advantage |
| 32 | Integration + balance tuning | Playtesting, wave composition, speed parameters | Feels fair |

**Key Teaching Moment (Unit 17):**
The 6510 doesn't have structs. You fake them with a single table and stride access. If each enemy uses 5 bytes (type, x, y, speed, alive), enemy 0 starts at offset 0, enemy 1 at offset 5, enemy 2 at offset 10. `LDA enemy_table,X` with X set to the right multiple gives you struct-like access. This pattern underpins every game from here on.

**Key Teaching Moment (Unit 31):**
The VIC-II detects sprite-sprite collisions in hardware — reading `$D01E` tells you which sprites overlap. No distance calculations needed. This is a genuine C64 advantage over platforms like the Spectrum. But: the register resets when read, and it only tells you WHICH sprites collided, not which pair. You still need logic to determine what happened.

**End of Phase 2:** Varied, escalating challenge. All 8 sprite slots in active use. Sprite system understood deeply.

---

## Phase 3: Firepower (Units 33-48)

**Goal:** Power-ups make the player stronger. Sprite allocation becomes strategic.
**6510 Focus:** Bit manipulation (AND/ORA/EOR), 16-bit arithmetic, stack operations.
**Key challenge:** With 8 sprite slots total — player (1) + bullet (1) + enemies (up to 6) — adding power-up items and shields means something has to give. This phase teaches allocation thinking.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 33 | Sprite allocation plan (who gets which slot) | Bit flags with `AND`/`ORA` for slot tracking | System design |
| 34 | Power-up drops from killed enemies | Reuse dead enemy's sprite slot for power-up item | Collectibles exist |
| 35 | Collect power-up = effect | `PHA`/`PLA` for state preservation during transitions | System works |
| 36 | Speed boost power-up | Temporary state with frame countdown in zero page | Agility |
| 37 | Rapid fire power-up | Fire rate as variable, `DEC` timer per frame | Firepower |
| 38 | Power-up collect sound | SID voice 2, distinct waveform from laser | Satisfying pickup |
| 39 | Power-up visible on HUD | Character display update routine | Know what you have |
| 40 | Power-ups are temporary (timer) | 16-bit countdown with `SBC` and borrow | Strategic decisions |
| 41 | Timer warning (flashing HUD element) | Frame counter `AND` mask for blink rate | Know when it ends |
| 42 | Double shot (two bullets from one press) | Bullet pool, shared update routine | Firepower |
| 43 | Spread shot (three directions) | Velocity tables for angle offsets | Screen coverage |
| 44 | Shield (one free hit) | State flag in zero page | Defensive option |
| 45 | Shield visual (sprite colour change) | `$D027` manipulation, BRIGHT palette choice | See protection |
| 46 | Shield break sound/visual | Combined SID + colour register feedback | Dramatic feedback |
| 47 | Power-up spawn frequency tuning | Probability per kill, wave-dependent rates | Balance |
| 48 | Integration + balance | Sprite allocation audit, power-up playtesting | Rewarding loop |

**C64-Specific:**
- Power-ups reuse a dead enemy's sprite slot — no sprite wasted on a static pickup
- Shield shown via sprite colour change (no extra sprite needed)
- Double/spread shot shares bullet sprites by rapid cycling
- The 8-sprite limit forces design discipline: if everything needs a sprite, you plan carefully

**End of Phase 3:** Player has meaningful choices. Power-ups feel great. The 8-sprite limit is a design challenge, not a bug.

---

## Phase 4: Incoming (Units 49-64)

**Goal:** Enemies shoot back. Raster interrupts introduced for stable timing and colour effects.
**6510 Focus:** Interrupts (SEI/CLI), IRQ vector, raster register, hardware timing.
**Key moment:** Raster interrupts are the single most important C64 programming technique. They're introduced here for timing, but they'll unlock multiplexing in Phase 7.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 49 | Enemy bullet (one at a time) | Bullet pool pattern, sprite slot reuse | Danger from above |
| 50 | Enemy bullet sprite | Distinct graphic from player bullets | Visible threat |
| 51 | Enemy bullet hits player | Shared collision routine (generic, reusable) | Real danger |
| 52 | Enemy fire sound | SID voice 3 (noise channel for gunshot) | Audio warning |
| 53 | Random enemy fires | SID oscillator 3 for random (`$D41B`) — free random numbers | Unpredictable |
| 54 | Shooter enemy type (fires aimed) | Direction calculation via subtraction | Smart enemies |
| 55 | Multiple enemy bullets | Pool allocation, cycling freed sprite slots | Intensity |
| 56 | Raster interrupts explained | `$D012`, `$D01A`, IRQ vector (`$FFFE`), `SEI`/`CLI` | **The big unlock** |
| 57 | Main loop on raster sync | IRQ-driven frame timing replaces busy-wait | Smooth animation |
| 58 | Raster colour bar in border | Colour change at specific scanline via raster IRQ | C64 signature effect |
| 59 | Aimed vs random shot mix | Probability via `AND` mask on `$D41B` random byte | Variety |
| 60 | Player bullet destroys enemy bullet | Bullet-bullet collision check | Skill option |
| 61 | Player death = bullets cleared | State reset, sprite disable sequence | Fair restart |
| 62 | Difficulty ramp per wave | Parameter tables indexed by wave number | Escalation |
| 63 | Bullet density tuning | Max bullet count, fire rate caps per wave | Not overwhelming |
| 64 | Integration + combat balance | Full playtesting with raster-stable timing | Challenging but fair |

**Key Teaching Moment (Unit 56):**
Raster interrupts are the C64 programmer's most powerful tool. The VIC-II triggers an interrupt when the electron beam reaches a specific screen line. Your code runs at *exactly* that moment — not "sometime during the frame" but precisely at line N. This enables: stable frame timing (now), colour effects (Phase 5), and sprite multiplexing (Phase 7). Every serious C64 game uses raster interrupts. Learning them here pays off for the entire curriculum.

**Key Teaching Moment (Unit 53):**
The SID gives you free random numbers. Voice 3's oscillator runs independently — set it to noise waveform, then read `$D41B` for a random byte whenever you want. No seed, no algorithm, no code. This is a genuine C64 luxury.

**End of Phase 4:** Proper two-way combat with raster-stable timing. The colour bar in the border proves the technique works. Foundations laid for everything that follows.

---

## Phase 5: Stardust (Units 65-80)

**Goal:** Visual polish to commercial standard. Custom characters, multicolour sprites, raster effects.
**6510 Focus:** Character set manipulation, VIC bank switching, colour RAM, self-modifying code.
**The moment:** The game's namesake starfield finally appears — as custom character graphics, not sprites.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 65 | Custom character set basics | VIC memory setup (`$D018`), character data format | New visual system |
| 66 | Starfield background (custom chars) | Character ROM → RAM copy, custom tile design | **The starfield appears** |
| 67 | Scrolling stars (character animation) | Rotating character data in RAM, frame timing | Depth and motion |
| 68 | Multiple star speeds (two layers) | Different update rates per character group | Parallax feel |
| 69 | Explosion animation (sprite, 4 frames) | Sprite pointer cycling, frame counter | Visual impact |
| 70 | Player death explosion (bigger) | Multi-sprite explosion reusing freed slots | Dramatic stakes |
| 71 | Screen flash on death | `$D020`/`$D021` border + background flash | Emphasis |
| 72 | Enemy spawn animation | Sprite Y-expand (`$D017`) toggle effect | Polish |
| 73 | Multicolour sprite mode | `$D01C` bit set, `$D025`/`$D026` shared colours | Rich detail |
| 74 | Multicolour ship and enemies | Redesigned sprites (double-wide pixels, 3 colours) | **Visual upgrade** |
| 75 | Raster colour splits | Multiple raster IRQs: different `$D021` per zone | C64 signature |
| 76 | Colour cycling on title screen | Frame-driven colour register rotation | Attract mode flair |
| 77 | Custom HUD font | Character set includes custom digits/glyphs | Cohesive look |
| 78 | Score flash on increase | Colour RAM manipulation, timed reset | Feedback |
| 79 | Smooth sprite movement (fractional) | Fixed-point: 16-bit position, high byte → register | Professional feel |
| 80 | Integration + visual consistency | Audit all graphics, sprite/character harmony | Looks like a real game |

**Key Teaching Moment (Unit 65):**
The VIC-II displays characters from a 2KB block of memory. By default this is the character ROM. But you can point it at RAM and fill that RAM with whatever graphics you want. This is how C64 games create backgrounds: custom character sets with tiles designed for the game. The starfield is just a handful of characters with different dot patterns arranged across screen RAM.

**Key Teaching Moment (Unit 73):**
Multicolour mode doubles the pixel width but gives each sprite 3 colours plus transparent. Standard sprites: 24×21 pixels, 1 colour. Multicolour: 12×21 double-wide pixels, 3 colours. Two colours (`$D025`/`$D026`) are shared across all multicolour sprites; the third is per-sprite (`$D027`+). Most commercial C64 games use multicolour. The trade-off is less horizontal detail for more colour depth.

**End of Phase 5:** The game looks commercially polished. Parallax starfield, multicolour sprites, raster colour effects. Screenshots would sell it.

---

## Phase 6: Waveform (Units 81-96)

**Goal:** Full SID soundtrack and rich sound design. The chip that defined a generation.
**6510 Focus:** SID register architecture, ADSR envelopes, filter control, timer-driven music playback.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 81 | SID architecture deep dive | Register map (`$D400`-`$D41C`), 3-voice structure | Understanding the chip |
| 82 | ADSR envelopes | Attack-Decay-Sustain-Release values and timing | Shaped sounds, not bleeps |
| 83 | Waveform types | Triangle, sawtooth, pulse, noise — selection and character | Tonal variety |
| 84 | Sound effect library | Parameterised routine (waveform, freq, ADSR, sweep) | Varied SFX |
| 85 | Replace all placeholder sounds | Integrate crafted SFX throughout the game | Cohesive audio |
| 86 | Title music (2 voices) | Note table (freq values), sequence data, playback routine | Atmosphere |
| 87 | Three-voice music | Voice 3 bass or counter-melody, interleaved playback | Full SID richness |
| 88 | Music timing via CIA timer | CIA timer 1 interrupt for stable tempo | Rock-solid playback |
| 89 | Music stops on game start | State-controlled playback, clean voice release | Clean transition |
| 90 | Game over jingle | Short descending phrase | Punctuation |
| 91 | Wave complete jingle | Short ascending phrase | Achievement |
| 92 | High score jingle | Celebratory phrase, distinct from others | Distinction |
| 93 | SID filter | Low-pass/high-pass/band-pass (`$D418`), cutoff, resonance | SID character |
| 94 | Filter sweeps on explosions | Dynamic cutoff frequency during sound effect | **That SID sound** |
| 95 | Sound priority (SFX steal voice) | Voice stealing with priority queue, don't cut music | No ugly cutoff |
| 96 | Integration + audio balance | Volume, filter routing, voice allocation audit | Sounds great |

**SID-Specific:**
The SID has features no other 8-bit sound chip matches: proper ADSR envelopes (not just on/off), a resonant multi-mode filter, ring modulation, and oscillator sync. Phase 6 doesn't just add "music" — it teaches what makes the SID *the SID*. The filter (Unit 93) is the single most distinctive feature. When you sweep the cutoff frequency during an explosion, you get that unmistakable C64 sound that people still compose music for today.

**End of Phase 6:** Audio matches the visuals in quality. The SID sings. Three-voice music, filter sweeps, punchy effects — the full package.

---

## Phase 7: Command (Units 97-112)

**Goal:** Boss fights that demand sprite multiplexing — the C64's signature advanced technique.
**6510 Focus:** Raster-precise timing, sprite multiplexing algorithm, complex state machines.
**Key moment:** A boss built from 4 sprites + player + bullets + enemies exceeds 8 slots. Multiplexing becomes necessary, not optional.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 97 | Mini-boss every 3 waves | Conditional trigger on wave count | Early taste |
| 98 | Mini-boss: tough enemy (3 hits) | Hit counter, damage state tracking | Tougher target |
| 99 | Mini-boss movement pattern | Simple pattern table (left-right-dive sequence) | Distinct behaviour |
| 100 | Boss every 5 waves (4 sprites) | Multi-sprite entity, coordinated positioning | **Impressive size** |
| 101 | The 8-sprite problem | Analysis: boss(4) + player(1) + bullets = overflow | Understanding the limit |
| 102 | Sprite multiplexing | Reuse sprite registers at different Y via raster IRQ | **The C64 trick** |
| 103 | Boss movement (sweep pattern) | Complex pattern table with timing data | Menacing behaviour |
| 104 | Boss health bar (custom characters) | Gradual depletion display in HUD | Visible progress |
| 105 | Boss hit flash | Sprite colour register toggle on collision | Satisfying feedback |
| 106 | Boss shoots (spread pattern) | Multiple bullet spawn positions, angle offsets | Dangerous |
| 107 | Boss phase 2 at 50% health | State machine transition, pattern change | Escalation |
| 108 | Boss death (big explosion sequence) | Scripted multi-sprite chain explosion | Payoff |
| 109 | Boss defeat bonus + jingle | Score reward, SID celebration | Triumph |
| 110 | Second boss type (different shape, pattern) | Table-driven entity: swap data, same system | Variety |
| 111 | Boss warning (border pulse + SID siren) | Combined visual/audio anticipation cue | Drama |
| 112 | Integration + boss balance | Health/damage tuning, multiplexer stability | Memorable, fair fights |

**Key Teaching Moment (Unit 102):**
Sprite multiplexing is the technique that separates bedroom C64 games from professional ones. The VIC-II draws the screen top-to-bottom. Once a sprite has been fully drawn (the beam is past its last scanline), you can repoint that sprite's position and data pointer to display it again further down the screen. A raster interrupt fires just below the first appearance; the handler repositions the sprite for its second. This is how Armalyte and IO display dozens of sprites with only 8 hardware slots. The raster interrupt skills from Phase 4 make this possible.

**End of Phase 7:** Boss fights are the highlight. Multi-phase encounters with real drama, powered by sprite multiplexing.

---

## Phase 8: Launch (Units 113-128)

**Goal:** Commercial release quality. Everything a real 1986 C64 game would ship with.
**6510 Focus:** Code optimisation, memory management, I/O routines, PAL/NTSC detection.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 113 | High score table (top 5) | Sorted insertion, multi-byte comparison | Competition |
| 114 | Initials entry (3 characters) | Keyboard matrix scanning, character input | Ownership |
| 115 | High scores shown on title | Persistent display integration | Bragging rights |
| 116 | Difficulty select (3 levels) | Menu system, joystick cursor navigation | Accessibility |
| 117 | Difficulty affects gameplay | Parameter tables per difficulty level | Real difference |
| 118 | Extra life at 10,000 points | Threshold detection, celebration effect + jingle | Skill reward |
| 119 | Two-player alternating mode | Player state switching, turn management | Social |
| 120 | Score comparison at game over | Side-by-side display | Competition |
| 121 | Attract mode (auto-play demo) | Recorded input playback or simple AI | Professional |
| 122 | Demo on title after timeout | Timer-triggered state change | Shop display |
| 123 | PAL/NTSC detection | CIA timer comparison, speed adjustment | Platform correct |
| 124 | Continue option (wave restart) | Limited continues, score penalty | Forgiveness |
| 125 | Loading screen (charset art) | Advanced character graphics layout | Presentation |
| 126 | Credits screen | Text display with colour effects | Professional |
| 127 | Final balance + bug sweep | Systematic edge case testing | Release ready |
| 128 | **Complete game — final .prg** | Packaging, crunching, autostart | **Ship it** |

**End of Phase 8:** A game you could put on tape and sell through a 1986 software house. High scores with initials, attract mode, two-player, difficulty select — the full commercial package.

---

## C64-Specific Debugging (Throughout)

**Sprite Issues:**
- No sprite visible? Check `$D015` (enable bits), `$07F8`+ (data pointer), and that sprite data exists at the right address
- Wrong position? X positions >255 need the corresponding bit in `$D010`
- Wrong multicolour? Check `$D01C` (multicolour enable), `$D025`/`$D026` (shared colours)
- Sprite behind background? Check `$D01B` priority register

**VIC-II Display Issues:**
- Screen garbled after charset change? Check VIC bank (`$DD00` bits 0-1) and screen/charset pointer (`$D018`)
- Characters wrong? Character data must be within the selected VIC bank (16KB boundary)
- Colour RAM wrong? Colour RAM is always at `$D800` regardless of VIC bank

**SID Issues:**
- No sound? Check gate bit (bit 0 of control register) — must be set to start
- Sound doesn't stop? Clear the gate bit, check ADSR release value isn't zero
- Wrong pitch? Frequency is 16-bit (low byte + high byte) — check both registers
- Filter not audible? Check `$D418` for filter mode bits AND volume, check `$D417` for filter routing

**Raster Interrupt Issues:**
- IRQ not firing? Check `$D01A` (raster IRQ enable bit), IRQ vector at `$FFFE`/`$FFFF`, and `CLI`
- Double interrupt? Acknowledge by writing to `$D019` at the START of your handler
- Unstable timing? Raster line jitter is normal — stabilise with NOP slide or double-IRQ
- Multiplexing glitches? Raster line must be BELOW the sprite's last scanline before repositioning

**General 6510 Issues:**
- Values corrupted after interrupt? Handler must save/restore A, X, Y (PHA/TXA/PHA/TYA/PHA, reverse on exit)
- Slow performance? Move hot variables to zero page — zero-page operations are 1 cycle faster
- Joystick reads wrong? Use port 2 (`$DC00`), not port 1 (`$DC01`) — port 1 conflicts with keyboard

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 4 (Unit 64) | Phase 8 (Unit 128) |
|--------|-------------------|--------------------|--------------------|
| Graphics | Single-colour sprites | + Raster colour bar, smooth movement | Multicolour, parallax starfield, custom font |
| Enemies | One type, falls down | 4+ types, aimed shots, shooter type | + Bosses, mini-bosses, multiplexed sprites |
| Player | Move + shoot | Power-ups, shield, spread shot | + Difficulty select, attract demo |
| Audio | Single SID voice beeps | Varied SFX on 3 voices | Full 3-voice music, filter sweeps, priority |
| Input | Joystick port 2 | Same | + Keyboard option, menu selection |
| Modes | Single play | Same | Two-player, 3 difficulties, attract mode |
| 6510 Skill | LDA, STA, branches | Interrupts, 16-bit maths, tables | Multiplexing, SID filter, full toolkit |

---

## What This Teaches Beyond the Game

By completing Starfield, learners are ready for:
- **Platform Panic (Game 2):** Sprite positioning → character movement. Hardware collision → platform physics.
- **Maze Raider (Game 3):** Custom character sets → tile-based maze design. Colour RAM → wall colours.
- **Sprite Storm (Game 9):** Basic multiplexing → full sorted sprite multiplexer with interrupt chains.
- **Every future game:** The raster interrupt framework, sprite management patterns, and SID sound engine from Starfield are reused and extended throughout the curriculum.

Starfield isn't just Game 1. It's the foundation.

---

**Version:** 2.0
**Last Updated:** 2026-02-05
