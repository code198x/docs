# Game brief

A brief is the reviewable specification for a guided game project on any system or language track, including BASIC. Apply [the charter](../PROJECT.md) and [curriculum design](curriculum.md). Historical ancestors and commercial comparisons are optional evidence, not admission requirements.

Store a brief at `platforms/<system>/games/<slug>/brief.md`. Use a stable identity rather than a numbered game slot. Record **status** (proposal, agreed specification, or existing design pending reconciliation), target configuration, language, and the source/catalogue locations used to establish implementation state.

## Experience and scope

Describe the central mechanic, the player's recurring activity, decisions and feedback. Explain why it is enjoyable to build and play, why it suits the target and language, and what makes the finished project complete. Name content scale, ending or repeatable cycle, and intended session length where useful. Choose failure and retry behaviour for this game rather than requiring a losing state. Explain how consequences, feedback and progress support its intended experience, including recovery where relevant. Identify deliberate exclusions and design risks.

A small BASIC game need not be commercially saleable. Selected ambitious projects may state a higher target. Scope must justify itself through experience and teaching rather than feature parity with another game.

## Learning and connections

State what the project introduces, reinforces and briefly recalls across programming, maths, game design, assets and hardware. Identify knowledge used without requiring attendance at particular lessons. Explain how a reader arriving from elsewhere can understand the starting point.

Connect to Foundations, Maths for Games, The Craft, existing patterns and Vault entries selectively. Record missing entries as authoring work; do not link to pages that do not exist. Explain the relationship to preceding, following or revisited games and useful contrasts with other systems.

## Target and tools

Separate the development host and tools from required runtime hardware. Name model, memory, display standard, input, storage and any peripheral or expansion. For an extension, state what it provides, how the original machine communicates with it, which constraint changes and which bottleneck remains.

Specify source organisation, assembler or language environment, asset converters, built output, emulator or hardware checks, and transfer or loading method. Verify tool access before promising execution. Identify build-time work versus runtime work. Explain cross-development explicitly.

## Graphics, sound and content

Describe what the learner creates, how it is represented and prepared, and why it supports play. Cover readability, animation timing, sound design, composition or arrangement as appropriate. State palette, storage, channel and timing budgets only when established for the target.

Name deliberate silence and resource priorities. Explain how levels, encounters, instructions, controls, accessibility and narrative develop alongside code. Record asset provenance, permissions and credits.

## Runnable development sequence

For each stage record:

| Stage | Playable or inspectable result | New idea and local explanation | Changes to code/data/assets | How to check it |
|---|---|---|---|---|

Build through meaningful states. Necessary files generally come from preceding work; document any supplied dependency and how it is taught. A stage can be incomplete while the game grows. Mark the stage that fulfils the finished-game promise and any later revisit explicitly.

Avoid hidden engines, wholesale unexplained rewrites, fixed unit counts and arbitrary technique quotas. Use a naive version and upgrade where the experienced limitation teaches something useful.

## Verification and finishing

Define observable checks for rules, boundaries, unusual or held input, reset/retry, win/loss where applicable, and the complete play cycle. Plan representative end-to-end runs and human playtesting. Check visuals and listen to audio; a screenshot cannot prove timing or input behaviour.

Record exact target and tool configurations, execution results, limitations and unverified claims. Include regressions for faults discovered during development. Name what would change the design recommendation.

Plan packaging, instructions, credits, permissions and feedback. Identify techniques worth extracting into the Pattern Library, with links back to their complete game. Follow [the content workflow](content-creation-workflow.md) before claiming completion.
