# Decision: Sätteri markdown processor for the website

**Status:** Active (2026-06-30). Applies to the `website` repo (`astro.config.mjs`,
`src/lib/satteri-highlight.ts`). Supersedes the unified/remark markdown pipeline.

## The decision

The website's markdown processor moves from Astro's `unified()` (remark/rehype)
pipeline to **`satteri()`** — Astro 7's native Rust markdown processor. Syntax
highlighting keeps the existing **CSS Custom Highlight API** approach (the
DOM-size optimisation in `src/lib/`): a custom Sätteri HAST plugin
(`code198xHighlightPlugin`) wraps `shiki-highlight-api`'s `codeToHighlightHtml`
to emit byte-identical highlighting markup, replacing the old
`remark-shiki-highlight-api` + `rehypePreTabindex` plugins.

This was reached during the Astro 6 → 7 upgrade, after the unified migration was
already in place (see § Path here).

## Why

**Build speed.** Sätteri parses markdown ~47× faster than unified. End-to-end the
production build dropped from **~43s to ~26s (≈40%)** for 2003 pages; dev-server
reparse on content edits is near-instant. Measured, not estimated — the unified
*parse* (not Shiki tokenizing) was the dominant build cost, so the native parser
wins big here.

**Highlighting is unchanged.** Code-block output is byte-identical to the old
pipeline (verified across the curriculum, block-IDs normalised). The CSS Custom
Highlight API DOM-size win (≈1 text node per line, not per token) is preserved —
we did **not** adopt span-per-token highlighting.

## The smartypants tradeoff (the real cost)

Sätteri's smart-punctuation differs from unified's on ~156 prose pages. An audit
(current vs Sätteri, every page, each quote/dash change classified) found
**~234 fixes vs ~8 genuine regressions (~23:1)**:

- **Fixes (dominant):** 151 opening-double-quote corrections. The unified pipeline
  systematically used a *closing* quote `”` to *open* a quotation (`”word…`);
  Sätteri renders `“word…`. Plus possessive/contraction apostrophes (`Compute!’s`).
- **Regressions (all fixed in content):** 5 inch-marks (`3.5"`/`5.25"`/`9"` →
  Sätteri opened the quote) — now written with the double-prime `″` so no
  smartypants touches them; and 3 possessive `*Title*'s` at sentence starts that
  Sätteri read as opening quotes — now written with an explicit `’`.

Code blocks are never smartypanted, so this is prose-only.

## Constraints / assumptions

- **Content is 100% MDX** (1813 files, zero `.md`). Sätteri wraps injected HTML as
  a *Fragment* node for `.mdx` and a *raw* node for `.md`; the plugin is configured
  `{ mdx: true }`. If `.md` content is ever added, it needs the `{ mdx: false }`
  variant (raw nodes) or it will render escaped. This is why the plugin takes an
  `mdx` flag rather than hard-coding one.
- `CodeFromFile` is unaffected — it calls `shiki-highlight-api` directly and never
  went through the markdown processor.

## Alternatives considered

- **Stay on unified.** Rejected: gives up the ~40% build win for no benefit; the
  unified pipeline also carried the opening-quote bug.
- **Sätteri + native Shiki highlighting (Path A).** Rejected: span-per-token output
  abandons the DOM-size optimisation and forces a CSS rewrite, for no speed gain
  over Path B.
- **Expressive Code (`satteri-expressive-code`, Path C).** Rejected: measured
  ~41.6s build (EC's frame/annotation rendering ate the parser win), adds a flat
  ~3.4KB-gzip/page framework payload, and replaces the Range-based DOM model. Worth
  revisiting only if its features (frames, copy buttons, line markers) are wanted
  for their own sake — a separate decision.

## Incidental finds (not addressed here)

- `browse/by-platform.astro` sorts systems by year with **no tiebreaker**, so
  same-year entries order nondeterministically build-to-build (surfaced as a
  `ZVI`/`BRA` flip). Pre-existing; orthogonal to this change.
- The old `shikiConfig` carried self-referential aliases (`amos→amos`,
  `ca65→ca65`) that crash native Shiki. Removed with the dead `shikiConfig` block.
