# Phase 5: Illumination

**Game:** Shadowkeep (ZX Spectrum Game 1)
**Units:** 65–80
**Theme:** Visual polish — UDG graphics, pixel work, animation
**Z80 Focus:** Screen memory layout (the "thirds"), bit shifts (SLA/SRL/RLC), UDG character definition, pixel plotting
**Hardware:** Screen bitmap non-linear layout, UDG area, character set manipulation
**Status:** Planned

---

## Overview

Until now, the game uses attribute colours and ROM characters — functional but visually sparse. Phase 5 transforms the look with User Defined Graphics (UDGs) and direct pixel manipulation. The player becomes a recognisable figure. Enemies become distinct creatures. Walls become stone and wood. The keep stops looking like coloured blocks and starts looking like a place.

The Z80 focus is the Spectrum's infamous screen memory layout. Pixel rows are not consecutive in memory — they're interleaved in thirds, with rows 0, 8, 16... in one group, rows 1, 9, 17... in another. The address calculation formula is the most notorious piece of Spectrum programming, and mastering it is a rite of passage.

UDGs are simpler: redefine character shapes by writing 8 bytes of pixel data to a designated area. Each character is 8×8 pixels, and 21 characters (A–U) can be redefined. This gives the game custom wall tiles, item icons, player/enemy graphics — all within the character-cell grid that collision still relies on.

---

## Prerequisites from Phase 4

- LDIR — used for character set copying and screen buffer operations
- Contended memory awareness — pixel work in screen memory is timing-sensitive
- Room buffer — Phase 5 draws UDG characters based on buffer contents
- Attribute system — still the collision backbone; pixel graphics are decorative overlay

---

## Unit Progression

| Unit | Title | New Z80 Concept | Game Addition |
|------|-------|----------------|---------------|
| 65 | UDG Basics | Write 8 bytes to UDG area, print custom character | Custom graphic on screen |
| 66 | Player UDG | Design player character (adventurer figure) | **Recognisable player** |
| 67 | Enemy UDGs | Distinct creature designs (rat, bat, ghost) | Enemy variety |
| 68 | Wall UDGs | Stone, wood, iron tile designs | Textured walls |
| 69 | Item UDGs | Key, potion, treasure, sword icons | Clear item graphics |
| 70 | Player Walk Animation | Alternate between 2–4 UDG frames per direction | Animated movement |
| 71 | Enemy Walk Animation | Patrol cycle with frame alternation | Living creatures |
| 72 | Screen Memory Layout | The thirds formula: address from (x, y) pixel coordinates | **The Spectrum rite of passage** |
| 73 | Pixel Plotting | Set/clear individual pixels in screen bitmap | Fine detail |
| 74 | Room Transition Effect | Wipe effect: fill screen pixel-by-pixel or line-by-line | Polished transitions |
| 75 | Door Opening Animation | Sequence of UDG frames: closed → opening → open | Visual feedback |
| 76 | Death Animation | Player character breaks apart (2–3 frames) | Dramatic death |
| 77 | Title Screen Design | Character art: "SHADOWKEEP" in custom font | Presentation |
| 78 | Colour Themes per Zone | Different attribute palettes: dungeon=blue, crypt=green, tower=yellow | Area identity |
| 79 | Status Bar Polish | Custom font characters, clean layout | Professional HUD |
| 80 | Integration + Consistency | Audit all graphics, fix colour clash issues | Cohesive visual style |

---

## Key Teaching Moments

### User Defined Graphics (Unit 65)

The Spectrum reserves memory for 21 user-defined characters (codes 144–164, corresponding to letters A–U). Each character is 8 bytes — one per pixel row, 8 bits per row. Writing new values to the UDG area redefines the character shape. Print the character code to screen, and the custom graphic appears. UDGs stay within the character-cell grid, so attribute-based collision still works perfectly.

### The Screen Memory Layout (Unit 72)

The Spectrum's screen bitmap is not laid out linearly. The 192 pixel rows are organised in three thirds (0–63, 64–127, 128–191), and within each third, rows are interleaved in groups of 8. The formula:

```
Address = $4000 + ((y AND 7) × 256) + ((y AND 56) × 4) + ((y AND 192) × 32) + (x ÷ 8)
```

In Z80, this translates to bit manipulation on the Y coordinate:
- Bits 0–2 of Y → bits 8–10 of the address (which pixel row within a character cell)
- Bits 3–5 of Y → bits 5–7 of the address (which character row within a third)
- Bits 6–7 of Y → bits 11–12 of the address (which third)

This is genuinely confusing the first time, but the pattern is elegant once understood. A lookup table of row addresses avoids calculating it at runtime.

### Colour Clash Management (Unit 80)

The attribute system allows only one INK and one PAPER colour per 8×8 cell. When two differently-coloured objects overlap the same cell, one colour wins and the other is lost — "colour clash." In Shadowkeep, character-cell movement mostly avoids this (each entity occupies its own cell). But animation frames, status bar borders, and room transitions can trigger it. Phase 5 audits every visual element for clash and fixes or works around each case.

### Animation via UDG Cycling (Unit 70)

Walk animation replaces the UDG definition bytes each frame rather than printing different character codes. This means the character code on screen stays the same, but its appearance changes. Benefit: no need to re-print the character or update screen RAM. Cost: all instances of that character change simultaneously. For a single player character, this is perfect.

---

## Z80 Concepts Introduced

1. UDG memory — writing character definitions to the UDG area (Unit 65)
2. Character design — 8×8 pixel grid as 8 bytes (Unit 66)
3. Screen address calculation — the thirds formula in Z80 (Unit 72)
4. `SLA` / `SRL` / `RLC` — bit shift instructions for address calculation (Unit 72)
5. Pixel set/clear — `OR`/`AND` with bit mask at calculated address (Unit 73)
6. Row address lookup table — pre-calculated addresses for fast pixel access (Unit 72)
7. UDG animation — overwrite character definition bytes per frame (Unit 70)

---

## Hardware

### New in Phase 5

| Resource | Purpose | Introduced |
|----------|---------|-----------|
| UDG area (address in system variable $5C7B) | 21 custom character definitions, 8 bytes each | Unit 65 |
| Screen bitmap ($4000–$57FF) | Direct pixel manipulation | Unit 72 |

### Screen Address Quick Reference

| Pixel Y | Third | Base Address |
|---------|-------|-------------|
| 0–63 | Top | $4000–$47FF |
| 64–127 | Middle | $4800–$4FFF |
| 128–191 | Bottom | $5000–$57FF |

---

## Game State at Phase End

After Unit 80:

- **Custom graphics** — player, enemies, walls, items all have designed UDG characters
- **Animation** — player walks with 2–4 frame cycle, enemies animate during patrol
- **Room transitions** — wipe effect between rooms
- **Door animation** — opening sequence on unlock
- **Death animation** — player character breaks apart
- **Title screen** — "SHADOWKEEP" in custom character art
- **Zone themes** — each area has a distinct colour palette
- **Status bar** — custom font, clean layout, professional look
- **Pixel access** — screen memory layout understood, pixel plotting available

The game looks like a commercial Spectrum release from 1984–85.

---

## What Carries to Phase 6

- **Screen memory mastery** — essential for timing-aware beeper routines
- **UDG system** — sound visualisation could update UDGs
- **Tight loops** — bit manipulation skills transfer to timing loops for audio
- **Polished presentation** — title screen ready for music

---

**Version:** 1.0
**Last Updated:** 2026-02-06
