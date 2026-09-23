# Working with existing code

**Status:** Progression with one local Sonar unit 09 revisit exercise. The exercise changes a marker in a learner's copy; the maintained game source is unchanged. Later refactoring, regression and extension companions remain proposals. No existing project has been rebuilt or ported as part of this documentation pass.

Apply [unit continuity and editing conventions](../unit.md), [website/source ownership](../../website.md), [diagnosis](testing-and-diagnosis.md), [abstraction](abstraction-and-portability.md), [lifecycle](state-lifecycle-and-recovery.md), [reproducibility](randomness-and-reproducibility.md) and [profiling](profiling-progression.md). Current machines are Spectrum, C64, NES and Amiga. Revisit earlier games when a new question gives the old code a purpose; no separate maintenance module or wholesale rewrite is required.

## Existing foundations and gaps

The inspected Sonar unit 09 already teaches saving source/tape and a fresh-load whole visit. Meet BASIC unit 11 extracts an actually duplicated heading. Tail Chase unit 05 replaces shifting coordinates with circular storage and distinguishes capacity from live cells. Bright Spark explicitly documents routine state and completion. Starfield 17's source exposes entry routines, spawn mapping and audio handover. Dash 14 and Flock 11 expose main-loop/handler or hardware-reader boundaries through the existing audits.

These are maintenance material already. The missing explanation is how to return to a working project, establish what it does and select a narrow change before following new editing instructions. Missing exercises are learner-led code location, a preserved baseline and a comparison against an explicit change contract. More advanced migration and performance work remains behind timing, representation and calling-convention prerequisites.

## The recurring revisit

1. **Recover:** identify the project/checkpoint, source, assets and generated outputs. Read its instructions and actual build recipe; do not infer a command from another machine's folder.
2. **Establish a baseline:** build/load the unchanged project in the named configuration and repeat a small meaningful scenario. Save source identity, input/state and observed output. An existing binary alone does not prove the current source builds.
3. **Describe the intended change:** one sentence plus what must remain true. Classify it as behaviour, refactoring, optimisation or an extension; mixed work can be split into reviewable stages.
4. **Explain before editing:** locate the observable behaviour, follow the caller and data, name owners/lifetimes and hardware/timing assumptions. Predict the result and a plausible regression.
5. **Change narrowly:** edit the responsible code or data; preserve the working checkpoint. Follow the existing style unless a demonstrated problem justifies changing it.
6. **Compare:** repeat the scenario, inspect the prediction, check a meaningful boundary and the formerly working behaviour. Diagnose the first divergence, including stale outputs or incorrect test setup.
7. **Keep or undo:** inspect the exact diff, record evidence and commit/save a named checkpoint. A discarded experiment still teaches something; retain notes without replacing the working game.

A beginner can do this with two named source/tape copies and a short note. Once file-based development is taught, use the project's Git repository: inspect status, record a baseline, make a small commit or branch for the experiment, inspect the diff and save the explained repair. Do not teach destructive reset/clean commands as a way to recover from uncertainty or sweep unrelated edits into a checkpoint. Explain source versus generated artefacts before deciding what belongs in a commit.

## Build and run are part of understanding

Source audit examples, not claims that these commands were executed here:

- Spectrum Sonar final source is `sinclair-zx-spectrum/basic/sonar/teaching/unit-08/steps/step-01.bas`; unit 09 specifies named tape SAVE/LOAD and a fresh 48K session. Compare the loaded listing with the intended source, and distinguish a real load from a snapshot or injection.
- C64 Starfield `unit-17/Makefile` builds `steps/*.asm` using Asm198x's ACME dialect and PRG output. Select the actual step file; “unit 17” contains several cumulative states.
- NES Dash `unit-14/Makefile` uses Asm198x's ca65 dialect to produce `dash.nes`; its `run` target names FCEUX. That target does not establish an installed emulator or make it the required project capture route.
- Amiga Flock `unit-11/Makefile` uses Asm198x's vasm dialect to create the executable and Build198x to master an ADF; its `run` target names FS-UAE. Inspect those tool dependencies and the intended launch environment rather than assuming that assembling alone creates a bootable disk.

Use current tool help and the supported capture manifest contract when writing runnable instructions. Record versions/configuration for a reproducible exercise. A stale binary, missing asset or wrong checkpoint is a setup finding, not a reason to alter game logic until it appears to work. Do not revive retired development containers as the default build path.

## Staged revisit map

| Revisit / reason | Prerequisites and exercise | Evidence and learner outcome |
|---|---|---|
| **Local: Sonar 09**, a half-forgotten saved game | Fresh load, variables and subroutines. Locate latest-probe drawing, trace old/new cells, change `>` to `+` in line 2170 and explanatory text at 5060 in a copy. | Predict old-marker removal. Check two distinct probes, a repeated probe and retry: one marker, retained clues, no duplicate count. Explain why the grid logic did not need a rewrite. |
| Meet BASIC 11, revisited after Bright Spark | Calls and shared state. Compare the pre-extraction heading with the shared routine; identify caller position/colour assumptions. | Explain the existing refactor, test both call sites, and state why a general layout engine adds no value to this task. |
| Bright Spark 02/04/07 | Trace `p`, `lit`, note and blocking completion before a cue change. Use the already queued duration/fault experiment and repeated-replay checks. | A longer cue intentionally changes sound, panel duration and input opportunities. Classify it as behaviour change; diagnose a stale note or leaked state at its assignment/entry boundary. |
| Tail Chase 04 → 05/06 | Arrays, live occupancy, indices and update order. Revisit coordinate shifting versus circular storage with the same valid movement/growth cases. | Verify ordinary/wrapped body order and collision rules. This is a representation change intended to preserve rules, with altered copy work/storage; measure before claiming whole-game speed. |
| C64 Starfield 17 | Routine contracts, state transitions, nine-bit position and SID ownership. Locate `enter_game`, then use the planned missing-reset or high-bit fixture separately. | Explain which initialisation and renderer state matters before repairing it. A new wave requirement may justify a named shared entry job; one missing assignment calls for a local repair. |
| NES Dash 14 → 17 | NMI/main flow, controller state, transfer windows and audio updates. Trace where game over gates main and what the handler still does before adding retry/pause. | Map state ownership and dependencies; extend one lifecycle transition after the timing corrections. No claim that unit 14 already has complete replay/pause. |
| Amiga Flock 11 → 15/17 | Sample lifetime, `soundtick`, spawn routine and frame-counter mixing. Follow a cue from event through hardware request and countdown before changing priority or randomness. | Explain why changing one call site may affect articulation, repeatability or resource ownership. Use existing priority/seed experiments; do not make the current halt loop into a claimed OS return. |
| Crates 07/08 → Night Patrol prepared data | Authoring/stored/runtime formats and validation. Follow an edited map through conversion to consumed data; use the planned stale-output fixture. | Diagnose whether a wrong cell came from authoring, generation, loading or gameplay. Repeated hand-edit mistakes can justify the bounded converter; one typo does not require an asset framework. |

Use shared Foundations tracing/contracts as support, Pattern Library entries after their assumptions are checked, and Vault/hardware references when a disputed machine behaviour matters. A learner need not finish another platform to revisit their own game.

## Refactor versus change

Refactoring preserves a stated behaviour contract while reorganising implementation. A new marker, faster movement, different random-call sequence or longer cue changes behaviour even if the program still “works”. Optimisation often preserves game rules while intentionally changing execution cost; describe both, rather than hiding it under “cleanup”.

Preservation is broader than the final image. A change can alter input-sampling opportunities, sound duration, register/flag values, stack use, memory footprint, buffer lifetime, transfer order or a hardware deadline. State the budget and observable contract relevant to the game. Not every refactor must be byte-identical or cycle-identical, but changed time/space use must remain within the required bounds and be reported. For a cycle-sensitive beeper loop, instruction timing can be part of the sound itself.

Before extracting a routine, inspect its callers and clobbers; before sharing data, inspect who writes it and when it remains live. Keep structural work separate from a new rule where practical so a regression has fewer possible causes. Compare baseline and changed states with a known seed/input schedule or fixed scenario when randomness would obscure the comparison.

## Two decisions worth practising

**A local change is enough:** Sonar's latest marker is selected in one renderer line, with one instruction string explaining it. Keep the surrounding control/data flow intact. If another marker remains, investigate old-cell redraw; do not redesign the grid to solve a presentation fault.

**Repeated difficulty justifies restructuring:** Tail Chase repeatedly copies body coordinates as length grows; circular storage has a concrete motivation and a cost in index/wrap reasoning. Crates repeatedly needs reliable authored map validation; a small converter can prevent a class of mistakes. Ask which burden is removed and what new explanation/testing burden appears. Neither duplication nor abstraction is automatically wrong.

A later extension exercise must state the new requirement first. For example, a second independently timed Flock channel requires separate playback state, not merely another register address. Keep the previous single-channel version runnable while the new ownership is demonstrated. Do not add a general mixer in anticipation of unspecified future games.

## Verification and implementation order

1. **Authored locally now:** Sonar 09's baseline, code-location, prediction, marker-change and regression exercise. It preserves the original and distinguishes behavioural change from refactoring. No new native execution evidence or changed game sample is claimed.
2. **Authored locally: Tail Chase C08a.** Unit 05 adds a stopped-program straight-route inspection at moves 8, 9 and 12, with prediction, folded help and expected live coordinates. Unit 06 separates a representation-preserving change from the new growth rule, follows the existing diagnostic into a rejected body move, and checks repeated restart. The companion at `code-samples/sinclair-zx-spectrum/basic/tail-chase/teaching/comparison/` compares all 64 existing unit 04/05 movement/rejection records after checking source/tape hashes, then checks unit 06's common opening, growth and collision. `results.json` records the comparison. Slot indices are reconstructed, while body coordinates come from the retained ROM-execution traces. No new native run, speed measurement, hardware evidence or shifting-growth implementation is claimed. The temporary STOP/PRINT exercise remains to be independently executed; it intentionally changes timing and presentation. Ordinary source checkpoints are preserved.
3. Attach the existing Starfield, Dash, Flock and converter fault companions to this revisit method; do not create duplicate implementations or reorder their prerequisites.
4. Later Git/build diagnostics, resource-lifetime changes and timing-sensitive refactors require their concrete project tooling/calling contracts. No broad rewrite, universal architecture or advanced maintenance framework is commissioned.

Checks should catch meaningful failures: a two-line presentation change needs an inspected diff and relevant play observations, not a new test suite; a storage refactor needs state/boundary comparisons; an interrupt or DMA change needs target-specific timing/lifetime evidence. Keep authoring/static validation separate from native behaviour evidence and learner playtesting.
