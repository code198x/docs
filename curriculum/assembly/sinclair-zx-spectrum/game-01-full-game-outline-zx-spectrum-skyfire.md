# Full Game Outline: ZX Spectrum Skyfire (128 Units)

**Game:** Skyfire (Game 1)
**Units:** 128 (8 phases × 16 units)
**Target Quality:** Commercial-grade fixed-screen shooter (1985-86 era)
**Comparable To:** Arcadia, Spectipede → evolving to Xenon, Zynaps quality by completion

---

## What Makes This "Spectrum"

The ZX Spectrum has:
- **No hardware sprites** — everything is software-rendered
- **Attribute colour system** — 8×8 cells, one foreground + background per cell
- **Colour clash** — design WITH it, not against it
- **Beeper sound** — one channel, creative tricks required
- **No joystick standard** — keyboard is primary (Kempston optional)

This shooter embraces these constraints. Phase 1 uses attribute blocks for immediate results. Phase 2 upgrades to pixel-level sprites — the foundation skill for every game that follows.

---

## Design Philosophy

- **One concept per unit** — never overwhelming
- **Always playable** — from Unit 2 onwards
- **Debugging inline** — every unit includes "if it doesn't work"
- **Z80 skill per unit** — assembly concepts build alongside the game
- **Attribute system central** — colour IS the game's visual identity
- **Beeper sound from Unit 4** — not silent until late game
- **Pixel sprites from Phase 2** — foundation for all future games
- **Commercial quality by Unit 128** — a real game

---

## Z80 Assembly Progression

| Phase | Z80 Focus |
|-------|-----------|
| 1 (First Light) | Registers, LD, loops, conditions, jumps, input, subroutines |
| 2 (Pixel Craft) | Screen memory, lookup tables, XOR drawing, bit shifting, indirect addressing |
| 3 (The Swarm) | Data structures, arrays, table-driven design, random numbers, state machines |
| 4 (Crossfire) | Object pools, 16-bit arithmetic, bit flags, shared routines |
| 5 (Spectral) | Pixel plotting, animation systems, custom character sets |
| 6 (Resonance) | T-state timing, port I/O, beeper engine, interrupt basics |
| 7 (Nemesis) | Complex state machines, pattern tables, large entity management |
| 8 (Launch) | Sorted arrays, hardware detection, menu systems, tape loading |

By Unit 128, learners have a working knowledge of the Z80 instruction set, Spectrum memory layout, and the core techniques needed for every subsequent game.

---

## Phase 1: First Light (Units 1-16)

**Goal:** Complete game loop — shoot enemies, score points, die, restart.
**Z80 Focus:** Registers, memory, loops, conditions, subroutines.
**Graphics:** Attribute blocks (coloured 8×8 cells). Fast, visible, teaches the attribute system.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 1 | Ship on screen (attribute block) | `LD`, memory addresses, `DJNZ` loops | See your ship (coloured cell) |
| 2 | Keyboard moves ship (QAOP) | `IN` port, `CP`, conditional `JP` | **Control something** |
| 3 | Fire button shoots (SPACE/M) | RAM variables, `INC`/`DEC` | Bullet flies up |
| 4 | Laser sound (beeper) | `OUT` port ($FE), timing loops | Satisfying "pzzt" |
| 5 | One enemy appears | Constants, data bytes (`DB`) | Target exists |
| 6 | Bullet hits enemy | `CP` comparisons, `AND` logic | **It dies!** |
| 7 | Explosion effect + sound | Sequencing, frame counters | Feedback |
| 8 | Score display | 16-bit `ADD`, number→ASCII conversion | See your points |
| 9 | Enemies spawn continuously | `CALL`/`RET` subroutines, R register random | Challenge |
| 10 | Enemy touches ship = death | Bounding box collision | You can die |
| 11 | Game over screen | Game states, string output | End state |
| 12 | Press key to restart | State reset, initialisation routines | **Complete loop** |
| 13 | Title screen | Screen layout, attribute fills | Feels real |
| 14 | Three lives | Game state variables | Forgiveness |
| 15 | Lives display + death flash | Attribute flash, border colour | Feedback |
| 16 | Integration + edge cases | Boundary checks, debugging | Solid foundation |

**Spectrum-Specific Unit 1:**
```asm
; Ship is a coloured attribute cell
; Bright cyan on black = %01000101
ld a,%01000101
ld (ship_attr_addr),a

; Fill the cell's pixels so colour shows
ld hl,ship_screen_addr
ld b,8
ship_fill:
    ld (hl),$ff
    inc h
    djnz ship_fill
```

**If it doesn't work (Unit 1):**
- **No colour?** Check attribute address ($5800+) vs screen address ($4000+)
- **Wrong position?** Screen layout is non-linear — use the formula, don't guess
- **Colour wrong?** Bits are `FBPPPIII` — Flash, Bright, Paper(3), Ink(3)

**End of Phase 1:** Playable shooter with Spectrum character. Simple attribute-block graphics, but a complete game.

---

## Phase 2: Pixel Craft (Units 17-32)

**Goal:** Upgrade from attribute blocks to pixel-level sprites. THE foundation skill for every future game.
**Z80 Focus:** Screen memory layout, lookup tables, XOR drawing, bit shifting, indirect addressing.
**Graphics:** 8×8 pixel sprites with clean movement and colour.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 17 | Spectrum screen memory explained | Address calculation (the thirds) | Understanding the beast |
| 18 | Y→address lookup table | Tables with `DW`, indexed reads | Fast address conversion |
| 19 | Draw 8×8 graphic (ship) | `LD (HL),A` in loops, `INC H` patterns | Real ship graphic |
| 20 | Erase before redraw | XOR drawing (`XOR (HL)`) or clear+draw | Clean movement |
| 21 | Ship moves with pixel graphic | Combined screen + attribute updates | **Professional look** |
| 22 | Draw enemy graphic | Reusable draw routine, parameters via registers | Enemies look real |
| 23 | Multiple enemy graphics | Indirect addressing (`HL` as pointer to sprite data) | Visual variety |
| 24 | Bullet as pixel graphic | Small sprite (1×4 pixels) | Sharp bullets |
| 25 | Explosion animation frames | Frame counter + sprite table | Visual drama |
| 26 | Attribute colour per entity | Separate attribute writes alongside pixels | Colour + detail |
| 27 | Pre-shifted sprites | Bit shifting (`SRL`, `RR`) for sub-cell X | Sub-cell positioning |
| 28 | Smooth horizontal movement | Pixel-level X, not just cell-level | Fluid control |
| 29 | Background preservation | Save-under buffer, restore before draw | Clean compositing |
| 30 | Colour clash management | Design rules: spacing, attribute-aware movement | Spectrum mastery |
| 31 | Performance tuning | `HALT` for frame sync, draw order | Smooth animation |
| 32 | Integration + pixel polish | All graphics upgraded, consistent style | Looks like a real game |

**Key Teaching Moment (Unit 17):**
The Spectrum screen memory layout is notorious. The address for pixel row Y is NOT simply `$4000 + Y × 32`. The screen is divided into thirds, with rows interleaved within each third. This is the single most important thing to understand about Spectrum graphics, and we teach it with a lookup table — practical, fast, and avoids the maths entirely until learners are ready.

**If it doesn't work (Unit 19):**
- **Garbled graphics?** You're incrementing the address wrong — `INC H` moves down one pixel row within a character cell, but wraps oddly at cell boundaries. Use the lookup table.
- **Ghost images?** You're not erasing the old position before drawing the new one.
- **Flickering?** Draw during the vertical blank — sync with `HALT`.

**End of Phase 2:** Game looks genuinely good. Pixel sprites with colour, smooth movement, clean compositing. The learner now has the core drawing skills for every Spectrum game.

---

## Phase 3: The Swarm (Units 33-48)

**Goal:** Multiple enemy types with distinct behaviours. The game gets interesting.
**Z80 Focus:** Data structures, arrays, table-driven design, random numbers, state machines.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 33 | Enemy data structure (type, x, y, speed, alive) | Struct-like records in RAM | Organised enemies |
| 34 | Enemy array (8 enemies) | Array iteration, stride offset | Multiple enemies |
| 35 | Fast enemy (red, dives down) | Speed as data field, parameterised movement | Variety begins |
| 36 | Slow enemy (green, drifts sideways) | Horizontal + vertical movement | Pacing contrast |
| 37 | Zigzag enemy (yellow, weaves) | Sine-like table or direction toggle | Movement patterns |
| 38 | Colour = type (instant recognition) | Attribute byte as enemy property | Visual identity |
| 39 | Different point values per type | Table-driven scoring | Risk/reward |
| 40 | Wave system (clear all = next wave) | State transitions, enemy count tracking | Structure |
| 41 | Wave composition tables | Data-driven wave definitions | Varied challenge |
| 42 | Faster spawning each wave | Difficulty ramping via timer adjustment | Escalation |
| 43 | Wave number display | HUD update routine | Progress visible |
| 44 | Formation spawns (groups entering together) | Timed spawn sequences | Visual flair |
| 45 | Spawn + wave complete sounds | Audio integrated with game events | Punctuation |
| 46 | Brief pause between waves | Timer-based delays | Breathing room |
| 47 | BRIGHT attribute for elite variants | Bit manipulation on attribute byte | Visual hierarchy |
| 48 | Integration + balance | Playtesting, parameter tuning | Feels fair and varied |

**Design Note:**
Enemies are distinguished primarily by attribute colour — this is the Spectrum way. Red dives, green drifts, yellow weaves, cyan shoots (introduced next phase). The learner is designing with the hardware, not fighting it. BRIGHT variants of each colour indicate tougher elites without needing different graphics.

**End of Phase 3:** The game has personality. Each enemy type is instantly recognisable and behaves differently.

---

## Phase 4: Crossfire (Units 49-64)

**Goal:** Two-way combat — enemies shoot back, player gets power-ups. Real gameplay depth.
**Z80 Focus:** Object pools, 16-bit arithmetic, bit flags, shared/generic routines.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 49 | Enemy bullet (one at a time) | Object pool basics | Danger from above |
| 50 | Enemy bullet hits player | Shared collision routine (generic) | Real danger |
| 51 | Enemy fire sound | Distinct from player laser | Audio cue |
| 52 | Random enemy fires | Probability via `AND` mask on random byte | Unpredictable |
| 53 | Shooter enemy type (cyan) | New entry in type table | Role variety |
| 54 | Multiple enemy bullets (pool of 4) | Pool allocation and recycling | Intensity |
| 55 | Aimed shots (toward player) | Direction calculation, 16-bit subtraction | Smart enemies |
| 56 | Aimed vs random mix | Probability tables, difficulty scaling | Variety |
| 57 | Power-up drops from killed enemies | Collectible object spawning | Rewards exist |
| 58 | Speed boost power-up | Temporary state, timer countdown | Agility |
| 59 | Rapid fire power-up | Fire rate as variable, timer duration | Firepower |
| 60 | Double shot (two bullets) | Multiple objects from single input | Coverage |
| 61 | Wide shot (three directions) | Angle offsets for bullet velocity | Screen control |
| 62 | Shield (one free hit) | State flag, BRIGHT on ship | Defensive option |
| 63 | Power-up flash (`FLASH` attribute) + border colour | Attribute animation, port writes | Visibility |
| 64 | Integration + combat balance | Tuning fire rates, power-up frequency | Challenging but fair |

**Spectrum-Specific:**
- Enemy bullets use a different INK colour from enemies — avoids clash confusion
- Power-ups use `FLASH` attribute to stand out (the Spectrum's built-in "look at me")
- Active power-up shown via border colour (free real estate on the Spectrum)
- Shield shown via `BRIGHT` on ship attribute

**End of Phase 4:** Proper two-way combat with meaningful player choices. Dodging, shooting, and power-up strategy.

---

## Phase 5: Spectral (Units 65-80)

**Goal:** Visual polish to commercial standard.
**Z80 Focus:** Pixel plotting, animation systems, custom character sets.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 65 | Starfield background (pixels in PAPER area) | Pixel plot routine, random placement | Depth and atmosphere |
| 66 | Multiple star speeds (parallax) | Speed tables, modular update | Layered feel |
| 67 | Stars don't cause colour clash | Attribute-aware plotting | Technical care |
| 68 | Multi-frame explosion (4 frames) | Animation state machine | Real impact |
| 69 | Player death sequence | Scripted multi-frame sequence | Dramatic stakes |
| 70 | Screen shake (scroll offset trick) | Temporary address offset | Game feel |
| 71 | Enemy spawn animation (flash in) | Attribute fade-in sequence | Polish |
| 72 | Score highlight on change | Temporary attribute modification | Feedback |
| 73 | Custom font (8×8 characters) | Character set definition, `DEFS` | Cohesive look |
| 74 | Title screen upgrade (large text, colours) | Combining custom chars + attributes | Presentation |
| 75 | Colour scheme per wave group | Attribute palette swaps | Visual variety |
| 76 | Wave transition effect (wipe/flash) | Screen manipulation routines | Punctuation |
| 77 | Bullet trail effect (pixel persistence) | Delayed erase technique | Visual flair |
| 78 | Near-miss border flash | Proximity detection, `OUT` ($FE) | Tension builder |
| 79 | Attract mode colour cycling | Attribute animation on title | Eye-catching |
| 80 | Integration + visual consistency | Audit all graphics, clean up clash | Looks professional |

**Key Design Decision:**
The starfield uses individual pixels plotted within the PAPER colour area — they're white dots on black. Because they exist only in screen memory (not attribute memory), they don't cause colour clash with the attribute-coloured game objects above them. This is a classic Spectrum technique: layer pixel detail underneath attribute colour.

**End of Phase 5:** The game looks commercially polished. Distinctive Spectrum visual style.

---

## Phase 6: Resonance (Units 81-96)

**Goal:** Rich beeper sound design — music, effects, and a proper sound engine.
**Z80 Focus:** T-state timing, port I/O, interrupt basics, music data formats.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 81 | Beeper fundamentals deep dive | `OUT` ($FE), T-state counting | Understanding pitch |
| 82 | Pitch control routine | Loop length → frequency relationship | Full range |
| 83 | Duration control | Outer loop for note length | Notes, not just bleeps |
| 84 | Sound effect library | Parameterised routine (pitch, duration, sweep) | Varied SFX |
| 85 | Sweep effects (rising, falling) | Pitch modification per cycle | Laser, explosion, power-up |
| 86 | Replace placeholder sounds | Integrate new SFX throughout game | Cohesive audio |
| 87 | Multi-voice trick (rapid alternation) | Interleaved timing loops | Richer sound |
| 88 | Note table (frequency→loop values) | Lookup table of pitch constants | Musical scale |
| 89 | Simple melody player | Note + duration data, sequence reader | Music possible |
| 90 | Title screen tune | Composition as data bytes | Atmosphere |
| 91 | Game over jingle | Short descending phrase | Punctuation |
| 92 | Wave complete jingle | Short ascending phrase | Achievement |
| 93 | High score jingle | Distinct celebratory phrase | Distinction |
| 94 | In-game rhythmic pulse | Short periodic beep, minimal gameplay halt | Tension |
| 95 | Sound priority system | Queue with priority levels, don't interrupt music | No cutoff or clash |
| 96 | Integration + audio balance | All sounds at right volume/priority | Sounds great |

**Spectrum-Specific:**
The beeper halts the CPU during playback — every sound pauses gameplay briefly. This is a fundamental Spectrum constraint. Sound effects must be SHORT (a few hundred T-states). Music can only play when gameplay is paused (title screen, between waves, game over). The in-game rhythmic pulse (Unit 94) is a compromise: a tiny periodic beep that adds atmosphere without noticeable gameplay interruption.

**End of Phase 6:** Impressive beeper sound for a single-bit speaker. Punchy effects, recognisable jingles, a title tune.

---

## Phase 7: Nemesis (Units 97-112)

**Goal:** Boss fights that use everything we've built — graphics, audio, and effects combined.
**Z80 Focus:** Complex state machines, pattern tables, large entity management.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 97 | Mini-boss every 3 waves | Conditional trigger on wave count | Early taste |
| 98 | Mini-boss: tough enemy (3 hits) | Hit counter, damage state | Tougher target |
| 99 | Mini-boss movement pattern | Simple pattern table (left-right-dive) | Distinct behaviour |
| 100 | Boss every 5 waves (multi-cell, 4×2) | Large entity rendering (multiple draws) | Impressive size |
| 101 | Boss movement (sweep pattern) | Complex pattern table with timing | Menacing behaviour |
| 102 | Boss health bar in HUD | Gradual depletion display | Visible progress |
| 103 | Boss hit flash (`BRIGHT` toggle) | State toggle on collision | Satisfying feedback |
| 104 | Boss shoots (spread pattern) | Multiple bullet spawn positions | Dangerous |
| 105 | Boss phase 2 at 50% (colour change) | State machine transition | Escalation |
| 106 | Phase 2 = faster, angrier pattern | Parameter modification on state change | Drama |
| 107 | Boss death (big explosion sequence) | Multi-frame, multi-cell scripted effect | Payoff |
| 108 | Boss defeat bonus + jingle | Score reward, audio celebration | Triumph |
| 109 | Second boss type (different shape, pattern) | Polymorphic entity (table-driven) | Variety |
| 110 | Second boss unique attack (aimed burst) | Different firing pattern | Fresh challenge |
| 111 | Boss warning (border pulse + sound) | Combined audiovisual cue | Anticipation |
| 112 | Integration + boss balance | Playtesting, health/damage tuning | Memorable, fair fights |

**Design Note:**
Bosses are built from multiple attribute cells — the largest "sprites" in the game. A 4×2 cell boss is 32×16 pixels with attribute colour, making it visually imposing. Phase transitions change the boss's attribute colour (e.g., green → yellow → red as health drops), giving clear visual feedback using the same system learners already understand.

**End of Phase 7:** Boss fights are the highlight. Multi-phase encounters with real drama.

---

## Phase 8: Launch (Units 113-128)

**Goal:** Commercial release quality. Everything a real 1986 Spectrum game would ship with.
**Z80 Focus:** Sorted arrays, hardware detection, menu systems, tape loading.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 113 | High score table (top 5) | Sorted array insertion, comparison | Competition |
| 114 | Initials entry (3 characters) | Character input, cursor, keyboard decode | Ownership |
| 115 | High scores shown on title | Persistent display integration | Bragging rights |
| 116 | Difficulty select (3 levels) | Menu system, cursor navigation | Accessibility |
| 117 | Difficulty affects gameplay | Parameter tables per difficulty level | Real difference |
| 118 | Extra life at 10,000 points | Threshold detection, celebration effect | Skill reward |
| 119 | Two-player alternating mode | Player state switching, turn management | Social |
| 120 | Score comparison at game over | Side-by-side display | Competition |
| 121 | Kempston joystick support | `IN` ($1F), bit mapping | Hardware access |
| 122 | Sinclair joystick support | Keyboard port remapping | More options |
| 123 | Input selection menu | Configuration, control abstraction layer | Player choice |
| 124 | Attract mode (auto-play demo) | Recorded or AI-driven input | Professional |
| 125 | Demo plays on title after timeout | Timer-triggered state change | Shop display |
| 126 | Loading screen (attribute art) | Screen data layout, tape presentation | Professional |
| 127 | Final balance + bug sweep | Systematic edge case testing | Release ready |
| 128 | **Complete game — build final binary** | SNA/TAP creation, packaging | **Ship it** |

**End of Phase 8:** A game worthy of a 1986 software house release. High scores with initials, joystick support, attract mode, two-player — the full package.

---

## Spectrum-Specific Debugging (Throughout)

**Colour Clash Issues:**
- If colours bleed: Check objects stay within attribute cell boundaries
- If objects disappear: They're same INK as PAPER
- If background corrupts: You're writing to wrong attribute address

**Screen Address Issues:**
- Screen layout is non-linear (thirds interleaved)
- Use lookup table for Y→address conversion
- `INC H` moves down within character row, not to next pixel row
- Character row boundary crossing needs special handling

**Beeper Issues:**
- If sound affects gameplay: Keep sounds SHORT (100-200 T-states)
- If no sound: Check border I/O port ($FE)
- If wrong pitch: Check inner loop count
- If sound cuts other sound: Implement priority system (Unit 95)

**Keyboard Issues:**
- Keys are active LOW (0 = pressed)
- Each half-row is a separate port address
- Multiple simultaneous keys: read each port separately
- Ghost keys possible with certain combinations

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 4 (Unit 64) | Phase 8 (Unit 128) |
|--------|-------------------|--------------------|--------------------|
| Graphics | Attribute blocks | Pixel sprites, smooth movement | Starfield, explosions, custom font |
| Enemies | One type, falls | 4+ types, formations, aimed shots | + Bosses, mini-bosses, phases |
| Player | Move + shoot | Power-ups, shield, spread shot | + Difficulty select, attract demo |
| Audio | Single beep | Varied SFX | Full beeper music, jingles, priority |
| Input | QAOP + fire | Same | + Kempston, Sinclair, selection menu |
| Modes | Single play | Same | Two-player, 3 difficulties, attract |
| Z80 skill | LD, JP, loops | Data structures, 16-bit maths | Full working knowledge |

---

## What This Teaches Beyond the Game

By completing Skyfire, learners are ready for:
- **Shatter (Game 2):** Collision → ball physics. Fixed-point movement from pre-shifted sprites.
- **Cavern (Game 3):** Pixel sprites → character movement. Screen addresses → platform levels.
- **Blitz (Game 9):** Screen memory mastery → software scrolling.
- **Every future game:** The draw routine, lookup table, and input abstraction from Skyfire are reused and extended throughout the curriculum.

Skyfire isn't just Game 1. It's the toolbox.

---

**Version:** 2.0
**Last Updated:** 2026-02-05
