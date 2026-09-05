# Curriculum component assessment

This is an assessment for the current curriculum direction, not a commitment to build every idea. Component names below refer to implementations in the website's `src/components/`; their props and tests remain authoritative. No new curriculum interface is required before the Spectrum specifications can be agreed.

## Available foundations

| Teaching need | Existing components | Use and limits |
|---|---|---|
| Explain code and changes | `CodeFromFile`, `CodeDiff`, `Output` | Display real sources and focused changes; pseudocode remains distinct from executable code |
| Trace values and decisions | `TraceTable`, `FlowDiagram`, `TruthTable`, `LogicCircuit` | Tables and diagrams support conceptual lessons; `TraceTable` is a semantic static table, not an interpreter |
| Inspect representation | `MemoryMap`, `RegisterBits`, `SpriteGrid`, `SpectrumBitmapLayout` | Explain data layouts with named assumptions; the Spectrum bitmap component is machine-specific |
| Draw and examine graphics | `SpriteEditor`, `Figure`, `NativeImage`, `ImageComparison` | Existing editing/display primitives support asset experiments; inspect format and export support before promising an asset workflow |
| Hear or see an outcome | `AudioClip`, `VideoPlayer`, `VideoEmbed`, `FieldVideo` | Pair media with captions and useful alternatives; media playback does not teach composition by itself |
| Try target code | `AssembleAndRun`, `Emulator`, `Workbench` | Existing execution/display facilities have different contracts; confirm machine and language support rather than treating them as one universal runner |
| Find a route or setup | `FirstStepCallout`, `CurriculumPosition`, `PathCard`, `UnitSteps`, `SetupCallout` | Review copy for optional preparation and independent entry; do not add completion gates |

## Proposed next steps, in order of demonstrated need

1. **Target and build information.** Begin with a consistent brief/lesson table naming runtime machine, model, memory, extensions, input and host tools. If repeated across the first re-specified games, factor it into one accessible `TargetConfiguration` component backed by explicit metadata. Do not infer runtime capabilities from a fleet badge.
2. **Local concept connections.** Use short prose and existing links first. If repeated presentations need a component, it should state the immediate concept and why the optional deeper explanation helps. No prerequisite checklist or interruption between every step.
3. **Steppable traces.** A small, bounded enhancement could show state changes for a loop, queue or opponent state machine while retaining a printable `TraceTable`. Specify the state transitions and test trace consistency before implementation. A full pseudocode interpreter remains a separate proposal, not a dependency of Foundations.
4. **Spatial and behavioural experiments.** Use existing grids and diagrams for distance, collision, pursuit and route finding. Build an interactive grid only when a worked game demonstrates the need to vary obstacles, tie-breaking or perception. Show the rule and its limits; avoid a general simulation framework before there is a lesson to validate it.
5. **Asset comparisons.** Reuse image/audio primitives to compare palette, animation timing, channel allocation and readability. Extend export/conversion tools only around an agreed target format. A tracker, animation studio or universal asset editor is not implied by asset-creation coverage.

## Acceptance conditions for any addition

Essential explanation remains readable without running an interaction. Provide keyboard operation, visible focus, labelled controls, touch targets of at least 44 CSS pixels and narrow-screen layouts without page overflow. Do not depend solely on colour, sound, hover or animation. Respect reduced motion and user-controlled playback; reserve media dimensions to prevent layout shifts.

A visualisation must name what it models and what it omits. A hand-authored trace is not execution evidence; an emulator result is tied to its version and configuration. Test meaningful state transitions and reset behaviour, inspect keyboard/touch use and screenshots, and use the existing accessibility checks. Avoid adding a new framework or duplicate component when a small extension serves the lesson.
