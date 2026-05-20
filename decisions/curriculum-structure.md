# Decision: Curriculum Structure

## The decision

The curriculum's per-platform scope is locked at:

- **4 platforms** (Spectrum, C64, NES, Amiga) for the assembly track.
- **4 games per platform**, each at the multi-disciplinary commercial bar.
- **256 units per game**, totalling 1,024 units per platform and 4,096 units across the curriculum.

The quality bar at the endpoint of each game's full 256 units is **mid-tier full-price** — the £7.95 1987 Hewson/Gremlin/Mikro-Gen/Durell tier. Real commercial product, ambitious, not pretending to be Ultimate's absolute top.

Internal phase structure is per-game brief. Phase sizes must be powers of 2 (8, 16, 32, etc.). Each game's brief sets its own phase trajectory; there is no universal "Phase 1 = N units" rule. Shadowkeep's Phase 1 commitment is Arc 1 at 16 units (see [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md)).

The total represents roughly the same authoring time as the previous 1,408-unit-per-platform plan, because multi-disciplinary units are 2–3× the per-unit work of code-led units. The new bar doesn't cost more total time; it produces fewer-but-better games for the same time.

## Why

Earlier curriculum versions oscillated between 16-game tracks (v3.0) and 4-game tracks (v4.0). The current 4-game structure is the right cut — each game can carry distinct platform-defining ambition (Spectrum: attribute system, software pixel scrolling, isometric, capstone production). But the v4.0 per-game unit counts (128/256/512/512) were sized for code-led work.

Under [real-retro-games.md](real-retro-games.md), multi-disciplinary units cost 2–3× their code-led predecessors. At those costs, the v4.0 counts compound to multi-decade authoring time even at sustained pace. Reducing per-game count is the only honest move that doesn't compromise the quality bar.

256 units per game is the target where:

- The game credibly reaches mid-tier full-price scale (~80–300 rooms or equivalent gameplay scope, animated sprites, beeper + AY music, custom loaders, multi-level structure).
- The authoring time per game is commensurate with what real mid-tier Spectrum/C64/NES/Amiga studios produced in 3–6 person-months.
- The full curriculum (4 × 4 × 256 = 4,096 units) remains within the same total authoring envelope as the previous code-led plan.

## What this means

### Per-platform scope

- **Spectrum:** Shadowkeep (Game 1), then three more games. Game 2 was Ionfire (scrolling shmup, 256 units in v4.0); Game 3 was Grimstone (isometric, 512); Game 4 was Dawnreach (capstone, 512). All rescope to 256; specific ambition recalibrates per game when each brief is touched.
- **C64:** Cadence (Game 1), then three more games sized at 256 each. Game 2-4 TBD.
- **NES:** Nightshade (Game 1), then three more games sized at 256 each. Game 2-4 TBD.
- **Amiga:** Exodus (Game 1), then three more games sized at 256 each. Game 2-4 TBD.

### Per-game phase structure

Phase trajectories are declared in each game's brief. Phase sizes are powers of 2 (8, 16, 32, etc.). The number and shape of phases per game depends on how the game's spiral progression naturally divides — there is no universal pattern.

Brief Section 7 (phase trajectory) declares the per-game phase breakdown. Shadowkeep's trajectory is the worked example: Arcs 1+2 at 16 units each for October (32 total), with Arcs 3+4 post-October. See [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md) and [shadowkeep-four-arc-framing.md](shadowkeep-four-arc-framing.md).

For some games, fewer larger phases may make more sense than many small ones. The brief decides.

### Acceleration assumption

The 4,096-unit total is only viable if authoring accelerates as the project matures. Specifically:

- **Pattern reuse** compounds across games on the same platform.
- **Brief format and authoring workflow** mature, reducing per-unit overhead.
- **Visual/audio infrastructure** built for Game 1 generalises to Game 2.
- **LLM-assisted authoring** improves over the project's lifespan.
- **Eventually, contributors and a community** generate patterns and reduce the solo-authoring load.

Realistic acceleration likely brings later games to 60–70% of Game 1's authoring time per platform — not the 10× speedup that would make 4,096 units a short project. The bet is that *combined* acceleration sources bend the curve enough to make the total viable across years rather than decades.

**This assumption is load-bearing.** If acceleration doesn't materialise, scope must be cut — fewer games per platform, fewer platforms, or longer timeline. The decision tree for that scenario is per-platform: if a platform's Game 1 takes longer than projected, defer Games 2–4 on that platform until acceleration materialises elsewhere first.

### Relationship to existing curriculum docs

The current `docs/platforms/sinclair-zx-spectrum/assembly.md` (v4.0, 2026-03-09) has per-game unit counts of 128/256/512/512. Those revise to 256/256/256/256. The accompanying "concept," "skills taught," and "why" copy for Games 2–4 will need reconciliation when each game's brief is touched in turn — particularly Game 3 (Grimstone, isometric adventure), which was sized for Knight Lore scale and may need design adjustment to fit 256 units. That reconciliation is forthcoming work, not blocked on this decision.

The curriculum doc previously named Game 1 as "Gravelight" (single-screen platformer) while implementation was Shadowkeep. Reconciliation completed 2026-05-13; spec is now at v5.0 and aligned. (Historical: the original v4.0 Dawnreach concept assumed Game 1 was a platformer; v5.0 flags the design implication of the Game 1 change for Dawnreach's eventual brief work.)

## Drift triggers

If curriculum-level planning shows any of these patterns, stop and re-read this decision:

- A new game proposed at >256 units without explicit justification and a scope-cut elsewhere.
- A new platform added without acknowledging it adds 1,024 units to the total.
- Acceleration treated as guaranteed rather than load-bearing assumption.
- Per-game scope creeping toward Ultimate top-tier (Knight Lore / Head Over Heels scale with multi-frame everywhere) — that's a 256+ unit ambition, not a 256-unit ambition.
- Per-platform game count creeping past 4.
- "Just one more game" or "let's also do platform X" without budget reconciliation.

## Status

Active. Captured 2026-05-13. Descends from [real-retro-games.md](real-retro-games.md). The structural commitment that operationalises the multi-disciplinary bar at curriculum scale. Per-platform curriculum docs now live under `docs/platforms/{system}/`.
