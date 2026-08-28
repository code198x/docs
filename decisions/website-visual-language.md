# Decision: Website visual language

The site's visual language is a **synthesis**: the production design system's architecture carrying the fanzine exploration's period character, as one language whose density is dialled by surface.

It is not a pivot to the fanzine wireframes, and not the shipped production aesthetic left alone. Evolving production only keeps the dev-tool genericness; pivoting wholesale abandons working infrastructure; running two visually separate zones risks reading as two sites.

The two poles already agree on most of it — warm cream background, chunky hard-offset shadow, per-system colour, "SYSTEMS" as the nav term, Caveat already loaded. Genuine divergence is two axes: **type roles and character density**. So this is re-roling and additive texture, not a rebuild.

## Zoning — character in the margins, legibility in the column

Character is zoned by surface, not applied uniformly.

**Discovery and marketing surfaces** — homepage, system landing, fleet, timeline, vault, contribute — carry full character: handwritten display headings, tilt, paper grain, marker highlights, sticky notes, CRT shots.

**Reading surfaces**, unit pages above all, keep character in the margins and the voice: kicker, drop cap, system stripe, sticky-note asides, chatty "Try this" boxes, a cartoon in the corner. **Body prose and code listings are set in genuinely legible faces at AA contrast** — never Caveat or Patrick Hand at paragraph scale.

The rule is that **character and legibility are separate levers**. The 1984 precedent — Usborne books, the Crash and Input type-in pages — was hugely characterful *and* set its body copy and listings in clean type. The amusement came from everything around the text, never from making the read harder.

A learner reads a unit page for thirty to ninety minutes. It has to be the calmest surface, or the period homage becomes an accessibility bug.

## Views are cheap, templates are debt

Where two page designs both look right, the test is whether the alternate is a different template or a different view of the same data.

- **Fleet** (timeline / by-maker / by-tier) — views over one dataset via `?by=`. One page, a view switcher.
- **Curriculum overview** (TOC / guided) — one template. The TOC is the page; "New here? start with these →" is an affordance on it.
- **Unit** (marginalia / sidebar) — one reading template, the calm sidebar. BASIC and assembly differ by **character density layered on top**: BASIC units get type-in marginalia and a chattier voice, assembly runs austere. A flag decides how much fanzine is poured on, not a second template.

Six maintained templates collapse to three, each with a couple of modes. That matters for a solo maintainer.

## Type — re-role, no new fonts

Inter, JetBrains Mono and Caveat are already loaded. They are re-roled rather than replaced.

- **Caveat** (`--font-script`) — display only: masthead, hero, pull-quotes, drop caps, marginalia. Hard size floor around 28px.
- **Inter** — body at 16–17px; headings in **Inter 800/900, sentence case**. Replacing mono-uppercase headings is the single biggest de-genericiser.
- **JetBrains Mono** — the machine voice only: code, terminal and CRT blocks, status badges, eyebrows, data labels.
- Special Elite, Russo One, Oxanium and Orbitron leave the working set.
- Muted tokens (`--c-fg-muted` `#94a3b8`, the fanzine's `--ink-faint`) are decorative and large-only, never small informational text.

## What carries over from production

Token architecture, spacing scale, semantic colours, dark mode, responsive layer, `prose.css`. The **67-system manifest with auto-emitted `--p-{id}-primary` tokens and the 25° hue-collision rule** — the binding answer to per-system identity, superseding any bespoke-motif-per-machine approach. The lesson diagram primitives. Square corners, 3px borders and the chunky offset shadow as the structural signature, held constant everywhere so the site never feels like two sites. Real saturated system colours, used only inside that system's pages, with site chrome staying neutral.

## Reconciled conflicts

**Corners:** square wins — it is the signature. Warmth comes from texture and type, not rounding.

**Voice:** editorial surfaces are self-deprecating first person; instructional surfaces are confident second person with almost no "we". No emoji; Lucide icons and period glyphs only.

## Dark mode — warm ink on dark paper

The brand is warm newsprint, so night mode stays warm rather than turning cool slate-navy: warm-charcoal page `#1a1714`, cream text `#efe7d6`, accents brightened. It reads as the same product with the lights down, not a separate theme. It lives as a `[data-theme="dark"]` token block in the shared token sheet.

- **Hard shadows flip to a warm offset lighter than the page** (~`#322a1c`). Black on near-black vanishes; a lighter offset reads as a second sheet behind the card, which is on brand for print.
- Textures invert to faint light dots; bright elements dim to avoid glare; already-dark code blocks are unchanged.
- **Theme control is three-way: Auto / Light / Dark.** Auto follows `prefers-color-scheme`; the two overrides persist in `localStorage` and apply through an inline no-FOUC `<head>` script before paint.

## Drift triggers

- Setting unit-page body prose or a code listing in a handwriting face.
- Marginalia built with absolute positioning or hardcoded offsets — it will not survive variable content.
- Proposing a second full page template where a view or a mode over an existing one would do.
- A wholesale pivot to either pole: "let's just go full fanzine", "drop the paper stuff and ship it clean".
- Mono-uppercase returning as the default heading style.
- A bespoke per-machine motif system competing with the system manifest.
- New typefaces added before the re-roled three are proven insufficient.
