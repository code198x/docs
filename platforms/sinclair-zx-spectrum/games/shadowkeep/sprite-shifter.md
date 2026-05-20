# Shadowkeep — Sprite Shifter Specification

> *"Pre-shifted sprite tables: 8 versions per frame, generated at build time, masked drawing at runtime. The thing that makes the hooded thief walk smoothly across the keep."*

**Anchored to:** [shadowkeep-32-engineering-plan.md](shadowkeep-32-engineering-plan.md) §5.2, [shadowkeep-32-memory-budget.md](shadowkeep-32-memory-budget.md) §3.2.

**Implements:** Engine subsystem A2 (sprite shifter + masked draw primitive). **Blocks:** Units 5-8 (hero work).

---

## 1. Purpose

Enable a 16×16 sprite to be drawn at any pixel column on the Spectrum screen, with the background preserved underneath the sprite, at speed acceptable for 50 fps animation.

**Why pre-shifted, not runtime shift:** runtime bit-shifting of a sprite takes ~25 T-states per byte. A 16×16 sprite is 32 image bytes plus 32 mask bytes per frame; shifting each costs ~1,600 T-states. Pre-shifting is free at runtime — we just look up the right shifted version.

**Memory cost confirmed:** 768 bytes per source frame (8 shifts × 96 bytes per shifted form). 5 hero frames = 3,840 bytes.

---

## 2. Source format

### 2.1 Piskel file layout

Each source sprite lives under its game's asset directory:

```
code-samples/sinclair-zx-spectrum/assets/game-01-shadowkeep/sprites/<role>/
    source.piskel         ← canonical editable file (Piskel's JSON format)
    frame-0.png           ← exported frames (PNG, indexed)
    frame-1.png
    ...
```

Pipeline-validation assets that are not part of any game live separately:

```
code-samples/sinclair-zx-spectrum/assets/test/sprites/test-pattern.png
```

Future games get their own `assets/game-NN-<name>/sprites/` tree — the per-game prefix avoids namespace collisions across the 16-games-per-platform plan.

Frames are exported as **single PNGs**, not sprite sheets — each frame is one numbered file. This keeps the conversion script simple (no PNG-row-splitting logic).

### 2.2 PNG format conventions

Each PNG is **16 wide × 16 tall** (for hero / NPC) or **other-specified** size (decorations may vary). The sprite is drawn with:

| PNG pixel | Means | Image bit | Mask bit |
|---|---|---|---|
| Transparent (alpha 0) | Background — no sprite here | 0 | 1 (preserve background) |
| Opaque "ink" colour (e.g., black) | Sprite pixel set | 1 | 0 (overwrite) |
| Opaque "fill" colour (e.g., white) | Sprite pixel clear (visible cell-attribute paper) | 0 | 0 (overwrite) |

Two opacity-by-colour conventions, in order of preference:

1. **Alpha-based** (default): alpha-0 pixels are transparent; everything else is sprite content. Image bit = 1 if pixel is the designated "ink" colour (default: pure black `#000000`); 0 otherwise.

2. **Magenta-key** (fallback if Piskel exports don't preserve alpha cleanly): a single colour (`#FF00FF` bright magenta) marks transparent. Any other colour is sprite content; image bit = 1 if colour is "ink" (default: black), 0 if "fill" (default: white).

The convention is selected by the `--alpha` or `--magenta` flag on `convert_sprite.py`.

### 2.3 Naming convention

Sprite frames named `<role>-<state>-<frame>`. Examples:

```
assets/game-01-shadowkeep/sprites/hero/walk-down-0.png
assets/game-01-shadowkeep/sprites/hero/walk-down-1.png
assets/game-01-shadowkeep/sprites/hero/walk-down-2.png
assets/game-01-shadowkeep/sprites/hero/walk-down-3.png
assets/game-01-shadowkeep/sprites/hero/idle.png

assets/game-01-shadowkeep/sprites/npc-spectre/walk-0.png
assets/game-01-shadowkeep/sprites/npc-spectre/walk-1.png
assets/game-01-shadowkeep/sprites/npc-spectre/walk-2.png
assets/game-01-shadowkeep/sprites/npc-spectre/walk-3.png

assets/game-01-shadowkeep/sprites/decoration/pillar.png
assets/game-01-shadowkeep/sprites/decoration/altar.png
assets/game-01-shadowkeep/sprites/decoration/sconce.png
assets/game-01-shadowkeep/sprites/decoration/gold-0.png         ← idle gold
assets/game-01-shadowkeep/sprites/decoration/gold-sparkle-1.png ← sparkle frames
assets/game-01-shadowkeep/sprites/decoration/gold-sparkle-2.png
assets/game-01-shadowkeep/sprites/decoration/gold-sparkle-3.png
```

---

## 3. Conversion script: `convert_sprite.py`

### 3.1 Invocation

```bash
python tools/convert_sprite.py \
    --input  assets/game-01-shadowkeep/sprites/hero/walk-down-0.png \
    --output code-samples/sinclair-zx-spectrum/game-01-shadowkeep/sprites/hero_walk_down_0.inc \
    --label  hero_walk_down_0 \
    --shifts 8 \
    --alpha
```

Flags:
- `--input` — source PNG path
- `--output` — destination .inc path
- `--label` — assembly label prefix (each shift becomes `<label>_shift_N`)
- `--shifts` — number of shifts to generate (8 for hero/NPC; 1 for cell-aligned decorations)
- `--alpha` or `--magenta` — transparency convention

### 3.2 Algorithm

1. Load PNG with Pillow (Python imaging library).
2. Verify width = 16 (hero/NPC) or width ≤ 24 (decorations).
3. For each shift offset 0-7:
   a. Compute output width in bytes: `ceil((source_width + shift) / 8)`. For 16-wide source: 2 bytes at shift 0, 3 bytes at shifts 1-7.
   b. For each row 0 to height-1:
      - For each output byte 0 to width_bytes-1:
        - For each bit 0-7:
          - Compute source pixel x = byte*8 + bit - shift
          - Read pixel at (x, row) from PNG
          - If source x < 0 or x >= source_width or pixel is transparent: image bit = 0, mask bit = 1
          - If pixel is "ink": image bit = 1, mask bit = 0
          - If pixel is "fill" (opaque but not ink): image bit = 0, mask bit = 0
        - Compose image_byte and mask_byte from the 8 bits
      - Emit `defb image_byte, mask_byte, image_byte, mask_byte, ...` (interleaved)
4. **Output uniform width**: even shift 0 (only needing 2 bytes) is padded to 3 bytes — the third byte is `image=0, mask=$FF` (fully transparent). This keeps the runtime draw loop uniform.
5. Self-check: invert the algorithm — read the generated bytes, reconstruct an image, compare to the source. Catch mask/image alignment bugs.

### 3.3 Output format

```asm
; Generated by convert_sprite.py
; Source: assets/game-01-shadowkeep/sprites/hero/walk-down-0.png
; Size: 16x16, 8 pre-shifted versions, interleaved (image,mask) pairs
; Each shift: 16 rows × 3 bytes (image+mask) × 2 = 96 bytes
;
; Memory cost: 8 × 96 = 768 bytes total

hero_walk_down_0_shift_0:
    defb $00, $ff, $00, $ff, $00, $ff   ; row 0
    defb $00, $ff, $7e, $81, $00, $ff   ; row 1  (hood outline starts)
    defb $00, $ff, $42, $bd, $00, $ff   ; row 2  (hood shadow)
    ;     ^img  ^msk  ^img  ^msk  ^img  ^msk
    ; ... 13 more rows ...

hero_walk_down_0_shift_1:
    defb $00, $ff, $00, $ff, $00, $ff   ; row 0
    defb $00, $7f, $3f, $80, $00, $ff   ; row 1  (same pixels shifted right by 1)
    ; ... 14 more rows ...

; ... shifts 2-7 ...
```

**Total: 8 shifts × 16 rows × 6 bytes per row = 768 bytes per sprite frame.**

### 3.4 Self-check output

If conversion succeeds, the script writes a small JSON file alongside the .inc:

```json
{
  "source": "assets/game-01-shadowkeep/sprites/hero/walk-down-0.png",
  "label": "hero_walk_down_0",
  "size": [16, 16],
  "shifts": 8,
  "bytes_per_shift": 96,
  "total_bytes": 768,
  "checksum_image": "a1b2c3...",
  "checksum_mask": "d4e5f6..."
}
```

Re-running the script with the same source produces identical bytes (deterministic output). The JSON is for verification only — not used by the assembler.

---

## 4. Runtime data structures

### 4.1 Sprite address lookup table

For each sprite asset, a flat array of addresses, indexed by `frame × 8 + shift`:

```asm
; Hero address lookup. 5 frames × 8 shifts = 40 entries × 2 bytes = 80 bytes.
hero_sprite_table:
    defw hero_walk_down_0_shift_0, hero_walk_down_0_shift_1
    defw hero_walk_down_0_shift_2, hero_walk_down_0_shift_3
    defw hero_walk_down_0_shift_4, hero_walk_down_0_shift_5
    defw hero_walk_down_0_shift_6, hero_walk_down_0_shift_7
    ; ... 4 more frames, 8 shifts each ...
```

Lookup at runtime:
```asm
; Inputs: A = frame (0-4), B = shift (0-7)
; Output: HL = sprite data address
get_hero_sprite_addr:
    sla a                ; frame * 2 (entries are 2 bytes)
    sla a                ; * 4
    sla a                ; * 8 — but each frame has 8 entries × 2 bytes = 16 bytes
    sla a                ; * 16
    ; Actually: frame*16 + shift*2
    ; Simpler approach below
```

A cleaner version (frame*16 + shift*2):
```asm
get_hero_sprite_addr:
    add a, a             ; A = frame * 2
    add a, a             ; A = frame * 4
    add a, a             ; A = frame * 8
    add a, a             ; A = frame * 16 (entries-per-frame × bytes-per-entry)
    ld c, a
    ld a, b              ; A = shift
    add a, a             ; * 2 (each entry is 2 bytes)
    add a, c             ; A = frame*16 + shift*2
    ld e, a
    ld d, 0
    ld hl, hero_sprite_table
    add hl, de           ; HL = address-of-entry
    ld a, (hl)
    inc hl
    ld h, (hl)
    ld l, a              ; HL = sprite data address
    ret
```

~50 T-states. Acceptable.

### 4.2 Screen address per row

A 16-row sprite spans the screen non-linearly (the Spectrum's bitmap layout). Cleanest approach: a **per-row screen-address table** computed at sprite-draw time, given top-row screen address.

```asm
; Inputs: HL = top-row screen address
; Output: 16 16-bit screen addresses in scratch space
build_row_addrs:
    ld de, row_addrs_scratch
    ld b, 16
.loop:
    ld a, l
    ld (de), a
    inc de
    ld a, h
    ld (de), a
    inc de
    ; Advance HL to next scanline. Within a cell row, that's +$0100.
    ; At cell-row boundary (every 8 rows), the address changes differently.
    ; Use the standard "next scanline" helper:
    inc h                ; +$0100 (next scanline within cell)
    ld a, h
    and $07
    jr nz, .same_cell
    ; Crossed cell boundary — adjust
    ld a, l
    add a, 32            ; +$20 to L
    ld l, a
    jr nc, .no_carry
    inc h                ; carry into H
.no_carry:
    ld a, h
    sub 8                ; back up one cell-row in H
    ld h, a
    ; Special case: crossing the third-of-screen boundary every 64 rows.
    ; ... (this needs care; see implementation notes below)
.same_cell:
    djnz .loop
    ret
```

**Implementation note:** the Spectrum row-to-address arithmetic is gnarly. The canonical recipe is to maintain a `row_addrs` table populated once when the hero moves into a new cell (every 8 frames at 1-pixel-per-frame), not every frame. Computation cost amortises.

Actual implementation deferred to Phase 0 build; the spec just commits to the *interface* (a table of 16 row addresses, populated when needed).

### 4.3 Object struct (sprite carriers)

Each object in the Y-sort list has:

```
object_struct:
    defb x_pixel         ; 0-255 (left edge of sprite)
    defb y_pixel         ; 0-191 (top edge of sprite)
    defb type            ; HERO, NPC, PILLAR, ALTAR, GOLD, DOOR, etc.
    defb frame           ; current animation frame (0-N)
    defb anim_timer      ; ticks until next frame
    defb state           ; type-specific (e.g., NPC patrol direction)
    defb reserved_0
    defb reserved_1
    ; 8 bytes per object total
```

16 objects max × 8 bytes = 128 bytes.

---

## 5. Runtime draw primitive

### 5.1 Masked sprite draw

```asm
; Inputs: HL = sprite data address (pointer into pre-shifted table)
;         IX = row_addrs (table of 16 16-bit screen addresses)
;         B  = number of rows to draw (16 for hero)
;
; Each row: 3 bytes wide (24 bits). For each byte:
;   screen_byte = (screen_byte AND mask) OR image
;
; Trashes: A, B, C, DE, HL, IX

draw_sprite_3wide_16tall:
    ld c, 16             ; row counter
.row_loop:
    ; Fetch screen address for this row
    ld e, (ix+0)
    ld d, (ix+1)
    inc ix
    inc ix
    
    ; Byte 0
    ld a, (de)
    and (hl)             ; mask
    inc hl
    or (hl)              ; image
    inc hl
    ld (de), a
    inc e
    
    ; Byte 1
    ld a, (de)
    and (hl)
    inc hl
    or (hl)
    inc hl
    ld (de), a
    inc e
    
    ; Byte 2
    ld a, (de)
    and (hl)
    inc hl
    or (hl)
    inc hl
    ld (de), a
    
    dec c
    jr nz, .row_loop
    ret
```

**Per-row cost** (rough Z80 T-state count):
- 3 × (LD A, (DE): 7 + AND (HL): 7 + INC HL: 6 + OR (HL): 7 + INC HL: 6 + LD (DE), A: 7 + INC E: 4) = 3 × 44 = 132
- Plus row setup (~30 T-states) = 162 T-states per row
- 16 rows × 162 = 2,592 T-states per sprite

At 50 fps and 69,888 T-states per frame, drawing one sprite = ~3.7% of frame. We can draw ~25 sprites per frame at this cost. Sufficient.

### 5.2 Erase (restore background)

Standard approach: save what was under the sprite before drawing, restore before next draw.

```asm
; Save-under: copy 16 rows × 3 bytes = 48 bytes to save buffer
save_under_sprite:
    ld c, 16
.row_loop:
    ld e, (ix+0)
    ld d, (ix+1)
    inc ix
    inc ix
    
    ld a, (de)
    ld (hl), a
    inc hl
    inc e
    ld a, (de)
    ld (hl), a
    inc hl
    inc e
    ld a, (de)
    ld (hl), a
    inc hl
    
    dec c
    jr nz, .row_loop
    ret
```

**Save buffer per sprite:** 48 bytes. Per object × 16 objects = 768 bytes. (Listed as 1,024 bytes in the memory budget as "save-under-objects" — overhead absorbs this estimate.)

---

## 6. Performance budget

For 16 sprites on screen (worst case in Arc 2 with NPCs + decoration + hero):

- Save-under (per sprite): ~1,800 T-states × 16 = 28,800 T-states
- Draw (per sprite): ~2,600 T-states × 16 = 41,600 T-states

**Total sprite update: ~70,400 T-states.** That's roughly one full frame (69,888 T-states).

This is *very* tight. Strategies:

1. **Don't save-under for static decorations.** Pillars, altars, sconces never move. Save them at room load, never re-save.
2. **Use object lists sparingly.** Static decorations live in room data; only moving things (hero, NPCs, gold-sparkle in progress) live in the object list.
3. **Skip occluded sprites.** If a sprite is fully behind another (large Y-difference), the front sprite's draw already covers it — skip the back one's draw.

After optimisation, expected typical-frame sprite work: 20,000-30,000 T-states (~30-40% of frame). Plus music, AI, input — total around 50-60% of frame. Comfortable.

---

## 7. Edge cases

### 7.1 Sprite partially off-screen

A sprite at x=-4 to x=11 (i.e., off the left edge) needs clipping. Approach:

- **Left edge:** the leftmost column of the sprite is off-screen. Skip byte 0 of each row.
- **Right edge:** the rightmost column is off-screen. Skip byte 2 of each row.
- **Top edge:** start drawing from row N instead of row 0.
- **Bottom edge:** stop drawing at row 16 - N.

Implementation: branch in draw routine based on `x_pixel` and `y_pixel`. Adds ~20 T-states per row for the branch tests; acceptable.

**Simplification for Arc 1:** the hero cannot leave the screen boundary (collision detection prevents it). Decorations are at fixed positions inside the room. So **partial-off-screen only matters for NPCs that walk to room edges** — handle that case explicitly in NPC update logic, not by clipping in draw.

### 7.2 Sprite crossing third-of-screen boundary

Every 64 rows the Spectrum's bitmap address changes by a different formula (third boundaries at row 0, 64, 128, 192). A 16-row sprite *can* cross these boundaries.

Mitigation: pre-computed `row_addrs` table (4.2) handles this correctly. Once the table is right, draw is right.

### 7.3 Sprite drawn over screen vs cell boundaries

The Spectrum's attribute area is per-cell (8×8). When a 16-wide sprite occupies cells at column 5 and 6, those cells' attribute bytes are independent.

For Arc 1 (uniform hero attribute), we set both cells' attributes to the hero attribute when the hero is drawn. For Arc 2 (lighting), attributes are set by the lighting pass and the sprite respects them — i.e., the hero appears in whatever the local light says.

---

## 8. Build integration

### 8.1 Directory structure

```
code-samples/sinclair-zx-spectrum/
    assets/
        sprites/
            hero/
                source.piskel
                walk-down-0.png
                walk-down-1.png
                walk-down-2.png
                walk-down-3.png
                idle.png
            npc-spectre/
                source.piskel
                walk-0.png
                ...
            decoration/
                source.piskel
                pillar.png
                altar.png
                ...
    game-01-shadowkeep/
        sprites/                 ← generated .inc files
            hero_walk_down_0.inc
            hero_walk_down_1.inc
            hero_idle.inc
            npc_spectre_walk_0.inc
            ...
        unit-01/
            01-a-pixel-in-the-dark.asm
            ...
```

### 8.2 Makefile target

```makefile
SPRITES_PNG := $(wildcard assets/game-01-shadowkeep/sprites/*/*.png)
SPRITES_INC := $(patsubst assets/game-01-shadowkeep/sprites/%/%.png, game-01-shadowkeep/sprites/%_%.inc, $(SPRITES_PNG))

assets: $(SPRITES_INC)

game-01-shadowkeep/sprites/%_%.inc: assets/game-01-shadowkeep/sprites/%/%.png
	python tools/convert_sprite.py \
		--input $< \
		--output $@ \
		--label $(basename $(notdir $<)) \
		--shifts 8 \
		--alpha
```

The actual Makefile will need refinement (the patsubst is rough), but the *idea* is: `.png` files → `.inc` files via the conversion script.

### 8.3 Assembly include

```asm
; In game-01-shadowkeep/unit-05/05-the-hooded-thief.asm

            include "sprites/hero_walk_down_0.inc"
            include "sprites/hero_walk_down_1.inc"
            ; ...
            include "sprites/hero_idle.inc"

hero_sprite_table:
            defw hero_walk_down_0_shift_0, hero_walk_down_0_shift_1
            ; ... etc.
```

`pasmonext` supports `include`.

---

## 9. Decisions to make during Phase 0

These are not in the spec because they require seeing the tool in action:

- **Convention: alpha-based or magenta-key?** Try Piskel exports; pick whichever round-trips cleanly. Default: alpha.
- **Decoration shifts: 1 (cell-aligned) or 8 (sub-cell)?** Default: 1 for known decorations; revisit if a designed sprite needs sub-cell positioning.
- **Where do pre-shifted tables physically live (memory address)?** Default: $5E00-$7BD0 in the overflow zone. Decide after measuring actual size.
- **Save-under buffer location and size.** Default: 1 KB at end of working RAM region. Decide based on memory budget update.

---

## 10. Validation gates

Before Unit 5 (the first user of the shifter) can publish:

- [ ] `convert_sprite.py` produces deterministic, byte-identical output across runs
- [ ] Round-trip self-check passes for at least one test sprite
- [ ] At least one sprite assembles via `pasmonext --sna` without errors
- [ ] At least one sprite renders correctly on Emu198x at shift 0
- [ ] All 8 shifts of one sprite render correctly (no off-by-one, no broken mask)
- [ ] Sprite drawn at every column 0-23 renders cleanly (no left-edge bleed, no right-edge bleed)
- [ ] Draw timing measured: ≤3,000 T-states per 16×16 sprite draw + save-under

Once these gates pass, the shifter is approved and Unit 5 art work can proceed.

---

## 11. Reference

- [shadowkeep-32-engineering-plan.md](shadowkeep-32-engineering-plan.md) — Section 5.2 (sprite shifter overview), Section 6 (asset pipeline)
- [shadowkeep-32-memory-budget.md](shadowkeep-32-memory-budget.md) — Section 3.2 (memory cost confirmed)
- [vault/hardware/ula.mdx](../vault/hardware/ula.mdx) — Spectrum bitmap addressing
- [vault/hardware/z80.mdx](../vault/hardware/z80.mdx) — instruction T-state costs

## Log

| Date | Event |
|---|---|
| 2026-05-18 | Spec written. Pending Phase 0 implementation. |
