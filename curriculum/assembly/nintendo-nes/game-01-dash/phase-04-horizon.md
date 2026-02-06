# Phase 4: Horizon

**Game:** Dash (NES Game 1)
**Units:** 49-64
**Theme:** Hardware scrolling -- the world opens beyond one screen
**6502 Focus:** PPUSCROLL mechanics, nametable seam writes, VBlank budgeting, 16-bit scroll position, indirect indexed addressing
**Hardware:** PPUSCROLL ($2005), PPUCTRL nametable bits ($2000), Sprite 0 hit ($2002 bit 6)
**Status:** Planned

---

## Overview

Phase 4 is the NES showing off. Hardware scrolling is the console's gift to platformers -- the PPU shifts the entire display by any number of pixels, every frame, for free. No redrawing, no Blitter, no CPU cost. Write the scroll position to PPUSCROLL ($2005) and the hardware does the rest.

The challenge isn't scrolling -- it's feeding data. As the camera moves right, new tiles must appear at the right edge. The NES has two nametables side by side; you write the next column to the one about to scroll into view. One column per frame during VBlank. The seam is invisible because the PPU wraps between nametables.

Sprite 0 hit splits the screen: the status bar stays fixed while the level scrolls. This technique is used by nearly every NES game with a HUD.

---

## Prerequisites from Phase 3

- Refined jump physics (variable height, coyote time, buffering)
- Metatile system with collision types
- Multiple levels with transitions
- Health system and checkpoints

---

## Unit Progression

| Unit | Title | New 6502 Concept | Game Addition |
|------|-------|------------------|---------------|
| 49 | PPUSCROLL Basics | `$2005` double-write (X then Y), latch reset via `$2002` | Screen shifts |
| 50 | Smooth Camera Follow | Camera tracks player, scroll increments per frame | World moves with you |
| 51 | Camera Dead Zone | Don't scroll until player reaches edge threshold | Comfortable view |
| 52 | 16-Bit Scroll Position | Two bytes, carry into nametable select bit | Beyond 255 pixels |
| 53 | Nametable Seam Loading | Write new column at scroll edge during VBlank | **Seamless world** |
| 54 | Seam Column from Level Data | 16-bit level pointer, read metatile column ahead | Data-driven scrolling |
| 55 | Attribute Seam Update | Update attribute bytes at nametable boundary | Correct colours at edge |
| 56 | VBlank Budget Management | Measure cycle cost, split work across frames | Stable rendering |
| 57 | Scroll-Aware Collision | World coords to screen coords for tile checks | Collision still works |
| 58 | Scroll-Aware Sprites | Subtract scroll offset for on-screen X position | Objects stay in place |
| 59 | Camera Bounds | Stop scrolling at level start/end | No overrun |
| 60 | Horizontal Mirroring | Nametable layout option for wide scrolling | Level shape |
| 61 | Long Level (4+ Screens) | Extended level data, tested scrolling over distance | Real content |
| 62 | Scroll Speed Zones | Different max speeds per section | Pacing control |
| 63 | Status Bar with Sprite 0 | Sprite 0 hit splits scroll: HUD fixed, level scrolls | **Professional HUD** |
| 64 | Integration + Scroll Stability | Edge cases, seam glitches, performance | Solid scrolling |

---

## Key Teaching Moments

### PPUSCROLL (Unit 49)

PPUSCROLL ($2005) is a double-write register. The first write sets horizontal scroll (0-255), the second sets vertical scroll. But the internal latch must be in the right state -- reading $2002 (PPUSTATUS) resets it. The write sequence:

```asm
; Set scroll position (in NMI handler, after all VRAM writes)
    bit $2002           ; Reset latch
    lda scroll_x        ; Horizontal scroll (0-255)
    sta $2005
    lda #$00            ; Vertical scroll (0 for side-scroller)
    sta $2005
```

The nametable select bits in PPUCTRL ($2000) extend the scroll range beyond 255 pixels. When scroll_x overflows from 255 to 0, toggle the nametable bit to switch to the adjacent nametable -- seamless 512-pixel scrolling.

### Nametable Seam Loading (Unit 53)

As the camera scrolls right, a new column of tiles must be written at the edge about to become visible. The NES has two nametables arranged side by side (with horizontal mirroring). Write to the nametable that's currently off-screen. One column = 30 tile writes = 60 PPU register writes ($2006 address + $2007 data, 30 times). This fits within VBlank if done efficiently.

### Sprite 0 Hit (Unit 63)

Place a sprite (sprite 0 in OAM) at the bottom edge of the status bar area. When the PPU draws this sprite and it overlaps a non-transparent background pixel, it sets bit 6 of $2002 (PPUSTATUS). The code:

1. Clear the Sprite 0 flag by reading $2002
2. Write scroll = 0 for the status bar (no scroll)
3. Wait for Sprite 0 hit (poll $2002 bit 6)
4. Write the gameplay scroll value

The status bar renders with scroll 0 (fixed), then the level renders with the camera scroll. Two display zones, one screen.

---

## 6502 Concepts Introduced

1. Double-write PPU registers -- $2005 latch behaviour (Unit 49)
2. 16-bit scroll tracking -- two bytes with carry to nametable bit (Unit 52)
3. Column-based nametable writes -- sequential $2006/$2007 pattern (Unit 53)
4. VBlank cycle budgeting -- count writes per frame (Unit 56)
5. World-to-screen coordinate conversion -- subtract scroll offset (Unit 57)
6. Sprite 0 hit polling -- `BIT $2002` / `BVS`/`BVC` pattern (Unit 63)
7. Split-scroll technique -- different scroll values for different screen zones (Unit 63)

---

## Hardware

### New in Phase 4

| Register | Address | Purpose | Introduced |
|----------|---------|---------|------------|
| PPUSCROLL | $2005 | Horizontal and vertical scroll (double-write) | Unit 49 |
| PPUCTRL bits 0-1 | $2000 | Nametable select (extends scroll range) | Unit 52 |
| Sprite 0 hit | $2002 bit 6 | Screen split detection | Unit 63 |

---

## Game State at Phase End

After Unit 64:

- **Hardware scrolling** -- smooth pixel-level camera following the player
- **Seamless nametable loading** -- new columns appear as the camera moves
- **Attribute seam updates** -- colours correct at the scroll boundary
- **Camera dead zone** -- player moves freely in the centre before scrolling triggers
- **Camera bounds** -- scroll stops at level start and end
- **Long levels** -- 4+ screens of continuous gameplay
- **Fixed status bar** -- Sprite 0 hit keeps HUD in place while level scrolls
- **Scroll-aware collision** -- tile checks work in world coordinates
- **Scroll-aware sprites** -- objects positioned relative to camera

The world scrolls. The NES is doing what it was built for. Levels are no longer confined to one screen.

---

## What Carries to Phase 5

- **Nametable write patterns** -- reused for tile animation and dynamic background changes
- **VBlank budget awareness** -- essential when adding music engine and more PPU updates
- **Sprite 0 technique** -- extended for palette splits and parallax effects
- **Scroll coordinate system** -- all future game objects use world coordinates

---

**Version:** 1.0
**Last Updated:** 2026-02-06
