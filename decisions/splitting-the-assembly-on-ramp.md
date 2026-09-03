# Decision: how the assembly on-ramp gets split, and in what order

**Status:** ACCEPTED — 2026-09-03. Implements
[`front-of-curriculum-architecture.md`](front-of-curriculum-architecture.md),
which decided the split on 2026-06-05 and has been built for every language
except assembly. This record decides only the *sequence*, because doing it as
one job means re-cutting 69 published units a month before Crash! Live.

## Where the tree is

Counted from `src/content/curriculum/` on 2026-09-03, not from a tracker:

| Layer | Spectrum | C64 | NES | Amiga |
|---|---|---|---|---|
| 1 · General Programming | built, shared — 11 units, plus Numbers and Bits at 6 | — | — | — |
| 2 · Machine briefing | **missing** | **missing** | **missing** | **missing** |
| 3 · Meet \<language\> | Meet BASIC 15 | Meet C64 BASIC 15 | *no BASIC on the hardware* | Meet AMOS 17, Meet Blitz 15 |
| 3 · Meet Assembly | **absent — 16 units inside `meet-the-machine`** | **absent — 16** | **absent — 18** | **absent — 19** |

The split is done for every language except the one all four systems share.
Layer 2 does not exist anywhere.

## Why it is not a file move

The seam runs through the middle of units, not between them. The Spectrum's
unit 6 is:

```
## The attribute byte                   <- briefing
## Two consequences worth holding onto  <- briefing
## Assemble and run                     <- Meet Assembly
## Try this: mix your own colour        <- Meet Assembly
## When it's wrong, see why             <- Meet Assembly
```

Every machine-fact unit has that shape, because that is what the old design
asked for — the units teach the machine *through* assembly, which is the
conflation the 2026-06-05 record was written to end.

## The decision — three jobs, not one

1. **Rename the on-ramp to Meet Assembly.** Mechanical: 163 prose links, 82
   files, 79 code-sample directories, plus redirects for URLs live since June.
   Changes no content, and makes the tree speak the decision's vocabulary.
2. **Write the briefing as a new module.** Additive. Nothing existing is
   re-cut, no links move, no published unit changes.
3. **Trim the briefing-shaped halves out of the existing units.** Editorial and
   expensive. Unit by unit, opportunistically, as those units are revised
   anyway — every one still recommends pasmo.

**Order: 2, then 1, then 3.** Step 2 delivers what the curriculum is missing
and risks nothing. Step 1 is an afternoon whenever convenient. Step 3 rides
along with revisions already due.

**Scope: the Spectrum first.** Steps 1 and 2 are per-system independent, and
the Spectrum is the Crash! Live track. The other three follow the pattern once
it has been proved once.

**Accepted cost: temporary duplication.** Colour and the screen get introduced
in the briefing and again in the on-ramp until step 3 catches up. Untidy in a
way a reader does not notice, and better than re-cutting the launch track in
September.

## Where the briefing lives

It feeds *every* language path for a machine, so it cannot sit under
`assembly/`. The route (`src/pages/[...slug].astro`) special-cases Foundations
by asking `getSection(platformSlug)` and otherwise requires
`{system}/{track}/{module}/{unit}`, with the track typed
`'assembly' | 'basic' | 'amos' | 'blitz'`.

A track-less `{system}/{module}/{unit}` would render with the fallback unit
count and wrong breadcrumbs. **So the briefing takes a pseudo-track segment**
— `{system}/machine/meet-the-machine/{unit}` — which needs only the track
union widened and a units catalogue entry, rather than a second path shape in
the router.

The name goes back to what the 2026-06-05 record assigned it: *Meet the
Machine* keeps its name in its briefing role, which is why step 1 has to
happen before the old module can be trimmed into it.

## What the Spectrum briefing contains

Per the record it must **stay concrete** — the constraints shown running, not
lectured. That is newly practical: the emulator now embeds in a lesson page
and boots from a tape in about a second, so a briefing unit can *show* a
constraint rather than describe it.

Five units, each ending in something on screen:

1. **A Machine From 1982** — what it was, what it cost, who bought it, why
   there were so many of them. Boots to the copyright line.
2. **The Z80 Inside It** — an 8-bit CPU at 3.5 MHz, and what that number buys.
   Shows work that finishes instantly against work that visibly does not.
3. **Sixteen Colours, Eight at a Time** — the attribute file, and clash as the
   consequence. The constraint that gives the machine its look.
4. **One Bit of Sound** — the beeper: on or off, and everything else is timing.
5. **48K, and Where It Goes** — ROM, screen, your program, and running out.

*What assembly is, and why it matters* is **not** here. It is layer 3 and opens
Meet Assembly — and `foundations/from-source-to-silicon` is scaffolded and may
already own the language-neutral half of that answer. Check before writing it
twice.

## Related

- [`front-of-curriculum-architecture.md`](front-of-curriculum-architecture.md) — the split this sequences
- [`lessons-assemble-in-the-page.md`](lessons-assemble-in-the-page.md) — the embed that makes "show it running" cheap
- [`curriculum-structure.md`](curriculum-structure.md) — one concept per unit, no fixed unit counts
