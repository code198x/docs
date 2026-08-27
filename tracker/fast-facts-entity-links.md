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

## How this fits the sidebar

The Vault entry layout already has `aside.vault-sidebar` at `1fr 260px`, carrying the table
of contents, a **Details** block rendered from frontmatter, and Browse links. Fast facts
belongs beside `Details` rather than in the prose flow — and `Details` already duplicates
some of it, since founding dates and platforms appear in both.

Two open questions for that work:

1. **Rail width.** At p90 of 88 characters, values wrap to two or three lines in 260px.
   Fine for `Developer: Midway`, cramped for a list of six colleagues.
2. **The 29 caveat bullets.** 29 fast-facts pairs carry a ⚠, and 28 of those are the long
   ones — Gargoyle's "there was a third", CRL's provenance note, the "press evidence in this
   library" coverage warnings. Those are arguments, not facts, and belong in the prose where
   the argument lives. They should move before any migration, not during it.

## Sequence

1. Spec floor — done, `code198x/docs#8`.
2. Sidebar design: component, rail width, and the 29 caveats moved to prose.
3. Entity-link pass: 859 mechanical, 183 by hand.
4. Only then sweep `## Overview` out of the entries, against the final shape.

Doing 4 before 2 means two large diffs across the same paragraphs.
