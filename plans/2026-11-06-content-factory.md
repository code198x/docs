# Plan: a content factory with many entry points

6 November 2026. A proposal, not an adopted direction. Steps marked **(ask)** need Steve's decision first.

## Bottom line

Code198x already does most of its work as a series of agent-run stations with human review: Vault batches, game productions, the books' listing harness. This plan joins them into one factory that can be entered from any subject: a Vault candidate, a system, a person, a game, a demo, a technique or a Craft topic. Work on one subject finds and queues the next. Steve approves briefs and finished work; agents do the rest; the family's tools are the gates.

The scarce input is Steve's judgement, not production. The factory spends it on choosing what to make and on taste, and on nothing a check can do instead.

## What already exists

| Part | Where | Role in the factory |
|---|---|---|
| Vault | website `src/content/vault/`: 1,621 entries, 23 categories including `demos`, `groups`, `events` and `techniques`; `ai_generated` and `reviewed` on every entry | The largest surface; its links are the graph readers see |
| Vault frontier | `vault-candidates.csv` (IDs, status, why, `link_from`, triage notes, `covered_by`, writing issue) and `vault-candidates.md` | The work queue, with an admission rule: "A candidate earns an entry by helping a reader of an existing entry or lesson, not by being mentioned." |
| Vault gates | website `scripts/check-vault-{links,sources,dates,frontmatter-vs-prose,imagery,platform-balance}.mjs`, `find-vault-duplicates.mjs`, `vault-candidates.mjs` | Machine checks for the Vault line |
| Systems | website `src/content/systems/`: 162 files, with `tier` (`live`, `next`, `planned`, `edge`, `beyond`) and `devReady` | The system-led entry point |
| Knowledge graph | `ops/scripts/knowledge.py` over `reference/_tools/facts.sqlite`: entities, aliases, releases and edges with evidence | Finds neighbours (people, companies, releases) from primary sources |
| Production workflow | `specifications/content-creation-workflow.md`; website per-game review checks; `scripts/check-release.sh`; the `Emulator` component | The production line's stations, written for people |
| Book tools | `code198x/books` `tools/check-listings.rb`, `tools/capture-screens.rb` | Assemble, run and capture listings headless, with byte-identical captures |
| Tools | Emu198x (33 machine runtimes, headless and scripted), Asm198x, Isa198x, Build198x | Gates that run the code |

## The model: one graph, several lines

**Subjects** are the things the site covers: systems, people, companies, groups, games, demos, techniques, hardware, events, magazines, and Craft topics such as paper prototyping, maths for games, game design and the economics of computers and games.

**Surfaces** are the places a subject can appear: a Vault entry, a system page, a production (game or demo) in a track, a pattern, a From the Metal article, a Craft lesson, a Field Note, and later a book chapter.

A run starts at one subject, on any surface, and makes three kinds of move:

1. **Fill.** Give the subject a surface it lacks: a Vault entry for a candidate, a pattern for a technique, a fuller profile for a system.
2. **Link.** Connect existing work: add the reciprocal links a candidate names, and link Vault entries and curriculum both ways.
3. **Spawn.** Record new subjects found along the way as candidates. A run **records** spawns; it never fills them in the same run.

Each surface has its own **line**: stations and gates suited to its cost.

| Line | Stations | Human gate |
|---|---|---|
| Vault entry | triage → sources → write → link → check | Batch review in Steve's own time (`reviewed: true`) |
| System profile | capability (what the machine can do, from `reference/`, Isa198x and Emu198x support) → historical use (what it was used for, from the knowledge graph and Cat198x) → curriculum hooks | Batch review |
| Explainer (From the Metal, pattern, Craft lesson) | question → sourced explanation → runnable example → links | Batch review |
| Production (game or demo) | brief → finished endpoint → runnable stages → units → fan-out → review → publish | **Approve the brief**, then **play or watch the finished production** |
| Link pass | find mentions that should link → add links → check | None beyond the checks |

The cost decides the gate. Cheap work flows and is reviewed in batches. A production or a new track needs its brief agreed first, as this repository's `AGENTS.md` already requires for new lineups ("New lineups require agreement before bulk lesson development").

## Entry points

**Vault-led.** A candidate becomes an entry. The run adds the links named in its `link_from`, records new candidates it meets, and proposes curriculum hooks. A person leads to the systems they worked on and the games they made; a game leads to its techniques; a technique leads to a pattern, a From the Metal article or a production that needs it.

**System-led.** Pick one of the 162 systems. Give it a sourced Vault entry and a system profile covering what the machine can do and what it was used for. Name its support surfaces precisely (Emu198x, Asm198x, curriculum). Then propose curriculum hooks: Craft lessons and From the Metal articles it can illustrate and, where there's a concrete teaching purpose, a production brief. "Wider systems enter through a concrete teaching purpose" (`PROJECT.md`) still decides whether a system gets a track.

**Subject-led.** Start from a Craft topic, for example the economics of budget software. Find its historical anchors in the Vault, link both ways, and propose a production that shows it in play.

**Production-led.** Start from an agreed brief, as `content-creation-workflow.md` already describes, and fan the production's evidence out to From the Metal, the Vault, Field Notes and patterns.

## Keeping it in bounds

- **Admission.** The Vault's rule applies to every surface: a subject earns work by helping a reader of something that already exists.
- **Priority by demand.** Rank candidates by how many existing pages would link to them (the length of `link_from`), plus whether they connect to a live track or a system with tools. Demand comes from the site, not from the agent.
- **A budget per run.** At most two hops from the start; fill about one batch (around ten items); record every spawn but fill none.
- **No merging by guesswork.** The knowledge graph never auto-merges fuzzy identity matches (see `build_graph.py`). The factory follows the same rule: an uncertain identity goes to the frontier as a question, not into an entry.
- **Everything is a pull request.** Work happens in worktrees and ends in a pull request. Nothing reaches the site without passing the gates and, for its line, a person.

## Steps

Each step ends in a commit and a check that can fail.

0. **(ask) Demos in the charter.** Change "Each step is a full game, not a tech demo" in `PROJECT.md` to "a finished production: a full game or a full demo", and add a "What makes a finished demo" section. The wording was drafted in conversation on 6 November 2026. Verify: the production line's demo gate (step 7) quotes the new section.

1. **Prove the gates can fail.** Run each existing Vault and release check against a deliberate fault: a broken link, an unsourced claim, a frontmatter date that contradicts the prose, a duplicate. Verify: every check exits non-zero on its fault. List any that don't, and fix them before the factory relies on them.

2. **(ask) One frontier or several.** Add a `surface` column to `vault-candidates.csv`, so non-Vault work (patterns, explainers, system profiles, production hooks) joins the same queue with the same IDs and issues. The alternative is a sibling frontier file per surface. Recommendation: one file, because a spawn often crosses surfaces. Verify: existing rows keep their IDs and statuses; `vault-candidates.mjs` still runs.

3. **Rank by demand.** Extend `vault-candidates.mjs` to score open rows by `link_from` length and by connection to live tracks or systems with tools. Verify: hand-check that the top ten on current data deserve to be there, and that a row with no referring pages scores zero.

4. **Expansion step.** A script or agent that, given a subject, proposes neighbours from `knowledge.py`, existing Vault links and `reference/` indexes, and writes them to the frontier as candidates with evidence. It never creates entries. Verify: run it on three entries Steve knows well and compare against his expectations; `find-vault-duplicates.mjs` finds no new duplicates; one deliberately ambiguous name comes back as a question, not a merge.

5. **The Vault line as a saved workflow.** Encode the existing batch process (as in `plans/2026-10-27-vault-continuation.md`) as a workflow that takes a list of candidate IDs and ends in a draft pull request with review notes. Verify: one batch runs end to end with all gates green, and a planted fault makes it stop.

6. **(ask) System profiles.** Define what a system profile contains, and what evidence moves a system between the existing `tier` values. Read the current tier definitions before proposing anything. Pilot on one thin system that Emu198x already runs, such as the Oric Atmos, Jupiter Ace or Dragon. Verify: every claim in the profile cites a source, and every support surface it names is checked by running the tool.

7. **The production line, piloted on the first Spectrum demo.** Add a production record (target models, stages, expected captures, play or run scripts), extending the website catalogues rather than inventing a format. Build one `verify` command that runs every gate and exits non-zero on any failure. For a demo, the key gate is that it runs to its end, with matching repeat runs, on every model it names. Verify: a deliberately mistimed effect fails on the model it breaks and passes on the others. Emulator bugs found here become emu198x issues for the Emu198x session.

8. **The explainer line.** Generate a From the Metal article from the pilot demo's evidence: one broken rule, traced across machines and decades, with a live figure. Verify: every fact cites a source; the figure runs in the page; the article links to the production and the production links back.

9. **One walk that exercises everything.** Start from a Spectrum multicolour candidate. No `techniques/` entry covers it yet; check for coverage under other names first. Fill the Vault entry, spawn its neighbours (the Pentagon, the Russian disk magazines, the groups that used the effect), link it to `techniques/raster-effects` and `techniques/attribute-aware-design` where the prose supports it, and connect it to the step 8 article and the step 7 demo. Verify: every surface the walk touches passes its gates, and the frontier holds the spawns.

10. **Measure, then decide on scale.** Record how many minutes of Steve's time each item took, what the gates missed, and what reviewers changed. Verify: a short Field Note or review file with the numbers. Scale up only the lines whose gates caught what review would have caught.

## Risks

- **Volume outruns review.** Cheap production makes admission and priority more important. If the review queue grows faster than Steve clears it, the factory slows down; it doesn't lower the bar.
- **Polished but empty prose.** The voice rules (plain, engaging, concrete, sourced, no invented names) must be checks or reviewer instructions, not hopes.
- **Single-source claims.** Find a second source or mark the claim single-sourced, as the Vault already does.
- **Honesty about AI.** Every Vault entry already carries `ai_generated` and `reviewed`. **(ask)** Extending these flags to other surfaces (From the Metal, patterns, lessons) is a schema change.
- **Demo parties.** Check a party's rules on AI-assisted work before entering anything.
- **Parallel agents.** Worktrees, unique temporary names, `cd` before `git`, staging by explicit path, and no `git stash`. The workflows must enforce these.
