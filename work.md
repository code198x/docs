# Current work

This file holds bounded next work and proposals. [PROJECT.md](PROJECT.md) owns agreed direction; source files and catalogues establish implementation state. Remove completed items instead of keeping a second status history.

## Spectrum sequences

**Status: review scope; no replacement game lineup has been adopted.** The [project charter](PROJECT.md) and [game-brief specification](specifications/brief.md) govern the work. The agreed quality standard is a complete, enjoyable and deliberately finished game for its scope; BASIC games need not meet commercial standards.

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

Produce reviewable game briefs and a sequence mapping before lesson rewrites. Record concrete missing shared explanations, Vault entries, patterns and component needs. Resolve substantive conflicts with the briefing and separate recommendations from decisions. Historical versions remain in Git; the current specifications should not require reading amendment chains to discover the project goals.

Use the [retained game-design material](platforms/README.md) alongside current sources. Existing sample/prototype files and capture manifests are the starting point for execution, not an old prose claim that a tool or game is verified.

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
