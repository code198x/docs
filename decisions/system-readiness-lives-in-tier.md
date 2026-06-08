# Decision: System readiness lives in `tier`, not in parallel fields

> **STATUS: Accepted 2026-06-08.** A machine's readiness is **one field** — `tier`
> in its `website/src/content/systems/<slug>.yaml`. The fleet wall, the homepage
> feature band, the active-vs-coming-soon split, and landing-page routing all
> **derive** from `tier`. Set it there and nowhere else. This is the
> presentation-layer sibling of [state-lives-in-catalogues](state-lives-in-catalogues.md):
> state is data; query it where it lives, don't retype it.

## Why

On 2026-06-08, flipping the Commodore 64 and NES to live should have been a
one-line edit (`tier: next` → `tier: live`). It wasn't. The site read **three**
hand-maintained fields that all had to agree:

- `tier` (live/next/planned/edge/beyond) — drove the fleet wall.
- `status` (active/coming-soon) — drove routing and the active/coming-soon helpers.
- `curriculumStatus` (free text like "Game 1 Phase 2 live") — drove **nothing**,
  rendered nowhere, and had gone stale on every machine.

Worse, the homepage band hard-coded *which* slugs were live in a parallel array.
So the `tier` flip updated the fleet wall but the homepage still said "next" — a
second copy of the truth, drifted. A redundant field is only ever as fresh as the
last person who remembered to update both, and a *wrong* readiness badge is worse
than none.

## The rule

- **Authoritative for readiness:** the `tier` field, full stop. `tier` is required.
- **Everything else derives:**
  - *active vs coming-soon* → `isActivePlatform()` in `lib/platforms.ts`
    (`tier ∈ {live, next}`). There is no `status` field.
  - *fleet wall badge / column* → `tier` directly.
  - *homepage feature band* → membership and badge from `tier`; **order by how
    much curriculum each machine has** (complete modules, counted from the
    catalogues — see [state-lives-in-catalogues](state-lives-in-catalogues.md)),
    so the machine with the most content leads, on merit, not a hand-kept list.
  - *landing-page routing* → `[platform].astro` renders the generic template for
    everything `!isActivePlatform()`; live/next machines have bespoke page trees.
- **Removed for good:** `status`, `curriculumStatus`, `recommendationTag` — gone
  from the schema and all 67 system files. If a human-readable progress line is
  ever wanted, *derive* it from the module catalogues; if an editorial
  recommendation badge is ever wanted, add a field the day a component renders it.

## Drift triggers

Stop and re-read this decision if you find yourself about to:

- add a `status`-like field to the systems schema, or any second field that
  encodes "is this machine ready / live / active";
- write a hard-coded list of slugs in a component to mean "the live ones" / "the
  featured ones" (e.g. `const liveSlugs = [...]`) — derive from `tier` instead;
- hand-type a per-system "Phase N live" / "Volume 1 done" string — that's a mirror
  of the catalogues and will rot;
- make "going live" require editing more than the single `tier` line.

## Done 2026-06-08

Consolidated onto `tier` (website commit "Make C64 and NES live; derive system
readiness from tier alone"): `status`/`curriculumStatus`/`recommendationTag`
removed across the schema + 67 files; `isActivePlatform()` added; the homepage
band rederived from `tier` + content. Going live is now one line in one file.
