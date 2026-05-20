# Decision: Pattern Library Flow and Categorisation

## The decision

The Pattern Library is **populated from curriculum**, not the other way round. Patterns are emergent outputs of curriculum authoring — reusable techniques surfaced when a curriculum unit produces something worth lifting out for general use — rather than reference artefacts that curriculum is built against.

The library uses **technique-based categorisation** within each platform (and a cross-platform sibling), with optional language-specific buckets where the language affects implementation:

- Common technique categories: **ai, audio, framework, input, physics, rendering**.
- Language-specific buckets where useful: **assembly, basic** (on platforms with both tracks).
- A **cross-platform** directory with the same technique categories, for patterns that genuinely transcend platforms.

Polish content (title screens, attract modes, options menus, score tables) is **not** a separate category. These artefacts decompose into compositions of the existing technique categories — title screen = rendering + framework + audio + input — and patterns surface accordingly.

## Why

Two related corrections from earlier framings:

1. **Direction of flow.** Earlier discussion treated patterns as reference inputs to curriculum — "the curriculum teaches against the Pattern Library." That's backwards. Curriculum produces complete games; patterns get extracted when a technique used in curriculum proves general enough to lift out. The library accumulates over time as curriculum work surfaces reusable techniques.
2. **Categorisation scheme.** Earlier proposals invented gameplay/presentation/shell/production/optimisation buckets. The actual existing scheme decomposes "gameplay" into composable techniques (ai, physics, input, framework) and "presentation" into media types (audio, rendering). Cleaner, more useful for discovery, and already in place.

The flow-from-curriculum model also reinforces the multi-disciplinary commitment from [real-retro-games.md](real-retro-games.md). Patterns emerge across all five disciplines because curriculum units land work in all five disciplines. The library naturally captures visual patterns alongside code patterns alongside audio patterns.

## What this means

### For curriculum authoring

When a curriculum unit produces a reusable technique — a sprite-flicker-avoidance routine, an attribute-decoding pattern, a beeper SFX driver, a palette strategy — that technique is a candidate for pattern extraction. The unit's brief Section 9 (Pattern Library extractions) names the candidates; promotion to the library happens when the technique proves reusable across multiple uses.

### For pattern entries

Each pattern entry lives at `patterns/{platform}/{category}/{pattern-name}/` or `patterns/cross-platform/{category}/{pattern-name}/`. The categories are fixed (see above); the pattern names follow each category's conventions.

### For polish content

"Ship It"-type content (title screens, attract modes, options menus, score tables) is curriculum, not a library category. The curriculum may include polish-focused units or pathways; the patterns those units surface go into the existing technique categories. A title-screen unit might surface patterns in rendering (drawing the screen), framework (state-transition machine), and audio (title music driver) — three pattern entries, three categories, one composable polish artefact.

### Existing entries are correctly categorised

The current four BASIC patterns on Spectrum (seven-segment-digits, progress-bar, text-utilities, screen-frame) and the ten candidate patterns documented in `docs/curriculum/patterns/BASIC-PATTERN-ENTRIES.md` are correctly slotted into the technique categories. No structural rework needed.

## Drift triggers

If pattern-library planning shows any of these patterns, stop and re-read this decision:

- New top-level categories proposed without first checking whether the content decomposes into existing categories.
- "Polish" or "ship" suggested as a category.
- Patterns proposed in the abstract ("we should have a pattern for X") rather than extracted from curriculum work.
- Curriculum units written to "teach against" specific Pattern Library entries — that's reverse flow; units teach techniques, and patterns get extracted when units surface them.
- Cross-platform patterns proposed without a clear platform-neutral implementation; cross-platform is for genuinely platform-neutral concepts, not for "we'll port this later."

## Status

Active. Captured 2026-05-13. Lighter-touch decision; codifies existing Pattern Library architecture and corrects two earlier framing errors (direction of flow, categorisation scheme). Descends from [real-retro-games.md](real-retro-games.md) — multi-disciplinary curriculum naturally surfaces patterns across all five disciplines.
