# Shadowkeep — Y-Sort Object System Specification

> *"An object list with depth. The hero walks behind the pillar, then in front of it, because the list is drawn back-to-front each frame. The thing that makes the keep three-dimensional in a two-dimensional renderer."*

**Anchored to:** [shadowkeep-32-engineering-plan.md](shadowkeep-32-engineering-plan.md) §5.3, [shadowkeep-32-memory-budget.md](shadowkeep-32-memory-budget.md) §3.6, [shadowkeep-32-sprite-shifter.md](shadowkeep-32-sprite-shifter.md).

**Implements:** Engine subsystem A3 (object list + Y-sort + dispatched draw). **Blocks:** Units 9 (introduction), 10-14 (consumers), all of Arc 2.

---

## 1. Purpose

Render a screen of multiple sprites at proper depth — pillars block the hero when the hero is behind them; the hero blocks pillars when in front. Without Y-sort, the renderer draws in a fixed order and depth is wrong half the time.

The model:

- **Each frame:** clear last frame's sprites; for each object in Y-sorted order (smallest Y first), draw it; the result is back-to-front (objects with smaller Y appear behind, larger Y in front).
- **Hero is just another object.** No special "draw hero on top" code path. The Y-sort puts the hero in the right place automatically.

This is the [Atic Atac](/vault/games/atic-atac) approach. The Spectrum's flat 2D bitmap gets perceived depth through draw order.

---

## 2. Data structures

### 2.1 Object struct

Each object occupies 16 bytes in RAM:

```asm
; Object struct (16 bytes)
;
; Offset Field                  Purpose
; -----  ---------------------  -------------------------------------------
; 0      x_pixel                Left edge of sprite, screen-pixel column (0-255)
; 1      y_pixel                Top edge of sprite, screen-pixel row (0-191)
; 2      sprite_type            HERO, NPC_SPECTRE, PILLAR, ALTAR, etc.
; 3      frame                  Current animation frame within type
; 4      anim_timer             Ticks until next frame (0 = advance now)
; 5      state                  Type-specific state byte
;                               (NPC: patrol direction; gold: sparkle stage; etc.)
; 6      vel_x                  Pixels/frame velocity (signed)
; 7      vel_y                  Pixels/frame velocity (signed)
; 8-9    save_under_addr        Pointer to save-under bitmap buffer slot (or 0)
; 10     flags                  Bit flags (see below)
; 11     reserved
; 12-15  type-specific data     (e.g., patrol bounds for NPC, sparkle counter for gold)
```

**Flags byte (offset 10):**

```
bit 0   ACTIVE       1 = slot in use; 0 = empty slot
bit 1   VISIBLE      1 = draw it; 0 = skip drawing (off-screen, etc.)
bit 2   MOVING       1 = save-under needed; 0 = static, no save-under
bit 3   MASKED       1 = masked sprite (use mask data); 0 = opaque sprite (faster)
bit 4   ANIMATING    1 = frame may advance based on anim_timer
bit 5   COLLIDES     1 = participates in collision (hero, NPC); 0 = decoration only
bit 6-7 reserved
```

### 2.2 Object array

```asm
; 16 object slots × 16 bytes = 256 bytes
object_array:
    defs 16 * 16
```

Slot 0 is conventionally the hero (special-cased in input handling but otherwise just another object).

### 2.3 Sort index

Per frame, after sort: an array of slot indices in Y order.

```asm
; 16 bytes — slot indices, sorted ascending by y_pixel
sort_indices:
    defs 16
```

Drawing iterates `sort_indices[0]` through `sort_indices[15]`, skipping any with !ACTIVE or !VISIBLE.

### 2.4 Sprite type dispatch table

```asm
; For each sprite_type, two entries:
;   - draw_fn:   address of draw routine
;   - sprite_table: address of the sprite-data lookup (frame × shift)
sprite_type_table:
    defw draw_hero,         hero_sprite_table       ; 0 = HERO
    defw draw_npc_spectre,  npc_spectre_sprite_table; 1 = NPC_SPECTRE
    defw draw_npc_guard,    npc_guard_sprite_table  ; 2 = NPC_GUARD (if used)
    defw draw_pillar,       pillar_sprite_data      ; 3 = PILLAR
    defw draw_altar,        altar_sprite_data       ; 4 = ALTAR
    defw draw_sconce,       sconce_sprite_data      ; 5 = SCONCE
    defw draw_gold,         gold_sprite_data        ; 6 = GOLD
    defw draw_door,         door_sprite_data        ; 7 = DOOR
    ; ... up to ~16 types
```

Each draw routine takes the object's data in agreed registers (e.g., `IX = object pointer`, `HL = sprite_table`).

---

## 3. Object lifecycle

### 3.1 Add

```asm
; Inputs: A = sprite_type, B = x_pixel, C = y_pixel
; Output: HL = pointer to allocated object, or 0 if no free slot
object_add:
    ld hl, object_array
    ld de, 16            ; slot size
    ld ixh, 16           ; max slots
.scan:
    bit 0, (hl+10)       ; check ACTIVE flag (pseudo-code; actual: ld a,(hl); add a,10; bit...)
    jr z, .found
    add hl, de
    dec ixh
    jr nz, .scan
    ; No free slot
    ld hl, 0
    ret
.found:
    ; Initialise slot
    ld (hl), b           ; x_pixel
    inc hl
    ld (hl), c           ; y_pixel
    inc hl
    ld (hl), a           ; sprite_type
    ; ... zero out rest, set flags ...
    ret
```

Cost: ~100 T-states average, ~300 worst-case (last slot in array).

### 3.2 Remove

```asm
; Input: HL = pointer to object's flags byte (offset 10 in the struct)
object_remove:
    res 0, (hl)          ; clear ACTIVE
    ret
```

Trivial. Slot becomes available for the next `object_add`.

### 3.3 Update (per-frame)

For each active, animating object:

```asm
object_update_all:
    ld ix, object_array
    ld b, 16
.loop:
    bit 0, (ix+10)       ; ACTIVE?
    jr z, .next
    
    bit 4, (ix+10)       ; ANIMATING?
    jr z, .move_only
    
    ; Decrement anim_timer; if zero, advance frame
    dec (ix+4)
    jr nz, .move_only
    inc (ix+3)           ; next frame
    ld a, (ix+3)
    ; ... clamp to type's frame count (type-dispatched) ...
    ld (ix+4), default_anim_speed
    
.move_only:
    ; Apply velocity
    ld a, (ix+0)
    add a, (ix+6)        ; x_pixel += vel_x
    ld (ix+0), a
    ld a, (ix+1)
    add a, (ix+7)        ; y_pixel += vel_y
    ld (ix+1), a
    
.next:
    ld de, 16
    add ix, de
    djnz .loop
    ret
```

Cost: ~80 T-states per inactive slot, ~200 per active. 16 slots = ~3,000 T-states worst case.

### 3.4 Hero / NPC AI integration

Hero and NPC update is *outside* the generic per-object update. Each frame:

1. `hero_update()` — reads input, sets hero velocity, handles transitions.
2. `npc_update_all()` — each NPC's patrol AI updates velocity.
3. `object_update_all()` — generic update applies velocities and advances animations.
4. `collision_check()` — hero-vs-NPC, hero-vs-pickup.
5. `sort_objects()` — Y-sort.
6. `draw_objects()` — back-to-front draw.

---

## 4. The sort

### 4.1 Algorithm: insertion sort on indices

Insertion sort is O(n²) but with n=16 the constants are small, and the input is *almost-sorted each frame* (objects rarely change Y dramatically), so the amortised cost is near O(n).

```asm
; Inputs: object_array filled, sort_indices initialised to [0,1,2,...,15]
; Outputs: sort_indices reordered such that 
;          object_array[sort_indices[i]].y_pixel <= object_array[sort_indices[i+1]].y_pixel
;          for all i
sort_objects:
    ld b, 15             ; outer loop: i = 1 to 15
    ld c, 1              ; i
.outer:
    ; Read sort_indices[c] into D
    ld hl, sort_indices
    ld e, c
    ld d, 0
    add hl, de
    ld d, (hl)           ; D = sort_indices[c] (the index of object to insert)
    
    ; Get this object's Y
    push hl
    ld hl, object_array + 1   ; +1 to point at y_pixel
    ld e, d
    add hl, de
    ld e, d
    sla e
    sla e
    sla e
    sla e
    ld d, 0
    add hl, de           ; HL = object[D].y_pixel
    ld a, (hl)           ; A = key Y
    pop hl
    
    ; Insertion: shift right until we find position
    ld e, c
    dec e                ; j = c - 1
.inner:
    ; Compare A with object[sort_indices[j]].y_pixel
    ; If A < that, shift; else stop
    ; ... details elided ...
    
    dec e
    jp p, .inner         ; loop while j >= 0
    
.found_position:
    ; Insert D at position e+1
    ; ... shift logic ...
    
    inc c
    dec b
    jr nz, .outer
    ret
```

**Cost in practice:** for almost-sorted input (typical), inner loop runs ~1-2 iterations per outer = ~30 inner total. Each inner iteration ~30 T-states. Sort total: **~1,000 T-states.**

For worst case (reverse-sorted input): inner loop runs ~120 iterations × 30 T-states = ~3,600 T-states. Still acceptable.

### 4.2 Skip empty slots

Empty slots have `y_pixel = ?` (uninitialised) which would break sort. Solution: set `y_pixel = 255` for empty slots; they sort to the end and are skipped in draw (via ACTIVE flag check).

Alternative: maintain a separate "live count" and only sort the first N indices.

Default: set `y_pixel = 255` for empty slots. Simpler.

---

## 5. The draw

```asm
draw_objects:
    ld ix, sort_indices
    ld b, 16
.loop:
    ld a, (ix+0)         ; slot index
    inc ix
    
    ; Look up the object
    push ix
    ld ixh, 0
    ld ixl, a
    add ix, ix           ; ×2
    add ix, ix           ; ×4
    add ix, ix           ; ×8
    add ix, ix           ; ×16 (16 bytes per object)
    ld bc, object_array
    add ix, bc           ; IX = &object[slot]
    
    bit 0, (ix+10)       ; ACTIVE?
    jr z, .next
    bit 1, (ix+10)       ; VISIBLE?
    jr z, .next
    
    ; Dispatch to type-specific draw
    ld a, (ix+2)         ; sprite_type
    sla a
    sla a                ; × 4 (each table entry is 4 bytes)
    ld c, a
    ld b, 0
    ld hl, sprite_type_table
    add hl, bc
    
    ld e, (hl)           ; draw_fn low
    inc hl
    ld d, (hl)           ; draw_fn high
    inc hl
    
    push hl              ; save table position
    ld hl, draw_objects_resume
    push hl              ; return address
    push de              ; draw_fn address
    ret                  ; jump to draw_fn (with HL = sprite_table from next entry)
    
draw_objects_resume:
    pop hl               ; restore table position
    
.next:
    pop ix
    djnz .loop
    ret
```

**Per-object draw cost** (using hero draw from sprite-shifter spec): ~2,600 T-states + ~100 T-states dispatch + ~50 T-states sort-list traversal = **~2,750 T-states per visible object.**

With save-under: +1,800 T-states = **~4,550 T-states per visible moving object.**

For a typical 8-object scene (hero + 1 NPC + 6 decorations): ~25,000 T-states = 36% of frame. Within budget.

---

## 6. Object types and their behaviours

Defined types and their dispatch entries:

| Type | Frames | Animating | Saves under | Moves | Notes |
|---|---|---|---|---|---|
| HERO | 5 (4 walk + idle) | Yes | Yes | Yes | Index 0 always; input-driven |
| NPC_SPECTRE | 4 (walk cycle) | Yes | Yes | Yes | Patrol AI |
| NPC_GUARD | 4 (walk cycle) | Yes | Yes | Yes | Different patrol (if Unit 24 uses new sprite) |
| PILLAR | 1 | No | No | No | Static; save once at room load |
| ALTAR | 1 | No | No | No | Static |
| SCONCE | 1 (or 2 for flicker) | Optional | No | No | Light source position; flicker is cosmetic |
| GOLD_IDLE | 1 | No | No | No | Static until picked up |
| GOLD_SPARKLE | 3 (sparkle frames) | Yes | Yes | No | Brief animation on pickup, then removed |
| DOOR_CLOSED | 1 | No | No | No | Initial state |
| DOOR_OPENING | 4 (anim) | Yes | Yes | No | Triggered by transition |
| DOOR_OPEN | 1 | No | No | No | Steady state after opening |
| EXIT | 1 | Optional pulse | No | No | Static; pulse via attribute, not bitmap |

---

## 7. Hero special-casing

The hero is index 0 by convention. Some things are easier when you can assume "slot 0 is the hero":

- **Input updates hero directly:** `hero_x = object_array[0].x_pixel`
- **Collision queries the hero specifically:** `gold-vs-hero` uses slot 0's bounding box
- **Transition logic respawns hero:** sets slot 0's position

But the hero is otherwise a regular object — its Y position participates in sort, its draw uses the dispatch table, etc.

---

## 8. Room load: object population

When a room loads:

1. Clear all objects (`object_array[*].flags &= ~ACTIVE`)
2. Restore hero (slot 0) with current position
3. Read room's decoration list — for each (type, x, y) entry, `object_add(type, x, y)`
4. Read room's NPC list — same
5. Read room's gold list — same (those not already collected)
6. Save-under for static (non-moving) decorations — save once
7. Initial sort + draw

The room's decoration list lives in room data (see [tile-map spec](shadowkeep-32-tile-map.md)).

---

## 9. Performance summary

| Operation | Cost (T-states) | Per frame |
|---|---|---|
| Object update (all 16 slots) | ~3,000 | once |
| Sort (almost-sorted input) | ~1,000 | once |
| Draw + save-under (per moving object) | ~4,500 | × moving count |
| Draw (per static visible object) | ~2,750 | × static visible (once per redraw) |
| Dispatch overhead | ~150 per object | × 16 worst case |

Typical frame with 8 visible (hero + NPC + 6 decorations): ~25,000 T-states = **~36% of frame**.

Worst case with 16 visible: ~55,000 T-states = **~80% of frame**. Music + AI + input must fit in remaining 20%. Tight; designs should avoid this case (decorations don't usually exceed 6).

---

## 10. Static vs moving optimisation

**Decorations are mostly static.** Pillars, altars, sconces don't move and don't animate (except a possible flicker). For these:

- Save-under once at room load (~2,000 T-states one-time cost)
- Draw once at room load
- Skip them in per-frame draw (set `VISIBLE = 0` until something requires redraw)

The only case requiring decoration redraw is when the hero passes in front of one — but layered rendering handles this automatically because the hero draws over the decoration.

**The flip side:** when the hero moves out of "in front of" a decoration, the cell underneath needs the decoration restored. This is exactly what save-under is for. The hero's restore-under (called before next draw) puts back whatever pixels were there — which for a decoration cell is the decoration.

So static decorations don't need active management. The hero's save-under-restore handles overlap correctly.

---

## 11. Validation gates

Before Unit 9 (the object-system introduction) can publish:

- [ ] Object struct fits in 16 bytes; all 16 slots in 256 bytes
- [ ] `object_add` and `object_remove` work with isolated unit tests
- [ ] `object_update_all` advances animation timers correctly
- [ ] Insertion sort produces Y-sorted index list
- [ ] Sort handles edge cases: all same Y (stable), one slot occupied, full 16, empty slots
- [ ] Draw correctly dispatches to type-specific draw routine
- [ ] Hero (slot 0) renders in correct Y position relative to pillars
- [ ] Hero passes behind pillar when Y < pillar.Y; in front when Y > pillar.Y
- [ ] Worst-case frame (8 objects, all moving) completes within frame budget

---

## 12. Decisions to make during Phase 0

- **Sort algorithm precise implementation.** Insertion sort spec'd; may swap for shell sort if profiling shows benefit.
- **Object struct layout precise.** Field offsets may shift after first implementation; adjust spec to match.
- **Save-under buffer allocation strategy.** Per-object (1 KB) vs shared pool (smaller). Decide after measuring how many moving objects there actually are.
- **Frame budget review.** Re-measure once draw routines are real; spec budgets are estimates.

---

## 13. Reference

- [shadowkeep-32-engineering-plan.md](shadowkeep-32-engineering-plan.md) — Section 5.3 (Y-sort overview)
- [shadowkeep-32-memory-budget.md](shadowkeep-32-memory-budget.md) — Section 3.6 (working RAM allocation)
- [shadowkeep-32-sprite-shifter.md](shadowkeep-32-sprite-shifter.md) — Section 5 (draw primitive)
- [vault/games/atic-atac.mdx](../vault/games/atic-atac.mdx) — the engine archetype this implements

## Log

| Date | Event |
|---|---|
| 2026-05-18 | Spec written. Implementation in Phase 0 / Unit 9. |
