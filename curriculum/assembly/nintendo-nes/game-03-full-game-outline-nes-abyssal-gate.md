# Full Game Outline: NES Abyssal Gate (512 Units)

**Game:** Abyssal Gate (Game 3)
**Units:** 512 (16 phases × 32 units)
**Genre:** Metroidvania
**Inspired by:** Metroid, Castlevania III, Kid Icarus, Blaster Master
**Target Quality:** Commercial-grade exploration action (1989–91 era)

---

## Premise

Below the ruined city, the gate opened. Something came through — not alive, not dead, but spreading. The tunnels are vast: five regions of interconnected caverns, each with its own ecosystem warped by the gate's influence. Bioluminescent fungi light the Crystal Hollows. Frozen rivers carve through the Glacial Rift. Machinery still churns in the Abandoned Works. Magma pulses beneath the Molten Abyss. And at the centre: the Gate Chamber, where the rift between worlds stays open.

You drop in with a basic weapon and no way back up. Every ability you find — wall jump, double jump, dash, morph, charge beam, missiles — opens new paths through old rooms. The world is one connected map. No loading screens. No level select. Just deeper and deeper into the abyss.

---

## Why This Game

Metroid defined the Metroidvania. A non-linear world that opens as the player gains abilities. Backtracking that reveals secrets. An atmosphere of isolation. And technically: the MMC3 mapper with its scanline counter, bank switching for varied tilesets, and battery SRAM for progress saves.

Abyssal Gate teaches:
- **MMC3 mapper** — the most important NES mapper
  - PRG bank switching (8KB switchable banks for code and data)
  - CHR bank switching (multiple tilesets per region, swap mid-frame for variety)
  - Scanline counter (IRQ at specific scanline for HUD split, parallax, status bar)
- **Large connected world** — 200+ rooms in one seamless map
- **Ability gating** — 8+ abilities that progressively open the world
- **Non-linear design** — multiple valid routes through the game
- **Map system** — fog-of-war minimap, filling in as the player explores
- **Advanced APU** — per-region themes, DMC samples for bass and impact
- **Battery SRAM** — multiple save slots with comprehensive game state

---

## 6502 Progression

| Phase | 6502/NES Focus |
|-------|---------------|
| 1-2 | MMC3 setup: bank registers, PRG switching, CHR switching |
| 3-4 | Scanline counter: IRQ setup, HUD split, mid-frame effects |
| 5-6 | World structure: room connections, scrolling within rooms, seamless transitions |
| 7-8 | Abilities: wall jump, double jump, dash, morph, charge beam, missiles |
| 9-10 | 5 regions with distinct tilesets, enemies, and bosses |
| 11-12 | Map system, saves, percentage tracking |
| 13-14 | Advanced APU: per-region themes, DMC samples, atmospheric audio |
| 15-16 | Polish, multiple endings, sequence-break design, distribution |

---

## Phase 1-2: The MMC3 (Units 1–64)

**Phase 1 (Units 1-32): MMC3 Fundamentals**

The MMC3 (mapper 4) is the most common advanced NES mapper. It provides:
- 8KB switchable PRG banks (2 switchable + 2 fixed)
- 2KB/1KB switchable CHR banks (6 switchable banks)
- Scanline counter (IRQ fires after N scanlines)
- Battery-backed SRAM support

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 1-4 | MMC3 iNES header and bank setup | Mapper 4 header, bank register writes ($8000/$8001) | MMC3 initialised |
| 5-8 | PRG bank switching | Switch 8KB PRG banks to load different code/data modules | More than 32KB accessible |
| 9-12 | CHR bank switching | Switch CHR banks for different tilesets. Region 1 tiles vs Region 2 tiles. | Visual variety per area |
| 13-16 | Basic room with CHR from banked ROM | A room rendered with tiles from a switched CHR bank. Different CHR bank = different visual theme. | **Tileset switching works** |
| 17-20 | Player character (from Dash, refined) | Running, jumping, shooting — same PPU fundamentals, now on MMC3 | Player in MMC3 context |
| 21-24 | Scrolling within rooms | Some rooms are wider than one screen. Horizontal scroll (from Dash) within a room boundary. | Room-internal scrolling |
| 25-28 | Room connections | Walk to room edge → load new room data → transition. No scroll between rooms (instant swap or brief fade). | Room transitions |
| 29-32 | 10 connected rooms | A small section of the Crystal Hollows. Walk between rooms. Different tile arrangements. | Explorable area |

**Phase 2 (Units 33-64): Scanline Counter**

The MMC3's scanline counter is the feature that separates it from simpler mappers.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 33-36 | Scanline IRQ setup | $C000 (latch), $C001 (reload), $E000 (disable), $E001 (enable) | Counter configured |
| 37-40 | HUD split | IRQ fires at scanline 32. Above: fixed HUD (health, missiles, map). Below: scrolling game area. | **Split-screen HUD** |
| 41-44 | HUD content | Health bar (heart tiles), missile count, mini-map indicator, ability icons | Status display |
| 45-48 | Scroll independence | HUD nametable area doesn't scroll. Game area below scrolls normally. PPUSCROLL set in IRQ handler. | Fixed HUD + scrolling game |
| 49-52 | CHR swap mid-frame | Change CHR bank in the IRQ handler: HUD uses one tileset, game area uses another. | Mixed tilesets per frame |
| 53-56 | Water reflection effect | Second scanline IRQ at the "water line": below this, flip scroll direction for a reflection. | Visual effect via IRQ |
| 57-60 | Sprite 0 as backup | Sprite 0 hit ($2002 bit 6) for timing-critical effects when scanline counter isn't precise enough. | Dual timing systems |
| 61-64 | Performance and stability | IRQ handler must be fast (~100 cycles). Test for timing conflicts with NMI. Edge cases. | Robust IRQ system |

**Key Teaching Moment (Units 37-40):**
The scanline counter fires an IRQ after N scanlines. Set N to 32 → the IRQ fires at the bottom of the HUD. In the handler: change PPUSCROLL to the game camera position. Above the IRQ: PPUSCROLL is 0 (HUD stays fixed). Below: PPUSCROLL follows the player. One hardware feature creates a professional split-screen display. Nearly every late-era NES game uses this.

**End of Phase 2:** MMC3 with PRG/CHR switching and scanline-driven HUD split. The mapper is mastered.

---

## Phase 3-4: The World (Units 65–128)

**Phase 3 (Units 65-96): World Structure**

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 65-72 | Room data format | Per-room: metatile grid, enemy list, door connections, flags (save point, boss, item). PRG bank per region. | Data-driven rooms |
| 73-80 | Region 1: Crystal Hollows | 40+ rooms. Bioluminescent theme (blue/green palette). Crystal terrain, water pools, tight tunnels. | First region |
| 81-88 | Doors and transitions | Doors connect rooms. Transition: brief fade, load new room data (possibly from different PRG bank), fade in. | Seamless world |
| 89-96 | Save rooms | Special rooms with a save point. Interact → write state to SRAM. Restore health. | Save system |

**Phase 4 (Units 97-128): Abilities**

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 97-100 | Wall jump | Touch a wall while airborne → press jump to kick off. Opens vertical shafts. | Movement upgrade |
| 101-104 | Charge beam | Hold fire button → charge builds (sprite flicker) → release for powerful shot. Breaks charge blocks. | Weapon upgrade |
| 105-108 | Missiles | Sub-weapon: limited ammo, high damage. Opens missile doors. Found in Crystal Hollows boss room. | Gated progression |
| 109-112 | Morph ball | Press down twice → player shrinks to 8×8. Fits through 1-tile gaps. New sprite set. | **Movement paradigm shift** |
| 113-116 | Bombs (morph mode) | In morph mode: press fire → drop bomb. Explodes after 2 seconds. Breaks bomb blocks. Self-boost (bomb jump). | Morph offensive ability |
| 117-120 | Double jump | Second jump in mid-air. Opens high ceilings. Found in Region 2. | Vertical expansion |
| 121-124 | Dash | Press a button → burst of horizontal speed. Pass through dash blocks. Found in Region 3. | Horizontal expansion |
| 125-128 | Ability gating audit | Map every room: which abilities are needed to reach it? Verify the progression is solvable in the intended order. Also verify no softlocks. | Design validation |

**Key Teaching Moment (Units 109-112):**
Morph ball changes everything. The player's collision box shrinks from 16×24 to 8×8. The sprite set swaps (CHR bank switch for the player's sprites). Movement physics change (no jumping, roll instead of walk). One ability transforms how the player interacts with every room they've already visited — old rooms reveal new paths. This is the core Metroidvania insight: abilities don't just add power, they redefine the world.

**End of Phase 4:** 8 abilities that progressively open the world. The explore-acquire-backtrack loop works.

---

## Phase 5-8: Regions and Combat (Units 129–256)

**Phase 5 (Units 129-160): Regions 2-3**
- **Region 2: Glacial Rift** — 40+ rooms. Ice physics (sliding), frozen enemies, blue/white palette. Boss: Frost Wurm.
- **Region 3: Abandoned Works** — 40+ rooms. Mechanical enemies, conveyor belts, grey/orange palette. Boss: Security Core.

**Phase 6 (Units 161-192): Regions 4-5**
- **Region 4: Molten Abyss** — 40+ rooms. Lava (damage floor), heat shimmer palette effect, red/orange. Boss: Magma Leviathan.
- **Region 5: Gate Chamber** — 20+ rooms. All tile types, all enemy types, dark palette with rift glow. Final boss: The Abyssal.

**Phase 7 (Units 193-224): Boss Design**
- 5 region bosses + 5 mini-bosses. Each grants an ability or upgrade.
- Multi-phase state machines. Bosses use 4-8 sprites (multiplexed if needed at the same Y position).
- Boss arenas: fixed rooms with no scrolling. Scanline IRQ provides the HUD above.
- Weak points, telegraphed attacks, learnable patterns. Tough but fair.

**Phase 8 (Units 225-256): Enemy Variety**
- 15+ enemy types across 5 regions. Region-specific: crystal crawlers, ice bats, robot drones, magma slugs, shadow wraiths.
- Enemy spawning from room data. Enemies respawn when the player re-enters a room.
- Bullet patterns: aimed, spread, homing (varies by enemy type and region).
- Sprite limit management: 8-per-scanline limit. Flicker cycling for fairness. Priority: player > player bullets > nearest enemies.

**End of Phase 8:** 200+ rooms across 5 regions. 5 bosses, 5 mini-bosses, 15+ enemy types. Content-complete.

---

## Phase 9-10: Map and Saves (Units 257–320)

**Phase 9 (Units 257-288): Map System**
- Pause screen shows a grid map of all rooms (á la Super Metroid, but NES-scale).
- Fog of war: rooms start grey. Visited rooms fill in with their region colour.
- Player position: blinking dot on the map. Save points: distinct marker.
- Item locations: revealed if the player has collected a region's map item.
- Map data stored compactly: 1 bit per room (visited/not) = ~25 bytes for 200 rooms.

**Phase 10 (Units 289-320): Battery SRAM Saves**
- 3 save slots. Each stores: player position, health, abilities acquired, missiles, bombs, map exploration bits, boss defeat flags, item collection flags.
- ~128 bytes per save slot. Save at save points. Auto-save on boss defeat.
- Completion percentage calculated from items collected + map explored + bosses defeated.
- Save file selection on title screen with completion percentage shown per slot.

**End of Phase 10:** Full map system and battery save. The player can track their exploration and resume across sessions.

---

## Phase 11-12: Audio (Units 321–384)

**Phase 11 (Units 321-352): APU Music**
- Per-region themes: Crystal Hollows (ethereal, echoing), Glacial Rift (sparse, crystalline), Abandoned Works (mechanical, rhythmic), Molten Abyss (intense, driving), Gate Chamber (ominous, building).
- Boss theme: intense, different from region themes.
- Title theme, save room theme, item acquisition jingle, boss defeat fanfare.
- NMI-driven sequencer (from Wyrdstone, expanded).

**Phase 12 (Units 353-384): DMC and SFX**
- DMC bass drum for boss encounters and intense moments.
- DMC impact sample for charge beam and missile hits.
- Sound effects: jump, land, wall-kick, dash, morph, charge, shoot, missile, damage, door, save, item collect.
- SFX temporarily steal pulse channel 2. Music continues on pulse 1 + triangle + noise.
- Audio adapts to region: reverb simulation (brief echo notes) in Crystal Hollows, metallic ring in Abandoned Works.

**End of Phase 12:** Atmospheric per-region soundtrack with DMC bass. Every action has audio feedback.

---

## Phase 13-14: Design Depth (Units 385–448)

**Phase 13 (Units 385-416): Sequence Breaking**
- The intended path: Crystal Hollows → Glacial Rift → Abandoned Works → Molten Abyss → Gate Chamber.
- Deliberate sequence breaks: skilled players can reach Region 3 before Region 2 using advanced bomb-jumping. This is designed in, not a bug.
- Softlock prevention: verify no combination of out-of-order abilities can trap the player.
- Speedrun consideration: the fastest route through the game skips optional items. Design this route to be satisfying.

**Phase 14 (Units 417-448): Multiple Endings**
- Ending 1 (under 40% completion): escape, but the gate stays open. Brief ending.
- Ending 2 (40-90% completion): gate closes, but the ruins remain. Standard ending with credits.
- Ending 3 (90%+ completion): gate closes, ruins restored, extended ending sequence with full story.
- Completion percentage gates the ending. Rewards thorough exploration without punishing casual play.

**End of Phase 14:** Sequence-break-aware design, 3 endings, speedrun-viable routing. Deep replayability.

---

## Phase 15-16: Production (Units 449–512)

**Phase 15 (Units 449-480): Polish**
- Palette effects: region-specific palette cycling (water shimmer, lava pulse, gate glow).
- Screen shake on boss hits and explosions.
- Parallax via scanline IRQ: background layer in certain rooms scrolls at half speed.
- Transition effects: region-border rooms have a visual shift (palette fades between region colours).
- NTSC/PAL detection and adaptation.

**Phase 16 (Units 481-512): Ship It**

| Unit | You Add | Result |
|------|---------|--------|
| 481-484 | Title screen with animated gate effect | Presentation |
| 485-488 | Three ending sequences implemented and tested | Narrative reward |
| 489-492 | Completion percentage display on save select and ending | Replay incentive |
| 493-496 | Time tracking (optional speedrun clock) | Speedrun community |
| 497-504 | Final testing: all regions, all abilities, all bosses, all endings, both save and no-save paths | Release quality |
| 505-508 | ROM image: iNES header, MMC3 banks, valid .nes file | Distribution |
| 509-512 | **Complete game** | **Ship it** |

---

## Technical Notes

### MMC3 Bank Layout

```
PRG-ROM (256KB = 16 × 16KB pages, or 32 × 8KB pages):
  Banks 0-5: Region data (room layouts, enemy data) — 1-2 banks per region
  Banks 6-9: Game engine code (movement, combat, abilities, PPU routines)
  Banks 10-13: Music data, sound engine, DMC samples
  Banks 14-15: Fixed bank (NMI, reset, IRQ handlers, lookup tables)

CHR-ROM (128KB = 16 × 8KB pages):
  Pages 0-4: Region tilesets (background) — one per region
  Pages 5-7: Shared tilesets (HUD, text, common elements)
  Pages 8-12: Sprite tilesets — player, enemies per region, bosses
  Pages 13-15: Boss sprites, effects, title screen
```

### Scanline IRQ for HUD

```asm
; Set up MMC3 scanline counter for HUD split at line 32
setup_hud_irq:
    lda #32
    sta $C000           ; Set scanline latch
    sta $C001           ; Reload counter
    sta $E001           ; Enable IRQ

; IRQ handler
irq_handler:
    pha
    ; Acknowledge IRQ
    sta $E000           ; Disable (acknowledge)
    sta $E001           ; Re-enable for next frame

    ; Set scroll for game area (below HUD)
    lda camera_x
    sta $2005           ; X scroll
    lda camera_y
    sta $2005           ; Y scroll

    ; Optionally switch CHR bank for game area tiles
    lda #0
    sta $8000           ; Select CHR bank register 0
    lda region_chr_bank
    sta $8001           ; Set region-specific tileset

    pla
    rti
```

### Room Data Format

```
Per room (variable length, ~40-80 bytes compressed):
  Header: 4 bytes
    - Width (1-2 screens), Height (1-2 screens)
    - Region ID (determines CHR bank and palette)
    - Flags: save_point, boss_room, item_room, dark_room
  Metatile grid: width × height × 1 byte (metatile index)
    - RLE compressed
  Door list: N × 4 bytes
    - Direction (N/S/E/W/up/down)
    - Target room ID (16-bit)
    - Target door index
  Enemy list: N × 3 bytes
    - Type, X, Y
  Item list: N × 3 bytes
    - Type, X, Y (0 if already collected — check save data)
```

### Ability Flags

```
One byte in zero page:
  Bit 0: Wall jump
  Bit 1: Charge beam
  Bit 2: Missiles
  Bit 3: Morph ball
  Bit 4: Bombs
  Bit 5: Double jump
  Bit 6: Dash
  Bit 7: (reserved — grapple? x-ray?)

Room gating: each door can require specific ability bits.
  Door flag byte AND ability byte = door flag byte → passable
```

---

## The NES Arc

| Game | Mapper | Key technique | World scale |
|------|--------|--------------|-------------|
| Dash | NROM (0) | PPU, scrolling | Linear platformer |
| Wyrdstone | NROM/UNROM | Screen transitions, SRAM | 64-screen overworld + 5 dungeons |
| Abyssal Gate | MMC3 (4) | Bank switching, scanline IRQ | 200+ room connected world |

Each game multiplies the world size. Dash is a corridor. Wyrdstone is a map. Abyssal Gate is a labyrinth.

---

## Changelog

- **v1.0 (2026-03-09):** Initial outline. New Game 3 for the restructured NES assembly track. Metroidvania with MMC3 mapper, ability gating, and 200+ connected rooms.
