# Content model

[Project purpose](../PROJECT.md) owns intent. The website's `src/content.config.ts`, collection loaders, route code and source files establish what the site implements. Update those together when changing a schema; this guide explains their responsibilities rather than duplicating every field.

## Curriculum hierarchy

System material follows **system → track → module → unit**. Shared material follows **section → module → unit**. A module can be a game, a teaching module or an interval. One game may grow over several modules. Bare module slugs identify content; ordered catalogue arrays establish sequence. Neither slug numbering nor a fixed unit count establishes progression.

System tracks currently include assembly, BASIC, AMOS, Blitz and machine introductions. These implemented identifiers are not a requirement that every system offer all of them. Foundations and Craft are shared sections. Maths for Games currently sits under Craft; its broader intended coverage is set out in [Curriculum design](curriculum.md).

## Files and state

| Location in the website | Responsibility |
|---|---|
| `src/content/systems/` | Fleet identity, status tiers and distinct tool/development capabilities |
| `src/content/modules/` | Ordered module catalogues, sections or system/track membership, groups and routes |
| `src/content/units/` | Unit metadata keyed by `moduleSlug`, including phase ranges and availability |
| `src/content/curriculum/` | Authored MDX: `index.mdx`, `unit-NN.mdx`, `getting-started.mdx` |
| `src/content/vault/` | Encyclopaedic entries |
| `src/content/patterns/` | Reusable techniques |
| `src/lib/modules.ts` and route helpers | Counts, lookups and derived navigation |

Catalogue statuses (`coming-soon`, `in-progress`, `complete`) describe editorial state. Unit availability, authored files, downloadable sources, build results and execution evidence answer different questions. Verify each claim against its appropriate source; a populated catalogue does not prove a finished or working lesson.

Module `kind` can be `game`, `teaching` or `interval`. `requires`, `suggests` and route references currently describe navigation relationships. The curriculum's policy is knowledge-based entry: explain what a reader needs, allow equivalent experience and never implement attendance checks or pass/fail access gates.

Unit-page frontmatter currently requires `title`, numeric `game` and numeric `unit`; description, publication date and tags have their schema-defined optional/default behaviour. Module-page frontmatter has its own schema. Check it instead of copying obsolete templates. Layout, system context, neighbours and counts are derived by the website; do not hand-maintain them in each page.

Runnable sources belong in the code-samples repository and are included with `CodeFromFile`. Pseudocode, trace data and explanatory fragments follow [Code samples](code-samples.md); a conceptual unit does not need a pretend executable artefact.

Do not keep separate prose completion totals, language-support matrices or platform counts. Trackers describe a bounded investigation or proposal. Catalogues and Git remain the source of current inventory.
