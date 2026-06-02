# Decision: Modules, not games

> **STATUS: Accepted and migrated, 2026-06-01.** The curriculum's unit of
> sequencing is the **module**, not the game. A *game* is a buildable artefact a module may teach;
> one game can be taught by several modules (revisits). This record defines the model.
> **The one-time migration was executed 2026-06-01** — website commits `8150b9c5` (Spectrum: drop
> `game-NN-`, namespace to platform/track/slug), `6360d667` (C64/Amiga/NES namespacing), `1652ba12`
> (rename the `games` collection to `modules`), `b884433b` (wire the Primer + Gloaming as the first
> assembly modules), `8a2aa18c` (redirect shipped URLs). No `game-NN-` prefixes remain; the catalogue
> is `modules/`; slugs are bare. It was carried out the **same day** the design was accepted, so the
> original "migration pending / nothing mechanical happens until approved" wording was never updated
> — **corrected 2026-06-02.** (The migration-plan detail below is preserved as the executed record.)

## The decision

The curriculum is an ordered sequence of **modules**. A module is a slot in the learning path with
its own identity. What a module *teaches* varies:

- a **game** module builds a playable artefact (Gloaming, Shadowkeep);
- a **teaching** module builds machine literacy with no game (the Primer, "Meet the Machine");
- an **interval** module steps out into academic depth between games
  (see [between-game-intervals.md](between-game-intervals.md) — intervals are simply a module kind).

Crucially, **a game is not a module** — it's the artefact a module teaches, and it can be taught by
**more than one module**. "Gloaming" the game may be taught first by the *Gloaming* module
(foundations) and revisited later by a *Smooth Motion* module (make the movement glide). Same game,
two modules, at two depths.

## The model

A **module** (the collection currently mis-named `games`):

```yaml
slug:    meet-the-machine     # URL-bearing identity. NO number baked in.
name:    "Meet the Machine"    # display name
kind:    teaching | game | interval
game:    gloaming              # (game modules only) the artefact taught; shared across revisits
pass:    1                     # (optional) which visit to that game — 1 = first, 2 = revisit…
order:   …                     # position in the sequence — array order in the YAML
status:  complete | in-progress | coming-soon
tagline, skills, phase?, thumbnail?
```

- **Order lives in the catalogue, not the slug.** Modules are an ordered list. Inserting one is
  inserting a row — it renames nothing.
- **Slugs are clean identities:** `meet-the-machine`, `gloaming`, `shadowkeep`, `smooth-motion`.
  No `game-NN-` prefix. The number that used to encode order is gone; order is data.
- **A game** is just the `game:` value shared by the modules that teach it. Its code samples and
  screenshots live per-module (each module's units own their files), because a revisit builds its
  own continuation.

URLs become `/{platform}/{track}/{module-slug}/unit-NN`, e.g.
`/sinclair-zx-spectrum/assembly/meet-the-machine/unit-01`,
`/sinclair-zx-spectrum/assembly/gloaming/unit-05`.

## Why — the powerful part: revisiting

Treating modules and games as distinct unlocks **revisiting a game at a higher level** — the spiral
model ([spiral-and-incremental.md](spiral-and-incremental.md)) applied at *game* scale:

- The learner deepens something **familiar** rather than starting cold each time. On the revisit the
  game is known; only the new technique is new — pure one-concept focus
  ([incremental-code-samples.md](incremental-code-samples.md)).
- It is **deprecation-pairs** ([deprecation-pairs.md](deprecation-pairs.md)) at game granularity:
  *"remember Gloaming's jerky cell-step? we revisit Gloaming and make it glide"* — the same game,
  upgraded, as the motivated payoff.
- Where a technique deepens a game we've *already built*, the gentle-ramp inserts (*Smooth Motion*,
  *Overlap*) can become **revisits of Gloaming** rather than throwaway new games — continuity, not churn.

**Revisiting is a tool for depth, not a mandate to shrink the curriculum.** Breadth stays primary:
covering the genres — maze, shooter, platformer, puzzle, beat-'em-up, racer, adventure — needs *many
distinct games*, because you cannot teach a shooter by revisiting a maze. The model serves both axes;
the next section is how you choose.

## Breadth and depth — new game, revisit, or mini-game collection

The curriculum covers genres broadly *and* deepens some games. Three module shapes, chosen by *what's
being taught*:

- **A new game** — when covering a **genre we haven't taught** (or a genuinely fresh take within one).
  Genre breadth is a primary goal, so *most* game modules are new games. A new genre always wants a
  new game.
- **A revisit** — when **returning to a game we've already built** earns the lesson continuity and
  payoff (the spiral / deprecation-pair move). A deliberate choice, used where familiarity carries
  its weight — not the default, and never a reason to fold one genre into another.
- **A mini-game collection** — a period-authentic conceit (compilation tapes, multi-event sports
  games like *Track & Field*): one module teaching several tiny games. It packs a few small mechanics
  or genres, but there's a ceiling — only so many genres fit one collection before it wants splitting
  into distinct game modules. (Mechanically still a `kind: game` module whose game is a collection; no
  new schema needed until it earns one.)

Rule of thumb: **new genre → new game; deeper technique on a game we built → revisit; a clutch of
small mechanics → a collection.**

## Tensions this resolves

This is why it's a keystone — it dissolves a stack of things we kept bumping into:

1. **The original Gloaming-vs-Shadowkeep clash.** Both wanted `game-01`. With numberless slugs they
   are simply `gloaming` and `shadowkeep`, ordered in the catalogue. The collision that started all
   this just vanishes.
2. **The Primer's placement.** Not "game 0" — it's the first *module*, `kind: teaching`.
3. **The catalogue-numbering cascade.** Inserting a module before Shadowkeep renames *nothing*
   (order is data, not slug). The deferred numbering decision evaporates.
4. **Between-game intervals.** A module `kind`, first-class, no special-casing.
5. **The stale-16 lineup vs the gentle-ramp lineup.** Reconciliation becomes *reorder the module
   list* — not 93 directory renames.
6. **Shadowkeep's arcs / "ships only its start in October".** Later arcs can be later *revisit
   modules* of the same game, sequenced where the ramp wants them.
7. **"Is it a game?" awkwardness** (Primer, intervals, the tiny game). Answered by `kind`.
8. **Number-in-slug fragility** — every renumber forcing a mass rename. Gone for good: slugs are
   stable identities, order is catalogue data.

## Migration plan (one-time; execute only after approval)

**Scope is the whole curriculum, in one pass.** The collection, schema, and routing are global, so the
migration spans all **7 platform/track combos** (Spectrum assembly + BASIC, C64 assembly + BASIC,
Amiga assembly + AMOS, NES assembly), **92 game modules**, **232 unit pages** — not Spectrum assembly
alone. BASIC needs no design change (its games are already a module sequence) but rides the same
rename; it is the only **shipped** track (8 complete Spectrum BASIC games, live landing), so its URLs
change and get redirects. One pass keeps the slug convention consistent everywhere and cuts once;
phasing was considered and rejected — site traffic is negligible so far, so the shipped-URL risk is
low and not worth a two-pass split.

From the survey: 7 catalogue YAMLs, 78 units YAMLs, 324 MDX `game:` fields, 338 files referencing
`game-NN-` slugs, ~93 module directories × 3 mirrors (curriculum, code-samples, images), plus
helpers/layouts/routing and published URLs. Sequenced so the build stays green:

1. **Name the slugs.** Map every existing `game-NN-slug` → bare `slug` across *all* platform/track
   combos (~92 modules) — mostly mechanical (strip the prefix), checking uniqueness *within* each
   platform+track and resolving any collisions. Record current order for each catalogue.
2. **Schema** (`content.config.ts`): `games` → `modules` (base `content/games` → `content/modules`);
   add `kind`, `game`, `pass`; `units` `gameSlug` → `moduleSlug`; unit-pages drop the `game:` number
   (module identity is derived from the path, per the existing computed-fields philosophy) — keep
   `unit:`.
3. **Move + rename directories** (`game-NN-slug` → `slug`) across curriculum, code-samples, images.
4. **Update references** (338 files): `CodeFromFile` srcs, image paths, internal links.
5. **Code**: `lib/games.ts` → `lib/modules.ts` (rename funcs/types); `lib/units.ts`
   (`gameSlug` → `moduleSlug`); `[...slug].astro` (module name from the catalogue, not slug-derived;
   `gameName` → `moduleName`); `GameLayout` → `ModuleLayout`; the track-overview page.
6. **Published URLs**: update the launch page, RSS, vault backlinks; add Astro **redirects** from the
   old `/{platform}/{track}/game-NN-slug/` URLs to the new ones — concentrated on the shipped Spectrum
   BASIC games. Redirects are cheap insurance here rather than critical: traffic to date is negligible,
   so a missed redirect is low-cost. Don't *gate* the migration on perfect redirect coverage; add them,
   prioritise the live BASIC URLs, move on.
7. **Build + verify** (`npm run build`, Pagefind) green before commit.
8. **Then, separately:** wire the Primer as the first module; reconcile the lineup to the gentle-ramp
   order (now just catalogue order); later, add revisit modules.

The migration is mechanical once the model is fixed — large but well-defined, and done once.

## Records to amend (after migration)

Done in the migration (commit `de59533`):

- `CLAUDE.md` — Content Collections + CodeFromFile sections restated around modules
  (collection `modules`, bare slugs, `module-pages`, `getModulesWithCounts`, uniform
  `{platform}/{track}/{slug}/` paths). ✓
- The deferred catalogue-numbering question — closed by this record. ✓

Done in the docs-refresh pass (commits `d2fe1fe`, this commit):

- `specifications/content-model.md` — hierarchy and collections restated around modules. ✓
- `specifications/unit.md` — current path + minimal frontmatter; computed fields documented. ✓
- `specifications/code-samples.md`, `information-architecture.md`,
  `content-creation-workflow.md` — uniform `{platform}/{track}/{slug}/` paths. ✓
- `decisions/system-url-structure.md` — contradiction resolved: bare module slugs,
  re-ordering is a data edit; track-in-URL unchanged. ✓
- `decisions/between-game-intervals.md` — module model supplies the mechanism (`kind:
  interval`) and closes its placement/numbering question; stays exploratory pending cadence. ✓
- `decisions/spectrum-assembly-gentle-ramp.md` — lineup reframed as a module sequence; tiny
  game named Gloaming; *Smooth Motion* / *Overlap* noted as candidate Gloaming revisits. ✓
- `decisions/curriculum-structure.md` — rewritten around the module spine, the technique
  budget, and no-fixed-unit-counts (the 4×256 / powers-of-2 model retired). ✓
- `specifications/curriculum.md` — checked; no module-structural staleness (only legitimate
  `/vault/games/` links). ✓

Still deferred — historical or low-traffic, no build impact:

- `design/synthesis/*.html` mockups — carry `game-NN-` URLs; refresh when reworked.
- `platforms/sinclair-zx-spectrum/games/shadowkeep/*`, `tracker/*` — platform content and
  live trackers; touch when next edited.
- `docs/log.md` and this record's migration plan — historical, left as written.

## Drift triggers

- Reaching for a number-in-slug again (`module-01-…`, `game-02-…`) — order is catalogue data; slugs
  are bare identities. If you're renumbering directories, stop.
- Treating a game and a module as 1:1 — a game can have several modules (revisits); a module may
  teach no game (teaching/interval).
- Collapsing distinct genres into revisits to shrink the game count — breadth across genres is a
  primary goal; a new genre always wants a new game. Revisit only when returning to a *specific game
  we built* earns continuity.
- Doing the migration piecemeal so the build goes red, or shipping a URL change without redirects.

## Status

Accepted and migrated 2026-06-01 (Pass 1 namespacing, Pass 2 collection rename, Pass 3 wiring +
redirects — all build-green; a docs-prose refresh is deferred, see "Records to amend"). Supersedes the deferred catalogue-numbering
discussion. Relates to [spiral-and-incremental.md](spiral-and-incremental.md),
[deprecation-pairs.md](deprecation-pairs.md), [between-game-intervals.md](between-game-intervals.md),
[incremental-code-samples.md](incremental-code-samples.md),
[spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md), and
[in-curriculum-wasm-playground.md](in-curriculum-wasm-playground.md) (CodeFromFile→playground holds,
now keyed by module).
