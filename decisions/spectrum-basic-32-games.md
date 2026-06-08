# Decision: Spectrum BASIC 32-game lineup (v6.4)

## The decision

The Spectrum BASIC curriculum ships **32 games across 4 volumes, 8 games per volume**. Powers-of-2 hold per-volume (8) and total (32). Decided 2026-05-19 during a concept-progression brainstorm pass. v6.4 (2026-05-19) supersedes v6.3 same day with the [inspired-by-not-clones-naming.md](inspired-by-not-clones-naming.md) rename pass applied — see [spectrum-basic-v6.4-renames.md](spectrum-basic-v6.4-renames.md) for the 11 renamed games. Supersedes the v6.2 16-game / 4-per-volume lineup.

October 2026 launch ships **Volume 1 only — 8 games**. Volumes 2-4 ship through approximately 2028-29.

## Why

Three independent forces pushed toward expansion:

1. **The curriculum was missing a trig-canonical game.** Brick Bash (Breakout) carried the full SIN/COS/TAN/ATN/ASN/ACS/PI introduction under v6.2 — but Breakout uses minimal trig in practice. The honest reading: the curriculum needed Asteroids (1979) as the genuine trig-using game. Adding Asteroids broke the 4-per-volume lattice.

2. **Volume 4 had structural problems.** Blockstorm (wave shooter) was stranded among V4's story-system games with "Pacing" as a stretched headline. Stonefall (Boulder Dash) was V4-sized engineering weight in a V3 slot. Stories-and-systems V4 wanted *splits* of its biggest games (Rooftops, Stonefall, Dorin, Thornwood), not single oversized slots.

3. **V1 and V2 were less Usborne-faithful than they should have been.** *Computer Spacegames* (1982) and *Practise Your BASIC* (1983) — the named pedagogy anchors — were collections of *many tiny programs*, not 4 medium ones each. V1 at 4 games was already noted as Usborne-thin under v6.2's gradual-pedagogy rationale.

Rather than cut a canonical game to fit Asteroids (every game post-canon-first audit earns its place) or accept a broken lattice, the curriculum doubled to 32. The result is *more honest* on every axis: more Usborne-tradition tiny programs in V1, more canonical turn-based games in V2, the trig-canonical game in V3 alongside other missing canon (Pong, Frogger, Pac-Man), and proper room for V4's deepest games via splits.

## The lineup

Volume 1 — First Programs (slots 1-8): **Story Builder**, Lucky Number, **Oracle Stone**, Reflex, Dice Roller, Bright Spark, Hi-Lo, Touchdown.

Volume 2 — Patterns of State (slots 9-16): **Cipher**, Quiz Master, **Locksmith**, **Sonar**, **Three in a Row**, **The Caverns**, **Yearfall**, Crates.

Volume 3 — Worlds and Rules (slots 17-24): Tail Chase, **Volley**, Brick Bash, **Drift**, **Quickstep**, **The Hungry Maze**, Night Patrol, Blockstorm.

Volume 4 — Stories and Systems (slots 25-32): Rooftops Pt 1, Stonefall Pt 1, Rooftops Pt 2, Stonefall Pt 2, Dungeons of Dorin Pt 1, Thornwood Manor Pt 1, Dungeons of Dorin Pt 2, Thornwood Manor Pt 2.

Bold marks names changed from v6.3. **Story Builder** replaces Banner (v6.5, 2026-05-25) — Banner's "just PRINT" concept didn't sustain a standalone game; Story Builder teaches the same Output concept with interactivity via INPUT and a shareable Mad Libs payoff. See [spectrum-basic-v6.4-renames.md](spectrum-basic-v6.4-renames.md) for the v6.4 rename rationale.

V4 uses **2-deep tour-then-deepen ordering**: introduce two storytelling forms (Rooftops, Stonefall), deepen both; introduce two more (Dorin, Thornwood), deepen both. Volume midpoint at slot 28/29 marks the shift from graphical traditions to narrative traditions.

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

**BASIC progression shifts.** UDGs at Blockstorm (slot 24) not Rooftops. Trig (SIN/COS/PI) at Asteroids (slot 20); TAN/ASN/ACS cut as unused-in-BASIC-games. FOR/NEXT at Dice Roller (slot 5). 2D arrays at Battleship (slot 12). SAVE/LOAD at Dorin Pt 2 (slot 31).

**Embedded concepts grow from 15 to 20:** Anticipation, Atmosphere, Trade-offs / delayed consequences, Authored experience, Emergent stories added.

## Drift triggers

Pull this decision record up before proceeding if you see any of these patterns:

- "16 games" or "4 games per volume" in any newly-written content — these are v6.2 framings, superseded.
- A proposal to *cut* a v6.3 game to "restore powers-of-2 cleanliness" — the lattice already holds at 8-per-volume and 32-total; cutting is not for cosmetics.
- A new game proposed for the curriculum that is *constructed-for-curriculum* rather than canonical — canon-first audit still binds.
- A V4 game written as a single non-split entry (e.g., "Rooftops" without Pt 1 / Pt 2) — the 2-deep ordering depends on the splits.
- A proposal to *re-merge* a V4 Pt 1 / Pt 2 pair into one game — the splits are pedagogical, not packaging; merging undoes V4's tour-then-deepen structure.
- Any suggestion to teach machine code from a BASIC game — clean separation from Assembly track still holds (per v6.2).
- Trig functions TAN/ASN/ACS appearing in any BASIC game spec — these are cut.
- "Pacing" appearing as a *headline* concept anywhere — it is now an *embedded* concept; Escalation is Blockstorm's headline.
- UDGs introduced in a game before slot 24 (Blockstorm) — incorrect under v6.3.

## Cost accepted

**V1 launch ship doubles** from 4 games to 8 games for October 2026. Six new V1 games to write (Banner, Magic 8-Ball, Reflex, Dice Roller, Hi-Lo, Touchdown) plus two existing built games to migrate (Lucky Number, Bright Spark). All new V1 games are small (3-6 topics each), so the topic-count growth is roughly 50%, not 100%. (Post visual-enhancement-pass: Hi-Lo grows to **11** units with new unit "The Cards"; Touchdown grows to **14** units with new unit "The View".) Achievable in the five-month runway but tighter than v6.2's V1 ship plan.

**Post-October curriculum doubles** from 16 games to 32. Multi-year commitment, ship through approximately 2028-29 instead of 2027-28.

**Vault audit scope grows** — every new game needs vault-thread entries. The vault audit remains a prerequisite for the spec's launch ship.

## Related decisions

- [[spectrum-basic]] (project memory — current-state summary of the BASIC track)
- [october-2026-launch-spec.md](october-2026-launch-spec.md) (binding launch scope; Volume 1 ships)
- [commercial-bar-revamp.md](commercial-bar-revamp.md) (assembly Game 1s — separate track; carries forward unchanged)
- `website/src/content/modules/sinclair-zx-spectrum/basic.yaml` (catalogue, source of truth for *which games in which volume*; see [state-lives-in-catalogues.md](state-lives-in-catalogues.md))
- `docs/platforms/sinclair-zx-spectrum/basic.md` (curriculum spec, source of truth for *what each game teaches*)
