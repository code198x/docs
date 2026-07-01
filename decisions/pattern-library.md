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

Each pattern entry lives at `patterns/{platform}/{track}/{category}/{pattern-name}/`, where `{track}` is the language (`assembly`, `basic`, `amos`, `blitz`…). Cross-platform patterns live at `patterns/cross-platform/{category}/{pattern-name}/` — no track, because they span languages by definition. The categories are fixed (see above); the pattern names follow each category's conventions. See the [2026-07-01 amendment](#amendment-2026-07-01-uniform-track-level) for why the track level is universal.

### For polish content

"Ship It"-type content (title screens, attract modes, options menus, score tables) is curriculum, not a library category. The curriculum may include polish-focused units or pathways; the patterns those units surface go into the existing technique categories. A title-screen unit might surface patterns in rendering (drawing the screen), framework (state-transition machine), and audio (title music driver) — three pattern entries, three categories, one composable polish artefact.

### Existing entries are correctly categorised

The four BASIC patterns on Spectrum (seven-segment-digits, progress-bar, text-utilities, screen-frame) and the further candidate BASIC patterns are correctly slotted into the technique categories. The *categorisation* was always right; only the *track placement* changed — see the [2026-07-01 amendment](#amendment-2026-07-01-uniform-track-level), which extended the track level to every platform.

## Drift triggers

If pattern-library planning shows any of these patterns, stop and re-read this decision:

- New top-level categories proposed without first checking whether the content decomposes into existing categories.
- "Polish" or "ship" suggested as a category.
- Patterns proposed in the abstract ("we should have a pattern for X") rather than extracted from curriculum work.
- Curriculum units written to "teach against" specific Pattern Library entries — that's reverse flow; units teach techniques, and patterns get extracted when units surface them.
- Cross-platform patterns proposed without a clear platform-neutral implementation; cross-platform is for genuinely platform-neutral concepts, not for "we'll port this later."

## Amendment (2026-07-01): uniform track level

**What changed.** The language track (`assembly`, `basic`, …) is now a level in **every** platform's path, not only platforms that already hold patterns in two languages. C64, Amiga and NES patterns moved from `{platform}/{category}/` to `{platform}/assembly/{category}/`, matching the Spectrum's existing `assembly/` + `basic/` split. Cross-platform is the sole exception — it spans languages, so it stays `cross-platform/{category}/`.

**Why this supersedes "no structural rework needed."** The original decision inserted a track bucket only where a platform *already* had both tracks in the library. That left C64 and Amiga flat — but both are multi-track platforms whose curricula (C64 BASIC, Amiga AMOS and Blitz) are already live, so their BASIC/AMOS/Blitz patterns are a near-certain near-term output, not a hypothetical. Under the old rule each of those would have forced a per-platform migration (moving existing assembly patterns into an `assembly/` bucket) at the moment the first second-track pattern landed. Making the track level universal now pays that cost once, while the library is small (~29 patterns), and yields a rule that is stateable without exceptions: *every pattern is `platform/track/category/name`*. NES keeps a single `assembly/` track by its nature — no BASIC dev target for the console ever existed — accepting one semantically-thin level in exchange for a layout with no special cases.

**Why not a frontmatter field instead of a path segment.** Track has to stay in the path: the same technique (e.g. a game loop) will exist in both BASIC and assembly, and without the directory split those same-named entries would collide at one URL. A `track` frontmatter field could be *added* later for browse-by-language, but it cannot *replace* the path segment.

**Cost paid.** ~29 pattern files moved; body links rewritten to insert `/assembly/`. Routing, breadcrumbs and filtering read the platform/category/difficulty from frontmatter, so only URLs changed; `evolution`/`related` use bare slugs and were unaffected. Pre-launch, so URL churn carries no external cost.

## Status

Active. Captured 2026-05-13; amended 2026-07-01 (uniform track level — see above). Lighter-touch decision; codifies existing Pattern Library architecture and corrects two earlier framing errors (direction of flow, categorisation scheme). Descends from [real-retro-games.md](real-retro-games.md) — multi-disciplinary curriculum naturally surfaces patterns across all five disciplines.
