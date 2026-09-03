# Decision: Website visual language

**Scope.** This record owns what the site *looks like*. It sits under
[`198x/decisions/family-visual-identity.md`](https://github.com/198x/198x/blob/main/decisions/family-visual-identity.md),
which is umbrella-scoped and binds the wordmark, palette and type roster of every
sibling. Where the two meet, the family record wins unless this one names the
rule it is overriding and why. **Sequencing and migration mechanics live in
[`adopting-198x-ui.md`](adopting-198x-ui.md)** — decisions about the language go
here, not there.

**Reconciled with the family record 2026-09-03.** The type section below had gone
stale: it still re-roled Caveat and Inter eight days after the family record
retired both, without naming it. That is the quiet shadowing `CLAUDE.md` warns
about, and it is fixed in place rather than noted as superseded.

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

## Type — the family roster, three faces, three jobs

Set by the family record §4. Three faces, and the site does not add a fourth.

- **Nebula Sans** — interface, headings, the slogan. Headings are **sentence case**; replacing mono-uppercase headings is the single biggest de-genericiser.
- **Literata** — long-form reading, editorial display, all captions. Unit prose is long-form reading, so it sets here rather than inheriting the interface face. Its optical-size axis is the mechanism when a surface wants a different voice — not another family.
- **JetBrains Mono** — the machine voice only: code, terminal and CRT blocks, status badges, eyebrows, data labels.

**Caveat and Inter are retired**, along with Special Elite, Russo One, Oxanium and Orbitron. Caveat's display role — masthead, hero, pull-quotes, drop caps, marginalia — passes to Literata at display optical size. The character that face was carrying comes from the palette, from Literata, and from the writing.

**Display headings reserve their descender.** Line-heights here are unitless
multipliers, and display headings set them below 1 for tight multi-line stacking.
Literata's content area is about 1.48em, so at any usable display ratio its ink
drops past the element box and collides with whatever sits close beneath — the
Vault strapline was the first casualty. Measured at 84px: 0.82 overlaps by
19.6px, 1.0 by 12.5px, and **the family record's own display ratio of
`calc(68 / 64)` still overlaps by 9.8px**. Nothing clears until about 1.35, which
is body leading on a display heading.

So the fix is `padding-bottom: 0.25em` on the heading, in em so it tracks the
`clamp()`, rather than loosening the leading. This is a property of the face, not
a symptom of badly-tuned line-heights, and it applies to anything setting Literata
large — the kit's type scale included.

Muted tokens (`#94a3b8`) are decorative and large-only, **never small informational text**. `--color-text-muted` currently holds that value and is used as though it were body-safe; that is a live defect against this rule.

## What carries over from production

Token architecture, spacing scale, semantic colours, dark mode, responsive layer, `prose.css`. The **67-system manifest with auto-emitted `--p-{id}-primary` tokens and the 25° hue-collision rule** — the binding answer to per-system identity, superseding any bespoke-motif-per-machine approach. The lesson diagram primitives. Square corners and 3px borders as the structural signature, held constant everywhere so the site never feels like two sites.

**The chunky offset shadow is retired** (2026-09-03). It was named here as part of that signature; it went because it was not liked, and the family record's lift ladder — soft shadow in light, neutral glow in dark — replaces it. Square corners and the border weight carry the signature on their own. Real saturated system colours, used only inside that system's pages, with site chrome staying neutral.

## Reconciled conflicts

**Corners:** square wins — it is the signature. Warmth comes from texture and type, not rounding.

**Voice:** editorial surfaces are self-deprecating first person; instructional surfaces are confident second person with almost no "we". No emoji; Lucide icons and period glyphs only.

## Dark mode — warm ink on dark paper

The brand is warm newsprint, so night mode stays warm rather than turning cool slate-navy: warm-charcoal page `#1a1714`, cream text `#efe7d6`, accents brightened. It reads as the same product with the lights down, not a separate theme. It lives as a `[data-theme="dark"]` token block in the shared token sheet.

- **Lift changes medium rather than colour.** Shadow models ink on paper and a dark ground is not paper, so lift becomes a neutral glow in dark — the thing emits rather than casts, which is what these machines did. One ladder, two renderings, from the family record §6.
- Textures invert to faint light dots; bright elements dim to avoid glare; already-dark code blocks are unchanged.
- **Theme control is three-way: Auto / Light / Dark.** Auto follows `prefers-color-scheme`; the two overrides persist in `localStorage` and apply through an inline no-FOUC `<head>` script before paint.

## Drift triggers

- Setting unit-page body prose or a code listing in a display face, or reaching for a fourth family when a surface wants a different voice. Literata's optical-size axis is the mechanism.
- Marginalia built with absolute positioning or hardcoded offsets — it will not survive variable content.
- Proposing a second full page template where a view or a mode over an existing one would do.
- A wholesale pivot to either pole: "let's just go full fanzine", "drop the paper stuff and ship it clean".
- Mono-uppercase returning as the default heading style.
- A bespoke per-machine motif system competing with the system manifest.
- New typefaces added before the family roster of three is proven insufficient.
- **Removing a display heading's `padding-bottom` as redundant**, or "fixing" the
  collision it prevents by loosening the leading. Literata does not clear its own
  descender until about 1.35; see § Type.
- **Reinstating the chunky offset shadow**, or reading square corners and 3px borders as needing a hard shadow to complete them. They carry the signature alone; the shadow was retired on 2026-09-03.
- **Overlap or bleed built into a unit's reading column.** Character is zoned to the margins there for a stated reason — a learner is in that column for thirty to ninety minutes.
