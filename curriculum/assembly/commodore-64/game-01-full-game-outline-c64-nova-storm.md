# Full Game Outline: C64 Nova Storm (128 Units)

**Game:** Nova Storm (Game 1)
**Units:** 128 (8 phases × 16 units)
**Genre:** Wave-based space shooter
**Inspired by:** Katakis, Galaga, Armalyte, Delta
**Target Quality:** Commercial-grade fixed-screen shooter (1985–86 era)
**Predecessor:** Adapts and refines the Starfield outline (v2.0, 2026-02-05)

---

## Premise

The nova is coming. A dying star at the edge of the sector has sent a shockwave of debris and hostile ships ahead of it. Your interceptor is the only craft still operational. Hold the line, destroy wave after wave, and survive until the fleet evacuation completes.

Immediate engagement: ship on screen in unit 1, shooting in unit 3, SID pounding in unit 4. The C64's hardware sprites and SID chip do the heavy lifting. The learner builds a game that looks and sounds like a real C64 release because it uses the same hardware the same way.

---

## What Makes This "C64"

- **8 hardware sprites** — real movable objects, no software rendering needed
- **SID sound chip** — 3 voices with ADSR, resonant filter, ring mod
- **VIC-II video** — sprites, custom characters, raster interrupts, 16 colours
- **CIA chips** — joystick input, keyboard scanning, precision timers
- **Zero page** — 256 bytes of fast variable storage
- **$D41B** — free random numbers from the SID noise oscillator

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
| 8 (Launch) | Code optimisation, memory management, PAL/NTSC detection, distribution |

---

## Phase 1: Ignition (Units 1–16)

**Goal:** Complete game loop — shoot enemies, score points, die, restart.
**6510 Focus:** Registers, addressing modes, zero page, branches, subroutines.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 1 | BASIC stub + ship sprite on screen | `LDA`/`STA`, memory addresses, VIC-II sprite registers | See your ship |
| 2 | Joystick moves ship | `LDA $DC00`, `AND` bit mask, `BEQ`/`BNE` branches | **Control something** |
| 3 | Fire button shoots | Zero-page variables, `INC`/`DEC` | Bullet flies up |
| 4 | Laser sound (SID voice 1) | `STA $D4xx`, waveform + gate bit | Satisfying "pew" |
| 5 | One enemy sprite | Sprite enable bits (`ORA`), sprite positions | Target exists |
| 6 | Bullet hits enemy | `CMP` comparisons, coordinate distance check | **It dies!** |
| 7 | Explosion sound + sprite flash | SID noise channel, sprite colour register | Feedback |
| 8 | Score display | 16-bit `ADC` with carry, BCD/hex→decimal | See your points |
| 9 | Enemies spawn continuously | `JSR`/`RTS`, SID oscillator 3 for random ($D41B) | Challenge |
| 10 | Enemy touches ship = death | Bounding box or hardware collision ($D01E) | Stakes |
| 11 | Game over screen | Game states, screen RAM text | End state |
| 12 | Press fire to restart | State machine reset, initialisation | **Complete loop** |
| 13 | Title screen | Screen RAM + colour RAM, character output | Presentation |
| 14 | Three lives | Game state in zero page, HUD update | Forgiveness |
| 15 | Life lost flash/sound | Border flash ($D020), SID death sound | Feedback |
| 16 | Integration + edge cases | Screen boundaries, sprite X bit 8 ($D010) | Solid foundation |

**End of Phase 1:** Playable shooter with hardware sprites, SID sound, scoring, lives. A complete game loop.

---

## Phase 2: The Fleet (Units 17–32)

**Goal:** Multiple enemy types with distinct behaviours. All 8 sprite slots managed.
**6510 Focus:** Indexed addressing, lookup tables, indirect addressing.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 17 | Enemy data table (type, x, y, speed, alive) | `LDA table,X`, stride access | Organised enemies |
| 18 | Multiple enemies from table | Loop with index offset, zero-page pointer | Several on screen |
| 19-21 | Fast/slow/zigzag enemy types | Speed as data field, sine table for zigzag | Movement variety |
| 22-24 | Different sprites, colours, point values per type | Sprite pointer table, colour table, score table | Visual distinction |
| 25-28 | Wave system: composition tables, escalating spawns | Data-driven waves, counter-based triggers | Structure |
| 29-30 | Sprite priority and X high bit | $D01B, $D010 bit manipulation | Correctness |
| 31 | Hardware collision detection | $D01E sprite-sprite, $D01F sprite-background | C64 advantage |
| 32 | Integration + balance tuning | Playtesting, wave composition | Feels fair |

**Key Teaching Moment (Unit 17):** Stride-based table access. Each enemy uses 5 bytes. `LDA enemy_table,X` with X as the stride offset gives struct-like access. This pattern underpins every C64 game from here on.

**End of Phase 2:** Varied enemies, wave system, all 8 sprite slots active. Sprite system understood deeply.

---

## Phase 3: Firepower (Units 33–48)

**Goal:** Power-ups, weapon upgrades, sprite allocation strategy.
**6510 Focus:** Bit manipulation, 16-bit arithmetic, stack operations.

Power-ups (speed boost, rapid fire, double shot, spread shot, shield) are dropped by killed enemies, reusing the dead enemy's sprite slot. The 8-sprite limit forces design discipline: player(1) + bullet(1) + enemies(6) is already full. Adding power-ups means smart slot management.

**End of Phase 3:** Weapon variety, meaningful choices, the 8-sprite limit as design constraint.

---

## Phase 4: Incoming (Units 49–64)

**Goal:** Enemies shoot back. Raster interrupts for stable timing and colour effects.
**6510 Focus:** Interrupts (SEI/CLI), IRQ vector, raster register, hardware timing.

The most important phase in the C64 curriculum. Raster interrupts are introduced for frame timing (Unit 56-57), then used for colour effects (Unit 58). The SID's $D41B provides free random numbers for enemy fire timing. Enemy bullets share sprite slots with player bullets via allocation cycling.

**Key Teaching Moment (Unit 56):** Raster interrupts — the VIC-II triggers an IRQ at a specific scanline. Your code runs at *exactly* that moment. This enables stable frame timing, colour effects, and (in Phase 7) sprite multiplexing. Every serious C64 game uses them.

**End of Phase 4:** Two-way combat with raster-stable timing. Colour bar in the border proves the technique.

---

## Phase 5: Stardust (Units 65–80)

**Goal:** Visual polish — custom characters, multicolour sprites, raster effects.
**6510 Focus:** Character set manipulation, VIC bank switching, colour RAM.

The parallax starfield (custom character animations at different speeds), multicolour sprites ($D01C, $D025/$D026), explosion animations, and raster colour splits transform the game's look to commercial standard.

**End of Phase 5:** Multicolour sprites, parallax starfield, raster colour effects. Looks like a real C64 game.

---

## Phase 6: Waveform (Units 81–96)

**Goal:** Full SID soundtrack — the chip that defined a generation.
**6510 Focus:** SID register architecture, ADSR envelopes, filter, CIA timer-driven music.

Three-voice music with CIA timer-driven playback. Filter sweeps on explosions. Sound priority system (SFX temporarily steal a voice, restore it cleanly). Title music, game-over jingle, wave-complete fanfare.

**Key Teaching Moment (Unit 93):** The SID's resonant filter. Low-pass, high-pass, band-pass modes. Sweep the cutoff frequency during an explosion: that unmistakable C64 sound. The filter is what makes the SID *the SID*.

**End of Phase 6:** Three-voice music, filter sweeps, punchy effects. The SID sings.

---

## Phase 7: Command (Units 97–112)

**Goal:** Boss fights with sprite multiplexing.
**6510 Focus:** Raster-precise timing, sprite multiplexing algorithm, state machines.

Boss enemies built from 4 sprites (the boss) + player + bullets exceed 8 slots. Sprite multiplexing reuses slots at different Y positions via raster interrupts. Multi-phase boss patterns (idle → telegraph → attack → recover). Boss health bar, phase transitions at 50% health.

**Key Teaching Moment (Unit 102):** Sprite multiplexing — once a sprite is drawn (beam past its last scanline), repoint its position and data pointer via raster IRQ. The same slot displays twice. This is how Armalyte displays dozens of sprites with 8 hardware slots.

**End of Phase 7:** Multi-phase boss encounters powered by sprite multiplexing. The game's highlight.

---

## Phase 8: Launch (Units 113–128)

**Goal:** Commercial release quality. Ship it.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 113-115 | High score table with initials | Multi-byte sort, keyboard matrix | Competition |
| 116-117 | Difficulty select (3 levels) | Menu, parameter tables | Accessibility |
| 118 | Extra life at 10,000 points | Threshold, celebration | Skill reward |
| 119-120 | Two-player alternating | State switching, score comparison | Social play |
| 121-122 | Attract mode + demo on title timeout | Recorded input, timer trigger | Professional |
| 123 | PAL/NTSC detection | CIA timer comparison | Platform correct |
| 124 | Continue option (wave restart) | Limited continues | Forgiveness |
| 125 | Loading screen | Character art | Presentation |
| 126 | Credits | Text with colour effects | Professional |
| 127 | Final balance + bug sweep | Systematic testing | Release quality |
| 128 | **Complete game — final .prg** | Packaging, autostart | **Ship it** |

---

## C64-Specific Debugging

**Sprites:** Check $D015 (enable), $07F8+ (data pointer), $D010 (X high bit), $D01C (multicolour), $D01B (priority).

**VIC-II:** Check VIC bank ($DD00), screen/charset pointer ($D018), colour RAM ($D800+).

**SID:** Check gate bit (bit 0 of control register), ADSR release, 16-bit frequency, filter routing ($D417), volume ($D418).

**Raster:** Check $D01A (enable), IRQ vector, acknowledge via $D019, stabilise with NOP slide.

**6510:** Save A/X/Y in interrupt handler. Use zero page for hot variables. Use port 2 ($DC00) for joystick.

---

## What This Teaches Beyond the Game

Nova Storm is the C64 foundation. Every technique transfers:
- **Coldframe (Game 2):** Sprite management → large character animation. Raster timing → scrolling. SID → atmosphere.
- **Warfront (Game 3):** Multiplexing → 16+ sprites. Character sets → scrolling terrain. CIA timers → music during action.
- **Capstone (Game 4):** Everything combined, plus fast loader, drive programming, demo-scene effects.

---

## Detailed Phase Breakdowns

The predecessor outline (`game-01-full-game-outline-c64-starfield.md`) contains per-unit detail for all 8 phases, including code examples, debugging guides, and key teaching moments. Nova Storm follows the same structure with updated naming. Refer to the Starfield outline for the complete unit-by-unit breakdown.

---

## Changelog

- **v1.0 (2026-03-09):** Initial outline. Adapts Starfield (v2.0) to the restructured 4-game curriculum as Nova Storm. Same genre, same 6510 progression, updated naming and cross-references.
