# Full Game Outline: ZX Spectrum Gravelight (128 Units)

**Game:** Gravelight (Game 1)
**Units:** 128 (8 phases × 16 units)
**Genre:** Single-screen platformer
**Inspired by:** Manic Miner, Jet Set Willy, Monty on the Run
**Target Quality:** Commercial-grade single-screen platformer (1984–85 era)

---

## Premise

Deep beneath the hills, the old mine shafts still glow. Crystals embedded in the rock give off a faint light — gravelight, the miners called it. The shafts collapsed decades ago, but the crystals remain, scattered across crumbling platforms and guarded by creatures that made the darkness their home.

You descend. Twenty levels of platforms, hazards, and creatures stand between you and the deepest crystal — the Heartstone. Each level fits on a single screen. Collect every crystal, reach the exit, descend further. The mine gets darker and more dangerous as you go. The creatures get faster. The platforms get trickier. The gravelight gets dimmer.

---

## What Makes This "Spectrum"

The attribute system IS the game:
- **INK colour = terrain type.** Blue = solid rock (wall). Cyan = platform (walkable). White = crystal (collectible). Yellow = exit (goal).
- **BRIGHT = active items.** BRIGHT crystals haven't been collected. Dim ones have.
- **FLASH = danger.** FLASH on a cell means instant death — acid pools, electrical arcs, crushing hazards.
- **PAPER = background.** Black paper for most levels. Different paper colours for themed zones.
- **Collision detection = one attribute read.** Check the INK colour at the target cell. One instruction. No hitbox maths, no sprite overlap checks. The attribute system makes collision trivially efficient.

Colour clash — the Spectrum's most famous limitation — is embraced. The player moves on an 8-pixel grid (character cells). Platforms are character-cell aligned. This isn't a constraint; it's the design. Manic Miner worked the same way.

---

## Design Philosophy

- **Attributes from Unit 1** — the Spectrum's defining feature is the first thing taught
- **Gravity by Unit 6** — the learner feels platformer physics early
- **Playable level by Unit 16** — complete single-screen platformer by end of Phase 1
- **Colour is gameplay** — INK means terrain, BRIGHT means item, FLASH means hazard
- **Character-cell movement** — 8-pixel grid, matching the attribute grid perfectly
- **Beeper sound from Unit 12** — not silent until late game
- **20 levels, not 20 rooms** — single-screen levels, each a self-contained puzzle
- **48K and 128K** — core game fits 48K, 128K gets AY music and extra levels
- **Commercial quality by Unit 128** — worthy of the CRASH! Live stage

---

## Z80 Assembly Progression

| Phase | Z80 Focus |
|-------|-----------|
| 1 (Descent) | LD, INC/DEC, JP/JR, CP, AND/OR, CALL/RET, IN/OUT, DJNZ, BIT/SET/RES |
| 2 (Hazards) | Indirect addressing (HL), lookup tables, multi-field data structures |
| 3 (Creatures) | XOR for animation, array processing, FRAMES system variable, timer management |
| 4 (The Shafts) | LDIR/LDDR block operations, RLE compression, contended memory timing |
| 5 (Gravelight) | Screen memory thirds, bit shifts (SLA/SRL/RLC), UDG definition, pixel plotting |
| 6 (Echoes) | Timing loops for beeper, AY register access, IM 2 interrupt mode, DI/EI |
| 7 (The Deep) | 128K memory paging ($7FFD), dynamic attribute manipulation, state machines |
| 8 (Heartstone) | Keyboard matrix scanning, TAP/TZX file creation, memory audit, optimisation |

---

## Phase 1: Descent (Units 1–16)

**Goal:** One playable level — move, jump, collect crystals, reach the exit.
**Z80 Focus:** Registers, basic addressing, loops, conditions, ports.
**The Spectrum way:** Attributes ARE the game world. One attribute read = collision detection.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 1 | Coloured block on screen | `LD A,n` / `LD (addr),A`, attribute addresses | See a colour |
| 2 | Attribute byte anatomy | `AND`/`OR` for INK, PAPER, BRIGHT, FLASH bits | Understand colours |
| 3 | Level drawn from attributes | `DJNZ` loop, attribute fill | Platforms and walls visible |
| 4 | Keyboard input | `IN A,($FE)`, row selection, key detection | Read key presses |
| 5 | Player character on screen | Write to screen RAM, position tracking | **Character visible** |
| 6 | Horizontal movement | `INC`/`DEC`, `CP`/`JR` boundary check | Move left/right on 8-pixel grid |
| 7 | Wall collision | Read attribute at target cell, check INK colour | **Walls block movement** |
| 8 | Gravity | Check attribute below player each frame; if not platform, fall | Player falls |
| 9 | Landing on platforms | Detect platform below (INK = cyan), stop falling | **Stand on platforms** |
| 10 | Jumping | Key press sets upward velocity; gravity decays it | **Jump arc** |
| 11 | Jump collision | Check attribute above during ascent; ceiling stops jump | Head-bonk on rock |
| 12 | Beeper sound | `OUT ($FE),A` bit 4 toggle, timing loop | Jump and land sounds |
| 13 | Crystal items | BRIGHT attribute marks crystals; collect on touch, `RES 6,(HL)` | **Shining crystals** |
| 14 | Crystal counter | `CALL` ROM routine, number display | "Crystals: 3/8" |
| 15 | Exit door | Specific attribute marks exit; opens when all crystals collected | **Goal visible** |
| 16 | Level complete | All crystals → exit opens, touch exit → victory fanfare, level done | **Playable level** |

**Attribute as Game Language:**
```z80
; Check what's at the target position before moving
; INK 1 (blue) = rock wall
; INK 5 (cyan) = platform
; INK 7 (white) + BRIGHT = crystal
; INK 6 (yellow) = exit
; FLASH set = hazard (any INK)

check_cell:
    ld a,(hl)           ; Read attribute at target cell
    bit 7,a             ; FLASH bit set?
    jr nz,hazard_hit    ; Yes → damage player
    bit 6,a             ; BRIGHT bit set?
    jr nz,check_crystal ; Might be a crystal
    and $07             ; Isolate INK colour (bits 0-2)
    cp 1                ; INK 1 = rock wall?
    jr z,blocked        ; Yes → can't move
    cp 5                ; INK 5 = platform?
    jr z,on_platform    ; Yes → solid ground
    cp 6                ; INK 6 = exit?
    jr z,check_exit     ; Yes → check if all crystals collected
    jr open_space       ; Otherwise → air, fall through
```

**Gravity Implementation:**
```z80
; Each frame: check if the player is standing on something solid
; If not, fall one character cell downward

apply_gravity:
    ld a,(player_y)
    inc a                   ; Cell below player
    ld h,a
    ld a,(player_x)
    ld l,a
    call get_attribute      ; Read attribute at (player_x, player_y+1)
    and $07                 ; Isolate INK
    cp 5                    ; Platform?
    ret z                   ; Yes → standing, don't fall
    cp 1                    ; Wall?
    ret z                   ; Yes → standing on wall
    ; Not standing on anything → fall
    ld a,(player_y)
    inc a
    ld (player_y),a
    ret
```

**If it doesn't work (Phase 1):**
- **No colour?** Check you're writing to $5800+ (attributes), not $4000+ (bitmap)
- **Wrong cell?** Address = $5800 + (row × 32) + column. Rows 0–23, columns 0–31
- **Falls through platforms?** Check attribute BELOW player, not AT player position
- **Jump doesn't work?** Velocity must be negative (upward). Gravity adds positive (downward) each frame
- **Can't collect crystals?** Check BRIGHT bit (bit 6) AND INK colour, not just one
- **Items don't disappear?** `RES 6,(HL)` clears the BRIGHT bit at attribute address HL

**End of Phase 1:** Playable single-screen platformer. Jump between platforms, collect crystals, reach the exit. The attribute system proven as game design tool. Looks like Manic Miner.

---

## Phase 2: Hazards (Units 17–32)

**Goal:** Moving platforms, crumbling platforms, hazard types, multiple levels.
**Z80 Focus:** Indirect addressing (HL), lookup tables, 16-bit arithmetic, data structures.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 17 | Moving platforms | Horizontal platform shifts each frame via attribute writes | Dynamic level |
| 18 | Platform ride | Player moves with platform if standing on it | **Ride moving platforms** |
| 19 | Crumbling platforms | Platform disappears N frames after first touch | Tension |
| 20 | Conveyor belts | Platform pushes player left or right | Directional force |
| 21 | FLASH hazards | Acid pools, electrical arcs — FLASH attribute = instant death | Visual danger |
| 22 | Hazard animation | FLASH cycles automatically (hardware) — no CPU cost | Free animation |
| 23 | Lives system | 3 lives, death animation, respawn at level start | Stakes |
| 24 | Death sound | Beeper: descending tone | Audio feedback |
| 25 | Air supply | Timer counts down — reach exit before air runs out | Time pressure |
| 26 | Air bar display | Character-based bar depletes in status area | Visible urgency |
| 27 | Level data format | Byte array: 32×24 attributes + metadata (crystals, air, start pos) | Data-driven levels |
| 28 | Second level | Load level 2 from data, different layout | Progression |
| 29 | Level transition | Clear screen, "LEVEL 2" text, draw new level | Pacing |
| 30 | Five levels | 5 distinct layouts with escalating hazards | Variety |
| 31 | Level themes | Different PAPER colour per level zone (black, blue, green) | Visual progression |
| 32 | Integration + balance | Hazard placement, air timing, platform routes | Fair but challenging |

**Key Teaching Moment (Unit 17):**
Moving platforms are attribute manipulation in real-time. Each frame: clear the platform's old position (write PAPER-only attribute), write the platform at its new position (write platform attribute). The platform moves because the attributes move. No sprites, no bitmap work — pure attribute animation.

**Key Teaching Moment (Unit 22):**
FLASH is free animation. Set bit 7 on a hazard cell's attribute and it blinks automatically — the ULA handles it. No CPU cycles, no frame counting, no code. This is the Spectrum giving you something for nothing: a visual danger indicator that costs zero performance.

**End of Phase 2:** Moving platforms, crumbling floors, conveyors, hazards, air supply, 5 levels. The game has genuine challenge and variety.

---

## Phase 3: Creatures (Units 33–48)

**Goal:** Enemies that patrol, chase, and guard crystals.
**Z80 Focus:** Array processing, XOR for animation, FRAMES variable, timer management.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 33 | Enemy character | Second character on screen, position tracked | Creature visible |
| 34 | Horizontal patrol | Direction toggles on wall/edge hit | Back-and-forth movement |
| 35 | Vertical patrol | Same logic, vertical axis — climbing creatures | Up-and-down |
| 36 | Enemy-platform collision | Enemies walk on platforms, fall off edges (or turn) | Enemies respect terrain |
| 37 | Enemy touches player | Position comparison: same cell = death | **Contact kills** |
| 38 | Enemy animation | `XOR` to toggle between two character codes | Visual life |
| 39 | Multiple enemies | Enemy data table: position, direction, speed, type. `DJNZ` loop | Several per level |
| 40 | Speed variety | Speed field: move every N frames, different N per enemy | Fast and slow creatures |
| 41 | Flying enemies | Ignore gravity, move freely (bats, ghosts) | Air threats |
| 42 | Chaser enemies | Move toward player position each N frames | Active pursuit |
| 43 | Invincibility frames | FRAMES variable ($5C6A) timer after hit | Brief immunity |
| 44 | Border flash on hit | `OUT ($FE)` border colour change | Dramatic feedback |
| 45 | Enemy spawn per level | Level data includes enemy definitions | Level-specific creatures |
| 46 | Enemy variety | Different UDG per type (crawler, bat, ghost) — Phase 5 adds graphics, Phase 3 uses placeholders | Type distinction |
| 47 | Level 6-10 | 5 more levels using all hazard and enemy types | Expanded content |
| 48 | Integration + balance | Enemy placement, speed tuning, fairness | Tense but learnable |

**Key Teaching Moment (Unit 36):**
Enemy-platform collision reuses the player's gravity check: read attribute below enemy, if not platform, fall (or turn around for non-flying types). One collision routine serves both player and enemies. The attribute system's consistency means every entity plays by the same rules.

**Key Teaching Moment (Unit 38):**
`XOR` flips bits. If character codes are $80 and $81, `XOR $01` toggles between them instantly — one instruction, no branch. Faster than compare-and-branch, generalises to any pair. This is the Z80 programmer's animation trick.

**End of Phase 3:** Crawlers, bats, ghosts, and chasers guard the crystals. 10 levels of platforming with enemies. The mine is dangerous.

---

## Phase 4: The Shafts (Units 49–64)

**Goal:** 20 levels, compressed data, a map screen, polished progression.
**Z80 Focus:** LDIR block operations, RLE compression, contended memory, 16-bit arithmetic.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 49 | LDIR block copy | `LDIR` for fast memory fill | Instant level draw |
| 50 | Level buffer | Working buffer: decompress → modify → display | Levels reset on death |
| 51 | Run-length encoding | Compression: value + count pairs | Compact level storage |
| 52 | RLE decompression | Expand to attribute buffer, then LDIR to screen | Levels from compressed data |
| 53 | 20 levels | Full level set, index lookup | Complete game content |
| 54 | Level themes | 4 zones of 5 levels each: Shallows (cyan), Depths (blue), Fungus (green), Core (red) | Visual progression |
| 55 | 16-bit level pointers | `LD HL,(addr)` for level address table | Efficient level lookup |
| 56 | Map screen | Show all 20 levels as a grid; completed levels marked | **Player orientation** |
| 57 | Password system | 4-letter code per zone start (levels 1, 6, 11, 16) | Resume progress |
| 58 | Contended memory | $4000–$7FFF timing penalty — why screen writes are slow | Understanding hardware |
| 59 | Fast attribute fill | Write outside contended window, or accept the cost | Practical timing |
| 60 | Difficulty curve | Level ordering: easy → hard within each zone, reset at zone boundary | Pacing |
| 61 | Bonus levels | Hidden levels accessed via secret exits | Reward exploration |
| 62 | Score multiplier | Collecting crystals quickly = combo bonus | Skill reward |
| 63 | Per-level par time | Beat the par = bonus points | Speedrun incentive |
| 64 | Integration + balance | Full 20-level playthrough, route through zones | Complete and balanced |

**Key Teaching Moment (Unit 49):**
`LDIR` copies BC bytes from HL to DE. One instruction replaces an entire loop. Level transitions go from multi-frame redraws to near-instant: decompress to buffer, then LDIR the buffer to attribute RAM. This is the Z80's genuine luxury.

**Key Teaching Moment (Unit 51):**
An uncompressed level is 768 bytes (32×24 attributes). Twenty levels = 15KB. With RLE compression (3:1 typical for platformer levels), the same content fits in 4-5KB. Compression isn't academic — it's how Manic Miner's 20 levels fit in 48K alongside the code, graphics, and music.

**End of Phase 4:** 20 levels across 4 themed zones. RLE compressed. Map screen. Password system. The game is content-complete.

---

## Phase 5: Gravelight (Units 65–80)

**Goal:** UDG characters, pixel work, animation — the visual transformation.
**Z80 Focus:** Screen memory thirds, bit shifts, UDG definition, pixel plotting.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 65 | UDG basics | Write 8 bytes to UDG area | First custom character |
| 66 | Player UDG | Miner figure: helmet, lamp, boots | **Recognisable player** |
| 67 | Player walk animation | 2-4 UDG frames per direction | Animated movement |
| 68 | Jump and fall frames | Mid-air pose, landing crouch | Expressive physics |
| 69 | Enemy UDGs | Crawler (insect), bat (wings), ghost (wispy), chaser (eyes) | Distinct creatures |
| 70 | Enemy animation | 2-frame cycle per enemy type | Living creatures |
| 71 | Platform UDGs | Stone, wood, crystal, crumbling (cracked) | Textured terrain |
| 72 | Screen memory layout | The thirds formula, row address lookup table | **Spectrum rite of passage** |
| 73 | Pixel plotting | Set/clear individual pixels via bit shifts | Fine detail |
| 74 | Crystal sparkle | Pixel animation on BRIGHT cells — brief twinkle | Collectibles glow |
| 75 | Death animation | Player breaks apart (2-3 UDG frames) | Dramatic death |
| 76 | Level transition effect | Wipe: attribute fill line-by-line, or dissolve pattern | Polished transitions |
| 77 | Title screen | "GRAVELIGHT" in custom characters with crystal motif | Presentation |
| 78 | Zone colour themes | Different wall/platform UDGs per zone | Zone identity |
| 79 | Status bar polish | Custom font, crystal icon, air bar design | Professional HUD |
| 80 | Integration | Colour clash audit, visual consistency across 20 levels | Cohesive look |

**Key Teaching Moment (Unit 72):**
The screen memory layout is the Spectrum's most infamous quirk. Pixel rows are interleaved in thirds:
- Bits 7-6 of Y select the third (0, 1, or 2)
- Bits 5-3 select the character row within the third
- Bits 2-0 select the pixel row within the character

A lookup table (24 entries for 192 pixel rows) avoids runtime calculation. This is the rite of passage — every Spectrum programmer learns this.

**End of Phase 5:** UDG characters transform the game from coloured blocks to an atmospheric mine. The miner has a walk cycle. Creatures are recognisable. Platforms have texture. It looks like a commercial release.

---

## Phase 6: Echoes (Units 81–96)

**Goal:** Sound — beeper and AY. Music and effects that bring the mine to life.
**Z80 Focus:** Timing loops, AY registers, interrupt mode 2.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 81 | Beeper fundamentals | `OUT ($FE),A` bit 4, timing loop = pitch | First controlled tone |
| 82 | Pitch table | Loop lengths for musical notes | Tuneable pitch |
| 83 | Sound effect library | Parameterised routine: pitch, duration, sweep | Jump, land, collect, die, hazard |
| 84 | Pitch slides | Sweep delay value over time | Crystal collect: ascending slide |
| 85 | Multi-tone | Rapid frequency alternation | Richer beeper sound |
| 86 | Beeper music | Note sequence + timing playback | 48K title music |
| 87 | In-game beeper | Brief sound phrases between frames | Ambient mine sounds |
| 88 | AY-3-8912 basics | Register access via $FFFD/$BFFD, 3 voices | **128K sound chip** |
| 89 | AY sound effects | Hardware envelopes, noise channel for crumbling | Richer effects |
| 90 | AY music engine | 3-voice playback, pattern data | Background music |
| 91 | Per-zone themes | Different AY music per zone (eerie, tense, ominous, triumphant) | Musical progression |
| 92 | Interrupt mode 2 | `IM 2`, vector table, 50Hz handler | **Music during gameplay** |
| 93 | 48K/128K detection | AY register write/read test | Automatic audio selection |
| 94 | SFX over music | Temporarily steal AY voice for effects, restore | Layered audio |
| 95 | Audio balance | Volume levels, SFX priority, music doesn't drown effects | Professional mix |
| 96 | Integration | All audio paths tested on 48K and 128K | Cohesive sound |

**Key Teaching Moment (Unit 81):**
The 48K beeper is one bit on one port. A timing loop toggles it: longer loop = lower pitch, shorter = higher. Sound blocks the CPU — the fundamental constraint shaping all 48K audio. Brief effects between frames, not continuous music.

**Key Teaching Moment (Unit 92):**
`IM 2` with a vector table drives a 50Hz interrupt handler. The handler calls the AY music sequencer: read next note, write frequency registers, advance pattern position. Music plays automatically while the game runs. This is how every commercial 128K game handles background audio.

**End of Phase 6:** Full audio for both models. 48K gets beeper effects and title music. 128K gets 3-voice AY soundtrack with per-zone themes and interrupt-driven playback.

---

## Phase 7: The Deep (Units 97–112)

**Goal:** Darkness, atmosphere, boss levels, advanced mechanics.
**Z80 Focus:** Dynamic attribute manipulation, 128K memory paging, complex state machines.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 97 | Fog of war | Distant attributes set to black-on-black | **Limited visibility** |
| 98 | Light radius | Manhattan distance from player position | Reveal nearby cells |
| 99 | Lamp mechanic | Light radius shrinks over time; collect lamp oil to restore | Resource management |
| 100 | Flickering edge | FLASH on radius boundary | Torchlight atmosphere |
| 101 | Dark level enemies | Only visible within light radius | Surprise encounters |
| 102 | Boss level | Every 5th level: large enemy (2×2 UDGs), health bar, pattern attacks | **Guardian encounters** |
| 103 | Boss pattern | Telegraph → attack → recover → repeat. Learnable, fair. | Pattern design |
| 104 | Boss health bar | Character-based depletion in status area | Visible progress |
| 105 | Boss defeat | Victory fanfare, zone complete, bonus points | Triumph |
| 106 | Gravity wells | Cells that pull the player downward faster | Environmental hazard |
| 107 | Springboards | Cells that launch the player upward (higher than normal jump) | Vertical traversal |
| 108 | Breakable walls | Specific walls destroyed after N jumps against them | Hidden routes |
| 109 | Secret crystals | Hidden BRIGHT cells revealed only in light radius or after breaking walls | Exploration reward |
| 110 | 128K extra levels | Memory paging ($7FFD) for 4 bonus levels | Reward for 128K owners |
| 111 | Level select (128K) | After completion: replay any level for score attack | Replayability |
| 112 | Integration | Darkness tuning, boss fairness, secret placement | Atmospheric and fair |

**Key Teaching Moment (Unit 97):**
Fog of war is pure attribute manipulation. Set all level attributes to INK 0 / PAPER 0. Then restore original attributes only within the light radius of the player. The bitmap data stays in screen memory — hidden graphics are invisible because INK equals PAPER. Revealing a cell is a single attribute write. The entire technique costs almost nothing and is uniquely Spectrum.

**End of Phase 7:** Darkness, lamp resource, boss encounters, springboards, breakable walls, 128K bonus levels. The mine is atmospheric and deep.

---

## Phase 8: Heartstone (Units 113–128)

**Goal:** Commercial release quality — the complete package for CRASH! Live.
**Z80 Focus:** Keyboard matrix, TAP/TZX formats, memory audit, optimisation.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 113 | High score table | Multi-byte comparison, sorted insertion | Top 5 scores |
| 114 | Name entry | Full keyboard matrix scanning ($FE rows) | 3-letter initials |
| 115 | High scores on title | Integrated display, 128K disk persistence | Bragging rights |
| 116 | Difficulty select | Menu: Easy (5 lives, slow enemies), Normal (3 lives), Hard (2 lives, fast) | Accessibility |
| 117 | Difficulty parameters | Speed, enemy count, air supply, light radius per difficulty | Real difference |
| 118 | Ending sequence | Reach the Heartstone: screen fills with light, mine transforms, surface reached | **Narrative reward** |
| 119 | Credits | Scrolling text with crystal sparkle effects | Attribution |
| 120 | Attract mode | Recorded input replays level 1 | Demo mode |
| 121 | Attract on title timeout | 10-second timer → demo starts | Professional presentation |
| 122 | Loading screen | Character art displayed during tape load | First impression |
| 123 | Turbo loader | Faster-than-ROM loading routine | Reduced load time |
| 124 | 48K memory audit | Fit in ~42KB: code + 20 levels compressed + UDGs + music | All Spectrums |
| 125 | 128K memory map | Extra levels in paged RAM, AY music data | Best experience |
| 126 | Final testing | Every level, every enemy, every platform, every difficulty | Release quality |
| 127 | TAP/TZX creation | Tape format headers, turbo blocks | Distribution |
| 128 | **The finished game** | Build, test, document | **Ship it at CRASH! Live** |

**End of Phase 8:** A game worthy of the CRASH! Live stage. 20+ levels, 4 bosses, fog of war, dual audio, high scores, attract mode, turbo loading, and a proper ending.

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 4 (Unit 64) | Phase 8 (Unit 128) |
|--------|-------------------|--------------------|--------------------|
| Graphics | Attribute blocks, ROM font | + zone themes, fast transitions | UDGs, animation, fog of war |
| World | 1 level | 20 levels, map, passwords | + boss levels, secrets, 128K extras |
| Enemies | None | + 4 types, multiple per level | + bosses, dark-room encounters |
| Mechanics | Walk + jump + collect | + hazards, moving/crumbling platforms | + darkness, springboards, breakable walls |
| Audio | Single beeper tone | + effect library | Full AY music, interrupt-driven |
| Features | Jump + collect + exit | + air supply, combos, par times | High scores, attract, difficulty, turbo load |
| Z80 Skill | LD, CP, JR, DJNZ | + LDIR, RLE, 16-bit | Full instruction set, IM 2, paging |

---

## CRASH! Live Milestone Plan

For the October launch, not all 128 units need to be published. The minimum viable showcase:

- **Phase 1 complete (units 1-16):** Playable single-screen platformer. This alone is demonstrable.
- **Phase 2 complete (units 17-32):** Moving platforms, hazards, 5 levels. A real game.
- **Phases 3-4 in progress:** Enemies and 20 levels. Enough for a compelling demo.

The first 32 units (Phases 1-2) should be the priority for October. They produce a playable, visually interesting game that demonstrates the teaching approach. Phases 3-8 can follow post-launch.

---

## What This Teaches Beyond the Game

By completing Gravelight, learners are ready for:
- **Ionfire (Game 2):** Screen memory mastery from Phase 5 enables software scrolling. Gravity physics from Phase 1 transfer to ship movement. Beeper/AY skills from Phase 6 provide the soundtrack.
- **Grimstone (Game 3):** Attribute manipulation and UDG skills transfer directly to isometric rendering. The compression from Phase 4 handles larger worlds. 128K paging enables the room count.
- **Capstone (Game 4):** Every technique from Gravelight is foundation. The capstone combines scrolling (Game 2), isometric (Game 3), and all of Gravelight's polish into a commercial release.
- **Every future Spectrum game:** Attribute-based design, UDG graphics, beeper/AY audio, 48K/128K detection, screen memory layout, and LDIR block operations are reused throughout.

Gravelight isn't just Game 1. It's the foundation.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Replaces Shadowkeep (top-down maze) with Gravelight (single-screen platformer). Retains Z80 progression and attribute-first teaching from Shadowkeep. Adds platformer mechanics (gravity, jumping, platforms, air supply) and CRASH! Live milestone plan.
