# Decision: Shadowkeep Four-Arc Framing

> **AMENDED 2026-05-29 by [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md).**
> Shadowkeep is re-scoped to a **cell-based atmospheric** flick-adventure — which *reinforces*
> this doc's **Atmosphere (Sense of Place)** headline rather than contradicting it. The four-arc
> structure stands, and **Arcs 3–4 are already cell-based-friendly**: inventory, item-gating,
> tape save/load, hidden rooms, lore, day/night palette shifts and collection endings need no
> pre-shift / masking / Y-sort. The advanced rendering Trunk relocates to Greypeak + inserts; the
> Arc 1–2 per-unit refinements (point 4 below) are re-paced to cell-based atmosphere.

> **AMENDED AGAIN 2026-06-02 by [modules-not-games.md](modules-not-games.md) +
> [curriculum-structure.md](curriculum-structure.md).** The four arcs are **illustrative chapters,
> not fixed 16-unit blocks**, and they now map onto the **module model**: a game can be taught by
> several modules, and the four arcs are **separate modules**, not one ~64-unit game. **Arc 1 = the
> `shadowkeep` pass-1 module (*the Place*)**, authored for October as an extension of Gloaming;
> **Arcs 2–4 = later `game: shadowkeep` revisit modules** (pass 2+), slotted into the lineup after
> intervening games, each within its own 1–2-majors budget. The "~64 units" total below is a
> direction-of-travel marker, not a count. The genre-honesty table and drift triggers (no combat /
> classes / spells / quest-state / branching narrative in Shadowkeep) **all still bind** — the
> module split changes packaging and pacing, not what Shadowkeep *is*.

## The decision

Extends [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md) with a **full four-arc framing** for Shadowkeep:

- **Arc 1 — *Foundations and a Place*** (Units 1-16) — unchanged, October ship
- **Arc 2 — *Inhabitants and Identity*** (Units 17-32) — unchanged, October ship
- **Arc 3 — *Beyond the Walls*** (Units 33-48) — new, post-October Year 1 (~2027-28)
- **Arc 4 — *Heroes and Stories*** (Units 49-64) — new, post-October Year 2 (~2028-29)

October ship scope is UNCHANGED — still 32 units, Arcs 1+2 only. The drift triggers in the 32-unit commitment doc ("Extending past 32 units within October" is still binding) all hold. This decision extends Shadowkeep's *full-game* commitment to four arcs while keeping the *October ship* commitment exactly as it was.

## Why

Three reasons:

1. **The "first chapter of a longer game" framing in the existing commitment doc needed a concrete plan.** The current doc has "Shadowkeep Arc 3+ ... post-October" in out-of-scope. Naming Arcs 3-4 turns vague "first chapter" into a real design.
2. **Cross-game prerequisite seeding.** Several other curriculum games (V2.10 multi-screen platformer, V1.4 strategic procedural, V1.6 action-RPG, V1.7 parser per [spectrum-assembly-track.md](spectrum-assembly-track.md)) depend on techniques Arcs 3-4 introduce (tape save/load, location-graph data, combat state machine, quest state, item systems). With Arcs 3-4 explicit, the tech-tree is honest.
3. **The 32-unit commitment underplays Shadowkeep's role.** Memory's direction-of-travel implies ~110-220 units per game on average across the curriculum. Shadowkeep at 32 was an October-relevant commitment, not a per-game total. Four-arc framing brings Shadowkeep to ~64 units — still conservative against direction-of-travel.

## What this means

### Arc 3 — *Beyond the Walls* (Units 33-48)

*Thematic identity: the keep is no longer alone. Items matter, places connect, the hero remembers, the world holds secrets.*

- **Sub-arc 3.1 — *Items that Matter*** (33-36): inventory state, item-gated transitions, inventory limits, item effects (torch / key / glyph). *Sabre Wulf, Knight Lore, Pentagram traditions.*
- **Sub-arc 3.2 — *Beyond One Keep*** (37-40): outdoor tile set, multi-location traversal, per-location state persistence, return-and-find mechanic. *(Location-graph data structure and full day/night cycle are V1.4 Whitewinter's primary teaching — Shadowkeep uses a lighter mood-palette variation.)*
- **Sub-arc 3.3 — *The Persistent Hero*** (41-44): tape save, tape load + validation, in-memory save/pause/resume, save/load menu UI. *Pentagram + standard late-86 tradition.*
- **Sub-arc 3.4 — *Secrets and Lore*** (45-48): hidden rooms (Atic Atac secret-room mechanic), lore fragments (collectable atmospheric text), active items affecting the world (torch lights nearby cells, key opens door, glyph reveals secret), the bestiary (visual collection of creatures encountered). *Flick-adventure atmospheric depth. NOT dialogue trees or quest states.*

**Arc 3 ship gate:** Inventory with 6+ item types; multiple-location traversal with 2-3 areas beyond original keep; working tape save/load on real hardware; secrets-and-lore system with hidden content the player must discover.

### Arc 4 — *The Greater World* (Units 49-64)

*Thematic identity: the keep is part of something larger. Time, place, completion all matter.*

- **Sub-arc 4.1 — *Atmospheric Cycles*** (49-52): time-of-day cycle affecting which rooms/NPCs active, weather and mood states, palette shifts per state, the keep's seasons (long-cycle environmental change). *Knight Lore's atmospheric polish extended.*
- **Sub-arc 4.2 — *Multiple Keeps*** (53-56): outdoor traversal between locations, a second keep with distinct character/tile set, return mechanic, a third keep (deeper / more dangerous). *Pentagram + Underwurlde tradition.*
- **Sub-arc 4.3 — *Endings*** (57-60): collection-based unlock (find all lore items / artifacts for true ending), mediocre ending if incomplete, true ending if complete, second-playthrough content. *Atic Atac's completion-based win condition extended. Endings are completion-based, NOT branching-narrative based.*
- **Sub-arc 4.4 — *Completion*** (61-64): 64-unit polish discipline, complete soundtrack, shipping cassette artefact (Spectrum Next + TZX 48K), final completed-state machine.

**Arc 4 ship gate:** Time-of-day cycle working; 2-3 distinct keeps beyond Shadowkeep; collection-based true-ending unlock; final polished build on real Spectrum Next + TZX 48K.

### Per-unit refinements to Arcs 1-2 (in time for October)

The Arc 1-2 plan benefits from refinements identified during the v0.1 brainstorm audit. These are *prose-and-naming changes*, not new units — they fit within the existing 32-unit budget:

1. **Headline at doc header:** "Shadowkeep — Volume 1, Game 1. Headline: **Atmosphere (Sense of Place)**."
2. **Design-concept names per unit.** Each unit's title becomes the design concept the unit teaches; technique sits below as "Code primitive." Example: U11 — title *Mood through Constraint*; code primitive `compute_lighting()`.
3. **Read-Alongside + Modern Equivalent lines per unit.** Each unit cites a specific Atic Atac / Knight Lore / Cybernoid II moment that descends from the technique, and a modern game using the same design idea.
4. **Six unit refinements:**
   - U14 — explicitly introduces **SFX driver** (was implicit in U17 footsteps)
   - U15 — pure beeper composition focus (driver moved to U14)
   - U18 — reframed: per-object animation state machine (not just door creak reinforcement)
   - U20 — reframed: variety as mood palette (not loose "floor and shadow")
   - U24 — reframed: **behaviour tables + hazard variation** (not just "second NPC")
   - U28 — reframed: **room-graph data structure + per-room theming** (not just "third room"); seeds Arc 3.2 and V2.10's load-bearing techniques
5. **Embedded Design Concepts section** added — Atmosphere through restraint, Authored level design, Animation budget, Identity through silhouette, Audio as place, Polish as discipline — listing surfacing units.
6. **Extend per-unit Definition of Done** with "Headline + design concept made explicit in the prose" (point 10).

These refinements need to land in [shadowkeep-32-unit-plan.md](../platforms/sinclair-zx-spectrum/games/shadowkeep/per-unit-plan.md) before October to give the launch the design-concept-clarity bar.

## Genre honesty — what Arcs 3-4 are NOT

Initial drafts of Arcs 3-4 (within the brainstorm) included combat depth, character classes, XP/leveling, spell systems, branching narrative, multi-NPC dialogue, and quest-state machines. **None of these are Shadowkeep's tradition.** Atic Atac, Knight Lore, Sabre Wulf, Pentagram, Underwurlde — none used those mechanics. Those techniques belong to:

| Technique | Primary home (curriculum game) |
|-----------|--------------------------------|
| Combat state machine | V3.20 Edge of Iron (Way of the Exploding Fist tradition) |
| Spell system | V1.6 Embergate (Firelord / action-RPG tradition) |
| Projectile in object list | V3.17 Hostraider (Cybernoid II — V3 shooters) |
| Class data + selection | V1.6 Embergate |
| XP / level system | V1.6 Embergate |
| Class-conditional behaviour | V1.6 Embergate |
| Item-class binding | V1.6 Embergate |
| Menu-based dialogue | V1.7 The Lantern Path (Hobbit-class parser) |
| Quest state | V1.7 The Lantern Path |
| Multi-NPC dialogue | V1.7 The Lantern Path |
| Branching narrative flags | V1.7 The Lantern Path |
| Multiple endings (narrative-branching) | V1.7 The Lantern Path |
| Main quest state machine | V1.7 The Lantern Path |
| Location-graph data | V1.4 Whitewinter (Lords of Midnight) |
| Full day/night cycle (Singleton-class) | V1.4 Whitewinter |

Shadowkeep's Arcs 3-4 (revised above) instead deepen the **flick-adventure** tradition: items that matter, multiple keeps, atmospheric cycles, secrets and lore, collection-based endings. Cleaner curriculum-wide; honest with Shadowkeep's canon.

## Drift triggers

- **Adding combat / classes / spells / quest-state / branching narrative to Shadowkeep** in any future session or unit work. These belong to V1.6 / V1.7 / V3.17 / V3.20 per the genre honesty table above. If you find yourself reaching for these in Shadowkeep, stop — you've drifted.
- **Treating Arcs 3-4 as October scope.** They're post-October, period. The October drift triggers all still bind.
- **Building games that depend on Arcs 3-4 techniques** (V2.10 Hollowhalls inherits tape save) *before* Arc 3 ships — that game would have to re-derive. Either wait, or re-derive consciously.
- **Re-scoping Arcs 3-4 to fit a smaller timeline.** Arc scope is what it is; if timeline slips, that's a separate decision, not a re-scope.
- **Treating Shadowkeep as "just" 32 units** in long-horizon planning. The October ship is 32; the full Shadowkeep is 64.

## Status

Active. Captured 2026-05-19. Same-day revision applied to Arcs 3.4 and 4 after honest-question audit identified genre-drift (combat / classes / branching narrative moved to V1.6 / V1.7 / V3.17 / V3.20 where canonically primary). Extends [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md) — does not supersede. Amended 2026-05-29 by [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md) — Shadowkeep re-scoped to cell-based atmosphere; four-arc structure and Arcs 3–4 stand; advanced rendering Trunk relocated to Greypeak. Amended again 2026-06-02 by [modules-not-games.md](modules-not-games.md) + [curriculum-structure.md](curriculum-structure.md) — four arcs reframed as illustrative chapters mapping onto separate modules (Arc 1 = pass-1 *the Place*; Arcs 2–4 = later revisit modules); counts illustrative; genre-honesty table and drift triggers unchanged. Anchored in [[spectrum-assembly]] (current-state Assembly summary).

Per-unit refinements (point 4 above) need application to `docs/platforms/sinclair-zx-spectrum/games/shadowkeep/per-unit-plan.md` as the next concrete step. The redistributed techniques become primary teachings in their natural games when those games are spec'd.
