# Phase 5: Stardust

**Game:** Starfield (C64 Game 1)
**Units:** 65–80
**Theme:** Visual polish to commercial standard
**6510 Focus:** Custom character sets, VIC bank switching, colour RAM manipulation, self-modifying code
**Hardware:** VIC-II memory configuration ($D018, $DD00), multicolour sprite mode, raster colour splits
**Status:** Planned

---

## Overview

Phase 5 is where the game transforms from "playable" to "impressive." Custom character sets replace the default ROM font with designed tiles. Multicolour sprites double the colour depth of every on-screen entity. Raster colour splits paint different background colours per screen zone. The starfield — until now just asterisks and periods from the default character set — becomes a proper animated parallax effect with custom star characters.

The 6510 focus is memory configuration. The VIC-II reads graphics from a configurable 16KB window. Understanding which bank, which offset, and how `$D018` and `$DD00` interact is essential C64 knowledge. Self-modifying code appears here too — the fastest way to update character graphics is to write directly to the instruction that loads them.

By Unit 80, screenshots of the game would be indistinguishable from a commercial 1985 release.

---

## Prerequisites from Phase 4

- Raster interrupts — essential for colour splits and timed VIC-II register changes
- Frame-locked timing — all animation runs at consistent speed
- Interrupt handler structure — Phase 5 adds additional raster interrupts for screen zones
- All sprite slots managed — Phase 5 redesigns sprites in multicolour mode

---

## Unit Progression

| Unit | Title | New 6510 Concept | Game Addition |
|------|-------|-----------------|---------------|
| 65 | Custom Character Set Basics | VIC memory setup (`$D018`), character data format | New font system |
| 66 | Starfield Characters | Character ROM → RAM copy, custom tile design | **Proper starfield graphics** |
| 67 | Scrolling Stars | Rotating character data in RAM, frame timing | Animated star movement |
| 68 | Two-Speed Stars | Different update rates per character group | Parallax depth |
| 69 | Explosion Animation | Sprite pointer cycling, frame counter | 4-frame explosion |
| 70 | Player Death Explosion | Multi-sprite explosion reusing freed slots | Dramatic death |
| 71 | Screen Flash on Death | `$D020`/`$D021` simultaneous border + background flash | Emphasis |
| 72 | Enemy Spawn Animation | Sprite Y-expand (`$D017`) toggle effect | Spawn polish |
| 73 | Multicolour Sprite Mode | `$D01C` bit set, `$D025`/`$D026` shared colours | Rich sprite detail |
| 74 | Multicolour Ship and Enemies | Redesigned sprites (double-wide pixels, 3 colours) | **Visual upgrade** |
| 75 | Raster Colour Splits | Multiple raster IRQs, different `$D021` per zone | Screen zones |
| 76 | Title Screen Colour Cycling | Frame-driven colour register rotation | Attract mode flair |
| 77 | Custom HUD Font | Character set includes custom digits and glyphs | Cohesive look |
| 78 | Score Flash on Increase | Colour RAM manipulation, timed reset | Feedback |
| 79 | Smooth Sprite Movement | Fixed-point: 16-bit position, high byte → register | Sub-pixel precision |
| 80 | Integration + Visual Consistency | Audit all graphics, sprite/character harmony | Cohesive visual style |

---

## Key Teaching Moments

### VIC-II Memory Configuration (Unit 65)

The VIC-II reads character graphics from a 2KB block within its current 16KB bank. By default: bank 0 ($0000–$3FFF), character ROM at $1000. To use custom characters, copy the ROM to RAM and point $D018 at the new location. The interplay between `$DD00` (CIA2 port A, bits 0–1 select the bank) and `$D018` (bits 1–3 select character memory offset within the bank) is the most confusing VIC-II concept — and the most important to master.

### Custom Starfield (Unit 66)

Phase 1's starfield used default ROM characters (asterisks and periods). Phase 5 replaces them with purpose-designed characters: single-pixel dots, dot clusters, tiny streaks. Each character occupies an 8×8 cell but uses just a few pixels, so multiple star styles fit in a handful of character definitions. The visual difference is striking — the starfield goes from "ASCII art" to "space backdrop."

### Multicolour Sprites (Unit 73)

Multicolour mode doubles pixel width but gives each sprite 3 colours plus transparent. Standard mode: 24×21 pixels, 1 colour. Multicolour: 12×21 double-wide pixels, 3 colours. Two colours (`$D025`/`$D026`) are shared across all multicolour sprites; the third is per-sprite (`$D027`+). Most commercial C64 games use multicolour. The trade-off — less horizontal detail for more colour depth — is almost always worth it.

### Raster Colour Splits (Unit 75)

Building on Phase 4's single colour bar, multiple raster interrupts change `$D021` at different screen lines. The play area might have a dark blue background, while the HUD zone at the top has black. This gives the illusion of a more colourful display than the C64's 16-colour limit would suggest. The technique requires chained raster interrupts — each handler sets up the next.

### Self-Modifying Code (Unit 67)

Animating characters in RAM means writing to the character data bytes. The fastest way to do this on the 6502 is self-modifying code: the instruction that loads the animation frame has its operand overwritten each frame. This avoids an indirect load, saving cycles in a tight loop. Self-modifying code is controversial on modern machines but essential on the 6502, where every cycle counts.

---

## 6510 Concepts Introduced

1. VIC bank selection — `$DD00` bits 0–1 (Unit 65)
2. Character memory pointer — `$D018` bits 1–3 (Unit 65)
3. Character ROM to RAM copy — reading from ROM overlay (Unit 66)
4. Self-modifying code — overwriting instruction operands at runtime (Unit 67)
5. Multicolour sprite mode — `$D01C`, `$D025`/`$D026` shared colours (Unit 73)
6. Chained raster interrupts — each handler schedules the next (Unit 75)
7. Fixed-point positioning — 16-bit values, high byte drives hardware register (Unit 79)

---

## Hardware Registers

### New in Phase 5

| Register | Purpose | Introduced |
|----------|---------|-----------|
| `$D018` | VIC-II memory pointers (screen + character offset) | Unit 65 |
| `$DD00` | CIA2 port A (bits 0–1 = VIC bank select) | Unit 65 |
| `$D01C` | Multicolour sprite enable (1 bit per sprite) | Unit 73 |
| `$D017` | Sprite Y-expand (1 bit per sprite) | Unit 72 |
| `$D025` | Sprite multicolour 0 (shared) | Unit 73 |
| `$D026` | Sprite multicolour 1 (shared) | Unit 73 |

---

## Game State at Phase End

After Unit 80:

- **Custom character set** — purpose-designed font, star tiles, HUD glyphs
- **Animated starfield** — scrolling custom characters at two parallax speeds
- **Multicolour sprites** — ship and all enemies redesigned with 3 colours each
- **Explosion animation** — 4-frame sprite sequence on enemy death
- **Raster colour splits** — different background colours for play area and HUD
- **Title screen effects** — colour cycling on the title text
- **Sub-pixel movement** — fixed-point positions for smooth sprite motion
- **Score flash** — colour RAM highlight when score increases

The game looks professionally made. Screenshots sell it.

---

## What Carries to Phase 6

- **VIC-II memory configuration** — understanding banks and offsets is needed when managing both character sets and sprite data
- **Raster interrupt chaining** — Phase 6 uses CIA timer interrupts alongside raster IRQs for music
- **Self-modifying code** — useful for optimised SID register updates
- **Fixed-point math** — frequency calculations for SID pitch control

---

**Version:** 1.0
**Last Updated:** 2026-02-06
