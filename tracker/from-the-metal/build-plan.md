# "From the Metal" — build plan (teed up)

**Status:** Ready to build. **Channel decided:** site-canonical (full fidelity on
the site; Substack mirrors excerpts with `rel=canonical` back to the site).
**Feasibility:** confirmed against the real codebase 2026-06-30 — contained build,
no major hidden cost.

This is the executable plan for the design handoff in this folder:
[`handoff-readme.md`](handoff-readme.md) (full spec + the 14-article catalogue),
[`implementation-guide.md`](implementation-guide.md) (the original build guide),
`designs/*.dc.html` (prototypes — read intent from the markup, **do not** port
`support.js`), and `screenshots/*.png` (the pixel oracle — verify each page
against its numbered shot).

## Bottom line

The handoff's riskiest assumption — custom Shiki grammars for 6502 / Z80 / 68000 —
**checks out**. The grammars exist (`website/src/syntax/{6502,z80,m68k,…}.tmLanguage.json`,
registered in `src/lib/load-custom-languages.ts`) and are wired in. So the
`<CodeFigure>` component is a styling-and-chrome job, not a grammar-authoring one.
The copy is final in the handoff, so phases are mostly rendering + porting.

## Decisions needed first (Steve)

Three things the handoff didn't anticipate, each a real call before/while building:

1. **C64-blue brand drift.** The handoff uses C64 blue `#4a4dff` for the wordmark
   `x`, the kicker, and the blinking caret. **The site has since rebranded** to a
   warm "house" palette (`--color-primary` ≈ `#b74d2d`); platform blue is no longer
   a global token. The handoff's own rule says "don't correct accents to brand" —
   so keeping the blue is defensible, but it reintroduces a hue the site retired.
   **Keep the blue literally, or re-anchor to the house palette?**
2. **Dark mode.** The site ships a full dark theme; the designs are **light-only
   beige**. **Light-lock the series, or author dark variants?**
3. **Editorial code-annotation colour.** The prototypes tint *specific comments*
   amber ("this is the point") and metric annotations red/green/yellow. That's
   editorial, not syntax highlighting — Shiki colours all comments uniformly.
   Recommended: keep the header **metric chip** as the state-coloured element (a
   component prop) + use the highlighter's existing meta-string line emphasis
   (`{3,4}`, `focus{…}`, `+/-` — see `src/lib/satteri-highlight.ts`), and accept
   uniform comment colour. The per-comment amber is a fidelity nice-to-have.

## Key feasibility facts (the ones that shape the build)

- **Highlighting engine is not raw Shiki.** `astro.config.mjs` sets
  `syntaxHighlight: false` and uses `@astrojs/markdown-satteri` +
  `src/lib/satteri-highlight.ts`, calling `codeToHighlightHtml()` from
  `shiki-highlight-api` (theme `dark-plus`), output via the CSS Custom Highlight
  API (a `<style>`+`<script>` keyed by `blockId`), **not** inline spans.
  `<CodeFigure>` should call `codeToHighlightHtml(code, { lang, theme:'dark-plus', blockId })`
  exactly like `src/components/CodeFromFile.astro` (lines ~69–115, including the
  `<pre tabindex="0">` a11y tweak and emitting `result.css`/`result.script`), then
  wrap the returned `<pre>` in the dark figure chrome.
- **Design tokens** live in `Layout.astro` `:root` (not a `colors_and_type.css`).
  Most map exactly (`--c-bg`→`--color-bg`, `--c-surface`→`--color-surface`,
  `--c-fg`→`--color-text`, `--font-mono`→`--font-family-mono`,
  `--font-body`→`--font-family-sans`). Near-misses to use as literals or
  series-scoped vars: card border `#e7e1cf`, section rule `#e0d9c6`, inline-code
  chip `#ece7d6`, `--shadow-chunky` (site is `4px 4px 0 /.18`). The **per-article
  accent** is a frontmatter field, passed as an inline `--accent` CSS var — the
  repo already uses this idiom (`patterns/index.astro` `style={\`--pc: ${color}\`}`).
- **Content collections** fit cleanly (Zod + `glob` loader in `src/content.config.ts`).
- **No `prose.css` / `data-platform`** — the article layout brings its own
  scoped prose styles (like `who-this-is-for.astro` / `patterns/index.astro`).
- **Fonts** (Inter + JetBrains Mono) already provisioned via the Astro Font API —
  **do not** add Google Fonts `<link>`.
- **Global print CSS** in `Layout.astro` (~line 1163) forces white bg + hides
  nav/footer; the article's print CSS must **override** it (beige page, dark
  figures, `@page` margins, `break-inside: avoid` on `figure`/`pre`/callout).
- Repo is Astro `^7.0.3` (handoff says 5) — immaterial; MDX/collections/Font API
  all current.

## Phased build

0. **Land the handoff in-repo** — done (this folder, `docs` repo). The screenshots
   are the build session's pixel oracle.
1. **Content model** — `fromTheMetal` collection in `content.config.ts`
   (schema: title, description, pubDate, cpu, category, accent, order, audiences,
   teaser); `src/content/from-the-metal/`; `FromTheMetalLayout.astro`; route
   `pages/from-the-metal/[...slug].astro`; hub stub `pages/from-the-metal/index.astro`.
   Separate route + layout — not the curriculum catch-all.
2. **`<CodeFigure>` component** (highest residual risk) — wrap `codeToHighlightHtml`
   per `CodeFromFile.astro`; dark header bar (left `label`, optional right `metric`
   chip with `state` → `#fca5a5`/`#86efac`/`#fcd34d`); italic `<figcaption>`; the
   `#0f172a` body + `#1e293b` 3px border. Resolve decision 3 here.
3. **Article layout/template** — masthead (wordmark + 3px rule + accent back-link),
   `--accent` kicker, mono H1, Inter lede, h2/p rhythm, inline-code chip, closing
   callout, `>`-caret footer with the verbatim closing line
   (*"Every great programmer started with one instruction."*). Print CSS that
   overrides the global. Validate vs `screenshots/01-unroll-loops.png`.
4. **Port the 14 articles** (mechanical, ×14) — copy is final in the `.dc.html`
   sources; one MDX each; set cpu/accent/category/order/audiences/teaser from the
   catalogue (`handoff-readme.md` lines ~102–117). British spellings, no emoji,
   verbatim closing line. Verify each vs its numbered screenshot.
5. **The hub** — 3→2→1 card grid, 6px top accent bar, hover lift + chunky no-blur
   shadow growing to accent, blueprint-grid bg, blinking caret
   (`prefers-reduced-motion`-guarded), footer link to the board. Data-driven from
   `getCollection`.
6. **The board** — standalone `pages/from-the-metal/audiences.astro` (the "Five
   Audiences / Twelve Stories" piece), a static data array like
   `who-this-is-for.astro`; 12 cards; wire the 5 "Read →" cross-links.
   *(Note: the board's own copy is internal-marketing and partly stale — platform
   count, "Docker toolchains", fixed counts — apply the same claims discipline as
   the site reconciliation when porting.)*
7. **Wire the two router doors** — in `who-this-is-for.astro`: door 2
   (abstraction-curious) replace its `soon` note with a link to `/from-the-metal`;
   door 4 (performance-aware) drop `gap: true` and add the link. Closes the last
   two "coming soon" doors.
8. **Substack mirror** (publishing checklist, not code) — excerpts on Substack
   with `rel=canonical` → the site article; site-first.
9. **Technical-accuracy pass** (gating, channel-independent) — the 14 articles'
   assembly + cycle counts are unverified editorial content; verify against the
   primary reference library (`198x/reference/`) and the **Asm198x `isa` crate**
   (the authored ISA spec is the source of truth for opcode→cycles) before publish.

## Effort & risk

- **Effort:** phases 2–4 are the bulk; 4 is large only by repetition (14×), low by
  difficulty (copy final). 0/1/5/6/7/8 small-to-medium.
- **Risks, ranked:** (1) ~~grammars~~ de-risked; (2) C64-blue brand drift —
  decision; (3) dark mode — decision; (4) global print CSS override; (5) minor
  token near-misses + bring-own prose styles.

**This is a future-session build.** Steps 1–3 of the audience-targeting plan
(claims reconciliation, the router + nav trim, the `/teaching` page) are shipped;
this is step 4, and the two router doors it closes are the only "coming soon"
cards left.
