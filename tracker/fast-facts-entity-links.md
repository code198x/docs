# Fast Facts as entity references

**Status:** Measured, not yet acted on
**Scope:** Vault content (`code198x/website`, `src/content/vault/`) and the Vault entry layout
**Measured:** 2026-08-27, while planning the freeform-structure change

---

## The finding

Fast-facts blocks are already structured data wearing markdown. Across 1,285 entries:

- **5,822 pairs**, and **every one** is in `**Label:** value` form. Nothing needs parsing
  heuristics.
- Median value is **40 characters**, p90 is **88**. Only 5% run past 120.
- **1,664 distinct labels** — this is per-entry key/value, not a fixed schema. It renders as
  a definition list, not a table.

The part worth acting on: **908 pairs (16%) name something that already has a Vault entry
and do not link to it.** Only 106 pairs (2%) currently link. Counting each name inside a
comma-separated value separately gives **1,042 resolvable references**.

That is a backlog of missing internal links, sitting in the most structured part of the
Vault, in the place a reader is most likely to want to click.

## Where the links would go

| Target category | Refs | |
|---|---:|---|
| companies | 424 | 41% |
| games | 187 | 18% |
| **people** | **183** | **18%** |
| systems | 74 | 7% |
| magazines | 54 | 5% |
| groups, techniques, culture, tools, other | 120 | 12% |

The labels cluster by entity type, which is what makes typed values possible:
`Developer`, `Publisher`, `Company`, `Manufacturer`, `Founder`, `Creator`, `Designer`,
`Director`, `Group` → people and companies. `Platform`/`Platforms` → systems.
`Known for` → games. `Press evidence in this library` → magazines.

## ⚠ Why this must not be an automatic migration

**82% is safe to resolve mechanically. The 18% that lands on `people/` is not.**

Only two Vault titles collide outright — `fairlight` (group and game) and `renegade` (game
and company) — and only 2 of the 1,042 references touch them. That test is reassuring and
it measures the wrong thing.

The real hazard is a name that resolves to exactly one entry and still means somebody else.
[`people/david-jones-magic-knight`](../../website/src/content/vault/people/david-jones-magic-knight.mdx)
is the standing case: the Vault held **two** entries for the DMA Design founder and **none**
for the Mastertronic *Magic Knight* author of the same name. A name-matching linker would
have pointed every David Jones credit at the wrong man with full confidence, and a
collision test would not have flagged it, because there was only ever one entry with that
title.

That entry states the rule it came from: **a name is not an identifier.** Where a credit is
the only evidence, the honest options are to disambiguate explicitly or to leave the link
out — never to guess.

So:

- **Non-person references (859):** safe to resolve mechanically, with the output reviewed as
  a diff rather than trusted.
- **Person references (183):** generate as *candidates*. Each needs a human to confirm the
  name in the credit is the person in the entry.

## Options, not a plan

**Nothing here is decided.** A sidebar was raised as a possibility, not chosen, and the
scope question it belongs to is still open. What follows is the design space as measured.

### Two separate decisions

**How fast facts render** is presentational. **What form the underlying pairs take** is
architectural. They are worth deciding together only because one pass would touch the same
1,285 entries.

The [Knowledge Model](../PRINCIPLES.md) is a third thing again, and does not constrain
either: it is an internal store for tracking connections between entities, never a published
surface. A rendered fast-facts block is a *consumer* of facts, not a home for them.

### Rendering

The Vault page already has `aside.vault-sidebar` at `1fr 260px`, carrying the table of
contents, a **Details** block built from frontmatter, and Browse links. Fast facts would sit
beside `Details`, which already duplicates part of it — founding dates and platforms appear
in both.

Taking the pairs out of the prose flow is what actually frees the body to be freeform, which
is the point of the structure change in the spec.

### Source format — the decision worth making carefully

This is the seam a knowledge store would later attach to, so it is where optionality is
worth preserving.

All 5,822 pairs are already `**Label:** value`, so they are parseable today. But parsing
prose to recover structure is fragile, and 1,664 distinct labels means no schema is being
enforced — `Founded` and `Founder`, `Platform` and `Platforms`, `Creator` and `Creators` all
coexist.

If the pairs move into frontmatter or a typed block during the rendering work, they become
directly consumable rather than recoverable-by-regex, at little extra cost over the same
pass. If they stay as prose bullets, every future consumer re-implements the parse.

⚠ **A typed format should not force a schema.** 1,664 labels is not sloppiness — a magazine
entry and a CPU entry genuinely need different facts. Typing the *reference* (this value
points at an entity) is separable from constraining the *label set*, and only the first is
needed to make the 1,042 relationships machine-readable.

### Independent of that choice

Two items hold whichever way the above goes.

1. **The 29 caveat bullets.** 29 fast-facts pairs carry a ⚠, and 28 of those are the long
   ones — Gargoyle's "there was a third", CRL's provenance note, the "press evidence in this
   library" coverage warnings. Those are arguments, not facts. They read better in prose and
   would not survive a move into a data structure.
2. **Rail width, if Option A.** At p90 of 88 characters, values wrap to two or three lines
   in 260px.

### Verification status has nowhere to live

Scrubbing the corpus-coverage boilerplate (`code198x/website#287`) surfaced a gap this
tracker should hold.

**238 of 239 company entries carry a `founded:` value in frontmatter**, rendered by the
sidebar as "Active: 1980–…". Exactly one entry — `companies/crl-group` — said in prose that
its value was unsourced, and that note has now gone with the rest of the boilerplate.

The note was in the wrong place, but it was recording something real. CRL's `founded: 1980`
is not supported by anything in this library, and the page asserts it anyway. The other 237
are not thereby verified; they are simply unannotated, and there is no way to tell the two
states apart.

`PRINCIPLES.md` says each fact should where practical retain its sources, confidence and
verification status, and separately that uncertainty should be preserved rather than
manufactured. A published date with no verification field does the opposite by default.

This was the clearest small case for whatever the fact format turned out to be: a `founded`
value wants a source beside it, not a paragraph elsewhere on the page apologising for it.

**Half settled.** `sources` now carries per-field evidence, and eleven company registrations
are cited to Companies House.

CRL is not one of them, and the near miss is worth keeping. Company 01472275 is "CRL Group
Ltd", incorporated 1980-01-11 — matching this Vault's CRL on name and on year, which is
exactly why it was believed. It was CLWYD REFRIGERATION LIMITED until 2016: a Conwy
refrigeration business that took the name thirty-six years after Clement Chambers founded
the games publisher. `previous_company_names` and the registered office settle it, and
neither had been checked.

So CRL's `founded: 1980` remains unsourced, and the general problem stands: most `founded`
values carry no source, and absence means only that nobody has checked.

### What would change the reading

- If most of the 4,808 non-resolvable values turn out to be restatements of the prose, fast
  facts is worth shrinking rather than relocating.
- If the 183 person references have a high error rate on inspection, name-matching is
  unsafe for the mechanical 859 too, and the whole pass becomes manual.
- If a second consumer (Emu198x, Asm198x) wants these facts, Option A stops being viable and
  C becomes a holding position rather than a choice.
