# Full Game Outline: ZX Spectrum Ionfire (256 Units)

**Game:** Ionfire (Game 2)
**Units:** 256 (8 phases × 32 units)
**Genre:** Horizontal scrolling shoot 'em up
**Inspired by:** R-Type, Zynaps, Nemesis, Cybernoid
**Target Quality:** Commercial-grade scrolling shooter (1987–89 era)

---

## Premise

The ion storms have breached the orbital defences. Your ship — a salvaged interceptor with an experimental ion cannon — is the last thing between the swarm and the colonies. Five sectors of alien-infested space, each ending in a massive bio-mechanical guardian. The ship scrolls through landscapes that have no right to exist on a Spectrum: smooth pixel scrolling through caverns, asteroid fields, and organic hives.

Software pixel scrolling on hardware with no scroll registers. This is the Spectrum's crowning technical achievement — and the reason this game is Game 2.

---

## Why Software Scrolling Matters

The Spectrum has no hardware scroll registers. No BPLCON1. No PPUSCROLL. No $D016. The screen doesn't move unless the code moves every byte of screen memory manually.

A single-pixel horizontal scroll on the Spectrum requires:
1. Shift every byte in the bitmap area (6,144 bytes) right by one bit
2. Load the new column of pixel data at the left edge
3. Scroll the attribute area (768 bytes) when a full 8-pixel shift completes
4. Do all of this within a single frame (~69,888 T-states on 48K) while the ULA fights for bus access

R-Type on the Spectrum was a technical miracle. Zynaps proved it was repeatable. This game teaches how they did it — and the learner builds it from scratch.

---

## Design Philosophy

- **Scrolling from Phase 1** — the signature technique is introduced immediately, not saved for late
- **Character-cell scrolling first** — shift the screen by 8 pixels (one character) as the entry point
- **Pixel scrolling in Phase 2** — the hard version: shift by 1 pixel, smooth and continuous
- **Contended memory is the enemy** — the ULA steals CPU cycles during display; this shapes every design decision
- **Gameplay despite the technique** — scrolling is the enabler, not the game. Enemies, weapons, bosses make it worth playing
- **48K first, 128K enhanced** — core game in 48K; 128K adds AY music, more levels, double-buffered scroll
- **256 units for depth** — scrolling alone would fill 128 units; adding a complete shooter on top demands 256

---

## Z80 Progression

| Phase | Z80 Focus |
|-------|-----------|
| 1 (Approach) | Attribute scrolling, screen memory layout review, timing awareness |
| 2 (Breach) | Bit shifts (SLA/SRL/RR/RL), carry flag chaining, pixel-level operations |
| 3 (Swarm) | Sprite rendering (XOR/OR to screen), clipping, restore-under |
| 4 (Arsenal) | Lookup tables, sine tables, fixed-point arithmetic for movement |
| 5 (Sectors) | Level streaming, column-based tile maps, memory management |
| 6 (Resonance) | AY register programming, interrupt-driven music, SFX mixing |
| 7 (Guardians) | State machines, multi-part sprites, pattern scripting |
| 8 (Aftermath) | Double buffering (128K), contention-aware scheduling, optimisation |

---

## Phase 1: Approach (Units 1–32)

**Goal:** Character-cell scrolling with a moving ship. The screen shifts by 8 pixels per frame.
**Z80 Focus:** LDIR/LDDR for screen shifting, attribute management, contended memory.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 1 | Recap: screen memory | Address calculation, attribute layout (from Gravelight) | Foundation confirmed |
| 2 | A static background | Fill screen with terrain pattern using attribute colours | Space to scroll |
| 3 | Shift attributes left by one cell | `LDIR` to copy 31 bytes over 32, new column at right | **Attributes scroll** |
| 4 | Shift bitmap left by one cell | `LDIR` per pixel row (192 rows × 31 bytes) | **Bitmap scrolls** |
| 5 | Combined scroll | Attributes + bitmap scroll together. Screen shifts left by 8 pixels. | Character-cell scrolling |
| 6 | New column data | Right edge receives new tile data (from a tile map in memory) | Content feeds in |
| 7 | Tile map | Array of column data: each column is 24 tile codes. Map is wider than the screen. | Level data structure |
| 8 | Tile rendering | Tile code → 8 bytes of bitmap + 1 attribute byte. Drawn at the right edge. | Tile lookup and draw |
| 9 | Scroll speed | Scroll one character cell per N frames (adjustable). Slower = easier to play. | Speed control |
| 10 | Contended memory timing | Measure: how long does the scroll take? $4000-$7FFF costs ~1.5× normal. | **Understanding contention** |
| 11 | Scroll outside display | Time the scroll during the vertical blank (border area). Less contention. | VBlank-aware scheduling |
| 12 | Player ship | A character (UDG or ROM) placed on screen. Joystick moves it. | Player control |
| 13 | Ship over scrolling background | Ship moves independently of the scroll. Erase old position, draw new. | Sprite on scrolling bg |
| 14 | Ship-terrain collision | Check attribute at ship position. Wall colour = death. | Terrain avoidance |
| 15 | Terrain variety | Cavern: floor and ceiling close in, openings to fly through. | Level design |
| 16 | First playable scroll | Ship flies through scrolling cavern. Dodge terrain. Character-cell scroll. | **Milestone: it scrolls** |
| 17 | Static enemies | Enemies placed in the tile map. Scroll into view on the right. | Enemies appear |
| 18 | Enemy collision | Ship touches enemy = death. Attribute check or position check. | Contact damage |
| 19 | Bullet | Fire button: bullet character moves right. Off-screen → deactivate. | Shooting |
| 20 | Bullet-enemy collision | Bullet reaches enemy position → enemy destroyed, score. | Kills |
| 21 | Explosion effect | Enemy replaced with explosion character for N frames, then cleared. | Destruction feedback |
| 22 | Score display | Score in a status bar (top or bottom row, outside scroll area). | HUD |
| 23 | Lives | 3 lives, death animation (ship flash), respawn. | Stakes |
| 24 | Multiple enemy types | Different characters, different point values. Placed via tile map. | Variety |
| 25 | Wave patterns | Enemies that move after scrolling into view (horizontal, vertical, diagonal). | Active enemies |
| 26 | Enemy bullet | Some enemies fire left. Player must dodge. | Bidirectional threats |
| 27 | Power-ups | Dropped by specific enemies: speed, weapon, shield. | Upgrades |
| 28 | End of level | After N columns scrolled: scrolling stops, boss area begins. | Level structure |
| 29 | Boss (character-cell) | A large enemy (4×4 characters) with a health bar. Fires patterns. | First boss |
| 30 | Boss defeat | Health depleted → explosion sequence → "SECTOR 1 CLEAR". | Victory |
| 31 | Sector 1 complete | Full character-cell scrolling level with enemies, boss, and scoring. | Playable sector |
| 32 | Performance audit | Time the full game loop. Where are the bottlenecks? What needs to be faster for pixel scrolling? | Ready for Phase 2 |

**End of Phase 1:** A complete scrolling shooter using character-cell scrolling (8 pixels per shift). One sector with enemies and a boss. It works, it plays, it looks decent — but the scroll is visibly chunky. Phase 2 fixes that.

---

## Phase 2: Breach (Units 33–64)

**Goal:** Smooth pixel scrolling — shift by 1 pixel per frame instead of 8.
**Z80 Focus:** Bit shift instructions, carry flag chaining, pixel-level scroll.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 33 | The bit shift | `SRL (HL)`: shift one byte right by one bit. The rightmost bit falls into the carry flag. | Fundamental operation |
| 34 | Chained shift | `RR (HL)` on the next byte: carry flag feeds in from the left. Two bytes shift as one 16-bit value. | Carry chaining |
| 35 | Shift one row | Loop across 32 bytes of one pixel row. Each byte's carry feeds the next. One row shifts 1 pixel right. | Full row shift |
| 36 | Shift all rows | 192 pixel rows shifted. The entire bitmap moves 1 pixel. Slow but correct. | Full screen pixel shift |
| 37 | Timing: the problem | 192 rows × 32 bytes × ~8 T-states = ~49,000 T-states minimum. Plus contention. It's too slow for one frame. | Understanding the cost |
| 38 | Partial screen scroll | Only scroll the play area (rows 8-184, 22 character rows). Status bar stays fixed. | Reduced workload |
| 39 | Unrolled loops | Replace DJNZ loops with sequential shift instructions. Faster: no loop overhead. | Loop unrolling |
| 40 | Screen thirds | Process one third at a time, interleaved with other work. | Workload distribution |
| 41 | Fine scroll + coarse scroll | Count pixel shifts. After 8 pixel shifts, do a character-cell scroll instead. Reset pixel counter. | Hybrid approach |
| 42 | The fine/coarse technique | Fine scroll: shift 7 times (1-7 pixels). Coarse scroll: LDIR one character cell, reset to 0. Smooth and efficient. | **The commercial technique** |
| 43 | New pixel column | After coarse scroll, draw new tile at right edge. During fine scroll, the edge tile is partially visible. | Tile streaming |
| 44 | Attribute scroll sync | Attributes only shift on coarse scroll (every 8 frames). Fine scroll doesn't affect attributes. | Sync management |
| 45 | Smooth scroll working | The screen scrolls smoothly at 1 pixel per frame. The cavern flows past. | **Pixel scrolling achieved** |
| 46 | Player on pixel scroll | Ship movement unchanged — still character-cell aligned (or pixel-aligned if ambitious). | Player over smooth bg |
| 47 | Enemies on pixel scroll | Enemies scroll with the background (world-space position minus scroll offset). | World-relative enemies |
| 48 | Scroll speed variation | Variable scroll speed: slow for caverns, faster for open space. | Pacing |
| 49 | Terrain from tile map | Pixel-scrolled terrain fed from the same tile map as Phase 1. | Data reuse |
| 50 | Parallax (simple) | Attribute colour changes suggest depth: distant stars (dim) shift every 2 frames while foreground shifts every frame. | Cheap parallax |
| 51 | Ship pixel movement | Ship moves at pixel precision (not character-cell). UDG drawn at pixel position. | Sub-cell player movement |
| 52 | Pixel collision | Check bitmap pixels at ship position, not just attributes. More precise. | Pixel-level collision |
| 53 | Restore-under for ship | Save screen data before drawing ship; restore it before redrawing. No ghost trails. | Save/restore buffer |
| 54 | Multiple sprites | Ship + bullet + enemies all using restore-under. Ordering matters. | Sprite compositing |
| 55 | Sprite clipping | Sprites near screen edges need partial drawing. Don't write outside screen RAM. | Edge clipping |
| 56 | Sector 2 terrain | New tile set: asteroid field. Open spaces, floating rocks, narrow gaps. | Visual variety |
| 57 | Sector 2 enemies | New enemy types for the asteroid field. Faster, different patterns. | Gameplay variety |
| 58 | Sector 2 boss | Different boss with different patterns. Larger. More projectiles. | Boss variety |
| 59 | Sector 2 complete | Full pixel-scrolled sector with new terrain, enemies, and boss. | Second level |
| 60 | Contention profiling | Measure exactly where contention costs the most. Map the timing. | Deep hardware understanding |
| 61 | Contention-aware scroll | Schedule shift operations to avoid the worst contention windows. | Optimised timing |
| 62 | Frame budget | Total: scroll + sprites + enemies + collision + HUD must fit in one frame. Map the budget. | Performance budgeting |
| 63 | Dropped frame handling | If the frame takes too long: skip the scroll update, keep game logic running. Graceful degradation. | Frame skip strategy |
| 64 | Integration | Sector 1 + 2 playable. Smooth pixel scroll. Restore-under sprites. Performance mapped. | **Phase 2 complete** |

**Key Teaching Moment (Unit 42):**
The fine/coarse hybrid is how commercial Spectrum shooters work. Seven pixel shifts (each shifting the entire bitmap by 1 bit) followed by one character-cell shift (LDIR, moving bytes not bits). The pixel shifts are expensive; the character shift is cheap. After the character shift, the pixel counter resets and the cycle repeats. The result: smooth scrolling that most frames can handle.

**End of Phase 2:** Smooth pixel scrolling at 1 pixel per frame. Two playable sectors. Restore-under sprites. This is the technique that made R-Type on the Spectrum possible. The learner has built it from scratch.

---

## Phase 3: Swarm (Units 65–96)

**Goal:** Enemy variety, formation patterns, weapon upgrades.
**Z80 Focus:** Lookup tables, sine tables for movement, fixed-point arithmetic.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 65-68 | Enemy formation system | Sine table for wave patterns, formation data, spawn triggers | Swooping enemy waves |
| 69-72 | Weapon upgrade system | Ion cannon levels 1-3, spread shot, rear fire. Power-up drops. | Weapon variety |
| 73-76 | Enemy bullet patterns | Aimed shots, spread shots, streaming fire. Dodge-based gameplay. | Bullet hell (lite) |
| 77-80 | Terrain interaction | Destructible walls, hidden passages, terrain-embedded turrets. | Interactive environment |
| 81-84 | Sector 3: Organic Hive | Biological terrain, pulsing walls, spawner nests. Distinct visual theme. | Third sector |
| 85-88 | Shield and charge mechanics | Shield absorbs one hit. Charge shot: hold fire for powerful blast. | Advanced player mechanics |
| 89-92 | Mid-level checkpoints | Restart from checkpoint on death, not level start. Fairness for a long level. | Checkpoint system |
| 93-96 | Integration and balance | Enemy density, power-up frequency, checkpoint placement. All 3 sectors polished. | Three sectors complete |

**Key Teaching Moment (Units 65-68):**
Sine tables drive enemy wave patterns. Pre-compute 256 SIN values (0-255 mapped to -127..+127). Enemy Y position = base_Y + sine_table[frame_counter AND 255]. One array lookup per enemy per frame — negligible cost, beautiful curves. The same table serves weapon wobble, boss movement, and parallax offsets.

**End of Phase 3:** Three sectors with varied terrain, enemy formations, weapon upgrades, bullet patterns, and bosses. A real shmup.

---

## Phase 4: Arsenal (Units 97–128)

**Goal:** Sectors 4 and 5. Full weapon system. Complete 5-sector game.
**Z80 Focus:** Memory management, level streaming, complex game state.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 97-104 | Sector 4: Machine Fortress | Metal terrain, mechanical enemies, conveyor hazards, turret boss | Fourth sector |
| 105-112 | Sector 5: The Core | Alien organic + machine hybrid. Final boss with multiple phases. | Fifth sector |
| 113-116 | Weapon system complete | All upgrades, all weapon types, visual distinction per level | Full arsenal |
| 117-120 | Difficulty curve | Sector 1 gentle, sector 5 intense. Enemy speed/density/pattern escalation. | Balanced progression |
| 121-124 | Score attack features | Score multiplier for chains, bonus for no-death sectors, leaderboard incentive | Replay motivation |
| 125-128 | Integration | Full 5-sector playthrough. 48K memory audit. Performance stable. | **Five sectors complete** |

**End of Phase 4:** All 5 sectors playable. Complete weapon system. Balanced difficulty. The game is content-complete.

---

## Phase 5: Resonance (Units 129–160)

**Goal:** Audio — beeper effects and AY soundtrack.
**Z80 Focus:** AY programming, interrupt-driven music, SFX prioritisation.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 129-136 | Beeper effect library | Laser fire, explosion, power-up collect, death, boss hit | 48K audio |
| 137-144 | AY music engine | Per-sector themes, boss music, title theme. Interrupt-driven. | 128K soundtrack |
| 145-152 | SFX over music | Temporarily steal AY voice for effects, restore seamlessly | Layered audio |
| 153-160 | Audio integration | Balance, 48K/128K detection, title music, end music | Complete audio |

**End of Phase 5:** Full audio. 48K beeper effects. 128K three-voice AY soundtrack with per-sector themes.

---

## Phase 6: Guardians (Units 161–192)

**Goal:** Boss polish, visual effects, sector transitions.
**Z80 Focus:** State machines, multi-part sprites, scripted sequences.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 161-168 | Boss state machines | Each boss: idle → telegraph → attack → recover. Multiple phases. Pattern scripting. | Rich boss encounters |
| 169-176 | Multi-part bosses | Bosses from multiple sprites. Weak points. Destructible parts. | Imposing guardians |
| 177-184 | Sector transitions | Scroll stops, terrain opens out, boss arena, post-boss warp effect | Dramatic pacing |
| 185-192 | Visual effects | Explosion particles, screen shake (attribute flash), warp tunnel between sectors | Visual polish |

**End of Phase 6:** Five memorable boss encounters with multi-phase patterns, destructible parts, and dramatic transitions. The bosses are the game's highlight.

---

## Phase 7: Sectors (Units 193–224)

**Goal:** Level streaming, parallax, visual variety, 128K enhancements.
**Z80 Focus:** Memory management, 128K paging, double buffering.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 193-200 | Level streaming | Tile map loaded progressively, not all in memory. Column-by-column from compressed data. | Memory-efficient levels |
| 201-208 | Parallax enhancement | Background layer using attribute manipulation (distant stars move slower). | Depth illusion |
| 209-216 | 128K double buffer | Alternate screen pages ($4000 and $C000) for tear-free scrolling | Smooth display |
| 217-224 | 128K extra content | Bonus sector, extended weapon system, enhanced parallax | Premium experience |

**End of Phase 7:** Level streaming for unlimited level length. Parallax depth. 128K double-buffered scrolling for tear-free display.

---

## Phase 8: Aftermath (Units 225–256)

**Goal:** Commercial polish. Ship it.
**Z80 Focus:** Optimisation, distribution formats, final integration.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 225-228 | Title screen | "IONFIRE" with scrolling starfield demo, ship flying through | Presentation |
| 229-232 | High score table | Top 5, name entry, display on title | Bragging rights |
| 233-236 | Attract mode | Recorded playthrough of sector 1 opening | Demo mode |
| 237-240 | Difficulty select | Easy (slow scroll, weak enemies), Normal, Hard (fast scroll, dense fire) | Accessibility |
| 241-244 | Continue system | Restart from last sector reached (limited continues) | Fairness |
| 245-248 | Ending sequence | Final boss defeated → ship escapes → colony saved → credits roll | Narrative closure |
| 249-252 | Loading screen and turbo loader | Custom artwork, fast loading routine | Professional package |
| 253-254 | 48K/128K testing | Full playthrough on both models. Memory audit. Performance verification. | Release quality |
| 255 | TAP/TZX creation | Tape format, turbo blocks, loading sequence | Distribution |
| 256 | **The finished game** | Final build | **Ship it** |

---

## Technical Notes

### The Fine/Coarse Scroll Algorithm

```z80
scroll_frame:
    ld a,(scroll_pixel)
    inc a
    cp 8
    jr z,.coarse_scroll

    ; FINE SCROLL: shift bitmap right by 1 pixel
    ld (scroll_pixel),a
    call shift_bitmap_right_1px
    ret

.coarse_scroll:
    ; COARSE SCROLL: shift bytes right by 1 position
    xor a
    ld (scroll_pixel),a
    call shift_bitmap_right_8px    ; LDIR-based byte shift
    call shift_attributes_right    ; Attribute scroll
    call draw_new_column           ; New tile at left edge
    ret

shift_bitmap_right_1px:
    ; For each of 192 pixel rows:
    ;   Start at rightmost byte of row
    ;   SRL (HL) to shift right, carry out
    ;   Move left: RR (HL) to chain carry in
    ;   Repeat across 32 bytes
    ; Unrolled inner loop for speed
    ...
```

### Restore-Under Sprite System

```z80
; Before drawing a sprite:
;   Save the screen bytes it will overwrite
; After game logic:
;   Restore the saved bytes (erasing the sprite)
;   Then draw at the new position

draw_sprite:
    ; Save background at new position
    ld hl,screen_addr
    ld de,save_buffer
    ; Copy 8 rows × 2 bytes (16×8 sprite)
    ...
    ; XOR sprite data onto screen
    ld hl,screen_addr
    ld de,sprite_data
    ; XOR 8 rows
    ...

erase_sprite:
    ; Copy save_buffer back to screen
    ld hl,save_buffer
    ld de,old_screen_addr
    ...
```

### Frame Budget (48K, ~69,888 T-states per frame)

| Task | T-states (approx) | % of frame |
|------|-------------------|------------|
| Pixel scroll (fine) | 25,000-35,000 | 36-50% |
| Sprite draw/erase (5 sprites) | 8,000-12,000 | 11-17% |
| Enemy AI + movement | 4,000-6,000 | 6-9% |
| Collision detection | 2,000-3,000 | 3-4% |
| HUD update | 1,000-2,000 | 1-3% |
| AY music (128K, IM 2) | 2,000-3,000 | 3-4% |
| **Available margin** | **~10,000-20,000** | **~15-28%** |

The scroll consumes 35-50% of the frame. This is why every other system must be efficient. Contention during the display period makes the effective budget even tighter.

### Contention Windows

The ULA steals CPU time during screen display (T-states 14335-57343 per frame on 48K). Each access to $4000-$7FFF during this window costs an extra 1-6 T-states. Strategies:
- Schedule the scroll during vertical blank (border time)
- Accept some contention but minimise accesses during peak display
- 128K: use double buffering to scroll the off-screen page (no contention)

---

## CRASH! Live Strategy

Ionfire is unlikely to be ready for October — it's a 256-unit game and the scrolling technique alone takes months to master. However, a **tech demo** showing smooth pixel scrolling with a ship flying through terrain would be a powerful complement to Gravelight:

- Phases 1-2 (64 units) produce: pixel-smooth scrolling, ship, basic enemies
- Even Phase 1 alone (32 units): character-cell scrolling with enemies is demonstrable

If Gravelight Phases 1-2 are the launch content, Ionfire Phase 1 could be a "coming next" preview.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. New Game 2 for the restructured Spectrum assembly track. Software pixel scrolling as the signature technique.
