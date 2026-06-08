# Sinclair ZX Spectrum — Assembly Curriculum

**Platform:** Sinclair ZX Spectrum
**Track:** Z80 Assembly
**Shape:** A sequence of **modules** across 6 volumes — a `teaching` Primer, then the Volume-1 game and revisit modules (~11 entries), with Volumes 2–6 sketched. The original 44-game lattice plus the gentle-ramp opening (Primer + *Gloaming* + two rendering inserts). ~2,400 units, illustrative. Modules — not games — are the unit of sequencing; one game can span several modules ([decisions/modules-not-games.md](../../decisions/modules-not-games.md)).
**October 2026 ship:** The gentle assembly opening — Primer (*Meet the Machine*) + the complete tiny game *Gloaming* + the start of the cell-based *Shadowkeep* (its **Place**). All 16 units of the Place are live — Arc 1 complete (a finishable, replayable flick-adventure).
**Status:** Active. v0.4 — reconciled to the gentle-ramp + module model.

**Strategic context:** The **governing** decision for the track's opening, the per-game technique budget, and the re-scope of Shadowkeep is [decisions/spectrum-assembly-gentle-ramp.md](../../decisions/spectrum-assembly-gentle-ramp.md). The track is sequenced as modules per [decisions/modules-not-games.md](../../decisions/modules-not-games.md) (migrated 2026-06-01: bare slugs, `modules/` catalogue, ordering = catalogue array position). The original track structure is [decisions/spectrum-assembly-track.md](../../decisions/spectrum-assembly-track.md) (44-entry lattice, layer model, branches — amended by the gentle-ramp), with [decisions/spectrum-assembly-per-game-scope.md](../../decisions/spectrum-assembly-per-game-scope.md) (per-game unit estimates, now illustrative). Shadowkeep's own records, both amended for the cell-based Place: [decisions/shadowkeep-32-unit-commitment.md](../../decisions/shadowkeep-32-unit-commitment.md) and [decisions/shadowkeep-four-arc-framing.md](../../decisions/shadowkeep-four-arc-framing.md). Also: [decisions/inspired-by-not-clones-naming.md](../../decisions/inspired-by-not-clones-naming.md) (naming), [decisions/curriculum-structure.md](../../decisions/curriculum-structure.md) (multi-disciplinary bar, no fixed unit counts), [decisions/real-retro-games.md](../../decisions/real-retro-games.md), [decisions/spiral-and-incremental.md](../../decisions/spiral-and-incremental.md), [decisions/constraint-position.md](../../decisions/constraint-position.md). Project state: the `modules/*.yaml` catalogues + git (see [state-lives-in-catalogues](../../decisions/state-lives-in-catalogues.md)).

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

**The 44-game L0 lattice across 6 volumes, plus the gentle-ramp opening.** The native-48K lattice is 44 entries (V1–V6 below); ahead of and within Volume 1 sit the `teaching` Primer, the tiny first game *Gloaming*, and the two rendering inserts (*Smooth Motion*, *Overlap*) that the [gentle-ramp decision](../../decisions/spectrum-assembly-gentle-ramp.md) adds. The track is sequenced as **modules** ([modules-not-games](../../decisions/modules-not-games.md)) — ordering is the module catalogue's array position, not the positional numbers in the tables below. Total scope ~2,400 units; **all unit counts here are illustrative markers, not targets** ([curriculum-structure](../../decisions/curriculum-structure.md)).

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

Revised lineup per the [gentle-ramp decision](../../decisions/spectrum-assembly-gentle-ramp.md): the Primer and *Gloaming* open the track, and the rendering Trunk spreads across two inserts into Greypeak rather than being front-loaded into Shadowkeep. Counts are illustrative.

| # | Entry | Tradition | Headline / role | New major technique(s) | ~Units |
|---|-------|-----------|-----------------|------------------------|--------|
| — | **Primer** | — | Meet the Machine (`teaching`, not a game) | machine literacy | ~8–12 |
| 1 | **Gloaming** | tiny first game | "I finished a game in asm" | game loop; cell sprite + collision | ~20 |
| 2 | **Shadowkeep** | Ultimate / Atic Atac | Atmosphere (Sense of Place) | room-data + flick transitions; atmosphere craft | 32 (Oct) / 64 full |
| 3 | **Smooth Motion** (insert) | — | smoothness | pre-shifted sprites (sub-cell movement) | ~20 |
| 4 | **Overlap** (insert) | — | sprites over scenery | masked sprite drawing | ~20 |
| 5 | **Greypeak** | Ritman / Knight Lore (iso) | Depth (Spatial Illusion) | Y-sort depth ordering + isometric projection | ~56 |
| 6 | **Underlight** | Crow / Hewson / Starquake / Sabre Wulf | Openness (Non-Linear Geography) | large room-graph + map streaming | ~64 |
| 7 | **Whitewinter** | Singleton / Lords of Midnight | Scale (Procedural Vastness) | procedural generation + location-graph | ~80 |
| 8 | **Brace and Boon** | Ritman / Head Over Heels | Duality (Two-Character Mechanics) | dual-entity control + state | ~64 |
| 9 | **Embergate** | Crow / Firelord, Gauntlet ports | Power (Equipment Progression) | combat state machine; classes / XP / spells | ~80 |
| 10 | **The Lantern Path** | Melbourne House / Hobbit parser | Conversation (Modelled World) | parser + dialogue + quest state | ~80 |
| 11 | **The Last Banner** | Lothlorien / Yankee, Arnhem | Decision (Resource Trade-Offs) | tactical grid | ~48 |

*Numbering note:* the gentle-ramp opening renumbers Volume 1 (Gloaming = game 1). Volumes 2–6 below keep their original v0.3 positional numbers (9–44), and the L+4a variant labels (e.g. *V1.2 Greypeak* — now game 5, *V3.17 Hostraider*) likewise read against the old numbering. A full catalogue renumber is deferred; ordering is in any case the module catalogue's array position, not these labels ([modules-not-games](../../decisions/modules-not-games.md)). *Whitewinter / Embergate / Lantern Path* are each multi-technique and likely need internal sub-arc discipline or their own inserts when spec'd — flagged by the gentle-ramp budget rule.

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
| 1 | LDIR + block-copy basics | Gloaming (cell save/restore) |
| 2 | Pre-computed lookup tables | Gloaming / Shadowkeep (screen-address tables) |
| 3 | Register pair strategy | Smooth Motion (pre-shift) |
| 4 | Loop unrolling | Smooth Motion (pre-shift) |
| 5 | Software clipping at edges | Overlap (masking) |
| 6 | Self-modifying code (runtime) | V3 Hostraider |
| 7 | Stack-as-data-pointer | V3 Hostraider |
| 8 | Dirty-rectangle redraw (named) | V3 Hostraider |
| 9 | T-state counting | V3 Ironstreak |

The first five are introduced across the gentle opening (Gloaming → Smooth Motion → Overlap), where the rendering Trunk now lives; four in V3, where action density makes them existential. (The old mapping filed practices 1–5 under engine-first Shadowkeep units 2–8 — those units were retired when Shadowkeep became the cell-based Place.)

---

## Tech-tree (Trunk + Branches A-G)

Techniques cluster into a Trunk + Branches model. Each layer's techniques are prerequisites for the next.

- **Trunk (Layers 1-4)** — introduced *gently across the opening* (Primer → Gloaming → Smooth Motion → Overlap → Greypeak), **not** front-loaded into Shadowkeep; every later game inherits. See [decisions/spectrum-assembly-gentle-ramp.md](../../decisions/spectrum-assembly-gentle-ramp.md)
- **Branch A** — Adventure depth (Shadowkeep's later revisit modules, flick-adventure tradition: items + multiple keeps + secrets + atmospheric cycles per [decisions/shadowkeep-four-arc-framing.md](../../decisions/shadowkeep-four-arc-framing.md))
- **Branch B** — Platformer specifics (V2)
- **Branch C** — Scrolling and density (V3)
- **Branch D** — Real-world sim (V4 sport / vehicle)
- **Branch E** — True 3D (V4 3D entries)
- **Branch F** — Cross-cutting specials (parser, isometric, procedural)
- **Branch G** — Audio hardware (AY + 128K — introduced V2.16 *The Witch's Year*, deepened V3.17 *Hostraider*)

**Deprecation pairs are first-class teaching moments**, not refactors. When a richer technique replaces a simpler one, the transition is the lesson. These pairs now play out *across games* — the simple version ships in an earlier game, the upgrade motivated by its felt limitation in a later one:

- cell-snapped movement (Gloaming) → pre-shifted sprite tables (Smooth Motion)
- single-draw rendering (Shadowkeep, the Place) → masked drawing (Overlap) → Y-sort layered rendering (Greypeak)
- attribute-byte-as-collision (Gloaming / Shadowkeep) → tile-map collision (Greypeak)
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

The October artefact is **the gentle assembly opening**, not "32 units of Shadowkeep" ([gentle-ramp](../../decisions/spectrum-assembly-gentle-ramp.md) § October reframed):

> Primer (*Meet the Machine*) + the *complete* tiny game **Gloaming** + the start of the cell-based **Shadowkeep** (its **Place**).

This is the more achievable launch: a learner can actually *finish* a real game in assembly by October, and the hardest engineering is off the critical path. All other track work is post-October.

**Shadowkeep is the cell-based Place** — pass 1 of a game told across several modules ([modules-not-games](../../decisions/modules-not-games.md)), carrying Gloaming's engine. **All 16 units are live** (sub-arcs 1.1–1.4) — Arc 1 complete: a lit, furnished, scored, themed, finishable and replayable flick-adventure. Counts are illustrative. Its later arcs (items, multiple keeps, tape save/load, secrets, atmospheric cycles) become **later revisit modules**, sequenced into the lineup after intervening games — not a single 64-unit block. The signature technique is **bitmap dithering** (perceived shades from mixed INK/PAPER pixels), used for textured stone, distance-based lighting, and per-room mood.

**The advanced rendering engine is *not* built in Shadowkeep.** Pixel-level pre-shifted/masked sprite movement, Y-sort layered rendering, and tile-map-decoupled collision are **relocated** to the rendering games — *Smooth Motion* (pre-shift), *Overlap* (masking), *Greypeak* (Y-sort + iso) — each motivated by a felt limitation of the game before it. Shadowkeep hits commercial bar the Manic Miner / Atic Atac way: art, lighting, room design, audio, completeness. Reference points: *Atic Atac*, *Manic Miner*, *Knight Lore* (for Greypeak's iso).

**Genre honesty:** Shadowkeep stays in the flick-adventure tradition. Combat / classes / XP / spells / branching narrative / multi-NPC dialogue / quest state / full Singleton-class location-graph are NOT taught in Shadowkeep — they're primary teaching in V1.6 Embergate (action-RPG), V1.7 The Lantern Path (parser), V1.4 Whitewinter (procedural), V3.17 Hostraider (projectile), V3.20 Edge of Iron (combat). See [decisions/shadowkeep-four-arc-framing.md](../../decisions/shadowkeep-four-arc-framing.md) for the full redistribution table.

**The old engine-first Units 1–8 were retired** (2026-06-02) when Shadowkeep reset to the cell-based Place; preserved in git history. Units 1–16 of the Place are now live — Arc 1 complete.

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
| 2026 Oct | Gentle opening: Primer + Gloaming + start of cell-based Shadowkeep (Place) | ~40–50 across the opening; the Place's 12 live |
| 2027-28 | Shadowkeep's later revisit modules + the rendering inserts (Smooth Motion / Overlap) + start of Greypeak | ~50 new Assembly |
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

- **v0.4 (2026-06-02) — current.** Reconciled to [spectrum-assembly-gentle-ramp.md](../../decisions/spectrum-assembly-gentle-ramp.md) and [modules-not-games.md](../../decisions/modules-not-games.md). Removed the engine-first framing throughout: "Shadowkeep introduces Trunk Layers 1–4 / every game inherits", the four-arcs-of-16 (64-unit) structure, the "32 units of Shadowkeep ships in October" anchor, and the three engine commitments as Shadowkeep content. The rendering Trunk now spreads across the gentle opening (Primer → Gloaming → Smooth Motion → Overlap → Greypeak); Shadowkeep is the cell-based *Place* (16 units live — Arc 1 complete; signature technique bitmap dithering); the October artefact is the gentle opening. Volume 1 lineup, Engineering-Practice first-encounters, tech-tree Trunk and deprecation pairs, timeline, and header all updated. Track sequenced as **modules**, not games (bare slugs, catalogue array position). Unit counts marked illustrative per [curriculum-structure.md](../../decisions/curriculum-structure.md) (the powers-of-2 / fixed-count framing was already retired there). V2–V6 positional numbering left at v0.3 pending a full catalogue renumber (separate). v0.3 lineup and engine-first detail preserved in git history.
- **v0.3 (2026-05-19).** Wholesale rewrite. Track structure expanded from 4 games to 44 entries across 6 volumes per [decisions/spectrum-assembly-track.md](../../decisions/spectrum-assembly-track.md). Working-draft inspired-by names locked for all 44 entries. Layer model (L0 + L+1 + L+3 + L+4a + L+4b) introduced. Three-axis design pattern (headline + concept + technique) replaces the old single-name pattern. Tech-tree with deprecation pairs (Trunk + Branches A-G) replaces the implicit progression. Three cross-cutting axes (Design Concepts / Engineering Practices / Production Craft) named. Shadowkeep four-arc framing (64 units, October ships Arcs 1+2 = 32) replaces the 256-unit / 17-phase v5.0 framing. Per-entry unit budgets per [decisions/spectrum-assembly-per-game-scope.md](../../decisions/spectrum-assembly-per-game-scope.md). Genre honesty applied to Shadowkeep (combat / classes / parser / branching narrative redistributed to V1.6 / V1.7 / V3.17 / V3.20). Three deleted v5.0 entries (Ionfire, Grimstone, Dawnreach) preserved in git history; their content was 4-game-track planning that no longer applies.
- **v5.0 (2026-05-13):** 4 games × 256 units restructure under the multi-disciplinary commitment. Game 1 reconciled as Shadowkeep. Preserved in git history.
- **v4.0 (2026-03-09):** Reduced from 16 to 4 assembly games. Preserved in git history.
- **v3.x and earlier:** 16-game curriculum. Preserved in git history.
