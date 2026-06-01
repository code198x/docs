# Content Model

How units, tracks, modules, and platforms relate. This page captures patterns and gotchas from applying the curriculum spec.

## Hierarchy

**Platform** → **Track** → **Module** → **Unit**

- Platforms: C64, ZX Spectrum, Amiga, NES
- Tracks: assembly, BASIC (where applicable)
- Modules: the unit of sequencing. A module has a `kind` — `game` (teaches a buildable game), `teaching` (a non-game on-ramp like *Meet the Machine*), or `interval` (a short between-game step). One game can span several modules (revisits); a module may teach no game. See [decisions/modules-not-games.md](../decisions/modules-not-games.md).
- Units: each produces a runnable result; count per module varies. Unit counts are illustrative markers, not targets (see [decisions/spectrum-assembly-gentle-ramp.md](../decisions/spectrum-assembly-gentle-ramp.md)).

Module **slugs are bare identities** (no `game-NN-` prefix); ordering comes from the catalogue array position, not the slug.

## Content collections (Astro)

Three MDX collections share `src/content/curriculum/` as base directory:

| Collection | Pattern |
|------------|---------|
| `unit-pages` | `**/unit-*.mdx` |
| `module-pages` | `**/index.mdx` |
| `getting-started-pages` | `**/getting-started.mdx` |

YAML data collections:
- `src/content/modules/{platform}/{track}.yaml` — module catalogue (ordered array; each entry carries `kind` and, for `game` modules, the `game` it teaches)
- `src/content/units/{platform}/{track}/{slug}.yaml` — unit details (source of truth for counts), keyed by `moduleSlug`

## Computed fields

Layout, prevLesson, nextLesson, totalUnits, system are **derived from the entry path** in `[...slug].astro`. Never put these in frontmatter.

## Key helpers

In `src/lib/modules.ts`:

- `getModulesWithCounts(platform, track)` — lists modules with unit counts
- `getUnitsEntry(platform, track, slug)` — gets unit metadata for a module

## Unit archetypes

Not labels — design tools for planning:

| Archetype | Purpose |
|-----------|---------|
| Discovery | Standard teaching unit (most common) |
| Challenge | Problem-solving with recent skills |
| Synthesis | Combining concepts into complete program |
| Deep Dive | Hardware internals, "why it works" |
| Tutorial | Step-by-step guided construction |
| Showcase | Demonstrates what's possible (inspirational) |

## Gotchas

- **MDX files live in `src/content/curriculum/`**, not `src/pages/`. The `src/pages/` directory only has `.astro` files.
- **YAML validation**: check `src/content.config.ts` for schema if validation fails. Common issue: missing required frontmatter fields.
- **Code samples live in `/code-samples/`** — never inline in MDX. Use `CodeFromFile` component.
