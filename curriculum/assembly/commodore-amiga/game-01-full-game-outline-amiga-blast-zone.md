# Full Game Outline: Amiga Blast Zone (128 Units)

**Game:** Blast Zone (Game 1)
**Units:** 128 (8 phases × 16 units)
**Target Quality:** Commercial-grade fixed-screen shooter (1987-88 era)
**Comparable To:** Arcadia (Amiga), early PD shooters → approaching Menace, Hybris-level polish by completion

---

## What Makes This "Amiga"

The Amiga has three custom chips working in concert:
- **Agnus** — DMA controller, Blitter (hardware rectangle copier), Copper (display list coprocessor)
- **Denise** — Display output, 8 hardware sprites (16px wide), playfield rendering
- **Paula** — 4 channels of 8-bit sampled audio, disk I/O

And supporting them:
- **68000 CPU** — 16/32-bit processor with 8 data + 7 address registers, real multiply/divide
- **Chip RAM** — all graphics, sound, and DMA data must live here (512KB on A500)
- **Bootable disks** — programs boot from ADF images via Kickstart

This shooter showcases the chipset symphony. Player is a hardware sprite (fast, DMA-driven). Enemies are BOBs — Blitter Objects of any size. The Copper creates gradient skies and colour effects. Paula plays real sampled explosions and four-channel music. The result is unmistakably Amiga.

---

## Design Philosophy

- **One concept per unit** — never overwhelming
- **Always playable** — from Unit 2 onwards
- **Bootable from Unit 1** — learners can run their game immediately
- **Debugging inline** — every unit includes "if it doesn't work"
- **68000 skill per unit** — assembly concepts build alongside the game
- **Chipset harmony** — Copper, Blitter, and Paula all introduced by Phase 2
- **Sampled sound from Unit 4** — that Amiga audio quality, immediately
- **Commercial quality by Unit 128** — a real game

---

## 68000 Assembly Progression

| Phase | 68000 Focus |
|-------|-----------|
| 1 (Bootblock) | MOVE.B/W/L, D0-D7/A0-A7 registers, addressing modes, BEQ/BNE, BSR/RTS |
| 2 (Blitter Storm) | Blitter registers, minterms, bitwise ops (AND/OR/EOR), MULU for offset calc |
| 3 (Payload) | MOVEM for register save/restore, subroutine parameters, SUBQ/ADDQ |
| 4 (Flak) | DBRA loops, address register indirect with offset, word/long alignment |
| 5 (Copper Sky) | Copper instruction format (WAIT/MOVE), bitplane pointer arithmetic, DMA timing |
| 6 (Four Voices) | Paula registers, DMA audio, CIA timer interrupts, data-driven sequencing |
| 7 (Titan) | Complex data structures, LEA for address calc, performance-aware Blitter scheduling |
| 8 (Gold Master) | System restoration (Exec), memory management, optimisation techniques |

By Unit 128, learners have a working knowledge of the 68000 instruction set, the OCS custom chipset, and the DMA-driven architecture that makes the Amiga unique.

---

## Phase 1: Bootblock (Units 1-16)

**Goal:** Complete game loop — shoot enemies, score points, die, restart. Bootable from disk.
**68000 Focus:** MOVE, registers, addressing modes, branches, subroutines.
**Graphics:** Hardware sprites only (no playfield needed yet). The simplest way to get something on screen.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 1 | Bootable ADF + Copper list + ship sprite | `MOVE.L`, custom register writes, Copper list format | See your ship, **can run it** |
| 2 | Joystick moves ship | `BTST` for bit testing, `JOY1DAT` + XOR decode for directions | **Control something** |
| 3 | Fire button shoots (sprite bullet) | RAM variables, `ADD.W`/`SUB.W` for movement | Bullet flies up |
| 4 | Laser sample plays | Paula channel: sample pointer, length, period, volume | Satisfying "pew" |
| 5 | One enemy sprite | Second sprite pointer in Copper list, sprite data format | Target exists |
| 6 | Bullet hits enemy | `CMP.W`, `BLT`/`BGT` branches, distance check | **It dies!** |
| 7 | Explosion sample + sprite flash | Paula channel 2, sprite colour change in Copper | Feedback |
| 8 | Playfield for score display (bitplanes) | Bitplane pointers in Copper, `BPLCON0`, planar pixel format | See your points |
| 9 | Enemies spawn continuously | `BSR`/`RTS` subroutines, timer-based spawn logic | Challenge |
| 10 | Enemy touches ship = death | Bounding box collision (coordinate-based) | You can die |
| 11 | Game over screen | Blitter rectangle copy for text rendering | End state |
| 12 | Fire button restarts | State machine, hardware register reinitialisation | **Complete loop** |
| 13 | Title screen with Copper colours | Copper colour changes between screen zones | Feels real |
| 14 | Three lives | Game state variables, display update | Forgiveness |
| 15 | Life lost effect | Copper background flash, death sample | Feedback |
| 16 | Integration + edge cases | Chip RAM constraints, sprite boundaries, DMA setup | Solid foundation |

**Amiga-Specific Unit 1:**

Unlike other platforms, the Amiga needs a Copper list just to display anything — the Copper sets up bitplane pointers, colours, and the display window. And the program must live on a bootable disk. Unit 1 teaches all three: Copper list, hardware sprite, and ADF creation.

```asm
; Take over hardware
    move.w  #$7FFF,$DFF09A      ; Disable all interrupts
    move.w  #$7FFF,$DFF096      ; Disable all DMA

; Install Copper list
    lea     copper_list,a0
    move.l  a0,$DFF080          ; COP1LC
    move.w  #0,$DFF088          ; COPJMP1 — start Copper

; Enable DMA: Master + Copper + Sprites
    move.w  #$82A0,$DFF096      ; DMACON set

.loop:  bra .loop               ; Main loop (for now)

copper_list:
    dc.w    $0120               ; SPR0PTH
    dc.w    ship>>16
    dc.w    $0122               ; SPR0PTL
    dc.w    ship&$FFFF
    dc.w    $01A2,$0FFF         ; COLOR17 = white (sprite colour 1)
    dc.w    $FFFF,$FFFE         ; End of Copper list

    SECTION gfx,DATA_C          ; Must be in chip RAM
ship:
    dc.w    $6040,$7800         ; VSTART, HSTART, VSTOP, control
    dc.w    %0000011111100000,%0000000000000000
    ; ... sprite pixel rows ...
    dc.w    0,0                 ; End of sprite data
```

**Creating a bootable ADF (Unit 1):**
```bash
vasmm68k_mot -Fhunkexe -kick1hunks -o blastzone blastzone.asm
xdftool blastzone.adf create && xdftool blastzone.adf format "BlastZone"
xdftool blastzone.adf makedir s && xdftool blastzone.adf boot install
echo "blastzone" > startup-sequence
xdftool blastzone.adf write startup-sequence s/startup-sequence
xdftool blastzone.adf write blastzone
```

**If it doesn't work (Unit 1):**
- **Black screen?** DMACON not set — need `$82A0` minimum (Master + Copper + Sprites).
- **No sprite?** Sprite data not in chip RAM. Use `SECTION name,DATA_C`.
- **Wrong position?** Sprite header words encode position in a packed format — check VSTART/HSTART/VSTOP.
- **Wrong colours?** Sprite 0 uses COLOR17-19 (`$DFF1A2`-`$DFF1A6`). Set them in the Copper list.
- **Won't boot?** Check startup-sequence is in `s/` directory and executable name matches.
- **Guru Meditation?** Word/long access on odd address, or code at wrong location.

**End of Phase 1:** Playable Amiga shooter, bootable from disk. Hardware sprites on a black background, with sampled sound.

---

## Phase 2: Blitter Storm (Units 17-32)

**Goal:** Enemies upgrade from hardware sprites to BOBs (Blitter Objects). The Blitter chip mastered.
**68000 Focus:** Blitter register setup, minterms, bitwise operations, MULU for offset calculation.
**Key moment:** BOBs can be any size — no more 16-pixel-wide limit. This is how Amiga games draw most game objects.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 17 | Blitter explained — copy a rectangle | Blitter registers, `BLTCON0`, `BLTSIZE` trigger | Understanding the chip |
| 18 | Draw a BOB (enemy graphic on playfield) | Source→dest with minterm, modulo calculation (`MULU`) | Enemy drawn |
| 19 | Cookie-cut masking for transparency | Mask data (source B), minterm `$0FCA` | Clean BOB edges |
| 20 | Erase BOB (restore background) | Save-under buffer, Blitter restore blit | No ghost images |
| 21 | BOB movement (erase-draw cycle) | Frame loop: erase old position, draw new | Smooth movement |
| 22 | Multiple BOBs from enemy table | Data table with `LEA` + offset, `DBRA` loop | Several enemies |
| 23 | Fast enemy (dives straight down) | Speed as data field, parameterised update | Variety begins |
| 24 | Slow enemy (drifts sideways) | Combined X+Y velocity from data table | Pacing contrast |
| 25 | Zigzag enemy (weaves as it falls) | Direction toggle or sine table lookup | Movement patterns |
| 26 | Different BOB graphics per type | Graphic pointer in enemy data, `MOVE.L (An)` indirect | Visual distinction |
| 27 | Different colours per type | Palette choice per enemy, Copper colour setup | Instant recognition |
| 28 | Wave system (clear all = next wave) | Enemy alive counter, state transitions | Structure |
| 29 | Wave composition tables | Data-driven definitions (types, counts, speeds) | Varied challenge |
| 30 | Draw order (Y-sorted) | Sorted draw list for correct overlap | Visual correctness |
| 31 | Wait for Blitter (`BLTBUSY`) | Polling `DMACONR` bit 14, avoiding race conditions | Stable rendering |
| 32 | Integration + balance | Blitter throughput testing, wave tuning | Feels fair |

**Key Teaching Moment (Unit 17):**
The Blitter is a hardware rectangle copier with built-in logic. It combines up to three source areas (A, B, C) into a destination (D) using boolean operations called minterms. For game graphics, the critical operation is "cookie-cut": source A is the BOB graphic, source B is a transparency mask, source C is the existing background, destination D is where the result goes. The Blitter does this in hardware, far faster than the CPU. Understanding the Blitter is the key to all Amiga game graphics.

**Key Teaching Moment (Unit 19):**
A BOB without masking is a rectangle — it overwrites whatever's behind it. The cookie-cut minterm (`$0FCA`) means: "where the mask says opaque, use the BOB pixel; where the mask says transparent, keep the background." This single concept is what makes BOBs look like real game objects rather than blocks stamped on the screen.

**End of Phase 2:** Enemies are proper BOBs — any size, masked transparency, smooth movement. The Blitter does the heavy lifting.

---

## Phase 3: Payload (Units 33-48)

**Goal:** Power-ups with Amiga audiovisual flair. Hardware sprites used creatively for player effects.
**68000 Focus:** MOVEM for register save/restore, subroutine parameters, SUBQ/ADDQ.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 33 | Power-up drops (BOB, smaller graphic) | New BOB type, spawn on enemy death | Collectibles exist |
| 34 | Collect power-up = effect | Player sprite ↔ BOB collision, state change | System works |
| 35 | Speed boost power-up | Temporary state, `SUBQ` frame countdown | Agility |
| 36 | Rapid fire power-up | Fire rate as variable, timer decrement | Firepower |
| 37 | Power-up collect sample | Paula channel 3, distinct sample | Satisfying |
| 38 | Copper colour cycle on power-up pickup | Copper WAIT + MOVE for background flash | Amiga visual flair |
| 39 | Power-ups are temporary (timer) | 32-bit countdown with `SUB.L` | Strategic decisions |
| 40 | Timer display (Copper colour bar) | Copper colour bar width = remaining time | Amiga-native HUD |
| 41 | Double shot (two bullet sprites) | Hardware sprite pair management | Coverage |
| 42 | Spread shot (three directions) | Velocity tables for angle offsets | Screen control |
| 43 | Shield (one free hit) | Hardware sprite overlay on player | Defensive option |
| 44 | Shield visual (sprite attached to player) | Sprite position offset, colour palette | See protection |
| 45 | Shield break effect + sample | Sprite removal, multi-channel audio | Dramatic feedback |
| 46 | `MOVEM` for subroutine safety | Save/restore D0-D7/A0-A6 in one instruction | Clean code |
| 47 | Power-up spawn frequency tuning | Probability per kill, wave-dependent rates | Balance |
| 48 | Integration + balance | Power-up playtesting, visual/audio coherence | Rewarding loop |

**Amiga-Specific:**
- Power-up BOBs use Copper colour cycling to sparkle — Copper changes their palette each frame
- Shield is a second hardware sprite attached to the player's position (sprites are "free" — no CPU cost)
- Timer bar is a Copper effect: wait for the right scanline, change background colour for N pixels, then change back. Width shrinks as time runs out. Pure Amiga — no bitmap needed.

**End of Phase 3:** Power-ups feel great. The Copper does things no other platform can.

---

## Phase 4: Flak (Units 49-64)

**Goal:** Enemies shoot back. Many objects on screen — Blitter scheduling becomes real.
**68000 Focus:** DBRA loops, address register indirect with offset, word/long alignment awareness.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 49 | Enemy bullet (BOB) | Bullet pool, new BOB type in draw list | Danger from above |
| 50 | Enemy bullet graphic | Distinct small BOB, sharp visibility | Clear threat |
| 51 | Enemy bullet hits player | Sprite↔BOB collision (cross-system check) | Real danger |
| 52 | Enemy fire sample | Paula channel, distinct from player laser | Audio warning |
| 53 | Random enemy fires | Linear feedback shift register (`EOR.L`, `LSR.L`) | Unpredictable |
| 54 | Shooter enemy type (fires aimed) | Direction calculation with `SUB.W` and lookup table | Smart enemies |
| 55 | Multiple enemy bullets (pool of 6) | `DBRA` pool iteration, allocation/free tracking | Intensity |
| 56 | Aimed vs random shot mix | Probability table, difficulty-scaled | Variety |
| 57 | Player bullet destroys enemy bullet | BOB↔BOB collision | Skill option |
| 58 | Blitter queue management | Operation sequencing, `BLTBUSY` between blits | No glitches |
| 59 | Player death = bullets cleared | Pool reset, state cleanup | Fair restart |
| 60 | Difficulty ramp per wave | Parameter tables indexed by wave number | Escalation |
| 61 | Bullet density tuning | Max count, fire rate limits per wave | Not overwhelming |
| 62 | DMA budget awareness | Blitter time vs CPU time per frame | Performance thinking |
| 63 | Address alignment discipline | Word-align all DMA data, `EVEN` directive | No address errors |
| 64 | Integration + combat balance | Full combat playtesting, stable Blitter | Challenging but fair |

**Key Teaching Moment (Unit 58):**
The Blitter and CPU share the bus. While the Blitter is copying a rectangle, the CPU stalls on chip RAM access. With many BOBs (enemies + bullets + explosions), Blitter operations queue up. You MUST check `BLTBUSY` in `DMACONR` before starting a new blit. Not checking causes corrupted graphics — the single most common Amiga programming bug.

**Key Teaching Moment (Unit 63):**
The 68000 requires word and long-word data to be on even addresses. An odd-address `MOVE.W` or `MOVE.L` triggers an address error exception — instant Guru Meditation. The `EVEN` assembler directive after `DC.B` data blocks prevents this. It's a constant discipline on the Amiga that doesn't exist on 8-bit platforms.

**End of Phase 4:** Intense two-way combat. The Blitter handles the load without glitching.

---

## Phase 5: Copper Sky (Units 65-80)

**Goal:** Visual polish that showcases the Amiga's unique capabilities. The Copper becomes creative tool, not just plumbing.
**68000 Focus:** Copper instruction format (WAIT/MOVE), bitplane pointer arithmetic, DMA timing.
**Key moment:** The Copper has been setting up the display since Unit 1. Now it becomes the star — gradient skies, colour bars, palette effects.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 65 | Copper gradient background | Copper WAIT + MOVE for `COLOR00` per scanline | **That Amiga look** |
| 66 | Animated gradient (breathing sky) | Frame-driven Copper list modification in RAM | Living background |
| 67 | Starfield layer (bitplane pixels) | Separate bitplane with pixel plots, priority behind BOBs | Parallax depth |
| 68 | Multiple star speeds | Different update rates per star group | Layered motion |
| 69 | Explosion animation (BOB, 4 frames) | Frame cycling, animation state machine | Visual impact |
| 70 | Multi-frame explosion sequence | Large BOB expanding outward | Drama |
| 71 | Player death sequence | Multi-step visual + Copper flash + sample | Stakes |
| 72 | 32-colour mode (5 bitplanes) | `BPLCON0` depth field, extra bitplane pointers | Rich palette |
| 73 | Colour palette design | OCS 12-bit RGB ($0RGB), palette planning for gameplay clarity | Amiga colour mastery |
| 74 | Smooth BOB movement (subpixel) | Fixed-point: 32-bit position, `SWAP` for high word | Professional feel |
| 75 | Copper colour bars in border | Classic Amiga demo effect, multiple WAITs per frame | Signature flair |
| 76 | Palette themes per wave group | Copper list palette swap, mood change | Visual variety |
| 77 | Score highlight on change | Copper colour change at score position | Feedback |
| 78 | Enemy spawn effect (Copper flash) | Localised colour change at spawn Y-position | Polish |
| 79 | Clean display composition | Sprite/BOB/playfield priority tuning (`BPLCON2`) | Professional |
| 80 | Integration + visual consistency | All graphics audited, coherent style | Looks commercial |

**Key Teaching Moment (Unit 65):**
The Copper is the Amiga's secret weapon. It has only two instructions: WAIT (wait for the beam to reach a screen position) and MOVE (write a value to any custom chip register). That's it. But these two instructions can change colours, switch bitplanes, reposition sprites, and reshape the display mid-frame. A gradient sky is just: WAIT for line N, MOVE new colour to `COLOR00`, WAIT for line N+1, MOVE different colour, repeat. Simple concept, stunning result. This is what made people walk past an Amiga in a shop and stop.

**Key Teaching Moment (Unit 72):**
OCS bitplanes work in powers of 2: 1 bitplane = 2 colours, 2 = 4, 3 = 8, 4 = 16, 5 = 32. Each additional bitplane doubles the colour count but also doubles the DMA bandwidth. Five bitplanes give 32 colours but consume significant bus time. Game design means choosing: do you need 32 colours, or do you need the CPU time that 16-colour mode (4 bitplanes) would free up?

**End of Phase 5:** The game looks like a commercial Amiga title. Copper gradient sky, 32 colours, smooth animation. Screenshots would sell it.

---

## Phase 6: Four Voices (Units 81-96)

**Goal:** Full four-channel audio — sampled music and rich sound design. Paula sings.
**68000 Focus:** Paula DMA registers, CIA timer interrupts, data-driven sequencing.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 81 | Paula architecture deep dive | Channel registers: pointer, length, period, volume | Understanding the chip |
| 82 | Sample playback control | Period→pitch relationship, volume control (0-64) | Controlled audio |
| 83 | Note table (period values) | Amiga period lookup table, `MOVE.W` to `AUDxPER` | Musical scale |
| 84 | Sound effect library | Parameterised routine: sample, period, volume, priority | Varied SFX |
| 85 | Replace all placeholder sounds | Integrate crafted samples throughout the game | Cohesive audio |
| 86 | Two-channel melody | Note+duration sequence data, interrupt-driven playback | Music begins |
| 87 | Four-channel pattern sequencer | Row/pattern data structure, `MOVEM` for IRQ register save | Full arrangement |
| 88 | Music timing via CIA-B timer | `$BFD400`+ timer interrupt for stable tempo | Rock-solid playback |
| 89 | Music fades on game start | Volume ramp-down, DMA channel management | Clean transition |
| 90 | Game over jingle | Short descending sample phrase | Punctuation |
| 91 | Wave complete jingle | Short ascending phrase | Achievement |
| 92 | High score jingle | Celebratory phrase, distinct from others | Distinction |
| 93 | Channel stealing (SFX over music) | Priority system: channels 2-3 for SFX, 0-1 protected for music | No ugly cutoff |
| 94 | In-game music (background) | 2 channels music + 2 channels SFX split | Atmosphere + action |
| 95 | Volume envelopes | Software amplitude ramp per note, fade-in/fade-out | Shaped sounds |
| 96 | Integration + audio balance | Mix levels, channel allocation, stereo balance | Sounds great |

**Paula-Specific:**
Paula plays samples — real recorded audio, not synthesised waveforms. You provide a pointer to sample data in chip RAM, a length (in words), and a period (playback speed). Paula reads the data via DMA automatically. Lower period = higher pitch. This is why Amiga music sounds distinctive: it's actual recorded instruments, drums, and effects, not approximations.

Our sequencer is a simplified pattern player — not ProTracker-compatible, but teaching the same concepts. Production Amiga games typically used a pre-written replay routine (P61, LSP, or the ProTracker playroutine). The sequencer we build here teaches how they work under the hood.

**End of Phase 6:** Four-channel music with sampled instruments, punchy effects, proper channel management. That Amiga sound.

---

## Phase 7: Titan (Units 97-112)

**Goal:** Boss fights with large BOBs. The Blitter's true power — any size, any complexity.
**68000 Focus:** Complex data structures, LEA for address calculation, performance-aware Blitter scheduling.
**Key moment:** A 64×64 pixel boss is just one Blitter operation — the Amiga doesn't care how big your sprites are. The limit is Blitter bandwidth per frame.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 97 | Mini-boss every 3 waves | Conditional trigger on wave count | Early taste |
| 98 | Mini-boss: tough enemy (3 hits, 32×32 BOB) | Hit counter, larger BOB graphic | Imposing target |
| 99 | Mini-boss movement pattern | Pattern table with timing data | Distinct behaviour |
| 100 | Boss every 5 waves (64×64 BOB) | Large Blitter operation, extended graphic data | **Impressive size** |
| 101 | Boss movement (sweep pattern) | Complex pattern table, smooth interpolation (`ASR` for easing) | Menacing |
| 102 | Boss health bar (Copper) | Copper colour bar, width proportional to remaining health | Visible progress |
| 103 | Boss hit flash | Temporary palette change via Copper at boss Y-position | Satisfying feedback |
| 104 | Boss shoots (spread pattern) | Multiple bullet spawn positions, angle offsets | Dangerous |
| 105 | Boss phase 2 at 50% health | State machine transition, pattern + palette change | Escalation |
| 106 | Boss death (big explosion sequence) | Multi-frame scripted BOB animation, chain of samples | Payoff |
| 107 | Boss defeat bonus + jingle | Score reward, celebratory sample sequence | Triumph |
| 108 | Blitter budget with boss active | Prioritised draw order, deferred erases if needed | Performance |
| 109 | Second boss type (different graphic, pattern) | Table-driven entity: swap data pointers, same system | Variety |
| 110 | Second boss unique attack (aimed burst) | Different firing pattern, new samples | Fresh challenge |
| 111 | Boss warning (Copper flash + siren sample) | Combined visual/audio anticipation cue | Drama |
| 112 | Integration + boss balance | Health/damage tuning, Blitter frame budget stable | Memorable, fair fights |

**Key Teaching Moment (Unit 100):**
On the C64, "how big can a sprite be?" means 24×21 pixels (or 8 sprites multiplexed). On the NES, a "big" enemy is 4 sprites bolted together. On the Amiga, a BOB can be any size the Blitter can handle. A 64×64 boss is one Blitter operation — it just takes more DMA cycles. The Amiga's constraint isn't "how many objects" but "how much Blitter time per frame." Understanding this budget is what separates a smooth game from a stuttering one.

**End of Phase 7:** Boss fights are the highlight. Large, multi-phase encounters with real visual and audio drama.

---

## Phase 8: Gold Master (Units 113-128)

**Goal:** Commercial release quality. "Gold master" — the final disk image sent for duplication.
**68000 Focus:** System restoration, memory management, Exec library calls, optimisation.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 113 | High score table (top 5) | Sorted insertion, multi-byte comparison | Competition |
| 114 | Initials entry | Raw key handling via CIA, character display | Ownership |
| 115 | High scores on title | Persistent display integration | Bragging rights |
| 116 | Attract mode (auto-play demo) | Recorded input playback | Professional |
| 117 | Two-player alternating | Player state switching, turn management | Social |
| 118 | Score comparison at game over | Side-by-side display | Competition |
| 119 | Difficulty select | Menu system, joystick cursor navigation | Accessibility |
| 120 | Difficulty affects gameplay | Parameter tables per level | Real difference |
| 121 | Extra life at 10,000 | Threshold detection, celebration effect + jingle | Skill reward |
| 122 | PAL/NTSC detection | `VPOSR` register check, speed adjustment | Platform correct |
| 123 | Custom boot screen | Loading graphic displayed via Copper during disk load | Presentation |
| 124 | Workbench integration | Disk icon (.info file), proper tooltypes | Distribution polish |
| 125 | Clean system exit | Restore OS: Copper, interrupts, DMA, system structures | Professional |
| 126 | Credits screen | Text display with Copper colour effects | Professional |
| 127 | Final balance + bug sweep | Systematic testing across A500/A600 configurations | Release ready |
| 128 | **Complete game — gold master ADF** | Final disk image, boot tested, icon included | **Ship it** |

**Key Teaching Moment (Unit 125):**
On the C64, your program owns the machine forever. On the Amiga, the operating system was there first. When the game exits, it MUST restore everything: the OS Copper list, system interrupts, DMA state, and the view structure. Failing to do this crashes the machine. This is a uniquely Amiga concern — and it teaches proper resource management that transfers to every platform with an OS.

**End of Phase 8:** A game worthy of Amiga PD libraries or a budget release. Boot screen, Workbench icon, clean exit — the full professional package.

---

## Amiga-Specific Debugging (Throughout)

**Black Screen / No Display:**
- DMACON not set (`$DFF096`) — need `$82A0` minimum (Master + Copper + Sprites)
- Copper list not started — must write COP1LC (`$DFF080`) then strobe COPJMP1 (`$DFF088`)
- Copper list in fast RAM — must be in chip RAM (`SECTION name,DATA_C`)
- Copper list not terminated — last entry must be `$FFFF,$FFFE`
- Bitplane pointers wrong in Copper list — check high/low word split

**Sprite Issues:**
- Sprite DMA not enabled — DMACON bit 5 (`$0020`)
- Sprite data not in chip RAM
- Position encoded wrong — sprite header packs VSTART, HSTART, VSTOP in two words
- Sprite colours not set — sprite 0 uses COLOR17-19 (`$DFF1A2`+), not COLOR01-03

**BOB Issues:**
- Not waiting for Blitter — check `DMACONR` bit 14 (BLTBUSY) before EVERY blit
- Wrong minterm — cookie-cut needs `$0FCA`, simple copy needs `$09F0`
- Ghost images — not restoring background (save-under) before drawing new position
- Source/dest not in chip RAM — all Blitter data must be DMA-accessible
- Modulo wrong — modulo = playfield width in bytes minus BOB width in bytes

**Audio Issues:**
- No sound — audio DMA not enabled in DMACON (bits 0-3 for channels 0-3)
- Volume zero — `AUDxVOL` registers range 0-64, not 0-255
- Sample data not in chip RAM
- Wrong pitch — period is inversely proportional to frequency (lower period = higher pitch)
- Sample loops forever — length register sets repeat length; set to 1 word of silence to stop

**Crashes (Guru Meditation):**
- Address error — word or long access on odd address (68000 requires alignment)
- Illegal instruction — code has jumped into data (check branches and return addresses)
- Bus error — accessing non-existent memory
- Stack overflow — too many `BSR`/`JSR` without corresponding `RTS`

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 4 (Unit 64) | Phase 8 (Unit 128) |
|--------|-------------------|--------------------|--------------------|
| Graphics | Hardware sprites on black | + BOBs, bitplane playfield | Copper gradients, 32 colours, large bosses |
| Enemies | One hardware sprite | 4+ BOB types, aimed shots, shooter type | + Bosses (64×64), mini-bosses, phases |
| Player | Sprite, move + shoot | Power-ups, shield sprite, spread shot | + Difficulty select, attract demo |
| Audio | 2 samples (laser, explosion) | Varied samples, 4 channels used | 4-channel music, SFX priority, envelopes |
| Modes | Single play | Same | Two-player, 3 difficulties, attract mode |
| Distribution | Bootable ADF | Same | Custom boot screen, Workbench icon, clean exit |
| 68000 Skill | MOVE, branches, BSR | Blitter ops, interrupts, DMA | Full chipset mastery |

---

## The Amiga Challenge

Where other platforms have constraints, the Amiga has abundance — and that's its own kind of problem:
- **Bitplane format** — planar graphics are confusing until the penny drops. Pixel (X, Y) doesn't map to a simple byte offset.
- **Chip RAM boundary** — everything the custom chips touch must be in chip RAM. Forget this and nothing works.
- **DMA contention** — Blitter, Copper, bitplanes, sprites, and audio all share the bus. Understanding the budget is the Amiga programmer's core discipline.
- **Word alignment** — the 68000 crashes on odd-address word access. Constant vigilance.
- **System restoration** — unlike the C64, you borrowed the machine from the OS. Give it back properly.

The power is real. Learning to wield it tastefully is the challenge.

---

## What This Teaches Beyond the Game

By completing Blast Zone, learners are ready for:
- **Signal (Game 2):** Hardware sprites → multi-sprite characters. Copper display setup → playfield scrolling.
- **Shatter Point (Game 3):** BOB rendering → ball physics with Blitter collision maps.
- **Parallax (Game 9):** Single playfield → dual playfield for parallax scrolling.
- **Every future game:** The Copper list framework, Blitter operations, Paula audio engine, and bootable disk creation from Blast Zone are reused and extended throughout the curriculum.

Blast Zone isn't just Game 1. It's the chipset masterclass.

---

**Version:** 2.0
**Last Updated:** 2026-02-05
