# Current work

This file holds bounded next work and proposals. [PROJECT.md](PROJECT.md) owns agreed direction; source files and catalogues establish implementation state. Remove completed items instead of keeping a second status history.

## Spectrum sequences

**Status: BASIC opening direction agreed; remaining game lineups under review.** The [Meet BASIC specification](platforms/sinclair-zx-spectrum/basic/meet-basic.md) owns the guided introduction through short projects and the recommended opening into Bright Spark and Touchdown. The [lesson and source mapping](platforms/sinclair-zx-spectrum/basic/meet-basic-plan.md) has an A1–A3 implementation slice: draft lessons and nine verified BASIC checkpoints, including input and sentence-building. Steve has tested and approved revised A1–A3 and confirmed the host-keyboard fix in native use. Publication still requires the coordinated route/catalogue migration. The remaining arcs are not yet implemented. The [project charter](PROJECT.md) and [game-brief specification](specifications/brief.md) govern the work. The agreed quality standard is a complete, enjoyable and deliberately finished game for its scope; BASIC games need not meet commercial standards.

### Evidence to start from

The website has a substantial BASIC sequence and an assembly opening, with sample sources and [retained game plans](platforms/README.md). Inspect the website’s `src/content/modules/sinclair-zx-spectrum/`, the corresponding unit metadata and authored MDX, and `code-samples/sinclair-zx-spectrum/` together. Availability labels alone are insufficient evidence of what a learner can build.

Existing ideas include introductory BASIC programs, deduction and guessing games, quizzes and stories, grid puzzles, resource decisions and action games. The assembly material includes machine/language introductions, Gloaming and Shadowkeep, with plans extending beyond the implemented opening. Retain these as candidates and evidence, not an instruction to port each BASIC game to assembly.

Foundations now uses pseudocode. Read the actual rewrite rather than assuming the old Sinclair BASIC coverage. Maths for Games and Game Feel already have material under Craft, including planned unit breakdowns; a landing page or breakdown does not establish authored lessons. The broader Craft, AI, data-structure and asset coverage in the charter remains work to develop.

### Review questions

For each existing or proposed game, explain its recurring activity and appeal; its fit to Spectrum and language; what it introduces, reinforces or recalls; and the programming, maths, design, asset and hardware ideas that grow together. Map links to shared explanations, the Vault and useful reusable patterns without making those links essential missing instructions.

Plan meaningful runnable stages and a complete endpoint. Specify target configuration, host tools, source/build outputs and checks. Compare alternative game choices where they teach something different. Do not preserve arbitrary counts, commercial comparisons or genre exclusivity as requirements.

BASIC and assembly each admit independent entry. A brief recall of programming concepts can accompany the first real example; an explanation of syntax and machine behaviour must remain local. Gloaming's compact assembly scope and Shadowkeep's room-based systems deserve assessment for their distinct teaching roles; neither fixes the new sequence in advance.

### Models and wider systems

The existing Spectrum opening uses a stock 48K target; previous plans also discuss 128K facilities and Spectrum Next use. Keep the distinction between running a stock-compatible program on a Next and requiring Next-specific facilities. Before changing a game's target, check its actual source, brief, build recipe and execution evidence. Do not transfer a later model's capabilities into an earlier model's description.

A later expanded-machine project may be valuable if it explains the extension, what the Spectrum still does, the communication interface, changed constraints and new bottlenecks. Cross-development tools are host conveniences, not target expansions.

Keep useful contrasts with C64, Amiga, NES and future systems visible. Reusing a mechanic should illuminate a difference in language, CPU, memory, display, sound or input; it is not a requirement for identical projects or lesson counts.

### Next output

Use the [Meet BASIC lesson and source mapping](platforms/sinclair-zx-spectrum/basic/meet-basic-plan.md) for implementation. A1–A3 are approved drafts with verified target-side checkpoints and user-reported native acceptance. A4 is drafted with two verified checkpoints, finishing Story Builder with a setting, another event and readable presentation. Review A4 next, then begin Lucky Number with a known secret and useful clues. Coordinate the route/catalogue migration before publishing the revised module. Reconcile Bright Spark and Touchdown's briefs with that opening. Keep subsequent BASIC and assembly choices as proposals for joint review.

Produce reviewable game briefs and a sequence mapping before lesson rewrites. Record concrete missing shared explanations, Vault entries, patterns and component needs. Resolve substantive conflicts with the briefing and separate recommendations from decisions. Historical versions remain in Git; the current specifications should not require reading amendment chains to discover the project goals.

Use the [retained game-design material](platforms/README.md) alongside current sources. Existing sample/prototype files and capture manifests are the starting point for execution, not an old prose claim that a tool or game is verified.

### Entry-route findings for joint review

A source review of the current Spectrum entry route found these conflicts to resolve alongside the game specifications. They are findings, not an adopted replacement sequence:

- The BASIC track landing says no previous programming experience is assumed, but `basic/meet-basic/index.mdx` and its first unit direct complete beginners to Foundations. Unit 1 also refers to having written `SHOW` in General Programming. Decide the local explanation needed for independent entry before revising the primer.
- The track metadata calls BASIC a gateway preparing readers for assembly, while its body correctly says the routes are independent. Align this framing when reviewing the track.
- Spectrum `getting-started.mdx` covers both assembly and BASIC conversion, but its final action sends everyone to assembly. Align that system-specific guide with the general Setup Guide’s separate BASIC and assembly routes, and check that a BASIC beginner can reach the emulator and keyword editor.
- Spectrum getting-started and native-setup pages give different macOS Fuse installation commands (`fuse-emulator` and `fuse`). The native page also foregrounds Pasmo while getting-started recommends Asm198x. Verify current installation instructions and choose a clear canonical setup path; do not infer installer success from the existence of the tools locally.
- The first BASIC unit uses two step files and two captures that exist in the samples and website trees. It explains `P` for `PRINT`, but then says to type `RUN` without explaining how to enter that keyword in the chosen emulator. Include the exact target/editor configuration and a first-run check in the joint review.

The reviewed navigation is Systems → ZX Spectrum → BASIC → Meet BASIC → Unit 1. File and page presence establishes availability only. This review has not verified a fresh installation, replayed the first program or established that a screenshot matches execution. Keep those checks explicit in the subsequent Spectrum work.

## Website components

This is an assessment for the current curriculum direction, not a commitment to build every idea. Component names below refer to implementations in the website's `src/components/`; their props and tests remain authoritative. No new curriculum interface is required before the Spectrum specifications can be agreed.

### Available foundations

| Teaching need | Existing components | Use and limits |
|---|---|---|
| Explain code and changes | `CodeFromFile`, `CodeDiff`, `Output` | Display real sources and focused changes; pseudocode remains distinct from executable code |
| Trace values and decisions | `TraceTable`, `FlowDiagram`, `TruthTable`, `LogicCircuit` | Tables and diagrams support conceptual lessons; `TraceTable` is a semantic static table, not an interpreter |
| Inspect representation | `MemoryMap`, `RegisterBits`, `SpriteGrid`, `SpectrumBitmapLayout` | Explain data layouts with named assumptions; the Spectrum bitmap component is machine-specific |
| Draw and examine graphics | `SpriteEditor`, `Figure`, `NativeImage`, `ImageComparison` | Existing editing/display primitives support asset experiments; inspect format and export support before promising an asset workflow |
| Hear or see an outcome | `AudioClip`, `VideoPlayer`, `VideoEmbed`, `FieldVideo` | Pair media with captions and useful alternatives; media playback does not teach composition by itself |
| Try target code | `AssembleAndRun`, `Emulator`, `Workbench` | Existing execution/display facilities have different contracts; confirm machine and language support rather than treating them as one universal runner |
| Find a route or setup | `FirstStepCallout`, `CurriculumPosition`, `PathCard`, `UnitSteps`, `SetupCallout` | Review copy for optional preparation and independent entry; do not add completion gates |

### Proposed next steps, in order of demonstrated need

1. **Target and build information.** Begin with a consistent brief/lesson table naming runtime machine, model, memory, extensions, input and host tools. If repeated across the first re-specified games, factor it into one accessible `TargetConfiguration` component backed by explicit metadata. Do not infer runtime capabilities from a fleet badge.
2. **Local concept connections.** Use short prose and existing links first. If repeated presentations need a component, it should state the immediate concept and why the optional deeper explanation helps. No prerequisite checklist or interruption between every step.
3. **Steppable traces.** A small, bounded enhancement could show state changes for a loop, queue or opponent state machine while retaining a printable `TraceTable`. Specify the state transitions and test trace consistency before implementation. A full pseudocode interpreter remains a separate proposal, not a dependency of Foundations.
4. **Spatial and behavioural experiments.** Use existing grids and diagrams for distance, collision, pursuit and route finding. Build an interactive grid only when a worked game demonstrates the need to vary obstacles, tie-breaking or perception. Show the rule and its limits; avoid a general simulation framework before there is a lesson to validate it.
5. **Asset comparisons.** Reuse image/audio primitives to compare palette, animation timing, channel allocation and readability. Extend export/conversion tools only around an agreed target format. A tracker, animation studio or universal asset editor is not implied by asset-creation coverage.

### Questions and answer feedback

A lightweight question-and-explanation presentation is a candidate for the checks described in [Unit guidance](specifications/unit.md#questions-and-feedback). Begin with authored questions and separated answers; standard HTML `details`/`summary` can provide an accessible reveal without a quiz engine. Check the current MDX rendering and print behaviour before adopting it as a repeated pattern.

If several lessons need a shared component, first specify a prompt, optional choices and an explanatory answer. Multiple-choice feedback should explain the misconception; open questions should allow discussion rather than automatic grading. Keep answers readable on paper, controls keyboard-accessible and feedback understandable without colour alone. Do not require accounts, persistent scores, completion tracking or a passing mark. This remains a component proposal, not an implemented facility.

### Acceptance conditions for any addition

Essential explanation remains readable without running an interaction. Provide keyboard operation, visible focus, labelled controls, touch targets of at least 44 CSS pixels and narrow-screen layouts without page overflow. Do not depend solely on colour, sound, hover or animation. Respect reduced motion and user-controlled playback; reserve media dimensions to prevent layout shifts.

A visualisation must name what it models and what it omits. A hand-authored trace is not execution evidence; an emulator result is tied to its version and configuration. Test meaningful state transitions and reset behaviour, inspect keyboard/touch use and screenshots, and use the existing accessibility checks. Avoid adding a new framework or duplicate component when a small extension serves the lesson.

## Vault editorial work

Check existing entries and their source citations before creating new ones. Two useful investigations survive the earlier task notes:

- Resolve useful entity mentions in Fast Facts and body prose to the correct existing entry. Match the person or organisation in context, not just the display name; namesakes must not acquire each other’s credits. Treat automatic matches as suggestions for review. Derive current candidates from content rather than copying an old count.
- Identify missing entries from real curriculum and Vault links. Earlier work found candidate clusters around British software publishers and the LightWave/Video Toaster ecosystem. Check which entries now exist, retain precise source evidence for any remaining gap, and prioritise entries that help an actual lesson. An old backlog is not evidence that someone still lacks an entry.

For game playtesting, work from the current program and its brief: held as well as tapped inputs, buffered actions, repeated title/retry cycles, readable feedback, audio timing, difficulty and whether the game remains interesting after its rules are understood. Record findings with the game and distinguish scripted correctness from human playtesting.

## Website editorial follow-through

Apply the charter’s plain-language navigation and publishing guidance during the House UI review. Review About, the systems directory and the three editorial hubs together with the homepage. “Systems” replaces “The Fleet”; further renaming remains a proposal until reviewed in context.

Prepare a What’s New entry when the House UI is ready to release, linking to the finished site and explaining the reader-facing improvements. Consider From the Metal or Field Notes only where the work yields a useful explanation or an evidenced investigation. No release announcement is implied by the existence of a preview.

Try a small explanatory illustration before adding a site-wide visual treatment. Later candidates include verified game captures on relevant system cards and asset close-ups linked to lessons. Check the actual assets, provenance and target configuration before selecting them.

## Shared module outline review

Review the Maths for Games and Game Feel outlines and their catalogue metadata against the charter before developing their units. Maths currently assumes completion of Numbers & Bits, uses Sinclair BASIC as its shared demonstrator and makes sweeping claims about arithmetic costs across machines. Distinguish pursuit from pathfinding and behaviour design from arithmetic. Game Feel needs a review of universal prescriptions about grace periods, feedback and timing. Retain useful examples while making entry independent, language-neutral explanations concrete and machine claims specific. The Craft index offers a paper experiment and identifies both modules as outlines; it does not establish completed units or settle a new module structure.
