# Unit specification

A unit gives a focused explanation and a meaningful result within a guided sequence. Apply [curriculum design](curriculum.md) and [writing voice](writing-voice.md); use [the content model](../website.md#content-and-navigation) for paths and schema.

## Teaching shape

Establish what we are making or investigating, and why it matters now. Explain the knowledge used locally, with optional links for depth. Show a useful expected result, then grow the program or experiment through understandable stages.

At each stage explain the change, its mechanism and the observation that checks it. Code, graphics, sound and design decisions belong together when the feature needs them. Do not delay all polish until a final ceremonial unit.

System-building stages should run. A Foundations or Craft stage may instead produce a paper model, trace, diagram or pseudocode result. State which kind of evidence it supplies.

Give instructions, useful troubleshooting and optional experiments. Use headings that fit the material; introductions, summaries, Vault boxes and modern comparisons are not compulsory repeated sections.

## Questions and feedback

Use a short check where it advances the explanation, for example before revealing a result, after a tricky distinction or when combining ideas. Consider:

- **Predict:** what will this loop display, or where will the object move next?
- **Trace:** record the score and lives after this sequence of events.
- **Explain:** why does this collision rule treat touching edges differently?
- **Diagnose:** find the first point where this trace disagrees with the intended rule.
- **Change and observe:** alter one value, predict its effect, then compare with the result.
- **Compare:** which sprite remains readable against this background, and what would you change?

State the assumptions and give enough information to reason about the answer. Use plausible alternatives when testing a misconception; avoid trick wording, irrelevant trivia and questions answerable only by remembering a term from another page. Offer occasional short module-level checks that combine ideas, without forcing a test after every unit.

Give the answer with its reasoning and, where helpful, explain a tempting wrong answer. Open design questions need examples and criteria rather than an automatic right/wrong mark. Make explanations easy to reveal after an attempt, without withholding them until a score is reached. A parent or teacher should be able to use the same question and explanation in conversation or on paper.

Check worked answers against the stated pseudocode or target program, and verify claimed experimental results. An answer-reveal component does not execute the example or prove it correct. Questions can begin as ordinary prose with a clearly separated explanation; interactive scoring is not required.

## Continuity

Keep complete runnable states in the sample repository. `CodeFromFile` supplies an inspectable full state. Use named `steps/step-NN` files when a unit has multiple runnable stages.

### Showing changes

In introductory lessons, state the editing action explicitly: “Replace line 10”, “Add lines 30, 40 and 50”, or name the routine and the exact insertion point. Show ordinary code containing exactly what to enter, without diff markers or deleted code. Explain deletions separately. In BASIC, distinguish the program's line numbers from positions in a source file; avoid adding a second set of numbers beside the listing.

While programs are short, show the complete listing at each runnable checkpoint and identify which lines to enter or replace. A separate changed-lines block is useful only when it makes the action clearer; do not duplicate every short listing mechanically. Follow the change with an expected result and a purposeful prediction or experiment.

As programs grow, show the changed routine or a focused excerpt with enough context and precise placement instructions, and provide the complete source separately. Keep excerpts tied to maintained samples so they agree with the runnable state.

Do not use `CodeDiff` as the required editing instructions in introductory lessons. Reserve diffs for optional comparisons after explaining their notation, or for lessons that teach tools such as version control. The essential building sequence must remain understandable without reading a diff.

Do not hide essential implementation in unexplained starter code. When reusing files from a previous game, name them, explain their contracts and provide a clear route to understanding them. Restructuring should be motivated and taught as a visible change.

A unit's size follows its teaching load, not a fixed line count or duration. Explain unfamiliar syntax and hardware at the point of use. The reader should not need to assemble the essential explanation from several linked pages.

## Media and execution

Use [capture manifests](../website.md#capture-and-execution) where the supported tooling permits. Keep the input sequence and initial state reproducible. Distinguish a cold boot or real tape load from direct program injection or a snapshot. If setup writes alter game state, record them; never present that setup as an ordinary playthrough.

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
