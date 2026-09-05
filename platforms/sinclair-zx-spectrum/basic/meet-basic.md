# Meet BASIC

**Status: agreed module direction; detailed lesson breakdown and implementation pending.**

Meet BASIC is the guided introduction to programming in Sinclair BASIC on the ZX Spectrum. It teaches through short projects, combining the useful existing primer and early programs rather than placing both sequences one after the other. Apply the [curriculum specification](../../../specifications/curriculum.md) and [unit guidance](../../../specifications/unit.md).

## Place in the curriculum

The recommended opening is **Meet BASIC → Bright Spark → Touchdown**. This settles the opening direction, not the remaining BASIC lineup or any assembly sequence. Bright Spark and Touchdown still need their individual briefs reconciled with the sequence review before lesson development.

Foundations explains programming concepts through pseudocode. Meet BASIC introduces the Spectrum's language, editor and working environment, explaining the concepts locally for readers who have not attended Foundations. The games then develop larger, sustained projects with increasingly interesting mechanics.

Beginners should find a coherent recommended route through Meet BASIC. Readers with relevant experience can use individual sections as references or begin with Bright Spark. Its opening must describe the knowledge used and link to specific explanations, without requiring completion of the primer. Independent entry to assembly remains unchanged.

Meet BASIC ends when readers can make, run, change, save and investigate a small program. It does not need to introduce every command or representation a later game will use. Sequence storage, indexing and more substantial decomposition can arrive in Bright Spark with local explanations.

## Target and working environment

The runtime target is a stock 48K ZX Spectrum using Sinclair BASIC, its keyboard editor, screen and beeper. No expansion or assembly-language helper is required. Other Spectrum models and legacy modes are separate compatibility checks, not permission to rely on their additional facilities.

The principal learner experience is entering, running and editing BASIC in the target environment, whether on an emulator or original hardware. Explain the host keyboard mapping and keyword-entry modes for the documented emulator. Show precisely how to enter and run commands; do not explain `PRINT` entry and then assume the reader knows how to enter `RUN`.

Save and reopen a small program early. Distinguish a saved BASIC program or tape image from an emulator snapshot and explain which method the instructions use. Name the file, where it is saved and how to load it again. Include an original-hardware saving route where supported by checked instructions.

When introducing a host-edited `.bas` source and conversion to a tape image, explicitly call this cross-development: the editor and converter run on the host; the resulting program runs on the Spectrum. This is an alternative workflow to explain when useful, not another installation requirement before the first program. Select and verify the canonical emulator, converter and commands during implementation; the conflicting existing setup instructions are not a settled tool specification.

## Project sequence

These are project arcs, not fixed lesson counts or a requirement to retain every existing feature. Each arc contains short runnable stages and a clear endpoint. Reuse and reshape the existing work; do not concatenate its current lessons unchanged.

| Arc | Experience and endpoint | Programming introduced locally | Design, assets and machine understanding |
|---|---|---|---|
| A greeting that becomes **Story Builder** | Enter a greeting, change it, ask for words and produce a short personalised story. Save and reopen it. | Keyword entry, immediate commands and stored lines, line numbers, `PRINT`, variables, `INPUT`, strings and execution order. | Write inviting prompts and legible output. Explain how supplied words become data used by the program. A creative toy needs no score or losing condition. |
| **Lucky Number** | Make a guess, receive a useful clue, continue until successful and choose another round. | Numeric variables, comparisons, `IF`, repetition with `GO TO`, random selection and a guess counter where useful. | Choose a number range and explain it. Combine words with colour and sound so the clue remains understandable without either. Explain why the program repeats and how it stops. |
| **Oracle Stone** | Ask a question and receive a selected response with deliberately designed presentation. | Selecting among responses; counted repetition where repeated presentation motivates it; `GO SUB` and `RETURN` when duplicated work gives them a purpose. | Author responses, choose colours and brief sounds, and investigate pauses. Explain that random selection does not interpret the question. Keep the experiment short rather than adding features to justify its place. |
| **Movement and input experiment** | Move a marker within a bounded screen area while the program continues to run. A small Reflex experiment may substitute if its timing and input rules are specified and checked. | Screen coordinates, `PRINT AT`, `INKEY$`, a continuing update loop, position changes and boundary decisions. | Draw, erase and redraw a readable marker. Compare waiting for input with polling. Investigate held keys, pace and screen edges. Explain the difference between an iteration count and measured elapsed time. |

Within each arc, show the smallest useful result first, then motivate the next change. Save named checkpoints and show focused differences alongside complete sources. A new project may begin a new small listing; code carried forward must be identified and explained. Do not supply an unexplained menu, drawing framework or game engine.

The movement experiment is the default planning choice. Choosing the exact experiment and distributing ideas between lessons are implementation decisions within this specification, provided the resulting route meets the teaching and verification requirements.

## Optional and later projects

**Dice Roller** can sit alongside Lucky Number as an optional probability experiment: compare predictions with observed frequencies and explain any scaling used in a chart. It is not a prerequisite for Bright Spark. Keep the display within its intended area for the permitted sample sizes.

**Hi-Lo** and **Quiz Master** remain candidates for later short projects. Do not squeeze them into Meet BASIC merely because they are smaller than the main games. A learner-authored quiz is a programming project; the curriculum's questions and feedback serve a different purpose.

The shorter projects remain valuable on their own. Their treatment here does not require commercial standards, and their integration must not remove useful existing public routes without a replacement or redirect plan.

## Teaching responsibilities and connections

Explain unfamiliar terms and syntax where they first matter. A beginner arriving directly must be able to follow the example without leaving to acquire its essential explanation. Use selective links to Foundations for deeper treatments of variables, decisions, repetition, routines and debugging. Inspect its actual pseudocode lessons rather than implying that readers have already learnt Sinclair syntax there.

Use maths in the service of the program: number ranges, comparisons, counting and row/column positions. Use The Craft for deeper questions about clues, anticipation, feedback and responsiveness when those explanations exist. Planned shared units cannot carry missing instructions.

Let readers create the words, screen arrangement, colour choices and small sound cues. Explain why those choices help someone use the program. Keep instructions and important feedback available in text; colour and sound can reinforce them. Introduce asset provenance and credits proportionately when a project uses supplied material.

Debugging belongs throughout: deliberately change a value, predict the result, inspect what happened and narrow down a discrepancy. Teach saving and recovery before work becomes costly to lose. A later debugging reference can gather the techniques without deferring their first use.

Useful questions include tracing the order of numbered lines, predicting whether a guess repeats the loop, explaining where `RETURN` resumes execution, and predicting a marker's next position at an edge. Provide answers with reasoning. No score, passing mark, account or completion gate controls progression.

A comparison with another system should explain a useful difference in BASIC syntax, input, display or sound without assuming that readers have studied it. Meet BASIC is a Spectrum introduction, not a template imposed on every machine.

## Evidence and reuse

The existing website has fifteen authored Meet BASIC units and separate early-project lessons. Those files establish the starting material, not implementation of this revised specification:

- [Meet BASIC lessons](https://github.com/code198x/website/tree/main/src/content/curriculum/sinclair-zx-spectrum/basic/meet-basic) and the [BASIC module catalogue](https://github.com/code198x/website/blob/main/src/content/modules/sinclair-zx-spectrum/basic.yaml).
- [BASIC lesson sources](https://github.com/code198x/website/tree/main/src/content/curriculum/sinclair-zx-spectrum/basic) and [sample programs](https://github.com/code198x/code-samples/tree/main/sinclair-zx-spectrum/basic).
- Retained briefs for [Story Builder](../games/story-builder/brief.md), [Lucky Number](../games/lucky-number/brief.md), [Oracle Stone](../games/oracle-stone/brief.md), [Reflex](../games/reflex/brief.md) and [Dice Roller](../games/dice-roller/brief.md). Their old unit counts, exclusions and prior-learning assumptions do not govern this module.

Use Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming* for source checking: chapters 1–3 for initial programs, decisions and input; chapters 4–5 for repetition and subroutines; chapter 11 for random numbers; chapters 15–19 for screen output, colour, graphics, keyboard polling and sound; chapter 20 for tape storage. Check the edition and exact passage when citing a technical claim in a lesson. Historical context belongs only where sourced and useful; it is not needed to justify these small programs.

## Implementation and verification

1. Map the existing lessons and samples onto these arcs. Identify retained stages, duplicated explanations, necessary new stages and reference material. Set unit boundaries by teaching load, with no fixed count or duration.
2. Reconcile the BASIC entry and setup copy with independent entry. Verify one documented path from opening the emulator to running, editing, saving and reopening the first program.
3. Build the revised sample sequence in the sample repository, then write lessons around those runnable states. Keep source changes, screenshots and instructions in agreement.
4. Check each checkpoint in the named 48K environment. Record emulator version, model, loading method and tools; distinguish typed entry, converted tape loading, injected BASIC and snapshot loading. Original-hardware verification and other-model compatibility are separate evidence.
5. Check input validation, boundaries, empty or long text where accepted, held and released keys, another round and return to editing. For Reflex, verify the clock, units and false-start behaviour before calling the result a reaction time. For movement, observe pacing and input rather than relying on a still image.
6. Inspect the screen and listen to audio. Confirm that prompts and results remain usable with sound muted and without relying on colour alone. Ensure repeated output does not unexpectedly scroll or overwrite instructions.
7. Ask a reader new to the environment to follow the opening without verbal rescue; use observed difficulties to repair explanations and setup. This is an authoring check, not a learner examination.
8. Update catalogue ordering, descriptions, links and redirects with the lesson changes. Keep Bright Spark's sequence storage and indexing explanations local rather than expanding the primer to pre-teach them. Publish only when the revised route and its artefacts have been checked.

This specification supplies no new build or execution result. The next deliverable is a concrete lesson-and-source mapping for Meet BASIC, followed by checked implementation; the remainder of the Spectrum game sequence stays under review.
