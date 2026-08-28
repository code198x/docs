# Decision-record triage

Working document. Delete it once executed — it is a worklist, not a record.

50 records, 4,832 lines. Proposed disposal below. Correct the buckets; the mechanical work follows from them.

## Delete — 4 records, 284 lines

| Record | Lines | Why |
|---|---|---|
| `cross-system-foundations.md` | 67 | Says SUPERSEDED on its face, 2026-06-05 |
| `number-systems-primer.md` | 69 | Says SUPERSEDED on its face, 2026-06-05 |
| `spectrum-basic-v6.4-renames.md` | 77 | A one-off rename pass. If the renames shipped, this is history |
| `regional-release-titles.md` | 71 | Draft awaiting your approval since 2026-08-08. Approve it or delete it |

Marking a record SUPERSEDED instead of deleting it is the habit under discussion. Git holds what it said.

## Fold — 10 records, 629 lines, into 4 homes

| Record | Lines | Folds into |
|---|---|---|
| `systems-not-platforms.md` | 52 | **one website/IA decision** |
| `system-url-structure.md` | 62 | " |
| `system-readiness-lives-in-tier.md` | 62 | " |
| `website-design-zoning.md` | 67 | " |
| `visual-direction-synthesis.md` | 117 | " |
| `british-english.md` | 15 | **a conventions record** — it is a line, not a decision |
| `seven-repos.md` | 23 | the repo map; it is a layout fact |
| `examples-as-files-and-screenshots.md` | 59 | `incremental-code-samples.md`, which it already says it builds on |
| `craft-and-pattern-library.md` | 105 | `pattern-library.md`, or delete if the migration finished |
| `phase-boundaries.md` | 67 | `curriculum-structure.md`, which it descends from |

Five website records with no status section between them become one. Three of the ten have no status section at all, which is usually the tell.

## Keep and rewrite — 21 records

Live rules. Rewritten to current truth, banners deleted, bodies made consistent with their own headers.

`real-retro-games.md` · `commercial-bar-revamp.md` · `curriculum-structure.md` · `deprecation-pairs.md` · `spiral-and-incremental.md` · `incremental-code-samples.md` · `incremental-construction-units.md` · `endpoint-first-authoring.md` · `constraint-position.md` · `inspired-by-not-clones-naming.md` · `a-game-needs-jeopardy.md` · `modules-not-games.md` · `pattern-library.md` · `state-lives-in-catalogues.md` · `built-artefacts-are-published-not-committed.md` · `satteri-markdown-processor.md` · `front-of-curriculum-architecture.md` · `foundations-numbers-and-bits.md` · `foundations-logic-and-gates.md` · `next-tier-first-wave.md` · `game-completeness-bar.md`

The worst accretion is here: `curriculum-structure.md` carries eight amendment markers and its drift triggers contradict its own opening banner; `commercial-bar-revamp.md` carries an ADDED block and a suspension note; `incremental-code-samples.md`, `inspired-by-not-clones-naming.md` and `pattern-library.md` each record an amendment date in their status line.

## Re-derive — 11 records, 1,595 lines

Every lineup and ladder is downstream of the game bar and of games-as-doors. Rewriting them before those settle wastes the work; keeping them as-is leaves eleven records describing a curriculum the project has stopped building.

`spectrum-assembly-gentle-ramp.md` (347) · `amiga-basic-amos-and-blitz.md` (374) · `shadowkeep-four-arc-framing.md` (142) · `shadowkeep-32-unit-commitment.md` (140) · `spectrum-basic-lineup.md` (137) · `amiga-assembly-lineup.md` (90) · `nes-primer-generalisation-probe.md` (87) · `amiga-assembly-primer.md` (82) · `c64-basic-volumes-2-4.md` (75) · `c64-assembly-lineup.md` (72) · `nes-assembly-lineup.md` (69)

Hold until the bar and the door rule are settled, then rewrite or delete as one pass. Expect most to shrink and some to disappear — the lineups exist to order games that no longer need ordering.

## Hold — 4 records

| Record | Lines | Until |
|---|---|---|
| `october-2026-launch-spec.md` | 153 | After CRASH! Live, then delete — it is a plan with an expiry date |
| `between-game-intervals.md` | 78 | Marked exploratory. Promote or delete; a door held open for three months is a decision not taken |
| `in-curriculum-wasm-playground.md` | 69 | Same |
| `visual-enhancement-pass.md` | 435 | The largest record in the folder and it is a work item, not a decision. Belongs in `tracker/` or is finished |

## Where it lands

| Bucket | Records | Lines |
|---|---|---|
| Delete | 4 | 284 |
| Fold | 10 | 629 → 4 homes |
| Keep and rewrite | 21 | — |
| Re-derive | 11 | 1,595 |
| Hold | 4 | 735 |

50 records become roughly 26 once folding and deletion are done, before the re-derive pass shrinks the lineups further.

## What stops it coming back

Add `AMENDED`, `SUPERSEDED`, `ADDED 20`, `now dropped` and `no longer` to the stale-phrase patterns in `check-agent-context.py`. A rule that only lives in a document is a rule that gets amended by banner; one that fails a check does not.
