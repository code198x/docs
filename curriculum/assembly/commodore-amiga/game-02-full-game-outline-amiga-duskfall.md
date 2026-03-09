# Full Game Outline: Amiga Duskfall (256 Units)

**Game:** Duskfall (Game 2)
**Units:** 256 (8 phases × 32 units)
**Genre:** Parallax showcase (side-scrolling action)
**Inspired by:** Shadow of the Beast, Agony, Lionheart
**Target Quality:** Commercial-grade parallax showcase (1989–91 era)

---

## Premise

The sun sets over the Veillands. The dusk brings creatures from beyond the horizon — shadow beasts that dissolve in daylight. You run east, toward the source, through a world that scrolls in impossible depth: distant mountains barely move, mid-ground forests drift, foreground ruins rush past. Seven layers of parallax. The Amiga defined itself with this effect. Shadow of the Beast made people buy the machine. Duskfall teaches how it worked.

---

## Why This Game

Shadow of the Beast was a tech demo that happened to be a game. Psygnosis used dual playfield mode — two independent 3-bitplane playfields scrolling at different speeds — to create an illusion of depth that no other home computer could match. It made the Amiga's reputation.

Duskfall teaches:
- **Dual playfield mode** (DBLPF in BPLCON0) — two independent scrolling layers
- **Hardware scroll registers** (BPLCON1) — fine scroll per playfield
- **Bitplane pointer arithmetic** (BPLxPT) — coarse scroll via pointer manipulation
- **Copper per-line effects** — gradient skies, colour cycling, water reflections
- **Blitter BOBs** — software sprites composited onto the scrolling background
- **BOB save/restore** — save background, draw BOB, restore on next frame
- **Paula MOD music** — ProTracker module playback during gameplay
- **DMA timing** — understanding when the Blitter and CPU can coexist

---

## 68000 Progression

| Phase | 68000/Amiga Focus |
|-------|------------------|
| 1 (Horizon) | Display setup, dual playfield, hardware scroll registers, Copper gradients |
| 2 (Layers) | Multi-speed parallax, bitplane pointer maths, fine/coarse scroll cycle |
| 3 (Silhouettes) | Blitter BOBs (cookie-cut), save/restore background, BOB animation |
| 4 (Pursuit) | Player movement, combat, enemies as BOBs, collision |
| 5 (Dusk) | Per-line Copper effects: colour gradients, water reflections, atmospheric haze |
| 6 (Resonance) | Paula MOD playback, SFX mixing, per-stage themes |
| 7 (The Veil) | 5 stages with distinct parallax configurations, bosses, level streaming |
| 8 (Dawn) | Title, high scores, difficulty, ADF distribution, polish |

---

## Phase 1: Horizon (Units 1–32)

**Goal:** Dual playfield display with two independently scrolling layers.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 1-4 | Display setup review | Bitplanes, Copper list, DIWSTRT/DIWSTOP, DDFSTRT/DDFSTOP (from Exodus) | Display configured |
| 5-8 | Dual playfield mode | BPLCON0 DBLPF bit. Two playfields: PF1 (bitplanes 1,3,5), PF2 (bitplanes 2,4,6). Independent palettes. | **Dual playfield active** |
| 9-12 | Playfield 1: background | Mountains and sky. 3 bitplanes (8 colours). Drawn in static bitmap. | Background layer |
| 13-16 | Playfield 2: foreground | Ground, platforms, obstacles. 3 bitplanes (8 colours). The gameplay layer. | Foreground layer |
| 17-20 | Foreground scrolling | BPLCON1 fine scroll (PF2). BPLxPT pointer adjustment for coarse scroll. The foreground moves. | **Foreground scrolls** |
| 21-24 | Background scrolling (slower) | BPLCON1 fine scroll (PF1) at half speed. BPLxPT for PF1 coarse. Two layers, different speeds. | **Parallax!** |
| 25-28 | Copper gradient sky | Copper changes background colour per scanline. Blue at top → orange at horizon. Sunset. | Atmospheric sky |
| 29-32 | Terrain data | Foreground tile map. New columns drawn at scroll edge. Level data drives the scroll. | Data-driven scrolling |

**Key Teaching Moment (Units 5-8):**
Dual playfield mode is the Amiga's unique display trick. Set the DBLPF bit in BPLCON0, and the six bitplanes split into two independent 3-bitplane (8-colour) playfields. Each has its own scroll registers, its own palette entries, and its own priority. Playfield 1 is the background; Playfield 2 is the foreground with transparency where its colour 0 appears. One hardware feature creates multi-layer parallax.

**Key Teaching Moment (Units 17-20):**
Hardware scrolling on the Amiga: BPLCON1 bits 0-3 control PF1 fine scroll (0-15 pixels). Bits 4-7 control PF2 fine scroll. When fine scroll reaches 16, reset to 0 and adjust the BPLxPT bitplane pointers by 2 bytes (one word = 16 pixels in lowres). The coarse scroll is invisible — the bitmap data simply starts from a different offset. No data copying, no shifting bytes. Pure pointer maths.

**End of Phase 1:** Dual playfield parallax with a Copper gradient sky. Two layers scrolling at different speeds. The Amiga's visual signature, from scratch.

---

## Phase 2: Layers (Units 33–64)

**Goal:** Multiple parallax speeds, smooth scrolling, tile streaming.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 33-36 | Variable scroll speeds | PF1 at 1/4 speed, PF2 at full speed. Multiple speed ratios tested. | Depth control |
| 37-40 | Copper scroll splits | Copper changes PF1 scroll mid-frame: sky layer at 1/8 speed, mountain layer at 1/4 speed — within one playfield. | **Three+ speed layers** |
| 41-44 | Tile-based foreground | 16×16 pixel tiles. Tile map wider than screen. New column drawn at leading edge via Blitter. | Tiled terrain |
| 45-48 | Tile variety | Ground, platform, wall, slope (visual only), decoration. Multiple tile graphics per terrain type. | Visual richness |
| 49-52 | Background tile layers | Background layer also tiled: distant mountains, mid-ground trees. Drawn once (static) or slowly scrolled. | Layered backgrounds |
| 53-56 | Oversized bitmap for scroll | Bitmap wider than display: extra columns provide scroll margin. Blitter draws new tiles into the margin. | Smooth tile streaming |
| 57-60 | DMA timing | Bitplane DMA, Blitter DMA, and CPU all compete for chip RAM bus. Measure when each has access. | DMA awareness |
| 61-64 | Scroll performance | Full parallax running at 50fps. Profile the frame: Copper setup, Blitter tile draw, pointer updates. | Performance budget |

**End of Phase 2:** Multi-speed parallax with tiled terrain streaming. 4+ effective parallax layers. Smooth, tear-free, 50fps.

---

## Phase 3: Silhouettes (Units 65–96)

**Goal:** Blitter BOBs — software sprites composited onto the scrolling background.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 65-68 | Blitter copy (A→D) | BLTCON0 minterms, source/destination pointers, Blitter size register | Raw Blitter copy |
| 69-72 | Cookie-cut (A=source, B=mask, C=bg, D=result) | Full minterm: D = (A AND B) OR (C AND NOT B). Masked sprite onto background. | **BOB rendering** |
| 73-76 | Save background | Before drawing BOB: Blitter copies background area to a save buffer. | Save-under |
| 77-80 | Restore background | Before next frame's BOB draw: Blitter copies save buffer back. No ghost trails. | Clean restore |
| 81-84 | BOB animation | Multiple frames per BOB. Pointer swap per frame. Walk cycle, attack cycle. | Animated BOBs |
| 85-88 | Player BOB | The runner: walk cycle (4 frames), jump, attack, death. Composited onto scrolling PF2. | **Player on parallax** |
| 89-92 | Player movement | Joystick moves player. Horizontal movement relative to scroll. Jump with gravity. | Platform physics |
| 93-96 | Player-terrain collision | Read pixel data from the foreground bitplane at player position. Solid = blocked. | Collision on scrolling bg |

**Key Teaching Moment (Units 69-72):**
Cookie-cut masking is the Blitter's signature operation. The minterm `D = (A AND B) OR (C AND NOT B)` means: where the mask (B) is set, use the source image (A). Where the mask is clear, keep the background (C). The result (D) is a sprite cleanly composited onto the background. One Blitter operation per BOB — no CPU involvement in the pixel work.

**End of Phase 3:** Player runs and jumps on a multi-layer parallax background. BOBs composited via Blitter cookie-cut with save/restore. The core display system is complete.

---

## Phase 4: Pursuit (Units 97–128)

**Goal:** Combat, enemies, and gameplay on the parallax display.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 97-100 | Player attack | Button press → attack animation → hitbox active for N frames | Melee combat |
| 101-104 | Enemy BOBs | Enemies with world-space positions. Scroll into view. Patrol or chase. | Enemies on parallax |
| 105-108 | Enemy-player collision | BOB overlap detection (bounding box based on world positions) | Contact damage |
| 109-112 | Enemy defeat | Attack hitbox overlaps enemy → enemy death animation → score | Kills |
| 113-116 | Ranged attack | Player fires a projectile BOB. Travels right. Hits enemies or exits screen. | Ranged combat |
| 117-120 | Enemy variety | Walkers, flyers, shooters. Different BOB graphics, speeds, behaviours. | Threat variety |
| 121-124 | Health and lives | Health bar in Copper panel (below game area). 3 lives. | Stakes |
| 125-128 | Stage 1 complete | Full scrolling stage with enemies, combat, health, score. End-of-stage boss area. | **First stage playable** |

**End of Phase 4:** A complete side-scrolling action game on multi-layer parallax. One stage with enemies and a boss. Plays like Shadow of the Beast — but with better combat.

---

## Phase 5: Dusk (Units 129–160)

**Goal:** Advanced Copper effects that define the Amiga's visual character.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 129-132 | Per-line colour gradients | Copper changes palette entries per scanline. 256 apparent colours from 32 palette entries. | Smooth gradients |
| 133-136 | Water reflection | Below a "water line": Copper reverses scroll direction and applies blue palette shift. Foreground reflects. | **Water reflection** |
| 137-140 | Colour cycling | Copper rotates palette entries each frame. Water appears to flow. Fire flickers. Stars twinkle. | Animated palette |
| 141-144 | Atmospheric haze | Distant parallax layers: Copper blends their palette toward the sky colour. Distance fog effect. | Depth haze |
| 145-148 | Per-stage palettes | Each stage has a time-of-day palette: Stage 1 (sunset), Stage 2 (twilight), Stage 3 (night), Stage 4 (pre-dawn), Stage 5 (dawn). | Visual journey |
| 149-152 | Copper rainbow | Smooth rainbow effect across the sky (Copper cycles through all 4096 colours). Used in title/transitions. | Amiga showcase |
| 153-156 | Screen flash effects | Boss hit: Copper overrides palette briefly (all white). Damage: red flash. Collect: gold flash. | Visual feedback |
| 157-160 | Copper performance | How many Copper instructions fit in a frame? When do Copper waits overlap with bitplane DMA? | Copper timing mastery |

**Key Teaching Moment (Units 133-136):**
Water reflection is a single Copper trick: at the water line, reverse the vertical scroll direction. The bitplane pointers count backward instead of forward, so the image appears flipped. A blue palette shift tints the reflection. One Copper WAIT + a few MOVEs create a convincing reflection without any CPU cost or extra memory.

**End of Phase 5:** Per-line gradients, water reflections, colour cycling, atmospheric haze. The Amiga's visual identity, fully expressed.

---

## Phase 6: Resonance (Units 161–192)

**Goal:** Paula MOD music and sound effects.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 161-168 | Paula audio setup | DMA audio channels, sample pointer, length, period, volume. Play a sample. | First audio |
| 169-176 | MOD playback engine | ProTracker module format. Pattern sequencer. 4 channels. CIA timer-driven. | **Music plays** |
| 177-180 | Per-stage themes | Stage 1: melancholic sunset. Stage 3: tense night. Stage 5: triumphant dawn. | Musical journey |
| 181-184 | SFX mixing | Sound effects on channels 2-3. Music on channels 0-1. Brief SFX interrupts then restores. | Audio layering |
| 185-188 | SFX library | Attack, hit, enemy death, collect, jump, land, boss damage, door. | Comprehensive audio |
| 189-192 | Audio balance | Volume levels, SFX priority, music doesn't drown effects, effects don't kill music | Professional mix |

**End of Phase 6:** ProTracker MOD playback with per-stage themes. SFX mixed over music. The Amiga sounds as good as it looks.

---

## Phase 7: The Veil (Units 193–224)

**Goal:** 5 complete stages with distinct parallax configurations and bosses.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 193-196 | Stage 2: Twilight Forest | Darker palette, tree silhouettes in PF1, forest floor in PF2. Bat enemies. | Second stage |
| 197-200 | Stage 3: Night Ruins | Near-black palette with moonlight highlights. Ruin platforms. Ghost enemies. Water section with reflection. | Third stage |
| 201-204 | Stage 4: Pre-Dawn Marsh | Mist effect (Copper haze layer), marsh terrain, swamp creatures. Faint sky brightening. | Fourth stage |
| 205-208 | Stage 5: Dawn | Palette brightens across the stage. Final enemies. The source revealed. Vertical section (climb). | **Final stage** |
| 209-212 | 5 bosses | One per stage. Multi-BOB constructions. Pattern attacks. Escalating difficulty. | Guardian encounters |
| 213-216 | Boss arenas | Scroll stops. Arena boundaries. Background shifts to boss-specific parallax. | Dramatic encounters |
| 217-220 | Level streaming | Stages are longer than memory. Load new tile columns from disk during scroll (masked by Blitter copy). | Memory management |
| 221-224 | Stage transitions | Current stage fades (Copper palette → black). New stage loads. Palette fades in. Brief title card. | Paced progression |

**End of Phase 7:** 5 stages spanning sunset to dawn. Distinct parallax configurations, enemies, and bosses per stage. The visual journey mirrors the time of day.

---

## Phase 8: Dawn (Units 225–256)

**Goal:** Commercial polish, distribution.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 225-228 | Title screen | "DUSKFALL" with Copper rainbow and parallax landscape demo. MOD title theme. | Presentation |
| 229-232 | Attract mode | Automated playthrough of Stage 1 opening. Shows parallax in motion. | Demo |
| 233-236 | High scores | Top 5 with initials. Score based on enemies, time, health remaining. | Competition |
| 237-240 | Difficulty select | Easy (slow scroll, weak enemies, more health), Normal, Hard (fast, dense, less health) | Accessibility |
| 241-244 | Ending sequence | Stage 5 boss defeated → the veil lifts → dawn breaks across all parallax layers (Copper palette transitions from night to full daylight) → credits over sunrise | **Narrative climax** |
| 245-248 | ADF creation | Bootable disk with loader, title, 5 stages (multi-file or compressed single load) | Distribution |
| 249-252 | System-friendly startup | Proper Exec-compatible startup, save/restore system state | OS compatibility |
| 253-256 | **Complete game** | Testing, balance, polish | **Ship it** |

---

## Technical Notes

### Dual Playfield Mode

```asm
; Enable dual playfield
    move.w  #$6200,BPLCON0(a5)  ; 6 bitplanes + DBLPF
    ; PF1 = bitplanes 1,3,5 (background)
    ; PF2 = bitplanes 2,4,6 (foreground)

; Independent scroll:
    ; BPLCON1 bits 0-3 = PF1 fine scroll
    ; BPLCON1 bits 4-7 = PF2 fine scroll
    move.w  d0,BPLCON1(a5)  ; Combined fine scroll value

; Independent palette:
    ; PF1 uses colours 0-7
    ; PF2 uses colours 8-15 (colour 8 = transparent)
```

### Copper Per-Line Gradient

```asm
; In the Copper list:
; For each scanline in the sky area:
    dc.w    $2C01,$FFFE     ; WAIT for line $2C
    dc.w    COLOR00,$046C   ; Set background to dark blue
    dc.w    $2D01,$FFFE     ; WAIT for line $2D
    dc.w    COLOR00,$058C   ; Slightly lighter blue
    ; ... one WAIT+MOVE pair per scanline
    ; 256 lines = 512 Copper instructions for full-screen gradient
```

### BOB Cookie-Cut

```asm
; Blitter cookie-cut: composite BOB onto background
; A = BOB source data
; B = BOB mask
; C = background (screen)
; D = destination (screen, same as C for in-place composite)

blit_bob:
    ; Wait for Blitter
    btst    #14,DMACONR(a5)
    bne.s   blit_bob

    move.l  a0,BLTAPT(a5)      ; Source image
    move.l  a1,BLTBPT(a5)      ; Mask
    move.l  a2,BLTCPT(a5)      ; Background
    move.l  a2,BLTDPT(a5)      ; Destination (same as background)
    move.w  #$0FCA,BLTCON0(a5) ; Minterm: D = (A AND B) OR (C AND NOT B)
    move.w  #0,BLTCON1(a5)
    move.w  #(screen_width-bob_width)/8,BLTAMOD(a5)  ; Modulos
    move.w  #(screen_width-bob_width)/8,BLTBMOD(a5)
    move.w  #(screen_width-bob_width)/8,BLTCMOD(a5)
    move.w  #(screen_width-bob_width)/8,BLTDMOD(a5)
    move.w  #(bob_height*64)+(bob_words),BLTSIZE(a5)  ; Start blit
    rts
```

### Frame Budget

| Task | Time (approx) | Notes |
|------|---------------|-------|
| Copper list execution | ~15μs per instruction | Runs in parallel with display |
| Blitter: BOB draw (32×32, 3 planes) | ~50μs per BOB | 6 BOBs = ~300μs |
| Blitter: save/restore | ~50μs per BOB | 6 BOBs = ~300μs |
| Blitter: tile column draw | ~100μs | Once per coarse scroll |
| CPU: player physics | ~20μs | Position, gravity, collision |
| CPU: enemy AI (6 enemies) | ~60μs | Movement, state updates |
| CPU: collision detection | ~30μs | Player-enemy, bullet-enemy |
| MOD replay (CIA interrupt) | ~100μs per tick | ~4 ticks per frame |
| **Total** | **~1ms** | **Frame = 20ms (50fps). Generous margin.** |

The Amiga has headroom. The frame budget is comfortable at 50fps with 6 BOBs, parallax, Copper effects, and MOD music. The challenge isn't speed — it's getting the DMA scheduling right so Blitter, Copper, and bitplane fetch don't collide.

---

## The Amiga Arc (So Far)

| Game | Chipset focus | Display technique | Scale |
|------|-------------|------------------|-------|
| Exodus | Blitter as game mechanic | Single playfield, bitmap terrain | Fixed-screen puzzle |
| Duskfall | Copper + dual playfield | Multi-layer parallax, BOB sprites | 5-stage side-scroller |

Exodus teaches the Blitter. Duskfall teaches the Copper and dual playfield. Together they cover two of the three custom chips. Redline will complete the triangle with advanced Copper per-scanline rendering.

---

## Changelog

- **v1.0 (2026-03-09):** Initial outline. New Game 2 for the restructured Amiga assembly track. Parallax showcase with dual playfield mode.
