# Content Model

How units, tracks, games, and platforms relate. The formal spec is in `docs/CURRICULUM-SPECIFICATION.md`; this page captures patterns and gotchas from applying it.

## Hierarchy

**Platform** → **Track** → **Game** → **Unit**

- Platforms: C64, ZX Spectrum, Amiga, NES
- Tracks: assembly, BASIC (where applicable)
- Games: ~10 per track, progressive complexity
- Units: ~5-15 per game, each produces a runnable result

## Content collections (Astro)

Three MDX collections share `src/content/curriculum/` as base directory:

| Collection | Pattern | Count |
|------------|---------|-------|
| `unit-pages` | `**/unit-*.mdx` | ~480 |
| `game-pages` | `**/index.mdx` | ~94 |
| `getting-started-pages` | `**/getting-started.mdx` | 4 |

YAML data collections:
- `src/content/games/{platform}/{track}.yaml` — game catalogue
- `src/content/units/{platform}/{track}/{game}.yaml` — unit details (source of truth for counts)

## Computed fields

Layout, prevLesson, nextLesson, totalUnits, system, gameName are **derived from the entry path** in `[...slug].astro`. Never put these in frontmatter.

## Key helpers

- `getGamesWithCounts(platform, track)` — lists games with unit counts
- `getUnitsEntry(platform, track, game)` — gets unit metadata

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
