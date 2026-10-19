# Carry the game studies into The Craft and the Pattern Library

Proposal for review, 19 October 2026. Agreed study order: M.U.L.E. observation pass, Pac-Man, SimCity. This does not implement a new navigation, content schema or module.

## What the current site already gives us

The charter and `specifications/craft-coverage.md` already separate seven Craft responsibilities. Game Feel has four controls-and-response lessons; Maths for Games has probability and aiming sequences. Game Design, Game AI and Game Data and Algorithms are agreed homes, not completed courses. More historical subjects do not require more top-level sections.

Website checkout `7412570891a79c0485b3d894cefd4cf74eb924eb` contains 71 pattern files: 27 rendering, 16 audio, 15 framework, seven physics and six input. Fourteen are cross-platform; the other 57 belong to four machines. The schema permits AI, but this inventory has no AI entries. These are file counts, not claims that all examples are executed or independently validated.

`src/content.config.ts` fixes five platform values and six categories. `PatternDirectory.astro` searches titles, summaries, tags, platform names and BASIC/assembly inferred from the path. It filters by machine, subject and difficulty. This is a useful existing directory; a design question, a verified implementation and a game study currently have no explicit shared identity.

The state-machine pattern already discusses transitions, priority and input edges. Escalation as Data already represents difficulty settings as a table. Extend or improve these before creating nearly identical pages. Its opening claim that a game without a difficulty curve is merely a demo also needs revisiting: the charter explicitly allows creative and puzzle games without obligatory failure or escalation. That is an editorial gap, not a reason to add another pattern.

## Questions earned by the studies

| Study | Reader's question | Craft home | Adaptable technique, if developed | Evidence boundary |
| --- | --- | --- | --- | --- |
| Spacewar! | Why does releasing thrust leave us moving? | Maths for Games; Game Feel | Velocity integration and a deliberate update order | Explain an approximation; do not call it a full orbital model |
| Adventure | How can a short command name something in a world? | Game Data and Algorithms; Game Design | Tokenisation, object lookup, command dispatch and world-state predicates | Distinguish original parser behavior from a new teaching parser |
| Monty Mole | What makes an obstacle readable and a route worth attempting? | Game Design; Game Feel | Collision classification, checkpoints and explicit action states | Ground cultural context in sources; do not infer a designer's motive from a level |
| Elite | How can a small machine suggest a huge world? | Game Data and Algorithms; Graphics and Animation | Seeded generation, compact representations and projection | Separate inspected algorithms from the impression made on the player |
| Manic Miner | How can one screen teach a route without explaining it in words? | Game Design; Game Feel | Predictable obstacle cycles and collision rules | Teach legibility and retry costs as well as timing |
| Lemmings | What does the player control when the characters act for themselves? | Game AI; Game Design | Per-entity states, assignment of an action and bounded resource counts | Do not imply the original uses a modern generic AI framework |
| Boulder Dash | What changes when removing a tile also removes support? | Game Data and Algorithms; Game Design | Grid updates, support tests and explicit scheduling | Traversal order can change results; demonstrate alternatives |
| M.U.L.E. | Why can an individual bargain be bad for the whole colony? | Game Design | Resource accounting, staged production and matched offers | Original rules and our interpretation are distinct; a diagram is not a play observation |
| Pac-Man (next) | How can a few opponent rules create different pressures? | Game AI; Game Feel | Target selection, legal turns, tie-breaking and timed modes | Preserve original implementation quirks; avoid invented ghost personalities as explanations |
| SimCity (afterwards) | How does the player reason about consequences that arrive later? | Game Design; Game Data and Algorithms | Tick scheduling, spatial summaries and visible feedback | Identify edition; do not universalise its chosen social/economic model |

Production, marketing, packaging, audience and cultural reception belong in the whole-game account and related Vault subjects. They can support practical Craft work when a reader has a concrete decision to make. They should not be squeezed into an implementation-pattern category just to connect everything.

## First Craft increment to propose after the observations

A small Game Design opening: **What makes this a choice?** Start with a colony that can afford one food installation or one energy installation. Show what each supports and what is sacrificed. Let a reader predict a consequence, trace one clearly labelled invented round, and change one rule. Bring in M.U.L.E. as a historical example after the choice is understood. No dependence on playing or completing the study; no claim to reproduce the complete M.U.L.E. economy.

A subsequent AI opening can use a small maze to compare direct pursuit with aiming ahead. That is an original experiment motivated by the Pac-Man study, not a copied level or a purported faithful reimplementation. Hold implementation until the study and lesson design have been reviewed.

## Pattern Library: three possible scales

1. Add categories and tags to the present machine-first structure. Cheap and compatible, but it still duplicates a technique when several machines or languages implement it. Appropriate for a modest immediate expansion.
2. Give a reusable technique one conceptual identity with linked implementations and examples. Keep the existing machine pages and URLs, add problem-led discovery, and distinguish pseudocode, executable samples and evidence. Recommended direction to prototype: it answers both “how do I do this?” and “how does my machine do it?” without stripping out constraints.
3. Build a general relationship graph across all content and make it the primary navigation. Broader reach, but higher authoring/migration cost and an unproven reader benefit. A graph can support search later; it is not an agreed architecture.

Do not combine every concern into one all-purpose pattern record. A design principle, an algorithm, a hardware routine, a worked example and a historical account have different jobs. Link them with a specific purpose rather than writing the same explanation five times.

## Prototype questions and migration constraints

- Can a beginner find “make an enemy seem to anticipate me” without knowing a machine, algorithm name or category?
- Can a C64 reader still go straight to a verified, adaptable C64 implementation?
- Can one technique link to several implementations without implying identical behaviour or hardware costs?
- Can a reader see whether code is pseudocode, built, executed or validated against a named outcome?
- Do existing URLs and incoming links continue to resolve, with explicit redirects if a move is eventually approved?
- Can the catalogue add another machine and language without unrelated schema edits and implicit path guessing?

Audit existing pattern content and link integrity before changing the model. Prototype with the existing state machine, input-edge detection and two grounded study examples; avoid a bulk rewrite. Compare task completion on narrow and wide screens, keyboard navigation, search without JavaScript, and the migration of existing relation fields. Choose the smallest change that demonstrates a reader benefit.

## Proposed delivery order

Finish the M.U.L.E. observation increment. Develop Pac-Man, then SimCity, as separate reviewed study changes. Keep updating this evidence-led map. Propose the first Game Design lesson with concrete materials, and a separate small Pattern Library prototype, before any structural implementation. The scope and principles in PROJECT.md and the current specifications remain binding.

## Pac-Man and SimCity research: concrete next examples

Pac-Man now supplies sourced distinctions between a target, a legal local turn and a timed mode. A small AI explanation should let readers change one target while keeping movement rules fixed, then change the movement rule while keeping the target fixed. This avoids a “personality” label replacing the actual algorithm. Its original corner cases stay in the historical study; an original teaching experiment can choose simpler, explicit rules.

SimCity adds a separate Game Design question: **How can a player see a consequence that arrives later?** Begin with an invented little settlement and one delayed resource change. Let the reader compare the map, a warning and a time graph, predict an outcome, then change one condition. Distinguish an action cost, a recurring cost, stored resources and a rate. Do not present an invented teaching economy as the SimCity formula, or a game model as evidence for real planning policy.

For Pattern Library prototypes, these yield two bounded implementations after design approval: target selection plus legal-neighbour choice, and a scheduled update with history samples and an explicit feedback display. The explanatory lesson owns intent, the pattern owns adaptable mechanics, and the study owns historical evidence. A pattern should state its assumptions, update order, units, costs and verification; a new category does not supply those things by itself.

The existing escalation entry's implied compulsory curve remains an editorial question for review. SimCity makes the conflict with the charter's creative-game allowance concrete: a worthwhile session can end because a reader is pleased with a place, not because a difficulty curve reaches a losing state. No binding scope, pattern schema, navigation or published lesson is changed in this proposal.
