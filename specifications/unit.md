# Unit specification

A unit gives a focused explanation and a meaningful result within a guided sequence. Apply [curriculum design](curriculum.md) and [writing voice](writing-voice.md); use [the content model](content-model.md) for paths and schema.

## Teaching shape

Establish what we are making or investigating, and why it matters now. Explain the knowledge used locally, with optional links for depth. Show a useful expected result, then grow the program or experiment through understandable stages.

At each stage explain the change, its mechanism and the observation that checks it. Code, graphics, sound and design decisions belong together when the feature needs them. Do not delay all polish until a final ceremonial unit.

System-building stages should run. A Foundations or Craft stage may instead produce a paper model, trace, diagram or pseudocode result. State which kind of evidence it supplies.

Give instructions, useful troubleshooting and optional experiments. Use headings that fit the material; introductions, summaries, Vault boxes and modern comparisons are not compulsory repeated sections.

## Continuity

Keep complete runnable states in the sample repository and show focused changes with `CodeDiff` where appropriate. `CodeFromFile` supplies an inspectable full state. Use named `steps/step-NN` files when a unit has multiple runnable stages.

Do not hide essential implementation in unexplained starter code. When reusing files from a previous game, name them, explain their contracts and provide a clear route to understanding them. Restructuring should be motivated and taught as a visible change.

A unit's size follows its teaching load, not a fixed line count or duration. Explain unfamiliar syntax and hardware at the point of use. The reader should not need to assemble the essential explanation from several linked pages.

## Media and execution

Use [capture manifests](../infrastructure/media-capture-pipeline.md) where the supported tooling permits. Keep the input sequence and initial state reproducible. Distinguish a cold boot or real tape load from direct program injection or a snapshot. If setup writes alter game state, record them; never present that setup as an ordinary playthrough.

Inspect screenshots at their displayed size. Use video or interaction checks for movement, timing and input. Listen to sound examples. Captions describe the observed state and why it matters. Provide readable alternatives where information would otherwise depend only on colour or sound.

Screenshots and illustrations have different jobs. A diagram may explain memory; a captured frame proves only what was visible in that particular execution.

## MDX

System units live at `src/content/curriculum/<system>/<track>/<module>/unit-NN.mdx` in the website. Shared units live at `src/content/curriculum/<section>/<module>/unit-NN.mdx`.

Use the fields accepted by `src/content.config.ts`: `title`, optional `description` and `pubDate`, and the required `game` and `unit` numbers; `tags` may be supplied. The numeric `game` field is an implementation requirement, not a curriculum-wide fixed game count. Navigation and system metadata are derived rather than copied into frontmatter.

Use existing components for code, outputs, traces and diagrams. Pseudocode can be inline; maintained executable listings belong in code-samples. Check imports and use paths relative to the component's documented content root.

## Ready to publish

- The unit fits an agreed specification and can be understood by its intended reader.
- Every runnable state builds or loads with the stated tools and behaves as described in the named configuration.
- The expected result, media, experiments and troubleshooting were checked; limitations are explicit.
- Code and assets develop through explained changes, with provenance and permissions addressed.
- Required links resolve and provide useful context. Proposed pages are not presented as available.
- The prose follows the editorial standard and the relevant site checks pass.

These are authoring checks, not learner pass/fail gates. At game completion, also run the end-to-end and playtesting checks in [the workflow](content-creation-workflow.md).
