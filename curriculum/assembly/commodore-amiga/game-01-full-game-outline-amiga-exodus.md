# Full Game Outline: Amiga Exodus (128 Units)

**Game:** Exodus (Game 1)
**Units:** 128 (8 phases x 16 units)
**Target Quality:** Commercial-grade terrain puzzle (1989-90 era)
**Comparable To:** PD puzzle games -> evolving to Lemmings, The Humans-level polish by completion

---

## What Makes This "Amiga"

The Amiga has three custom chips working in concert:
- **Agnus** -- DMA controller, Blitter (hardware rectangle copier), Copper (display list coprocessor)
- **Denise** -- Display output, 8 hardware sprites (16px wide), playfield rendering
- **Paula** -- 4 channels of 8-bit sampled audio, disk I/O

And supporting them:
- **68000 CPU** -- 16/32-bit processor with 8 data registers (D0-D7) + 7 address registers (A0-A6), real multiply/divide
- **Chip RAM** -- all graphics, sound, and DMA data must live here (512KB on A500)
- **Bootable disks** -- programs boot from ADF images via Kickstart

This terrain puzzle makes the Blitter the game design tool. Digging a tunnel is a Blitter clear. Building a bridge is a Blitter copy. Testing if terrain exists below a creature is a Blitter comparison. Every game action is a hardware operation -- learners see the chipset working because it IS the gameplay. The Copper splits the screen for the UI panel. Paula plays satisfying terrain sounds. The 68000 orchestrates the creatures. The result is unmistakably Amiga.

---

## Design Philosophy

- **Blitter from Unit 1** -- the Amiga's defining feature is the first thing taught
- **Bootable from Unit 1** -- learners can run their game immediately
- **One concept per unit** -- never overwhelming
- **Always playable** -- from Unit 5 onwards, creatures walk
- **Terrain IS gameplay** -- bitmap modification as core mechanic, not just decoration
- **Copper from Unit 1** -- the display list that defines Amiga graphics
- **Sampled sound from Unit 8** -- that Amiga audio quality, early
- **Debugging inline** -- every unit includes "if it doesn't work"
- **68000 skill per unit** -- assembly concepts build alongside the game
- **Commercial quality by Unit 128** -- a real game

---

## 68000 Assembly Progression

| Phase | 68000 Focus |
|-------|-----------|
| 1 (Landfall) | MOVE.B/W/L, D0-D7/A0-A7 registers, addressing modes, BEQ/BNE, BSR/RTS, Copper list format |
| 2 (Excavation) | Blitter registers, minterms, bitwise ops (AND/OR/EOR), MULU for offset calculation |
| 3 (Guidance) | MOVEM for register save/restore, BTST for input, subroutine parameter patterns, DBRA loops |
| 4 (Pathways) | Address register indirect with displacement, LEA for address calculation, word alignment |
| 5 (Copper Sky) | Copper instruction timing, bitplane pointer arithmetic, DMA scheduling |
| 6 (Resonance) | Paula registers, DMA audio, CIA timer interrupts, data-driven sequencing |
| 7 (Cascade) | Complex data structures, optimised Blitter scheduling, performance profiling |
| 8 (Salvation) | System restoration (Exec), memory management, disk I/O, optimisation techniques |

By Unit 128, learners have a working knowledge of the 68000 instruction set, the OCS custom chipset, and the DMA-driven architecture that makes the Amiga unique.

---

## Phase 1: Landfall (Units 1-16)

**Goal:** Creatures walking across bitmap terrain. Display setup, Copper list, basic creature AI.
**68000 Focus:** MOVE, registers, addressing modes, branches, subroutines.
**The start:** A Copper list, bitplane display, and bitmap terrain. Creatures walk, fall, turn at walls. The foundation of everything.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 1 | Bootable ADF + Copper list + coloured screen | `MOVE.L`, custom register writes, Copper WAIT/MOVE | Coloured display |
| 2 | Bitplane display | Bitplane pointers in Copper, `BPLCON0` setup | Bitmap visible |
| 3 | Draw terrain (filled rectangle) | Direct memory writes to bitplane data, pixel addressing | Land on screen |
| 4 | Creature sprite on screen | Hardware sprite data, sprite pointers in Copper | **Creature visible** |
| 5 | Creature walks right | Position increment per frame, `ADD.W` | Movement |
| 6 | Creature turns at screen edge | `CMP.W` boundary check, direction toggle | Back and forth |
| 7 | Terrain collision (floor check) | Read pixel below creature's feet from bitplane | **Creature respects terrain** |
| 8 | Creature falls without floor | Gravity: descend when no pixel below | Falls into gaps |
| 9 | Terrain sound (footstep sample) | Paula: sample pointer, length, period, volume, DMA trigger | Audio feedback |
| 10 | Multiple creatures | Creature data table, `BSR`/`RTS` subroutines, loop | Several walking |
| 11 | Exit zone | Target area on right side, detect creature arrival | **Goal defined** |
| 12 | Creature count display | Copper screen split, text in lower panel | Saved / Total |
| 13 | Score: creatures saved | Increment on arrival, display update | Progress |
| 14 | Level complete | All creatures arrived or lost, result screen | End condition |
| 15 | Title screen | Copper gradient background, text rendering | Feels real |
| 16 | Integration + polish | Creature spacing, fall speed, terrain shape | Solid foundation |

**Amiga-Specific Unit 1:**
```asm
; Copper list (must be in Chip RAM)
copper_list:
    dc.w $0100,$0200    ; BPLCON0 = 0 bitplanes (colour only)
    dc.w $0180,$0000    ; COLOR00 = black (background)
    dc.w $0182,$0F00    ; COLOR01 = red

    ; Wait for middle of screen
    dc.w $6001,$FFFE    ; WAIT for line $60
    dc.w $0180,$000F    ; COLOR00 = blue

    ; End of Copper list
    dc.w $FFFF,$FFFE    ; WAIT for impossible position (end)

; Point Copper to our list
    lea copper_list,a0
    move.l a0,$DFF080   ; COP1LC = address of Copper list
    move.w #$0000,$DFF088 ; COPJMP1 = restart Copper
```

**If it doesn't work (Unit 1):**
- **No display?** Check DMA is enabled: write `$8380` to `$DFF096` (DMACON) for Copper + bitplane + Blitter DMA
- **Wrong colours?** Copper list must end with `$FFFF,$FFFE`. Missing end = random colours
- **Crashes?** Copper list and all graphics data must be in Chip RAM (first 512KB)
- **Nothing boots?** Bootblock must be at track 0, sector 0 of the ADF. Check disk layout

**End of Phase 1:** Creatures walk across terrain, fall into gaps, arrive at the exit. The display framework is solid. Bootable from disk.

---

## Phase 2: Excavation (Units 17-32)

**Goal:** Blitter terrain modification -- the core game mechanic. Dig, build, and redirect.
**68000 Focus:** Blitter registers, minterms, bitwise operations, MULU for offset calculation.
**Key moment:** The first time a terrain pixel is cleared and a creature walks through the gap. The Blitter IS the game.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 17 | Blitter basics: rectangle clear | `BLTCON0`, `BLTDPT`, `BLTSIZE`, DMA operation | Erase a rectangle |
| 18 | Dig ability | Click to assign digger, creature clears terrain below | **Terrain modification** |
| 19 | Blitter copy: rectangle fill | Source + destination channels, minterm for copy | Fill a rectangle |
| 20 | Build ability | Creature places terrain ahead at current height | Bridge over gap |
| 21 | Blitter line draw | Blitter line mode for angled surfaces | Ramps |
| 22 | Redirect ability | Place a wall that reverses creature direction | Traffic control |
| 23 | Dig sound (sample) | Paula channel 2, digging sample | Satisfying feedback |
| 24 | Build sound (sample) | Paula channel 3, building sample | Construction feel |
| 25 | Blitter wait (DMABUSY) | Poll `$DFF002` bit 14 before next Blitter op | No corruption |
| 26 | Cookie-cut masking | A/B/C/D channels with minterm for masked copy | Clean creature rendering |
| 27 | Creature rendered as BOB | Blitter cookie-cut onto terrain bitplane | Smooth creature on terrain |
| 28 | BOB restore (background save) | Save before draw, restore before next draw | No trails |
| 29 | Multiple abilities active | Different creatures doing different tasks simultaneously | Complex behaviour |
| 30 | Ability limit per level | Counter per ability type, display remaining | Strategy |
| 31 | Undo: stop ability | Cancel current task, creature resumes walking | Correction |
| 32 | Integration + Blitter tuning | Operation timing, visual polish, ability balance | Core mechanic solid |

**Key Teaching Moment (Unit 17):**
The Blitter copies rectangles between memory areas using DMA -- no CPU cycles spent. Set source, destination, size, and the operation (minterm), then trigger. The Blitter runs in the background while the CPU continues. For terrain modification: destination is the bitplane data, the operation is AND with zero (clear) to dig, or OR with ones (set) to build. Hardware does the work.

**Key Teaching Moment (Unit 26):**
Cookie-cut masking uses all four Blitter channels. A = mask (the shape), B = source image (the creature), C = background (existing screen), D = destination (screen). The minterm combines them: `D = (A AND B) OR (NOT A AND C)`. This pastes the creature cleanly onto the background without destroying surrounding pixels. One Blitter operation, perfect compositing.

**Amiga-Specific:**
```asm
; Blitter clear: dig a rectangle in terrain
; A0 = destination address in bitplane
; D0 = width in words, D1 = height in rows
dig_terrain:
    btst #14,$DFF002    ; Wait for Blitter idle
    bne.s dig_terrain

    move.l a0,$DFF054   ; BLTDPTH = destination
    move.w #$0100,$DFF040 ; BLTCON0 = D channel only, minterm $00 (clear)
    move.w #$0000,$DFF042 ; BLTCON1 = no special modes
    move.w d2,$DFF066   ; BLTDMOD = destination modulo
    move.w d3,$DFF058   ; BLTSIZE = height << 6 | width (triggers blit)
    rts
```

**End of Phase 2:** Dig, build, and redirect. The Blitter modifies terrain in real time. Creatures respond to the changed landscape. The core puzzle mechanic works.

---

## Phase 3: Guidance (Units 33-48)

**Goal:** Player interaction -- selecting creatures, assigning abilities, UI panel.
**68000 Focus:** MOVEM for register save, BTST for input, subroutine parameters, DBRA loops.
**Key concept:** The Copper splits the screen: gameplay area above, UI panel below. Mouse input selects creatures and assigns abilities.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 33 | Mouse input | `JOY0DAT` ($DFF00A), button via CIAA PRA | Cursor movement |
| 34 | Cursor sprite | Hardware sprite follows mouse position | Visible cursor |
| 35 | Creature selection | Click near creature, highlight selected | **Direct interaction** |
| 36 | Ability assignment | Click ability in panel, then click creature | Dig/Build/Redirect |
| 37 | Copper screen split | WAIT at panel line, change colours/bitplanes | Gameplay + UI panel |
| 38 | UI panel layout | Ability icons, creature count, timer display | Information display |
| 39 | Ability icons (BOBs) | Blitter-drawn icons in panel area | Clickable buttons |
| 40 | Pause ability | Creature stops walking, blocks others | Traffic jam control |
| 41 | Climb ability | Creature ascends vertical surfaces | Vertical movement |
| 42 | Float ability | Creature falls slowly (reduced gravity) | Safe descent |
| 43 | Explode ability | Creature destroys terrain in radius around itself | Sacrifice play |
| 44 | Selection highlight | Flashing sprite or colour change on selected creature | Clear feedback |
| 45 | Release rate control | Speed up/slow down creature spawn rate | Timing control |
| 46 | Nuke button | Explode all creatures (give up on level) | Reset option |
| 47 | Timer display | Countdown timer, level fails when expired | Time pressure |
| 48 | Integration + UI polish | Click accuracy, ability feedback, panel layout | Usable interface |

**Key Teaching Moment (Unit 37):**
The Copper splits the screen by WAITing for a specific raster line, then changing display parameters. At the panel line: switch to a different set of bitplane pointers (the panel graphics), change palette colours, maybe reduce to fewer bitplanes. The gameplay area and UI panel are independent -- different resolutions, different palettes, different scroll positions. One Copper list, two display zones. This is how Lemmings, Speedball, and every Amiga game with a panel works.

**Key Teaching Moment (Unit 43):**
The explode ability clears a circular area of terrain. The Blitter clears a rectangular region; the circle is approximated by clearing several rectangles of decreasing width at increasing Y offset. Or: pre-calculate a circular mask in memory and use a masked Blitter clear. Either way, terrain vanishes, creatures fall through, and the sacrificed creature is gone. Strategic sacrifice -- the signature Lemmings-style mechanic.

**End of Phase 3:** Full creature interaction. Mouse-driven selection, 7 abilities, Copper screen split, UI panel. The puzzle game is playable.

---

## Phase 4: Pathways (Units 49-64)

**Goal:** Level data, terrain types, and smarter creature AI.
**68000 Focus:** Address register indirect with displacement, LEA, word alignment, data structures.
**Key concept:** Levels are bitmap data loaded from disk. Different terrain types (dirt, rock, steel) respond differently to abilities.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 49 | Level data format | Bitmap terrain stored as compressed data | Structured levels |
| 50 | Level loading from disk | `trackdisk.device` read, decompression to Chip RAM | Levels from ADF |
| 51 | Multiple levels | Level table, load next on completion | Progression |
| 52 | Level select screen | Menu with level names, cursor navigation | Choose level |
| 53 | Terrain type: rock | Different pixel pattern, cannot be dug | Routing constraint |
| 54 | Terrain type: steel | Indestructible, blocks all abilities | Hard boundary |
| 55 | Terrain type: water | Kills creatures on contact, fills spaces | Lethal hazard |
| 56 | Multi-bitplane terrain | 2+ bitplanes for terrain types (colour = type) | Type from colour |
| 57 | Creature AI: wall turn | Smarter turn detection, handle overhangs | Robust walking |
| 58 | Creature AI: crowd behaviour | Creatures interact, queue behind pausers | Group dynamics |
| 59 | Trap door entrance | Creatures spawn from specific point | Level design tool |
| 60 | Multiple entrances | Several spawn points, creatures distributed | Complex flow |
| 61 | Multiple exits | Different target zones, all must be reached | Routing puzzle |
| 62 | Save threshold | "Save 80%" to pass, display target | Difficulty per level |
| 63 | Password system | Level progress encoded as code, entry on title | Persistence |
| 64 | Integration + level design | 8+ levels, varied terrain, difficulty curve | Real content |

**Key Teaching Moment (Unit 56):**
Multiple bitplanes encode terrain type through colour. Bitplane 0 alone (1 bit) means dirt (brown). Bitplane 0 + 1 (2 bits) means rock (grey). Only bitplane 1 means steel (blue). The Blitter checks which bitplane combination exists at a position to determine what the ability can do. Dig checks: is it dirt? If rock or steel, refuse. The display doubles as the data structure.

**Key Teaching Moment (Unit 50):**
Level data lives on the ADF disk. Loading uses `trackdisk.device` -- the Amiga's low-level disk I/O. Read sectors from disk into a Chip RAM buffer, decompress (RLE or similar), and write the result to the bitplane memory. Each level is a bitmap with terrain pre-drawn. Level design happens in a paint program; the game just loads and renders it.

**End of Phase 4:** Multiple levels with different terrain types, multiple entrances/exits, passwords. A real puzzle game with content.

---

## Phase 5: Copper Sky (Units 65-80)

**Goal:** Visual polish to commercial standard. Copper gradients, bitplane art, animation.
**68000 Focus:** Copper instruction timing, bitplane pointer arithmetic, DMA scheduling.
**The moment:** A Copper gradient sky above the terrain transforms the look from functional to beautiful.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 65 | Copper gradient sky | WAIT/MOVE per raster line, colour gradient | **Atmospheric sky** |
| 66 | Dynamic gradient (time of day) | Modify Copper list colours per frame | Living sky |
| 67 | Parallax cloud layer | Separate bitplane with different scroll rate | Depth |
| 68 | Terrain texture detail | Dithering patterns, surface detail in bitplane data | Rich terrain |
| 69 | Creature animation frames | Multiple sprite images, cycle per frame | Walking animation |
| 70 | Ability animation | Dig sparks, build placement, explosion expanding | Visual feedback |
| 71 | Water animation | Cycling colours via Copper for flowing water | Living hazard |
| 72 | Entrance animation | Trap door opens, creatures emerge | Polished spawn |
| 73 | Exit animation | Creatures celebrate on arrival, dance sprites | Satisfying arrival |
| 74 | Palette design per theme | Different colour sets: grass, snow, cave, desert | Visual variety |
| 75 | Background detail | Decorative elements behind terrain (mountains, trees) | Rich environment |
| 76 | Screen transitions | Copper fade to black between levels | Smooth flow |
| 77 | Death animation | Creature "pops" when killed (expanding circle clear) | Clear feedback |
| 78 | Title screen art | Multi-bitplane illustration, Copper colour cycling | Presentation |
| 79 | Level preview | Brief display of terrain before timer starts | Orientation |
| 80 | Integration + visual audit | Copper timing, palette harmony, animation consistency | Looks professional |

**Key Teaching Moment (Unit 65):**
A Copper gradient writes a new colour value to `COLOR00` on every raster line. The Copper WAITs for line N, MOVEs a colour, WAITs for line N+1, MOVEs the next colour. 200 lines = 400 Copper instructions for a smooth gradient from light blue to dark blue. The Copper executes in parallel with the display -- zero CPU cost. This is the effect that makes people say "it looks like an Amiga."

**Key Teaching Moment (Unit 67):**
Parallax: a second bitplane set scrolls at half the camera speed. The Copper points to different bitplane addresses for the sky zone, then switches to the terrain bitplanes below. Two independent scroll rates from one display. The Copper makes this trivial -- split the screen, change the pointers, different worlds.

**End of Phase 5:** Gradient skies, parallax clouds, animated creatures, themed palettes. Screenshots would sell this game.

---

## Phase 6: Resonance (Units 81-96)

**Goal:** Full Paula soundtrack and sound design. Four channels of sampled audio.
**68000 Focus:** Paula registers, DMA audio, CIA timer interrupts, data-driven sequencing.
**The Amiga difference:** Real sampled audio, not synthesis. Every sound is a recording.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 81 | Paula architecture overview | Register map, 4 DMA channels, sample format | Understanding the chip |
| 82 | Sound effect: dig | Raw 8-bit sample, period/volume control | First real sound |
| 83 | Sound effect library | Parameterised playback routine (sample, period, volume) | Build, redirect, explode, arrive, die |
| 84 | Replace placeholder sounds | Integrate crafted samples throughout | Cohesive audio |
| 85 | MOD file format | 4-channel tracker format: patterns, samples, sequences | Music data structure |
| 86 | MOD player (basic) | Read pattern data, set Paula registers per row | **Background music** |
| 87 | CIA timer for music tempo | CIA-B timer interrupt triggers row advance | Rock-solid timing |
| 88 | Title music | Full 4-channel MOD, atmospheric theme | Atmosphere |
| 89 | In-game music | Looping level theme, lighter than title | Gameplay backdrop |
| 90 | Music per theme | Different MOD per level theme (grass, cave, etc.) | Variety |
| 91 | SFX over music | Channel stealing with priority, restore after SFX | No ugly cutoff |
| 92 | SFX mixing | Multiple effects on available channels | Rich audio |
| 93 | Victory jingle | Short celebratory phrase on level complete | Punctuation |
| 94 | Failure sound | Descending phrase on level fail | Feedback |
| 95 | Ambient sounds | Wind, water, creature chatter on low priority | Atmosphere |
| 96 | Integration + audio balance | Volume levels, channel allocation, music/SFX coexistence | Sounds great |

**Key Teaching Moment (Unit 82):**
Paula plays raw 8-bit signed samples via DMA. Set the sample start address (`AUDxLC`), length (`AUDxLEN`), period (`AUDxPER` -- lower = higher pitch), and volume (`AUDxVOL`). Then enable the channel's DMA bit in `DMACON`. Paula fetches samples automatically. One setup, continuous playback. The CPU is free to run the game.

**Key Teaching Moment (Unit 86):**
A MOD file contains 4 channels of note/instrument/effect data arranged in patterns. Each pattern is 64 rows. The song is a sequence of pattern indices. The player reads one row per tick, looks up the instrument's sample address and base period, applies note-to-period conversion, and writes to Paula registers. Four channels, four instruments at once, real samples -- the sound that defined a generation.

**End of Phase 6:** Full 4-channel MOD music with themed tracks, crafted sample SFX, and priority mixing. Paula sings.

---

## Phase 7: Cascade (Units 97-112)

**Goal:** Complex puzzles that demand ability combinations and precise timing.
**68000 Focus:** Complex data structures, optimised Blitter scheduling, performance profiling.
**The cascade:** Multiple abilities working together in sequence -- dig, then redirect, then build, then climb. Failure cascades too: one mistake kills everyone.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 97 | Timed puzzles | Actions must happen at specific moments | Precision |
| 98 | Chain reactions | One creature's action enables another's path | Combo puzzles |
| 99 | Split flow | Creatures diverge to reach multiple exits | Routing complexity |
| 100 | Conveyor terrain | Creatures move faster/slower on specific surfaces | Movement modifier |
| 101 | Teleport zones | Creatures warp between positions | Spatial puzzles |
| 102 | One-way terrain | Creatures can only pass in one direction | Flow control |
| 103 | Lava/acid (rising hazard) | Timer-driven terrain destruction from below | Time pressure |
| 104 | Wind zones | Horizontal force affects falling creatures | Physics modifier |
| 105 | Skill-limited puzzles | Only 1-2 of each ability, every use counts | Minimal solutions |
| 106 | Puzzle sequences (tutorial) | Early levels teach one mechanic at a time | Learning curve |
| 107 | Expert puzzles | Multi-step solutions requiring all abilities | Challenge |
| 108 | Blitter performance | Optimise multiple Blitter ops per frame | Stable framerate |
| 109 | Many creatures (30+) | Object pool management, efficient update loop | Busy screen |
| 110 | Creature pathfinding | Smarter AI for crowd situations | Less frustration |
| 111 | Level design: 20 levels | Full set with difficulty curve across themes | Complete content |
| 112 | Integration + puzzle balance | Solution testing, alternative paths, fairness | Satisfying difficulty |

**Key Teaching Moment (Unit 98):**
Chain reactions: assign "digger" to creature A, which digs through dirt and falls into a lower passage. Assign "builder" to creature B, which builds a bridge over a gap that creature A's digging created. Creature C walks across B's bridge to reach the exit. Each ability enables the next. The puzzle is designing the sequence; the satisfaction is watching it cascade.

**Key Teaching Moment (Unit 108):**
The Blitter is fast but not instant. Each operation takes time proportional to the rectangle size. Multiple operations per frame (dig + build + 10 creature BOBs) can exceed the frame budget. Solutions: queue operations by priority, split large blits across frames, or use the CPU for small operations while the Blitter handles large ones. Real-world performance management.

**End of Phase 7:** 20 levels of cascading puzzles. Ability combinations, terrain types, timing challenges. Every level has a satisfying "aha" moment.

---

## Phase 8: Salvation (Units 113-128)

**Goal:** Commercial release quality. Everything a real 1990 Amiga game would ship with.
**68000 Focus:** System restoration, memory management, disk I/O, optimisation.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 113 | High score table (top 5) | Sorted insertion, multi-byte comparison | Competition |
| 114 | Name entry | Keyboard input, character display | Ownership |
| 115 | High scores on title | Display integration | Bragging rights |
| 116 | Difficulty select (3 levels) | Menu system, cursor navigation | Accessibility |
| 117 | Difficulty affects gameplay | Fewer abilities, faster timer, higher save threshold | Real difference |
| 118 | Level editor preview | Simple terrain paint with mouse | Creative mode |
| 119 | Two-player mode | Split-screen or alternating, separate levels | Social play |
| 120 | Attract mode | Auto-play demo showing a solution | Professional |
| 121 | Demo on title timeout | Timer-triggered state change | Shop display |
| 122 | Credits screen | Scrolling text with Copper effects | Attribution |
| 123 | System restoration | Restore Exec, interrupts, DMA state on exit | Clean exit |
| 124 | Memory audit | Chip RAM usage map, optimisation pass | Fits in 512KB |
| 125 | Disk loading optimisation | Fast loader, progress display | Quick loads |
| 126 | 30 levels final set | Complete level pack with full difficulty curve | Content |
| 127 | Final testing | Edge cases, ability interactions, level solvability | Release quality |
| 128 | **Complete game -- final ADF** | Bootable disk, documentation | **Ship it** |

**End of Phase 8:** A game worthy of an Amiga Power review. 30 levels, full soundtrack, attract mode, two-player, proper system restoration. Bootable from disk.

---

## Amiga-Specific Debugging (Throughout)

**Display Issues:**
- Black screen? Check DMACON (`$DFF096`) has bitplane, Copper, and sprite DMA enabled
- Wrong colours? Copper list must end with `$FFFF,$FFFE`. Check WAIT positions match actual raster lines
- Garbled display? Bitplane pointers must be word-aligned (even addresses). Check modulo values
- Sprites invisible? Sprite DMA must be enabled. Sprite data must be in Chip RAM. Check Copper sprite pointers

**Blitter Issues:**
- Blitter does nothing? Check DMACON has Blitter DMA enabled. Check BLTSIZE write triggers the blit
- Corruption? Always wait for Blitter idle (`DMABUSY` in `$DFF002` bit 14) before starting a new operation
- Wrong area affected? Check BLTDPTH points to correct bitplane. Check modulo accounts for screen width minus blit width
- Cookie-cut wrong? Minterm must match: A=mask, B=source, C=background, D=destination. Common minterm: `$FCA` for `(A AND B) OR (NOT A AND C)`

**Audio Issues:**
- No sound? Check DMACON has audio DMA enabled for the channel. Sample must be in Chip RAM
- Wrong pitch? Period register is inverse: lower values = higher pitch. 428 = middle C at PAL rate
- Clicks between samples? Ensure sample data starts and ends at zero crossing
- Music stops? CIA timer interrupt must be properly acknowledged (write to ICR)

**68000 Issues:**
- Address error (crash)? Word and long operations must use even addresses. `MOVE.W` from odd address = exception
- Data corruption? MOVEM at subroutine start/end preserves registers. Check register list matches
- Chip RAM full? All display, sound, and Blitter data must be in first 512KB. Move code to Fast RAM if available

**Creature Issues:**
- Creatures walk through terrain? Pixel check must test the correct bitplane at the correct offset
- Creatures fall forever? Floor check must look one pixel below feet, not at feet position
- Abilities don't work? Check creature state machine allows transition from "walking" to ability state

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 4 (Unit 64) | Phase 8 (Unit 128) |
|--------|-------------------|--------------------|--------------------|
| Graphics | Flat colour terrain, hardware sprites | + multi-bitplane terrain types | Gradient skies, parallax, themed palettes |
| World | 1 level | 8+ levels, terrain types, multi-entrance | 30 levels, full difficulty curve |
| Creatures | Walk + fall | + crowd behaviour, smarter AI | 30+ creatures, pathfinding, animations |
| Abilities | None | Dig + Build + Redirect + 4 more | All abilities, chain reactions, combos |
| Audio | One sample | + effect library | Full MOD music, themed tracks, SFX |
| Features | Walk to exit | + passwords, timer, terrain types | High scores, attract, 2-player, editor |
| 68000 Skill | MOVE, BSR, branches | + Blitter, DBRA, displacement | Full chipset mastery, system restoration |

---

## What This Teaches Beyond the Game

By completing Exodus, learners are ready for:
- **Signal (Game 2):** Blitter BOB skills transfer to lane-crossing object rendering. Copper screen split for HUD reused
- **Shatter Point (Game 3):** Blitter fills become brick rendering and destruction. Ball physics builds on creature position tracking
- **Ascent (Game 4):** Cookie-cut masking becomes platformer character rendering. Gravity and collision build on creature physics
- **Parallax (Game 9):** Copper display list skills enable multi-layer parallax scrolling. Blitter performance awareness enables smooth scrolling
- **Every future game:** The Copper list framework, Blitter operation patterns, Paula audio engine, and system restoration from Exodus are reused throughout the curriculum

Exodus isn't just Game 1. It's the foundation.

---

**Version:** 1.0
**Last Updated:** 2026-02-06
