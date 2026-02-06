# Phase 7: The Deep

**Game:** Shadowkeep (ZX Spectrum Game 1)
**Units:** 97–112
**Theme:** Darkness, atmosphere, and boss encounters
**Z80 Focus:** Advanced attribute manipulation, complex state machines, distance calculations
**Hardware:** BRIGHT/FLASH for atmospheric effects, 128K memory paging
**Status:** Planned

---

## Overview

Phase 7 transforms the keep from a maze into an experience. The signature mechanic is darkness: only cells near the player are visible. Beyond the light radius, attributes are set to black-on-black — walls and items invisible until approached. A torch item expands the radius. FLASH creates flickering torchlight at the edges. The keep becomes atmospheric.

Boss encounters appear: larger, pattern-based enemies that guard critical rooms. Unlike patrol enemies, bosses have health bars, telegraphed attacks, and multiple phases. Defeating a boss unlocks a new area or grants a unique item.

Special items add depth: a speed potion, an invisibility cloak (enemies ignore the player briefly), a magic map (reveals all rooms). These use timers and state flags that build on earlier patterns but combine them in new ways.

---

## Prerequisites from Phase 6

- Interrupt mode 2 — game timing and music playback
- AY control — atmospheric audio for dark rooms and boss encounters
- FRAMES system variable — timer-based effects
- Complete attribute/UDG system — Phase 7 manipulates attributes dynamically

---

## Unit Progression

| Unit | Title | New Z80 Concept | Game Addition |
|------|-------|----------------|---------------|
| 97 | Fog of War | Set distant attributes to black-on-black | **Limited visibility** |
| 98 | Light Radius | Calculate distance from player, reveal nearby cells | See 3 cells around player |
| 99 | Torch Item | Expands light radius to 5 cells when held | Exploration aid |
| 100 | Flickering Light | FLASH bit on radius edge creates torchlight effect | **Atmospheric edges** |
| 101 | Dark Room Enemies | Enemies visible only within light radius | Surprise encounters |
| 102 | Boss Enemy Design | Larger entity (2×2 characters), health system | Imposing guardian |
| 103 | Boss Movement Pattern | Telegraphed attacks: pause → charge → recover | Learnable pattern |
| 104 | Boss Health Bar | Character-based bar, depletes on hits | Visible progress |
| 105 | Boss Phase 2 | Pattern change at 50% health, faster/new attack | Escalation |
| 106 | Boss Defeat | Room reward unlocked, victory fanfare | Triumph |
| 107 | Secret Walls | Walk into specific walls to pass through | **Hidden passages** |
| 108 | Traps | Floor tiles that trigger on step (spikes, pits) | Careful navigation |
| 109 | Magic Items | Speed potion, invisibility cloak, magic map | Special powers |
| 110 | Item Combination | Use key + gem to unlock final area | Puzzle depth |
| 111 | 128K Extra Rooms | Additional rooms loaded via memory paging ($7FFD) | Bonus content |
| 112 | Integration + Balance | Darkness tuning, boss fairness, item placement | Atmospheric and fair |

---

## Key Teaching Moments

### Fog of War via Attributes (Unit 97)

Darkness is pure attribute manipulation. At the start of each frame, set all room attributes to INK 0 / PAPER 0 (black on black). Then, for each cell within the light radius, restore the original attribute from the room buffer. The bitmap data stays in screen memory — only the attributes change. This means the "hidden" graphics are still there; they're just invisible because INK and PAPER are the same colour. Revealing a cell is a single attribute write, not a screen redraw.

### Distance Calculation (Unit 98)

The light radius needs Manhattan distance: `|player_x - cell_x| + |player_y - cell_y|`. The Z80 has no absolute value instruction, so negative results from `SUB` are detected via the carry flag and negated with `NEG`. Comparing the sum against the radius threshold determines visibility. This pattern — distance calculation with conditional negation — appears throughout game programming.

### Boss as Multi-Character Entity (Unit 102)

A 2×2 character boss occupies four attribute cells. Movement means updating four positions. Collision detection checks four cells. The boss's state machine manages: idle → telegraph → attack → recover → idle. Telegraphing (the boss flashes or pauses before attacking) gives the player time to react — fair but tense.

### 128K Memory Paging (Unit 111)

The 128K Spectrum has 8 RAM pages of 16KB each, but only 4 are visible at once. Port $7FFD selects which page appears at $C000–$FFFF. Extra rooms, graphics, or music data can live in banked RAM — paged in when needed. The write-and-verify pattern ensures the page switch worked. This is the learner's first encounter with bank switching.

---

## Z80 Concepts Introduced

1. Dynamic attribute manipulation — bulk set/restore per frame (Unit 97)
2. Manhattan distance — `SUB` / `NEG` / `ADD` for radius check (Unit 98)
3. `NEG` — negate accumulator for absolute value (Unit 98)
4. Multi-cell entity — 2×2 character boss with coordinated movement (Unit 102)
5. Telegraph pattern — timer-based state with visual warning (Unit 103)
6. Memory paging — port $7FFD for 128K bank selection (Unit 111)
7. Secret tile detection — specific attribute value treated as passable wall (Unit 107)
8. Trap trigger — step detection via position check against trap table (Unit 108)

---

## Hardware

### New in Phase 7

| Port/Resource | Purpose | Introduced |
|---------------|---------|-----------|
| `$7FFD` | 128K memory paging register | Unit 111 |
| FLASH bit (attribute bit 7) | Flickering torchlight effect | Unit 100 |

### Attribute Techniques

| Technique | Effect | How |
|-----------|--------|-----|
| Black-on-black | Hidden cell (fog) | INK 0, PAPER 0 |
| FLASH on edge | Flickering torchlight | Set bit 7 on radius boundary |
| BRIGHT on items | Glowing collectibles | Set bit 6 (existing) |
| Restore from buffer | Reveal cell | Copy original attribute byte |

---

## Game State at Phase End

After Unit 112:

- **Fog of war** — only nearby cells visible, darkness beyond
- **Torch item** — expands visibility radius from 3 to 5 cells
- **Flickering light** — FLASH on radius edges creates torchlight atmosphere
- **Boss encounters** — 2×2 character bosses with health bars and two phases
- **Boss telegraph** — attacks are telegraphed, giving time to react
- **Secret walls** — hidden passages reward exploration
- **Traps** — floor hazards require careful movement
- **Magic items** — speed, invisibility, map reveal
- **128K bonus rooms** — extra content for 128K players
- **Item combination** — use two items together to unlock final area

The keep is atmospheric and dangerous. Darkness creates tension. Bosses create drama. Secrets reward curiosity.

---

## What Carries to Phase 8

- **128K paging** — extra content and high score persistence
- **Complex state machines** — menu systems, attract mode, difficulty settings
- **Complete game systems** — all mechanics in place, Phase 8 polishes and packages
- **Dynamic attribute work** — title screen effects, attract mode visuals

---

**Version:** 1.0
**Last Updated:** 2026-02-06
