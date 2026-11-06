# Plan: a content factory with many entry points

6 November 2026. A proposal for review. Decisions Steve has made are marked **agreed** with their date.

## Bottom line

Code198x already does most of its work as a series of agent-run stations with human review: Vault batches, game productions, the books' listing harness. This plan joins them into one factory that can be entered from any subject: a Vault candidate, a system, a person, a game, a demo, a technique or a Craft topic. Work on one subject finds and queues the next. Steve approves briefs and finished work; agents do the rest; the family's tools are the gates.

The scarce input is Steve's judgement, not production. The factory spends it on choosing what to make and on taste, and on nothing a check can do instead.

The curriculum is the main product. It is the factory's strongest source of demand (what lessons need) and its strictest gate (what learners can follow), not only where other work ends up.

## What already exists

| Part | Where | Role in the factory |
|---|---|---|
| Vault | website `src/content/vault/`: 1,621 entries, 23 categories including `demos`, `groups`, `events` and `techniques`; `ai_generated` and `reviewed` on every entry | The largest surface; its links are the graph readers see |
| Vault frontier | `vault-candidates.csv` (IDs, status, why, `link_from`, triage notes, `covered_by`, writing issue) and `vault-candidates.md`. About 3,200 rows, almost all `needs-triage` | The Vault's work queue, with an admission rule: "A candidate earns an entry by helping a reader of an existing entry or lesson, not by being mentioned." |
| Vault gates | website `scripts/check-vault-{links,sources,dates,frontmatter-vs-prose,imagery,platform-balance}.mjs`, `find-vault-duplicates.mjs`, `vault-candidates.mjs` | Machine checks for the Vault line |
| Systems | website `src/content/systems/`: 162 files. `tier` is the single source of truth for curriculum readiness (4 `live`, 6 `next`, 124 `planned`, 13 `edge`, 14 `beyond`). The `emu198x` and `devReady` flags record support surfaces, and `npm run surfaces:gaps` lists what's missing | The system-led entry point |
| Knowledge graph | `ops/scripts/knowledge.py` over `reference/_tools/facts.sqlite`: entities, aliases, releases and edges with evidence | Finds neighbours (people, companies, releases) from primary sources |
| Production workflow | `specifications/content-creation-workflow.md`; website per-game review checks; `scripts/check-release.sh`; the `Emulator` component | The production line's stations, written for people |
| Book tools | `code198x/books` `tools/check-listings.rb`, `tools/capture-screens.rb` | Assemble, run and capture listings headless, with byte-identical captures |
| Tools | Emu198x (33 machine runtimes, headless and scripted), Asm198x, Isa198x, Build198x, Format198x | Gates that run the code, and where blocked work sends its demand |
| Tool workflows | umbrella `docs/workflows/add-a-new-system.md`, `add-an-emulator-core.md`, `add-a-new-cpu.md`, `add-build-format-support.md`, `add-curriculum-support.md` | How a tool gains the support that blocked work asks for |
| AI disclosure | website `src/pages/ai.astro`, *How 198x uses AI* | Says AI writes almost all first drafts and Steve reviews through pull requests before publication |

## The model: one graph, several lines

**Subjects** are the things the site covers: systems, people, companies, groups, games, demos, techniques, hardware, events, magazines, and Craft topics such as paper prototyping, maths for games, game design and the economics of computers and games.

**Surfaces** are the places a subject can appear: a Vault entry, a system page, a production (game, demo or tool) in a track, a pattern, a From the Metal article, a Craft lesson, a Field Note, and later a book chapter.

**How the curriculum is built.** A system can have several **tracks**: one per language (`basic`, `assembly`, `amos`, `blitz`), plus a `machine` track, the briefing every language track on that system assumes. Today the Spectrum has three, the Amiga three, the C64 two and the NES one. Foundations and The Craft are **sections**, not tracks. A track is a sequence of **modules**, and a module may teach concepts, build a production or revisit one (`kind: teaching`, `game` or `interval`). A track holds many **productions**, each a full game, a full demo or a finished tool, and one production can be built across several modules, each a numbered pass that revisits and extends it. **Units** are the lessons inside a module.

A run starts at one subject, on any surface, and makes three kinds of move:

1. **Fill.** Give the subject a surface it lacks: a Vault entry for a candidate, a pattern for a technique, a fuller profile for a system.
2. **Link.** Connect existing work: add the reciprocal links a candidate names, and link Vault entries and curriculum both ways.
3. **Spawn.** Record new subjects found along the way as candidates, in the queue for their surface (see step 2). A run **records** spawns; it never fills them in the same run.
4. **Block.** When a tool can't do what the work needs (the emulator lacks a machine or mis-times an effect, the assembler lacks a CPU or dialect, the build tools lack a media format), the run stops that item and records the blocker as a request to the tool. It never fakes a result or quietly drops the item. See "When the tools can't do it yet".

Each surface has its own **line**: stations and gates suited to its cost.

| Line | Stations | Human gate |
|---|---|---|
| Vault entry | triage → sources → write → link → check | Batch review in Steve's own time (`reviewed: true`) |
| System profile | capability (what the machine can do, from `reference/`, Isa198x and Emu198x support) → historical use (what it was used for, from the knowledge graph and Cat198x) → curriculum hooks | Batch review |
| Explainer (From the Metal, pattern) | question → sourced explanation → runnable example → links | Batch review |
| Track | propose one track's sequence of modules: which productions (games, demos, tools), in what order, which genres, demo formats or kinds of tool, and the capstone, with evidence of what the track already teaches. Then check it against the system's other tracks: distinct productions, independent entry points, and the shared `machine` briefing | **Steve agrees the sequence** |
| Production (game, demo or tool) | brief → finished endpoint → runnable stages → modules and units → fan-out → review → publish | **Approve the brief**, then **play, watch or use the finished production** |
| Progression (Craft, Foundations, recurring threads) | question → prototype or playground → sequence of lessons with exercises → links | **Steve approves the prototype**, then tests the sequence |
| Link pass | find mentions that should link → add links → check | None beyond the checks |

The cost decides the gate. Cheap work flows and is reviewed in batches. A production or a new track needs its brief agreed first, as this repository's `AGENTS.md` already requires for new lineups ("New lineups require agreement before bulk lesson development").

## Entry points

**Lesson-led.** Start from a lesson and fill what it needs: the pages it links to for depth, the explanation and exercise gaps the audits record against it, and the patterns its techniques deserve. See "The curriculum at the centre".

**Vault-led.** A candidate becomes an entry. The run adds the links named in its `link_from`, records new candidates it meets, and proposes curriculum hooks. A person leads to the systems they worked on and the games they made; a game leads to its techniques; a technique leads to a pattern, a From the Metal article or a production that needs it.

**System-led.** Pick one of the 162 systems and deepen its coverage: a sourced Vault entry and a system profile covering what the machine can do and what it was used for. Name its support surfaces precisely (Emu198x, Asm198x, curriculum). Then propose curriculum hooks: Craft lessons and From the Metal articles it can illustrate and, where there's a concrete teaching purpose, a production brief. Depth is not readiness: the factory never changes a system's `tier` (see step 8). "Wider systems enter through a concrete teaching purpose" (`PROJECT.md`) still decides whether a system gets a track. A thin system can feed Craft examples and From the Metal articles without one; a track comes only through the Track line, after Steve moves the system's tier.

**Subject-led.** Start from a Craft topic, for example the economics of budget software. Find its historical anchors in the Vault, link both ways, and propose a production that shows it in play.

**Production-led.** Start from an agreed brief, as `content-creation-workflow.md` already describes, and fan the production's evidence out to From the Metal, the Vault, Field Notes and patterns.

## The curriculum at the centre

**Demand.** Lessons already say what they need:

- `specifications/unit.md` has a lesson explain what it uses "with optional links for depth". A wanted link to a page that doesn't exist, or to an unreviewed Vault entry, becomes a candidate.
- `specifications/recurring-progressions.md` audits the four tracks for explanation gaps, exercise gaps and topic gaps. Each gap becomes a row in `content-candidates.csv`, citing the lesson it came from.
- `specifications/craft-coverage.md` lists planned Craft sequences; each becomes a candidate for the Progression line.

A page wanted by a lesson counts for more than one wanted by a Vault entry, so the Vault grows towards what learners need.

**Gates.** The curriculum specifications already set most of them:

- **Machine checks.** Every checkpoint builds and runs. BASIC listings survive Build198x's round trip and match the machine's `LIST`. Build198x's BASIC lint rejects Spectrum keywords used as variable names. Required links resolve, and proposed pages aren't presented as available (`unit.md`). A course's final source matches its accepted endpoint.
- **Reviewer checks, with Steve's sign-off.** One new idea per unit where it can be done, and programs contain only code that has been taught. Agents flag problems against these; they don't decide them.
- **People (agreed 6 November 2026).** Steve is the primary tester: he plays every game, watches every demo and works through new sequences before they publish, as `content-creation-workflow.md` requires. Trials with other learners, such as the trial pack the Foundations and Spectrum pilot is building, are used where practical, not required. The factory's job is to make Steve's testing and any learner trial cheap to run (ready-to-load builds, the expected result for each stage, a record of what he found), never to replace it.

## When the tools can't do it yet

If something can't be made to work today, the factory works out what would make it possible tomorrow. Blocked work is a signal of what the tools should do next.

- **Record the blocker.** The blocked item stays in its queue with status `blocked` and a link to an issue in the tool's own repository (emu198x, asm198x, isa198x, build198x, format198x and so on). The issue states the symptom, not a guessed mechanism. It includes a repeatable case (the production record and its script, or the listing and its expected result) and lists the content waiting on it.
- **Rank tool work by what it unblocks.** A tool issue's priority is the number of queued items it blocks, counted the same way as content demand. The tools' own sessions get a list driven by what the site needs, not by guesswork.
- **Missing machines and CPUs count too.** When content wants a machine no tool supports (Emu198x has no IBM PC or Apple II, for example), the request follows the umbrella workflows for adding a system, an emulator core, a CPU or a build format, and names its support surface precisely.
- **Unblock automatically.** When a tool issue closes and a release ships, its blocked items go back to `open` and re-run their gates. A fix isn't trusted until the content that was waiting on it passes.
- **Content becomes test material.** A production's verify script, and especially a demo's per-model timing, goes into the tool's regression corpus (Emu198x's private fixture store, with provenance), so a later change can't silently break it.
- **The factory doesn't edit the tools.** Tool changes happen in the tool's own repository and session, under its own decisions and review. The factory supplies the demand, the repeatable cases and the re-check.

## Keeping it in bounds

- **Admission.** The Vault's rule applies to every surface: a subject earns work by helping a reader of something that already exists.
- **Priority by demand.** Rank candidates by how many existing pages would link to them (the length of `link_from`), weighting links from lessons above links from other pages, plus whether they connect to a live track or a system with tools. Demand comes from the site, not from the agent.
- **A budget per run.** At most two hops from the start; fill about one batch (around ten items); record every spawn but fill none.
- **No merging by guesswork.** The knowledge graph never auto-merges fuzzy identity matches (see `build_graph.py`). The factory follows the same rule: an uncertain identity goes to the queue as a question, not into an entry.
- **Everything is a pull request.** Work happens in worktrees and ends in a pull request. Nothing reaches the site without passing the gates and, for its line, a person.

## Steps

Each step ends in a commit and a check that can fail.

0. **Demos and tools in the charter (done).** Demos agreed with Steve and merged on 6 November 2026 (#282): a track step is a finished production, a full game or a full demo, and `PROJECT.md` now has a "What makes a finished demo" section. Finished tools followed the same day, with a "What makes a finished tool" section (#283, merged). Verify: the production line's demo and tool gates (step 9) quote those sections.

1. **Prove the gates can fail (done 6 November 2026; see `audit/2026-11-factory-gates/REPORT.md`).** Run each existing Vault and release check against a deliberate fault: a broken link, an unsourced claim, a frontmatter date that contradicts the prose, a duplicate. Verify: every check exits non-zero on its fault. List any that don't, and fix them before the factory relies on them.

2. **Two queues, linked by ID (agreed 6 November 2026; done, see `content-candidates.md`).** `vault-candidates.csv` stays exactly as it is: its columns (`link_from` and `covered_by` hold Vault paths) and statuses belong to the Vault's review process, and its 3,000 untriaged rows would bury other work. Everything else (patterns, From the Metal articles, Craft lessons, system profiles, production hooks) goes in a new `content-candidates.csv` with its own IDs (`CC-0001` onwards), the columns those surfaces need (surface, subject, why, target system and models where relevant, status, issue), and a `from` column that can cite a `VC-` or `CC-` ID. A spawn that crosses surfaces is recorded in the right queue and points back by ID. Verify: a check rejects a `from` value that names no existing ID, and fails on a planted bad reference; `vault-candidates.csv` is unchanged.

3. **Rank by demand, with lanes for world computing and early subjects (agreed 6 November 2026; see `vault-candidates.md`).** The ranking lives in the docs repository's `scripts/check_vault_candidates.py`, not the website script this step first named. Demand is plain: each lesson that wants a subject counts 3 (`lesson:` references in `link_from`), each existing Vault entry 1. A weighting towards the ten core curriculum machines was tried and dropped: it pushed regional and 1960s subjects back, and plain demand already leans that way because the Vault does. Instead a `scope` column records region and period at triage, and each batch takes at least a third of its subjects from the world and early lanes. Verify: a row with no referrers scores zero; a lesson outranks two entries; the lanes select only their scopes; weakening a weight or a lane makes the tests fail.

4. **Curriculum demand (agreed 6 November 2026; see `vault-candidates.md`).** Only 11 of 548 lessons linked to the Vault, and none could name a page that doesn't exist, so lessons now say what they want: a `wants` frontmatter field naming Vault candidates or entries still awaiting review. The Vault ranking reads wants from the website at ranking time (each wanting lesson counts 3), replacing step 3's stored `lesson:` references, so demand follows the lesson and nothing is deleted when a want goes. The website warns, not fails, when a wanted entry is already reviewed, so review batches aren't blocked; `--wanted-reviews` lists those for the link pass. craft-coverage.md's unauthored Game AI areas, Game Feel sequences and modules, and recurring-progressions.md's eight threads, are 24 progression candidates in content-candidates.csv. A model pass to propose wants for existing lessons was considered and skipped: only 33 of 548 lessons mention an open candidate by name, nearly all coincidences (the curriculum's own *Meteor Storm*, the phrase "game over"), so a pass would mostly invent connections. Authors add wants as they write, as `specifications/unit.md` now asks. Verify: a lesson's want raises its candidate's demand and removing it lowers it again with the backlog unchanged; a want for an unknown candidate fails; the review groups separate.

5. **Expansion step.** A script or agent that, given a subject, proposes neighbours from `knowledge.py`, existing Vault links and `reference/` indexes, and writes them to the right queue as candidates with evidence. It never creates entries. Verify: run it on three entries Steve knows well and compare against his expectations; `find-vault-duplicates.mjs` finds no new duplicates; one deliberately ambiguous name comes back as a question, not a merge.

6. **Blocked work becomes tool demand.** Add the `blocked` status and an issue link to both queues, a check that every blocked row links to an open or closed issue in a family tool repository, and a report that ranks tool issues by how many items each one blocks. When an issue closes and its fix is released, the blocked items return to `open` and re-run their gates. Verify: a planted blocked row with no issue link fails the check; closing a test issue moves its items back to `open`; a re-run that still fails puts them back to `blocked` with a note.

7. **The Vault line as a saved workflow.** Encode the existing batch process (as in `plans/2026-10-27-vault-continuation.md`) as a workflow that takes a list of candidate IDs and ends in a draft pull request with review notes. Verify: one batch runs end to end with all gates green, and a planted fault makes it stop.

8. **System depth, separate from tier (agreed 6 November 2026).** `tier` stays the single source of truth for curriculum readiness, and moving a system between tiers stays Steve's decision. The factory may propose a move with evidence, never make one. Depth is a third axis beside readiness and support surfaces, and it is **derived, not stored**, in the manner of `npm run surfaces:gaps`: for each system, report whether it has a Vault entry and whether that entry is reviewed, a capability profile, a historical-use section, and how many linked games, techniques and patterns it has. A missing item is a gap the factory can pick up. Define the profile's sections first, then pilot on one thin `planned` system that Emu198x already runs, such as the Oric Atmos, Jupiter Ace or Dragon. Verify: the depth report changes when the pilot's profile lands; every claim in the profile cites a source; every support surface it names is checked by running the tool; no `tier` value changes.

9. **The production line, piloted on the first Spectrum demo.** Add a production record (target models, stages, expected captures, play or run scripts), extending the website catalogues rather than inventing a format. Build one `verify` command that runs every gate and exits non-zero on any failure. For a demo, the key gate is that it runs to its end, with matching repeat runs, on every model it names. For a tool, it is a round trip: work saved by the tool reloads identically, and the tool survives a scripted run of mistakes without losing it. Verify: a deliberately mistimed effect fails on the model it breaks and passes on the others. Emulator gaps and bugs found here go through step 6.

10. **The explainer line.** Generate a From the Metal article from the pilot demo's evidence: one broken rule, traced across machines and decades, with a live figure. Verify: every fact cites a source; the figure runs in the page; the article links to the production and the production links back.

11. **One walk that exercises everything.** Start from a Spectrum multicolour candidate. No `techniques/` entry covers it yet; check for coverage under other names first. Fill the Vault entry, spawn its neighbours (the Pentagon, the Russian disk magazines, the groups that used the effect), link it to `techniques/raster-effects` and `techniques/attribute-aware-design` where the prose supports it, and connect it to the step 10 article and the step 9 demo. Verify: every surface the walk touches passes its gates, and both queues hold the spawns.

12. **Measure, then decide on scale.** Record how many minutes of Steve's time each item took, what the gates missed, and what reviewers changed. Verify: a review file with the numbers. Scale up only the lines whose gates caught what review would have caught.

## Disclosing AI (agreed 6 November 2026)

*How 198x uses AI* already covers authorship across the site. What a reader needs on an individual page is whether a person has checked its claims. So the rule is: **a surface carries `ai_generated` and `reviewed` if it can be published before a person has checked it.**

- **Vault entries:** yes, as now.
- **From the Metal articles and patterns:** yes, but only if the factory publishes them in batches ahead of review. If they publish only after review, they don't need the flags.
- **Lessons and productions:** no. They publish only after Steve's approval, so the flags would always read the same, and the AI page covers them.

Adding the flags to a collection that needs them is a schema change for that collection, made only when its line starts publishing ahead of review.

**Field Notes are written by Steve.** The publishing guide says first-person accounts "must reflect the author's actual experience". The factory can draft a Field Note from evidence, but Steve rewrites it in his own words, or it is published in the third person.

## Risks

- **Volume outruns review.** Cheap production makes admission and priority more important. If the review queue grows faster than Steve clears it, the factory slows down; it doesn't lower the bar.
- **Polished but empty prose.** The voice rules (plain, engaging, concrete, sourced, no invented names) must be checks or reviewer instructions, not hopes.
- **Single-source claims.** Find a second source or mark the claim single-sourced, as the Vault already does.
- **Demo parties.** Check a party's rules on AI-assisted work before entering anything.
- **Parallel agents.** Worktrees, unique temporary names, `cd` before `git`, staging by explicit path, and no `git stash`. The workflows must enforce these.
