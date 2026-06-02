# Sinclair ZX Spectrum — Assembly Curriculum

**Platform:** Sinclair ZX Spectrum
**Track:** Z80 Assembly
**Shape:** 44 entries across 6 volumes (~2,396 units total)
**October 2026 ship:** Shadowkeep (V1.1), Arcs 1+2 = 32 units
**Status:** Active. v0.3 track structure locked.

**Strategic context:** Binding decisions are [decisions/spectrum-assembly-track.md](../../decisions/spectrum-assembly-track.md) (44-entry structure, layer model, branches), [decisions/spectrum-assembly-per-game-scope.md](../../decisions/spectrum-assembly-per-game-scope.md) (per-game unit estimates), [decisions/shadowkeep-32-unit-commitment.md](../../decisions/shadowkeep-32-unit-commitment.md) (Shadowkeep October scope), [decisions/shadowkeep-four-arc-framing.md](../../decisions/shadowkeep-four-arc-framing.md) (Shadowkeep full-game framing), [decisions/inspired-by-not-clones-naming.md](../../decisions/inspired-by-not-clones-naming.md) (naming convention), [decisions/curriculum-structure.md](../../decisions/curriculum-structure.md) (multi-disciplinary bar), [decisions/real-retro-games.md](../../decisions/real-retro-games.md), [decisions/spiral-and-incremental.md](../../decisions/spiral-and-incremental.md), [decisions/constraint-position.md](../../decisions/constraint-position.md). Live status: [tracker/revamp.md](../../tracker/revamp.md).

---

## North Star

Four claims with explicit roles:

- **Spine (outcome):** Commercial bar. *"You can ship a game CRASH would have reviewed."*
- **Method (journey):** Legends technique-by-technique. Each entry pegged to a named legend (Smith, Ultimate, Crow, Hewson, Ritman, Singleton, Priestley, Crammond, Evans).
- **Lens (framing):** Constraint as design language. 48K / 8×8 attribute / single-channel beeper limits ARE the design vocabulary, not obstacles around it.
- **Depth (level of teaching):** The machine at the metal. Every claim grounded in real bytes.

Method, lens, and depth all serve the spine.

---

## Track structure

**44 entries across 6 volumes.** Total scope ~2,396 units (per-game floors 28-96).

| Volume | Identity | Entries | Layer |
|---|---|---|---|
| V1 *Rooms and Worlds* | Player navigates space | 8 games (1-8) | L0 |
| V2 *Verticality and Gravity* | Player moves under constraint | 8 games (9-16) | L0 |
| V3 *Motion and Threat* | World comes at the player | 8 games (17-24) | L0 |
| V4 *Real World and Third Dimension* | Player operates a real-world thing | 8 games (25-32) | L0 |
| V1-4 late additions | Genre gaps | 4 games (33-36) | L0 |
| V5 *Beyond Games* | Demoscene productions | 4 productions (37-40) | L0 |
| V6 *The Next Generation* | Spectrum Next-native productions | 4 productions (41-44) | L+4b |

**Layer model** composes additional content onto a native L0 core:

- **L0** — 40 native 48K entries (V1-V5)
- **L+1** — 128K AY audio enhancement on selected L0 games
- **L+3** — Demoscene polish layer (from V5 techniques) on selected L0 title sequences and transitions
- **L+4a** — Selective Next-enhanced variants of ~6 L0 games (V1.2 Greypeak, V2.10 Hollowhalls, V3.17 Hostraider, V3.18 Ironstreak, V4.29 Coldstar, V4.30 Coreworks)
- **L+4b** — Volume 6: 4 Next-native productions designed specifically for Spectrum Next hardware

---

## Lineup

Working-draft names per the [inspired-by-not-clones convention](../../decisions/inspired-by-not-clones-naming.md). Each entry has a player-facing headline (one word) and a design concept (the generalisable design idea).

### Volume 1 — *Rooms and Worlds*

| # | Name | Tradition | Headline (Design Concept) | Units |
|---|------|-----------|---------------------------|-------|
| 1 | **Shadowkeep** | Ultimate / Atic Atac / Knight Lore | Atmosphere (Sense of Place) | 64 |
| 2 | Greypeak | Ritman / Ultimate / Knight Lore (iso) | Depth (Spatial Illusion) | 56 |
| 3 | Underlight | Crow / Hewson / Starquake / Sabre Wulf | Openness (Non-Linear Geography) | 64 |
| 4 | Whitewinter | Singleton / Lords of Midnight | Scale (Procedural Vastness) | 80 |
| 5 | Brace and Boon | Ritman / Head Over Heels | Duality (Two-Character Mechanics) | 64 |
| 6 | Embergate | Crow / Firelord, Gauntlet ports | Power (Equipment Progression) | 80 |
| 7 | The Lantern Path | Melbourne House / Hobbit parser | Conversation (Modelled World) | 80 |
| 8 | The Last Banner | Lothlorien / Yankee, Arnhem | Decision (Resource Trade-Offs) | 48 |

### Volume 2 — *Verticality and Gravity*

| # | Name | Tradition | Headline (Design Concept) | Units |
|---|------|-----------|---------------------------|-------|
| 9 | Salt Caverns | Smith / Manic Miner | Jump (Platform Physics) | 48 |
| 10 | Hollowhalls | Smith / Jet Set Willy | Traversal (Connected World) | 72 |
| 11 | Voidlift | Ultimate / Jetpac | Lift-off (Thrust Control) | 28 |
| 12 | The Goblin's Larder | Priestley / Trapdoor | Personality (Character-Forward Design) | 36 |
| 13 | Towerfast | Tehkan / Bombjack | Ascent (Vertical Progression) | 32 |
| 14 | Brindlewood | Ultimate / Sabreman, Underwurlde | Adventure (Goal-Free Exploration) | 64 |
| 15 | Twin Sparks | Taito / Bubble Bobble | Companionship (Shared-Screen Co-op) | 40 |
| 16 | The Witch's Year | Palace / Cauldron II | Mastery (Difficulty as Content) | 52 |

### Volume 3 — *Motion and Threat*

| # | Name | Tradition | Headline (Design Concept) | Units |
|---|------|-----------|---------------------------|-------|
| 17 | Hostraider | Crow / Cybernoid II | Density (Single-Screen Composition) | 64 |
| 18 | Ironstreak | Hewson / Zynaps | Speed (Horizontal Pressure) | 64 |
| 19 | Skylash | Crow / Light Force, 1942 | Rising (Vertical Pressure) | 52 |
| 20 | Edge of Iron | Beam / Way of the Exploding Fist | Combat (Animation-Driven Engagement) | 64 |
| 21 | Hivefall | Namco ports / Galaxians | Pattern (Formation Behaviour) | 40 |
| 22 | Wayguard | Williams ports / Defender | Patrol (Two-Sided Threat) | 52 |
| 23 | Grinder | Williams ports / Robotron | Survival (Wave Endurance) | 40 |
| 24 | March Iron | Konami ports / Green Beret | Onslaught (Auto-Scroll Forced Motion) | 44 |

### Volume 4 — *Real World and Third Dimension*

| # | Name | Tradition | Headline (Design Concept) | Units |
|---|------|-----------|---------------------------|-------|
| 25 | Ten Trials | Ocean / Daley Thompson | Rhythm (Cadence Input) | 52 |
| 26 | Cup Saturday | Ritman / Match Day | Coordination (Team Simulation) | 64 |
| 27 | Storm Bird | Digital Integration / Tornado | Flight (Aerial Control) | 64 |
| 28 | Switchback | various / Buggy Boy, Chequered Flag | The Road (Pseudo-3D Driving) | 52 |
| 29 | Coldstar | Bell/Braben port / Elite | Vastness (Wireframe Space) | 96 |
| 30 | Coreworks | Incentive / Driller, Castle Master | Volume (Solid Space) | 80 |
| 31 | The Long Passage | Malcolm Evans / 3D Monster Maze | Presence (First-Person View) | 32 |
| 32 | Stillwatcher | Crammond / The Sentinel | Vantage (3D Strategy) | 52 |

### V1-V4 late additions (genre gaps)

| # | Name | Tradition | Headline (Design Concept) | Units |
|---|------|-----------|---------------------------|-------|
| 33 | Greycoat | Townsend / Saboteur II | Patience (Line-of-Sight Avoidance) | 56 |
| 34 | The Drawn World | Melbourne House / Lord of the Rings | The Picture and the Word (Parser + Illustration) | 64 |
| 35 | Quoin | Tetris-port tradition | Stacking (Cascading State) | 28 |
| 36 | Baize | Sinclair / Steve Davis Snooker | Continuous Physics (Cue and Ball) | 48 |

### Volume 5 — *Beyond Games* (demoscene productions)

| # | Name | Tradition | Headline (Design Concept) | Units |
|---|------|-----------|---------------------------|-------|
| 37 | Hairline | Border tricks, raster colour | Beyond the Bitmap (Raster-Timed Tricks) | 20 |
| 38 | Living Surfaces | Plasma, fire, sin-scroll, particles | Living Surfaces (Procedural Texture) | 24 |
| 39 | Geometry's Pulse | Vector demos with music sync | Form in Motion (Vector + Music Sync) | 28 |
| 40 | The Long Night | Multi-part assembly / megademo | Authorship of Time (Demo Architecture) | 32 |

### Volume 6 — *The Next Generation* (Spectrum Next-native)

| # | Name | Tradition | Headline (Design Concept) | Units |
|---|------|-----------|---------------------------|-------|
| 41 | Newhall | Modern scene / hardware sprites + scroll | Sixteen-Bit Spectrum | 64 |
| 42 | Iron Hundred | Modern scene / sprite density | A Hundred Sprites | 52 |
| 43 | Truecolour | Incentive evolution / Layer 2 textured 3D | The Solid World | 72 |
| 44 | The Marchlands | Modern scene / tilemap mode + 2MB RAM | World-Sized Memory | 88 |

---

## Per-entry design pattern

Each entry carries three orthogonal axes:

1. **Player-facing headline** — one-word player-felt experience (Atmosphere, Jump, Density)
2. **Design concept** — the generalisable design idea (Sense of Place, Platform Physics, Single-Screen Composition)
3. **Technique** — engineering implementation, mapped separately in a cross-game tech-tree (Y-Sort Rendering, Gravity Physics, Hand-Composed Hazard Layout)

The game page renders headline + design concept as a dual-name. Techniques live separately as a cross-game matrix.

---

## Cross-cutting axes

| Axis | Items | What it teaches | Track applicability |
|------|-------|-----------------|---------------------|
| Embedded Design Concepts | ~10 | The WHY — atmosphere through restraint, authored level design, difficulty as design, etc. | Both BASIC and Assembly |
| Engineering Practices | 9 | The HOW-ENGINEERING — Z80 disciplines (LDIR, T-state counting, SMC, stack-as-data, etc.) | **Assembly only** — the differentiator from BASIC |
| Production Craft | ~15 | The HOW-PIPELINE — art tools, music trackers, loading screens, custom loaders | Both, more pronounced in Assembly |

### Engineering Practices first-encounter mapping

| # | Practice | First introduced |
|---|----------|------------------|
| 1 | LDIR + block-copy basics | Shadowkeep U2 |
| 2 | Pre-computed lookup tables | Shadowkeep U2 |
| 3 | Register pair strategy | Shadowkeep U7 |
| 4 | Loop unrolling | Shadowkeep U8 |
| 5 | Software clipping at edges | Shadowkeep U8 |
| 6 | Self-modifying code (runtime) | V3.17 Hostraider |
| 7 | Stack-as-data-pointer | V3.17 Hostraider |
| 8 | Dirty-rectangle redraw (named) | V3.17 Hostraider |
| 9 | T-state counting | V3.18 Ironstreak |

Five of nine are introduced in Shadowkeep; four in V3 (where action density makes them existential).

---

## Tech-tree (Trunk + Branches A-G)

Techniques cluster into a Trunk + Branches model. Each layer's techniques are prerequisites for the next.

- **Trunk (Layers 1-4)** — Shadowkeep introduces; every game inherits
- **Branch A** — Adventure depth (Shadowkeep Arcs 3-4, flick-adventure tradition: items + multiple keeps + secrets + atmospheric cycles per [decisions/shadowkeep-four-arc-framing.md](../../decisions/shadowkeep-four-arc-framing.md))
- **Branch B** — Platformer specifics (V2)
- **Branch C** — Scrolling and density (V3)
- **Branch D** — Real-world sim (V4 sport / vehicle)
- **Branch E** — True 3D (V4 3D entries)
- **Branch F** — Cross-cutting specials (parser, isometric, procedural)
- **Branch G** — Audio hardware (AY + 128K — introduced V2.16 *The Witch's Year*, deepened V3.17 *Hostraider*)

**Deprecation pairs are first-class teaching moments**, not refactors. When a richer technique replaces a simpler one, the transition is the lesson:

- cell-snapped movement → pre-shifted sprite tables (Shadowkeep Arc 1.2)
- single-draw rendering → Y-sort layered rendering (Shadowkeep Arc 1.3)
- attribute-byte-as-collision → tile-map collision (Shadowkeep Arc 1.4)
- flick transitions → smooth scroll (V3)
- isometric → pseudo-3D → wireframe 3D → solid 3D (V4)

---

## Tier hierarchy

- **Tier 1** = Games 1-16 (~960 units) — the spine; cut last
- **Tier 2** = Games 17-32 + late additions 33-36 (~880 units) — expansion + genre gaps
- **Tier 3** = V5 demoscene + V6 Next-native (~380 units)

### Cut hierarchy (timeline tightens)

1. V6 (L+4b) Next-native drops first
2. L+4a Next variants
3. V5 demoscene
4. L+1 retroactive AY enhancements
5. Tier 2 within V1-V4, inside-out by inverse-canonical-weight
6. Tier 1 last; *The Last Banner* (#8, canon-thin) is the demote candidate if Tier 1 is touched

Cuts apply only after a real timeline slip is identified. The default plan is the full 44.

---

## October 2026 ship

> **Current state (2026-06-02).** Shadowkeep was re-paced to the cell-based **_Place_** (pass 1 of a game across several modules — [modules-not-games](../../decisions/modules-not-games.md)), carrying Gloaming's engine. **12 units live** (sub-arcs 1.1–1.3); audio (1.4) remaining; counts illustrative. The three engine commitments described below (pre-shift/masked sprites, Y-sort, decoupled collision) are **relocated** to later rendering games and are *not* built in Shadowkeep. The arc / 32-unit / engine detail in this section is **superseded**, kept pending a fuller rewrite of this track-wide doc (entangled with the pending modules-not-games migration). Current sources: [tracker/revamp.md](../../tracker/revamp.md), the amended Shadowkeep decision records, and [games/shadowkeep/brief.md](games/shadowkeep/brief.md) (v3.0).

**Only Shadowkeep Arcs 1-2 / 32 units ships.** All other track work is post-October.

Shadowkeep (Volume 1, Game 1) is structured as four arcs of 16 units (64 total). October ships Arcs 1+2:

- **Arc 1 — *Foundations and a Place*** (Units 1-16)
- **Arc 2 — *Inhabitants and Identity*** (Units 17-32)
- Arc 3 — *Beyond the Walls* (Units 33-48) — post-October Year 1
- Arc 4 — *The Greater World* (Units 49-64) — post-October Year 2

**Three engine commitments** introduced progressively across Arc 1:

1. Pixel-level sprite movement (2-4 pixels per frame; pre-shifted sprite tables; masked sprite drawing)
2. Back-to-front Y-sorted layered rendering
3. Decoupled attribute / collision (collision lives in tile-map; attribute area becomes purely cosmetic)

Reference points: *Atic Atac*, *Knight Lore*, *Cybernoid II*.

**Genre honesty:** Shadowkeep stays in the flick-adventure tradition. Combat / classes / XP / spells / branching narrative / multi-NPC dialogue / quest state / full Singleton-class location-graph are NOT taught in Shadowkeep — they're primary teaching in V1.6 Embergate (action-RPG), V1.7 The Lantern Path (parser), V1.4 Whitewinter (procedural), V3.17 Hostraider (projectile), V3.20 Edge of Iron (combat). See [decisions/shadowkeep-four-arc-framing.md](../../decisions/shadowkeep-four-arc-framing.md) for the full redistribution table.

**The old engine-first Units 1–8 were retired** (2026-06-02) when Shadowkeep reset to the cell-based Place; preserved in git history. Units 1–12 of the Place are now live.

**Full Shadowkeep design:** [games/shadowkeep/brief.md](games/shadowkeep/brief.md) (v3.0, cell-based Place). Per-unit reference: [games/shadowkeep/per-unit-plan.md](games/shadowkeep/per-unit-plan.md). Beeper theme spec (sub-arc 1.4): [games/shadowkeep/beeper-spec.md](games/shadowkeep/beeper-spec.md). The engine-first specs (engineering-plan, memory-budget, object-system, sprite-shifter, tile-map) are archived under [games/shadowkeep/superseded/](games/shadowkeep/superseded/) — relocated techniques, not current.

---

## Per-game scope summary

**Heavy hitters (≥80 units):** Coldstar 96, The Marchlands 88, Whitewinter / Embergate / The Lantern Path / Coreworks 80 each.

**Small / focused (≤32 units):** Hairline 20, Living Surfaces 24, Voidlift / Quoin / Geometry's Pulse 28 each, Towerfast / The Long Passage / The Long Night 32 each.

**Per-volume totals:** V1 536, V2 372, V3 420, V4 492, late additions 196, V5 104, V6 276. Per-entry rationale in [decisions/spectrum-assembly-per-game-scope.md](../../decisions/spectrum-assembly-per-game-scope.md).

---

## Realistic shipping timeline

Multi-decade by design. Solo dev pace ~3-4 days per unit:

| Period | Focus | Approx units |
|--------|-------|--------------|
| 2026 Oct | Shadowkeep Arcs 1-2 | 32 (committed) |
| 2027-28 | Shadowkeep Arc 3 + BASIC V1 + start of V1.2 Greypeak | ~50 new Assembly |
| 2028-30 | V1 Games 1-8 substantially complete | ~250 |
| 2030-32 | V2 + late V1-4 additions | ~500 |
| 2032-35 | V3 | ~400 |
| 2035-38 | V4 | ~500 |
| 2038-40 | V5 + V6 | ~400 |
| 2040+ | Polish, naming workshops, late additions | rolling |

The project's North Star is end-to-end vintage games-development education at canonical depth; that doesn't fit in a year.

---

## BASIC gateway

The Sinclair BASIC curriculum is maintained separately. See [basic.md](basic.md) (32 games × 4 volumes × 8 per volume; v6.4 inspired-by-not-clones names; October ships Volume 1).

Together the two tracks form one Spectrum journey: BASIC is the on-ramp; Assembly takes the learner to commercial bar.

---

## Changelog

- **v0.3 (2026-05-19) — current.** Wholesale rewrite. Track structure expanded from 4 games to 44 entries across 6 volumes per [decisions/spectrum-assembly-track.md](../../decisions/spectrum-assembly-track.md). Working-draft inspired-by names locked for all 44 entries. Layer model (L0 + L+1 + L+3 + L+4a + L+4b) introduced. Three-axis design pattern (headline + concept + technique) replaces the old single-name pattern. Tech-tree with deprecation pairs (Trunk + Branches A-G) replaces the implicit progression. Three cross-cutting axes (Design Concepts / Engineering Practices / Production Craft) named. Shadowkeep four-arc framing (64 units, October ships Arcs 1+2 = 32) replaces the 256-unit / 17-phase v5.0 framing. Per-entry unit budgets per [decisions/spectrum-assembly-per-game-scope.md](../../decisions/spectrum-assembly-per-game-scope.md). Genre honesty applied to Shadowkeep (combat / classes / parser / branching narrative redistributed to V1.6 / V1.7 / V3.17 / V3.20). Three deleted v5.0 entries (Ionfire, Grimstone, Dawnreach) preserved in git history; their content was 4-game-track planning that no longer applies.
- **v5.0 (2026-05-13):** 4 games × 256 units restructure under the multi-disciplinary commitment. Game 1 reconciled as Shadowkeep. Preserved in git history.
- **v4.0 (2026-03-09):** Reduced from 16 to 4 assembly games. Preserved in git history.
- **v3.x and earlier:** 16-game curriculum. Preserved in git history.
