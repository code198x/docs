# Decision: Website information architecture

Vocabulary, URLs and where a system's readiness lives. One record, because all three answer the same question: what is the structure, and where is it stated once.

## "Systems", not "platforms"

The structural term across the site is **system**. That fixes the nav item ("Systems"), the fleet index URL (`/systems/`), the content-collection key, the directory name, and component names (`SystemCard`, `SystemMotif`, `SystemStripe`).

Editorial prose may use "platform" wherever it reads better. Only the structural vocabulary is fixed; sentences are free.

**Why.** In 1985 the playground question was "what system have you got?", and Crash reviewed systems — using the era's own word is free authenticity for a project whose premise is period accuracy. It also wears the whole fleet naturally: a Vectrex or a KIM-1 is a system, where calling it a platform sounds modern. And "platform" reads 2010s SaaS, which is the connotation a project at pains not to sound like a startup can do without.

The cost is that "platform" is marginally more familiar to a modern developer skimming. Prose may use it, so the cost is small.

## URLs

System at the root, track always explicit:

```
/{system-slug}/                                       system landing
/{system-slug}/{track-slug}/                          track overview
/{system-slug}/{track-slug}/{module-slug}/            module landing
/{system-slug}/{track-slug}/{module-slug}/unit-{NN}/  unit page
```

- **Track is in the URL on every system**, including single-track ones. A system that gains a second track later does not break the first's URLs, and the fleet stays consistent.
- **No `/curriculum/` or `/learn/` prefix.** `/{system}/` is the QR-code entry point printed on flyers and t-shirts.
- **`{module-slug}` is a bare identity** — no `game-NN-` prefix. Order is the module catalogue's array position, so renaming *and* re-ordering are free, and re-ordering needs no redirect.
- **Unit is `unit-{NN}`** — number only. Titles change; numbers are stable.

Shipped pre-module URLs keep working through redirects in `astro.config.mjs`.

## Readiness lives in `tier`

A machine's readiness is **one field**: `tier` in `website/src/content/systems/<slug>.yaml`. It is required, and everything else derives from it.

- *active vs coming-soon* → `isActivePlatform()` in `lib/platforms.ts` (`tier ∈ {live, next}`). There is no `status` field.
- *fleet wall badge and column* → `tier` directly.
- *homepage feature band* → membership and badge from `tier`; **ordered by how much curriculum each machine has**, counted from the catalogues, so the machine with the most content leads on merit rather than from a hand-kept list.
- *landing-page routing* → `[platform].astro` renders the generic template for everything `!isActivePlatform()`; live and next machines have bespoke page trees.

`status`, `curriculumStatus` and `recommendationTag` are gone from the schema and from all 67 system files. If a human-readable progress line is ever wanted, derive it from the module catalogues. If an editorial badge is ever wanted, add the field the day a component renders it.

**Why.** Flipping the C64 and NES to live should have been a one-line edit. It was not: the site read three hand-maintained fields that all had to agree, one of which rendered nowhere and had gone stale on every machine, while the homepage band hard-coded which slugs were live in a parallel array. A redundant field is only ever as fresh as the last person who remembered both, and a wrong readiness badge is worse than none.

This is the presentation-layer sibling of [state-lives-in-catalogues.md](state-lives-in-catalogues.md): state is data, queried where it lives, never retyped.

## Drift triggers

- Naming a nav item, URL segment, collection key or component "platform…", or putting the fleet at `/platforms/`.
- A unit or module URL without a `{track-slug}` segment.
- Re-introducing `/curriculum/`, `/learn/`, a `game-{NN}-` module prefix, or a descriptive slug on `unit-{NN}`.
- Treating slug position as the source of order — order is catalogue data.
- Adding a `status`-like field to the systems schema, or any second field encoding whether a machine is ready.
- A hard-coded list of slugs in a component meaning "the live ones" or "the featured ones".
- Hand-typing a per-system "Phase N live" string — a mirror of the catalogues, and it will rot.
- Making "going live" require editing more than the single `tier` line.

## Outstanding

The in-repo IA spec `specifications/information-architecture.md` is still v2.1 and uses `platform` and `/curriculum/{platform}/` throughout. This record is binding until that spec is brought into line with it.
