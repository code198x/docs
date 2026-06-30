# CLAUDE.md — implementation guide for the "From the Metal" series

This file orients an agent (or developer) implementing the designs in `designs/` inside the
production codebase. Read `README.md` first for the full spec; this file is the **build plan**.

## Target environment
Production is **Astro 5 + MDX** — `github.com/code198x/website`. Reuse what's already there:
- Design tokens live in `src/layouts/Layout.astro` (and the design system's `colors_and_type.css`).
  Use the `--c-*` / `--font-*` token names, not raw hex, wherever a token exists.
- Code highlighting is **Shiki** with custom grammars for 6502 / Z80 / 68000. The prototypes fake
  syntax color with hand-placed `<span>`s — **replace that with Shiki** and the existing grammars.
- Fonts come from the Astro Font API (Inter + JetBrains Mono already provisioned).
- MDX prose is styled by `prose.css` (`.prose`, platform-tinted via `data-platform`).

**Do not port `support.js` or the `.dc.html` format.** They exist only so the prototypes render in a
browser. Read design intent from the inline-styled markup between `<x-dc>…</x-dc>`.

## Content model mapping
- **Each article** → one MDX entry. Front-matter: title, description, pubDate, tags, learning-time,
  plus two custom fields this series needs: `cpu` (e.g. "6502") and `accent` (hex from the catalogue).
  Body = the article prose + code blocks (Shiki). The dark code "figure" with a header bar + metric
  chip + caption is a reusable MDX component — build it once (see below).
- **The hub** → a series landing route (e.g. `/from-the-metal`). Data-drives the 14 cards from the
  MDX collection, sorted by an `order` field. Card accent = entry `accent`; tag = `cpu · category`.
- **The board** (`Five Audiences`) → a standalone marketing page, not in the article collection.

## Build order (recommended)
1. **`<CodeFigure>` component** — the dark listing block: header bar (left label, optional right
   metric chip with a state color), Shiki-rendered body, italic caption. Every article uses it 1–3×.
   Get this pixel-right first; it's the most repeated unit and the hardest to eyeball later.
2. **Article layout** — masthead (wordmark + rule + back-link), accent kicker, H1, lede, the
   alternating h2/p prose rhythm, inline `<code>` chip style, the closing callout box, footer line.
   Wire the print CSS (Letter, reserved top/bottom margins, `break-inside: avoid` on figures/pre).
   Validate against `screenshots/01-unroll-loops.png` — it exercises every element including metric chips.
3. **One full article end-to-end** (Unroll Your Loops) — prove layout + `<CodeFigure>` + Shiki + print.
4. **Remaining 13 articles** — pure content; copy is final in the source files. Just set `cpu`/`accent`
   per the catalogue and paste prose + listings. Verify each against its numbered screenshot.
5. **The hub** — 3-col responsive card grid, hover lift + chunky shadow, blueprint-grid background,
   blinking caret, footer link to the board. Data-drive cards from the collection.
6. **The board** — single-column stack of 12 audience cards; wire the 5 "Read: … →" links to articles.
7. **Responsive + a11y pass** — grid 3→2→1; `prefers-reduced-motion` disables hover transitions and
   the caret blink; `<pre>` scrolls horizontally on mobile; focus outlines visible (keyboard-first).

## Fidelity checklist (easy to get wrong)
- Square corners everywhere except inline `<code>`/`<kbd>` (4px). No rounded cards.
- Shadows have **no blur** — `Npx Npx 0 color`. Hover grows the offset, doesn't soften it.
- Borders are **3px**, not 1px. They turn the accent color on hover.
- Surface is **beige `#f4f1e8`**, cards **cream `#fdfcf7`** — never white.
- JetBrains Mono for ALL headings/labels/code; Inter only for body paragraphs.
- British spellings, no emoji, numerals stay numeric. Keep the closing line verbatim:
  *"Every great programmer started with one instruction."*
- Accent colors are **topic-coded** and intentionally exceed the 4 platform hues — use the catalogue
  values as-is; don't "correct" them to brand colors.

## Verifying against screenshots
`screenshots/` has one PNG per design, numbered to match the catalogue (`00-index` … `15-messaging-board`).
They're reference renders of the prototypes — match layout, type scale, spacing, and color against them.

## Reference files
- `README.md` — full spec + the 14-row article catalogue (file → title → cpu → category → accent → audiences).
- `designs/*.dc.html` — the prototypes (inline-styled; read intent from the markup).
- `screenshots/*.png` — reference renders.
