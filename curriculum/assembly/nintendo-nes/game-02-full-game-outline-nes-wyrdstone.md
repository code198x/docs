# Full Game Outline: NES Wyrdstone (256 Units)

**Game:** Wyrdstone (Game 2)
**Units:** 256 (8 phases × 32 units)
**Genre:** Top-down adventure
**Inspired by:** The Legend of Zelda, StarTropics, Crystalis
**Target Quality:** Commercial-grade adventure (1987–89 era)

---

## Premise

The Wyrdstones are cracking. Five ancient stones that hold the land together — each in a different dungeon, each guarded by a creature drawn to the stone's power. The overworld is fracturing: rifts open in the ground, villages fall silent, monsters emerge from the earth. You're a villager with a sword and not much else. Find the dungeons. Defeat the guardians. Restore the stones before the land tears itself apart.

This is Zelda territory: an overworld to explore, dungeons to conquer, items to find, and a world that opens as your abilities grow. The NES was built for this — nametable screen transitions, battery SRAM for saves, and a tile system that makes top-down worlds natural.

---

## Why This Game

The Legend of Zelda proved the NES could sustain entire worlds. It introduced concepts that define game design to this day: overworld/dungeon duality, progressive item gating, battery-backed saves.

Wyrdstone teaches:
- **Screen-transition scrolling** — push-scroll between screens (different from Dash's continuous scroll)
- **Overworld structure** — a grid of screens forming a navigable map
- **Dungeon structure** — separate tileset, room-based layout, locked doors, boss rooms
- **Battery-backed SRAM** ($6000-$7FFF) — persistent save files
- **Real-time combat** — melee and ranged, with enemy AI variety
- **Item gating** — items found in dungeons unlock new overworld areas
- **HUD via nametable** — status display using background tiles, not sprites
- **Palette animation** — water shimmer, torch flicker, magical effects

---

## 6502 Progression

| Phase | 6502/NES Focus |
|-------|---------------|
| 1 (Overworld) | Screen transitions, nametable management, overworld data format |
| 2 (Combat) | Melee hitbox, enemy AI, knockback physics, health system |
| 3 (Dungeons) | Tileset switching, room-based layout, locked doors, keys |
| 4 (Items) | Inventory system, item-gated progression, sub-weapons |
| 5 (Guardians) | Boss state machines, multi-sprite entities, arena design |
| 6 (Sound) | APU music engine, per-area themes, SFX priority |
| 7 (World) | 5 dungeons, full overworld, battery SRAM saves |
| 8 (Release) | Palette effects, NTSC/PAL, high scores, distribution |

---

## Phase 1: Overworld (Units 1–32)

**Goal:** Explorable overworld with screen transitions and player movement.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 1-4 | Single screen with background tiles | PPU nametable setup (review from Dash), new tileset for top-down view | Overworld screen |
| 5-8 | Player character (4-directional sprite) | OAM setup, 4-directional walk animation, sprite flip | Player walks around |
| 9-12 | Screen transitions | Walk to screen edge → push-scroll to adjacent screen (PPU scroll + nametable swap) | **World opens up** |
| 13-16 | Overworld data | Grid of screens (8×8 = 64 screens). Each screen: 16×15 metatiles + connections. | Explorable map |
| 17-20 | Terrain collision | Solid tiles (rocks, trees, water) block movement. Metatile collision flags. | Can't walk through trees |
| 21-24 | Terrain variety | Grass, forest, mountain, water, sand, path tiles. Overworld feels like a real landscape. | Visual variety |
| 25-28 | NPCs | Standing characters in villages. Walk up → text box overlay. Brief dialogue ("The dungeon lies to the north.") | World has people |
| 29-32 | Text display system | PPU nametable overlay for text boxes. Character-by-character display. Button to dismiss. | Text engine |

**Key Teaching Moment (Units 9-12):**
Screen-transition scrolling is different from Dash's continuous scroll. The player walks to the edge; the screen push-scrolls to the adjacent screen over ~16 frames. During the transition, both nametables are visible (the NES has two). The new screen is written to the off-screen nametable, then PPUSCROLL sweeps across. This is how Zelda's overworld works.

**End of Phase 1:** An overworld of 64 screens connected by push-scroll transitions. Villages with NPCs. The world feels large.

---

## Phase 2: Combat (Units 33–64)

**Goal:** Real-time sword combat with enemy variety.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 33-36 | Sword swing | B button → sword sprite extends from player in facing direction for ~8 frames | Melee attack |
| 37-40 | Sword hitbox | Check if any enemy sprite overlaps the sword sprite. Damage on overlap. | Enemies take hits |
| 41-44 | Enemy: Slime | Basic enemy: moves randomly, damages player on contact. 1 HP. | First enemy |
| 45-48 | Enemy: Skeleton | Patrols a path, faster than slime. 2 HP. Knockback on hit. | Tougher enemy |
| 49-52 | Enemy: Archer | Stationary, fires projectile at player every N frames. Projectile is a sprite. | Ranged threat |
| 53-56 | Player health | Heart-based health (8 half-hearts = 4 full). Heart display in HUD (nametable tiles). | Health system |
| 57-60 | Knockback | Player and enemies bounce apart on contact. Brief invincibility frames (sprite flicker). | Fair combat |
| 61-64 | Enemy drops | Killed enemies drop hearts (health), rupees (currency), or keys (dungeon). Drops are sprites. | Loot |

**End of Phase 2:** Real-time combat with 3 enemy types, health, knockback, and drops. Feels like Zelda.

---

## Phase 3: Dungeons (Units 65–96)

**Goal:** First dungeon with room-based layout, locked doors, and a boss.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 65-68 | Dungeon tileset | Swap CHR bank (or use different pattern table half). Stone walls, floor, doors. | Dungeon visuals |
| 69-72 | Room-based layout | Dungeon is a grid of rooms. Transition between rooms (similar to overworld screens). | Dungeon structure |
| 73-76 | Locked doors | Some doors require a key. Key consumed on use. Multiple key colours (small keys + boss key). | Gated progression |
| 77-80 | Dungeon map item | Found in the dungeon: reveals room layout on the pause screen. | Navigation aid |
| 81-84 | Puzzle elements | Push blocks onto switches → door opens. Floor buttons triggered by standing on them. | Environmental puzzles |
| 85-88 | Dungeon enemies | Dungeon-specific enemies (bats, worms, armoured knights). Harder than overworld. | Dungeon threat level |
| 89-92 | Mini-boss | Mid-dungeon room with a tougher enemy. Drops a key or item. | Mid-dungeon challenge |
| 93-96 | Dungeon 1 boss | Multi-sprite boss with pattern (charge → rest → charge). Weak to sword during rest. Drops first Wyrdstone. | **First dungeon complete** |

**Key Teaching Moment (Units 65-68):**
The NES PPU has two pattern tables (CHR banks): one for background tiles, one for sprites. Switching to a different CHR bank gives a completely different tileset. On NROM (Dash), this is fixed. For Wyrdstone, we can use the second pattern table half, or prepare for the mapper upgrade in Abyssal Gate. The visual shift from green overworld to grey dungeon uses palette changes + different tile arrangements within the same CHR.

**End of Phase 3:** First complete dungeon with rooms, locked doors, puzzles, enemies, and a boss. The first Wyrdstone is recovered.

---

## Phase 4: Items (Units 97–128)

**Goal:** Inventory, sub-weapons, item-gated progression.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 97-100 | Item screen | Press Select → overlay shows collected items. Cursor selects active sub-weapon. | Inventory UI |
| 101-104 | Boomerang | Sub-weapon: thrown in facing direction, returns. Stuns enemies. Found in Dungeon 1. | First sub-weapon |
| 105-108 | Bomb | Sub-weapon: placed on ground, explodes after 2 seconds. Destroys cracked walls. | Destructible environment |
| 109-112 | Cracked walls on overworld | Bomb reveals hidden caves → new overworld areas accessible. Item gates world. | **Item-gated exploration** |
| 113-116 | Shield upgrade | Found in Dungeon 2. Reduces damage by half. | Defensive progression |
| 117-120 | Hookshot/raft | Found in Dungeon 3. Crosses water gaps on overworld. Opens new regions. | Movement upgrade |
| 121-124 | Dungeon 2: complete | Forest theme. New enemies. Boss: giant spider. Drops Wyrdstone 2. | Second dungeon |
| 125-128 | Dungeon 2 tested and balanced | Full playthrough of overworld exploration + 2 dungeons. | Content milestone |

**End of Phase 4:** Two dungeons complete. Inventory with sub-weapons. Item-gated overworld expansion. The game has the explore-find-unlock loop.

---

## Phase 5: Guardians (Units 129–160)

**Goal:** Dungeons 3-5, boss variety, and the endgame.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 129-136 | Dungeon 3: Waterfall Cavern | Water theme, current hazards, raft/hookshot used inside. Boss: water serpent. | Third dungeon |
| 137-144 | Dungeon 4: Fire Temple | Lava tiles (damage on contact), fire-themed enemies. Boss: flame knight. | Fourth dungeon |
| 145-152 | Dungeon 5: The Rift | Dark rooms (need lantern item), crumbling floors, mixed enemies. Final boss: the Rift Guardian. | Final dungeon |
| 153-156 | Wyrdstone restoration | All 5 stones → final overworld area unlocks → ultimate encounter | Endgame |
| 157-160 | Balance: dungeon difficulty curve | Dungeon 1 gentle, Dungeon 5 demanding. Item progression opens later dungeons. | Balanced progression |

**End of Phase 5:** 5 dungeons, 5 bosses, 5 Wyrdstones. The full adventure is playable.

---

## Phase 6: Sound (Units 161–192)

**Goal:** APU music engine, per-area themes.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 161-168 | APU music engine | NMI-driven note sequencer. Pattern data format. 2 pulse + triangle + noise. | Music framework |
| 169-176 | Themes | Overworld, dungeon, boss, village, title, game over. Each 16-32 bars. | Musical variety |
| 177-184 | SFX | Sword, hit, collect, door open, boss damage, death. Temporarily steal a channel. | Sound effects |
| 185-192 | DMC introduction | Bass drum or impact sample via DMC channel ($4010-$4013). First sampled audio. | DMC basics |

**Key Teaching Moment (Units 185-192):**
The DMC (Delta Modulation Channel) plays 1-bit delta-encoded samples. It's limited — low sample rate, quiet, buzzy — but it adds a bass punch that the other channels can't match. Commercial NES games used DMC for bass drums, voice clips, and impact sounds. This is the introduction; Abyssal Gate and the capstone will use it more extensively.

**End of Phase 6:** Full APU soundtrack with per-area themes, sound effects, and DMC bass. Sounds like a real NES game.

---

## Phase 7: World (Units 193–224)

**Goal:** Battery SRAM saves, full overworld, secrets.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 193-196 | Battery SRAM | Write game state to $6000-$7FFF. Persists across power cycles. | **Save game** |
| 197-200 | Save/load system | 3 save slots. Player selects on title screen. Save on pause menu. | Multiple saves |
| 201-204 | Save data format | Position, health, items, dungeon completion flags, rupees. ~64 bytes per slot. | Compact save state |
| 205-208 | Full overworld | 64 screens with terrain variety: villages, forests, mountains, desert, coast, ruins. | Complete world |
| 209-212 | Secret caves | Bomb-able walls on overworld reveal hidden caves with hearts, rupees, item upgrades. | Exploration reward |
| 213-216 | Heart containers | 5 hidden heart containers increase max health. Reward thorough exploration. | Capacity upgrades |
| 217-220 | Shops | Village NPCs sell items (arrows, bombs, potions) for rupees. | Economy |
| 221-224 | Overworld enemies per area | Different enemy types per terrain: slimes on grass, skeletons in ruins, bats in forest. | Regional variety |

**End of Phase 7:** Full overworld, 5 dungeons, battery SRAM saves, secrets, shops. A complete Zelda-scale adventure.

---

## Phase 8: Release (Units 225–256)

**Goal:** Commercial polish, distribution.

| Unit | You Add | 6502 Skill | Result |
|------|---------|------------|--------|
| 225-228 | Title screen | "WYRDSTONE" with animated tile effects. Save file selection with cursor. | Presentation |
| 229-232 | Ending sequence | Final Wyrdstone restored → rifts close → overworld heals → credits roll | Narrative closure |
| 233-236 | Palette effects | Water shimmer (palette cycling on water tiles). Torch flicker in dungeons. Magical glow on Wyrdstones. | Visual polish |
| 237-240 | Minimap | Pause screen shows overworld position and dungeon map (if map item collected). | Navigation |
| 241-244 | Second quest | After completion: harder version with remixed dungeon layouts and enemy placements. | Replayability |
| 245-248 | NTSC/PAL detection | Frame timing adjustment, music tempo correction | Compatibility |
| 249-252 | Final testing | All dungeons, all items, all saves, both quests | Release quality |
| 253-256 | **ROM image** | iNES header, PRG/CHR banks, valid .nes file that runs on hardware | **Ship it** |

---

## Technical Notes

### Screen Transition Scrolling

```asm
; Push-scroll from screen A to screen B (rightward)
;
; 1. Write screen B's nametable to the off-screen nametable
; 2. Over 16 frames, increment PPUSCROLL X from 0 to 256
; 3. At frame 16, swap which nametable is "current"

transition_right:
    ; Prepare: write screen B into nametable 1 (while nametable 0 is displayed)
    jsr load_screen_to_nametable1

    ; Scroll across 16 frames (16 pixels per frame = 256 pixels total)
    lda #0
    sta scroll_x
.scroll_loop:
    ; Wait for NMI
    jsr wait_nmi
    ; Increment scroll
    lda scroll_x
    clc
    adc #16
    sta scroll_x
    ; Set PPUSCROLL
    lda scroll_x
    sta $2005           ; X scroll
    lda #0
    sta $2005           ; Y scroll (unchanged)
    ; Check if complete
    lda scroll_x
    bne .scroll_loop

    ; Done: now nametable 1 is the displayed screen
    ; Swap active nametable tracking
    ...
```

### Battery SRAM

```asm
; Save game state to SRAM ($6000-$7FFF)
; Battery on the cartridge keeps SRAM powered when NES is off

save_game:
    ldx current_slot        ; 0, 1, or 2
    ; Calculate SRAM offset: slot × 64
    txa
    asl
    asl
    asl
    asl
    asl
    asl                     ; A = slot × 64
    clc
    adc #<$6000
    sta ptr_lo
    lda #>$6000
    adc #0
    sta ptr_hi

    ; Write save data
    ldy #0
    lda player_x
    sta (ptr_lo),y
    iny
    lda player_y
    sta (ptr_lo),y
    iny
    lda player_screen
    sta (ptr_lo),y
    ; ... health, items, dungeon flags, rupees
    rts
```

### Metatile Collision

Each metatile (2×2 tiles = 16×16 pixels) has a collision type:

```
0 = passable (grass, floor)
1 = solid (wall, rock, tree)
2 = water (impassable without raft)
3 = damage (lava, spikes)
4 = door (transitions to dungeon/room)
5 = pushable (push block)
6 = breakable (bomb-able wall)
```

Collision check: convert player's pixel position to metatile coordinates, look up the type in the screen's metatile grid.

### Memory Map (NROM — 32KB PRG + 8KB CHR)

```
PRG-ROM:
$8000-$9FFF: Game engine (movement, combat, PPU routines)
$A000-$BFFF: Dungeon data + enemy data
$C000-$DFFF: Overworld data (64 screens compressed) + music
$E000-$FFFF: NMI handler, reset, IRQ, lookup tables, text

CHR-ROM:
$0000-$0FFF: Background tiles (overworld + dungeon — shared)
$1000-$1FFF: Sprite tiles (player, enemies, items, effects)

SRAM:
$6000-$60BF: Save slot 0 (64 bytes)
$60C0-$617F: Save slot 1
$6180-$623F: Save slot 2
$6240-$7FFF: Scratch space
```

32KB PRG is tight for 64 overworld screens + 5 dungeons + music + engine. Compression is essential: metatile-based screens (~30 bytes per screen), RLE on dungeon rooms, compact music format. If 32KB isn't enough, Wyrdstone can use UNROM (mapper 2) for bank-switched PRG — a minor step before Abyssal Gate's MMC3.

---

## The NES Arc (So Far)

| Game | Mapper | Key technique | Scale |
|------|--------|--------------|-------|
| Dash | NROM (0) | PPU fundamentals, horizontal scrolling | Single-path platformer |
| Wyrdstone | NROM/UNROM (0/2) | Screen transitions, SRAM saves, combat | Open-world adventure |

Dash teaches the PPU. Wyrdstone teaches what you build with it: a world.

---

## Changelog

- **v1.0 (2026-03-09):** Initial outline. New Game 2 for the restructured NES assembly track. Top-down adventure with battery SRAM saves.
