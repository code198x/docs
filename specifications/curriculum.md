# Curriculum design

Apply [Project purpose and direction](../PROJECT.md). This specification assigns teaching responsibilities; it does not assert that every subject below has been written or commit to a new navigation structure.

## Shared subjects

### Foundations

Teach programming concepts in [pseudocode](pseudocode.md), supported by diagrams, trace tables and concrete examples. Distinguish understanding sequence, variables, decisions, repetition and decomposition from learning a language's syntax.

The rewritten material includes lists, named jobs and parameters, debugging, binary and hexadecimal, bit operations, floating- and fixed-point representation, truth tables, gates, and source-to-execution explanations. Use the actual lesson bodies to judge what they teach. Do not assume their existence makes them a prerequisite.

Basic collections and tracing belong here. Further data-structure and algorithm teaching should grow from game problems rather than enlarging the beginner on-ramp indefinitely.

### Maths for Games

Maths for Games currently sits within The Craft. Develop position, distance, direction, movement, probability and numerical representation through concrete game problems. Readers should be able to arrive when they need a tool, without completing a separate prerequisite course.

Explain the useful model before its optimisation. Fixed-point accumulators, lookup tables, root-free distance comparisons and approximation are applications, not the whole subject. Costs depend on language, CPU and workload. A direct pursuer is not an obstacle-solving pathfinder.

Foundations explains what a representation means; Maths for Games explains how it helps solve a game problem; system lessons implement it within a measured budget.

### The Craft

The Craft supplies developed, language-neutral explanations of game-making decisions. Paper, counters, diagrams and pseudocode can make an experiment concrete. Organise coherent sequences around questions, not a new top-level module for every item:

- Rules, state, goals, actions and consequences; decisions and trade-offs.
- The program loop (input, update, output) and the player's recurring activity (observe, decide, act, interpret feedback).
- Space, movement, collision and boundaries as design choices.
- Turn-based and real-time play; time, rhythm, pacing and pressure.
- Controls, responsiveness, forgiveness and game feel.
- Visual and audio feedback, readability and anticipation.
- Challenge, learning, difficulty, failure and retrying.
- Resources, scarcity, rewards and scoring.
- Opponents, interacting systems, uncertainty, predictability and fairness.
- Levels, encounters, progression, prototyping, playtesting and deliberate iteration.

A system lesson must still explain its immediate design decision. A link supplies depth or alternatives, not missing instructions.

### Game AI

Name the subject early: behaviour and decision-making for game entities. Machine learning is not a prerequisite.

Progress from patterns, patrols, pursuit, escape and reactions to states and transitions, perception, limited knowledge, memory, navigation, obstacle avoidance, pathfinding, priorities, weighted choices, controlled randomness and coordination.

The Craft explains behavioural intent and player experience. Maths supplies relevant tools; Foundations supplies programming concepts; system tracks build the behaviour. An opponent can be interesting because it warns, hesitates, makes mistakes or behaves predictably. Strongest possible play is not the universal goal.

### Data structures and algorithms

Give these deliberate coverage. Provisionally develop game-specific representation and algorithm work within The Craft, building on Foundations' lists and structure. Reassess that placement when a coherent sequence exists; a new top-level course is not yet settled.

Use enemies, bullets and pickups to compare arrays, records, collections, fixed pools and allocation. Use levels to compare grids, tile maps and sparse representations. Use nearby-object queries for searching and spatial partitioning; routes for graphs, queues, breadth-first search and later heuristics; events and undo for queues, stacks and histories; storage for encoding, compression and space–time trade-offs.

Start with what data represents and how much work an operation performs. Trace examples and count operations at different scales. Introduce complexity notation when it clarifies that experience. Compare plausible solutions and their costs on the relevant language and machine.

### Graphics, sound effects and music

Asset creation is taught, not merely supplied. [Graphics and audio](graphics-and-audio.md) covers creating assets, preparing them for a machine and integrating them into a game. Keep shared artistic principles connected to the target's actual facilities.

## Practices across the games

Plan recurring opportunities for:

- Debugging through reproduction, hypotheses, state inspection, tracing and reduced examples.
- Testing boundaries, unusual input, regressions and game-rule correctness.
- Decomposition, data representation and managing growing programs.
- Saving work, version control, source and asset organisation, reproducible builds and conversion.
- Instructions, controls, readable information, pause behaviour and alternatives to colour-only or sound-only cues.
- Scope, polish, credits, provenance, permissions, packaging, distribution and feedback.
- Multiplayer, beginning with shared-screen play where suitable.
- Narrative, dialogue, environmental storytelling and character expressed through behaviour.

These are coverage responsibilities, not a checklist every game or machine must exhaust.

## Guided development and multiple entry points

A module groups a coherent learning experience; it may teach concepts, build a game or revisit one. A unit develops a focused idea through meaningful, inspectable stages. Shared units may produce a trace, diagram or paper experiment; system-building units produce runnable results.

There are no universal unit durations, fixed code-diff limits or required counts. Keep changes small enough to explain, and split overloaded stages. A richer game can introduce several techniques across an understandable sequence.

For each arrival, state the knowledge used and explain enough to proceed. Within a game, continue from the preceding runnable state. Across games, show exactly which files and ideas are reused and where to obtain and understand them. Independent entry does not mean unexplained starter engines.

Teach a naive approach before an upgrade when experiencing its limitation makes the upgrade meaningful. Do not manufacture failure or repeat a detour solely to satisfy a formula. Restructuring can itself be a lesson when its purpose and effects are visible.

Offer optional experiments after guided work. Do not introduce pass/fail gates, hints-and-restores systems or gamification without an educational need. Production verification is separate from learner assessment.

## Checking understanding

Consider short quizzes and other checks within units and at useful points across a module. Their purpose is to let readers try an idea, explain their reasoning and recognise what needs another look. Choose the form and placement for that purpose; there is no required quiz count or end-of-unit template.

Mix prediction, tracing, explanation, diagnosis and small changes to a worked example. A question can revisit an earlier concept in a new game context without assuming the reader attended its original lesson. Supply enough context to attempt it and link to a fuller explanation where useful.

Multiple-choice questions can expose a specific misconception, but recognition alone is not the whole of understanding. Include opportunities to produce an answer, explain a choice or run an experiment. For design and asset questions, several answers may be defensible; discuss the trade-offs rather than inventing a single correct preference.

Keep feedback explanatory, available without penalty and useful to parents or teachers discussing the work. Readers can pause, retry or continue. Do not make progress depend on a score, add time pressure by default, or turn optional checks into a compulsory examination. See [Unit guidance](unit.md#questions-and-feedback) for authoring examples.

## Choosing system projects

Use [the game brief](brief.md) to compare appeal, teaching value and suitability. Retain, reshape or replace existing ideas on those grounds. Assembly is independent of BASIC; it need not port every BASIC game.

Choose projects that reveal each system's character. Compare language design, CPU architecture, memory, graphics, sound, input, storage, timing and bandwidth, and the circumstances behind those choices. Explain what transfers and what changes without assuming the Spectrum came first or portraying another machine as deficient.

State the target configuration and development workflow for every game. Read existing model and successor-machine decisions before changing scope. A modern host, emulator or transfer device does not silently change what a stock target can do.

## Connections

A useful link explains why to follow it: “The Foundations unit on binary numbers explores how these eight bits represent the row.” Avoid “you will remember”. Supply enough context locally to continue.

Lessons guide building; shared subjects develop concepts; the Vault gives fuller context; patterns make techniques reusable. Link in both directions where useful. Do not duplicate canonical explanations or turn the lesson into a list of compulsory excursions.
