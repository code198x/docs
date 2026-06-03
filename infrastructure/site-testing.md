# Site Testing (Playwright + axe + Lighthouse)

End-to-end, accessibility, and performance checks for the `website` repo.
Added 2026-06-03 alongside the `/family` cross-promotion page.

## Commands

```bash
cd website
npm run test:e2e     # Playwright e2e (desktop + Pixel 7 mobile)
npm run test:a11y    # axe WCAG 2.1 AA across 7 representative templates
npm run test:lh      # build, then Lighthouse CI (perf/a11y/best-practices/SEO)
```

All three auto-start a server (`test:e2e`/`test:a11y` use `npm run dev`;
`test:lh` builds and runs `npm run preview`), so no manual server needed.
Config: `playwright.config.ts`, `lighthouserc.cjs`. Tests in `tests/`.

## What's covered

- **e2e** (`tests/family.spec.ts`) — the `/family` page: no horizontal
  overflow, sibling cards + status badges, footer family-strip links.
- **a11y** (`tests/a11y.spec.ts`) — one page per template type (home, system
  landing, module index, unit, getting-started, vault, family), each checked in
  **both light and dark themes** (7 pages × 2 themes × 2 viewports = 28 runs).
  Fails on any serious/critical violation **not** in the baseline.
- **Lighthouse** — same 7 URLs against the production build. Accessibility is a
  hard gate (`minScore 0.9`); perf/best-practices/SEO start as warnings until
  baselined into budgets.

## The a11y baseline — burn it down

`tests/a11y-baseline.json` lists known pre-existing serious/critical violations
(with reasons) so the suite catches **new** regressions while the debt is paid
off. It is currently **empty** — the gated template pages have zero
serious/critical violations in both themes. Add an entry only with a written
reason, and burn it back down.

Code blocks scroll horizontally, so they're made keyboard-focusable
(`tabindex="0"`) via the `rehypePreTabindex` plugin in `astro.config.mjs` (for
markdown fences) and a string-replace in `CodeFromFile.astro` (for component
code) — clearing the former `scrollable-region-focusable` debt.

The setup pages are now fixed and gated too: the house brand token was darkened
(`--color-house-2` #c0512f → #b74d2d — imperceptible, passes AA on the beige
page bg), an unstyled prose link got an accessible ink, the recommended-tag
success green was made theme-aware, and the hand-authored `.code-block` divs got
`tabindex="0"`. The gated set is now 11 template pages (× 2 themes × 2 viewports
= 44 checks).

## Theme-aware accessible ink (brand colours as text)

Brand/platform colours (Sinclair red, Amiga orange, C64 blue, NES red, house
brick) are used both as fills (bars, borders, shadows — kept raw) and as small
text. As text they must meet AA on the current theme's surface, but the same
hex is too light on the light surface or too dark on the dark one.

`src/lib/contrast.ts` exports `accessibleInk(colour, bg)` (nudges lightness only
as far as needed to hit AA, preserving hue — colours that already pass are
returned unchanged) and `inkStyle(colour)` (emits the `--ink-l`/`--ink-d` pair).
An ancestor sets those two vars; the global `--ink` switch in `Layout.astro`
resolves to the theme-correct one, so any `color: var(--ink)` is accessible in
both themes. `<body>` sets the pair from Layout's `platformColor` prop, so most
pages inherit it automatically; components (PathCard, VaultCard, ReadingTime,
SectionHeader) set their own for their accent.

This replaced the old pattern of `color: var(--platform-color)` (and aliases
`--accent-color`, `--sys`, `--link-color`) which failed contrast in one theme or
the other. The footer copyright/credits were a separate fix — a design-contract
violation (small text wrongly using `--color-text-muted`, which the token
contract reserves for large/decorative text; switched to `--color-text-secondary`).

## Prose accessibility (Vale + readability)

We teach hard subject matter, so the prose itself shouldn't add *avoidable*
difficulty on top. Two advisory checks watch for it — both signals, neither a
gate:

```bash
cd website
npm run prose:style   # Vale — words, voice, spelling
npm run prose:read    # readability + long-sentence report
npm run prose:check   # both
```

- **Vale** (`.vale.ini`, `styles/Code198x/`) encodes the project Writing
  Principles as `suggestion`-level rules: `Substitutions` (short words beat
  long), `Weasel` (filler/hedges), `Condescending` (the "never condescending"
  voice — simply, obviously, trivial…), `BritishEnglish` (the British-English
  Critical Rule). `Passive` exists but ships **off** (`Code198x.Passive = NO`):
  regex passive-detection is the noisiest rule there is, and passive is often
  correct in hardware prose ("the interrupt is raised"). Curriculum currently
  draws ~217 suggestions across 357 files (~0.6 each) — a signal, not a
  firehose. Rule rationale and tuning notes in `styles/Code198x/README.md`.
- **Readability** (`scripts/prose-report.mjs`, zero-dependency) owns the thing
  Vale can't measure: sentence length and grade level. Strips code, JSX, tables
  and frontmatter, then reports Flesch-Kincaid grade and the sentences over ~30
  words (the splittable kind of sprawl). `--long N` tightens the threshold;
  pass paths to scope it.

The framing that matters: readability formulas inflate grade level for
unavoidable domain nouns ("Commodore", "emulator") and choke on tables, so their
absolute scores are noisy. The one actionable number is long sentences. The
curriculum averages grade **5.7** — its hardest assembly units score *easier*
than the explainer pages, because the difficulty lives in the concepts and code,
not the sentences. The vault (adult reference history) runs grade 11–13 by
design; it's a different audience, not a regression.

## Gotcha: CLI Chrome screenshots are not mobile emulation

Do not judge mobile layout with `chrome --headless --window-size=390,…
--screenshot`. It does not set a mobile layout viewport — it lays out wider and
clips the capture, so `vw` fonts render oversized and pages look like they
overflow when they don't. Use Playwright device profiles (`devices['Pixel 7']`)
and assert `documentElement.scrollWidth <= clientWidth`. Always validate a
screenshot tool against a known-good page before trusting it to diagnose a bug.
See `~/knowledge/headless-chrome-window-size-isnt-mobile-emulation.md`.
