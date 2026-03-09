# Full Game Outline: ZX Spectrum Grimstone (512 Units)

**Game:** Grimstone (Game 3)
**Units:** 512 (16 phases × 32 units)
**Genre:** Isometric adventure
**Inspired by:** Knight Lore, Head Over Heels, Batman, Cadaver
**Target Quality:** Commercial-grade isometric adventure (1986–89 era)

---

## Premise

Grimstone Keep has stood for a thousand years. Its corridors shift. Its rooms rearrange. Those who enter forget why they came. You were a knight once — you remember that much. Now you're something else: cursed, half-changed, stuck between forms. Somewhere in the keep is the Grimshard, the source of the curse. Break it and you break free. Fail, and you become another stone in the walls.

The curse manifests as a transformation mechanic: every N seconds, the player shifts between human and beast form. Human form can push blocks and use keys. Beast form can jump higher and survive falls. Some rooms require one form; some require the other. The timer is always ticking. The player must plan routes around the transformation — reaching the right room in the right form at the right time.

---

## Why Isometric Matters

Ultimate Play the Game released Knight Lore in 1984. It rendered a 3D world on hardware designed for flat text. The isometric projection — diamond-shaped tiles, depth-sorted objects, a z-axis for height — created the illusion of a three-dimensional castle on a machine with 256×192 pixels and attribute colour clash.

It was a paradigm shift. Before Knight Lore, Spectrum games were flat. After it, an entire genre existed: isometric adventures. Head Over Heels (1987), Batman (1986), La Abadía del Crimen (1987) — all descendants of Knight Lore's engine.

Grimstone teaches the learner to build that engine from scratch. The isometric projection, depth sorting, Z-height collision, and room rendering are genuine computer science — coordinate transforms, painter's algorithm, spatial reasoning. And the result looks like nothing else in the curriculum.

---

## Design Philosophy

- **Isometric from Phase 1** — projection maths start immediately
- **One rendered room by Phase 2** — visible result early, not months of theory
- **Depth sorting is the hard problem** — more time on this than any other single technique
- **The transformation mechanic IS the game design** — it's not a gimmick, it's the puzzle core
- **128K from Phase 10** — AY music, bank-switched room data, dual-page rendering
- **100+ rooms** — a real world, not a tech demo
- **5 zones, 5 bosses** — structure and progression
- **512 units for depth** — isometric rendering + adventure game + 128K features demand the full scope

---

## Z80 Progression

| Phase | Z80 Focus |
|-------|-----------|
| 1 (Foundations) | Isometric maths: coordinate transforms, multiplication via shifts/adds |
| 2 (Rendering) | Tile drawing, back-to-front rendering, UDG-based isometric tiles |
| 3 (Depth) | Painter's algorithm, sort by depth key, draw order management |
| 4 (Movement) | Isometric input mapping, grid movement, smooth animation |
| 5 (Z-Height) | Z-axis: jumping, falling, platforms at different heights |
| 6 (Interaction) | Push blocks, pressure plates, doors, switches |
| 7 (Rooms) | Room data format, connections, transitions, world structure |
| 8 (Creatures) | Isometric enemy movement, AI, combat |
| 9 (Transformation) | Timer system, form switching, form-specific abilities |
| 10 (Sound) | AY music for 128K, beeper effects for 48K |
| 11 (World) | 100+ rooms across 5 zones, zone themes |
| 12 (Puzzles) | Multi-room puzzles, item combinations, sequence puzzles |
| 13 (Bosses) | Boss encounters per zone, multi-phase patterns |
| 14 (Atmosphere) | Lighting, shadows, visual effects, narrative |
| 15 (128K) | Memory paging, bank-switched rooms, enhanced graphics |
| 16 (Release) | Title, high scores, save/passwords, distribution |

---

## Phase 1: Foundations (Units 1–32)

**Goal:** Understand isometric projection. Draw a single tile on screen.
**Z80 Focus:** Coordinate transforms, multiplication via shifts and adds.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 1 | What is isometric? | Concept: 2D screen represents 3D space. Diagram: world X/Y/Z → screen X/Y. | Mental model |
| 2 | The diamond tile | An 8×8 diamond shape (4 pixels wide at top, 8 in middle, 4 at bottom). Draw it manually. | Pixel-level understanding |
| 3 | World-to-screen formula | screen_x = (world_x - world_y) × tile_half_width. screen_y = (world_x + world_y) × tile_half_height. | The transform |
| 4 | Implementing the transform | Z80: multiply by tile_half_width using shifts and adds. No MUL instruction — build it. | Shift-based multiplication |
| 5 | One tile at calculated position | Apply formula to world position (3,2) → screen position. Draw diamond tile there. | **First isometric tile** |
| 6 | A row of tiles | Loop: draw tiles at (0,0), (1,0), (2,0)... They form a diagonal line going right-and-down. | Isometric row |
| 7 | A grid of tiles | Nested loop: draw tiles at every (x,y) from (0,0) to (7,7). A diamond-shaped floor appears. | **Isometric floor** |
| 8 | Tile graphics | Design proper isometric floor tile: top surface lighter, sides darker. 3D illusion. | Tile art design |
| 9 | Wall tiles | Isometric wall: a cube. Top face + left face + right face. Different shading per face. | Wall tile design |
| 10 | UDG-based tiles | Define tiles as UDG sets. Each isometric tile = 2-4 UDG characters arranged in a pattern. | UDG tile system |
| 11 | Floor and walls | Draw a room floor (8×8 grid) with walls around the edges. It looks like a room viewed from above-right. | **First isometric room** |
| 12 | Screen coordinate system | Map the room to screen pixels. Centre the room on the display. Define the viewport. | Screen mapping |
| 13 | Tile types | Floor, wall, block (pushable), platform (raised), empty (hole). Each a different tile graphic. | Tile variety |
| 14 | Room data format | Array: 8×8 grid, each byte = tile type. Room data → tile lookup → screen rendering. | Data-driven room |
| 15 | Room from DATA | Store a room layout in a data table. Read and render. Change the data → different room. | Data-driven rendering |
| 16 | Multiple rooms in data | 3 room layouts. Swap which one renders. The engine can show different rooms. | Room switching |
| 17 | Rendering order | Drawing left-to-right, top-to-bottom in world space = correct overlap for floor tiles. | Basic draw order |
| 18 | Wall occlusion problem | Walls drawn after floor tiles overlap correctly. But objects behind walls should be hidden. | The depth problem introduced |
| 19 | Depth key | Each object has a depth key: world_x + world_y (+ world_z for height). Higher key = drawn later = in front. | Depth key concept |
| 20 | Sorting by depth | Simple insertion sort on objects by depth key. Draw in sorted order. | Sort algorithm |
| 21 | Object on floor | Place a non-tile object (a block) at a grid position. Calculate screen position. Draw at correct depth. | Object in isometric space |
| 22 | Object behind wall | A block at (2,2) is correctly hidden behind a wall at (2,3) because the wall's depth key is higher. | **Depth sorting works** |
| 23 | Multiple objects | 3-4 blocks placed in a room. All sort and render correctly regardless of position. | Multi-object depth sort |
| 24 | Object types | Block (cube), gem (small item), door (tall rectangle), spike (flat hazard). Different graphics. | Object variety |
| 25 | Raised platforms | A tile at Z=1 (elevated). Screen Y offset by tile height. Draws above floor tiles. | Z-axis introduction |
| 26 | Stacking | Block on a platform: both render correctly. Block is higher in screen Y. | Objects at different heights |
| 27 | Z in depth key | Depth key = world_x + world_y + world_z. Objects at different heights sort correctly. | 3D depth sorting |
| 28 | Room with height | A room with floor tiles at Z=0, platforms at Z=1, and objects on both levels. All renders correctly. | Multi-height room |
| 29 | Rendering performance | Time the room renderer. How many objects before it's too slow? Optimise the sort. | Performance awareness |
| 30 | Dirty rectangle | Only redraw objects that moved. Track changed positions. Skip unchanged tiles. | Optimised rendering |
| 31 | Full room renderer | Complete: load room data → sort objects by depth → draw back-to-front → clean display. | Rendering engine complete |
| 32 | Three test rooms | Three rooms with different layouts, heights, and objects. Switch between them. Renderer handles all. | **Engine foundation** |

**End of Phase 1:** The isometric rendering engine draws rooms with floor tiles, walls, objects, and platforms at multiple heights. Depth sorting produces correct occlusion. The hardest computer science in the entire curriculum is solved.

---

## Phase 2: Movement (Units 33–64)

**Goal:** The player moves through isometric space. Grid-based, animated, with collision.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 33 | Player object | A character object placed in the room at a grid position. Rendered in the sort order. | Player in the world |
| 34 | Isometric input mapping | Up key = move in world (-x,-y) direction. Down = (+x,+y). Left = (-x,+y). Right = (+x,-y). | Input remapping for isometric |
| 35 | Grid movement | Player moves one grid cell per input. Position updates. Re-render. | **Player moves** |
| 36 | Smooth animation | Player slides between grid positions over 4-8 frames. Interpolate screen position. | Animated movement |
| 37 | Walk cycle | Player UDG frames: 2-4 per direction (NE, NW, SE, SW). Cycle during movement. | Character animation |
| 38 | Wall collision | Before moving: check if target grid cell is a wall tile. If wall: blocked. | Grid collision |
| 39 | Block collision | Target cell has a block object: blocked (for now — pushing comes later). | Object collision |
| 40 | Edge of room | Moving past the room boundary: trigger room transition (later). For now: blocked. | Boundary check |
| 41 | Idle animation | Player bobs or breathes when stationary. Subtle, one-frame alternation. | Idle state |
| 42 | Player facing | Player faces the direction of last movement. Different UDG per facing. | Directional sprites |
| 43 | Gravity in isometric | If the floor tile below the player is empty (hole), the player falls. Z decreases. | Falling |
| 44 | Landing | Player falls until hitting a solid tile at a lower Z. Landing animation + sound. | Fall resolution |
| 45 | Jumping | Jump button: player Z increases over frames (arc), then falls. Peak = 1 tile height. | Jump in isometric |
| 46 | Jump collision | Check Z-height at destination. Can't jump through a ceiling (tile at higher Z above). | Vertical collision |
| 47 | Landing on blocks | Jump onto a raised block or platform. Player Z matches the object's Z. | Platform landing |
| 48 | Walking off edges | Walk off a platform edge: player falls to the level below. | Edge detection |
| 49 | Player shadow | A small diamond shadow on the floor directly below the player. Helps judge position. | Spatial aid |
| 50 | Shadow at different heights | Shadow stays on the floor regardless of player Z. Visual grounding. | Height indicator |
| 51 | Camera/viewport | If the room is larger than the screen, viewport follows the player. | Scrolling viewport |
| 52 | Room rendering with player | Player is part of the depth sort. Walks behind walls, in front of objects at lower depth. | Correct player occlusion |
| 53 | Interaction prompt | Standing next to an object shows a subtle prompt ("?" or highlight). | Interaction feedback |
| 54 | Pick up items | Stand on a gem: collect it. Score increases. Gem removed from room. | Item collection |
| 55 | Inventory | Collected items stored in an inventory array. HUD shows icons. | Inventory system |
| 56 | Inventory display | Press I: overlay shows inventory contents. Press again to dismiss. | Inventory screen |
| 57 | Room data with player start | Room data includes player start position and facing. | Spawn points |
| 58 | Three rooms with movement | Player moves through three test rooms. Collision, jumping, and items work in all. | Movement complete |
| 59 | Status bar | Health, score, inventory icons, transformation timer (later), room name. | HUD design |
| 60 | Sound effects | Footstep beep per grid move. Jump sound. Land sound. Collect sound. | Basic audio |
| 61 | Movement polish | Input buffering (press key before previous move finishes). Responsive feel. | Input quality |
| 62 | Performance with player | Room re-renders on every player move. Is it fast enough? Profile. | Performance check |
| 63 | Incremental update | Only re-sort and redraw objects affected by movement. Background tiles cached. | Optimised update |
| 64 | Integration | Full isometric room with player, items, collision, jumping, sound. | **Phase 2 complete** |

**Key Teaching Moment (Unit 34):**
Isometric input mapping is counter-intuitive. The "up" key doesn't move the player up on screen — it moves them along the world's -X/-Y diagonal, which appears as up-and-left on screen. The learner must disconnect "screen direction" from "world direction." This is genuine 3D thinking on a 2D display.

**End of Phase 2:** The player moves through isometric rooms with full collision, jumping, item collection, and correct depth-sorted rendering. The engine is playable.

---

## Phase 3: Interaction (Units 65–96)

**Goal:** Push blocks, pressure plates, doors, switches — the puzzle mechanics.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 65-68 | Push blocks | Walk into a block → it slides one cell in push direction (if space behind is empty). Check behind-block collision. | **Core puzzle mechanic** |
| 69-72 | Pressure plates | Floor tiles that detect weight (player or block on them). Trigger state change. | Triggerable tiles |
| 73-76 | Doors | Locked doors block passage. Keys open matching doors (colour-coded). | Key/door puzzles |
| 77-80 | Switches | Wall switches toggle doors open/closed. Some switches are timed (door closes after N seconds). | Switch puzzles |
| 81-84 | Conveyor tiles | Floor tiles that push the player (and blocks) in a direction each frame. | Environmental hazards |
| 85-88 | Ice tiles | Floor tiles with no friction — player slides until hitting a wall or normal floor. | Sliding puzzles |
| 89-92 | Teleport tiles | Step on a teleport → appear at linked teleport in same room or different room. | Warp mechanic |
| 93-96 | Puzzle rooms | 5 test puzzle rooms using all mechanics. Solvable, satisfying, teaching the mechanics. | Puzzle design |

**Key Teaching Moment (Units 65-68):**
Push blocks must check two cells: the block's target (where it would move) AND the cell behind that (is there a wall stopping it?). In isometric space, "behind" depends on push direction. The learner implements directional two-cell-ahead checking — the same logic Sokoban uses, but in isometric coordinates.

**End of Phase 3:** Push blocks, pressure plates, doors, switches, conveyors, ice, teleports. The puzzle toolkit is complete.

---

## Phase 4: The Keep (Units 97–128)

**Goal:** Room connections, world structure, zone themes. The keep takes shape.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 97-104 | Room connections | Exit at room edge → load connected room. Player position maps to entry point of new room. Room transition animation. | World navigation |
| 105-112 | World map | 5 zones of 20+ rooms. Zone 1: Stone Halls. Rooms linked in a navigable graph. Map screen shows explored rooms. | World structure |
| 113-120 | Zone themes | Different tile graphics and colour palettes per zone. Stone (grey), Wood (brown), Crystal (cyan), Iron (red), Void (black). | Visual variety |
| 121-128 | Room transitions | Cross-fade or wipe between rooms. Brief "loading" covered by animation. Room state persisted (pushed blocks stay pushed). | Polished transitions |

**End of Phase 4:** 20+ rooms in Zone 1. Connected world with themed visuals. Room state persists. Map screen. The keep feels like a real place.

---

## Phase 5: Creatures (Units 129–160)

**Goal:** Enemies in isometric space.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 129-136 | Isometric enemy movement | Enemies move on the grid like the player. Patrol routes. Depth-sorted rendering. | Enemies in 3D space |
| 137-144 | Enemy variety | Crawlers (floor), flyers (Z=1, ignore holes), ghosts (pass through walls), bouncers (jump randomly) | Enemy types |
| 145-152 | Enemy-player collision | Contact = damage. Health system (4 hits). Invincibility frames. | Combat |
| 153-160 | Enemy-block interaction | Enemies walk around blocks. Some enemies push blocks (dangerous — can crush player). | Environmental interaction |

**End of Phase 5:** Four enemy types in isometric space, all depth-sorted correctly. Combat with health and invincibility.

---

## Phase 6: Transformation (Units 161–192)

**Goal:** The curse mechanic — the game's unique design hook.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 161-168 | Timer system | Countdown timer visible in HUD. When it reaches zero: transformation. | Timer mechanic |
| 169-176 | Form switching | Human → Beast (or reverse) with animation. Different UDG set per form. | Visual transformation |
| 177-184 | Form abilities | Human: push blocks, use keys, operate switches. Beast: jump 2 tiles high, survive long falls, claw attack (kills enemies on contact). | Form-specific gameplay |
| 185-192 | Form-dependent puzzles | Rooms that require specific forms. Timed route planning: "I need to be in beast form when I reach that ledge." | Strategic timing |

**Key Teaching Moment (Unit 185):**
The transformation timer turns every room into a time puzzle. The player must plan: "The high platform needs beast form. The locked door needs human form. I transform in 15 seconds. I need to reach the platform first, jump up, then wait for the transformation to use the key." This is game design that emerges from one simple rule (periodic form change) creating complex strategic decisions.

**End of Phase 6:** The transformation mechanic is complete. Human and beast forms with distinct abilities. Timed puzzles that require form planning.

---

## Phase 7: Sound (Units 193–224)

**Goal:** Full audio — beeper effects and AY soundtrack.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 193-200 | Beeper effect library | Footsteps, jump, land, push, collect, door, damage, death, transform | 48K audio |
| 201-208 | AY music engine | Per-zone themes (5 themes + boss + title). Interrupt-driven. | 128K soundtrack |
| 209-216 | Transformation audio | Musical motif plays during transformation. Eerie rising tone (human→beast) or descending (beast→human). | Signature sound |
| 217-224 | Audio integration | 48K/128K detection, SFX priority over music, volume balance | Complete audio |

**End of Phase 7:** Full audio. The transformation has a distinctive musical signature. Each zone has its own mood.

---

## Phase 8: The World (Units 225–256)

**Goal:** 100+ rooms across 5 zones. The full keep.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 225-232 | Zone 2: Timber Halls | 20+ rooms, wooden theme, new enemy types, new puzzles | Second zone |
| 233-240 | Zone 3: Crystal Caverns | 20+ rooms, crystalline theme, ice floors, light-based puzzles | Third zone |
| 241-248 | Zone 4: Iron Forge | 20+ rooms, industrial theme, conveyor puzzles, fire hazards | Fourth zone |
| 249-256 | Zone 5: The Void | 20+ rooms, dark theme (fog of war returns), the Grimshard somewhere within | Final zone |

**End of Phase 8:** 100+ rooms across 5 themed zones. The keep is vast and varied.

---

## Phase 9: Puzzles (Units 257–288)

Multi-room puzzle sequences that span zones. Items found in Zone 1 used in Zone 3. Keys that unlock shortcuts. Secret rooms behind breakable walls. The Grimstone world rewards exploration and lateral thinking.

---

## Phase 10: Bosses (Units 289–320)

One guardian per zone. Each boss occupies a 2×2 or larger isometric space. Multi-phase patterns: telegraph → attack → recover. Each requires the correct form to defeat (human boss needs beast combat, beast boss needs human puzzle-solving). The Zone 5 boss guards the Grimshard.

---

## Phase 11: 128K Features (Units 321–352)

Memory paging ($7FFD) for room data in banked RAM. 128K gets: more rooms (20 bonus rooms), enhanced tile graphics (double-buffered rendering for flicker-free transitions), AY music during room transitions (48K goes silent during load).

---

## Phase 12: Atmosphere (Units 353–384)

Dynamic lighting in the Void zone (fog of war from Gravelight, adapted to isometric). Shadow casting from walls. Transformation visual effects (screen border colour flash, brief attribute colour shift). Narrative text discoveries (journals, inscriptions found in rooms).

---

## Phase 13: Content Polish (Units 385–416)

100+ rooms reviewed and balanced. Puzzle fairness audit: every puzzle solvable, every transformation timer generous enough, every item reachable. Enemy placement tuned. Zone difficulty curve: Zone 1 gentle, Zone 5 demanding.

---

## Phase 14: Production (Units 417–448)

Title screen ("GRIMSTONE" in isometric block letters). Attract mode (automated walkthrough of Zone 1 opening). High score table. Difficulty select (Normal: 30-second transform timer; Hard: 20-second; Easy: 45-second). Password system per zone.

---

## Phase 15: Distribution (Units 449–480)

48K memory audit (fit 100+ rooms compressed + engine + graphics + beeper audio). 128K memory map (room banks + AY music + enhanced graphics). Turbo loader. Loading screen. TAP/TZX creation. +3 disk version.

---

## Phase 16: Release (Units 481–512)

**Goal:** Final testing, ending sequence, credits, ship.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 481-496 | Ending sequence | Grimshard destroyed → curse lifts → transformation stops → keep transforms (rooms brighten) → escape to daylight | Narrative climax |
| 497-508 | Final testing | Every room, every puzzle, every boss, every form, every zone, 48K and 128K | Release quality |
| 509-510 | Credits | Scrolling credits with isometric room in background | Attribution |
| 511 | Documentation | Player guide, map hints (printed or on-screen) | Player support |
| 512 | **The finished game** | Final build | **Ship it** |

---

## Technical Notes

### Isometric Projection

```z80
; World (wx, wy) → Screen (sx, sy)
; tile_half_width = 8 pixels, tile_half_height = 4 pixels
;
; sx = ORIGIN_X + (wx - wy) × 8
; sy = ORIGIN_Y + (wx + wy) × 4 - wz × 8

world_to_screen:
    ; Calculate (wx - wy) × 8
    ld a,(world_x)
    sub (world_y)           ; A = wx - wy (signed)
    ; Multiply by 8: shift left 3
    sla a
    sla a
    sla a                   ; A = (wx - wy) × 8
    ld b,a                  ; B = screen X offset

    ; Calculate (wx + wy) × 4
    ld a,(world_x)
    add a,(world_y)         ; A = wx + wy
    sla a
    sla a                   ; A = (wx + wy) × 4

    ; Subtract wz × 8 for height
    ld c,a
    ld a,(world_z)
    sla a
    sla a
    sla a                   ; A = wz × 8
    ld d,a
    ld a,c
    sub d                   ; A = (wx+wy)×4 - wz×8
    ld c,a                  ; C = screen Y offset

    ; Add origin
    ld a,b
    add ORIGIN_X
    ld (screen_x),a
    ld a,c
    add ORIGIN_Y
    ld (screen_y),a
    ret
```

### Depth Sorting

```z80
; Depth key for sorting: wx + wy + wz
; Higher key = drawn later = appears in front
;
; Simple insertion sort (sufficient for 20-30 objects per room)

sort_objects:
    ld b,(num_objects)
    dec b                   ; B = comparisons needed
.outer:
    push bc
    ld ix,object_table
    ld b,(num_objects)
    dec b
.inner:
    ; Compare depth key of object[i] and object[i+1]
    ld a,(ix+DEPTH_KEY)
    cp (ix+OBJ_SIZE+DEPTH_KEY)
    jr c,.no_swap           ; Already in order
    ; Swap the two entries
    call swap_objects
.no_swap:
    ; Advance to next pair
    ld de,OBJ_SIZE
    add ix,de
    djnz .inner
    pop bc
    djnz .outer
    ret
```

### Room Data Format

```
Room header: 8 bytes
  - Width, Height (always 8×8 for standard rooms)
  - Zone ID (determines tile set)
  - Connections: N room, S room, E room, W room (0 = no exit)
  - Flags: has_boss, has_secret, dark_room

Floor grid: 64 bytes (8×8, 1 byte per cell)
  - Tile types: 0=empty, 1=floor, 2=wall, 3=platform_z1, 4=ice, 5=conveyor_N, etc.

Object list: variable length
  - Count (1 byte)
  - Per object: type, world_x, world_y, world_z, flags (5 bytes each)

Enemy list: variable length
  - Count (1 byte)
  - Per enemy: type, world_x, world_y, patrol_data (variable)

Compressed: ~40-80 bytes per room (RLE on floor grid, compact object list)
100 rooms × 60 bytes average = ~6KB compressed
```

### Memory Map (48K)

```
$0000-$3FFF: ROM
$4000-$57FF: Screen bitmap (6,144 bytes)
$5800-$5AFF: Attributes (768 bytes)
$5B00-$5BFF: Printer buffer (unused — available)
$5C00-$5CBF: System variables
$5CC0-$7FFF: Free RAM (~9KB) — room buffer, sort buffer, object state
$8000-$BFFF: Game code (~16KB)
$C000-$FFFF: Room data (compressed), tile graphics, UDGs, music (~16KB)
```

### Memory Map (128K)

```
Pages 0-4: Game code + tile graphics + UDGs + beeper audio (~80KB available)
Pages 5-7: Room data banks (3 banks × 16KB = 48KB of room data — 800+ rooms possible)
Page 5 ($C000): Screen 1 (double buffering)
Page 7 ($C000): Screen 0 (normal)
AY music data: in banked RAM, paged in during interrupt handler
```

---

## CRASH! Live Strategy

Grimstone is a long game to build — 512 units. It won't be anywhere near complete for October. But the *engine* could be demonstrable:

- **Phases 1-2 (64 units):** Isometric room with player movement. This alone is impressive — "look, we're building Knight Lore from scratch."
- **As a tech demo alongside Gravelight:** Gravelight is the playable game; Grimstone is the "coming in 2027" preview.

The isometric engine is visually striking. Even a single room with a walking character and correct depth sorting would make an impact at CRASH! Live.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. New Game 3 for the restructured Spectrum assembly track. Isometric adventure with transformation mechanic.
