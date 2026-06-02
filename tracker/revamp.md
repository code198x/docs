# Curriculum Revamp Tracker

Live status for the October 2026 launch + the broader Spectrum-first commercial-bar revamp. See [decisions/commercial-bar-revamp.md](../decisions/commercial-bar-revamp.md) for the strategic call.

## October 2026 target

Spectrum content targets October 2026 for Crash! Live. Close to having enough to ship — BASIC V1 done, landing page shipped, Shadowkeep (re-paced to the cell-based **Place**, pass 1) at **12 units live** — sub-arcs 1.1–1.3 done, audio (1.4) remaining. October is a target, not a hard deadline.

> **Reconciliation note (2026-06-02).** Shadowkeep was re-paced (2026-05-29, gentle-ramp) and reset this session to the **cell-based _Place_** — pass 1 of a game spanning several modules ([modules-not-games](../decisions/modules-not-games.md)), carrying Gloaming's engine; the three old engine changes (pre-shift movement, Y-sort, decoupled collision) are **relocated** to later rendering games. Unit counts are **illustrative, not targets** ([curriculum-structure](../decisions/curriculum-structure.md)). The amended decision records and the per-unit plan are current; **the engine-first / 32-64-unit / powers-of-2 detail elsewhere in this tracker is superseded** and kept for history pending a fuller tracker rewrite.

Shadowkeep is the lead game. Cadence (C64), Nightshade (NES), Exodus (Amiga) defer wholesale to post-launch. Binding decisions: [october-2026-launch-spec.md](../decisions/october-2026-launch-spec.md), [shadowkeep-32-unit-commitment.md](../decisions/shadowkeep-32-unit-commitment.md), [shadowkeep-four-arc-framing.md](../decisions/shadowkeep-four-arc-framing.md), [spectrum-basic-32-games.md](../decisions/spectrum-basic-32-games.md), [spectrum-basic-v6.4-renames.md](../decisions/spectrum-basic-v6.4-renames.md), [real-retro-games.md](../decisions/real-retro-games.md), [curriculum-structure.md](../decisions/curriculum-structure.md), [spectrum-assembly-track.md](../decisions/spectrum-assembly-track.md), [inspired-by-not-clones-naming.md](../decisions/inspired-by-not-clones-naming.md).

## At-a-glance status

| Order | Track | What | Stage | Target |
|---|---|---|---|---|
| **1** | Spectrum Assembly | **Shadowkeep — _the Place_** (pass 1) | 12 units live (1.1 keep · 1.2 rooms · 1.3 light); audio (1.4) remaining | A complete cell-based Place; counts illustrative |
| **2** | Spectrum BASIC | **Volume 1 (8 games)** | **Done.** V2 work (Cipher) started | ~~Volume 1 ships October~~ Shipped |
| **3** | Spectrum vault | Review existing + fill referenced gaps | In progress | Every reference from a shipped unit resolves |
| **4** | Spectrum landing | Polished page for QR-code visitors | **Done** (initial version) | Polish pass before event |
| 5 | C64 Assembly | Cadence | **Deferred** — [platforms/commodore-64/assembly-skeleton.md](../platforms/commodore-64/assembly-skeleton.md) | Post-launch |
| 6 | NES Assembly | Nightshade | **Deferred** — [platforms/nintendo-entertainment-system/assembly-skeleton.md](../platforms/nintendo-entertainment-system/assembly-skeleton.md) | Post-launch |
| 7 | Amiga Assembly | Exodus | **Deferred** — [platforms/commodore-amiga/assembly-skeleton.md](../platforms/commodore-amiga/assembly-skeleton.md) | Post-launch |

## The principle that governs everything

**Quality bar is non-negotiable.** If runway runs short, we ship *fewer items at full quality*, never *more items at lower quality*. Cuts are to the count, never to the bar.

This is the whole point of the project. Doing it half-arsed loses the reason to be doing it at all.

## Locked decisions across the project

- **Bar (Assembly tracks):** mid-tier full-price at game endpoint — Hewson / Gremlin / Mikro-Gen / Durell era, ~£7.95 in period. Multi-disciplinary (code + visuals + audio + level + polish co-equal). See [decisions/real-retro-games.md](../decisions/real-retro-games.md) and [decisions/curriculum-structure.md](../decisions/curriculum-structure.md).
- **Bar (BASIC track):** Usborne 1984. On-ramp confidence-builder. *Computer Spacegames* not *The Hobbit*. Kids, beginners, returners. Short programs, type-it-in, see-it-work.
- **Voice (site-wide):** magazine-class, not academic. *Crash* / *Zzap!64* / *Your Sinclair* / *ACE*. Warm, technical, opinionated, never condescending. See [specifications/writing-voice.md](../specifications/writing-voice.md).
- **Unit counts: powers of 2, nested.** Per-game 8/16/32/64/128/256/512. Don't pad to hit a number.
- **Pattern (Cadence / Nightshade / Exodus):** type-in scaffold (Lucky Number style). Black boxes open progressively.
- **Pattern (Shadowkeep):** incremental scaffold within sub-arcs, spiral progression across arcs. No typed-in engine scaffold. Deliberate divergence from the C64/NES/Amiga pattern. See [decisions/spiral-and-incremental.md](../decisions/spiral-and-incremental.md).
- **Inspired-by, not clones:** every curriculum game references canon but ships as its own design. See [decisions/inspired-by-not-clones-naming.md](../decisions/inspired-by-not-clones-naming.md).

## Cut hierarchy (if scope needs trimming)

Per [decisions/shadowkeep-32-unit-commitment.md](../decisions/shadowkeep-32-unit-commitment.md):

1. Trim Shadowkeep Arc 2 sub-arcs back-to-front (2.4 → 2.3 → 2.2 → 2.1). Arc 1 alone (16 units) is the absolute floor.
2. BASIC V1 is shipped — no longer on the cut path.
3. Cuts to landing page or vault are last resort.

Vault completeness is protected; review work is fast.

Shadowkeep Arcs 3-4 and BASIC Volumes 2-4 are post-launch work.

## Definition of Done (per unit)

A unit isn't shippable until all nine tick:

- [ ] MDX written (magazine voice, length appropriate to the unit's teaching beat)
- [ ] Code listing assembles cleanly with the platform's tools
- [ ] Code listing runs correctly on the platform's emulator (Fuse for Spectrum, etc.)
- [ ] Code listing runs correctly on real hardware (Spectrum Next for Spectrum)
- [ ] At least one screenshot captured
- [ ] All `<CodeFromFile>` snippets exist in code-samples and assemble
- [ ] "Try this" experiments tested and produce the described result
- [ ] "If it doesn't work" troubleshooting reflects actual failure modes encountered during testing
- [ ] **All cross-references resolve to real content** — vault entries, pattern library entries, and other units linked from this unit must exist (or be catalogued as required, see [lesson-references.md](lesson-references.md))

## Cross-referencing discipline

Every unit weaves in links to relevant **vault entries** (games, hardware, people, techniques, culture) and **pattern library entries** as it teaches. This is what turns a curriculum from a tutorial into a living encyclopedia of 80s computing.

**Catalogue references as we go.** Each new unit's references are logged in [lesson-references.md](lesson-references.md). The catalogue surfaces vault gaps and reuse patterns deserving care.

## Crash! Live (October 2026) — launch scope

**Launch artefacts** (each at full bar):

1. **Shadowkeep — _the Place_ (pass 1).** Cell-based atmospheric flick-adventure carrying Gloaming's engine; the three old engine changes (pre-shift movement, Y-sort, decoupled collision) are **relocated** to later rendering games. Reference points: *Atic Atac*, *Knight Lore*. See `decisions/shadowkeep-32-unit-commitment.md` (amended) + `decisions/modules-not-games.md`. **12 units shipped** (sub-arcs 1.1–1.3); audio (1.4) remaining.
2. **Spectrum BASIC Volume 1 (8 games) at Usborne bar.** **Done.** V2 work started. Volumes 2-4 ship through ~2028-29.
3. **Spectrum vault: review existing + fill gaps.** Every reference from a shipped unit must resolve. **In progress.**
4. **Polished Spectrum landing page** for QR-code visitors. **Done** (initial version; polish pass before event).

**Form factor at event:** flyers, t-shirt, QR code → site. Site is the artefact.

**Hardware testing:** ZX Spectrum Next + Fuse emulator.

---

## Shadowkeep (Spectrum Assembly) — PRIORITY 1

> **Current state (2026-06-02) — read this first; the detail below is superseded.**
> Shadowkeep is now the cell-based **_Place_** (pass 1 of a game taught across several modules — [modules-not-games](../decisions/modules-not-games.md)), carrying Gloaming's engine. **12 units authored and live:** sub-arc **1.1 Into the Keep** (Hooded Figure · First Hall/dither · A Place to Move · The Keep's Hand), **1.2 A Keep of Rooms** (Room Graph · Through the Doorway · The Hero Remembers · Three Rooms), **1.3 Mood and Light** (Light and Shadow · Furnishings · Mood through Constraint · A Keep with Character). **Remaining for the Place:** sub-arc **1.4 The Keep Has a Voice** (audio: footsteps/SFX, the gold goal, a beeper theme, the title→explore→win→title loop, real hardware). Counts are illustrative. The three engine changes and the "attribute-decoupled / tile-map collision / sprite-shifter / object-system" detail below belong to the **superseded engine-first plan** and are relocated to later rendering games; kept for history. Current sources of truth: the amended `decisions/shadowkeep-32-unit-commitment.md` + `shadowkeep-four-arc-framing.md`, `decisions/modules-not-games.md`, `decisions/curriculum-structure.md`, and `platforms/sinclair-zx-spectrum/games/shadowkeep/per-unit-plan.md`.

**Genre:** Multi-room flick-adventure in the *Atic Atac* / *Knight Lore* tradition (cell-based; atmosphere via art, light and sound).

**Constraint position:** Period-faithful throughout — attribute graphics, bitmap dithering for shade and light, hand-pixelled tiles, flick-screen rooms, beeper. See [decisions/constraint-position.md](../decisions/constraint-position.md).

**Pattern:** Builds on Gloaming's engine; one named technique per unit; spiral across *modules* (later revisits grow the keep). No typed-in engine scaffold.

**Design + reference:**
- **Brief (v3.0, cell-based Place):** [platforms/sinclair-zx-spectrum/games/shadowkeep/brief.md](../platforms/sinclair-zx-spectrum/games/shadowkeep/brief.md)
- **Per-unit plan:** [per-unit-plan.md](../platforms/sinclair-zx-spectrum/games/shadowkeep/per-unit-plan.md)
- **Beeper theme spec (sub-arc 1.4):** [beeper-spec.md](../platforms/sinclair-zx-spectrum/games/shadowkeep/beeper-spec.md)
- **Archived engine-first specs** (pre-shift/mask, Y-sort, decoupled collision — *relocated* to the rendering games): [superseded/](../platforms/sinclair-zx-spectrum/games/shadowkeep/superseded/)

### Module trajectory (the module model; counts illustrative)

Shadowkeep is a game taught across several modules. Pass 1 is *the Place*; later content becomes revisit modules slotted into the lineup after intervening games.

| Module (pass) | Content | Status |
|---|---|---|
| **the Place (pass 1)** | a lit, furnished, composed, winnable cell-based flick-adventure — 1.1 keep · 1.2 rooms · 1.3 light · 1.4 audio | **1.1–1.3 done (12 units); 1.4 remaining** |
| inhabitants (revisit) | cell-based NPCs, threat, lives | later |
| identity (revisit) | numeric HUD / digit rendering, room names, score | later |
| beyond the walls (revisits) | items, tape save/load, multiple keeps, secrets & lore, atmospheric cycles, collection endings | later |

The three old engine changes — pre-shifted/masked sprites, Y-sorted layered rendering, attribute-decoupled tile-map collision — are **relocated** to the rendering games (Smooth Motion / Overlap / Greypeak) as deprecation-pair upgrades of the Place's cell-based look, *not* built in Shadowkeep.

### Genre honesty

Shadowkeep stays in the flick-adventure tradition. Combat / classes / XP / spells / branching narrative / multi-NPC dialogue / quest state / full Singleton-class location-graph are NOT taught in Shadowkeep — they're primary teaching in V1.6 Embergate, V1.7 The Lantern Path, V1.4 Whitewinter, V3.17 Hostraider, V3.20 Edge of Iron. See [decisions/shadowkeep-four-arc-framing.md](../decisions/shadowkeep-four-arc-framing.md) for the full redistribution table.

### Outstanding work

- [x] **v2.0 brief consolidated** (2026-05-20) from v1.0 brief + Phase 1 design doc + Unit 3 plan; aligned to 32-unit / four-arc framing
- [x] **32-unit per-unit plan** landed at `platforms/sinclair-zx-spectrum/games/shadowkeep/per-unit-plan.md`
- [x] **Engineering sibling docs** landed (engineering-plan, memory-budget, object-system, sprite-shifter, tile-map)
- [x] **Beeper composition spec** landed at `platforms/sinclair-zx-spectrum/games/shadowkeep/beeper-spec.md`
- [x] **Existing 8 published Units 1-8** stay live until each is hard-replaced
- [ ] **Build engine infrastructure** (~1-2 months): sprite shifter, mask-draw primitive, Y-sort object list, decoupled tile-collision map, pixel-art tooling, music composition workflow. Build-before-publish window.
- [ ] **Author Units 1-16 (Arc 1)** with the new engine, in order, replacing existing 8 at their paths
- [ ] **Author Units 17-32 (Arc 2)**
- [ ] **Beeper composition itself** (title theme — composing against the spec; surfaces Unit 15)
- [ ] **Test each unit** on Fuse + Spectrum Next
- [ ] **Capture screenshots per unit** — automation via `emu198x-spectrum --headless --script` + `capture-spectrum-screenshot.sh`

---

## Spectrum BASIC — Volume 1 ship plan (v6.4 lineup)

Source of truth: [decisions/spectrum-basic-32-games.md](../decisions/spectrum-basic-32-games.md) (32-game lineup), [decisions/spectrum-basic-v6.4-renames.md](../decisions/spectrum-basic-v6.4-renames.md) (11 inspired-by renames). Topic counts replace unit counts; variable per game.

### Volume 1 — First Programs — SHIPPED

| # | Game | Status | Headline |
|---|---|---|---|
| 1 | Banner | **Done** | Output |
| 2 | Lucky Number | **Done** | Response |
| 3 | Oracle Stone | **Done** | Chance |
| 4 | Reflex | **Done** | Tension |
| 5 | Dice Roller | **Done** | Accumulation |
| 6 | Bright Spark | **Done** | Pattern |
| 7 | Hi-Lo | **Done** | Narrowing |
| 8 | Touchdown | **Done** | Descent (Game Loop) |

**V1 shipped.** 8 games, ~48 units.

### Volume 2 — Patterns of State (post-October)

| # | Game | Status | Headline |
|---|---|---|---|
| 9 | Cipher (was Hangman) | New | Data-Driven |
| 10 | Quiz Master | Built (16 topics; needs migration + slot shift) | Progression |
| 11 | Locksmith (was Mastermind) | New | Deduction |
| 12 | Sonar (was Battleship) | New | Search |
| 13 | Three in a Row (was Tic-Tac-Toe) | New | Adversary |
| 14 | The Caverns (was Hunt the Wumpus) | New | Atmosphere |
| 15 | Yearfall (was Hammurabi) | New | Consequences |
| 16 | Crates | New | The Rule IS the Game |

### Volume 3 — Worlds and Rules (post-October)

| # | Game | Status | Headline |
|---|---|---|---|
| 17 | Tail Chase | Built (16 topics; needs migration + slot shift) | The Game Won't Wait |
| 18 | Volley (was Pong) | New | Volley |
| 19 | Brick Bash | New | Physics |
| 20 | Drift (was Asteroids) | New (trig-canonical game) | Momentum |
| 21 | Quickstep (was Frogger) | New | Timing |
| 22 | The Hungry Maze (was Pac-Man) | New | Pursuit |
| 23 | Night Patrol | Built (16 topics; needs migration + slot shift) | Defence |
| 24 | Blockstorm | Built (32 topics; needs cut + slot shift V4→V3) | Escalation |

### Volume 4 — Stories and Systems (post-October)

V4 uses 2-deep tour-then-deepen ordering. Pt 1 short names; Pt 2 longer.

| # | Game | Status | Headline |
|---|---|---|---|
| 25 | Rooftops | New | Character |
| 26 | Stonefall | New (V3→V4 under v6.3) | Custom Worlds |
| 27 | Skyhold (was Rooftops Pt 2) | New | Rooms |
| 28 | Deepworks (was Stonefall Pt 2) | New | Designed Worlds |
| 29 | Dorin (was Dungeons of Dorin Pt 1) | Built as Dungeons of Dorin (32 topics; needs cut + slot shift + slug rename) | Generated Worlds |
| 30 | Thornwood (was Thornwood Manor Pt 1) | New | Parser |
| 31 | Dungeons of Dorin (was Dorin Pt 2) | New | Systems |
| 32 | Thornwood Manor (was Thornwood Pt 2) | New | Living Worlds |

### Orphaned MDX (Wave 3 cleanup)

These built MDX folders need rename / cut to map to the v6.4 lineup:

- `game-02-wire-panic` — replaced by Reflex
- `game-04-hot-and-cold` — replaced by Touchdown
- `game-05-letter-soup` — replaced by Cipher
- `game-07-tail-chase` — content survives, moves to slot 17
- `game-08-minefield` — replaced by Locksmith; ATTR-teaching role moves to Crates
- `game-09-brick-bash` — moves to slot 19 (scaffolding only)
- `game-10-night-patrol` — content survives, moves to slot 23
- `game-11-stonefall` — splits Pt 1 (slot 26) + Pt 2 (slot 28); content survives
- `game-12-ink-spill` — replaced by Crates
- `game-14-blockstorm` — slot V4→V3 to 24; cut from 32 → smaller
- `game-15-dungeons-of-dorin` — splits Pt 1 (slot 29) + Pt 2 (slot 31); 32 topics reshape

### Total scope (v6.4)

**32 games, ~325-455 topics, ~480-760 hours.** V1 games are 3-8 topics each; V4 games 15-30 topics each.

---

## Spectrum landing page — DONE (initial)

Initial version shipped. Polish pass needed before event: QR-landing tested on a real phone from a printed flyer.

`/sinclair-zx-spectrum/` (platform landing) and `/crash-live/` (event-specific) both planned.

---

## Spectrum vault

Pass 3b-style review of existing entries + gap-fill from `lesson-references.md`. Every reference from a shipped unit must resolve.

Three sources of gaps:
1. Obvious canonical absences (e.g., *Knight Lore*)
2. Entries referenced by lesson content per [lesson-references.md](lesson-references.md)
3. Pass 3b-style review of existing entries

Less critical than lessons — review work is fast and protected from cuts.

---

## Deferred — Cadence (C64)

See [platforms/commodore-64/assembly-skeleton.md](../platforms/commodore-64/assembly-skeleton.md). Horizontal music-driven shoot-em-up (Otocky × Hubbard tradition). Phase 1 spec + Unit 1 MDX drafted before deferral; the original 16-unit spine, SID composition spec (3-stream byte-pair format, 130 BPM / A minor, voice roles), and outstanding-work list are preserved in this file's git history (commit prior to 2026-05-20). Recover when Cadence reactivates.

## Deferred — Nightshade (NES)

See [platforms/nintendo-entertainment-system/assembly-skeleton.md](../platforms/nintendo-entertainment-system/assembly-skeleton.md). Scrolling action-platformer (Castlevania × Mega Man tradition). Concept locked: multi-screen horizontal scrolling, NROM→UNROM mapper migration, hardware sprites, APU 3-voice + DPCM, boss at Phase 1 end. Full 16-unit spine and naming pending until reactivation.

## Deferred — Exodus (Amiga)

See [platforms/commodore-amiga/assembly-skeleton.md](../platforms/commodore-amiga/assembly-skeleton.md). Lost Vikings-style 3-creature puzzle (not a Lemmings clone). Concept locked: three creatures (Climber/*Reach*, Bruiser/*Break*, Engineer/*Use*) with direct control + 1/2/3 switching; item-based puzzle vocabulary; single multi-screen level by Phase 1 end. Original concept by Steve ~1990 (working name "Ellorrs"; pre-dates Lost Vikings). Full 16-unit spine + item set + level design pending reactivation.

---

## Log

| Date | Event |
|---|---|
| 2026-05-05 | Project initiated. Strategic decisions locked. Cadence Phase 1 spec + composition spec produced. Tracker created. |
| 2026-05-05 | **Crash! Live deadline (October 2026) surfaced.** Shadowkeep promoted to priority 1; Cadence / Nightshade / Exodus deferred. |
| 2026-05-05 | **BASIC bar locked: Usborne 1984.** Distinct from assembly's commercial-bar. |
| 2026-05-05 | **Voice locked site-wide: magazine-class.** *Crash* / *Zzap!64* / *Your Sinclair* / *ACE*. |
| 2026-05-05 | **Unit counts locked: powers of 2, nested.** Per-game 8/16/32/64/128/256/512. Don't pad to hit a number. |
| 2026-05-05 | **Quality bar locked as non-negotiable.** Cut count when runway tightens, not bar. |
| 2026-05-06 | **Shadowkeep Phase 1 design doc** landed. 16-unit incremental spine, 8-cell-type attribute vocabulary, 9-room layout. **Beeper composition spec** landed. |
| 2026-05-06 | **Hero sprite locked.** Single-frame 8×8 hooded thief silhouette. Bytes: `$18, $3C, $7E, $7E, $7E, $7E, $3C, $66`. |
| 2026-05-13 | **Major revamp of strategic framing.** Seven decisions captured: real-retro-games, october-2026-vertical-slice (later superseded), phase-boundaries, constraint-position, spiral-and-incremental, curriculum-structure, pattern-library. Shadowkeep compressed to 8-unit vertical slice. |
| 2026-05-13 | **Shadowkeep Units 1 + 2 authored** at the new bar (multi-disciplinary). Unit 1 *one byte at one address*; Unit 2 *The Great Hall Rises* with four progressive stages. |
| 2026-05-18 | **Shadowkeep 32-unit two-arc commitment** — 8-unit vertical slice framing retired; commitment to *Foundations and a Place* (Arc 1, 16 units) + *Inhabitants and Identity* (Arc 2, 16 units), with three engine changes (pixel sprite movement, Y-sorted rendering, decoupled attribute/collision). Visual/atmospheric bar of 8-unit slice was not met; engine and scope rethought. |
| 2026-05-19 | **Spectrum Assembly track structured at 44 entries** across 6 volumes per `decisions/spectrum-assembly-track.md`. Three-axis design pattern (headline + concept + technique). Layer model L0 + L+1 + L+3 + L+4a + L+4b. Tech-tree with deprecation pairs. |
| 2026-05-19 | **Shadowkeep four-arc framing** added — Arcs 3-4 post-October as flick-adventure-honest content (items / multiple keeps / tape save / secrets-and-lore for Arc 3; atmospheric cycles / collection endings for Arc 4). Genre-honesty redistribution: combat / classes / parser / branching narrative redistributed to V1.6 / V1.7 / V3.17 / V3.20. |
| 2026-05-19 | **Spectrum BASIC v6.3 → v6.4.** Expanded 16 → 32 games (8 per volume). Then v6.4 inspired-by rename pass: 11 games renamed under naming convention (Magic 8-Ball → Oracle Stone, Hangman → Cipher, Mastermind → Locksmith, Battleship → Sonar, Tic-Tac-Toe → Three in a Row, Hunt the Wumpus → The Caverns, Hammurabi → Yearfall, Pong → Volley, Asteroids → Drift, Frogger → Quickstep, Pac-Man → The Hungry Maze). V1 ship doubles from 4 to 8 games for October. |
| 2026-05-19 | **Per-game scope audit** for the 44 Assembly entries — `decisions/spectrum-assembly-per-game-scope.md`. Total ~2,396 units across the track. Heavy hitters (Coldstar 96, The Marchlands 88, Embergate / Lantern Path / Whitewinter / Coreworks 80 each); small / focused (Hairline 20, Voidlift / Quoin 28). |
| 2026-05-20 | **Docs/knowledge merge complete** — knowledge/ retired entirely; project documentation lives in docs/ as a single root. Path structure system-first: `platforms/{system}/` for per-platform refs, curricula, and games; `decisions/`, `specifications/`, `tracker/`, `infrastructure/` as other top-level dirs. |
| 2026-05-20 | **Shadowkeep brief v2.0** consolidated from v1.0 brief + shadowkeep-phase-1-design + shadowkeep-unit-3-plan into a single current-state brief aligned to the 32-unit / four-arc framing. The earlier "attribute byte = game rule" mechanic retired; attribute is now visual vocabulary only, collision lives in a tile-map. |
| 2026-05-20 | **Memory hoist + tracker tidy.** `memory/spectrum-assembly.md` and `memory/spectrum-basic.md` shrunk to pointers; structural curriculum content hoisted into `docs/platforms/sinclair-zx-spectrum/{assembly,basic}.md`. `assembly.md` rewritten from v5.0 (4 games × 256 units) to current v0.3 (44 entries × 6 volumes / Shadowkeep-V1.1). Tracker rewritten to align with 32-unit Shadowkeep commitment and current docs/ layout; Cadence/Nightshade/Exodus sections collapsed to pointers (full content preserved in git history). |
| 2026-05-26 | **October reframed as target, not hard deadline.** BASIC V1 done (8 games, ~48 units); landing page shipped; Shadowkeep 8/32. Close enough that urgency feels artificial. Session-start gate removed from CLAUDE.md. Tracker status table updated to reflect current state. |
| 2026-05-29 | **Shadowkeep re-paced — gentle ramp.** `decisions/spectrum-assembly-gentle-ramp.md`: the three engine changes (pre-shift movement, Y-sort render, decoupled attribute/collision) **relocated** out of Shadowkeep to later rendering games (Smooth Motion / Overlap / Greypeak). Shadowkeep re-scoped to a **cell-based atmospheric flick-adventure** carrying the tiny game's engine; commercial bar met via art/light/sound. The old engine-first Units 1–8 thereby superseded. |
| 2026-06-02 | **Records reconciled to the module model + no-fixed-counts.** Shadowkeep re-framed as a game spanning several modules; **pass 1 = _the Place_**, Arc 2 + Arcs 3–4 become later revisit modules. Amended `shadowkeep-32-unit-commitment.md` + `shadowkeep-four-arc-framing.md`; per-unit plan gains a Module-shape section; bitmap **dithering** adopted as the stone/lighting technique (Steve's call). |
| 2026-06-02 | **Shadowkeep reset + the Place authored (Units 1–12).** Old engine-first units retired (preserved in git); module reset to a coming-soon Place, then authored end-to-end through sub-arcs 1.1–1.3 — identity, dithered stone, movement, room-as-data, room graph, edge-matched doorways, per-room persistent state (chalk), three designed rooms, dither-density lighting, furnishings, per-room mood, multi-torch character. Each verified on Emu198x; build 1742→1754 pages. Unit `game:` frontmatter corrected to 2 (matching the index-1 convention). **Remaining: sub-arc 1.4 (audio).** |
