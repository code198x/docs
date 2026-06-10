# Decision: Spectrum BASIC lineup

> **AMENDED 2026-06-10 (fixed counts retired).** The earlier **"32 games / 4 volumes / 8 games per
> volume / powers-of-2"** frame is **retired** — it contradicted the curriculum-wide
> [curriculum-structure.md](curriculum-structure.md), which fixes no game or unit counts and names
> powers-of-2 phase sizing and fixed per-platform game counts as drift triggers. What survives: the
> **named, ordered volumes as uncounted arcs** (First Programs → Patterns of State → Worlds and
> Rules → Stories and Systems), the **game lineup and progression decisions** below, and the
> **canon-first / dual-name** discipline. A volume holds as many games as genre breadth and the
> one-new-technique-per-game budget call for — not a target; counts are illustrative markers that
> firm up at build time. Order and membership live in the catalogue
> (`website/src/content/modules/sinclair-zx-spectrum/basic.yaml`); slot numbers are dropped. The
> earlier same-day amendment's one progression change stands: **UDGs are foundational from Tail
> Chase** (the first Volume-3 game) so every later action game holds custom graphics; **Blockstorm
> *deepens* UDGs** (animation + speed). The trig split (SIN/COS/PI at Drift; TAN/ASN/ACS cut) is
> unchanged and already in the catalogue.

## The decision

The Spectrum BASIC curriculum is a **sequence of games grouped into named, ordered volumes** —
First Programs, Patterns of State, Worlds and Rules, Stories and Systems — built to the
multi-disciplinary quality bar under the per-game technique budget. There are **no fixed game or
unit counts**: a volume carries as many games as its genre breadth and the
one-new-technique-per-game budget require, and counts are illustrative markers, not contracts, per
[curriculum-structure.md](curriculum-structure.md). Volume membership and order are owned by the
catalogue. The named volumes, the game lineup, and the progression decisions in this record are the
current reference; the historical expansion reasoning (why the lineup grew from the v6.2 set) is
kept below for context. The naming pass is recorded in
[spectrum-basic-v6.4-renames.md](spectrum-basic-v6.4-renames.md) and
[inspired-by-not-clones-naming.md](inspired-by-not-clones-naming.md).

October 2026 launch ships **Volume 1 (First Programs)**. The later volumes ship over the following
years.

## Why

Three independent forces pushed toward expansion:

1. **The curriculum was missing a trig-canonical game.** Brick Bash (Breakout) carried the full SIN/COS/TAN/ATN/ASN/ACS/PI introduction under v6.2 — but Breakout uses minimal trig in practice. The honest reading: the curriculum needed Asteroids (1979) as the genuine trig-using game. Adding Asteroids broke the 4-per-volume lattice.

2. **Volume 4 had structural problems.** Blockstorm (wave shooter) was stranded among V4's story-system games with "Pacing" as a stretched headline. Stonefall (Boulder Dash) was V4-sized engineering weight in a V3 slot. Stories-and-systems V4 wanted *splits* of its biggest games (Rooftops, Stonefall, Dorin, Thornwood), not single oversized slots.

3. **V1 and V2 were less Usborne-faithful than they should have been.** *Computer Spacegames* (1982) and *Practise Your BASIC* (1983) — the named pedagogy anchors — were collections of *many tiny programs*, not 4 medium ones each. V1 at 4 games was already noted as Usborne-thin under v6.2's gradual-pedagogy rationale.

Rather than cut a canonical game to fit Asteroids (every game post-canon-first audit earns its place) or accept a broken lattice, the curriculum doubled to 32. The result is *more honest* on every axis: more Usborne-tradition tiny programs in V1, more canonical turn-based games in V2, the trig-canonical game in V3 alongside other missing canon (Pong, Frogger, Pac-Man), and proper room for V4's deepest games via splits.

## The lineup

The lineup below is the current reference order; it is owned by the catalogue and is uncounted — games may be added, split, or reordered within a volume as briefs are written.

Volume 1 — First Programs: **Story Builder**, Lucky Number, **Oracle Stone**, Reflex, Dice Roller, Bright Spark, Hi-Lo, Touchdown.

Volume 2 — Patterns of State: **Cipher**, Quiz Master, **Locksmith**, **Sonar**, **Three in a Row**, **The Caverns**, **Yearfall**, Crates.

Volume 3 — Worlds and Rules: Tail Chase, **Volley**, Brick Bash, **Drift**, **Quickstep**, **The Hungry Maze**, Night Patrol, Blockstorm.

Volume 4 — Stories and Systems: Rooftops Pt 1, Stonefall Pt 1, Rooftops Pt 2, Stonefall Pt 2, Dungeons of Dorin Pt 1, Thornwood Manor Pt 1, Dungeons of Dorin Pt 2, Thornwood Manor Pt 2.

Bold marks names changed from v6.3. **Story Builder** replaces Banner (v6.5, 2026-05-25) — Banner's "just PRINT" concept didn't sustain a standalone game; Story Builder teaches the same Output concept with interactivity via INPUT and a shareable Mad Libs payoff. See [spectrum-basic-v6.4-renames.md](spectrum-basic-v6.4-renames.md) for the v6.4 rename rationale.

V4 uses **2-deep tour-then-deepen ordering**: introduce two storytelling forms (Rooftops, Stonefall), deepen both; introduce two more (Dorin, Thornwood), deepen both. The volume's midpoint marks the shift from graphical traditions to narrative traditions.

Full headline concepts and embedded concepts per game live in the curriculum spec doc and the v6.3 reframe memory entry.

## What carries forward unchanged from v6.2

The architectural foundation of v6.2 is intact:

- North Star (comprehensive vintage games-dev education; legends thread to assembly)
- Canon-first audit (every game canonical, no constructed-for-curriculum)
- Dual-name concept pattern (player-facing headline + industry term)
- Gradual pedagogy (smallest working program first, add one concept per topic)
- Headline + embedded concepts pattern
- Techniques as a first-class axis per game
- Read-alongside (legends thread) and Modern equivalents
- Polish woven through, not unit-16 ceremony
- BASIC track clean of assembly
- Topics replace unit counts (variable per game)

v6.3 is structural and naming work on top of v6.2's foundation, not a re-architecture.

## What changes from v6.2

**Five headline renames** to remove naming collisions and match the dual-name pattern:
- Touchdown: "Real-Time Reactivity (Game Loop)" → **"Descent (Game Loop)"** (clears collision with Tail Chase's "The Game Won't Wait")
- Blockstorm: "Pacing" → **"Escalation (Difficulty Curves)"**
- Stonefall: "Level Design" → **"Designed Worlds (Level Design)"**
- Night Patrol: "Opponents (AI / Opponent Behaviour)" → **"Defence (Multi-Target)"** (Pac-Man now owns Chase AI in V3)
- Hunt the Wumpus: "Hidden Information" → **"Atmosphere (Hidden Information)"**

**Stonefall/Blockstorm swap.** Blockstorm moves V4 → V3 (now V3 capstone). Stonefall moves V3 → V4. Each game now lives where its engineering weight and concept theme belong.

**Sixteen new games** join the existing 16: Banner, Magic 8-Ball, Dice Roller, Hi-Lo (V1); Battleship, TTT, Wumpus, Hammurabi (V2); Pong, Asteroids, Frogger, Pac-Man (V3); plus four V4 splits (Rooftops Pt 1+2, Stonefall Pt 1+2, Dorin Pt 1+2, Thornwood Pt 1+2).

**BASIC progression shifts.** UDGs at Tail Chase — foundational from the first Volume-3 game (amended 2026-06-10; was Blockstorm); Blockstorm deepens UDGs with animation + speed. Rooftops deepens further with sprite-plus-text. Trig (SIN/COS/PI) at Drift; TAN/ASN/ACS cut as unused-in-BASIC-games. FOR/NEXT at Dice Roller. 2D arrays at Battleship. SAVE/LOAD at Dorin Pt 2.

**Embedded concepts grow from 15 to 20:** Anticipation, Atmosphere, Trade-offs / delayed consequences, Authored experience, Emergent stories added.

## Drift triggers

Pull this decision record up before proceeding if you see any of these patterns:

- Any **fixed game or volume count** asserted as a target — "8 games per volume", "32 games", "16 games", "4 per volume". All retired; volumes are uncounted arcs sized by genre breadth + technique budget (per [curriculum-structure.md](curriculum-structure.md)).
- **Powers-of-2 / lattice "cleanliness"** invoked as a reason to add or cut a game — that aesthetic is gone. Add a game for genre breadth; cut one only if it fails the canon-first or quality bar.
- **Slot numbers** ("slot 17", "slot 31") reappearing as position identifiers — order lives in the catalogue array, not a fixed index.
- A new game proposed for the curriculum that is *constructed-for-curriculum* rather than canonical — canon-first audit still binds.
- A V4 game written as a single non-split entry (e.g., "Rooftops" without Pt 1 / Pt 2) — the 2-deep ordering depends on the splits.
- A proposal to *re-merge* a V4 Pt 1 / Pt 2 pair into one game — the splits are pedagogical, not packaging; merging undoes V4's tour-then-deepen structure.
- Any suggestion to teach machine code from a BASIC game — clean separation from Assembly track still holds (per v6.2).
- Trig functions TAN/ASN/ACS appearing in any BASIC game spec — these are cut.
- "Pacing" appearing as a *headline* concept anywhere — it is now an *embedded* concept; Escalation is Blockstorm's headline.
- UDGs introduced later than Tail Chase — incorrect under the 2026-06-10 amendment; UDGs are foundational from the first Volume-3 game, and Blockstorm/Rooftops only *deepen* them.

## Cost accepted

*(Historical — the cost reasoning that justified the v6.2→v6.3 expansion. Retained for context; the
counts below describe that expansion, not a fixed target.)*

**The V1 launch ship grew** beyond the original v6.2 set for October 2026 — adding small new First
Programs games (Magic 8-Ball, Reflex, Dice Roller, Hi-Lo, Touchdown, plus Story Builder) alongside
the two already-built games (Lucky Number, Bright Spark). The new V1 games are small (3–6 topics
each), so the authoring growth was modest. Achievable in the runway, but tighter than the v6.2 plan.

**The post-October curriculum grew substantially** — a multi-year commitment shipping over the
following years. Under [curriculum-structure.md](curriculum-structure.md) the total is governed by
the technique budget and the acceleration assumption, not a game count.

**Vault audit scope grows** — every game needs vault-thread entries. The vault audit remains a
prerequisite for the spec's launch ship.

## Related decisions

- [[spectrum-basic]] (project memory — current-state summary of the BASIC track)
- [october-2026-launch-spec.md](october-2026-launch-spec.md) (binding launch scope; Volume 1 ships)
- [commercial-bar-revamp.md](commercial-bar-revamp.md) (assembly Game 1s — separate track; carries forward unchanged)
- `website/src/content/modules/sinclair-zx-spectrum/basic.yaml` (catalogue, source of truth for *which games in which volume*; see [state-lives-in-catalogues.md](state-lives-in-catalogues.md))
- `docs/platforms/sinclair-zx-spectrum/basic.md` (curriculum spec, source of truth for *what each game teaches*)
