# Decision: Multi-disciplinary Commitment

## The decision

Code198x builds real retro games, not toy examples. Every unit and every brief considers **code, visual design, audio, level design, and polish** in equal measure. A unit is complete when all five disciplines have landed at the relevant phase's commercial bar, not just when the code compiles.

## Why

The commercial bar set in [commercial-bar-revamp.md](commercial-bar-revamp.md) said games must be shippable in their era — but the briefs and units that grew under that rule remained code-led. The technique-first framing produced Phase 1 work that was technically clean but visually modest, sonically sparse, and pedagogically isolated. Shadowkeep Phase 1 at 9 rooms with single-frame sprites and no per-room visual direction is the immediate symptom: it claimed "1984 Ultimate-tier" while shipping at Mastertronic-budget scale.

The fix isn't more units. It's elevating the disciplines that briefs and units silently underweighted. Real Spectrum games — Knight Lore, Sabre Wulf, Head Over Heels — were not "code with visuals applied later." Their visual ambition, audio composition, and level design were authored at the same bar as the code, often by the same people, simultaneously.

Code198x teaches the *production* of real retro games. That requires the disciplines to be co-equal from the brief downward.

## What this means

### In briefs

Each game's brief declares targets for all five disciplines explicitly, not just code. Visual direction, audio direction, level design direction, and polish direction are first-class sections of the brief, not commentary attached to code work.

### In units

Each unit considers what it contributes across all five disciplines, not just which Z80/6502/68000 concept it introduces. Some units are code-led (mostly new technique); some are discipline-led (mostly visual or audio work). Both kinds count as units.

### In review

A unit is reviewable only when every discipline has landed at the relevant bar. "The code is correct" is necessary but not sufficient. Visual screenshots, audio output, level-design choices, and polish all factor into completeness.

### In economics

Multi-disciplinary units cost 2–3× the authoring time of code-led units. This is the correct cost of the commitment. The unit-count budgets in `docs/curriculum/` were sized for code-led work and need rebalancing under this decision — see the forthcoming curriculum-structure decision.

## Relationship to other decisions

- **Builds on** [commercial-bar-revamp.md](commercial-bar-revamp.md). That decision said "games must be commercially shippable." This decision sharpens it: shippable across all disciplines simultaneously.
- **The "commercial bar" itself sharpens.** The previous decision said "budget label 1986–1991." Under this decision the curriculum endpoint is **mid-tier full-price** (Hewson, Gremlin, Mikro-Gen, Durell era, ~£7.95 in period) — see the forthcoming curriculum-structure decision.

## Drift triggers

If a brief or unit shows any of these patterns, stop and re-read this decision:

- "The visuals can come later" / "polish goes in a separate pass" / "for now, use placeholder art."
- Brief Section 5 (Constraint position) is filled in detail but the Visual / Audio / Level / Polish direction sections are sketchy or absent.
- A unit that introduces a code concept but doesn't say what the unit's output *looks*, *sounds*, or *plays* like.
- Compounding language: "we'll get to the audio in Phase N" where N > current phase.
- Phrases like "tech demo" or "scaffolding for later" without an accompanying "and the visual/audio/level work that ships with it."
- Time pressure leading to "let's just ship the code and iterate on look later" — that's the failure mode this decision exists to prevent.

## Status

Active. Captured 2026-05-13. Master decision; subsequent decisions on brief format, spiral progression, and curriculum structure descend from this.
