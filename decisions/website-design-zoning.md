# Decision: Design zoning — character in the margins, legibility in the column

## The decision

The site's fanzine/magazine character is **zoned by surface**, not applied uniformly:

- **Discovery / marketing surfaces** (homepage, system landing, fleet, timeline,
  vault, contribute): full character — handwritten display headings, tilt, paper
  grain, marker highlights, sticky notes, CRT shots.
- **Reading surfaces** (unit pages above all): character lives in the *margins and
  the voice* — kicker, drop cap, system stripe, sticky-note asides, chatty "Try this"
  boxes, a cartoon in the corner. **Body prose and code listings are set in genuinely
  legible faces** (not Caveat / Patrick Hand at paragraph scale), at AA contrast.

The rule: **character ≠ degraded legibility.** They are separate levers. The 1984
precedent — Usborne books, the Crash/Input type-in pages — was hugely characterful
*and* set its body copy and listings in clean type. The amusement came from
everything around the text, never from making the read harder. The goal is "learning,
amusingly," not a choice between the two.

## Resolving the "two winners, both valid" page types

Test: **is the alternate a different template, or a different view of the same data?
Views are cheap. Templates are debt.**

- **Fleet (timeline / by-maker / by-tier):** views over one dataset (`?by=`). Keep all
  three — one page, a view switcher.
- **Curriculum overview (TOC / guided):** one template. The TOC is the page; "New
  here? start with these →" is an affordance on it, not a second page.
- **Unit (marginalia / sidebar):** one reading template (the calm sidebar). The
  BASIC-vs-assembly difference is **character density layered on top** — BASIC units
  get the type-in marginalia and chattier voice; assembly units run austere — not two
  divergent templates. A flag toggles how much fanzine is poured on.

Net: six maintained templates collapse to three, each with a couple of modes. That
matters for a solo maintainer.

## Why

- The unit page is where a learner reads for 30–90 minutes. It must be the calmest
  surface, or the period homage becomes a usability and accessibility bug
  (handwriting body text + low-contrast small caps).
- Zoning lets the site be *more* playful than a docs site on discovery surfaces while
  staying readable where reading happens.
- Fewer divergent templates is less debt for one person.

## Drift triggers

- Setting unit-page body prose or a code listing in a handwriting face.
- Marginalia built with absolute positioning / hardcoded offsets — it won't survive
  variable CMS content (see the design exploration's `UnitMagazineTypein`, which only
  holds together at a fixed artboard size).
- Proposing a second full page template where a view or mode over an existing one
  would do.

## Anchored in

- [Information architecture](../specifications/information-architecture.md)
- [Writing voice](../specifications/writing-voice.md) — magazine-class prose, anti-patterns
- CLAUDE.md Design Context — anti-pattern "dense academic walls of text"; voice "warm, never condescending"
- Distinct from [visual-enhancement-pass.md](visual-enhancement-pass.md), which is about in-game BASIC visuals, not site chrome.

## Log

| Date | Event |
|---|---|
| 2026-05-29 | Zoning principle + deferred page-type resolution recorded from the design critique discussion. |
