# Sinclair ZX Spectrum Curriculum

**Platform:** Sinclair ZX Spectrum
**Killer Feature:** Attribute colour system
**Assembly Games:** 4
**Total Units:** 1,024 (4 × 256)
**Curriculum bar:** mid-tier full-price — Hewson / Gremlin / Mikro-Gen / Durell era, ~£7.95 in period

**Strategic context:** See `docs/decisions/curriculum-structure.md` for the per-game unit budget rationale and the acceleration assumption it depends on, `docs/decisions/real-retro-games.md` for the multi-disciplinary commitment, `docs/decisions/spiral-and-incremental.md` for the within-phase incremental and across-phase spiral progression model, and `docs/decisions/constraint-position.md` for the era-authenticity taxonomy each game declares.

---

## Overview

The ZX Spectrum curriculum teaches Z80 assembly programming through four complete games. The sequence begins with the attribute system — the Spectrum's defining characteristic that created its distinctive visual style — and progresses through software scrolling, isometric projection, and professional production techniques until learners can produce commercial-quality games.

The Spectrum had no hardware sprites, no smooth scrolling, and a single-bit beeper for sound. Every impressive effect was achieved through software and creativity. This curriculum embraces those constraints, teaching learners to make the hardware sing through ingenuity.

By the final game, learners will have skills matching professional Spectrum developers of the mid-to-late 1980s — equivalent to mid-tier studios shipping at the £7.95 full-price tier.

---

## Assembly Track

### Structure

| Game | Units | Role |
|------|-------|------|
| 1 | 256 | Accessible entry — attribute system as game mechanic |
| 2 | 256 | Signature technique — software pixel scrolling |
| 3 | 256 | Ambitious — isometric adventure with 128K features |
| 4 | 256 | Capstone — commercial-quality dual-mode release |
| **Total** | **1,024** | |

Per-game phase structure is declared in each game's brief. Phase sizes are powers of 2 (8, 16, 32, etc.). Phase 1 of each game is conventionally an 8-unit vertical slice (the launch-artefact pattern from `docs/decisions/shadowkeep-32-unit-commitment.md`); subsequent phases scale as the spiral revisit's natural scope dictates.

---

### Game 1: Multi-room Top-down Adventure

**Units:** 256 (per-brief phase structure; Phase 1 = 8-unit vertical slice for October 2026 launch)
**Genre:** Multi-room top-down adventure
**Inspired by:** *Atic Atac* (Ultimate, 1983), *Sabre Wulf* (Ultimate, 1984)
**Working title:** Shadowkeep

**Concept:** A keep on a dark hill. Magic has gone wrong; the shadows walk its halls. The player enters alone to recover the Heart of the Keep, finds it, escapes. A multi-room top-down adventure where the Spectrum's attribute system *is* the entire game logic — walls are blue, treasure shines, hazards flash, doors hum cyan. Eight cell types decoded from a single attribute byte. The screen is the map; the attribute byte is the rule.

**Skills taught (across all 256 units, spiral-revisited across phases):**

- Z80 fundamentals (registers, addressing modes, flags, stack, indexed iteration)
- Screen memory layout ($4000-$57FF) and the three-thirds quirk
- Attribute memory ($5800-$5AFF) — INK, PAPER, BRIGHT, FLASH bits
- Keyboard input via port `$FE` half-row scanning
- Character-cell movement (8-pixel grid) with erase-and-redraw
- Bitmap sprite drawn over attribute-driven world with cell preservation
- Attribute-based collision detection
- Multi-room engine (room pointer table, N/S/E/W connection tables, state machine)
- Single-voice beeper music driver (port `$FE` bit 4, tick-counter timing)
- Beeper SFX layer interleaved with music
- 2-frame walking animation
- Multiple wandering enemy types with simple AI
- Save/load (later phases)
- AY-3-8912 music (128K, later phases)
- Bank switching for additional rooms (128K, later phases)
- Title screen with composed melody, attract mode, end-game sequence
- 128K detection and dual 48K/128K code paths
- Turbo tape loader and +3 disk support (capstone phases)

**Why first:** The attribute system is the Spectrum. A multi-room top-down adventure makes attribute reads and writes the core mechanic from unit 1 — every cell on screen carries one byte that says what it is, and `LD A,(HL)` plus `BIT n,A` is the entire ruleset. The Spectrum's defining feature becomes the game's design tool. *Atic Atac* and *Sabre Wulf* in 1983–84 set the bar for what an ambitious bedroom-coded Spectrum adventure could be; Shadowkeep reaches toward that bar from a 2025 vantage.

**Full Phase 1 design:** `knowledge/curriculum/shadowkeep-phase-1-design.md`.
**Beeper composition spec:** `docs/platforms/sinclair-zx-spectrum/games/shadowkeep/beeper-spec.md`.

---

### Game 2: Horizontal Scrolling Shoot 'Em Up

**Units:** 256 (unchanged in count from v4.0; now multi-disciplinary, so gameplay scope recalibrates during brief work)
**Genre:** Horizontal scrolling shmup
**Inspired by:** *R-Type*, *Zynaps*, *Nemesis*
**Working title:** Ionfire

**Concept:** Pilot a ship through alien landscapes, fight waves of enemies, defeat massive bosses. The Spectrum has no hardware scroll registers, so every pixel of scrolling is achieved through software — shift operations across screen memory, timed to avoid visible tearing. Building this game is the Spectrum's crowning technical achievement.

**Skills taught:**

- Software pixel scrolling (the hard technique — no hardware support)
- Contended memory timing (ULA steals cycles during screen refresh)
- Pixel-level shift operations across screen bytes
- Double buffering approaches for flicker-free display
- Background tile map management during scroll
- Pixel-precise collision detection
- Player ship with smooth multi-directional movement
- Weapon systems (primary fire, power-ups, charge shots)
- Enemy wave patterns and formation AI
- Large multi-character boss sprites
- Boss behaviour patterns (movement phases, weak points, attacks)
- Parallax effects via software (background layers at different speeds)
- Screen layout optimisation (attribute-friendly colour zones)
- Beeper sound engine (music during gameplay)
- Level progression with distinct visual themes
- Lives, continues, score, and high score persistence

**Why here:** Software pixel scrolling is the hardest thing to do well on the Spectrum. There are no scroll registers — every frame, the code shifts pixels across memory while the ULA fights for bus access. Games like *R-Type* on the Spectrum were technical miracles. This game teaches the technique through necessity: the gameplay demands scrolling, so the learner builds it. By the end, they understand contended memory timing at a level that makes every other Spectrum technique feel straightforward.

---

### Game 3: Isometric Adventure

**Units:** 256 (revised down from 512 in v4.0 — design adjustment needed during brief work; Knight Lore scale at full 140-room scope is not achievable in 256 multi-disciplinary units, so the game's scale or scope will recalibrate)
**Genre:** Isometric adventure
**Inspired by:** *Knight Lore*, *Head Over Heels*, *Batman*
**Working title:** Grimstone

**Concept:** Explore a castle or fortress rendered in isometric 3D. Push blocks onto pressure plates, avoid enemies, collect items, solve environmental puzzles. The Spectrum invented this genre — Ultimate's *Knight Lore* was the first isometric adventure, and it changed what people believed the hardware could do.

This is the first game to use 128K features: AY-3-8912 music, bank switching, and dual-page rendering.

**Skills taught:**

- Isometric projection mathematics (world-to-screen coordinate conversion)
- Depth sorting (painter's algorithm — draw back-to-front)
- Isometric tile and object rendering
- Z-height collision detection (walking on raised platforms, falling)
- Room-based world structure with transitions
- Push-block puzzles (Sokoban-style within isometric space)
- Pressure plates, doors, gates, keys
- Multiple enemy types with distinct behaviours
- Player abilities (jump, carry, push, use items)
- Inventory system
- Transformation or time mechanic (Knight Lore's werewolf, Head Over Heels' character switching)
- 128K detection and adaptation
- AY-3-8912 music (three channels, envelope, noise)
- Bank switching for room data
- Dual-screen rendering (draw off-screen, flip)
- Themed zones with distinct visual palettes (within attribute constraints)
- Save or password system for progress
- Title screen with AY music, in-game ambient sound

**Why here:** The isometric adventure is the Spectrum's unique gift to gaming. *Knight Lore* in 1984 made people believe the Spectrum could do 3D. This game teaches the mathematics behind the illusion — projection, depth sorting, Z-collision — while building a world large enough to justify 128K bank switching. It's where the curriculum's techniques come together: attribute mastery from Game 1, display timing from Game 2, and now spatial reasoning in isometric space.

**Scope recalibration:** At 256 units rather than the v4.0 512, full Knight Lore room count (~140 rooms) is unrealistic. Expect the brief to land at 40–60 rooms with mid-tier full-price polish per room, rather than a sprawling 100+-room world at thinner quality.

---

### Game 4: Capstone

**Units:** 256 (revised down from 512 in v4.0 — design adjustment needed during brief work)
**Genre:** Scrolling action-platformer with exploration
**Inspired by:** *Midnight Resistance*, *Ghosts 'n Goblins*, *Dan Dare III*
**Working title:** Dawnreach

**Concept:** A journey across the land toward the source of a spreading darkness. Five zones — Greenwood (forest), Ridgeway (mountains), Shorelands (coast), Ashfield (wasteland), and the Dawnreach (eastern tower) — each a scrolling landscape with unique terrain, enemies, and a guardian boss. The game combines techniques from Shadowkeep (attribute-driven gameplay, multi-room engine), Ionfire (scrolling, contended memory timing), and Grimstone (large-world structure, 128K features) into a single production.

**Design implication of the Game 1 change:** Dawnreach was originally conceived as a scrolling action-platformer building on Gravelight's platformer foundations. With Game 1 now Shadowkeep (multi-room adventure, not a platformer), Dawnreach's genre needs recalibration during brief work. Two paths: either keep the scrolling-action-platformer genre and teach platforming fresh (within Dawnreach's 256 units), or recalibrate to a scrolling-adventure genre that builds directly on Shadowkeep's foundations. Brief decides.

The capstone's new material is distribution and production: turbo tape loading, +3 disk support, 128K/48K dual-mode code paths, loading screens, and multi-load architecture. The finished game should look like it could sit on a shop shelf next to *Midnight Resistance* or *Dan Dare III*.

**Skills taught:**

- All techniques from Games 1-3 at mastery level
- Scrolling world with varied terrain and enemy placement
- Melee and ranged combat systems
- Multi-zone world design (distinct themes, palettes, enemy sets)
- 128K/48K dual-mode detection and code paths
- AY music on 128K with beeper fallback on 48K
- Turbo tape loader (custom loading routine, faster than ROM)
- +3 disk version (accessing the uPD765 FDC)
- Loading screen (displayed during tape/disk load)
- Professional title sequence
- Multiple difficulty levels
- Password or save system
- End-game sequence and credits
- Testing across models (48K, 128K, +2, +2A, +3)

**Why last:** The capstone proves the learner can ship a product. The game itself combines scrolling action with exploration — genres the learner has already mastered individually. The new challenge is production: making the game load from tape and disk, adapting to different Spectrum models, and presenting a professional package. Every game in the curriculum runs on real hardware; the capstone makes that fact visible through custom loaders and multi-model support.

**Scope recalibration:** At 256 units rather than the v4.0 512, the five-zone structure may compress to three or four zones with deeper per-zone work, or zones may shrink in length. The brief decides.

---

## BASIC Gateway

The Sinclair BASIC curriculum is maintained separately. See `/docs/platforms/sinclair-zx-spectrum/basic.md`.

---

## Changelog

- **v5.0 (2026-05-13):** Substantial revision driven by decisions captured 2026-05-13 (see `docs/decisions/`). Per-game unit count standardised at 256 across all four games (was 128/256/512/512), aligning with the multi-disciplinary commitment and the mid-tier full-price target. Total platform units 1,408 → 1,024. Game 1 reconciled — name is Shadowkeep (was Gravelight in v4.0); genre is multi-room top-down adventure (was single-screen platformer); inspirations are *Atic Atac* / *Sabre Wulf* (were *Manic Miner* / *Jet Set Willy*). Phase structure now per-brief rather than fixed; Phase 1 is conventionally an 8-unit vertical slice. Games 3 and 4 down from 512 units; design adjustment flagged for the brief work on each. **The four v4.0 game outline files (`game-01-full-game-outline-zx-spectrum-gravelight.md` and siblings for Ionfire/Grimstone/Dawnreach) were deleted** — they documented the previous 128/256/512/512 code-led plan at the wrong unit scale and (for Gravelight) the wrong Game 1 design; preserved in git history rather than confusing future readers as apparently-current spec.
- **v4.0 (2026-03-09):** Major restructure. Reduced from 16 to 4 assembly games. No-repetition rule across primary platforms. Every game inspired by a real commercial release. BASIC gateway expanded from 8 to 4 focused games. Previous 16-game curriculum preserved in game outline files for reference.
- **v3.20 (2026-02-06):** Replaced Game 1 (Skyfire) with Shadowkeep.
- **v3.0 (2026-01-18):** Initial 16-game curriculum.
