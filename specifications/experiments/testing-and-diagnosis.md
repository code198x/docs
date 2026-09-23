# Testing, diagnosis and experimental method

**Status:** Source-audited progression; Foundations Structure unit 04 has a local prediction exercise and revised investigation guidance. Later game exercises below are proposals unless identified as existing. No new debugger, test framework or broken game checkpoint has been implemented. Scope: Spectrum, C64, NES and Amiga.

This develops [recurring progressions](../recurring-progressions.md#4-testing-diagnosis-and-experimental-method). [Profiling](profiling-progression.md) owns measurement facilities and cost attribution; [timing](timing-and-interrupts.md) owns clocks and interrupt contracts; [scheduling](scheduling-ownership-headroom.md) owns handoff and overload experiments; [data and tools](data-memory-tools.md) owns converters and asset validation. We add an investigation method to those tasks rather than duplicate them.

## What exists, and what is missing

Paths below are relative to website `src/content/curriculum/`, unless stated otherwise. Matching runnable projects live in the code-samples repository.

| Inspected material | Existing coverage | Gap addressed here |
|---|---|---|
| `foundations/structure/unit-04.mdx` | Incorrect doubling calculation, visible values and paper trace | Previously disclosed the repair immediately and overstated what a mismatch proves. Local edit now asks for discriminating inputs, contrary evidence and regression checks. |
| `sinclair-zx-spectrum/assembly/meet-assembly/unit-08.mdx` and `DebuggerLesson.astro` | Reproduction, competing hypotheses, selected breakpoints, actual stepping, registers/RAM, two isolated fault sources and folded explanations | Reuse its method; do not replace it with a checklist-heavy debugger. Later lessons need opportunities to choose the observation without being told the fix. |
| Spectrum BASIC Crates unit 08 | One-at-a-time malformed rows/symbols/player counts, restore-and-rerun, structural validity versus solvability | Add a learner-selected discriminating case and a small retained regression table. The tests and validator already exist. |
| Spectrum BASIC Tail Chase unit 05 | Twelve storage slots versus four live cells; index wrap separate from world coordinates; stale-slot question | Turn the suggested repeated movement into a precise boundary trace with a failing variant and repair evidence. |
| C64 Starfield unit 17 and its sample capture recipes | Reproducible parked-player exploit, spread/hunt repair, nine-bit positions, BCD score growth and SID restoration | Ask for predictions before fixes. Separate rule correctness, numeric representation and game design claims; one losing run does not prove every safe strategy is gone. |
| NES Dash unit 14 sample; Amiga Flock unit 11 sample | Main/NMI flag and register preservation; explicit sound request/countdown routines | Isolated state/interrupt/calling-contract investigations, after learners understand the unmodified code. |
| Meteor Storm `verification/checkpoints.py` and the existing profiling plan | Maintained execution checks and bounded pool/timing experiments | Production scripts are evidence for authors, not automatically a learner lesson. Extract one question, not the whole verification infrastructure. |

The main gaps are **exercises and explanations**. Explicit deterministic reproduction, failure reduction and evidence arbitration are the later **teaching topics** to develop. Assertions, tracing and tests should answer a concrete question before acquiring a formal name.

## The recurring investigation

Use a short notebook entry or table, not a form that must be completed for every typo:

1. **Expected / actual:** name the rule, starting state and observed difference. Distinguish state, picture, sound and timing.
2. **Reproduction:** reset to a known checkpoint and repeat the smallest input sequence that still reveals it. Record the loaded build and relevant configuration.
3. **Hypothesis:** make a specific causal claim, such as “the wrap check rejects the last valid slot”, rather than “the array is broken”.
4. **Prediction:** state an observation that would support it and one that would contradict it. Decide where to observe before running.
5. **Experiment:** change or measure one relevant variable. Keep a working control; record instrumentation that may affect timing.
6. **Interpretation:** compare actual evidence with the prediction, including the possibility of a mistaken expectation or test fixture. Revise the hypothesis if necessary.
7. **Repair and regression:** address the cause, repeat the original failure, then repeat meaningful neighbouring and formerly passing cases. Explain why the change works.

Observing the first wrong value narrows the search; it does not always identify the cause. A corrupted register may have been damaged by an earlier call. A late sound may reflect delayed servicing rather than a faulty instrument. A screenshot cannot establish hidden state, and a pleasant sound cannot establish correct note duration or channel restoration.

## Progression through existing projects

| Stage and location | Prerequisites and bounded exercise proposal | Observable learner outcome |
|---|---|---|
| Visible values: Foundations Structure 04; recall locally in early BASIC | Input, arithmetic and output. **Local exercise implemented:** compare doubling with adding two for 5, 2, 0 and -3; predict before tracing. Two accidentally passes both expressions. | Explain why a passing example may fail to distinguish hypotheses; repair only the expression and retain four checks. No framework or machine knowledge required. |
| Boundaries and validation: Crates 08; Tail Chase 05–07 | Strings/arrays, loops, valid indices and live-cell rules. Choose short/exact/long rows; then trace slots 11, 12, 1 and distinguish stale storage from live occupancy. Create a labelled copy with one altered wrap comparison, not a fault in the working checkpoint. | Locate the first invalid or prematurely wrapped index; check both ordinary and wrap movement after repair. State that accepted map structure does not prove solvability. |
| Isolated routines and invariants: Meet Assembly 08 → Meteor Storm 12 | Calls, flags, memory and bounds. Use the existing movement faults first. Later check active-count ≤ capacity and refusal behaviour at empty, last-free and full pool states. A debug-only check may set a diagnostic byte and stop at a known safe point. | Distinguish bounds safety from correct hazard delivery; explain the invariant and the observation that violates it. Assertions must not silently clamp away the evidence. |
| Representation: Starfield 17; Meteor Storm byte-boundary drawing | Bit/byte representation and the actual comparison instruction. Compare positions just below/at/above 255 and scores around decimal carry. In a separate routine fixture, compare the same byte under signed and unsigned interpretations before choosing a branch. | Trace stored low/high parts, carry and interpreted value separately. Do not call BCD wrap, binary carry and signed overflow the same event; verify expected instruction flags against the CPU manual. |
| State transitions: Starfield 17, Dash 14/17, Flock 11/17 | Named states, entry/exit actions and sound ownership. Reset; title → play → result → retry with a recorded input schedule. Predict instrument/timer/score state on the second visit, not only the first. | Reveal stale state or an unintended transition; retain a transition table that checks restart and accepted/rejected requests. Link to the existing state-machine pattern. |
| Register and stack contracts: Meet Assembly calls → Dash 14 and Flock 11 | Return addresses, caller/callee contract and push/pop order taught first. In an isolated bounded call fixture, deliberately omit one required register restore; inspect the caller before and after. A later stack fixture pairs each save/restore and compares the stack pointer at equivalent boundaries. | Identify which value the caller needs preserved. Repair the contract and check another caller. Do not require every register to remain unchanged or corrupt a running game's return stack as the first demonstration. |
| Interleaving and deadlines: Dash 14/17; C64 CIA/raster work; Spectrum IM 2; later Amiga timer/DMA work | An understood playback update and the timing plan's interrupt introduction. Reuse the scheduling plan's forced intermediate-state and read/clear interleavings; use Meteor Storm 20's bounded expensive-path fixture for deadline diagnosis. | Predict a specific mixed state or missed service boundary, distinguish it from hardware sustain, and show the repair under the same schedule. Pausing/stepping can change the timing being investigated. |
| Files and assets: Crates converter → Night Patrol; Starfield sprites, Dash tiles, Flock samples | Authoring/stored/runtime representations and the consumer's actual layout. Reuse the data plan: malformed row, invalid symbol, stale output; later wrong byte count or placement in a separate asset fixture. | Report a useful error before consumption, identify the first wrong conversion stage, regenerate and compare consumer data. Round-trip tests only when recovery of the source is intended. |
| Minimal hardware experiment: later machine-specific timing/audio investigation | Register contracts, a reproducible disagreement and bounded capture. Reduce to one disputed register/timing operation, preserving the trigger, then compare documented behaviour, emulator observations and available hardware results. | State exactly what the test establishes for the named model/region/revision and what remains unknown. Do not require access to real hardware to complete the beginner route. |

Foundation links are support, not attendance prerequisites. Recall each method in the game that needs it. Vault sources provide historical/hardware context; consult the relevant CPU/chip source rather than treating a game lesson as hardware authority. Pattern Library candidates—bounds guards, state transitions, LFSR sequences and grace-window rules—should gain small counterexamples only after their game implementation is checked. Avoid a generic testing module that delays making the first game.

## Use the tools we actually have

The [profiling capability audit](profiling-progression.md#verified-tool-surface-and-limits) owns the wider tool inventory. This pass rechecked `DebuggerLesson.astro` and Emu198x `crates/emu198x-shell/src/mcp_tools.rs`; these are source checks, not execution of every native tool build.

- The Spectrum lesson UI supplies selected label stops, stepping, memory/register readings and recent steps. It does not expose an arbitrary watchpoint or conditional-expression interface.
- The shared native tool registers `run_until_mem_change`: it steps whole instructions until a watched byte changes, with a step limit. Teach this as a **bounded value-change watch**, not a bus-access watchpoint. A write of the same value is not a change, and intermediate accesses within a step are not established by that interface. Start with ordinary RAM, not registers whose reads have side effects.
- Shared PC/any-PC stops and bounded step observations can isolate a routine. A scripted predicate check at a stop is not a native conditional-breakpoint facility. “Budget exhausted” does not mean the expected instruction executed.
- The previously audited Spectrum cycle profiles and Amiga bounded CPU traces are later tools. Record truncation, timestamp resolution, guest versus host timing, tool build and relevant capability. Do not invent equivalent facilities on every machine.
- Existing sample capture scripts and Meteor Storm verification provide authoring precedents for deterministic runs. Before giving learners commands, execute the selected fixture with the selected tool version and document how to reset, stop and restore it.

For deterministic experiments, record the program/asset identity, machine model and region, initial state or seed, and inputs at defined **guest** update boundaries. A seed alone is insufficient if random calls or input sampling occur in a different order. Keep the fixed reproduction and add a second meaningful case; one fixed sequence is not broad coverage. Reduce an input recording by removing sections only while checking that the original failure remains.

## When evidence conflicts

Separate intended game rules, CPU/language semantics and hardware behaviour. An emulator can accurately run an incorrect game, and a game can look correct while relying on inaccurate emulation. Agreement among emulators that share an implementation is not independent confirmation.

Record the exact conflict, consult the original manual/datasheet and applicable errata or sourced hardware research, then build the smallest focused program that distinguishes the competing explanations. Compare real hardware results when available, naming configuration and measurement method. Retain conflicting observations and unresolved limits; do not change an expected result merely to make a test pass. The timing plan's cited Zilog, MOS and Commodore manuals and public NES research remain the hardware references for later fixtures. No new hardware timing claim is introduced here.

## Bounded implementation sequence

1. **Authored locally now:** Foundations Structure 04 prediction, interpretation and regression exercise. This is a paper/pseudocode exercise; no native execution or new sample is claimed.
2. **Authored locally, C04a:** Crates unit 08 now has a hidden-answer prediction and three-case learner record (valid row, short row, unknown symbol). The learner chooses evidence to distinguish length validation from symbol validation, then repeats the restored valid room. Existing runnable code is unchanged; no converter dependency. See the evidence section below.
3. **Then boundaries/representation:** a separate Tail Chase wrap fixture and Starfield right-edge/score comparisons. Preserve each working checkpoint and give an explicit reset/recovery instruction. Learners explain the evidence before revealing the repair.
4. **Attach later work to existing tasks:** Flock ownership, Dash timing/handoff, Meteor Storm profiling and the Crates converter use the method above. Bright Spark remains the already queued first implementation; these tasks do not reorder that agreement.

For every runnable fault companion, acceptance requires a reliable original failure, a prediction that distinguishes plausible causes, a bounded isolated fault, the smallest explained repair and at least one regression case that could catch a meaningful mistake. Keep corrected working samples intact. A trivial prose edit needs editorial checks; a tiny arithmetic example needs a checked trace; a stateful game repair needs targeted behavioural evidence. Scale the checks to the risk, not to the availability of a test runner.


## Input-edge pattern checks

C03b corrects `website/src/content/patterns/cross-platform/input/edge-detection.mdx`
locally, ready for review. The prerequisite is a machine-specific reader returning
normalised pressed bits, not raw hardware polarity. All consumers use one stored
sample per update. The entry policy seeds history from the current controls to
suppress inherited press edges while retaining held-state information.

Author arithmetic checks executed with Python on 22 September 2026:

- All 65,536 previous/current byte pairs: `current & (~previous & 255)` agrees
  with the Boolean just-pressed test for each of eight masks (524,288 checks).
- Seed $10; samples $10, $18, $08, $18: edge bytes $00, $08, $00, $10.
- Double-tap first press at update 0: no dash; second at 14: dash; second at 15:
  no dash. These are separate cases with fresh state.
- Presses at 0 and 300: no false match after timer expiry. Presses at 0, 2, 4:
  only update 2 dashes, since the pair is consumed. Each press edge presumes an
  intervening released sample, not merely continued holding.

The core exhaustive check is reproducible without test infrastructure:

```python
for previous in range(256):
    for current in range(256):
        edges = current & (~previous & 255)
        for bit in (1, 2, 4, 8, 16, 32, 64, 128):
            assert bool(edges & bit) == (bool(current & bit) and not bool(previous & bit))
```

This verifies the stated logic and traces, not assembled 6502/Z80 execution,
hardware readers, physical input latency or switch debouncing. Assembly fragments
state their supplied-reader and register-use contracts. No game sample changes.
A separate learner trial of the folded prediction remains pending. C11 can use
this corrected contract when developing the input-response experiment.


## Crates three-case diagnosis

C04a is locally authored, ready for review in
`website/src/content/curriculum/sinclair-zx-spectrum/basic/crates/unit-08-check-a-room-before-playing.mdx`.
The existing mistakes table becomes a guided three-case experiment with a folded
hint and explanation. Other validation cases remain optional, with answers folded.

The learner changes only DATA line 8010: valid `#------#`, short `#-----#`, and
unknown symbol `#--X---#`. They predict before execution, record the error and
row, and distinguish rejection by the loader from a drawing fault. The length
check at 4015 stops the seven-character case; the symbol check at 4095 stops X
at row 2, column 4. The existing screen reports the row only. Line 21 prevents
partially loaded data from entering play.

Recovery is concrete: restore `8010 DATA "#------#"`, RUN, S, inspect the initial
room, make a legal move and restart with R. Repeat the valid control between the
faults and at the end. Explain why the two errors reach different checks despite
sharing the reported row. This is the observable learner outcome; the converter
remains separate C04b work.

Verification on 22 September 2026 compared the current unit-08 source with
`code-samples/sinclair-zx-spectrum/basic/crates/teaching/verification/results.json`:
SHA-256 `f0ed96fee254f1a981d7ab3a3f651521c8ce1aeef4aecb89445b8f6a6da3531a`
 matches its passed validation checkpoint. That retained evidence names Emu198x
0.25.0, 48K ZX Spectrum PAL, ROM entry and tape save/load. Its `verify.py`,
`invalid_maps`, uses the exact short and X rows and restores edited DATA after
each case. The source/data text is unchanged in this delivery.

This pass also checked the three row lengths/symbol classifications and X's
column by direct arithmetic. Existing native results are reused, not represented
as a fresh emulator run. No original-hardware check or learner trial is claimed.
The usual website build/render checks cover the authored exercise; learner
feedback on predicting and selecting evidence remains pending.


## Early reasoning and handover review

R2's five-page local review covers Foundations Structure 02–04, Meet BASIC 04 and Sonar 09. These are refinements to authored material, not five new lessons or publication approval.

- Structure 02 asks learners to predict which callers change before revealing the shared-routine explanation. Unknown names are described as a contract/error problem, not guaranteed silent failure.
- Structure 03 distinguishes returned values from display effects; a missing argument does not acquire an invented empty value. Its local-name explanation matches the pseudocode specification, with the BASIC distinction explicit.
- Structure 04's diagnosis retains prediction before repair and contrary evidence. The trace now defines `prices = [10, 25, 5]`, matching totals 10, 35, 40. The conclusion no longer claims to cover every programming idea.
- Meet BASIC 04 says how to retain the readable listing, including learner edits, alongside the TAP. Fresh loading and required completion checks remain separate from optional additions.
- Sonar 09 marks the maintenance exercise as an optional revisit. Source inspection confirms marker/reset/clue responsibilities at the cited lines. The exercise now handles an early winning probe before the two-cell comparison.

The unchanged source identities match retained execution records: Meet BASIC `opening/unit-04/steps/step-02.bas` is SHA-256 `de9441df7468db77bc3366abb7d293caf8d9f0804c600cf4f8470cb5b72fd965`; Sonar `teaching/unit-08/steps/step-01.bas` is `7d481c35247c4bed8e9965a5e46ff4218ba4162c4330059abc638ef5bb467b7b`. Existing story evidence includes a fresh-process tape reload. This review did not repeat native execution, run the changed Sonar marker variant, test original hardware or recruit a learner.

Local validation: the 2,468-page Astro build, route/template-whitespace checks and lesson prose links pass. All five pages pass 390/1280px, light/dark browser checks (20 combinations): the selected explanations open by keyboard, source includes resolve, and no page-level horizontal overflow appears. Representative desktop/mobile screenshots were inspected. These checks establish local rendering, not user approval or a complete accessibility audit. The optional Sonar variant still needs execution evidence before a claim that it has been verified by running it.


## Shared-pattern review

R4a reviews existing edits in `patterns/cross-platform/input/edge-detection.mdx`, `framework/state-machine.mdx`, `framework/lfsr-random.mdx` and the previously corrected portions of `vault/techniques/random-numbers.mdx`. This is a focused review, not a claim that the whole Vault article or all assembly fragments have been verified.

- The input entry explanation distinguishes a startup read from reusing the already sampled state during a transition. It retains separate pressed bits, held state and history ownership.
- The state pattern now asks for the eight-update restart/pause trace before revealing the result. Transition priority, pause responsibilities and the existing initial state are retained.
- The LFSR pattern no longer claims to be taught in Maths for Games unit 6 (the authored unit is Place a point). Its timing-based seeding example explicitly waits for an update opportunity, reads Start, wraps to a byte and documents repeated seeds. An unexpected zero after initialisation is a diagnostic fault, not a reason to silently reset the generator.
- The adjacent partial-shuffle text now identifies the final selected slots. Unique selection warns that a full set cannot satisfy a retry and calls for an explicit exhausted result or bounded alternative. No random generator or game algorithm was changed.

Host arithmetic checks pass: 524,288 per-bit comparisons over every pair of input bytes; the right-shift `$B4` LFSR's 255 non-zero states; masked-nibble counts (zero 15 times, each other nibble 16); uniform-byte modulo-six counts (43/43/43/43/42/42) and rejection counts (42 each). Byte seed counters at 1/255/256/257 map to 1/255/1/1. Enumerating all 12 choice paths in a four-item/two-draw partial shuffle gives each ordered pair exactly once in the last two slots. These are arithmetic checks, not proof that a particular BASIC random source supplies independent uniform choices. Earlier C03 logic evidence retains its original scope; no new native run or learner trial is claimed.

Local validation: the isolated-output Astro build passes all 2,468 pages after the shared-output build failed on a missing generated Unity Vault chunk. Route and template-whitespace checks pass. The four reviewed pages pass 16 desktop/mobile, light/dark browser combinations, with keyboard reveals where present and no page-level overflow; representative screenshots were inspected. The transition-policy anchor resolves and the stale taught-in attribution is absent. This is not a full accessibility audit or publication.
