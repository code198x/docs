# Decision: Shadowkeep 32-Unit Arc 1+2 Commitment

**Status:** Active. Captured 2026-05-18. Descends from [commercial-bar-revamp.md](commercial-bar-revamp.md) and [real-retro-games.md](real-retro-games.md). (Supersedes an interim 8-unit vertical-slice decision from 2026-05-13; that earlier doc has been removed — git history preserves it.)

## The decision

Shadowkeep's October 2026 deliverable shifts from "8-unit vertical slice" to **32 units across two arcs of 16**: *Foundations and a Place* (Arc 1, units 1-16) and *Inhabitants and Identity* (Arc 2, units 17-32). The vertical-slice framing is retired; what ships is *Shadowkeep, Arc 1 + Arc 2: the first chapter of a longer game*, complete and artistically uncompromising.

Three engine changes are committed alongside the unit-count expansion:

1. **Pixel-level sprite movement.** The hero moves 2 or 4 pixels per frame, not 8. Pre-shifted sprite tables (or runtime shifting). Masked sprite drawing to preserve background pixels. The cell-snapped movement of the existing 8 units is retired.
2. **Back-to-front layered rendering.** A Y-sorted object list, drawn each frame. The hero passes behind pillars with lower Y; in front of pillars with higher Y. The single-layer "draw room, then hero on top" model is retired.
3. **Attribute area decoupled from collision.** Collision lives in a separate tile-map data structure. Attribute bytes become purely cosmetic — used for lighting, decoration, mood. The "attribute byte = game rule" mechanic that defined Units 5-6 of the existing slice is retired.

Together these changes lift Shadowkeep from *engine demonstration* to *commercial-bar 1987 game*. The reference points are [Atic Atac](/vault/games/atic-atac) (multi-room adventure with layered render), [Knight Lore](/vault/games/knight-lore) (atmospheric, animated character, masked sprite), and [Cybernoid II](/vault/games/cybernoid) (dense visual design, hand-crafted level art).

## Why

The 8-unit vertical-slice decision was made on 2026-05-13 under runway pressure. It produced working content — the engine demonstrably works — but the visual and atmospheric bar was not met. Screenshots of the existing Unit 8 read as *prototype*, not *game*. The hero is a static 8×8 silhouette. The walls are one stippled tile repeated. The title screen is white ROM-font text on black. There is no animation, no HUD, no decoration, no lighting, no character to the keep.

The honest diagnosis: the unit-by-unit didactic plan added one mechanic per unit and never had a unit dedicated to "make it beautiful." The vertical-slice framing was scaffolding for delivery, not a destination. With runway now visible (May → October = 5 months), the constraint shifts from *time* to *bar*. The right response is not "polish what we have" but "build the engine and the art the project actually wants."

The decision is to commit to the larger scope explicitly, document it as such, and re-frame what October ships as the *complete first chapter of Shadowkeep* — not a slice, not a demo, a real game.

## What ships in October

### Arc 1 — *Foundations and a Place* (Units 1-16)

Four sub-arcs of four units each. Each unit produces a real artistic deliverable alongside its code.

- **Sub-arc 1.1 — First Pixels (1-4):** Framebuffer fundamentals, designed stone tiles, varied wall types, tile-map data structure.
- **Sub-arc 1.2 — The Hooded Thief (5-8):** Designed hero sprite, four-frame walk cycle, pixel-level positioning, masked sprite drawing.
- **Sub-arc 1.3 — A World with Depth (9-12):** Y-sorted layered rendering, decorative objects (pillars, altars, sconces), attribute-driven lighting, the antechamber as a designed second place.
- **Sub-arc 1.4 — The Keep Stands (13-16):** Tile collision, gold pickup with sparkle, composed beeper title music, hand-pixelled title screen with logo art.

End-of-Arc-1 deliverable: a complete two-room game with atmosphere, depth, and a designed first impression. Title → play → victory → title loop.

### Arc 2 — *Inhabitants and Identity* (Units 17-32)

- **Sub-arc 2.1 — Sound and Motion (17-20):** Footstep SFX, animated doors, hero idle animation, varied floor tiles.
- **Sub-arc 2.2 — A Presence in the Dark (21-24):** First moving NPC sprite, hero-vs-NPC collision, lives and respawn, a second NPC variation.
- **Sub-arc 2.3 — A Game Knows Itself (25-28):** HUD bar (score / gold / lives), room names, score persistence, a third designed room.
- **Sub-arc 2.4 — Completion (29-32):** Atmosphere polish across all rooms, audio depth (SFX library expansion + music polish), Spectrum Next hardware testing, final presentation pass (title art polish, victory sequence, "completed" state).

End-of-Arc-2 deliverable: a three-room game with inhabitants, lives, score, HUD, atmospheric polish, and verified real-hardware playability.

## Drift triggers

If a discussion or unit shows any of these patterns, stop and re-read this decision:

1. **Extending past 32 units within October.** 32 is the commitment. Surplus time goes into polish within existing units, not new units.
2. **Adding mechanics in Arc 2 beyond the planned inhabitants / lives / score.** No inventory system, no save/load, no third-person view, no multiple keeps, no boss fights, no level select. Arc 2 is *atmosphere and threat*, not *system bloat*.
3. **Treating Arc 2 as optional or "if we have time".** Both arcs are committed. Arc 1 alone does not ship as the October deliverable.
4. **Reducing the bar within units to fit time pressure.** "We'll polish later" is the failure mode that produced the visual gap in the 8-unit slice. If a unit cannot meet the bar in its time budget, the response is to lengthen the budget — not to ship below the bar.
5. **Vertical-slice framing creeping back into marketing copy.** What ships is *"Shadowkeep, Arc 1 + Arc 2: foundations, a place, inhabitants, identity. The first chapter of a longer game."* Not a slice, not a demo, not a vertical-anything.

## What this means for the existing 8 units

The existing 8 units stay published at their current paths until replaced. Each new unit is a hard cutover at its path when the new version is ready.

**Engine evolution is the curriculum.** The new units don't presuppose the new engine — they *introduce* it. Sub-arc 1.2 introduces pixel positioning and masking (replacing the cell-snapped movement of old U4). Sub-arc 1.3 introduces layered rendering. Sub-arc 1.4's Unit 13 introduces tile-map collision (replacing the attribute-based collision of old U5).

**Publish pattern:** infrastructure first, then units in batches. The build-before-publish window is ~1-2 months of engine and pipeline work (sprite shifter, mask drawing primitive, Y-sort object list, decoupled tile-collision map, pixel-art tooling, music composition workflow). When that infrastructure lands, units are published in order — Unit 1, Unit 2, ... Unit 16 — replacing the old units one at a time. Arc 2 follows.

During the build months, visitors see a mixed-engine state: early units at the new bar, later units at the old bar. This is acceptable temporary inconsistency. The early units carry the case for the rest.

## What this means for the other launch artefacts

The October 2026 launch spec's four artefacts are unchanged in count; the Shadowkeep deliverable is the only one that grows.

- **BASIC track:** ships Volume 1 (8 games) for October per [spectrum-basic-32-games.md](spectrum-basic-32-games.md). Full curriculum is 32 games / 4 volumes; Volumes 2-4 post-October. Disciplined scoping required to keep BASIC from drifting into Shadowkeep budget.
- **Spectrum landing page:** done. `/sinclair-zx-spectrum/` and `/crash-live/` both live.
- **Spectrum vault:** done. 50+ entries reviewed/created across 10 sweep rounds. Minor touch-ups only.

## Cut hierarchy (revised)

If runway tightens, the cut order is:

1. **Trim Arc 2 sub-arc 2.4 (units 29-32).** "Completion" is partly polish; can be deferred. Arc 1 + Arc 2 sub-arcs 2.1-2.3 (28 units) is the minimum ship-able vertical.
2. **Trim Arc 2 sub-arc 2.3 (units 25-28).** HUD and room names can defer. 24 units is the next floor.
3. **Trim Arc 2 sub-arc 2.2 (units 21-24).** Inhabitants and lives defer. 20 units remains. This is the *real* lowest acceptable floor — Arc 1 plus sound/motion polish.
4. **Trim Arc 2 sub-arc 2.1 (units 17-20).** Arc 1 alone (16 units). This is genuine retreat — would require re-marketing as "Arc 1: foundations and a place, with Arc 2 coming." Avoid if at all possible.
5. **Below 16 units.** Decision-record violation. Don't do this.

Cuts apply only after a runway slip is identified. Cuts are *not* the default plan; the default plan is *both arcs, 32 units, October*.

## Out of scope (explicit)

- C64 / Cadence, NES / Nightshade, Amiga / Exodus — coming-soon cards, post-October.
- Shadowkeep Arcs 3-4 (post-October). Per [shadowkeep-four-arc-framing.md](shadowkeep-four-arc-framing.md): Arc 3 *Beyond the Walls* (items, multiple keeps, tape save, secrets-and-lore); Arc 4 *The Greater World* (atmospheric cycles, multiple keeps, collection-based endings). Combat / classes / spells / quest state / dialogue are NOT in Shadowkeep — those teach in V1.6 Embergate, V1.7 The Lantern Path, V3.17 Hostraider, V3.20 Edge of Iron.
- Pattern library work not downstream of a shipped unit's reference.
- Vault expansion beyond what shipped units cite.
- Aspirational platform totals (1024 / 2048 / 4096 across the four platforms) — direction of travel, not spec.

## Extended by

- [shadowkeep-four-arc-framing.md](shadowkeep-four-arc-framing.md) (2026-05-19) — adds Arcs 3-4 as post-October commitment (Beyond the Walls / Heroes and Stories). October ship scope and all drift triggers in this doc remain unchanged; the extension specifies Arcs 3-4 as a separate post-October commitment plus per-unit refinements to Arcs 1-2 for in-time-for-October updates.

## Anchored in

- [october-2026-launch-spec.md](october-2026-launch-spec.md) — broader launch scope (this supersedes its Shadowkeep portion).
- [commercial-bar-revamp.md](commercial-bar-revamp.md) — bar definitions per track.
- [real-retro-games.md](real-retro-games.md) — multi-disciplinary bar.
- [`docs/platforms/sinclair-zx-spectrum/games/shadowkeep/per-unit-plan.md`](../curriculum/shadowkeep-32-unit-plan.md) — full per-unit specifications.
- [`docs/tracker/revamp.md`](../curriculum/revamp.md) — live status tracker.

## Log

| Date | Event |
|---|---|
| 2026-05-18 | Decision captured. 32-unit commitment in two arcs. Three engine changes (pixel sprites, layered render, decoupled attribute) committed. Vertical-slice framing retired. BASIC track stays at 16. |
| 2026-05-19 | Extended by [shadowkeep-four-arc-framing.md](shadowkeep-four-arc-framing.md) — Arcs 3-4 added as post-October commitment. October ship scope unchanged. |
