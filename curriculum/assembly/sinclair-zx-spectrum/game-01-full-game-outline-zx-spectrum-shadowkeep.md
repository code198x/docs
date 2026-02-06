# Full Game Outline: ZX Spectrum Shadowkeep (128 Units)

**Game:** Shadowkeep (Game 1)
**Units:** 128 (8 phases × 16 units)
**Target Quality:** Commercial-grade top-down maze explorer (1984–85 era)
**Comparable To:** Atic Atac, Sabre Wulf → evolving to Knight Tyme, Dragontorc-level polish by completion

---

## What Makes This "Spectrum"

The Sinclair ZX Spectrum has:
- **Attribute system** — every 8×8 cell has INK, PAPER, BRIGHT, and FLASH, defining colour AND gameplay
- **Colour clash** — only one foreground and one background colour per cell, the defining constraint
- **Non-linear screen memory** — the infamous thirds layout, a rite of passage for every Spectrum programmer
- **Beeper audio (48K)** — one bit, one speaker, all sound generated in software
- **AY-3-8912 (128K)** — 3-voice sound chip with hardware envelopes, shared with Amstrad CPC
- **Z80 processor** — 16-bit register pairs, block operations (LDIR), single-bit instructions (BIT/SET/RES)
- **~42KB user RAM** — enough for a rich game, tight enough to need compression

This maze explorer showcases the attribute system as a game design tool. Walls are INK colour, floors are PAPER, items are BRIGHT, hazards are FLASH. Collision detection is a single attribute read. The Spectrum's most famous limitation — colour clash — is turned into the core mechanic. The result is unmistakably Spectrum.

---

## Design Philosophy

- **Attributes from Unit 1** — the Spectrum's defining feature is the first thing taught
- **Playable room by Unit 7** — walk, collide with walls, within the first phase
- **Colour is gameplay** — INK means wall, BRIGHT means item, FLASH means danger
- **Character-cell movement** — 8-pixel grid, matching the attribute grid perfectly
- **Beeper sound from Unit 12** — not silent until late game
- **Fog of war in Phase 7** — the attribute system enables darkness with a single technique
- **48K and 128K** — core game fits 48K, 128K gets AY music and extra rooms
- **Commercial quality by Unit 128** — a real game worthy of Crash magazine

---

## Z80 Assembly Progression

| Phase | Z80 Focus |
|-------|----------|
| 1 (Threshold) | LD, INC/DEC, JP/JR, CP, AND/OR, CALL/RET, IN/OUT, DJNZ, BIT/SET/RES |
| 2 (Relics) | Indirect addressing (HL), IX+displacement, 16-bit arithmetic, PUSH/POP |
| 3 (Sentinels) | XOR, array processing, FRAMES system variable, multi-field table loops |
| 4 (The Labyrinth) | LDIR/LDDR block operations, RLE compression, contended memory timing |
| 5 (Illumination) | Screen memory thirds, bit shifts (SLA/SRL/RLC), UDG definition, pixel plotting |
| 6 (Echoes) | Timing loops for beeper, AY register access, IM 2 interrupt mode, DI/EI |
| 7 (The Deep) | NEG for distance, dynamic attribute manipulation, 128K memory paging ($7FFD) |
| 8 (Escape) | Keyboard matrix scanning, memory audit, TAP/TZX file creation, optimisation |

By Unit 128, learners have a working knowledge of the Z80 instruction set, the Spectrum's screen and attribute system, beeper and AY audio, interrupt-driven timing, and the techniques that define Spectrum programming.

---

## Phase 1: Threshold (Units 1–16)

**Goal:** Single room — walk, collide with walls, collect items, exit.
**Z80 Focus:** Registers, basic addressing, loops, conditions, ports.
**The Spectrum way:** Attributes ARE the game world. One attribute read = collision detection.

| Unit | You Add | Z80 Skill | Result |
|------|---------|----------|--------|
| 1 | Coloured block on screen | `LD A,n` / `LD (addr),A`, memory addresses | See a colour |
| 2 | Attribute byte anatomy | `AND`/`OR` for INK, PAPER, BRIGHT, FLASH bits | Understand colours |
| 3 | Room drawn from attributes | `DJNZ` loop, attribute grid | Walls and floor visible |
| 4 | Keyboard input | `IN A,($FE)`, row selection, key detection | Read key presses |
| 5 | Player character on screen | Print to screen RAM, position tracking | **Character visible** |
| 6 | Character-cell movement | `INC`/`DEC`, `CP`/`JR` boundary check | Move on 8-pixel grid |
| 7 | Wall collision | Read attribute at target, check INK colour | **Walls block movement** |
| 8 | Room from data table | Byte array defines room layout | Data-driven room |
| 9 | Treasure items | BRIGHT bit marks collectibles, `BIT`/`RES` | Shining items |
| 10 | Collect treasure | Read attribute, check BRIGHT, update score | **Items work** |
| 11 | Score display | `CALL` ROM routine, number conversion | Score on status line |
| 12 | Beeper sound | `OUT ($FE),A` bit 4 toggle, timing loop | Collect sound |
| 13 | Exit door | Specific attribute marks the exit | Goal visible |
| 14 | Room complete | All treasures → door opens, exit detection | **Win condition** |
| 15 | Hazards and lives | FLASH = danger, 3 lives, death on touch | Stakes |
| 16 | Integration | Edge cases, status bar, restart | Solid single room |

**Spectrum-Specific Unit 1:**
```z80
; Set attribute at row 12, column 16 to yellow on blue
; Attribute address = $5800 + (row × 32) + column

    ld hl,$5800 + (12 * 32) + 16
    ld (hl),$46         ; PAPER 0 (black), INK 6 (yellow), no BRIGHT/FLASH
                        ; Binary: 00 000 110
```

**Attribute as Game Language:**
```z80
; Check what's at the target position before moving
; INK 1 (blue) = wall, INK 6 (yellow) = treasure, FLASH = hazard

check_collision:
    ld a,(hl)           ; Read attribute at target cell
    bit 7,a             ; FLASH bit set?
    jr nz,hazard_hit    ; Yes → damage player
    bit 6,a             ; BRIGHT bit set?
    jr nz,collect_item  ; Yes → pick up treasure
    and $07             ; Isolate INK colour (bits 0-2)
    cp 1                ; INK 1 = wall?
    jr z,blocked        ; Yes → can't move
    ; Otherwise → move allowed
```

**If it doesn't work (Phase 1):**
- **No colour?** Check you're writing to $5800+ (attributes), not $4000+ (bitmap)
- **Wrong cell?** Address = $5800 + (row × 32) + column. Rows 0–23, columns 0–31
- **Movement wrong direction?** Spectrum Y increases downward. Row 0 = top of screen
- **Collision not working?** Read the attribute BEFORE moving, not after
- **Items don't disappear?** `RES 6,(HL)` clears the BRIGHT bit at address HL

**End of Phase 1:** Playable single room. Navigate walls, collect items, exit. The attribute system proven as game design tool.

---

## Phase 2: Relics (Units 17–32)

**Goal:** Keys, doors, inventory, multiple rooms — the core puzzle mechanic.
**Z80 Focus:** Indirect addressing (HL), IX register, 16-bit arithmetic, lookup tables.
**Key concept:** Colour-coded keys match colour-coded doors. The attribute system encodes puzzle logic.

| Unit | You Add | Z80 Skill | Result |
|------|---------|----------|--------|
| 17 | Key items (coloured INK) | Different INK = different key type | Keys visible |
| 18 | Collect key | Inventory variable on collection | Player picks up keys |
| 19 | Door tiles | Specific attribute = locked door | Locked passages |
| 20 | Key opens matching door | Check inventory, allow passage | **Puzzle mechanic** |
| 21 | Multiple key colours | Bit flags (bit 0=red, bit 1=blue, etc.) | Colour-coded puzzles |
| 22 | Locked door sound | Beeper: low buzz (denied) | Feedback |
| 23 | Door open sound | Beeper: rising tone (success) | Feedback |
| 24 | Health system | Health points (1–4) replace instant death | Forgiveness |
| 25 | Potion item | New item type restores health | Strategic resource |
| 26 | Status bar | Health, score, keys in bottom rows | **Clear HUD** |
| 27 | Second room | `LD A,(HL)` indirect addressing, room index | Two rooms |
| 28 | Room transition | Clear screen, load new room, reposition player | Between rooms |
| 29 | Room connections | Data table: exits link to rooms | Directed navigation |
| 30 | Room variety | 4+ rooms, different layouts and items | Exploration |
| 31 | Room neighbour map | N/S/E/W connections per room | Coherent world |
| 32 | Integration + balance | Puzzle design, item placement, route flow | Satisfying exploration |

**Key Teaching Moment (Unit 21):**
Four keys in one byte: bit 0 = red, bit 1 = blue, bit 2 = green, bit 3 = yellow. `BIT 0,A` checks for red key. `SET 1,A` grants blue key. The Z80's single-bit instructions make this trivially clean — one byte, four keys, no wasted memory.

**Key Teaching Moment (Unit 27):**
The HL register pair holds a 16-bit address. `LD A,(HL)` reads the byte at that address. `INC HL` advances to the next byte. This is how the Z80 walks through data — point HL at room data, read each byte in sequence. Unlike the 6502's indirect indexed mode, HL is always available as a pointer.

**End of Phase 2:** 4+ rooms, coloured keys, matching doors, health, potions. The keep has depth and puzzles.

---

## Phase 3: Sentinels (Units 33–48)

**Goal:** Creatures that guard the keep — patrol AI, combat, danger.
**Z80 Focus:** Array processing, XOR for animation, timer management, FRAMES variable.

| Unit | You Add | Z80 Skill | Result |
|------|---------|----------|--------|
| 33 | Enemy character | Second character on screen, position tracked | Creature visible |
| 34 | Enemy patrol (horizontal) | Direction toggle on wall hit | Back-and-forth |
| 35 | Enemy patrol (vertical) | Same logic, vertical axis | Up-and-down |
| 36 | Enemy-wall collision | Reuse attribute check for enemies | Enemies respect walls |
| 37 | Enemy touches player | Position comparison, damage on match | **Contact hurts** |
| 38 | Damage sound | Beeper: low descending tone | Audio feedback |
| 39 | Invincibility frames | FRAMES variable ($5C6A) timer | Brief immunity |
| 40 | Enemy animation | `XOR` to toggle between two characters | Visual life |
| 41 | Multiple enemies | Enemy data table, `DJNZ` loop | Several per room |
| 42 | Different speeds | Speed field, frame-skip movement | Fast and slow |
| 43 | Border flash on hit | `OUT ($FE)` border colour change | Dramatic feedback |
| 44 | Sword item | New collectible enables attacking | Offensive option |
| 45 | Attack mechanic | Check adjacent cell facing direction | Defeat creatures |
| 46 | Enemy defeat | Remove, score bonus, defeat sound | Satisfying elimination |
| 47 | Enemies per room | Room data includes enemy spawn list | Room-specific creatures |
| 48 | Integration + balance | Placement, speed, combat fairness | Tense but fair |

**Key Teaching Moment (Unit 36):**
The attribute-check subroutine works identically for enemies. Pass target position, call the routine, check result. Enemies respect the same walls the player does — one collision system for everything. The attribute system's elegance pays off again.

**Key Teaching Moment (Unit 40):**
`XOR` flips bits. If the character codes are $41 and $42, `XOR $03` toggles between them — one instruction, no branches. This is faster than compare-and-branch and generalises to any pair of values.

**End of Phase 3:** Enemies patrol, player takes damage, sword enables fighting back. The keep is dangerous.

---

## Phase 4: The Labyrinth (Units 49–64)

**Goal:** Many rooms, compressed data, a map — the maze expands.
**Z80 Focus:** LDIR/LDDR block operations, RLE compression, contended memory, 16-bit arithmetic.
**Key moment:** `LDIR` — the Z80's hardware-accelerated block copy — transforms room transitions from sluggish to instant.

| Unit | You Add | Z80 Skill | Result |
|------|---------|----------|--------|
| 49 | LDIR block copy | `LDIR` for fast memory copy | Instant room draw |
| 50 | Room buffer | Working buffer, modify in place | Rooms reset on re-entry |
| 51 | Run-length encoding | Compression: value + count pairs | Compact storage |
| 52 | RLE decompression | Expand to attribute buffer | Rooms from compressed data |
| 53 | 8+ rooms | Expanded room table, index lookup | Larger world |
| 54 | Room themes | Different colour palettes per area | Visual variety |
| 55 | 16-bit room pointers | `LD HL,(addr)` for address tables | Many rooms |
| 56 | Map display | Visited rooms shown as grid on pause | **Player orientation** |
| 57 | Map data | Bit flags per room (visited, has key, has boss) | Tracked exploration |
| 58 | One-way passages | Enter but can't return | Routing challenge |
| 59 | Teleport tiles | Warp to distant room | Surprising navigation |
| 60 | Save points | Checkpoint, respawn here on death | Fairness |
| 61 | Contended memory | $4000–$7FFF timing penalty | Why screen is slow |
| 62 | Fast attribute fill | Timing-aware writes | Faster transitions |
| 63 | Room counter | "Room X of Y" in status bar | Progress |
| 64 | Integration + balance | Room flow, key routing, difficulty curve | Satisfying labyrinth |

**Key Teaching Moment (Unit 49):**
`LDIR` copies BC bytes from HL to DE. One instruction replaces an entire loop. Room transitions go from multi-frame redraws to near-instant loads. This is the Z80's genuine luxury — hardware-accelerated memory operations.

**Key Teaching Moment (Unit 51):**
An uncompressed room is 768 bytes. Sixteen rooms = 12KB. With RLE compression (3:1 to 5:1 ratio), the same content fits in 2–4KB. Compression is a practical necessity, not academic exercise.

**End of Phase 4:** 16+ rooms with map, themes, one-way passages, teleporters, and save points. A real labyrinth.

---

## Phase 5: Illumination (Units 65–80)

**Goal:** Visual polish — UDG characters, pixel work, animation.
**Z80 Focus:** Screen memory thirds, bit shifts, UDG definition, pixel plotting.
**The moment:** Custom graphics transform coloured blocks into an atmospheric dungeon.

| Unit | You Add | Z80 Skill | Result |
|------|---------|----------|--------|
| 65 | UDG basics | Write 8 bytes to UDG area | Custom character |
| 66 | Player UDG | Adventurer figure design | **Recognisable player** |
| 67 | Enemy UDGs | Distinct creature designs (rat, bat, ghost) | Enemy variety |
| 68 | Wall UDGs | Stone, wood, iron tiles | Textured walls |
| 69 | Item UDGs | Key, potion, treasure, sword icons | Clear items |
| 70 | Player walk animation | 2–4 UDG frames per direction | Animated movement |
| 71 | Enemy walk animation | Patrol cycle with frame switching | Living creatures |
| 72 | Screen memory layout | The thirds formula, row address lookup | **Spectrum rite of passage** |
| 73 | Pixel plotting | Set/clear individual pixels | Fine detail |
| 74 | Room transition effects | Wipe: line-by-line or dissolve | Polished transitions |
| 75 | Door opening animation | UDG frame sequence: closed → open | Visual feedback |
| 76 | Death animation | Character breaks apart (2–3 frames) | Dramatic death |
| 77 | Title screen | Character art: "SHADOWKEEP" | Presentation |
| 78 | Zone colour themes | Different palettes per area | Area identity |
| 79 | Status bar polish | Custom font, clean layout | Professional HUD |
| 80 | Integration | Colour clash audit, visual consistency | Cohesive look |

**Key Teaching Moment (Unit 72):**
The screen memory layout is the Spectrum's most infamous quirk. Pixel rows are interleaved in thirds. The address formula uses bit manipulation on the Y coordinate — bits 0–2 select the pixel row within a character, bits 3–5 select the character row within a third, bits 6–7 select the third. A row-address lookup table avoids runtime calculation.

**Spectrum-Specific:**
```z80
; Screen address for pixel row Y, column X
; Y bits: 76 543 210
; Address: 010 76 543 210 XXXXX
; Where XXXXX = X / 8

pixel_addr:
    ld a,d              ; D = Y coordinate
    and $07             ; Bits 0-2
    or $40              ; $4000 base
    ld h,a              ; High byte started
    ld a,d
    rra
    rra
    rra
    and $18             ; Bits 3-5 → bits 3-4
    or h
    ld h,a
    ld a,d
    and $c0             ; Bits 6-7
    rra
    rra
    rra
    or e                ; E = X / 8
    ld l,a
    ; HL now points to the correct byte
```

**End of Phase 5:** UDG characters, animation, pixel effects. Looks like a commercial 1984 Spectrum game.

---

## Phase 6: Echoes (Units 81–96)

**Goal:** Sound and music — from beeper to AY.
**Z80 Focus:** Timing loops, AY registers, interrupt mode 2, 48K/128K detection.
**The constraint:** 48K beeper blocks the CPU. 128K AY runs independently. Both must be supported.

| Unit | You Add | Z80 Skill | Result |
|------|---------|----------|--------|
| 81 | Beeper fundamentals | `OUT ($FE),A` bit 4, delay = pitch | First controlled tone |
| 82 | Pitch control | Loop length = frequency, note table | Tuneable pitch |
| 83 | Sound effect library | Parameterised routine | Collect, hit, door, death |
| 84 | Duration control | Outer loop counts cycles | Timed sounds |
| 85 | Pitch slides | Sweep delay value over time | Dramatic effects |
| 86 | Multi-tone | Rapid alternation between frequencies | Richer beeper |
| 87 | Staccato rhythms | Short bursts with gaps | Percussion feel |
| 88 | Title music (beeper) | Note sequence + timing playback | 48K atmosphere |
| 89 | In-game ambient | Brief phrases between frames | Subtle tension |
| 90 | AY-3-8912 | Register access via $FFFD/$BFFD | **128K sound chip** |
| 91 | AY sound effects | Hardware envelopes, noise channel | Richer effects |
| 92 | AY music engine | 3-voice playback, pattern sequencing | Background music |
| 93 | Interrupt mode 2 | `IM 2`, vector table, 50Hz handler | Music during gameplay |
| 94 | AY title music | Full 3-voice theme | Atmospheric title |
| 95 | 48K/128K detection | AY register write/read test | Automatic selection |
| 96 | Integration | Volume balance, SFX/music coexistence | Cohesive audio |

**Key Teaching Moment (Unit 81):**
The 48K beeper is one bit on one port. A timing loop toggles it. Sound blocks the CPU — the fundamental constraint that shapes all 48K audio design. Brief effects between game frames, not continuous music.

**Key Teaching Moment (Unit 93):**
`IM 2` sets up interrupt mode 2 with a vector table. A 50Hz interrupt from the ULA drives the AY music sequencer — music plays automatically during gameplay. This is how every commercial 128K game handles background audio.

**End of Phase 6:** Full audio for both models. 48K gets beeper effects and simple music. 128K gets 3-voice AY soundtrack with interrupt-driven playback.

---

## Phase 7: The Deep (Units 97–112)

**Goal:** Darkness, atmosphere, boss encounters, special items.
**Z80 Focus:** Dynamic attribute manipulation, distance calculation, complex state machines.
**The moment:** Fog of war — attributes set to black-on-black beyond the light radius — is pure Spectrum.

| Unit | You Add | Z80 Skill | Result |
|------|---------|----------|--------|
| 97 | Fog of war | Distant attributes set to black-on-black | **Limited visibility** |
| 98 | Light radius | Manhattan distance from player | Reveal nearby cells |
| 99 | Torch item | Expands radius from 3 to 5 | Exploration aid |
| 100 | Flickering light | FLASH on radius edge | Torchlight atmosphere |
| 101 | Dark room enemies | Visible only within radius | Surprise encounters |
| 102 | Boss enemy | 2×2 character, health system | Imposing guardian |
| 103 | Boss pattern | Telegraph → charge → recover | Learnable attacks |
| 104 | Boss health bar | Character-based depletion | Visible progress |
| 105 | Boss phase 2 | Pattern change at 50% health | Escalation |
| 106 | Boss defeat | Room reward, victory fanfare | Triumph |
| 107 | Secret walls | Walk through specific walls | Hidden passages |
| 108 | Traps | Floor triggers: spikes, pits | Careful navigation |
| 109 | Magic items | Speed potion, invisibility, map reveal | Special powers |
| 110 | Item combination | Use two items together for final area | Puzzle depth |
| 111 | 128K extra rooms | Memory paging ($7FFD) for additional content | Bonus areas |
| 112 | Integration | Darkness tuning, boss fairness, item balance | Atmospheric and fair |

**Key Teaching Moment (Unit 97):**
Fog of war is pure attribute manipulation. Set all room attributes to INK 0 / PAPER 0. Then restore original attributes only within the light radius. The bitmap stays in screen memory — hidden graphics are invisible because INK equals PAPER. Revealing a cell is a single attribute write. The entire technique is enabled by the system that makes the Spectrum the Spectrum.

**Key Teaching Moment (Unit 102):**
A 2×2 boss occupies four attribute cells. Movement updates four positions. Collision checks four cells. The state machine: idle → telegraph → attack → recover. Telegraphing gives the player time to react — tense but fair.

**End of Phase 7:** Fog of war, torchlight, bosses, secrets, traps. The keep is atmospheric and memorable.

---

## Phase 8: Escape (Units 113–128)

**Goal:** Commercial release quality — the complete package.
**Z80 Focus:** Keyboard matrix, code optimisation, TAP/TZX formats, memory management.

| Unit | You Add | Z80 Skill | Result |
|------|---------|----------|--------|
| 113 | High score table | Multi-byte comparison, sorted insertion | Top 5 scores |
| 114 | Name entry | Full keyboard matrix scanning | 3-letter initials |
| 115 | High scores on title | Display integration, 128K persistence | Bragging rights |
| 116 | Difficulty select | Menu system, key cursor | Easy/Normal/Hard |
| 117 | Difficulty affects gameplay | Parameter tables per level | Real difference |
| 118 | Continue system | Resume from save point | Forgiveness |
| 119 | Ending sequence | Escape to daylight, victory screen | **Narrative reward** |
| 120 | Credits | Scrolling text with colour effects | Attribution |
| 121 | Attract mode | Recorded input playback | Demo mode |
| 122 | Demo on title timeout | Timer-triggered transition | Shop display |
| 123 | Loading screen | Character art before game loads | Presentation |
| 124 | Two-player alternating | Turns, separate scores | Social play |
| 125 | 48K memory audit | Fit in ~42KB, remove waste | All Spectrums |
| 126 | Final testing | Edge cases, balance, difficulty curve | Release quality |
| 127 | TAP/TZX creation | Tape format, turbo loading | Distribution |
| 128 | **Complete game** | Final build, documentation | **Ship it** |

**End of Phase 8:** A game worthy of the Crash magazine pages. High scores, attract mode, two-player, 48K/128K support, and a proper ending.

---

## Spectrum-Specific Debugging (Throughout)

**Attribute Issues:**
- Wrong colour? Check attribute byte format: `FBPPPIII`. INK is bits 0–2, PAPER is bits 3–5
- Colour clash? Only one INK and one PAPER per 8×8 cell. Keep entities in separate cells
- BRIGHT not working? Bit 6 must be set. Check `BIT 6,(HL)` / `SET 6,(HL)`
- FLASH won't stop? Clear bit 7: `RES 7,(HL)`

**Screen Memory Issues:**
- Pixels in wrong row? The thirds layout is non-linear. Use a lookup table, not arithmetic
- Garbled display? Check you're writing to screen ($4000+) not attributes ($5800+)
- Slow writes? $4000–$7FFF is contended memory — ULA steals cycles during display

**Movement Issues:**
- Player walks through walls? Check attribute BEFORE moving, not after
- Player stuck? After blocking, ensure position hasn't already updated
- Wrong direction? Y increases downward on the Spectrum

**Sound Issues:**
- No beeper sound? Check bit 4 of the OUT value, not bits 0–2 (those are border colour)
- AY silent? Register select ($FFFD) then value ($BFFD) — order matters
- Music stutters? Ensure IM 2 handler is fast enough to complete before next interrupt

**General Z80 Issues:**
- Values corrupted after interrupt? Handler must save/restore AF, BC, DE, HL
- LDIR copies wrong data? HL = source, DE = destination, BC = count. Check all three
- 128K detection wrong? Write a unique value to AY, read it back. Zero means no AY

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 4 (Unit 64) | Phase 8 (Unit 128) |
|--------|-------------------|--------------------|--------------------|
| Graphics | Attribute blocks, ROM font | + room themes, fast transitions | UDGs, animation, fog of war |
| World | 1 room | 16+ rooms, map, themes | + secrets, 128K extras, ending |
| Enemies | None | + patrol types, multiple per room | + bosses, dark room encounters |
| Puzzles | Collect all, exit | + keys, doors, one-way passages | + item combinations, traps |
| Audio | Single beeper tone | + effect library, 128K AY detected | Full music, interrupt-driven |
| Features | Walk + collect + exit | + inventory, map, save points | High scores, attract, 2-player |
| Z80 Skill | LD, CP, JR, DJNZ | + LDIR, RLE, 16-bit | Full instruction set, IM 2, paging |

---

## What This Teaches Beyond the Game

By completing Shadowkeep, learners are ready for:
- **Shatter (Game 2):** Attribute collision transfers to breakout physics. Pixel movement from Phase 5 enables ball trajectory
- **Cavern (Game 3):** Character-cell movement becomes platformer physics. Gravity and jumping layer on top of the movement system
- **Ink War (Game 5):** Attributes become the core strategic mechanic. Everything Shadowkeep teaches about attributes is foundation
- **Blitz (Game 9):** Screen memory mastery enables software scrolling — the Spectrum's hardest technique
- **Every future game:** Attribute-based design, UDG graphics, beeper/AY audio, 48K/128K detection, and the screen memory layout are reused throughout the curriculum

Shadowkeep isn't just Game 1. It's the foundation.

---

**Version:** 1.0
**Last Updated:** 2026-02-06
