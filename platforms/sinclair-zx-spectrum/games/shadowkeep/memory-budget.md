# Shadowkeep — 48 KB Memory Budget Audit

> *"Every byte of a 48 KB Spectrum is accounted for. If it isn't here, we don't have room for it."*

**Anchored to:** [shadowkeep-32-engineering-plan.md](shadowkeep-32-engineering-plan.md). Updated as the engine takes shape.

## Why this matters

We have **48 KB** total. Of that, ~7 KB is fixed (screen + system) and the rest is ours. By Arc 2 we're storing: code, pre-shifted sprites (hero + NPC × 8 shifts × N frames), tile data, decoration sprites, music, SFX, three rooms of layout data, lighting cache, object lists, game state, and stack. Without a budget, we discover by Unit 24 that everything's broken because the third room overlaps the NPC sprite table.

This audit establishes:
1. The fixed memory map (Spectrum architecture)
2. Allocated regions with specific load addresses
3. Per-region byte counts with realistic estimates
4. Total used vs total available
5. Safety margin and risk register

---

## 1. Spectrum 48K memory map (architecture-level)

```
$0000-$3FFF  ROM (16 KB)                       — read-only, contains BASIC
$4000-$57FF  Screen bitmap (6 KB)              — pixel data, 256×192 @ 1bpp
$5800-$5AFF  Screen attribute (768 bytes)      — colour cells, 32×24
$5B00-$5BFF  Printer buffer (256 bytes)        — reclaimable if no printer use
$5C00-$5CB5  System variables (181 bytes)      — used by ROM IM 1 ISR
$5CB6-$5CCB  Channel info (22 bytes)           — used by ROM I/O
$5CCC-$7FFF  Free RAM (~9.8 KB)                — BASIC normally lives here
$8000-$FFFF  Free RAM (32 KB)                  — typically code + working RAM
```

**Contention warning:** the address range `$4000-$7FFF` is *contended* — the ULA and CPU share that memory bus, so the CPU is delayed during active scanlines when accessing it. Code that *runs* there is slowed; code that just *reads data* there is also slowed. Best practice:

- **Code lives at `$8000+`** (uncontended) for performance-critical paths.
- **Static data** *can* live in `$5CCC-$7FFF` if it's accessed rarely.

For Shadowkeep, we put everything at `$8000+` unless we need the headroom — Spectrum game memory is hierarchical: $8000+ first, then $5CCC-$7FFF for overflow.

---

## 2. Allocated regions

Specific addresses for the 32-unit Shadowkeep at completion. All addresses subject to refinement as we measure actual byte counts during build.

```
$0000-$3FFF  ROM                                              (16 KB)
$4000-$57FF  Screen bitmap                                    (6 KB)
$5800-$5AFF  Screen attribute (rewritten per-room by lighting) (768 B)
$5B00-$5BFF  Printer buffer (reclaimed for stack-saved data?)  (256 B)
$5C00-$5CCB  System variables + channels (untouched)           (204 B)

$5CCC-$5DFF  Reserved (BASIC area; left untouched, can reclaim if needed) (308 B)
$5E00-$7FFF  Pre-shifted sprite tables (overflow / large assets) (~8.5 KB)

$8000-$????  Code segment (entry, dispatch, all routines)      (~5 KB est.)
$????-$????  Tile and decoration sprite data                   (~700 B est.)
$????-$????  Music + SFX data                                  (~1 KB est.)
$????-$????  Room data (3 rooms × layout + decoration lists)   (~1.3 KB est.)
$????-$????  Working RAM (game state, object list, lighting)   (~1.5 KB est.)
$????-$FDFF  Free space (~21 KB headroom)
$FE00-$FFFF  Stack (512 bytes)
```

**Specific load addresses TBD** during Phase 0 — we set them after measuring real byte counts. The headroom shown is the expected surplus *after* allocating all known needs.

---

## 3. Detailed budget by category

Realistic estimates. **Numbers will shift** during the build; this is the planning baseline.

### 3.1 Code

Estimated size by sub-system. Z80 code density is roughly 30-50 bytes per "small routine," 100-300 bytes per "substantial routine."

| Sub-system | Est. bytes | Notes |
|---|---:|---|
| Tile rendering primitives | 500 | `draw_tile`, `draw_room`, attribute helpers |
| Sprite shifter dispatch | 200 | Selects pre-shifted table by `col & 7` |
| Masked sprite drawing | 250 | `AND mask / OR image` loop |
| Hero update + animation | 200 | Frame timing, walk-state machine |
| Object list management | 250 | Add/remove/sort/dispatch |
| Y-sort routine | 100 | Insertion sort, 16 slots max |
| Tile-map collision query | 100 | `can_move_to_pixel(x, y)` |
| Lighting computation (per room load) | 250 | Manhattan-distance flood, attribute write |
| Music driver (existing, refined) | 250 | From existing Unit 7, ported |
| SFX overlay | 200 | Queue + interleave with music |
| Keyboard input | 100 | QAOP + SPACE polling |
| State machine | 150 | TITLE/PLAY/VICTORY/GAMEOVER/COMPLETED |
| HUD render | 300 | Score, gold, lives glyphs |
| NPC update + AI | 350 | Patrol state machine, collision check |
| Game logic (pickup, victory, death, transition) | 500 | Per-event handlers |
| Title / completion presentation | 300 | Title art display, victory sequence |
| Utility (delay, draw_char, ROM helpers) | 200 | Small helpers, ROM calls |
| **Code total** | **~3,950** | ~4 KB |

### 3.2 Pre-shifted sprite data

The biggest single allocation. Per-sprite math:

**16×16 sprite, masked, pre-shifted:**
- Each row covers 16 pixels = 2 bytes (image) + 2 bytes (mask) = 4 bytes per row
- Per shift, the sprite occupies a 24-pixel-wide area = 3 bytes (image) + 3 bytes (mask) = 6 bytes per row
- 16 rows × 6 bytes = **96 bytes per shifted frame**
- 8 shifts × 96 = **768 bytes per source frame**

| Sprite | Frames | Bytes |
|---|---:|---:|
| Hero (4 walk + 1 idle) | 5 | 5 × 768 = **3,840** |
| NPC #1 (4 walk frames) | 4 | 4 × 768 = **3,072** |
| NPC #2 (4 frames, if used) | 4 | 4 × 768 = **3,072** (optional) |
| **Pre-shifted total (with NPC #2)** | | **~10 KB** |
| **Pre-shifted total (without NPC #2)** | | **~7 KB** |

NPC #2 is decision-deferred (Unit 24). If it's a behavioural variation of NPC #1 (same sprite), we save 3 KB. If it's a new sprite, we eat the cost.

### 3.3 Decoration sprites (cell-aligned, no shift)

Drawn at cell boundaries, so no pre-shifting needed. Smaller per-asset.

| Asset | Size | Frames | Bytes |
|---|---|---:|---:|
| Stone wall tiles (5 variations) | 8×8 | — | 5 × 8 = **40** |
| Floor tiles (5 variations) | 8×8 | — | 5 × 8 = **40** |
| Pillar | 16×24, masked | 1 | 16 × 6 = **96** |
| Altar | 24×16, masked | 1 | 16 × 6 = **96** |
| Sconce | 8×16, masked | 1 | 16 × 2 = **32** |
| Gold piece | 8×8, masked | 1 | 8 × 2 = **16** |
| Gold sparkle | 8×8, masked | 3 | 3 × 16 = **48** |
| Door | 16×16, masked | 4 (anim) | 4 × 64 = **256** |
| **Decoration total** | | | **~620** |

### 3.4 Music + SFX data

| Data | Est. bytes | Notes |
|---|---:|---|
| Title theme (composed, ~60 sec) | 500 | Per [beeper spec](shadowkeep-beeper-spec.md) byte-pair format |
| Footstep SFX | 50 | Short tone burst |
| Pickup chime | 80 | 2-3 note arpeggio |
| Door creak | 100 | Multi-note descending |
| Death sound | 80 | Descending tone |
| Victory chord (3-5 notes + held) | 120 | Final fanfare |
| SFX queue state | 32 | Active SFX position, timer |
| **Music + SFX total** | **~960** | ~1 KB |

### 3.5 Room and tile-map data

| Data | Per room | Rooms | Total |
|---|---:|---:|---:|
| Tile-map (22 × 16 cells) | 352 | 3 | **1,056** |
| Decoration object list (per room) | 64 | 3 | **192** |
| Light source positions | 16 | 3 | **48** |
| Room metadata (name string, transitions) | 32 | 3 | **96** |
| **Room data total** | | | **~1,400** |

### 3.6 Working RAM (game state)

Mutable game state lives in dedicated regions. Sizes are runtime allocations.

| Data | Bytes | Notes |
|---|---:|---|
| Hero state (position, frame, direction) | 16 | Updated per-frame |
| Score, gold count, lives, current room | 8 | |
| Best score (persistent across plays) | 4 | |
| Object list (16 slots × 16 bytes per slot) | 256 | Position, type, frame, state, etc. |
| Object sort indices | 16 | |
| Lighting cache for current room | 768 | Computed attribute bytes; rewritten on room load |
| Save-under-hero bitmap buffer | 64 | For dirty-rect erase-and-redraw |
| Save-under-hero attribute buffer | 4 | |
| Save-under-objects (16 × 64 bytes) | 1,024 | If we save background per-object — alternative is full room redraw each frame |
| SFX queue state | 32 | |
| State machine variables (game_state, transition_timer) | 16 | |
| Animation frame counters | 32 | Per-object animation timing |
| **Working RAM total** | **~2,250** | ~2.2 KB |

The save-under-objects buffer is the largest item here, and there's a design choice: per-object background-saving means we redraw fewer cells per frame, but it costs 1 KB. Alternative is "redraw whole room each frame" which is cheaper memory-wise but much costlier CPU-wise. For now budget the 1 KB.

### 3.7 Stack

The Z80 stack grows downward from initial SP. Typical use: ~200 bytes at peak (call depth ≤ 12, each call ≤ 16 bytes pushed). Reserve 512 bytes for safety.

`SP` initial value: `$0000` (which wraps to `$FFFF` on first push). Actual stack lives at `$FE00-$FFFF`.

---

## 4. Totals

```
Code:                       ~3,950 bytes     (≈4 KB)
Pre-shifted sprites:        ~7,000 bytes     (NPC #2 = behaviour-only)
                           ~10,000 bytes     (NPC #2 = new sprite)
Decoration sprites:           ~620 bytes
Music + SFX:                  ~960 bytes
Room data:                  ~1,400 bytes
Working RAM:                ~2,250 bytes
Stack:                        ~512 bytes
─────────────────────────────────────
Total (NPC #2 = behaviour):  ~16,700 bytes   (≈16.3 KB)
Total (NPC #2 = sprite):     ~19,700 bytes   (≈19.2 KB)
```

**Available RAM** (48 KB minus ROM and screen): ~41 KB
**Used:** 16-19 KB
**Free:** **22-25 KB headroom**

We are comfortable. Substantial slack for growth, surprises, and the inevitable underestimates.

---

## 5. Risk register (memory-specific)

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| M1 | Code bloat — actual code 2× estimate (8 KB instead of 4) | Medium | Low | Headroom absorbs. Watch per-unit code size during build. |
| M2 | Hero animation grows from 5 to 8 frames (more nuanced walk) | Low | Medium | Each extra frame = 768 bytes pre-shifted. 3 extra frames = +2.3 KB. Still fits with headroom. |
| M3 | NPC #2 is a new sprite (not behaviour variation) | Medium | Medium | 3 KB cost confirmed in budget. Decide explicitly at Unit 24 design time. |
| M4 | Decoration sprites need pre-shifting (artistic decision) | Low | High | Decoration sprites are designed to be cell-aligned. If a designed sprite ends up needing sub-cell positioning, costs jump significantly. Mitigate: enforce cell-alignment as a design constraint. |
| M5 | Pre-computed lighting per room (3× cache) | Low | Low | If we want all room lighting cached for instant transitions, +1,500 bytes. Still fits. |
| M6 | Save-under-objects becomes expensive | Medium | Low | Alternative is "redraw whole room each frame." That's CPU-expensive but memory-free. Defer this decision to Unit 9 implementation. |
| M7 | Music data is larger than 500 bytes | Medium | Low | A complex multi-section composition might run to 1 KB. Headroom absorbs. |
| M8 | Pre-shifted sprite tooling overhead — duplicate copies of edge data | Low | Low | Some shifters generate slightly larger output. Budget includes overhead. |

---

## 6. What we DON'T have room for

Forbidden by budget (not by spec — these would force re-scoping):

- A fourth NPC type — 3 KB more
- Multiple full-screen art assets (title, intro, outro) — each ~2 KB if hand-pixelled
- A second composed music track for in-game — 500-1000 bytes
- A 128K Spectrum port without restructuring (we explicitly commit to 48K)
- Save state to memory beyond best-score
- A 9-room keep (the Atic Atac scale would require restructuring)

If any of these become essential, they trigger a memory re-budget. Per the decision record, they would trip drift triggers (out-of-scope features) — so they shouldn't arise.

---

## 7. Pre-shifted sprite tooling implications

`convert_sprite.py` (the Piskel-PNG-to-bytes pipeline) must be careful about:

- **Mask-vs-image separation:** the source PNG uses one designated "transparent" colour (probably bright magenta or alpha-zero). The script generates two output streams: image (1 where opaque pixel set, 0 elsewhere) and mask (0 where opaque, 1 elsewhere — AND mask preserves background).
- **Pre-shift generation:** for each X-offset 0-7, the image bits are rotated right by N positions (with bytes growing by one column). 16-wide source becomes 24-wide shifted output.
- **Empty-row optimisation:** rows that are all-mask (no image) can be skipped — but that complicates the runtime draw loop. Defer this optimisation; pay the bytes.
- **Self-consistency check:** before emitting, the tool computes the shifted images and verifies they reverse-shift back to source. Catches mask/image alignment bugs early.

---

## 8. Build-time vs run-time memory

Some data is **build-time only** (defined as `.inc` files included in the source `.asm`, baked into the SNA image): code, sprite tables, music data, room data tables.

Some data is **run-time only** (allocated by `defs` or by `org`, populated during play): object list, save-under buffers, sort indices, animation state.

Some data is **build-time initial + run-time mutable**: room data table is built-time initial; gold pickup mutates it during play. So at runtime, the room data lives in RAM (mutable) but is initialised from build-time source.

The 32-unit plan's `init_state` routine (introduced in existing Unit 8, retained) handles the copy. This is how multi-playthrough state-reset works.

---

## 9. Memory layout diagram (estimated)

```
ADDRESS        REGION                                  SIZE      RUNNING TOTAL
─────────────────────────────────────────────────────────────────────────────
$0000-$3FFF    ROM                                     16 KB         (16 KB)
$4000-$57FF    Screen bitmap                            6 KB        (22 KB)
$5800-$5AFF    Screen attribute (lit per-room)          768 B       (22.75 KB)
$5B00-$5BFF    Printer buffer (untouched)               256 B       (23 KB)
$5C00-$5CCB    System vars / channels (untouched)       204 B       (23.2 KB)
$5CCC-$7FFF    Free / overflow zone                     9.8 KB free
$8000-$8F00    Code segment                             ~4 KB     (~27 KB)
$8F00-$9180    Decoration + tile sprites                ~640 B    (~27.6 KB)
$9180-$9580    Music + SFX data                         ~1 KB     (~28.6 KB)
$9580-$9AE0    Room data (3 rooms layout + objects)     ~1.4 KB   (~30 KB)
$9AE0-$A4E0    Working RAM (state, lists, lighting)     ~2.5 KB   (~32.5 KB)
$A4E0-$FDFF    Free space (BIG headroom)                ~22 KB free
$FE00-$FFFF    Stack                                    512 B     (48 KB)
$????-$????    Pre-shifted sprites: 7-10 KB             one of:
                                                        $5E00-$7BD0 (overflow zone)
                                                        OR $A500-$C300 (post-state)
```

**Layout TBD precisely in Phase 0** based on actual byte measurements. The runtime cost of accessing data at $5CCC-$7FFF is slightly higher (memory contention) but for static data (sprites) accessed during cell-aligned draws, this is acceptable. We may end up putting pre-shifted hero sprite at $5E00 and the rest at $8000+, or all at $8000+ if there's room. Decision: measure first, allocate second.

---

## 10. Validation

After Phase 0 (Week 4), with the first hero sprite and first room rendering:

- [ ] Measure actual code size (assembler reports)
- [ ] Measure actual pre-shifted sprite size for first hero frame
- [ ] Verify everything loads in a 48K SNA
- [ ] Verify program runs cleanly (no stack overflow, no overwrites)

If any single component is >50% above estimate, re-budget. Don't continue past Phase 0 with a known overrun.

Re-validate at:
- End of Phase 1 (Week 8): hero + walk cycle integrated
- End of Phase 2 (Week 12): full Arc 1 engine running
- End of Phase 3 (Week 16): NPC + lives
- End of Phase 4 (Week 20): full Arc 2 functionality

---

## 11. Reference

- [Spectrum memory map (vault entry)](../vault/systems/zx-spectrum.mdx) — the architecture authority
- [ULA contention details](../vault/hardware/ula.mdx) — why uncontended RAM matters for performance
- [shadowkeep-32-engineering-plan.md](shadowkeep-32-engineering-plan.md) — the parent plan

## Log

| Date | Event |
|---|---|
| 2026-05-18 | Initial budget. Comfortable headroom (~22-25 KB free). Re-measured during Phase 0 with real byte counts. |
