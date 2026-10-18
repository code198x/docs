# Spacewar! whole-game study pilot

**Status: draft for owner review, 18 October 2026.** Site placement, navigation and publication remain undecided. This is authoring work under [the charter](../../PROJECT.md), not a new module, public route, lesson prerequisite or claim of PDP-1 support. No website content is changed.

Read [the study](study.md) first. [Evidence](evidence.md) identifies sources, claim limits and outstanding work. [Observations](observations.json) records the selected browser implementation and bounded execution checks. [Connections](connections.md) separates existing destinations from gaps and gives placement options. The [plan](../../plans/2026-10-18-spacewar-study-pilot.md) records the task boundary.

## Agreed direction

Study the whole game: play, design, technology, creative practice, people, circumstances, production, release/distribution and reception. Let the material establish which relationships matter. The first four agreed subjects are Spacewar!, Wanted: Monty Mole, Elite and Lemmings. These are not four assigned design lessons, a compulsory chronological course or a commitment to finish a dozen studies. Rachel remains outside this tranche. Unsuccessful or overlooked games can earn later studies through what they reveal.

The draft's reference is the module labelled Spacewar! 3.1, 24 Sep 62, in Norbert Landsteiner's browser emulator. The module and engine response hashes are recorded. Independent comparison of the embedded tape with its upstream archival image remains outstanding. Contemporary descriptions and later versions are identified separately. No original-hardware verification, two-human-player session, timing calibration or accessibility trial is claimed.

## What this pass delivers

- A revised, reader-facing narrative covering the experience and the circumstances that made it possible, with source markers and a compact reading list. Research methods and review limits stay in the accompanying notes.
- Period technical and reception evidence, attributed later recollections, and explicitly bounded design interpretation.
- Five automated browser observations with the actual configuration and source-response identities; a repeatable observation script.
- Connections to existing Game Feel material and Vault coverage without inventing missing article destinations.
- Three placement options to evaluate against the actual draft.

## Repeating the bounded browser observations

Use an existing website checkout with its supported Node environment, installed `@playwright/test` and Chromium browser. From this documentation repository:

```sh
node studies/spacewar/observe.mjs --website ../website --output-dir /tmp/spacewar-review
```

The explicit output directory receives captures and `observations-raw.json`. Review the captures before adding qualitative conclusions. The script checks edition identity, non-empty executed memory changes, browser errors and actual script-response hashes; it does not automatically verify game physics or player experience. It closes every browser on completion or failure. Its raw output is not an automatic replacement for the reviewed observation record in this folder.

## Before publication

A human should review the draft and source interpretations, including the disagreements and unknowns in evidence.md. Confirm the reference image, conduct a two-player reading/play session on the named setup, and refine the activity instructions from what happens. Choose suitable imagery under existing capture/provenance rules, with credits and useful text explanations. Then agree placement and check the rendered website page, links, keyboard use, narrow screens and source presentation. Do not set a reviewed flag or claim those checks have happened on the strength of this draft.

The study includes four original explanatory diagrams, with text alternatives and a standard-library Python generator in figures/. They illustrate movement and the control-to-motion relationship; they are not captured game frames or a reconstruction of the PDP-1 implementation. No third-party photographs, screenshots, source files or game binaries are included. External articles, interviews and implementations are linked and attributed; they retain their own terms. Original draft prose follows the documentation repository's existing licence scope. Research notes record source roles, not a grant to reproduce their expression or media.
