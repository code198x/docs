# Decision: Spiral and Incremental Progression

## The decision

The curriculum uses two progression models at different scales:

- **Within a phase: incremental scaffold.** Each unit adds exactly one new capability on top of the previous. Linear, additive, one technique at a time. (The model the existing Shadowkeep design doc names; preserved.)
- **Across phases: spiral progression.** Each phase revisits earlier work at a higher level — adding animation to movement, scale to the room engine, depth to audio, richness to enemies. Earlier concepts are not just built upon but **deepened**.

The combination produces a learner trajectory that compounds rather than just stacks. Each arc returns to the keep at a richer level of sophistication.

## Why

Pure incremental progression — the model the previous design doc implicitly assumed — produces a single linear sequence: each unit adds something, nothing revisits. That works for code-led pedagogy: "in unit 7 we learn collision, in unit 8 we learn rooms, build forward." But it doesn't represent how real game development happens, and it underweights the most valuable learning beats.

Real Spectrum game development is iterative. The movement code in version 1 gets rewritten when you add animation. The room engine in version 1 gets refactored when you add 25 rooms. The audio driver evolves three times before shipping. Pretending the curriculum can be purely additive teaches a model that diverges from how the work actually happens.

Bruner's spiral curriculum model is the established pedagogical pattern for compounding skills: revisit concepts at successive levels of sophistication, with each revisit building on prior understanding rather than introducing something disconnected. Applied to retro game development, it produces a curriculum where learners genuinely deepen their grasp of each technique across phases — not because we re-teach it, but because they re-encounter it in a richer context that requires more of it.

The hybrid — incremental within, spiral across — avoids two failure modes:

- **Overwhelming learners with revisits.** Spiral *within* a phase would mean each unit reopens previous units. Pedagogically muddled.
- **Boring learners with pure addition.** Pure incremental across phases means each phase adds something new with no return to earlier material. Skills atrophy.

Both scales need their own progression model.

## What this means

### In brief Section 7 (phase trajectory)

Each phase entry declares two things:

- **What's new** (the incremental additions for the phase).
- **What revisits earlier work** (the spiral element — which earlier concepts return at a richer level).

Example for Shadowkeep Phase 3:

> *Phase 3: Animation and life.*
> *New:* 2-frame walking cycle, wandering shadow enemies, in-game beeper SFX layer.
> *Revisits:* Movement (now interleaved with animation timing), beeper driver (now handles SFX overlay), hero sprite (now multi-frame, with palette implications).

The "revisits" line is the explicit spiral declaration.

### In within-phase progression

Units inside a phase remain incremental. Unit N + 1 adds one capability on top of unit N. The "incremental scaffold" pattern preserved from the existing Shadowkeep design doc still holds — but it's now understood to apply *within* phases, not across them.

### In across-phase progression

Phase boundaries are spiral revisit points. When Phase N + 1 starts, expect to:

- Revisit some unit code from Phase N at a higher level (refactor, not rewrite from scratch).
- Find that some Phase N abstractions need generalising (the room engine that worked for 9 rooms needs work for 25).
- Bring earlier infrastructure up to the new phase's ambition level (the beeper driver that played title music now needs to interleave SFX).

This is not failure or scope creep. It's the point of spiral progression. Brief Section 7 names it; phase planning budgets for it.

### Relationship to phase-end gating

Each spiral revisit must still pass the phase-end commercial-bar gate ([phase-boundaries.md](phase-boundaries.md)). A phase that revisits animation can't ship a half-animated game; it ships a complete game that happens to be animated. Spiral progression and phase-end gating reinforce each other — both require completeness at every phase boundary.

## Drift triggers

If a phase plan or unit work shows any of these patterns, stop and re-read this decision:

- Brief Section 7 entries that only declare "what's new" without "what revisits."
- Within-phase units that try to revisit earlier work. Revisits belong at phase boundaries.
- "Phase 3 adds enemies" with no acknowledgement that movement and collision will need revisiting to accommodate them.
- Treating refactoring at phase boundaries as scope creep rather than the planned spiral revisit.
- "We're spiralling here, so we don't need to ship a complete game this phase" — the spiral gate and the commercial-bar gate are independent; both apply.
- Confusion between "incremental scaffold" (within phase) and "spiral progression" (across phases). The existing Shadowkeep design doc's incremental-scaffold language is still correct *for within-phase progression* — but the design doc as it stands is silent on the across-phase model.

## Status

Active. Captured 2026-05-13. Descends from [real-retro-games.md](real-retro-games.md) and reinforces [phase-boundaries.md](phase-boundaries.md). The Shadowkeep design doc will need a reconciliation pass to add the spiral declaration to its phase plan.
