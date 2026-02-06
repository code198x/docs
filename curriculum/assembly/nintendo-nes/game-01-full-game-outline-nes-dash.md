# Full Game Outline: NES Dash (128 Units)

**Game:** Dash (Game 1)
**Units:** 128 (8 phases x 16 units)
**Target Quality:** Commercial-grade side-scrolling platformer (1986-87 era)
**Comparable To:** Kung Fu, Mappy -> evolving to Mega Man, Castlevania-level polish by completion

---

## What Makes This "NES"

The NES has:
- **Two-chip architecture** -- CPU and PPU are separate; you talk to the PPU through registers, not shared memory
- **Tile-based everything** -- backgrounds are a 32x30 grid of 8x8 tiles; sprites are 8x8 or 8x16 tiles
- **CHR ROM** -- graphics baked into the cartridge. Tile design is a first-class concern
- **64 hardware sprites** -- generous count, but only 8 per scanline
- **VBlank discipline** -- PPU updates only during ~2,273 CPU cycles of vertical blank. Miss the window, corrupt the screen
- **NMI-driven game loop** -- the PPU fires NMI every frame; the game breathes at 60 Hz
- **Hardware scrolling** -- PPUSCROLL sets the scroll position; the PPU handles the rest
- **APU sound** -- 2 pulse + 1 triangle + 1 noise + 1 DMC channel, each with distinct character
- **ca65/ld65 toolchain** -- segments, linker config, and the iNES header define the cartridge format

This platformer teaches the tile-based mindset through its most natural use. Tiles become platforms. Sprites become the character. Hardware scrolling opens up the world. The PPU does the heavy lifting -- your job is to set up the right tiles, then tell the PPU where to put them. The VBlank window forces discipline. The APU gives that unmistakable NES sound. The result is a cartridge that feels like it came from 1986 Nintendo.

---

## Design Philosophy

- **One concept per unit** -- never overwhelming
- **Always playable** -- from Unit 2 onwards, always a character that can move
- **Debugging inline** -- every unit includes "if it doesn't work"
- **6502/ca65 skill per unit** -- assembly concepts build alongside the game
- **PPU separation central** -- understanding the CPU/PPU boundary is THE NES skill
- **VBlank discipline from Unit 1** -- PPU writes only during VBlank, always
- **Jump by Unit 3** -- the core platformer verb, immediate
- **Scrolling by Phase 4** -- the world opens up at the halfway point
- **APU sound from Unit 5** -- not silent until late game
- **Mapper 0 (NROM)** -- 32KB PRG-ROM + 8KB CHR-ROM, no bank switching
- **Commercial quality by Unit 128** -- a real game

---

## 6502 Assembly Progression

| Phase | 6502/ca65 Focus |
|-------|-----------------|
| 1 (First Steps) | Registers (A/X/Y), zero page, LDA/STA, ca65 segments, iNES header, NMI handler, PPU register protocol |
| 2 (Solid Ground) | Indexed addressing (LDA table,X), 16-bit pointer arithmetic, metatile data structures |
| 3 (Momentum) | Bit manipulation (AND/ORA/EOR), signed arithmetic, comparison chains (CMP/BCS/BCC) |
| 4 (Horizon) | PPUSCROLL mechanics, nametable seam writes, VBlank budgeting, indirect indexed addressing |
| 5 (Pattern Table) | CHR data format, attribute table bit packing, Sprite 0 hit technique, lookup tables |
| 6 (Pulse) | APU register architecture, timer-driven music, subroutine parameter patterns |
| 7 (The Gauntlet) | Object pools, complex state machines, OAM cycling, multi-sprite entities |
| 8 (Cartridge) | Code optimisation, NTSC/PAL detection, iNES options, memory layout mastery |

By Unit 128, learners have a working knowledge of the 6502 instruction set, PPU graphics, APU audio, hardware scrolling, and the VBlank-disciplined approach that defines NES development.

---

## Phase 1: First Steps (Units 1-16)

**Goal:** Character on screen that runs, jumps, and lands on platforms. Single-screen level with collectibles and a game loop.
**6502 Focus:** Registers, addressing modes, zero page, PPU register protocol, NMI basics.
**Startup reality:** Getting anything on screen requires the iNES header, PPU warmup, NMI handler, and OAM DMA. This phase builds the framework every NES game needs.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 1 | iNES header + PPU warmup + one sprite | ca65 `.segment`, iNES header bytes, `LDA`/`STA` | See your character |
| 2 | Controller moves character left/right | Read `$4016` (strobe + serial), `AND` bit mask, `BEQ`/`BNE` | **Control something** |
| 3 | A button jumps | Velocity variable, gravity (add each frame), upward impulse | **The core verb** |
| 4 | Landing on a floor | Y-position check against floor line, velocity reset | Solid ground |
| 5 | Jump sound (pulse channel) | `STA $4000`-`$4003`, duty cycle + timer | Satisfying leap |
| 6 | Background tiles (nametable) | `$2006`/`$2007` writes during VBlank, tile index concept | Visible level |
| 7 | Platform collision (stand on tiles) | Read metatile below feet, stop falling if solid | **Platforms work** |
| 8 | Wall collision (block sides) | Read metatile at sides, prevent horizontal overlap | Can't walk through walls |
| 9 | Collectible items (sprites) | Multiple OAM entries, `JSR`/`RTS` subroutines | Things to pick up |
| 10 | Collect item = score | `CMP` proximity check, score in zero page, nametable update | **Reward** |
| 11 | Collect sound | APU triangle channel, short note | Audio feedback |
| 12 | Hazard tiles (spikes) | Attribute-based tile type, damage on contact | Stakes |
| 13 | Three lives | Game state in zero page, HUD tile update | Forgiveness |
| 14 | Game over screen | Nametable writes, state machine | End state |
| 15 | Title screen + Start button | Full nametable write, button edge detection, state reset | **Complete loop** |
| 16 | Integration + polish | Sprite hiding (Y=`$EF`), boundary checks, animation frame | Solid foundation |

**NES-Specific Unit 1:**
```asm
; iNES header (16 bytes)
.segment "HEADER"
.byte "NES", $1A      ; Magic number
.byte $02              ; 2 x 16KB PRG-ROM
.byte $01              ; 1 x 8KB CHR-ROM
.byte $01              ; Vertical mirroring, Mapper 0
.byte $00              ; Mapper 0 (NROM)

.segment "CODE"
reset:
    sei                ; Disable interrupts
    cld                ; Clear decimal mode (not used on NES)
    ldx #$FF
    txs                ; Set stack pointer

    ; PPU warmup: wait for 2 VBlanks
    bit $2002          ; Clear VBlank flag
:   bit $2002
    bpl :-             ; Wait for first VBlank
:   bit $2002
    bpl :-             ; Wait for second VBlank

    ; Set up sprite 0 in OAM buffer
    lda #120           ; Y position
    sta oam_buf
    lda #$01           ; Tile number
    sta oam_buf+1
    lda #$00           ; Attributes (no flip, palette 0)
    sta oam_buf+2
    lda #120           ; X position
    sta oam_buf+3
```

**If it doesn't work (Unit 1):**
- **No sprite?** Check OAM DMA is running (`$4014` write in NMI). Check `$2001` has sprites enabled (bit 4)
- **Wrong tile?** Pattern table selection is in `$2000` bit 3. Check CHR data in the right bank
- **Sprite at wrong position?** OAM format is Y, tile, attributes, X -- not X, Y
- **Screen is grey?** PPU warmup needs 2 full VBlanks before enabling rendering

**End of Phase 1:** A character that runs and jumps across platforms. Single screen, but playable. The PPU framework is solid.

---

## Phase 2: Solid Ground (Units 17-32)

**Goal:** Tile-based level design with metatiles, multiple platform types, and player animation.
**6502 Focus:** Indexed addressing, 16-bit pointer arithmetic, data-driven design.
**Key concept:** Metatiles -- 2x2 groups of tiles that form a single logical block. The level is designed in metatiles, not individual tiles. This reduces data size and simplifies collision.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 17 | Metatile data structure | 16-bit pointers, 4-byte tile groups | Building blocks defined |
| 18 | Level data (metatile grid) | Indirect indexed addressing, row/column calculation | Data-driven level |
| 19 | Level renderer | Nametable fill from level data during VBlank-off | **Level from data** |
| 20 | Attribute table from metatiles | Bit packing (4 metatiles per attribute byte) | Correct colours |
| 21 | One-way platforms | Collision flag per metatile type, check only when falling | Jump through from below |
| 22 | Ladder tiles | Vertical movement when overlapping ladder metatile | Climbing |
| 23 | Player run animation | Sprite cycling between 2-4 frames | Visual life |
| 24 | Player facing direction | Sprite horizontal flip (OAM attribute bit 6) | Left and right |
| 25 | Idle and jump sprites | State-based sprite selection | Complete animation set |
| 26 | Level exit | Door or flag metatile triggers level complete | Goal |
| 27 | Second level | Level pointer table, load new level on exit | Progression |
| 28 | Level transition effect | Palette fade to black (VBlank palette writes) | Polish |
| 29 | Multiple metatile themes | Different tile indices per level theme | Visual variety |
| 30 | Coin counter | Separate collectible count, distinct from score | Collection goal |
| 31 | All coins = bonus | Level-end bonus for 100% collection | Completionist reward |
| 32 | Integration + level design | Playtest, adjust layouts, collision tuning | Well-designed levels |

**Key Teaching Moment (Unit 17):**
A metatile is 4 tiles arranged in a 2x2 square: top-left, top-right, bottom-left, bottom-right. Each metatile also has a collision type (solid, empty, one-way, ladder, hazard). The level is a grid of metatile indices. To render: look up the metatile, write its 4 tiles to the nametable, pack its palette into the attribute table. One metatile index = one byte of level data for 16x16 pixels. A 16-metatile-wide, 15-metatile-tall screen is just 240 bytes.

**Key Teaching Moment (Unit 21):**
One-way platforms only block the player when falling. Check: is the player's Y velocity positive (moving down)? Is the player's bottom edge at the platform's top edge? If both, land. Otherwise, pass through. This single check makes vertical level design work.

**End of Phase 2:** Proper level design with metatiles, animation, ladders, and one-way platforms. Multiple levels with transitions. Looks like a real platformer.

---

## Phase 3: Momentum (Units 33-48)

**Goal:** Jump feel refined to commercial quality. Player physics, hazards, and checkpoints.
**6502 Focus:** Signed arithmetic, bit manipulation, comparison chains.
**Key moment:** Variable-height jumping -- hold the button longer, jump higher. This single mechanic separates amateur platformers from professional ones.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 33 | Variable-height jump | Check button held, reduce upward velocity early on release | **Professional jump** |
| 34 | Jump apex hang | Reduced gravity near peak velocity | Floaty-good feel |
| 35 | Coyote time | Grace frames after leaving platform edge | Forgiving controls |
| 36 | Jump buffering | Buffer A press just before landing | Responsive |
| 37 | Moving platforms (horizontal) | Platform object with velocity, player rides on top | Dynamic level |
| 38 | Moving platforms (vertical) | Carry player upward, detach on jump | Elevators |
| 39 | Crumbling platforms | Timer on contact, collapse after delay | Urgency |
| 40 | Pit death and respawn | Y boundary check, life lost, respawn at checkpoint | Consequence |
| 41 | Checkpoint flag | Metatile triggers, save respawn position | Fairness |
| 42 | Invincibility frames | Damage cooldown with sprite flicker (OAM cycling) | Brief immunity |
| 43 | Health system (3 hits) | Health variable, HUD hearts display | Forgiveness |
| 44 | Heal item | Heart pickup restores one health point | Recovery |
| 45 | Spring tile | Upward boost on contact, high-bounce sound | Vertical traversal |
| 46 | Conveyor belt | Horizontal force applied while standing on belt tile | Movement hazard |
| 47 | Water tiles | Reduced gravity and speed when submerged | Environment variety |
| 48 | Integration + feel tuning | Constants for gravity, jump force, speeds -- balance everything | **Feels right** |

**Key Teaching Moment (Unit 33):**
Variable-height jumping works by cutting the upward velocity short. While the button is held and velocity is negative (moving up), gravity applies normally. When the button is released, multiply the remaining upward velocity by a fraction (e.g., halve it). The player decelerates faster, peaking sooner. One `LSR` instruction halves the velocity. Simple code, transformative feel.

**Key Teaching Moment (Unit 35):**
Coyote time: for a few frames after walking off a platform edge, the player can still jump. The code tracks "frames since grounded" -- if it's under the threshold (typically 4-6 frames), allow the jump. Without this, players feel cheated. With it, they feel skilled.

**End of Phase 3:** Jump feel matches commercial quality. Variable height, coyote time, jump buffering. Hazards and checkpoints make levels interesting.

---

## Phase 4: Horizon (Units 49-64)

**Goal:** Hardware scrolling -- the world opens beyond one screen.
**6502 Focus:** PPUSCROLL mechanics, nametable seam writes, VBlank budgeting, 16-bit scroll position.
**Key moment:** The first time the screen scrolls to reveal more level. Hardware scrolling is the NES's gift to platformers -- the PPU handles the pixel-perfect offset, you just manage the data.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 49 | PPUSCROLL basics | `$2005` double-write (X then Y scroll), timing after `$2006` | Screen shifts |
| 50 | Smooth camera follow | Camera tracks player, scroll increments per frame | World moves with you |
| 51 | Camera dead zone | Don't scroll until player reaches screen edge threshold | Comfortable view |
| 52 | 16-bit scroll position | Two bytes for scroll X, carry into nametable select | Beyond 255 pixels |
| 53 | Nametable seam loading | Write new column of tiles at the scroll edge | **Seamless world** |
| 54 | Seam column from level data | 16-bit level pointer, read metatile column ahead | Data-driven scrolling |
| 55 | Attribute seam update | Update attribute bytes at nametable boundary | Correct colours at edge |
| 56 | VBlank budget management | Measure cycles, split work across frames if needed | Stable rendering |
| 57 | Scroll-aware collision | Convert world coords to screen coords for tile checks | Collision still works |
| 58 | Scroll-aware sprites | Subtract scroll offset for on-screen X position | Objects stay in place |
| 59 | Camera bounds | Stop scrolling at level start/end | No overrun |
| 60 | Horizontal mirroring option | Nametable layout choices, vertical vs horizontal | Level shape |
| 61 | Long level (4+ screens) | Extended level data, tested scrolling over distance | Real content |
| 62 | Scroll speed zones | Different max speeds for sections (fast run, slow careful) | Pacing control |
| 63 | Status bar with Sprite 0 | Sprite 0 hit splits scroll: HUD fixed, level scrolls | **Professional HUD** |
| 64 | Integration + scroll stability | Edge cases, seam glitches, performance audit | Solid scrolling |

**Key Teaching Moment (Unit 49):**
PPUSCROLL is a double-write register. First write sets horizontal scroll (0-255), second write sets vertical scroll. But the scroll value is latched at specific times -- writes must happen after `$2006` reads reset the latch. Miss the timing and the scroll jumps. The NES hardware does the actual pixel shifting; your code just says "offset by this much."

**Key Teaching Moment (Unit 53):**
As the camera scrolls right, new tiles must appear at the right edge. The NES has two nametables side by side (with mirroring). You write the next column of tiles to the nametable that's about to scroll into view -- one column per frame during VBlank. The seam is invisible because the PPU wraps between nametables. This is how every scrolling NES game works.

**Key Teaching Moment (Unit 63):**
Sprite 0 hit splits the screen. Place a sprite at the bottom of the status bar. When the PPU draws that sprite, it sets a flag in `$2002`. Your code waits for this flag, then writes new scroll values -- the status bar stays fixed while the level scrolls. Nearly every NES game with a HUD uses this technique.

**NES-Specific:**
```asm
; Write PPUSCROLL after rendering status bar
; Wait for Sprite 0 hit
:   bit $2002
    bvs :-             ; Wait for flag to clear from last frame
:   bit $2002
    bvc :-             ; Wait for Sprite 0 hit

    ; Now set scroll for the gameplay area
    lda scroll_x
    sta $2005           ; Horizontal scroll
    lda #$00
    sta $2005           ; Vertical scroll (0 for side-scroller)
```

**End of Phase 4:** The world scrolls. Long levels, seamless nametable loading, status bar stays fixed. The NES is doing what it was built for.

---

## Phase 5: Pattern Table (Units 65-80)

**Goal:** Visual polish to commercial standard. CHR art, tile themes, background detail, colour.
**6502 Focus:** CHR data format, attribute table mastery, lookup tables, tile animation.
**The moment:** Custom tile art transforms generic blocks into a platformer world with character.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 65 | CHR tile design (background set) | Pattern table format: 2 bitplanes, 8x8 pixels, 4 colours | Custom world tiles |
| 66 | Themed tileset: outdoor | Trees, grass, hills, sky, clouds | First theme |
| 67 | Themed tileset: underground | Rock, dirt, crystals, lava | Second theme |
| 68 | Player sprite redesign | Multi-tile metasprite (2x2 tiles for 16x16 character) | **Recognisable character** |
| 69 | Metasprite routine | Table-driven multi-tile sprite rendering | Reusable system |
| 70 | Background detail tiles | Decorative tiles (windows, cracks, vines, signs) | Rich environments |
| 71 | Attribute table mastery | 4 palette zones per 32x32 pixel area | Correct colouring |
| 72 | Palette design per theme | 4 background + 4 sprite palettes per level | Cohesive colour |
| 73 | Tile animation (water, lava) | Swap CHR data during VBlank or use CHR bank tricks | Living world |
| 74 | Parallax background | Sprite 0 split: different scroll rate for sky | Depth |
| 75 | Player trail effect | Brief afterimage sprites during dash/run | Speed visual |
| 76 | Death animation | Multi-frame sprite sequence | Dramatic |
| 77 | Item collect animation | Sprite expansion then vanish | Satisfying |
| 78 | Screen shake on impact | Temporary scroll offset on damage | Dramatic feedback |
| 79 | Title screen art | Full nametable character art: "DASH" | Presentation |
| 80 | Integration + visual audit | Consistent tiles, attribute alignment, palette harmony | Looks professional |

**Key Teaching Moment (Unit 65):**
NES tiles use 2 bitplanes. Each 8x8 tile is 16 bytes: 8 bytes for bitplane 0, then 8 bytes for bitplane 1. The two planes combine to give 4 values per pixel (0-3), which index into a 4-colour palette. Designing tiles means thinking in 2-bit colour -- limited but distinctive. The constraint forces clarity.

**Key Teaching Moment (Unit 71):**
The attribute table is 64 bytes that colour the entire nametable. Each byte covers a 32x32 pixel area (4x4 tiles), split into four 16x16 quadrants. Two bits per quadrant select which of 4 background palettes to use. The packing is: `(top-left) | (top-right << 2) | (bottom-left << 4) | (bottom-right << 6)`. Metatiles align perfectly with attribute quadrants -- another reason metatiles are 16x16.

**End of Phase 5:** Custom CHR art, themed tilesets, parallax, animation. Screenshots would sell this game.

---

## Phase 6: Pulse (Units 81-96)

**Goal:** Full APU soundtrack and sound design. The five channels, each with purpose.
**6502 Focus:** APU register architecture, timer-driven music playback, channel management.
**The sound:** 2 pulse channels for melody and harmony, triangle for bass, noise for percussion. Plus DMC for samples.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 81 | APU architecture overview | Register map (`$4000`-`$4017`), channel structure | Understanding the chip |
| 82 | Pulse channel deep dive | Duty cycle, timer, length counter, envelope | Shaped melody notes |
| 83 | Sound effect library | Parameterised routine (channel, freq, envelope, sweep) | Jump, land, collect, hurt, die |
| 84 | Replace placeholder sounds | Integrate crafted SFX throughout the game | Cohesive audio |
| 85 | Triangle channel | Bass notes (no volume control, always on or off) | Foundation tone |
| 86 | Noise channel | Percussion: short noise bursts for snare, hi-hat | Rhythm |
| 87 | Title music (pulse melody) | Note table, sequence data, playback in NMI | Atmosphere |
| 88 | Two-channel harmony | Pulse 1 melody + Pulse 2 counter-melody | Rich sound |
| 89 | Full 4-channel music | Triangle bass + noise drums + two pulse voices | **Proper soundtrack** |
| 90 | Music engine (pattern-based) | Pattern pointer table, row sequencer, tempo control | Reusable engine |
| 91 | In-game music | Looping level theme, distinct from title | Gameplay atmosphere |
| 92 | Music stops for boss/event | State-controlled playback, clean channel release | Dynamic audio |
| 93 | SFX over music | Channel stealing with priority, restore after SFX | No ugly cutoff |
| 94 | DMC channel basics | Sample playback (if ROM space allows) | Sampled hits |
| 95 | Level-complete jingle | Short celebratory phrase | Punctuation |
| 96 | Integration + audio balance | Volume, tempo, SFX/music coexistence | Sounds great |

**Key Teaching Moment (Unit 82):**
Each pulse channel has a duty cycle (12.5%, 25%, 50%, 75%) that shapes its tone -- thin and reedy, or full and round. The envelope generator handles volume decay automatically. The sweep unit can bend pitch up or down. These hardware features mean rich sound without constant CPU intervention.

**Key Teaching Moment (Unit 90):**
A pattern-based music engine stores songs as a list of pattern pointers. Each pattern is a sequence of rows: note + duration. The NMI handler advances the row counter each frame, reads the next event when the current note expires, and writes to APU registers. Music plays automatically at rock-solid 60Hz timing -- the NMI is the metronome.

**End of Phase 6:** Full 4-channel soundtrack with music engine, crafted SFX, and priority system. The APU sings.

---

## Phase 7: The Gauntlet (Units 97-112)

**Goal:** Enemies, combat, and boss fights. The levels become a gauntlet.
**6502 Focus:** Object pools, complex state machines, OAM cycling, metasprite entities.
**Key challenge:** Managing many sprites -- player metasprite + enemies + collectibles + projectiles. OAM cycling prevents flicker when sprites share scanlines.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 97 | Walking enemy (patrol) | Object pool with state table, direction toggle at edges | Moving threat |
| 98 | Enemy-player collision | Bounding box check per enemy, damage on contact | **Danger** |
| 99 | Stomp mechanic | Check player falling onto enemy top, bounce up | Defeat by jumping on |
| 100 | Stomp sound + score | APU noise burst, score increment | Satisfying |
| 101 | Flying enemy (sine wave) | Lookup table for vertical offset, horizontal drift | Aerial threat |
| 102 | Shooting enemy (projectile) | Enemy fires toward player, simple aimed bullet | Ranged danger |
| 103 | Player projectile | B button throws/shoots, limited ammo or cooldown | Offensive option |
| 104 | Multiple enemy types per level | Type field in object data, behaviour dispatch | Varied challenge |
| 105 | OAM cycling | Rotate starting OAM index each frame to distribute flicker | Fair visibility |
| 106 | Boss: large metasprite | Multi-tile entity (4x4 tiles), coordinated movement | **Imposing** |
| 107 | Boss movement pattern | State machine: idle -> telegraph -> attack -> recover | Learnable fight |
| 108 | Boss health bar | Background tiles in HUD, deplete on hits | Visible progress |
| 109 | Boss phase 2 | Pattern change at 50% health, faster attacks | Escalation |
| 110 | Boss defeat sequence | Explosion sprites, victory jingle, door opens | Triumph |
| 111 | Level design with enemies | Placement, spawn triggers, scroll-based activation | Designed encounters |
| 112 | Integration + combat balance | Hit boxes, damage values, enemy placement | Challenging but fair |

**Key Teaching Moment (Unit 99):**
The stomp mechanic: if the player's Y velocity is positive (falling) and the player's bottom edge overlaps the enemy's top edge (within a few pixels), it's a stomp. The player bounces upward (set negative velocity), the enemy is defeated. If the overlap is horizontal instead, it's contact damage. The distinction is a few comparisons -- simple code, iconic mechanic.

**Key Teaching Moment (Unit 105):**
The NES allows 64 sprites but only 8 per scanline. When more than 8 overlap on the same line, the PPU drops the extras. OAM cycling rotates which sprites get priority each frame -- the dropped sprites change every frame, creating even flicker instead of invisible objects. Every commercial NES game does this.

**End of Phase 7:** Enemies, combat, and bosses. The gauntlet is complete. Every level is a designed encounter.

---

## Phase 8: Cartridge (Units 113-128)

**Goal:** Commercial release quality. Everything a real 1987 NES game would ship with.
**6502 Focus:** Code optimisation, memory management, NTSC/PAL considerations.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 113 | High score table (top 5) | Sorted insertion, multi-byte comparison | Competition |
| 114 | Name entry (3 characters) | On-screen keyboard, cursor navigation | Ownership |
| 115 | High scores on title | Display integration | Bragging rights |
| 116 | Difficulty select (3 levels) | Menu system, cursor navigation | Accessibility |
| 117 | Difficulty affects gameplay | Parameter tables per difficulty | Real difference |
| 118 | Extra life at score threshold | Threshold detection, 1-up jingle | Skill reward |
| 119 | Continue system | Level restart with limited continues | Forgiveness |
| 120 | Password system | Level progress encoded as 4-character password | Save without battery |
| 121 | Attract mode | Recorded input playback or simple AI demo | Professional |
| 122 | Demo on title after timeout | Timer-triggered state change | Arcade feel |
| 123 | NTSC/PAL detection | Frame timing comparison | Platform correct |
| 124 | Credits screen | Scrolling nametable text | Attribution |
| 125 | 8+ designed levels | Full level set with difficulty curve | Complete content |
| 126 | Final balance + testing | Edge cases, difficulty curve, boss fairness | Release ready |
| 127 | Memory audit | PRG-ROM and CHR-ROM usage map | Fits in NROM |
| 128 | **Complete game -- final .nes** | iNES packaging, documentation | **Ship it** |

**End of Phase 8:** A game you could put on a cartridge and sell in 1987. High scores, passwords, attract mode, 8+ levels -- the full commercial package.

---

## NES-Specific Debugging (Throughout)

**PPU Issues:**
- No sprites visible? Check `$2001` bits 3-4 (sprite/background enable). Check OAM DMA ($4014) runs in NMI
- Sprites at wrong position? OAM byte order is Y, tile, attributes, X. Y is one scanline early (actual display Y = stored Y + 1)
- Wrong tile? Check pattern table selection in `$2000` bit 3 for sprites. CHR data at correct addresses
- Sprite behind background? OAM attribute bit 5 controls priority
- Garbled nametable? Writes to `$2006`/`$2007` must happen during VBlank or with rendering off
- Attribute colours wrong? Each attribute byte covers 32x32 pixels (4x4 tiles). Bit packing: 2 bits per 16x16 quadrant

**Scrolling Issues:**
- Scroll jumps randomly? `$2005` and `$2006` share an internal latch. Read `$2002` to reset it before writing `$2005`
- Seam visible? Column writes must complete during VBlank. Reduce per-frame write count if over budget
- Wrong nametable? `$2000` bits 0-1 select the base nametable. Check these match your scroll state
- Status bar scrolls with level? Use Sprite 0 hit to split: write `$2005` after the hit flag

**Controller Issues:**
- Controls backwards? Check strobe write (`$4016` = 1, then 0) before reading. Each read returns one bit
- Button ghosting? Read all 8 bits even if you don't use them all. Store previous frame for edge detection
- No response? Verify `$4016` strobe sequence: write 1, write 0, then 8 reads

**APU Issues:**
- No sound? Write `$4015` to enable channels (bit per channel). Common to forget this
- Sound cuts off? Length counter may be expiring. Set bit 5 of the channel's first register to disable length counter
- Music tempo wrong? NMI fires at 60Hz (NTSC) or 50Hz (PAL). Adjust tick rate accordingly

**General 6502 Issues:**
- Values corrupted? NMI handler must save/restore A, X, Y (PHA/TXA/PHA/TYA/PHA, reverse on exit)
- Screen corruption during gameplay? You're writing PPU registers outside VBlank. All `$2006`/`$2007` writes in NMI only
- Game runs at wrong speed? Logic in NMI vs main loop matters. NMI for PPU updates and music; main loop for game logic

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 4 (Unit 64) | Phase 8 (Unit 128) |
|--------|-------------------|--------------------|--------------------|
| Graphics | Single sprite, basic tiles | + metatiles, themes, animation | Metasprites, parallax, CHR art |
| World | 1 screen | + hardware scrolling, long levels | 8+ levels, bosses, varied themes |
| Player | Run + jump | + variable jump, coyote time, wall physics | + combat, projectiles, full animation |
| Enemies | None | + hazard tiles, pits, moving platforms | Patrol, flying, shooting, bosses |
| Audio | One SFX | + effect library | Full 4-channel music, priority SFX |
| Features | Move + collect + die | + checkpoints, ladders, scrolling | High scores, passwords, attract, 2-player |
| 6502 Skill | LDA, STA, branches | + 16-bit, indexed, VBlank discipline | Full toolkit, music engine, object pools |

---

## What This Teaches Beyond the Game

By completing Dash, learners are ready for:
- **Crate Escape (Game 2):** Jump physics transfer directly. Metatile system reused for level design. Single-screen focus deepens platformer polish
- **Fracture Point (Game 3):** Tile-based backgrounds become breakout bricks. VBlank discipline enables dynamic nametable updates
- **Crypt Crawler (Game 5):** Metatile system becomes room renderer. Object pools manage monsters. State machines drive AI
- **Pixel Plains (Game 8):** Hardware scrolling becomes full-screen scrolling. Seam loading enables open worlds
- **Every future game:** The NMI framework, VBlank discipline, PPU update patterns, and APU music engine from Dash are reused throughout the curriculum

Dash isn't just Game 1. It's the foundation.

---

**Version:** 1.0
**Last Updated:** 2026-02-06
