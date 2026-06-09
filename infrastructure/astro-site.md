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

Defined in `src/content.config.ts`. Three MDX collections + two YAML collections. See [content model](../specifications/content-model.md) for details.

## Module thumbnails (track-overview pages)

`TrackGames.astro` shows a thumbnail per module on each track-overview page
(`/{platform}/{track}`). It picks the image in this order:

1. The module's explicit **`thumbnail:`** field (a `/images/...` path), if set.
2. Otherwise a **derived** path: `/images/{platform}/{track}/{slug}/unit-NN/screenshot.png`,
   where `NN` is the module's `unitsAvailable` (its last published unit).

So a module renders a thumbnail automatically **only if its last published unit
has a `screenshot.png`** — the convention the Emu198x capture pipeline follows
(Amiga units, and the newer Spectrum BASIC games). Modules that don't fit need
an explicit `thumbnail:`:

- **Game modules with a bespoke hero image** (`bleeper.png`, `dropzone.png`,
  `chamber.png`) — point `thumbnail:` at that image.
- **Teaching primers** whose last unit is error/debug screenshots — point at a
  representative earlier frame (e.g. the `MEET …` titlecard).
- **Modules whose last `screenshot.png` is a unit before `unitsAvailable`**
  (e.g. Starfield, Spectrum *Meet the Machine*) — point at the real last shot.

The path **must include the `{track}` segment** — images live under
`{platform}/{track}/{slug}/…`. (A TrackGames bug once omitted it, breaking every
track page's thumbnails; see git history.)

New modules: prefer emitting `unit-NN/screenshot.png` from the capture so the
derivation just works; reach for `thumbnail:` only when the image is named or
located differently.

## Key gotcha

MDX files live in `src/content/curriculum/`, **not** `src/pages/`. The `src/pages/` directory only contains `.astro` files (overview pages, dynamic routes, the catch-all).
