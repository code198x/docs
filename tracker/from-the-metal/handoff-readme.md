# Handoff: "From the Metal" — article series + messaging surfaces

## Overview
"From the Metal · What's Underneath" is a content series for **Code Like It's 198x** (https://code198x.com), an open-source project that teaches programming by building real games for classic 8/16-bit hardware (C64, ZX Spectrum, NES, Amiga).

The series reframes modern programming advice ("unroll your loops", "size to a power of two", "mind the stack") by showing the *hardware reason* underneath it, in real annotated assembly. It comprises:

- **1 index/hub page** — lists all 14 reads in a card grid, links out to each and to the messaging board.
- **14 article pages** — one concept each, identical editorial template, real 6502 / Z80 / 68000 assembly with cycle counts.
- **1 messaging board** — an internal/marketing artifact: the same product pitched to 12 audiences, ~40 words each. Not part of the public article reading flow, but cross-linked from the hub.

The intended production home is the existing **Astro 5 + MDX** site (`github.com/code198x/website`). Each article maps naturally to one MDX content entry; the hub maps to a series landing route; the board is a standalone marketing page.

## About the Design Files
The files in `designs/` are **design references created in HTML** — prototypes showing the intended look, typography, and layout, **not production code to copy directly**. They are authored in a small in-house component format (`.dc.html`, which boots via the bundled `support.js`); **do not** port that runtime. The task is to **recreate these designs in the target codebase's existing environment** — here, the Astro 5 + MDX site and its established components — using its patterns, content collections, and the project design system.

If implementing outside that repo, recreate them in the most appropriate framework for the project, preserving the visual system documented below.

## Fidelity
**High-fidelity (hifi).** Final colors, typography, spacing, and copy are all settled and should be reproduced precisely. Exact values are in **Design Tokens** below. The one area with intentional latitude: per-card/article *accent colors* in the topic system (see Design Tokens → "Accent color system") deliberately go beyond the strict 4-platform brand palette for topic legibility — keep them as specified.

## The design system (binding)
These designs already follow the **Code Like It's 198x — Design System**. Re-use the production tokens rather than the literal hex values where a token exists. Key signatures used throughout:

- **Surface:** C64 beige `#f4f1e8` page, cream `#fdfcf7` cards. Not white.
- **Text:** slate `#1e293b`; muted slate `#475569`; faint labels `#94a3b8` / `#a8a08a`.
- **Type:** **JetBrains Mono** for all headings, labels, kickers, code, nav, badges; **Inter** for body/paragraph copy; italic Inter for captions.
- **Square corners** (`border-radius: 0`) on cards; small radius only on inline `<code>`/`<kbd>`.
- **3px solid borders** on cards (`#e7e1cf`), going to the accent color on hover.
- **Chunky offset shadow**, no blur: `5px 5px 0 rgba(0,0,0,0.10)` at rest → `9px 9px 0 <accent>@18-20%` + `translateY(-4px)` on hover.
- **`// SECTION //`** mono uppercase markers; **`>`** caret on the footer line; **`→`** literal arrows on links.
- **British spellings**, no emoji, numerals stay numeric. Voice: confident, technical, romantic about the era.
- Closing line on every article: *"Every great programmer started with one instruction."*

> Production token names (use these): `--c-bg` (#f4f1e8), `--c-surface` (#fdfcf7), `--c-fg` (#1e293b), `--c-c64` (#4a4dff), `--c-spectrum` (#cc0000), `--c-nes` (#e30613), `--c-amiga` (#ff6600), `--font-mono` (JetBrains Mono), `--font-body` (Inter), `--border-card` (3px solid), `--shadow-chunky`. Full list in the design-system stylesheet `colors_and_type.css`.

---

## Screens / Views

### 1. Index / Hub — `From the Metal - Index.dc.html`
- **Name:** "From the Metal · What's Underneath" series hub.
- **Purpose:** Entry point; lets a reader browse all 14 articles and see who each is for, and jump to the messaging board.
- **Layout:**
  - Page: full-height, `padding: 72px 24px 96px`, beige background with a **22×22px faint blueprint grid** overlay (two `linear-gradient` lines at `rgba(74,77,255,0.04)`).
  - Centered column, `max-width: 1120px`.
  - **Header** (`max-width: 760px`): masthead row (wordmark "CODE LIKE IT'S 198x" with the `x` in C64 blue + a 3px beige rule + right-aligned mono label "A SERIES · 14 PARTS"); a `// FROM THE METAL //` kicker in C64 blue; an oversized mono H1 "WHAT'S / UNDERNEATH." (`clamp(36px,6.5vw,60px)`, line-height 1.02, letter-spacing -1.5px); a 19px intro paragraph.
  - `// THE READS //` section marker.
  - **Card grid:** `display:grid; grid-template-columns: repeat(3, 1fr); gap: 24px` — 14 cards.
  - **Footer row:** 3px top rule; left = `>` caret + closing line + blinking caret block (9×16px C64-blue, `steps(1)` 1s blink); right = mono link "Who's this for? See the messaging board →" to `Five Audiences.dc.html`.
- **Card component (each of the 14):**
  - `<a>` link, `display:flex; flex-direction:column`, cream bg, 3px `#e7e1cf` border, `5px 5px 0 rgba(0,0,0,0.10)` shadow.
  - **6px top accent bar** in the card's accent color.
  - Body `padding: 22px 24px 24px`, flex column, `flex:1`.
  - Top row: 2-digit index (`01`–`14`) in accent color + right-aligned platform·topic tag (e.g. "6502 · PERFORMANCE") in `#a8a08a`, 10px.
  - H2 title: JetBrains Mono 700, 18px, line-height 1.18, letter-spacing -0.3px.
  - Teaser: Inter 14px, line-height 1.5, `#475569`.
  - Bottom row (pinned with `margin-top:auto`): audiences label (9.5px, `#a8a08a`) + "Read →" in accent color, 12px 600.
  - **Hover:** `transform: translateY(-4px)`; shadow → `9px 9px 0 <accent>@~18-20%`; border-color → accent. Transition `0.3s cubic-bezier(0.16,1,0.3,1)` on transform/shadow, `0.15s` on border.
- **Card order, accent, tag, links** — see the **Article catalogue** table below.

### 2. Article template — all 14 `*.dc.html` reads
Every article is the same printable document template. Differences are only content + accent color.
- **Name:** varies (see catalogue).
- **Purpose:** Teach one concept by showing the hardware underneath it.
- **Layout:**
  - `<main>` centered, `max-width: 760px`, `padding: 64px clamp(24px,5vw,40px) 96px`, inherits beige background.
  - Wrapped in a `<table>` print-frame: a `thead`/`tfoot` spacer row (`0.7in`, shown only `@media print`) reserves top/bottom page margins so multi-page PDF output doesn't clip. Screen view hides them. `@page { size: letter; margin: 0 }`. **Re-implement this as the target stack's print CSS** — the table is a print-margin hack, not semantic structure.
  - **Masthead row:** wordmark + 3px rule + right-aligned **back-link** "← FROM THE METAL · <CPU>" to the index (mono 11px, `#94a3b8`, hover → C64 blue).
  - **Kicker:** `// <CATEGORY> · WHAT'S UNDERNEATH //` in the article's accent color, mono 12px 600, letter-spacing 2px.
  - **H1:** JetBrains Mono 700, `clamp(30px,5.2vw,44px)`, line-height 1.08, letter-spacing -0.5px, `text-wrap: balance`.
  - **Lede:** 20px Inter, `#475569`, line-height 1.55.
  - **Body:** alternating `<h2>` section heads (JetBrains Mono 700, 22px) and `<p>` (17px Inter, line-height 1.68, `text-wrap: pretty`). Inline `<code>` = JetBrains Mono 0.82em on `#ece7d6` chip, 4px radius, `2px 7px` padding. Inline emphasis uses italic `<em>` often tinted the accent color.
  - **Code figures** (`<figure>`): a dark header bar (`#1e293b`, `8px 16px`) with a left mono label (e.g. "6502 · ROLLED") and an optional right-aligned metric chip (e.g. "3,584 cycles" in a state color); then a `<pre>` block — bg `#0f172a`, text `#e2e8f0`, JetBrains Mono 14px, line-height 1.75, `padding: 20px 22px`, 3px `#1e293b` border. Inline `<span>`s color the assembly comments: muted `#7d8da3` for neutral notes, amber `#f0a868` for the "this is the point" annotations, `#fca5a5`/`#86efac`/`#fcd34d` for bad/good/middle metric states, `#5b6b86` for elision. A 13px italic Inter `<figcaption>` follows.
  - **Closing callout:** cream box, 3px `#e7e1cf` border, `6px 6px 0 rgba(0,0,0,0.10)` shadow, `padding: 26px 28px`, an 18px summary paragraph.
  - **Footer line:** 3px top rule + `>` caret + closing line (mono 13px, `#475569`).
- **Components & exact copy:** read each file in `designs/` — copy is final and should be reproduced verbatim, including the assembly listings, cycle counts, and annotations.

### 3. Messaging board — `Five Audiences.dc.html`
- **Name:** "One Product, Twelve Stories" — audience messaging board.
- **Purpose:** Internal/marketing reference: the same project pitched to 12 audiences, ~40 words each, voice adapted per audience.
- **Layout:** beige page, `max-width: 840px` column. Masthead ("MESSAGING · 12 AUDIENCES"), H1 "ONE PRODUCT, / TWELVE STORIES.", intro, `// HOW THE MESSAGE READS //` marker, then a **vertical stack** (`flex column`, gap 28px) of 12 cards.
- **Card:** cream, 3px border, `6px 6px 0` shadow, **6px top accent bar**; header row (2-digit index + ALL-CAPS audience name + right-aligned qualifier tag); a 19px Inter pitch paragraph; a dashed-top-rule footer with a `>` caret "leads with: <angle>" note and, on the cards that have a matching article, a right-aligned "Read: <title> →" link.
- **The 12 audiences (index, name, "leads with", → article if linked):**
  1. Absolute Beginners — reassurance + instant payoff.
  2. Parents & Educators — substance, safety, patience disguised as play.
  3. Retro Enthusiasts — specifics, names, romance of the era.
  4. Experienced Devs — depth, rigour, no hand-holding → `The Stack - 68000`.
  5. The Abstraction-Curious — the layer beneath the abstraction → `Unroll Your Loops - Article`.
  6. Performance-Aware — cycles, cache, speed from first principles → `Unroll Your Loops - Article`.
  7. Lapsed Coders — joy and return, not the grind.
  8. CS Students & Self-Taught — the fundamentals school skipped → `Two's Complement - 6502`.
  9. Indie Devs & Demoscene — constraint as craft.
  10. Embedded Engineers — directly transferable discipline → `The Stack - 68000`.
  11. Educators & Institutions — drop-in curriculum, open source.
  12. Funders & Press — scale, credibility, mission.

---

## Article catalogue (order, CPU, accent, category, audiences)

| # | File (`designs/…`) | Title | CPU | Category | Accent | Audiences shown |
|---|---|---|---|---|---|---|
| 01 | `Unroll Your Loops - Article` | Why "unroll your loops" is real advice | 6502 | PERFORMANCE | `#be123c` | Performance · Abstraction-curious |
| 02 | `Two's Complement - 6502` | When 255 + 1 = 0 | 6502 | ARITHMETIC | `#4a4dff` | CS students · Abstraction-curious |
| 03 | `Powers of Two - Z80` | Why everything is a power of two | Z80 | ARITHMETIC | `#cc0000` | Performance · CS students |
| 04 | `The Stack - 68000` | "Stack overflow" is a real place | 68000 | ARCHITECTURE | `#ff6600` | CS students · Embedded |
| 05 | `Racing the Beam - NES` | Racing the beam | NES (6502) | GRAPHICS | `#0e7490` | Game devs · Retro |
| 06 | `Lookup Tables - Amiga` | The fastest function is the one you already ran | 68000 | TABLES | `#7c3aed` | Demoscene · Performance |
| 07 | `Bitmasks & Registers - Spectrum` | The register is the bitfield | Z80 | HARDWARE | `#1f9d57` | CS students · Embedded |
| 08 | `Fixed Point - NES` | Mario moves in fractions of a pixel | NES (6502) | ARITHMETIC | `#b8860b` | Game devs · CS students |
| 09 | `Alignment - 68000` | Why your structs have holes in them | 68000 | MEMORY | `#475569` | Embedded · CS students |
| 10 | `Endianness - 6502 vs 68000` | Why the bytes come out backwards | 6502 vs 68000 | MEMORY | `#0d9488` | CS students · Embedded |
| 11 | `Pointers - 6502` | A pointer is just an address you stored | 6502 | MEMORY | `#4a4dff` | CS students · Abstraction-curious |
| 12 | `The Blitter - Amiga` | A chip that does nothing but move memory | 68000 | HARDWARE | `#ff6600` | Game devs · Demoscene |
| 13 | `Self-Modifying Code - 6502` | Code that rewrites itself | 6502 | CODE AS DATA | `#db2777` | Abstraction-curious · Retro |
| 14 | `Jump Tables - Z80` | What a `switch` actually compiles to | Z80 | CONTROL FLOW | `#cc0000` | Performance · CS students |

---

## Interactions & Behavior
- **Navigation:** Index card → article (whole card is the link). Article masthead "← FROM THE METAL · <CPU>" → index. Index footer → messaging board. Board cards (4, 5, 6, 8, 10) → their linked article. All plain `<a href>` navigation; no JS routing in the prototype. In production these become Astro routes / MDX links.
- **Card hover (index):** lift `translateY(-4px)`, grow chunky shadow to `9px 9px 0` in accent, border → accent. `0.3s cubic-bezier(0.16,1,0.3,1)`.
- **Link hover:** color shift only (faint → C64 blue / accent), no underline.
- **Blinking caret:** index footer, `@keyframes` toggling opacity at `steps(1)`, 1s infinite.
- **No other animation, no parallax, no scroll-jacking.** Respect `prefers-reduced-motion: reduce` (disable hover transitions + blink) when implementing.
- **Print/PDF:** article template is designed to export clean Letter pages — preserve `break-inside: avoid` on `figure`/`pre`/`blockquote`, `break-after: avoid` on headings, and the reserved top/bottom page margins.

## State Management
None. These are static content pages — no client state, no data fetching, no forms. In the Astro target, all content is build-time. The only "state" is CSS hover/focus.

## Design Tokens

**Surfaces & text**
- Page background: `#f4f1e8` (`--c-bg`)
- Card / callout surface: `#fdfcf7` (`--c-surface`)
- Card border: `#e7e1cf` (3px); section rules: `#e0d9c6` (3px); dashed rules: `#e0d9c6`
- Body text: `#1e293b` (`--c-fg`); secondary `#475569`; faint label `#94a3b8`; faintest tag `#a8a08a`
- Inline code chip bg: `#ece7d6`
- Code block: bg `#0f172a`, text `#e2e8f0`, header bar `#1e293b`
- Code comment spans: neutral `#7d8da3`, emphasis amber `#f0a868`, elision `#5b6b86`
- Metric/state colors: bad `#fca5a5`, good `#86efac`, mid `#fcd34d`

**Brand platform colors** (design system)
- C64 `#4a4dff` · Spectrum `#cc0000` · NES `#e30613` · Amiga `#ff6600`

**Accent color system** (per-card/article — topic-coded, intentionally broader than the 4 platform hues for legibility across 14 items): values are in the catalogue table. Keep as-is.

**Typography**
- Display/UI/code: **JetBrains Mono** (400/500/600/700)
- Body: **Inter** (400/500/600 + 400 italic)
- Scale (article): H1 `clamp(30px,5.2vw,44px)`/700/lh1.08/-0.5px; H2 22px/700; lede 20px/lh1.55; body 17px/lh1.68; caption 13px italic; code 14px/lh1.75; inline code 0.82em.
- Scale (index): H1 `clamp(36px,6.5vw,60px)`/700/lh1.02/-1.5px; card H2 18px/700/lh1.18; card teaser 14px/lh1.5.

**Spacing & shape**
- Border radius: `0` on cards/buttons/badges; `4px` on inline `<code>`/`<kbd>` only.
- Card border: 3px solid. Section rules: 3px solid.
- Shadows (no blur): cards `5px 5px 0 rgba(0,0,0,0.10)` → hover `9px 9px 0 <accent>@~0.18-0.20`; callouts/board cards `6px 6px 0 rgba(0,0,0,0.10)`.
- Index grid gap 24px; article max-width 760px; index max-width 1120px; board max-width 840px.

**Motion**
- Card transition: `0.3s cubic-bezier(0.16,1,0.3,1)` (transform, shadow); `0.15s` (border/color).
- Blink: `steps(1)`, 1s, infinite.

## Assets
- **Fonts:** Google Fonts — Inter + JetBrains Mono. The prototypes load them via `<link>`; in the Astro target use the existing Astro Font API setup (the design system already provisions both).
- **No images, icons, or logos** are used in these designs. The "CODE LIKE IT'S 198x" wordmark is plain styled text, not the SVG logo. (If you prefer, swap in the production `logo-stacked.svg` from the design system — optional.)
- **No emoji.** The only non-text glyphs are `>`, `→`, `//`, `←`, all typed characters.

## Responsive behavior
Prototypes are desktop-first. For production, apply the design system's responsive layer:
- Index 3-col grid → 2 → 1 column on narrow viewports.
- Board single-column stack already adapts (just reduce side padding).
- Article column is already fluid (`max-width: 760px` + `clamp()` padding); ensure `<pre>` blocks scroll horizontally on mobile (`overflow-x: auto`, already set).

## Screenshots
`screenshots/` contains one reference render per design, numbered to match the catalogue:
`00-index.png`, `01-unroll-loops.png` … `14-jump-tables.png`, `15-messaging-board.png`. Use them to
check layout, type scale, spacing, and color while implementing.

## Build plan
See **`CLAUDE.md`** for a recommended implementation order, the Astro/MDX content mapping, a
`<CodeFigure>` component spec, and a fidelity checklist.

## Files
All under `designs/`:
- `From the Metal - Index.dc.html` — the hub (start here).
- 14 article files — see the catalogue table for the full list and what each covers.
- `Five Audiences.dc.html` — the messaging board.
- `support.js` — the in-house `.dc.html` runtime, included **only** so the prototypes open and render in a browser for reference. **Do not port it.** Read the design intent from the markup, ignore the runtime.

> To preview: open any `.dc.html` in a browser (they reference `support.js` locally). The markup between `<x-dc>…</x-dc>` is the design; everything is inline-styled, so it reads straight off the source.
