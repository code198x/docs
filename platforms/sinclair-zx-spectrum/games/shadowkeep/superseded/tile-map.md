# Shadowkeep — Tile-Map and Collision Specification

> *"The tile-map carries the room's truth. The attribute area carries the room's mood. They are different data, in different places, with different jobs. Decoupling them is the design decision that lets the keep feel atmospheric and the hero walk through it correctly."*

**Anchored to:** [shadowkeep-32-engineering-plan.md](shadowkeep-32-engineering-plan.md) §5.4, [shadowkeep-32-memory-budget.md](shadowkeep-32-memory-budget.md) §3.5, §3.6.

**Implements:** Engine subsystem A4 (tile-map + decoupled collision). **Blocks:** Unit 13 (collision teaching), all of Arc 2 (which depends on stable collision semantics).

---

## 1. Purpose

In the existing 8-unit slice, the attribute byte at `$5800+row*32+col` carries both the *visual* (PAPER/INK/BRIGHT colour) and the *logical* (is this a WALL? a FLOOR? a GOLD?) information for each cell. This conflation has consequences:

- **Lighting can't differ from collision.** A WALL is `attr=$48` (PAPER 1, INK 0). To make a wall look "lit by torch" we'd need `attr=$46` (different colour), but that'd change its game-logical meaning.
- **Decoration must align with cells.** A pillar that's 16 wide and 24 tall must occupy whole cells with WALL attributes; can't have visual outline that crosses cell boundaries gracefully.
- **The thief moves cell-by-cell.** Pixel-level movement is impossible because the collision check expects cell-aligned positions.

The 32-unit engine **separates** these. The **tile-map** is a byte array indexed by `(row, col)` carrying *what's at that cell* (collision semantics). The **attribute area** ($5800-$5AFF) carries colour, set independently by the lighting pass. The pixel-level hero queries the tile-map for collision; the screen renderer uses the tile-map for *rendering*; lighting writes to the attribute area without touching tile-map.

---

## 2. Tile-map layout

### 2.1 Per-room data structure

Each room is 22 cells wide × 16 cells tall — the same dimensions the existing slice used. (Reserving rows 0-1 for HUD in Arc 2; rows 2-17 are the play area = 16 rows.)

```asm
; Per-room tile-map: 22 × 16 = 352 bytes
room_great_hall_tiles:
    defb T_WALL,  T_WALL,  T_WALL, ... (22 bytes of row 0)
    defb T_WALL,  T_FLOOR, T_FLOOR, ... (22 bytes of row 1)
    ; ... 14 more rows ...
    defb T_WALL,  T_WALL,  T_WALL, ... (22 bytes of row 15)
```

Each byte is a **tile ID** (see §3).

### 2.2 Memory cost

- Tile-map per room: **352 bytes**
- 3 rooms: **1,056 bytes**

Each room also has companion data:

- **Decoration list:** sequence of `(type, x_pixel, y_pixel)` entries, terminated by a sentinel. ~32-64 bytes per room.
- **Light source list:** sequence of `(x_cell, y_cell)` entries, terminated by sentinel. ~16 bytes per room.
- **Metadata:** name string (16 bytes), transitions table (8 bytes for the doors leading out), entry positions (4 bytes). ~32 bytes per room.

Per-room total: ~432 bytes. **3 rooms: ~1.3 KB** — matches §3.5 of the memory budget.

### 2.3 Source-of-truth vs. runtime mutation

Per the existing Unit 8 pattern: a *source* table baked into the SNA image, and a *runtime workspace* the game can mutate. `init_state` LDIRs source → workspace on each new playthrough.

```asm
; Source data (read-only, part of the SNA image)
room_great_hall_tiles_src:
    defb T_WALL, T_WALL, ...

; Workspace (RAM, mutated by gameplay — gold pickups change cells to T_FLOOR)
room_great_hall_tiles:
    defs 352
```

Same for decoration list (gold positions become "missing" after pickup, etc.).

---

## 3. Tile ID semantics

### 3.1 The ID-to-semantics table

Tile IDs are bytes 0-255, grouped by range:

| ID range | Category | Default collision | Default visual (Arc 1) |
|---|---|---|---|
| 0 | Empty | Passable (treated as floor) | No render — leaves screen black |
| 1-15 | Wall variations | Blocked | Render: corresponding wall tile |
| 16-31 | Floor variations | Passable | Render: corresponding floor tile |
| 32-47 | Decoration anchor cells | Blocked (mostly) | No render at this cell — decoration draws as a separate sprite-object |
| 48-55 | Gold cells | Passable + triggers pickup | Render: gold tile |
| 56-63 | Door cells | Passable + triggers transition | Render: door tile (or door-anim object) |
| 64-71 | Exit cell | Passable + triggers victory check | Render: exit tile |
| 72-127 | Reserved | — | — |
| 128-255 | Reserved | — | — |

### 3.2 Named constants

```asm
; Tile-ID constants (used in source data)
T_EMPTY         equ 0
T_WALL          equ 1   ; plain stone block
T_WALL_DECO     equ 2   ; decorated stone block (relief carving)
T_WALL_CORNER   equ 3   ; corner piece
T_WALL_ARCH     equ 4   ; archway lintel
; ... more wall variations ...
T_FLOOR         equ 16  ; plain floor
T_FLOOR_CRACKED equ 17  ; cracked floor variation
T_FLOOR_INSET   equ 18  ; floor with subtle inset detail
; ... more floor variations ...
T_PILLAR        equ 32  ; pillar (anchor; sprite-object draws over it)
T_ALTAR_NW      equ 33  ; altar's NW corner (multi-cell decoration)
T_ALTAR_NE      equ 34
T_ALTAR_SW      equ 35
T_ALTAR_SE      equ 36
T_SCONCE        equ 37  ; wall-mounted torch
T_GOLD          equ 48
T_DOOR_TO_ANTECHAMBER equ 56
T_DOOR_TO_GREAT_HALL  equ 57
T_DOOR_TO_CRYPT       equ 58
T_EXIT          equ 64
```

### 3.3 Collision query

```asm
; Input: A = tile ID
; Output: A = 0 if blocked, 1 if passable (carry flag set for passable)
is_tile_passable:
    ; Quick range-based dispatch
    cp 1
    jr c, .passable      ; T_EMPTY (0) is passable
    cp 16
    jr c, .blocked       ; 1-15 are walls
    cp 32
    jr c, .passable      ; 16-31 are floors
    cp 48
    jr c, .blocked       ; 32-47 are decoration anchors (mostly blocked)
    cp 72
    jr c, .passable      ; 48-71 are special-passable (gold, door, exit)
.blocked:
    xor a
    ret
.passable:
    ld a, 1
    scf
    ret
```

Or — even faster — a 256-byte lookup table:

```asm
; tile_passable[T] = 0 if blocked, 1 if passable
tile_passable:
    defb 1                ; T_EMPTY
    defb 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ; T_WALL...
    defb 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  ; floor variations
    defb 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ; decoration anchors
    defb 1, 1, 1, 1, 1, 1, 1, 1                          ; gold (passable)
    defb 1, 1, 1, 1, 1, 1, 1, 1                          ; doors (passable)
    defb 1, 1, 1, 1, 1, 1, 1, 1                          ; exit (passable)
    defs 184             ; rest = 0 (blocked by default)
```

256 bytes cost; ~15 T-states query. Worthwhile.

### 3.4 Trigger semantics

Some tiles trigger game logic when the hero enters:

| Tile ID range | Trigger |
|---|---|
| 48-55 (gold) | If `room_data[cell] != T_FLOOR` at time of step, increment `gold_taken`, mutate `room_data[cell] := T_FLOOR`, draw sparkle |
| 56-63 (door) | Trigger room transition; destination encoded in low bits or via door table |
| 64-71 (exit) | If `gold_taken == TOTAL_GOLD`, fire victory; else flash BORDER red |

The hero-update loop calls `tile_trigger_check(tile_id)` after a successful move; that routine dispatches by ID range.

---

## 4. Pixel-level collision query

The hero's collision check is the central operation.

### 4.1 Hero bounding box

A 16×16 hero sprite has a 16×16 bounding box. To check if the hero can be at pixel position (x, y):

1. Convert to tile coordinates: `tx = x / 8, ty = y / 8`
2. Check the cells the hero occupies:
   - **Top-left:** `(tx, ty)`
   - **Top-right:** `(tx + (15 if (x&7)==0 else 16) / 8, ty)` → simplified: `(tx + (1 if (x&7)==0 else 2), ty)`
   - Actually, since hero is 16 wide:
     - If x is cell-aligned (x % 8 == 0): hero occupies 2 cells horizontally
     - Else: hero occupies 3 cells horizontally (straddles 3 cells)
   - Same for y

3. For each cell the hero occupies, check `is_tile_passable(room_data[ty*22 + tx])`.
4. All must be passable; if any blocked, `can_move = false`.

### 4.2 Simplified check: 4 corners

A 16×16 sprite's 4 corners are at (x, y), (x+15, y), (x, y+15), (x+15, y+15). For a 16-wide hero this approximates the bounding-box check with 4 cell-lookups instead of 4-9.

Sprite occupies cells: `((x/8), (y/8))`, `((x+15)/8, (y/8))`, `((x/8), (y+15)/8)`, `((x+15)/8, (y+15)/8)`.

Note: if x is exactly cell-aligned and 15 = 7+8 puts the right edge at `((x+15)/8) = (x/8) + 1`, only 2 cells horizontally. Similarly for vertical. Worst-case 4 cells; best-case 2.

### 4.3 The query routine

```asm
; Input: D = target x_pixel, E = target y_pixel
; Output: A = 0 if blocked, 1 if passable (carry set for passable)
;
; Checks the four corners of the 16×16 sprite for collision.
can_move_to:
    ; Top-left corner
    ld a, d
    rrca
    rrca
    rrca                 ; A = x / 8
    and $1f              ; modulo 32 (rooms are 22 wide; A clamps to safe range)
    ld b, a              ; column
    
    ld a, e
    rrca
    rrca
    rrca
    and $1f              ; A = y / 8
    ld c, a              ; row
    
    ; Look up room_data[row][col]
    call get_tile_at_bc
    call is_tile_passable
    ret nc               ; blocked → return blocked
    
    ; Top-right corner
    ld a, d
    add a, 15
    rrca
    rrca
    rrca
    and $1f
    ld b, a              ; right column
    ; (row C unchanged for top-right)
    call get_tile_at_bc
    call is_tile_passable
    ret nc
    
    ; Bottom-left corner
    ld b, a              ; column for top-right preserved; need top-left's again
    ld a, d
    rrca
    rrca
    rrca
    and $1f
    ld b, a
    ld a, e
    add a, 15
    rrca
    rrca
    rrca
    and $1f
    ld c, a
    call get_tile_at_bc
    call is_tile_passable
    ret nc
    
    ; Bottom-right corner
    ld a, d
    add a, 15
    rrca
    rrca
    rrca
    and $1f
    ld b, a
    call get_tile_at_bc
    call is_tile_passable
    ret nc
    
    ; All four passable
    ld a, 1
    scf
    ret
```

**Cost:** 4 × (~30 T-states for cell lookup + ~15 T-states for passable check + ~20 T-states for boilerplate) = ~260 T-states. Cheap.

### 4.4 The fetch

```asm
; Input: B = column, C = row
; Output: A = tile ID at (col, row) in current room
get_tile_at_bc:
    ld a, c
    ld h, 0
    ld l, a
    add hl, hl           ; ×2
    add hl, hl           ; ×4
    add hl, hl           ; ×8
    add hl, hl           ; ×16
    ld a, l
    sla l                ; ×32 ... wait, this is wrong
    ; Actually: row × 22 needs multiplication
    ; Computed via add hl, hl + add hl, de loop or:
    ; row × 22 = row × 16 + row × 4 + row × 2 = row << 4 + row << 2 + row << 1
    ; Or use a precomputed row_start_table[16] = [0, 22, 44, ..., 330]
    ; The table approach is simpler:
    ld a, c
    add a, a
    ld c, a
    ld b, 0
    ld hl, row_start_table_room
    add hl, bc
    ld c, (hl)
    inc hl
    ld b, (hl)
    ; BC now = row offset in current room's tile-map
    
    ld a, b              ; ... actually want column too; restore from earlier
    ; ... (this is getting complex; see implementation note below)
    ret

row_start_table:
    defw 0, 22, 44, 66, 88, 110, 132, 154
    defw 176, 198, 220, 242, 264, 286, 308, 330
```

**Implementation note:** the row × 22 multiply is the awkward bit. A pre-computed `row_start_table[16]` (32 bytes) eliminates the multiply. The fetch becomes: read `row_start_table[row]` → add column → that's the offset into `current_room_tiles`. ~25 T-states.

---

## 5. Current-room indirection

The game can be in any of three rooms. The collision query needs to find the *current* room's tile-map.

```asm
; The current room's tile-map address — updated on each transition
current_room_tiles:
    defw room_great_hall_tiles   ; initial value
```

When entering a new room:

```asm
load_room:
    ; A = room ID (0 = great hall, 1 = antechamber, 2 = crypt)
    ld hl, room_tiles_table
    sla a                ; ×2 for 16-bit entries
    ld c, a
    ld b, 0
    add hl, bc
    ld c, (hl)
    inc hl
    ld b, (hl)
    ld (current_room_tiles), bc   ; update the indirection
    
    ; Also: LDIR source → workspace if mutable mode
    ; (See "Source vs workspace" in §2.3)
    
    ret

room_tiles_table:
    defw room_great_hall_tiles
    defw room_antechamber_tiles
    defw room_crypt_tiles
```

`get_tile_at_bc` reads `current_room_tiles` and uses that as the base address. One extra indirection, negligible cost.

---

## 6. Renderer reads tile-map

The room renderer iterates over the tile-map, drawing each cell. Pseudo-code:

```asm
; Render the current room
draw_current_room:
    ld hl, (current_room_tiles)
    ld b, 16             ; rows
    ld de, $4000 + (2 * $20)  ; start row 2 (after HUD); first row's screen address
.row:
    push bc
    ld c, 22             ; cols
.col:
    ld a, (hl)           ; tile ID
    call get_tile_sprite_addr  ; returns DE_sprite from tile lookup
    push hl
    push de              ; save screen pos
    ; ... draw 8-byte tile to screen ...
    pop de
    pop hl
    inc hl               ; next tile
    inc de               ; next column on screen
    dec c
    jr nz, .col
    ; Advance to next row on screen
    ; ... screen address increment ...
    pop bc
    djnz .row
    ret
```

The renderer **doesn't write to attribute area** — that's the lighting pass's job (§7).

---

## 7. Lighting pass

After loading the tile-map (and rendering it to bitmap), the lighting pass writes the attribute area.

### 7.1 Algorithm

```
for each cell (row, col) in the room:
    distance = min over (light_row, light_col) of |row - light_row| + |col - light_col|
    attribute = palette_by_distance[distance]
    write to $5800 + row*32 + col
```

Manhattan distance is a reasonable approximation. Two passes of horizontal/vertical sweep can compute it efficiently in O(N) where N = cells.

### 7.2 Light source list per room

Per room:

```asm
room_great_hall_lights:
    defb 4, 5             ; light at (col=4, row=5)
    defb 18, 5            ; light at (col=18, row=5)
    defb 11, 13           ; central altar's glow
    defb $FF              ; end marker

room_antechamber_lights:
    defb 1, 8             ; sconce on the west wall
    defb 21, 8            ; sconce on the east wall
    defb $FF
```

### 7.3 Palette

```asm
; Maps distance (0-N) to attribute byte
palette_by_distance:
    defb $46              ; distance 0-1: BRIGHT 1, PAPER 0, INK 6 (warm yellow glow)
    defb $46              ; distance 2-3: same
    defb $06              ; distance 4-5: normal yellow
    defb $07              ; distance 6+: cold white (distant from light)
    defb $07
    defb $07
    defb $07
    defb $07              ; max distance cap
```

8 distance bands, 1 byte each = 8-byte palette table.

### 7.4 Cost

Manhattan-distance flood is O(rows × cols × light_sources) worst case = 352 × 8 = 2,816 operations. Each op ~10 T-states = ~28,000 T-states. Runs **once per room load** — not per frame.

For Arc 1 Unit 11 (lighting introduction), this approach is correct. If we ever need real-time lighting (light source moves), we'd rework. Currently lights are static.

---

## 8. Attribute area independence

Once lighting writes the attribute area:

- **Renderer doesn't touch it.** Stays whatever lighting set.
- **Hero drawing doesn't touch it.** Hero's pixels appear in whatever attribute is at his current cell. (For Arc 1, hero attribute might be uniformly forced to a "hero attribute" — but a more atmospheric approach is to let the hero pick up the local lighting, so a hero in a torch-lit area glows.)
- **Decoration drawing doesn't touch it.** Same logic.

**The attribute area is owned by the lighting pass alone**. This is the central decoupling.

---

## 9. Room data file format (source-of-truth)

Each room's source data is a structured byte sequence:

```asm
; Room data record
;
; Bytes 0-1:      Pointer to tile-map source data (352 bytes)
; Bytes 2-3:      Pointer to decoration list
; Bytes 4-5:      Pointer to light source list
; Bytes 6:        Room name length
; Bytes 7-N:      Room name bytes (ASCII)
; Bytes N+1:      Number of transitions
; Bytes N+2-M:    Transitions list (each: door_tile_id, dest_room_id, hero_entry_x, hero_entry_y)
;
; Total: ~40 bytes record overhead + 352 bytes tile-map = ~392 bytes per room

room_great_hall:
    defw room_great_hall_tiles_src
    defw room_great_hall_decoration
    defw room_great_hall_lights
    defb 14                                       ; name length
    defm "THE GREAT HALL"
    defb 1                                        ; 1 transition
    defb T_DOOR_TO_ANTECHAMBER, 1, 6, 10          ; door → room 1, hero at (6,10)
```

This format is human-editable in the .asm source. Each room takes ~40 bytes of structural data plus the 352-byte tile-map plus decoration/lights lists.

---

## 10. Validation gates

Before Unit 13 (the collision teaching) can publish:

- [ ] Tile-ID semantics table approved and stable
- [ ] `is_tile_passable` query passes unit tests for each tile-ID range
- [ ] `can_move_to(x, y)` passes for hero at various sub-cell positions
- [ ] Hero is blocked at wall boundaries even when sub-cell-positioned
- [ ] Hero is passable through gaps as narrow as 16 pixels (2 cells wide)
- [ ] Gold pickup mutates `room_data[cell]` to T_FLOOR; visible change persists
- [ ] Door tiles trigger room transitions correctly
- [ ] Exit tile triggers victory only when `gold_taken == TOTAL_GOLD`
- [ ] Multi-room state persists correctly across transitions (gold collected in great hall doesn't reset on return)
- [ ] `init_state` correctly restores all rooms' tile-maps on new playthrough

---

## 11. Decisions to make during Phase 0

- **Precise tile-ID assignments.** §3.2 has a draft; final IDs settle when art is done and the variations are countable.
- **Lighting palette.** §7.3 has a draft; final palette set when designer decisions arrive in Unit 11.
- **Room data format details.** §9's format is reasonable; may shift slightly based on what makes editing easier.
- **Whether to store decoration list as flat array or sentinel-terminated.** Default: sentinel-terminated (simpler iteration). Revisit if memory matters.
- **Whether passable-tile lookup uses range-dispatch (§3.3 first version) or table-lookup (§3.3 second version).** Default: table-lookup (faster, +256 bytes RAM cost). Confirmed in memory budget.

---

## 12. The big picture

The collision system, the renderer, and the lighting pass *all read the same tile-map data* but interpret it differently:

```
                         ┌─── COLLISION reads tile ID → query passable?
                         │
ROOM_DATA (tile bytes) ──┼─── RENDERER reads tile ID → draw the tile bitmap
                         │
                         └─── LIGHTING ignores tile (reads light_sources separately)
                              writes to attribute area independently

ATTRIBUTE AREA ──────── owned exclusively by lighting pass
```

This is the architecture. The existing 8-unit slice didn't have this separation; the new 32-unit engine does. Every Arc 2 unit depends on it.

---

## 13. Reference

- [shadowkeep-32-engineering-plan.md](shadowkeep-32-engineering-plan.md) — Section 5.4 (overview)
- [shadowkeep-32-memory-budget.md](shadowkeep-32-memory-budget.md) — Section 3.5 (room data sizing)
- [shadowkeep-32-object-system.md](shadowkeep-32-object-system.md) — Section 8 (room load uses tile-map + decoration list)
- [shadowkeep-32-sprite-shifter.md](shadowkeep-32-sprite-shifter.md) — Section 1 (sprites drawn over tile renders)

## Log

| Date | Event |
|---|---|
| 2026-05-18 | Spec written. Implementation in Phase 0 / Unit 13. |
