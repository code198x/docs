# Astro Site

The website is built with Astro 6.x. Lives in the `website` repo.

## Commands

```bash
cd website && npm run dev    # Dev server on :4321
npm run build                # Prod build (runs Pagefind for search)
```

## Content routing

The `src/pages/[...slug].astro` catch-all route renders all curriculum content. MDX files in `src/content/curriculum/` are matched by path.

Computed fields (layout, prevLesson, nextLesson, totalUnits, system, gameName) are derived from the entry path in this route — **never in frontmatter**.

## Content collections

Defined in `src/content.config.ts`. Three MDX collections + two YAML collections. See [content model](../curriculum/content-model.md) for details.

## Key gotcha

MDX files live in `src/content/curriculum/`, **not** `src/pages/`. The `src/pages/` directory only contains `.astro` files (overview pages, dynamic routes, the catch-all).
