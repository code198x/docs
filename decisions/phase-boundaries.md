# Decision: Pedagogy Sequences, Commercial Bar Gates Phase Ends

## The decision

Within a phase, **pedagogy sets the sequence** — which technique each unit teaches, in which order, building on what came before. At every phase boundary, **the commercial bar gates the output** — the game must be a complete, playable, mid-tier full-price-bar artefact using only the techniques covered to that point.

The two principles work at different scales:

- **Per-unit:** pedagogy wins. Cleaner teaching, smaller code beats, one technique at a time.
- **Per-phase:** commercial bar wins. Whatever the unit-by-unit sequence, the phase-end output must be a complete game.

When they appear to conflict, the question is at what scale you're asking. Conflicts inside a phase mean reorder units or adjust the pedagogical scope. Conflicts at phase ends mean extend the phase or cut the game's scope — never ship an incomplete game at a phase boundary.

## Why

The previous Game 1 work failed precisely because this principle was implicit. Briefs and units progressed through techniques cleanly, but no phase-level commitment forced each phase to produce a complete game. Dash on NES ended a "phase" with one obstacle. Starfield on C64 ended with one enemy type. Exodus on Amiga ended with infrastructure but no game. Each was technically clean and pedagogically sequenced. None was complete at any phase boundary.

The fix in [commercial-bar-revamp.md](commercial-bar-revamp.md) said "phases must be complete games." This decision is the structural rule that makes that real: **the gating happens at phase boundaries, the sequencing happens within.**

Without this rule, the gravitational pull of code-led pedagogy quietly defers game-completeness phase by phase. With it, every phase has to clear a higher bar than "the code compiles and we taught a new technique."

## What this means

### In brief Section 7 (phase trajectory)

Each phase declares two things explicitly:

- **What new techniques the phase introduces** (the pedagogical content).
- **What complete game emerges at phase end** (the commercial-bar deliverable).

A phase entry that names techniques but not the resulting game is incomplete. A phase entry that names the game but skips the techniques is also incomplete. Both are required.

### In phase-end review

A phase passes review only when:

- All units in the phase pass the Definition of Done.
- The cumulative artefact is a complete game at the commercial bar for techniques covered to date — playable end-to-end, polished across all five disciplines, distributable.

"Almost a complete game" doesn't pass. "Will be a complete game once Phase N+1 lands" doesn't pass.

### When conflicts arise

The brief's Section 7 should be the place conflicts surface and resolve. If a phase's pedagogical content can't produce a complete game at the relevant bar, the response is:

1. **Adjust the phase's pedagogical scope** — split into two phases, or shift a technique to the next phase.
2. **Adjust the phase's game scope** — narrow what "complete game" means at this phase boundary (fewer rooms, fewer enemy types, smaller world).
3. **Never** "ship the phase as a tech demo and finish the game next phase." That's the failure mode this rule exists to prevent.

### Relationship to spiral-progression

Spiral progression (see forthcoming decision) means each phase revisits earlier work at a higher level. The phase-end commercial-bar gate applies at every spiral revisit too. A phase that adds animation can't ship an animated-but-half-broken game; it ships a complete game that happens to be animated.

## Drift triggers

If a phase plan or unit work shows any of these patterns, stop and re-read this decision:

- A phase boundary where the game is "almost playable" or "playable except for X."
- Brief Section 7 entries that name techniques but not a complete game.
- "Phase N ships the engine; Phase N+1 puts a game on top." Engines aren't phases.
- Cutting per-discipline polish to meet a phase-end deadline. Cut scope instead.
- "Pedagogical clarity requires we ship the units in this order even though the game won't be playable until unit 16." Reorder, or reduce, or extend the phase — but never ship a non-game at a phase boundary.
- Phase end-of-life check that asks "does the code work?" without asking "is this a complete game?"

## Status

Active. Captured 2026-05-13. Descends from [real-retro-games.md](real-retro-games.md) and [commercial-bar-revamp.md](commercial-bar-revamp.md). The structural rule that makes the multi-disciplinary commitment operational at phase scale.
