# Full Game Outline: NES Stellar Barrage (128 Units)

**Game:** Stellar Barrage (Game 1)
**Units:** 128 (8 phases × 16 units)
**Target Quality:** Commercial-grade fixed-screen shooter (1985-86 era)
**Comparable To:** Galaxian, Galaga → evolving to Gun Nac, Crisis Force-level polish by completion

---

## What Makes This "NES"

The NES has:
- **Two-chip architecture** — CPU and PPU are separate chips; you talk to the PPU through registers, not shared memory
- **Tile-based everything** — backgrounds are a 32×30 grid of 8×8 tiles; sprites are 8×8 or 8×16 tiles
- **CHR ROM** — graphics baked into the cartridge. Tile design is a first-class concern, not an afterthought
- **64 hardware sprites** — generous count, but only 8 per scanline (flickering is a technique, not a bug)
- **VBlank discipline** — PPU updates only during ~2,273 CPU cycles of vertical blank. Miss the window, corrupt the screen
- **NMI-driven game loop** — the PPU fires NMI every frame; the game breathes at 60 Hz
- **APU sound** — 2 pulse + 1 triangle + 1 noise + 1 sample channel, each with distinct character
- **ca65/ld65 toolchain** — segments, linker config, and the iNES header define the cartridge format

This shooter teaches the tile-based mindset. Where C64 programmers think in sprites and rasters, and Spectrum programmers think in pixels and attributes, NES programmers think in tiles and VBlank. The PPU does the heavy lifting — your job is to set up the right tiles, then tell the PPU where to put them. The 8-per-scanline limit forces smart flickering. The APU gives that unmistakable NES sound. The result is a cartridge that feels like it came from 1986 Konami or Capcom.

---

## Design Philosophy

- **One concept per unit** — never overwhelming
- **Always playable** — from Unit 2 onwards
- **Debugging inline** — every unit includes "if it doesn't work"
- **6502/ca65 skill per unit** — assembly concepts build alongside the game
- **PPU separation central** — understanding the CPU/PPU boundary is THE NES skill
- **VBlank discipline from Unit 1** — PPU writes only during VBlank, always
- **APU sound from Unit 4** — not silent until late game
- **Mapper 0 (NROM)** — 32KB PRG-ROM + 8KB CHR-ROM, no bank switching (simplest cartridge hardware)
- **Commercial quality by Unit 128** — a real game

---

## 6502 Assembly Progression

| Phase | 6502/ca65 Focus |
|-------|-----------------|
| 1 (Power On) | Registers (A/X/Y), zero page, LDA/STA, ca65 segments, PPU register protocol, NMI handler |
| 2 (Pattern Table) | Indexed addressing (LDA table,X), loops (DEX/BNE), CHR tile data format, nametable writes |
| 3 (Arsenal) | Bit manipulation (AND/ORA/EOR), 16-bit arithmetic (ADC/SBC with carry), subroutine patterns |
| 4 (Barrage) | Object pools, OAM cycling algorithm, comparison chains (CMP/BCS/BCC), flag management |
| 5 (Scanline) | Indirect addressing, VBlank budgeting, Sprite 0 hit technique, timed palette updates |
| 6 (Five Channels) | APU register architecture, timer-based sequence playback, channel stealing |
| 7 (Metasprite) | Composite entity tables, sorted OAM, complex state machines, multi-phase patterns |
| 8 (Cartridge) | Code optimisation, NTSC/PAL detection, iNES header options, memory layout mastery |

By Unit 128, learners have a working knowledge of the 6502 instruction set, PPU graphics, APU audio, and the VBlank-disciplined approach that defines NES development.

---

## Phase 1: Power On (Units 1-16)

**Goal:** Complete game loop — shoot enemies, score points, die, restart.
**6502 Focus:** Registers, addressing modes, zero page, PPU register protocol, NMI basics.
**Startup reality:** Getting anything on screen requires more setup than other platforms. The iNES header, PPU warmup (2 VBlanks), NMI handler, and OAM DMA must all be in place before a single sprite appears. This phase builds the framework every NES game needs.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 1 | iNES header + PPU warmup + one sprite | ca65 `.segment`, iNES header bytes, `LDA`/`STA` | See your ship |
| 2 | Controller moves ship | Read `$4016` (strobe + serial), `AND` bit mask, `BEQ`/`BNE` | **Control something** |
| 3 | A button shoots | Zero-page variables, `INC`/`DEC`, OAM buffer writes | Bullet flies up |
| 4 | Laser sound (pulse channel) | `STA $4000`-`$4003`, duty cycle + timer concept | Satisfying "pew" |
| 5 | One enemy sprite | Multiple OAM entries, sprite tile selection | Target exists |
| 6 | Bullet hits enemy | `CMP` distance checks, coordinate subtraction | **It dies!** |
| 7 | Explosion sound (noise channel) | `$400C`-`$400F`, noise period + length counter | Feedback |
| 8 | Score display (nametable tiles) | `$2006`/`$2007` writes during VBlank, number→tile index | See your points |
| 9 | Enemies spawn continuously | `JSR`/`RTS` subroutines, simple PRNG (LFSR in zero page) | Challenge |
| 10 | Enemy touches ship = death | Bounding box collision, signed comparison | You can die |
| 11 | Game over screen | Nametable writes, game state variable | End state |
| 12 | Start button restarts | Button edge detection (new press vs held), state reset | **Complete loop** |
| 13 | Title screen (nametable layout) | Full nametable write during rendering-off, attribute table | Feels real |
| 14 | Three lives | Game state in zero page, HUD tile update | Forgiveness |
| 15 | Life lost effect (palette flash) | Palette write during VBlank, timed restore | Feedback |
| 16 | Integration + edge cases | Screen boundary checks, hiding unused sprites (Y=`$FF`) | Solid foundation |

**NES-Specific Unit 1:**
```asm
.segment "HEADER"
.byte "NES", $1A        ; iNES magic number
.byte $02               ; 2 × 16KB PRG-ROM = 32KB
.byte $01               ; 1 × 8KB CHR-ROM
.byte %00000001         ; Vertical mirroring, mapper 0 (NROM)
.byte $00               ; No battery

.segment "CODE"
Reset:
    SEI                 ; Disable interrupts
    CLD                 ; Clear decimal (no effect on NES, good practice)
    LDX #$FF
    TXS                 ; Set stack pointer

    ; PPU warmup — MUST wait 2 VBlanks before touching PPU
:   BIT $2002
    BPL :-              ; First VBlank
:   BIT $2002
    BPL :-              ; Second VBlank — PPU now stable

    ; Load palettes
    LDA $2002           ; Reset PPU address latch
    LDA #$3F
    STA $2006           ; PPUADDR high byte
    LDA #$00
    STA $2006           ; PPUADDR low byte ($3F00)
    LDX #$00
:   LDA palette_data,X
    STA $2007           ; Write palette entry
    INX
    CPX #$20            ; 32 bytes (4 BG + 4 sprite palettes)
    BNE :-

    ; Set up sprite 0 (ship) in OAM buffer at $0200
    LDA #$C0
    STA $0200           ; Y position
    LDA #$01
    STA $0201           ; Tile index (from CHR ROM)
    LDA #$00
    STA $0202           ; Attributes (palette 0, no flip)
    LDA #$78
    STA $0203           ; X position (centred)

    ; Enable NMI and rendering
    LDA #%10000000
    STA $2000           ; PPUCTRL: NMI on
    LDA #%00011110
    STA $2001           ; PPUMASK: show sprites + background

Forever:
    JMP Forever         ; NMI handler does the work

NMI:
    PHA                 ; Save A
    LDA #$00
    STA $2003           ; Set OAM address
    LDA #$02
    STA $4014           ; OAM DMA from $0200 (513 cycles)
    PLA                 ; Restore A
    RTI

.segment "VECTORS"
.word NMI               ; $FFFA — NMI vector
.word Reset             ; $FFFC — RESET vector (mandatory)
.word 0                 ; $FFFE — IRQ vector (unused)

.segment "CHARS"
    ; 8KB of tile graphics: ship, enemies, font...
```

**If it doesn't work (Unit 1):**
- **Black screen?** Check `$2001` (rendering enabled), `$2000` (NMI enabled). Did you wait for 2 VBlanks before touching the PPU?
- **No sprite?** Check OAM data at `$0200`+. Check OAM DMA in NMI (`$4014`). Is `$2003` set to 0 before DMA?
- **Wrong position?** Y is byte 0, X is byte 3 (counterintuitive). Y values >`$EF` hide the sprite.
- **Wrong colours?** Sprite palettes start at `$3F10`. Colour 0 in sprite palettes is always transparent.
- **Assembler errors?** Check ca65 segment names match your `nes.cfg` linker config.
- **ROM doesn't load?** Check iNES header bytes — wrong PRG/CHR count means the emulator reads garbage.

**End of Phase 1:** Playable NES shooter. The boilerplate is done — iNES header, NMI handler, OAM DMA, palette loading, VBlank discipline — and every unit from here builds on this framework.

---

## Phase 2: Pattern Table (Units 17-32)

**Goal:** Multiple enemy types with distinct tile graphics. CHR ROM design becomes a first-class skill.
**6502 Focus:** Indexed addressing, loops, CHR tile data format, nametable calculations.
**Key concept:** On the NES, visual variety comes from tile design in CHR ROM. Each enemy type gets unique tiles — there's no "recolour the same sprite shape" shortcut like on C64. The NES has only 4 sprite palettes, so tile shape IS identity.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 17 | Enemy data table (type, x, y, speed, alive) | `LDA table,X` with stride offset, indexed addressing | Organised enemies |
| 18 | Multiple enemies from table | Loop with `DEX`/`BNE`, zero-page pointer | Several on screen |
| 19 | Fast enemy (dives down, unique tile) | Speed as data field, CHR tile design decisions | Variety begins |
| 20 | Slow enemy (drifts sideways, unique tile) | Combined X+Y velocity from table | Pacing contrast |
| 21 | Zigzag enemy (weaves, unique tile) | Direction toggle or sine table lookup | Movement patterns |
| 22 | Sprite palette selection per type | OAM attribute byte bits 0-1 (palettes 0-3) | Colour coding |
| 23 | Different point values per type | Score lookup table, indexed access | Risk/reward |
| 24 | Wave system (clear all = next wave) | Enemy alive counter, state transitions | Structure |
| 25 | Wave composition tables | Data-driven wave definitions (type mix, count) | Varied challenge |
| 26 | Faster spawning each wave | Timer adjustment per wave, difficulty ramp | Escalation |
| 27 | Wave display (nametable HUD update) | Nametable row write during VBlank | Progress visible |
| 28 | Enemy spawn sound (pulse 2) | `$4004`-`$4007`, short pitch sweep | Audio feedback |
| 29 | Wave start jingle (triangle) | `$4008`-`$400B`, triangle channel basics | Punctuation |
| 30 | Brief pause between waves | Frame counter delay, state machine transition | Breathing room |
| 31 | CHR tile design workflow | Pattern table format (2 bitplanes, 16 bytes/tile) | **Tile literacy** |
| 32 | Integration + balance | Wave composition tuning, tile and palette audit | Feels fair |

**Key Teaching Moment (Unit 17):**
The 6502 doesn't have structs. You fake them with a single table and stride access. If each enemy uses 5 bytes (type, x, y, speed, alive), enemy 0 starts at offset 0, enemy 1 at offset 5, enemy 2 at offset 10. `LDA enemy_table,X` with X set to the right multiple gives you struct-like access. This pattern underpins every NES game.

**Key Teaching Moment (Unit 31):**
NES tiles are 8×8 pixels, 2 bits per pixel (4 colours from a palette). Each tile is 16 bytes: 8 bytes for bitplane 0, then 8 bytes for bitplane 1. The pixel value is `(plane1_bit << 1) | plane0_bit`, indexing into the selected palette. This format is counterintuitive — you design each tile as two separate layers that combine. Understanding the raw CHR format means you can debug tile corruption, plan your tile budget (256 tiles per pattern table), and modify graphics through tooling. Every NES game lives or dies by its tile design.

**End of Phase 2:** Varied, escalating challenge. Each enemy type has unique tiles and behaviour. The learner thinks in tiles naturally.

---

## Phase 3: Arsenal (Units 33-48)

**Goal:** Power-ups make the player stronger. OAM buffer management becomes strategic.
**6502 Focus:** Bit manipulation (AND/ORA/EOR), 16-bit arithmetic (ADC/SBC with carry), subroutine design.
**Key challenge:** The NES has 64 sprite slots but only 8 visible per scanline. Power-up items, extra bullets, and shield overlays all consume OAM entries — and when they share scanlines with enemies, priority matters.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 33 | Power-up drops from killed enemies | OAM slot allocation routine, `JSR` | Collectibles exist |
| 34 | Collect power-up = effect | `AND`/`ORA` for state flags, `JSR` to effect handler | System works |
| 35 | Speed boost power-up | Temporary state with frame countdown in zero page | Agility |
| 36 | Rapid fire power-up | Fire rate as variable, `DEC` timer per frame | Firepower |
| 37 | Power-up collect sound (triangle) | `$4008`-`$400B`, short melodic ping | Satisfying |
| 38 | Power-up visibility (palette cycling) | Palette update during VBlank, frame-based cycle | Eye-catching |
| 39 | Power-ups are temporary (timer) | 16-bit countdown with `SBC` and carry chain | Strategic decisions |
| 40 | Timer display via HUD tiles | Nametable tile update for countdown digits | Know when it ends |
| 41 | Double shot (two OAM sprites) | Bullet pool array, paired allocation | Coverage |
| 42 | Spread shot (three directions) | Velocity tables for angle offsets, `LDA table,X` | Screen control |
| 43 | Shield (one free hit) | State flag in zero page, bit flag checking | Defensive option |
| 44 | Shield sprite overlay | Additional OAM entry layered on player position | See protection |
| 45 | Shield break effect + sound | OAM removal + palette flash + noise burst | Feedback |
| 46 | Power-up frequency tuning | Probability per kill, wave-dependent drop rates | Balance |
| 47 | No power-ups in Wave 1 | Wave number comparison before drop check | Earned, not given |
| 48 | Integration + balance | OAM allocation audit, power-up playtesting | Rewarding loop |

**NES-Specific:**
- Power-up items are sprites — they count against the 64-sprite total and 8-per-scanline limit
- Palette cycling for visibility must happen during VBlank (palette RAM is PPU memory, no mid-frame access)
- Shield = additional OAM sprite overlaid on the player's position (same tile, different palette for colour shift)
- The NES's 4 sprite palettes colour-code power-up types without needing different tiles

**End of Phase 3:** Power-ups feel great and add strategy. The learner manages the OAM buffer confidently.

---

## Phase 4: Barrage (Units 49-64)

**Goal:** Enemies shoot back. The 8-per-scanline limit hits hard and sprite flickering becomes essential.
**6502 Focus:** Object pools, OAM priority cycling, comparison chains, flag-based logic.
**Key moment:** When enemy bullets, player bullets, enemies, and the player all occupy the same scanlines, sprites vanish. This isn't a bug — it's the PPU's 8-per-scanline hardware limit. Flickering (rotating OAM order each frame) is the standard professional solution, and this is where learners build it.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 49 | Enemy bullet (one at a time) | Bullet pool pattern, OAM slot reuse | Danger from above |
| 50 | Enemy bullet tile | Distinct CHR tile from player bullets | Clear visual threat |
| 51 | Enemy bullet hits player | Shared collision subroutine (generic, reusable) | Real danger |
| 52 | Enemy fire sound (noise channel) | `$400C`-`$400F`, short noise burst | Audio warning |
| 53 | Random enemy fires | LFSR pseudo-random, probability via `AND` mask | Unpredictable |
| 54 | Shooter enemy type (fires aimed) | Direction calculation via subtraction | Smart enemies |
| 55 | Shooter worth more points | Type-based score lookup | Risk/reward |
| 56 | Multiple enemy bullets (pool of 4) | Pool allocation and recycling | Intensity |
| 57 | Bullet speed varies by wave | Wave-indexed parameter table | Escalation |
| 58 | Aimed vs random shot mix | Probability table, difficulty scaling | Variety |
| 59 | The 8-per-scanline problem | Analysis: count sprites on busy scanlines, observe vanishing | Understanding the limit |
| 60 | **Sprite flickering system** | OAM starting-index rotation per frame | **The NES technique** |
| 61 | Shoot enemy bullets (bullet-bullet collision) | Extended collision checks | Skill option |
| 62 | Death = all bullets cleared | Sprite hide routine (Y=`$FF` for all enemy bullets) | Fair restart |
| 63 | Bullet density tuning | Max bullet count, fire rate caps per wave | Balance |
| 64 | Integration + combat balance | Full playtesting with flickering active | Challenging but fair |

**Key Teaching Moment (Units 59-60):**
The PPU renders up to 8 sprites per scanline. The 9th and beyond don't appear that frame. When a wave of enemies fires downward and your bullets fly upward through the same scanline, something disappears. The professional solution: rotate the starting OAM index each frame. Frame 1 begins rendering from sprite 0; frame 2 from sprite 8; frame 3 from sprite 16. This distributes which sprites get hidden across frames, so everything flickers evenly rather than some sprites permanently vanishing. Every commercial NES shooter does this — from Gradius to Contra. The flicker IS the NES aesthetic. Players from 1986 never questioned it because every game behaved the same way.

**End of Phase 4:** Proper two-way combat. Sprite flickering handles busy screens professionally. The game feels like a real NES shooter.

---

## Phase 5: Scanline (Units 65-80)

**Goal:** Visual polish to commercial standard using NES-specific techniques.
**6502 Focus:** Indirect addressing, VBlank budgeting, Sprite 0 hit, palette/nametable timing.
**Key techniques:** The NES achieves visual richness through tile tricks — animated backgrounds, palette cycling, attribute table colour zones, and Sprite 0 hit for mid-frame effects. There's no framebuffer to manipulate; everything is tile choreography.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 65 | Starfield background (nametable tiles) | Background tile placement via `$2006`/`$2007` | Depth |
| 66 | Animated stars (tile swap in VBlank) | Selective `$2007` writes, VBlank byte budget (~440 max) | Motion |
| 67 | Multiple star types and speeds | Different tiles, different update frequencies | Variety |
| 68 | Explosion animation (multi-frame sprite) | OAM tile index cycling, frame counter | Impact |
| 69 | Multi-frame explosion sequence | Sprite tile + palette change per frame | Drama |
| 70 | Player death animation | Scripted multi-frame sequence, brief invincibility | Stakes |
| 71 | Screen flash (palette manipulation) | Full palette overwrite during VBlank, timed restore | Emphasis |
| 72 | Enemy spawn animation (flicker-in) | OAM Y-toggle for appear/disappear effect | Polish |
| 73 | Attribute table colour zones | Attribute table layout (16×16 pixel granularity) | Colour regions |
| 74 | Colour themes per wave group | Palette swap during VBlank, wave-indexed palette data | Visual variety |
| 75 | Custom title screen tiles | Full nametable + attribute table layout | Presentation |
| 76 | Palette cycling on title | Frame-driven palette rotation during VBlank | Attract mode flair |
| 77 | **Sprite 0 hit for status bar** | `$2002` bit 6 polling, mid-frame timing | **NES split-screen** |
| 78 | HUD isolated from game palette | Sprite 0 boundary, palette change after hit | Clean separation |
| 79 | Score flash on increase | Temporary HUD palette change, timed restore | Feedback |
| 80 | Integration + visual consistency | Tile audit, palette harmony, VBlank budget check | Looks professional |

**Key Teaching Moment (Unit 77):**
Sprite 0 hit is the NES technique for knowing when the PPU reaches a specific scanline. You place sprite 0 at the boundary between your HUD and the game area. When the PPU draws that sprite overlapping a non-transparent background pixel, bit 6 of `$2002` is set. Your code polls for this, then performs mid-frame changes — typically resetting scroll position to separate a fixed HUD from a scrolling game area. In Stellar Barrage (fixed screen), we use it to isolate the HUD palette from game-area palette changes. This technique is fundamental for every scrolling NES game that follows.

**Key Teaching Moment (Unit 66):**
CHR ROM tiles are baked into the cartridge — you can't modify them at runtime (no CHR RAM on NROM). But you can change WHICH tiles appear WHERE by writing to the nametable during VBlank. Animated stars work by cycling which tile index each star position uses. The VBlank budget is tight: ~2,273 CPU cycles minus OAM DMA (513) leaves ~1,760 cycles, enough for roughly 440 bytes of `$2007` writes. Plan your per-frame updates to fit this budget.

**End of Phase 5:** The game looks like a real NES cartridge. Animated starfield, palette effects, clean HUD, cohesive tile design.

---

## Phase 6: Five Channels (Units 81-96)

**Goal:** Full APU soundtrack and rich sound design — that distinctive NES sound.
**6502 Focus:** APU register architecture, timer-based sequence playback, channel management.
**Pacing reality:** Building a proper sound engine takes time. This phase builds incrementally from individual channel mastery to a reusable music/SFX sequencer.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 81 | APU architecture overview | Register map (`$4000`-`$4017`), 5-channel structure | Understanding the chip |
| 82 | Pulse channel deep dive | Duty cycle, timer (pitch), length counter, envelope | Shaped tones, not bleeps |
| 83 | Sound effect library (pulse-based) | Parameterised SFX routine (channel, pitch, envelope) | Varied effects |
| 84 | Replace placeholder sounds | Integrate crafted SFX throughout game | Cohesive audio |
| 85 | Triangle channel | `$4008`-`$400B`, linear counter, always full volume | Bass and melody |
| 86 | Noise channel deep dive | `$400C`-`$400F`, mode bit (metallic vs hiss), period | Percussion and SFX |
| 87 | Improved explosion/gunshot sounds | Noise with short period sweeps, envelope shaping | Punchy audio |
| 88 | Note frequency table | Lookup table: note name → timer value per channel | Musical scale |
| 89 | Simple sequence player | Note + duration arrays, frame-based advancement | Music possible |
| 90 | Title screen music (2 channels) | Pulse 1 melody + pulse 2 harmony | Atmosphere |
| 91 | Three-channel music | Triangle bass line added to title theme | **Full NES sound** |
| 92 | Music stops on game start | State-controlled playback, clean channel silence | Transition |
| 93 | Game over jingle | Short descending phrase (all 3 channels) | Punctuation |
| 94 | Wave complete + high score jingles | Distinct short celebratory phrases | Achievement |
| 95 | SFX over music (channel stealing) | SFX temporarily takes Pulse 2 or Noise, music resumes | No ugly cutoff |
| 96 | Integration + audio balance | Volume levels, SFX priority, music pacing | Sounds great |

**APU-Specific:**
- **Pulse 1 + 2** carry melody and harmony — 4 duty cycle settings give tonal variety (12.5%, 25%, 50%, 75%)
- **Triangle** provides bass — always full volume (no envelope), so it's pure and clean
- **Noise** handles percussion and explosions — short mode gives metallic hits, long mode gives white noise
- **DMC** (sample channel) is deliberately NOT used in this game — it causes controller read corruption when DPCM DMA steals CPU cycles from `$4016` reads. Better saved for later games when learners can handle the workaround
- SFX typically steal Pulse 2 or Noise, letting Pulse 1 melody and Triangle bass continue uninterrupted
- The APU's hardware envelope generator and length counter handle note shaping automatically — less CPU work than the Spectrum's beeper or the Amiga's Paula sequencing

**End of Phase 6:** That distinctive NES sound throughout. Three-channel music on the title screen, punchy crafted effects, clean channel management with SFX-over-music working smoothly.

---

## Phase 7: Metasprite (Units 97-112)

**Goal:** Boss fights using multi-tile composite sprites — the standard NES technique for large entities.
**6502 Focus:** Composite entity tables, sorted OAM writes, complex state machines.
**Key concept:** NES sprites are 8×8 (or 8×16) pixels. A boss needs to be bigger. Metasprites are groups of individual sprites positioned together from a shared origin. A 2×2 boss uses 4 OAM entries; a 4×2 boss uses 8 — an entire scanline's worth.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 97 | Mini-boss every 3 waves | Conditional trigger on wave count | Early taste |
| 98 | Mini-boss: tough enemy (3 hits) | Hit counter, damage state tracking | Tougher target |
| 99 | Mini-boss movement pattern | Simple pattern table (left-right-dive sequence) | Distinct behaviour |
| 100 | **Metasprite system** | Offset table (dx, dy, tile, attr per sub-sprite) | **Composite sprites** |
| 101 | Boss every 5 waves (2×2 metasprite) | 4 OAM entries positioned from single origin | Large enemy |
| 102 | Boss movement (sweep pattern) | Complex pattern table with timing data | Menacing behaviour |
| 103 | Boss health bar (nametable tiles) | Gradual tile depletion in HUD row | Visible progress |
| 104 | Boss takes hits | Hit detection against metasprite bounding box | Endurance |
| 105 | Boss hit flash (palette swap) | Alternate sprite palette during VBlank, timed restore | Feedback |
| 106 | Boss shoots (spread pattern) | Multiple bullet spawn positions from boss origin | Dangerous |
| 107 | Boss phase 2 at 50% health | State machine transition, faster/different pattern | Escalation |
| 108 | Boss death (chain explosion) | Scripted multi-sprite explosions across metasprite area | Payoff |
| 109 | Boss defeat bonus + jingle | Score reward, distinct audio celebration | Triumph |
| 110 | Second boss type (different tiles, pattern) | Metasprite data table swap, same rendering system | Variety |
| 111 | Boss warning sound + visual | Combined audio cue + palette pulse | Anticipation |
| 112 | Integration + boss balance | Health/damage tuning, OAM flickering under load | Memorable, fair fights |

**Key Teaching Moment (Unit 100):**
Metasprites are the NES answer to large game objects. You define a table of offsets: `(dx, dy, tile, attribute)` for each sub-sprite relative to an origin point. To draw, iterate the table and write each sub-sprite to the OAM buffer at `origin_x + dx`, `origin_y + dy`. To move the whole entity, just move the origin. This system scales from a 2×2 boss (4 sprites) to huge entities, and it's the same system used by every commercial NES game from Super Mario Bros to Mega Man.

**Key Teaching Moment (Unit 112):**
Boss fights stress the 8-per-scanline limit hardest. A 2×2 boss uses 4 sprites across 2 scanlines. Add the player (1 sprite), player bullets (1-3), and enemy bullets — and those scanlines overflow. The flickering system from Phase 4 earns its keep here. Professional NES games accept the flicker; it's part of the platform's character. Games like Contra and Gradius flicker constantly during boss fights, and nobody minded because it meant more action on screen.

**End of Phase 7:** Boss fights are the highlight. Metasprites look impressive, and the OAM flickering system handles the pressure gracefully.

---

## Phase 8: Cartridge (Units 113-128)

**Goal:** Commercial release quality. A .NES ROM worthy of a 1986 cartridge.
**6502 Focus:** Code optimisation, NTSC/PAL timing, memory layout, iNES configuration.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 113 | High score table (top 5) | Sorted array insertion, multi-byte comparison | Competition |
| 114 | Initials entry (3 characters) | Controller-based character selection, cursor logic | Ownership |
| 115 | High scores on title screen | Nametable layout integration, VBlank writes | Bragging rights |
| 116 | Attract mode (auto-play demo) | Recorded input playback or simple AI driver | Professional |
| 117 | Demo plays on title after timeout | Timer-triggered state transition | Shop display |
| 118 | Two-player alternating mode | Player state switching, turn management | Social |
| 119 | Score comparison at game over | Side-by-side nametable display | Competition |
| 120 | Difficulty select (3 levels) | Menu system, D-pad cursor navigation | Accessibility |
| 121 | Difficulty affects gameplay | Parameter tables indexed by difficulty | Real difference |
| 122 | Extra life at 10,000 points | Threshold detection, celebration effect + jingle | Skill reward |
| 123 | Extra life 1-UP sound | Distinct audio cue, brief invincibility flash | Feedback |
| 124 | NTSC/PAL timing detection | Frame rate measurement, speed adjustment tables | Platform correct |
| 125 | Continue option (wave restart) | Limited continues, score penalty | Forgiveness |
| 126 | Credits screen | Nametable text layout, palette effects | Professional |
| 127 | Final balance + bug sweep | Systematic edge case testing, VBlank budget audit | Release ready |
| 128 | **Complete game — final .NES ROM** | iNES header verification, clean build, nes.cfg audit | **Ship it** |

**End of Phase 8:** A game you could burn to a cartridge and play on real NES hardware. High scores with initials, attract mode, two-player, difficulty select — the full commercial package.

---

## NES-Specific Debugging (Throughout)

**Black Screen Issues:**
- `$2001` not set — rendering is off (check PPUMASK bits 3 and 4)
- `$2000` NMI not enabled — game loop never runs (check PPUCTRL bit 7)
- PPU warmup skipped — must wait for 2 VBlanks before any PPU access
- Palette all black — check palette data loaded correctly at `$3F00`+
- Wrong linker config — check `nes.cfg` segment definitions match ca65 source

**Sprite Issues:**
- OAM DMA not in NMI handler — check `$4014` write happens every frame
- Y position >`$EF` hides sprite — intentional feature, common trap for beginners
- Tile index wrong — check CHR ROM contents match expected indices
- Sprites vanishing — 8-per-scanline limit, implement flickering (Phase 4)
- Sprite 0 hit won't trigger at X=255 — hardware bug, use 254 or less

**Nametable Issues:**
- Garbled background — PPU address latch not reset (always read `$2002` before `$2006` writes)
- Wrong tiles displayed — check pattern table selection in PPUCTRL bit 4
- Wrong background colours — attribute table error (each byte covers 4×4 tiles in 2×2 groups)
- Corruption mid-screen — writing to PPU outside VBlank while rendering is enabled

**Controller Issues:**
- No input detected — strobe sequence wrong (must write `$01` then `$00` to `$4016`)
- Wrong button triggers action — buttons read in fixed order: A, B, Select, Start, Up, Down, Left, Right
- Random phantom presses — if using DMC audio, DPCM DMA corrupts controller reads. Read twice and compare

**Build/Toolchain Issues:**
- Linker errors — check `nes.cfg` defines all segments used in `.segment` directives
- ROM doesn't boot in emulator — RESET vector at `$FFFC` must point to valid code
- Wrong ROM size in emulator — iNES header PRG/CHR byte counts don't match actual data
- CHR tiles garbled — check `.segment "CHARS"` placement and that tile data is 16 bytes per tile

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 4 (Unit 64) | Phase 8 (Unit 128) |
|--------|-------------------|--------------------|--------------------|
| Graphics | Basic sprites, blank background | Varied enemy tiles, palette-coded types | Animated starfield, metasprite bosses, Sprite 0 HUD |
| Enemies | One type, falls | 4+ types, aimed shots, sprite flickering active | + Bosses with phases, metasprites, chain explosions |
| Player | Move + shoot | Power-ups, shield, spread shot | + Difficulty select, attract demo |
| Audio | Pulse "pew" + noise "boom" | Varied SFX, wave jingle, spawn sounds | Full 3-channel music, crafted SFX, priority system |
| Input | D-pad + A button | + Button edge detection | + Menu navigation, 2-player alternating |
| Modes | Single play | Same | Two-player, 3 difficulties, attract mode |
| 6502 Skill | LDA, STA, branches, PPU basics | Object pools, OAM cycling, flickering | Metasprites, sound engine, full PPU/APU mastery |

---

## What This Teaches Beyond the Game

By completing Stellar Barrage, learners are ready for:
- **Crate Escape (Game 2):** OAM management → character platformer sprites. Nametable tile layout → level design. Controller reading → variable-height jumps.
- **Fracture Point (Game 3):** CHR tile design → breakout block grid. Collision detection → ball physics. HUD tiles → score and lives display.
- **Ion Trail (Game 9):** Sprite 0 hit → proper scrolling split. Nametable writes → streaming level data. VBlank budgeting → smooth scroll updates.
- **Every future game:** The NMI handler, OAM DMA pattern, VBlank write discipline, sprite flickering system, metasprite renderer, and sound engine from Stellar Barrage are reused and extended throughout the curriculum.

Stellar Barrage isn't just Game 1. It's the cartridge template.

---

**Version:** 2.0
**Last Updated:** 2026-02-05
