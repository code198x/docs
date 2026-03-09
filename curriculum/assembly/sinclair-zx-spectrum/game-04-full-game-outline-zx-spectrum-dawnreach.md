# Full Game Outline: ZX Spectrum Dawnreach (512 Units)

**Game:** Dawnreach (Game 4 — Capstone)
**Units:** 512 (16 phases × 32 units)
**Genre:** Scrolling action-platformer with exploration
**Inspired by:** Midnight Resistance, Ghosts 'n Goblins, Dan Dare III, Turrican (Spectrum)
**Target Quality:** Late-era commercial release (1989–91 era)

---

## Premise

The land beyond the mountains is dying. The sun rises later each day, sets earlier each night. A darkness is spreading from the east, and the border towns are already lost. You're a ranger from the western settlements — the last one willing to make the crossing.

Five zones stretch between you and the source of the darkness: the Greenwood (forest), the Ridgeway (mountains), the Shorelands (coast and caves), the Ashfield (burned wasteland), and the Dawnreach — the eastern tower where the light is held captive. Each zone scrolls horizontally. Each has its own terrain, enemies, and a guardian. The journey is long. The game is hard. But the dawn is waiting.

---

## Why This Is the Capstone

Dawnreach requires every technique from Games 1-3:

| Technique | Origin | Use in Dawnreach |
|-----------|--------|-----------------|
| Attribute-based collision | Gravelight | Terrain collision on scrolling backgrounds |
| Gravity and jump physics | Gravelight | Platforming on scrolling terrain |
| UDG character design | Gravelight | Player, enemies, terrain tiles |
| Software pixel scrolling | Ionfire | Horizontal scrolling landscapes |
| Contention-aware rendering | Ionfire | Frame budget management |
| Restore-under sprites | Ionfire | Multiple moving objects on scrolling bg |
| Enemy wave patterns | Ionfire | Formation attacks, boss encounters |
| Depth sorting concepts | Grimstone | Foreground/background terrain layers |
| State machines | Grimstone | Boss patterns, NPC behaviour |
| Room/level data compression | Grimstone | Level streaming, RLE tile maps |
| 128K memory paging | Grimstone | Extra zones, AY music banks |
| Interrupt-driven music | Grimstone | Background music during gameplay |

Plus the new capstone techniques:
- **Turbo tape loader** — custom loading routine, faster than ROM
- **+3 disk support** — uPD765 FDC access for +3 disk version
- **Loading screen** — displayed during tape/disk load
- **128K/48K dual-mode** — detect and adapt at startup
- **Multi-zone streaming** — zones load progressively, not all in memory
- **Professional title sequence** — attract mode, demo, high scores
- **End-to-end production** — the complete package, ready for distribution

---

## The Five Zones

| Zone | Setting | Scroll | Terrain | Enemies | Guardian |
|------|---------|--------|---------|---------|----------|
| 1: Greenwood | Dense forest | Moderate | Trees, undergrowth, streams, bridges | Wolves, spiders, archers | The Thornqueen (living tree) |
| 2: Ridgeway | Mountain pass | Slow (climbing) | Rock faces, ledges, ice, waterfalls | Eagles, rock-throwers, wind gusts | The Stoneking (avalanche golem) |
| 3: Shorelands | Coastal caves | Moderate | Cliffs, tidal caves, beach, shipwrecks | Crabs, bats, sea creatures | The Tidecaller (whirlpool entity) |
| 4: Ashfield | Burned wasteland | Fast (open ground) | Scorched earth, ruins, ember pits | Fire elementals, ash wraiths, raiders | The Ember Lord (fire titan) |
| 5: Dawnreach | The eastern tower | Vertical (climbing) | Tower interior, mechanisms, light puzzles | Shadow guards, mirror constructs | The Eclipse (darkness itself) |

Each zone has distinct PAPER/INK colour palettes:
- Greenwood: green INK, black PAPER
- Ridgeway: white/cyan INK, blue PAPER
- Shorelands: cyan/yellow INK, blue PAPER
- Ashfield: red/yellow INK, black PAPER
- Dawnreach: white/yellow INK, black→white PAPER (brightening as you climb)

Zone 5 uses vertical scrolling (the tower climb), contrasting with the horizontal scrolling of zones 1-4. The learner implements both scroll directions.

---

## Core Mechanics

### Scrolling

Horizontal pixel scrolling (from Ionfire) with level-specific scroll speeds. The Greenwood scrolls at moderate pace. The Ashfield scrolls fast (open terrain, urgent). The Ridgeway scrolls slowly (climbing, precision). Zone 5 scrolls vertically.

### Platforming

Gravity, jumping, and platform collision (from Gravelight) applied to a scrolling world. The player jumps between platforms that scroll past. Moving platforms, crumbling ledges, and ice physics from Gravelight are reused.

### Combat

The player has a ranged weapon (throwing daggers, upgradeable) and a close-range attack (sword). Enemies approach from both directions. Power-ups upgrade weapon range, speed, and type.

Weapon upgrades:
| Weapon | Range | Speed | Special |
|--------|-------|-------|---------|
| Dagger | Short | Fast | Default |
| Longbow | Long | Medium | Arcing trajectory |
| Firebolt | Medium | Fast | Passes through enemies |
| Shield | N/A | N/A | Blocks projectiles for 3 hits |

### Exploration

Each zone has a main path (scrolling left to right) and optional side areas accessible via hidden routes — caves, treetops, underwater passages. Side areas contain weapon upgrades, health, bonus crystals, and lore fragments.

### Health and Lives

Health bar (8 hits). Health drops from enemies and side areas. 3 lives. Continue from zone start on game over. Password per zone.

---

## Phase Breakdown

### Phases 1-4: The Engine (Units 1–128)

**Phase 1 (Units 1-32): Scrolling Platformer Core**

Horizontal scrolling (pixel-smooth, from Ionfire's fine/coarse technique) with platformer physics (from Gravelight) combined. The player runs and jumps through a scrolling forest.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 1-4 | Scrolling engine setup | Fine/coarse scroll from Ionfire, adapted for platformer | Scrolling landscape |
| 5-8 | Player on scrolling bg | Restore-under sprite, gravity, jumping over scrolling terrain | **Running and jumping in scrolling world** |
| 9-12 | Terrain collision | Attribute check at player's world position (scroll offset + screen position) | Platforms work while scrolling |
| 13-16 | Tile map for zone 1 | Forest tiles: trees, ground, platforms, sky. Column-based streaming. | Greenwood terrain |
| 17-20 | Variable terrain | Slopes (visual only), gaps, bridges, overhangs. Level design variety. | Interesting terrain |
| 21-24 | Enemies on scrolling bg | Enemies with world-space positions. Scroll into view, patrol, scroll out. | Enemies in the world |
| 25-28 | Combat basics | Throw dagger (projectile sprite), enemy health, enemy death | **Player can fight** |
| 29-32 | Zone 1 first half | Complete scrolling section: forest terrain, enemies, gaps, platforms. Playable. | First playable section |

**Phase 2 (Units 33-64): Combat and Exploration**

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 33-40 | Weapon upgrades | Power-up drops, weapon switch, different projectile behaviours | Arsenal |
| 41-48 | Side areas | Hidden cave entrance → non-scrolling room (like Gravelight) → return to main path | Exploration reward |
| 49-56 | Zone 1 guardian: Thornqueen | Boss arena, multi-phase pattern, health bar | **First boss** |
| 57-64 | Zone 1 complete | Full Greenwood zone: terrain, enemies, side areas, boss, zone-clear sequence | First zone done |

**Phase 3 (Units 65-96): Zone Variety**

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 65-80 | Zone 2: Ridgeway | Mountain terrain, slow scroll, ice physics, vertical sections, Stoneking boss | Second zone |
| 81-96 | Zone 3: Shorelands | Coastal terrain, tidal mechanics (water level rises/falls), Tidecaller boss | Third zone |

**Phase 4 (Units 97-128): Final Zones**

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 97-112 | Zone 4: Ashfield | Fast scroll, fire hazards, open combat, Ember Lord boss | Fourth zone |
| 113-128 | Zone 5: Dawnreach | Vertical scrolling (new direction), tower climb, The Eclipse boss | **All five zones** |

**End of Phase 4:** All 5 zones playable with terrain, enemies, side areas, and bosses. The game is content-complete. 48K playable.

---

### Phases 5-8: Audio and Polish (Units 129–256)

**Phase 5 (Units 129-160): Audio**

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 129-136 | Beeper effect library | Weapon fire, enemy hit, damage, jump, land, collect, boss | 48K audio |
| 137-144 | AY music engine | Per-zone themes (5 + boss + title + ending). Interrupt-driven. | 128K soundtrack |
| 145-152 | Zone music design | Greenwood: pastoral. Ridgeway: sparse, echoing. Ashfield: urgent. Dawnreach: hopeful, building. | Musical journey |
| 153-160 | SFX integration | Effects over music, 48K/128K detection, volume balance | Complete audio |

**Phase 6 (Units 161-192): Visual Polish**

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 161-168 | UDG polish | Player walk/jump/attack/climb animations refined. Per-zone enemy designs. | Polished graphics |
| 169-176 | Parallax | Attribute-based background layer (distant mountains/sky shift slower than foreground) | Visual depth |
| 177-184 | Zone transitions | Scroll slows, terrain fades between zones, brief title card ("THE RIDGEWAY"), new palette loads | Dramatic pacing |
| 185-192 | Weather effects | Rain in Shorelands (falling dots), wind in Ridgeway (attribute flicker), ember sparks in Ashfield | Atmospheric detail |

**Phase 7 (Units 193-224): 128K and Production**

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 193-200 | 128K zone streaming | Zones loaded from banked RAM. Only current zone in main memory. Transition loads next zone. | Memory management |
| 201-208 | 128K enhanced content | Extra side areas, more enemy types, extended boss phases | Premium experience |
| 209-216 | Double-buffered scroll | 128K: alternate screen pages for tear-free scrolling | Smooth display |
| 217-224 | 48K memory audit | All 5 zones compressed fit in 48K. Code + graphics + beeper audio. Tight but achievable. | Universal compatibility |

**Phase 8 (Units 225-256): Title and Presentation**

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 225-228 | Title screen | "DAWNREACH" with sunrise motif. Scrolling landscape demo behind the title. | Presentation |
| 229-232 | Attract mode | Automated playthrough of Greenwood opening. Shows the game running. | Demo mode |
| 233-236 | High score table | Top 5, name entry, displayed on title | Competition |
| 237-240 | Difficulty select | Easy (12 health, weak enemies), Normal (8 health), Hard (4 health, fast enemies, no continues) | Accessibility |
| 241-244 | Password system | 4-letter code per zone. Resume progress without replay. | Fairness |
| 245-248 | Ending sequence | The Eclipse defeated → darkness recedes → dawn breaks → the land heals → journey home | **Narrative reward** |
| 249-252 | Credits | Scrolling credits over sunrise | Attribution |
| 253-256 | Integration | Full playthrough, balance, edge cases | Release quality |

---

### Phases 9-12: Distribution (Units 257–384)

**Phase 9 (Units 257-288): Turbo Loader**

The standard ROM tape loader runs at ~1500 baud. A turbo loader can achieve 3000-6000 baud — halving or quartering load time. This phase builds one from scratch.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 257-264 | Tape format basics | How tape data works: pilot tone, sync, data bytes, checksum. EAR bit reading. | Tape hardware understanding |
| 265-272 | Custom loader | Replace ROM loader with custom routine. Faster timing. Edge detection via `IN A,($FE)`. | Custom tape reading |
| 273-280 | Turbo encoding | Shorter pulses = faster data. Design the pulse timing. Test on real hardware (or accurate emulator). | Turbo timing design |
| 281-288 | Loader with screen | Display loading screen while data loads. Progress bar via border colour stripes. | Loading presentation |

**Phase 10 (Units 289-320): +3 Disk Support**

The Spectrum +3 has a 3" disk drive controlled by the NEC uPD765 FDC. This phase adds disk loading as an alternative to tape.

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 289-296 | +3 DOS basics | +3DOS API calls. Load a file from disk. Faster than tape by an order of magnitude. | Disk access |
| 297-304 | Disk-based zone loading | Each zone as a separate file. Load on zone transition. Near-instant compared to tape. | Fast zone switching |
| 305-312 | Save to disk | Save high scores and progress to disk. (Tape version uses passwords instead.) | Persistent state |
| 313-320 | +3 disk image creation | Build a .DSK image with all game files. Bootable from +3. | Disk distribution |

**Phase 11 (Units 321-352): Loading Screen and Multi-Model Testing**

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 321-328 | Loading screen design | A compelling image displayed during tape/disk load. Drawn in attribute art or pixel art. | First impression |
| 329-336 | 48K testing | Full playthrough on 48K. Memory tight? Performance stable? Every feature works? | 48K validation |
| 337-344 | 128K testing | Full playthrough on 128K. AY music, extra content, double buffer all working? | 128K validation |
| 345-352 | +2/+2A/+3 testing | Different Spectrum models have timing and hardware differences. Test on all. | Multi-model QA |

**Phase 12 (Units 353-384): TAP/TZX/DSK Creation**

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 353-360 | TAP file structure | Header blocks, data blocks, checksum bytes. Build a valid TAP. | Tape format |
| 361-368 | TZX file structure | Extended format with turbo blocks, custom pilot tones. More flexible than TAP. | Enhanced tape format |
| 369-376 | Multi-load architecture | Game loads in sections: loader → title → zone 1 → zone 2 (on demand). | Staged loading |
| 377-384 | Distribution package | TAP (standard), TZX (turbo), DSK (+3). Three distribution formats. | **Triple format release** |

---

### Phases 13-16: Final Polish (Units 385–512)

**Phase 13 (Units 385-416): Balance and Content**

Full difficulty curve review. Zone 1 should be welcoming. Zone 5 should be demanding. Enemy placement, health drop frequency, platform spacing, boss patterns — all tuned across three difficulty levels. Side area rewards balanced against main-path difficulty.

**Phase 14 (Units 417-448): Narrative and Atmosphere**

Lore fragments found in side areas tell the story of the darkness — what it is, where it came from, why the tower matters. Brief text between zones advances the journey narrative. The ending is earned: not just "you won" but "the dawn returns because you made the crossing."

Atmospheric details: birds in the Greenwood (occasional chirp via beeper), wind howling in the Ridgeway, waves in the Shorelands, crackling fire in the Ashfield, silence in the Dawnreach (eerie absence of ambient sound, then — as you climb — the dawn theme builds).

**Phase 15 (Units 449-480): Final Testing**

Systematic testing matrix:
- 3 difficulty levels × 5 zones × 2 models (48K/128K) = 30 full playthroughs
- Every side area accessible
- Every boss defeatable
- Every password works
- Every distribution format loads correctly
- Loading screen displays properly
- High scores persist (128K/+3) or passwords work (48K tape)

**Phase 16 (Units 481-512): Ship It**

| Unit | You Add | Z80 Skill | Result |
|------|---------|-----------|--------|
| 481-488 | Final ending polish | Dawn breaks: PAPER transitions from black to blue to cyan to white across the final screens. The Spectrum's attribute system delivers the thematic climax. | Attribute art as narrative |
| 489-496 | Inlay card text | Game description, controls, credits — the text that would appear on the cassette inlay. | Professional documentation |
| 497-504 | Player guide | Zone descriptions, hints (not solutions), controls reference. | Player support |
| 505-510 | Final bug sweep | Last pass. Every path, every edge case, every model. | Release quality |
| 511 | Version stamp | Build number, date, credits embedded in the binary. | Professional practice |
| 512 | **The finished game** | TAP, TZX, DSK. Complete. | **Ship it** |

---

## Technical Notes

### Combining Scrolling and Platforming

The key challenge: Ionfire's scrolling engine moves the world left. Gravelight's platformer physics move the player in world space. Combining them requires:

1. **World-space coordinates** for the player and all entities. The scroll offset is a camera position, not a movement.
2. **Screen position = world position - scroll offset.** The player can move left and right relative to the scroll.
3. **Terrain collision uses world coordinates** — look up the tile at the player's world position in the tile map, not their screen position.
4. **Auto-scroll vs player-scroll**: Some sections auto-scroll (player must keep up). Others scroll when the player moves right (exploration sections).

```z80
; Player screen position
; screen_x = player_world_x - scroll_offset
; Collision check at player's world position in tile map

check_terrain:
    ld a,(player_world_x)
    ld b,a
    ld a,(player_world_y)
    ld c,a
    ; Look up tile at (b,c) in the level tile map
    ; Tile map is indexed by world coordinates, not screen
    call get_tile_at_world_pos
    ; A = tile type
    cp TILE_SOLID
    ret z                   ; Solid: blocked
    cp TILE_PLATFORM
    ...
```

### Zone Streaming (128K)

Each zone is ~8-12KB compressed. On 128K, zones are stored in banked RAM:

```
Page 1: Zone 1 (Greenwood) + Zone 2 (Ridgeway)
Page 3: Zone 3 (Shorelands) + Zone 4 (Ashfield)
Page 4: Zone 5 (Dawnreach) + extra content
Page 6: AY music data (all zones)
```

Zone transition: page in the correct bank, decompress the new zone's tile map to a working buffer, reset scroll position, place player at zone start.

On 48K: zones load from tape (multi-load) or fit compressed in main RAM (tighter, fewer side areas).

### Frame Budget with Scrolling + Platforming + Combat

| Task | T-states (approx) | Notes |
|------|-------------------|-------|
| Pixel scroll (fine) | 25,000-30,000 | From Ionfire |
| Player sprite (restore-under) | 3,000-4,000 | Draw + erase |
| Enemy sprites (×4) | 12,000-16,000 | 4 simultaneous enemies |
| Projectile sprites (×2) | 4,000-6,000 | Player + enemy bullets |
| Collision detection | 3,000-5,000 | Player-terrain, bullet-enemy, enemy-player |
| Enemy AI | 2,000-4,000 | Movement, state updates |
| HUD update | 1,000-2,000 | Health, score, weapon |
| AY music (128K, IM 2) | 2,000-3,000 | Interrupt handler |
| **Total** | **~52,000-70,000** | **Tight on 48K (~69,888 T-states/frame)** |

On 48K, the frame budget is extremely tight. Optimisation strategies:
- Reduce to 3 simultaneous enemies (not 4) in 48K mode
- Simpler enemy AI on 48K (patrol only, no chase)
- Skip parallax on 48K (128K only)
- Accept occasional frame drops during dense combat

On 128K, double buffering eliminates tearing and provides more CPU time (no contention on the off-screen page).

---

## The Spectrum Arc

The four Spectrum assembly games form a complete journey:

| Game | Setting | Technique | Emotion |
|------|---------|-----------|---------|
| Gravelight | Underground mines | Attributes, platforming | Discovery, constraint |
| Ionfire | Outer space | Software scrolling | Speed, spectacle |
| Grimstone | Cursed castle | Isometric projection | Mystery, puzzle |
| Dawnreach | Surface world, journey east | Everything combined | Hope, determination |

The learner descends into mines, flies through space, explores a castle, and finally walks across the land toward the dawn. Each game teaches a major technique; the capstone combines them all. The setting brightens as the learner's skill grows — from underground darkness to open sunrise.

And the production techniques (turbo loader, disk support, multi-model testing) are the final lesson: making the game isn't enough. You have to ship it.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Spectrum assembly capstone. Scrolling action-platformer combining techniques from Gravelight, Ionfire, and Grimstone with production/distribution skills.
