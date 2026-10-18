# Spacewar! whole-game study pilot

**Status: draft for owner review, 18 October 2026.** Site placement, navigation and publication remain undecided. This is authoring work under [the charter](../../PROJECT.md), not a new module, public route, lesson prerequisite or claim of PDP-1 support. A paired draft website change supplies the unpublished visual preview and two supporting Vault drafts; nothing is merged or deployed.

Read [the study](study.md) first. [Evidence](evidence.md) identifies sources, claim limits and outstanding work. [Observations](observations.json) records the selected browser implementation and bounded execution checks. [Connections](connections.md) separates existing destinations from gaps and gives placement options. The [plan](../../plans/2026-10-18-spacewar-study-pilot.md) records the task boundary.

## Agreed direction

Study the whole game: play, design, technology, creative practice, people, circumstances, production, release/distribution and reception. Let the material establish which relationships matter. The first four agreed subjects are Spacewar!, Wanted: Monty Mole, Elite and Lemmings. These are not four assigned design lessons, a compulsory chronological course or a commitment to finish a dozen studies. Rachel remains outside this tranche. Unsuccessful or overlooked games can earn later studies through what they reveal.

The draft's reference is the module labelled Spacewar! 3.1, 24 Sep 62, in Norbert Landsteiner's browser emulator. The module and engine response hashes are recorded. The embedded tape has now been compared byte for byte with the matching member in the Steve Russell archive; captures/tape-identity.json records the identity. Contemporary descriptions and later versions are identified separately. No original-hardware verification, two-human-player session, timing calibration or accessibility trial is claimed.

## What this pass delivers

- A revised, reader-facing narrative covering the experience and the circumstances that made it possible, with source markers and a compact reading list. Research methods and review limits stay in the accompanying notes.
- Period technical and reception evidence, attributed later recollections, and explicitly bounded design interpretation.
- The original five short browser observations, plus a complete scripted encounter with destruction, inactive state and restart; three self-captured display frames, source-response identities and a repeatable capture script.
- Links to existing Maths, Game Feel and Vault material, plus two written companion drafts: [shooting from a moving ship](companions/shooting-from-a-moving-ship.md) and [designing a duel](companions/designing-a-duel.md). These are draft explanations, not newly published lessons.
- Three placement options to evaluate against the actual draft.

## Repeating the bounded browser observations

Use an existing website checkout with its supported Node environment, installed `@playwright/test` and Chromium browser. From this documentation repository:

```sh
node studies/spacewar/observe.mjs --website ../website --output-dir /tmp/spacewar-review
```

The explicit output directory receives captures and `observations-raw.json`. Review the captures before adding qualitative conclusions. The script checks edition identity, non-empty executed memory changes, browser errors and actual script-response hashes; it does not automatically verify game physics or player experience. It closes every browser on completion or failure. Its raw output is not an automatic replacement for the reviewed observation record in this folder.

The complete-round capture can be reproduced with capture-encounter.mjs; see [capture instructions and credits](captures/README.md).

## Inspirations and related coverage

The [whole-game study specification](../../specifications/game-studies.md) records the agreed approach for future studies. The [Vault disposition audit](vault-audit.md) checks named people, institutions and cultural works against existing articles, candidates and issues. It points to the single candidate CSV rather than commissioning a biography for every mention.

The pilot also follows particular lives, resources and routes of exchange: Russell's recollected railway/electronics and theatre interests, Japanese films watched in Boston, the club's controller materials and the different social setting of later Stanford play. These are bounded examples, not a survey of national computing cultures. The standing specification covers how later studies should investigate regional differences and changing people without flattening either.

## Before publication

A human should review the draft and source interpretations, including the disagreements and unknowns in evidence.md. Conduct a two-player reading/play session on the named setup, and refine the activity instructions from what happens. Review the selected screenshots and original diagrams, including their credits, captions and text alternatives. Then agree placement and check the rendered website page, links, keyboard use, narrow screens and source presentation. Do not set a reviewed flag or claim those checks have happened on the strength of this draft.

The study includes four original explanatory diagrams and three self-captured game-display PNGs. The diagrams illustrate concepts; they are not captured game frames or a reconstruction of the PDP-1 implementation. [Capture credits, purpose and conditions](captures/README.md) distinguish the game imagery from our own prose and diagrams. No third-party photograph, borrowed screenshot, source file, game binary, audio or video is bundled.

Interactive examples are deliberately deferred at the owner's request. This revision contains static images, explanations and worked calculations. It neither implements a simulator nor commits a later interactive feature to the delivery queue.

## Editorial website prototype

A separate draft website change develops opt-in article openings, integrated breadcrumbs, wider/captioned figures and pull quotes. Its development-only catalogue preview records the canonical documentation revision; use its sync script after text revisions rather than maintaining two independent essays. This study's publication home remains open. Header illustration is contemporary editorial artwork, while the existing game frames remain unchanged, credited captures.

## Home versions and onward routes

The broad input-method survey has become onward links; original controller history and the thrust-response explanation remain in the study. A short home-computer passage links to draft Vault entries for Budge's Apple II Space War and Star Control, with the latter's arcade intermediary named. Their detailed treatment belongs in those entries. Publication of the study depends on its linked destinations being present in the same release.

One or more original Spacewar-inspired curriculum games are a proposal in work.md, without assigned systems, development work or a delivery commitment. The game-study specification distinguishes selective examples and fuller games, with original implementation/presentation and reuse/naming checks.
