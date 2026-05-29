# Decision: Visual direction — synthesise, don't pivot

## The decision

The site's visual language is a **synthesis**: production's system architecture
(the bones) carrying the fanzine exploration's period character (the soul), as one
coherent language whose character density is dialled by surface per
[website-design-zoning.md](website-design-zoning.md).

It is **not** a pivot to the fanzine wireframes, and **not** the shipped production
aesthetic left as-is. Rejected alternatives: evolving production only (keeps the
dev-tool genericness), pivoting wholesale to the fanzine (abandons working,
systematic infrastructure), running two visually separate zones (risks reading as
two different sites).

## Why this is low-risk: the two poles already converge

The shipped production system and the fanzine exploration independently agreed on most
of the system:

| Axis | Production | Fanzine | Verdict |
|---|---|---|---|
| Background | beige `#f4f1e8` | paper `#f4ecdc` | same warm cream |
| Card shadow | chunky `4px 4px 0` | chunky `3px 3px 0` | same hard-offset gesture |
| Platform colour | real, per-system | per-platform tokens | same idea (production's is mature) |
| Nav term | `SYSTEMS` | "Platforms" | production already matches [systems-not-platforms.md](systems-not-platforms.md) |
| Body face | Inter | handwriting (the bug) | production is right |
| Script face | Caveat (`--font-script`) | Caveat (the display face) | both already ship it |

Genuine divergence is only **two axes**: type roles and character density. Everything
else is shared, so synthesis is mostly re-roling and additive texture — not a rebuild.

## What we keep from production (the bones)

- Token architecture, spacing scale, semantic colours, dark mode, responsive layer,
  `prose.css`.
- The **67-platform manifest + auto-emitted `--p-{id}-primary` tokens + hue-collision
  audit (the 25° rule)**. This is the binding answer to per-system identity scaling and
  supersedes any bespoke-motif-per-machine approach.
- Lesson diagram primitives (`SpriteGrid`, `SpriteEditor`, `RegisterBits`,
  `MemoryMap`, `CodeFromFile`).
- Square corners + 3px borders + chunky offset shadow as the structural signature,
  held constant across every surface so the site never feels like two sites.
- Real saturated platform colours (not the fanzine's muted proxies); platform-neutral
  site chrome, platform colour only inside that system's pages.

## What we take from the fanzine (the soul), zoned

Paper/halftone texture, magazine gestures (kicker, drop cap, pull-quote, sticky-note
marginalia), period display type, the honest-tier status system, the self-deprecating
editorial voice — **full on discovery/editorial surfaces, restrained on reading/app
surfaces.**

## Type — re-role, no new fonts

Inter, JetBrains Mono, and Caveat are all already loaded in production. Synthesis
re-roles them rather than choosing new ones:

- **Caveat (`--font-script`)** — soul / display: masthead, hero, pull-quotes, drop
  caps, marginalia. Accent-only, hard size floor ~28px.
- **Inter** — body at 16–17px; headings in **Inter 800/900, sentence case**. This
  replaces mono-uppercase headings and is the single biggest de-genericiser.
- **JetBrains Mono** — the **"machine voice"** only: code, terminal/CRT blocks, status
  badges, eyebrows, data labels.
- Drop Special Elite / Russo One / Oxanium / Orbitron from the working set (logo
  experiments at most). Caveat is auditionable but sufficient for v1.
- Contrast: slate body (`#1e293b`) is strong; **muted tokens (`--c-fg-muted`
  `#94a3b8`; the fanzine's `--ink-faint`) are decorative / large-only — never small
  informational text.**

## Reconciled conflicts

- **Corners:** square wins (the signature). Warmth comes from texture and type, not
  rounding.
- **Voice:** editorial surfaces are self-deprecating first-person; instructional / app
  surfaces are confident second-person, almost no "we". No emoji (production
  discipline); Lucide icons + period glyphs only.

## Dark mode

Warm "ink on dark paper" — **ratified over production's cool slate-navy.** The brand is
warm newsprint; night mode stays warm (warm-charcoal page `#1a1714`, cream text
`#efe7d6`, accents brightened) so it reads as the same product with the lights down,
not a separate cool theme. Lives as a `[data-theme="dark"]` token block in the shared
token sheet (→ `Layout.astro`).

- **Hard shadows flip to a warm offset *lighter* than the page** (~`#322a1c`), not a
  darker black — black-on-near-black vanishes. Reads as a "second sheet behind the
  card," on brand for print.
- **Textures invert** (faint light dots); bright elements (sticky notes) dim to avoid
  glare; already-dark code blocks are unchanged.
- **Theme control is three-way: Auto / Light / Dark.** Auto follows
  `prefers-color-scheme`; Light and Dark are explicit overrides, persisted
  (localStorage), applied by an inline no-FOUC `<head>` script before paint. Production
  already ships the persistence + anti-FOUC pattern — extend its toggle from two-way to
  three-way.

## Drift triggers

- Proposing a wholesale pivot to either pole ("let's just go full fanzine"; "drop the
  paper stuff and ship it clean").
- Mono-uppercase returning as the default heading style.
- A bespoke per-machine motif system competing with the platform manifest.
- New typefaces added before the re-roled three are proven insufficient.

## Anchored in

- [website-design-zoning.md](website-design-zoning.md) — how character density is dialled by surface
- [systems-not-platforms.md](systems-not-platforms.md), [system-url-structure.md](system-url-structure.md)
- Production design system: `github.com/code198x/website` (`src/layouts/Layout.astro` tokens, `astro.config.mjs` fonts).

## Log

| Date | Event |
|---|---|
| 2026-05-29 | Synthesis chosen over pivot / evolve / two-zones after reviewing the production design system against the fanzine wireframes. |
| 2026-05-29 | Mocked the full surface set (home, fleet, system landing, game landing, unit, vault, planned stub) on a shared `synthesis.css` token sheet. Dark mode ratified as warm "ink on dark paper" (not cool slate); theme control is three-way Auto/Light/Dark; dark hard-shadows use a warm offset lighter than the page. |
