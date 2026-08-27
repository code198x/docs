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

### Where the facts could live

The measurement above is a fact. What to do about it is not, and the choice is
architectural rather than presentational.

**Option A — render them in the entry layout.** The Vault page already has
`aside.vault-sidebar` at `1fr 260px`, carrying the table of contents, a **Details** block
built from frontmatter, and Browse links. Fast facts would sit beside `Details`, which
already duplicates part of it. Cheapest path; serves one consumer.

⚠ **This narrows the design space in the direction `PRINCIPLES.md` says to keep open.** The
Knowledge Model puts facts above the documents that describe them — independently
maintainable, carrying their own sources and confidence, reusable across the ecosystem, with
pages assembling from shared knowledge rather than owning it. 5,822 `**Label:** value` pairs
across 1,664 labels, plus 1,042 references to other entities, is a nascent entity–fact–
relationship store. Binding it to one repo's page layout spends that.

**Option B — lift the pairs into structured data** that any consumer can read, attach
evidence to each fact, and let the website render it. Serves the Knowledge Model directly.
Much larger, and `PRINCIPLES.md` also says not to stop development to design a perfect
ontology.

**Option C — do neither yet.** Fix the 908 links in place, in the markdown, and leave the
question of where facts live until the shape has been used more.

The two are separable: *how fast facts render* and *where facts live* are different
decisions, and treating them as one is what produced the sidebar-shaped answer.

### Independent of that choice

Two items hold whichever way the above goes.

1. **The 29 caveat bullets.** 29 fast-facts pairs carry a ⚠, and 28 of those are the long
   ones — Gargoyle's "there was a third", CRL's provenance note, the "press evidence in this
   library" coverage warnings. Those are arguments, not facts. They read better in prose and
   would not survive a move into a data structure.
2. **Rail width, if Option A.** At p90 of 88 characters, values wrap to two or three lines
   in 260px.

### What would change the reading

- If most of the 4,808 non-resolvable values turn out to be restatements of the prose, fast
  facts is worth shrinking rather than relocating.
- If the 183 person references have a high error rate on inspection, name-matching is
  unsafe for the mechanical 859 too, and the whole pass becomes manual.
- If a second consumer (Emu198x, Asm198x) wants these facts, Option A stops being viable and
  C becomes a holding position rather than a choice.
