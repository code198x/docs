# AMOS and Blitz tooling feasibility

**Status: proposal for investigation.** We should consider implementing an AMOS
interpreter or Blitz compiler if it makes reliable creation and investigation
substantially more accessible. First establish which learner problems it solves
and compare that work with improving access to the original tools.

The [AMOS course brief](amos/course-brief.md) recommends a small take-away game
for discussion; the [Blitz course brief](blitz/course-brief.md) retains a switch
puzzle as a candidate. Both need
repeatable run, edit, stop, save, reopen and error recovery. Neither requires a
new language implementation to begin a native prototype.

## Learner and authoring requirements

| Need | Minimum useful result | Evidence required |
| --- | --- | --- |
| Start creating | Open the selected environment and run a tiny program through documented controls | A fresh setup reaches the stated result without unmentioned files or steps. |
| Keep and resume work | Export or save source, reopen it and run the edited version | The reopened edit survives leaving the session; distinguish source, executable, artwork and emulator snapshot. |
| Recover | Stop a continuing program, locate an error, repair it and run again | The same learner-facing route succeeds after both an intentional error and ordinary termination. |
| Understand execution | Connect an input with a changed value, rule and visible result | A trace or inspection agrees with actual execution. Source stepping and variable watches are valuable candidates, not assumed available features. |
| Check lessons | Build or load exact maintained sources, drive input and inspect outcomes | Records identify source, language, runtime, machine/media and input; checks reject an intentionally wrong result. |
| Preserve the target | Explain which work occurs on the host and which on the Amiga | A host simulation is labelled as such; Amiga timing claims come from target execution and measurement. |

For the AMOS opening, initially investigate text output, validated choices,
values, decisions, loops and source storage. A later visual counter display can
motivate counted drawing and routines. Pointer controls, moving objects and
collision are later capabilities rather than prerequisites for this first game.
The full AMOS track can grow to substantial games as those needs emerge.
For Blitz, investigate output, action input, values,
arrays, routines, compilation and source/executable storage; add the selected
display and sound path after the interaction prototype. Exact command coverage
comes from accepted checkpoint programs and language research, not these topic
labels alone.

Browser execution is a delivery option to assess. An offline native workflow and
a browser editor have different packaging, storage and debugging requirements;
we have not selected one as the sole learner route.

## What the existing evidence establishes

The [greeting evidence](../../audit/2026-10-amiga-greetings/REPORT.md) and
[unit-five record](../../audit/2026-10-amiga-unit-five/REPORT.md) establish
selected execution in AMOS Professional 2.00 and AmiBlitz 3.13.0b under FS-UAE
3.2.35. The latter records A1200/68020, PAL, 2 MB chip and 8 MB fast memory,
Kickstart and Workbench 3.1. Retained failures include incorrect source-file
format assumptions, editor/recovery mistakes and missed brief input. These are
specific workflow problems to address, not proof that either language needs
reimplementation.

The [official AMOS source](https://github.com/AOZ-Studio/AMOS-Professional-Official/tree/533b4b1f5acd604814513f78e02c7b4796cb0531)
provides an original implementation to inspect. Its source licence and upstream
notices must be checked for the particular material reused. The
[AmiBlitz source repository](https://github.com/AmiBlitz/AmiBlitz3) and
[3.13.0b release](https://github.com/AmiBlitz/AmiBlitz3/releases/tag/v3.13.0b)
provide another research starting point. The
[upstream README](https://github.com/AmiBlitz/AmiBlitz3/blob/5dd815f880d72c5285b380ef3ddebfa5766d0626/README.md)
explicitly distinguishes IDE requirements from requirements of compiled output.
Source availability does not establish host portability, a complete build path,
permissions for every bundled component or compatibility with original Blitz 2.

The family's existing assembly build/capture direction is recorded in
[the tooling migration decision](https://github.com/stevehill1981/198x/blob/main/decisions/code198x-dev-tooling-migration.md).
It does not establish an AMOS or Blitz host compiler. Assess Emu198x integration
against actual language workloads before extending its assembly evidence to
these routes. Keep the checked third-party route available during investigation.

## Implementation options

| Option | Potential benefit | Substantial work and limitations | Useful first experiment |
| --- | --- | --- | --- |
| Original runtime or compiler in an emulated Amiga | Original language behaviour and a direct path to period software | Lawful media provision, startup, source import, editor controls, persistent storage, automation and diagnostics need a coherent delivery route. | Run an exact tiny source, change it, trigger and repair an error, save, restart and reopen; then execute one input/state checkpoint. |
| Compatible host interpreter, potentially delivered in a browser | Direct editing, fast experiments and deliberately designed inspection facilities | Implement parsing, evaluation, types, control flow, errors and required libraries. Graphics, input, sound, files and timing need explicit contracts. Host speed cannot stand in for Amiga speed. | Execute a small semantic comparison corpus, then one graphical/input program against the named original implementation. |
| Cross-compiler producing Amiga executables | Host authoring and repeatable builds with execution on the target | Implement language semantics, code generation, runtime/library calls, executable output and useful diagnostics. Debugging needs a separate source-to-execution design. | Compile values, decisions, a loop and a routine into an executable; load it on the target and compare its results and a deliberate failure with the original compiler. |

Choose independently for AMOS and Blitz. Reuse or adaptation of existing source
belongs in the feasibility work for each option; the choice is not automatically
between writing everything from scratch and changing nothing.

A compiler's runtime is part of the product. Generating valid 68000 instructions
alone does not reproduce screen, sound, input or OS behaviour. A host interpreter
that shows similar pictures also needs to match the language's observable rules
before it can be described as compatible.

## Compatibility and correctness

Select the dialect and exact reference version first. For Blitz, decide whether
the target is original Blitz BASIC 2, AmiBlitz or a documented common surface.
For AMOS, begin comparison against the checked Professional 2.00 environment.
Do not generalise a successful example to every version.

Build independent cases for expression precedence, number representation and
overflow, strings, assignment, conditions, loop bounds, routines and scope,
array bounds, errors and termination. Add drawing coordinates, palettes,
input states, sound and file behaviour as those capabilities enter scope.
Use original manuals and source to form expectations; investigate discrepancies
by executing the named original implementation.

The [family general-tools decision](https://github.com/stevehill1981/198x/blob/main/decisions/family-tools-are-general.md)
requires correctness within a supported capability. It allows staged breadth;
it does not allow hard-coding lesson examples or silently accepting unsupported
behaviour. Reject unsupported features with diagnostics that name them. Preserve the original tool's
observed behaviour, including inconvenient semantics, rather than quietly
inventing an easier dialect.

Native and browser builds of our own implementation agreeing would be one
implementation agreeing with itself. Keep original-runtime comparisons
independent. Neither compiler tests nor source inspection measures learning.

## Proposed feasibility experiment

Start with the existing original-tool route as a comparison baseline. This is a
recommendation for the investigation order, not a decision against building a
language implementation.

1. **Set the intended experience and dialect.** Decide how important immediate
   browser editing is, which native/offline route must remain available, and
   the Blitz version to teach. Confirm the provisional projects before adapting
   the tools around them.
2. **Inventory actual reusable tools and source.** Record revisions, build
   requirements, component permissions, diagnostics, source import and available
   automation. Check dependencies before proposing additions. Do not assign a
   new compiler or interpreter to Asm198x, Emu198x or a new repository without
   an ownership decision.
3. **Exercise the complete working loop in both languages.** Run the greeting,
   edited greeting, error/repair and save/reopen cycle from maintained source.
   Then run a bounded AMOS take/update/result test and a Blitz switch-state test,
   including held/released input and an ordinary exit. Reuse existing evidence
   where its route is identical; verify changed steps directly.
4. **Write a small semantic comparison corpus.** Include at least one boundary
   and deliberately wrong result for every checked operation. Record original
   outputs and failures before implementing the corresponding replacement.
   Keep source programs in code-samples and distinguish expected values from
   newly observed results.
5. **Compare delivery choices.** Report the work required to remove the actual
   setup, persistence and inspection difficulties. For a new implementation,
   propose a first supported surface, comparison criteria, runtime strategy and
   milestones for native/browser delivery. Give effort estimates only after
   source/build investigation; record the assumptions behind them.

The review should be able to choose: improve original-runtime delivery; approve
a bounded implementation prototype for either language; or gather one named
missing piece of evidence. A full interpreter or compiler remains a legitimate
destination. The first milestone must show useful compatibility and the
learner benefit that justifies continuing.

## Conditions that change the recommendation

Prefer improving original-runtime delivery if the complete working loop can be
made dependable and accessible with acceptable setup and persistence. Give a
new implementation greater priority if browser availability, source inspection
or repeatable authoring remains materially limited and a compatibility prototype
shows a credible way to improve it.

Reject a proposed replacement if it requires teaching different behaviour under
the original language's name, discards the target's relevant constraints, or
claims compatibility from the curriculum examples alone. Stop and revise the
scope after repeated unsuccessful experiments rather than turning course
development into an indefinite tooling dependency.
