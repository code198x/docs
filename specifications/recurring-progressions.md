# Recurring progressions through games

**Status:** Curriculum map with source-reviewed existing coverage, local prose improvements and proposed exercises. The current implementation scope remains Spectrum, C64, NES and Amiga. These are recurring threads, not eight new modules, a uniform engine design or a compulsory shared prerequisite course.

[Curriculum design](curriculum.md) owns the teaching approach. The [audio](experiments/audio-progression.md), [timing](experiments/timing-and-interrupts.md) and [profiling](experiments/profiling-progression.md) plans own their detailed experiments and hardware/tool contracts. This map connects them to other game-making decisions; it does not duplicate their implementation plans. [Current work](../work.md) owns the active queue.

## How to read the audit

**Existing** means the named lesson body or sample was inspected, not merely a catalogue entry. **Explanation gap** means a working idea lacks a clear account or has misleading prose. **Exercise gap** means readers need a controlled comparison or diagnosis opportunity. **Topic gap** means a distinct teaching responsibility was not developed in the inspected route; it is not a claim that no related sentence exists anywhere in the repository.

Locations below use website `src/content/curriculum/<system>/<language>/<game>/unit-*.mdx`. Spectrum/C64/NES/Amiga stand for `sinclair-zx-spectrum`, `commodore-64`, `nintendo-entertainment-system` and `commodore-amiga`. Foundations lives at `curriculum/foundations/`; Pattern Library and Vault paths are relative to `src/content/`. Existing shared resources are connection candidates, not certified hardware authorities. Check their review flags, citations and assumptions before linking them from a new lesson.

The inspected anchors include Crates units 07–08, Tail Chase unit 05, Night Patrol unit 07, Meteor Storm units 06–08/11–12/19–20, Starfield units 05/08/17, Dash units 05/11/14/17, Flock units 03/11/17, Foundations Structure and From Source to Silicon, and the linked audio/timing/profiling audits. Later Starfall, SID Symphony, Catacombs, Maelstrom, Thunder Run and Onslaught placements are provisional catalogue homes, not completed courses or newly approved game briefs.

## 1. Data representation and development tools

The [data, memory and tools progression](experiments/data-memory-tools.md) owns
the detailed asset/build audit and converter exercises. Crates unit 07 now has a
local representation trace and storage explanation; its proposed converter and
the later asset-budget exercises remain unimplemented.

**Existing:** Crates turns map symbols into board values and checks malformed rows; Night Patrol encodes prepared visibility changes; Meteor Storm turns coordinates into addresses and record offsets. Foundations covers lists, bits and translation. The audio players already show notes and durations as data.

| Progression question | Concrete placement and teaching |
|---|---|
| First problem and prerequisites | Crates units 02/07: the picture must represent a room that rules can inspect. Need variables, indexing and a row/column convention. C64 Starfield, NES Dash and Amiga Flock meet the same need through object coordinates and target-specific graphics data. |
| Smallest useful solution | Keep one explicit representation and a worked example: map symbol → cell value → rule → drawing. Inspect one generated sprite/tile/sample asset and the source that produced it. Name source, converted data, executable and captured output as different artefacts. |
| Later need | Night Patrol unit 07’s prepared changes justify build-time conversion; Meteor Storm units 11–12 justify record layouts. SID Symphony/Thunder Run/Onslaught justify instrument and pattern data, validators and compact storage. Teach a converter only after readers understand one record it emits. |
| Observable understanding | Change one map or instrument value, predict its bytes and result, rebuild, then identify a deliberately stale output. Explain which file to edit and which to regenerate. A valid but wrong value must be distinguished from invalid data. |
| Connections | Foundations `structure/unit-01`, `working-the-bits`, `from-source-to-silicon`; Vault `techniques/variables-memory` and `memory-mapping`; Pattern Library `cross-platform/framework/escalation-as-data`. Link a concrete format/conversion pattern only after it has a maintained implementation. |

**Gaps:** explanation — build-time versus runtime cost and same-build source/debug information; exercise — trace one asset all the way to execution, then diagnose a stale conversion; topic — a short, repeatable build/provenance/validation workflow across the game’s files. Do not turn this into an IDE course or require a new toolchain.

## 2. Scheduling, shared state and resource ownership

The [scheduling and headroom progression](experiments/scheduling-ownership-headroom.md)
now owns the concrete seven-stage sequence and contention/overload exercises.
Flock unit 11 and Meteor Storm unit 12 have local trace/question improvements;
priority code, context handoffs and overload policies remain proposed work.

**Existing:** Meteor Storm unit 06 keeps an interrupt handler small; unit 12 explains register preservation in a nested loop. Starfield unit 17 hands a sound voice between title music and laser. Flock unit 11 replaces a sound on its single channel. These are useful contracts, not general concurrency solutions.

| Progression question | Concrete placement and teaching |
|---|---|
| First problem and prerequisites | A second task needs a resource already in use: a cue interrupts a note or a drawing routine changes a loop register. Need calls/returns, state and a trace of one update. |
| Smallest useful solution | One owner writes the resource; another routine requests work through an explicit parameter or event. State inputs, outputs and clobbered values. Explain Starfield’s envelope restoration and Flock’s current replacement policy before adding queues or priorities. |
| Later need | Dash unit 17’s NMI/main handoff, planned SID Symphony and Starfall players, and Onslaught sample/channel work justify bounded handlers, multi-field publication, priorities and safe restoration. The timing plan specifies each machine’s acknowledgement and interrupt rules. |
| Observable understanding | Omit one restoration in an isolated checkpoint, identify the changed value/owner, then repair it. Later force an interrupt between two request writes and demonstrate a consistent publication scheme. Explain what happens when two requests arrive. |
| Connections | Foundations `structure/unit-02` and `unit-03`; Vault `techniques/interrupt-driven-music` and `raster-interrupts`; patterns `cross-platform/framework/state-machine`, `cross-platform/audio/tune-sequencer` and NES `assembly/framework/nmi-game-loop`. |

**Gaps:** explanation — channel numbers do not cover shared filter/envelope ownership; exercise — repeatable shared-state fault and repair; topic — explicit request lifecycle, overflow and publication contracts at the later integration stage. No beginner locks, threads or general event bus.

## 3. Memory, data movement and bandwidth

**Existing:** Tail Chase unit 05 separates capacity from live length and reuses slots. Night Patrol updates changed visibility cells. Meteor Storm prepares shifted graphics and traverses fixed records. Dash unit 14 budgets PPU writes; Flock’s sample and sprite data have machine-specific placement requirements.

| Progression question | Concrete placement and teaching |
|---|---|
| First problem and prerequisites | More objects need storage, or drawing unchanged cells takes unnecessary work. Need arrays/records, addresses and a clear distinction between state and picture. |
| Smallest useful solution | Reserve a bounded array; visit live entries; redraw only the known changed area. Count bytes stored and bytes moved separately. Tail Chase’s twelve allocated slots do not imply twelve live body cells. |
| Later need | Meteor Storm units 11–12/20 and Night Patrol unit 07 motivate prepared data versus repeated work. C64 Catacombs/Maelstrom can compare screen/character updates; NES Thunder Run can compare queued PPU transfers; Amiga Onslaught can compare sample storage and DMA demand. Explain a buffer handoff before double buffering, and one explicit copy before compression or streaming. |
| Observable understanding | Predict the bytes and operations for a small update; compare with a full redraw. Fill a pool safely, identify its overflow policy, and show that the following record remains unchanged. Compare added RAM/ROM with saved work. |
| Connections | Foundations `structure/unit-01`, `counting-in-twos` and `working-the-bits`; Vault `techniques/screen-memory`, `memory-management`, `double-buffering`; existing platform rendering patterns after their assumptions are checked. A reusable transfer-budget pattern is proposed, not already claimed. |

**Gaps:** explanation — stored size, CPU instructions and bus traffic are different costs; exercise — a byte-movement ledger under a real deadline; topic — bounded transfer queues/backpressure and streaming only when later games need them. No assumption that NES PPU transfers, C64 screen writes and Amiga DMA are interchangeable.

## 4. Testing, diagnosis and experimental method

The [testing and diagnosis progression](experiments/testing-and-diagnosis.md) owns the detailed investigation sequence, tool limits and later game exercises. Foundations Structure unit 04 now has a local prediction and regression exercise; runnable game fault companions remain proposed.

**Existing:** Foundations Structure unit 04 traces an incorrect calculation. Meet Assembly unit 08 uses a guided debugger. Crates unit 08 has one-at-a-time malformed-map experiments and recovery. Maintained verification scripts provide production evidence, but their existence alone does not teach learners testing.

| Progression question | Concrete placement and teaching |
|---|---|
| First problem and prerequisites | The answer or game state differs from the intended rule. Need a simple input, expected result and enough state to inspect. |
| Smallest useful solution | Write one prediction, run a reproducible case, inspect the first mismatch, change one thing and repeat the original case. Keep Crates’ restored valid room as a control. Add one boundary case and explain why it differs. |
| Later need | Tail Chase wrap/occupancy, Meteor Storm pools and boost, Starfield waves and voice handover, Dash restart/grace windows, Flock sound retriggers justify regression scenarios and event schedules. The profiling plan adds measurement rather than replacing correctness checks with speed tests. |
| Observable understanding | Present a small failing input/state, distinguish an invalid test expectation from a program fault, demonstrate the repair and rerun a formerly passing case. A screenshot is evidence of appearance, not proof of every game rule. |
| Connections | Foundations `structure/unit-04`, decisions and trace tables; Vault `techniques/collision-detection` for checked historical context; patterns `cross-platform/physics/aabb-collision`, `framework/lfsr-random` and `physics/grace-window`, tested against their stated assumptions. |

**Gaps:** explanation — production automation versus a learner’s hypothesis; exercise — keep a short regression table through two lessons; topic — reproducibility of random/input-driven cases and failure reduction as explicit later skills. Introduce invariant/property language only after concrete examples such as “a live crate still occupies one cell”.

The [randomness and reproducibility progression](experiments/randomness-and-reproducibility.md) develops fixed choices, seed/call-order diagnosis, mapping bias and deterministic scenarios. Bright Spark and Flock have local explanation exercises; native fault fixtures and replay remain proposed.

## 5. Simulation timing, presentation and responsiveness

The [timing and player feedback progression](experiments/timing-and-player-feedback.md) connects this thread with perception below. Local Bright Spark 04, Touchdown 05 and Game Feel 01 additions explain timing/feedback choices; later runtime comparisons and native trials remain proposed.

**Existing:** Meet Assembly unit 07 distinguishes update opportunities from moves. Meteor Storm units 17/19/20 separate elapsed time, boost steps and drawing. Dash and Flock introduce pacing and input. Local Game Feel controls lessons compare immediate motion, acceleration, braking and reversal; they remain local review material, not evidence of native timing.

| Progression question | Concrete placement and teaching |
|---|---|
| First problem and prerequisites | A held key repeats too quickly, a cue delays input, or movement changes when drawing becomes expensive. Need input/state/update and one known clock. |
| Smallest useful solution | One defined update cadence, an explicit held-versus-new-press rule, and a count of when input is sampled and state changes. Do not begin with variable-delta integration or interpolation. |
| Later need | Meteor Storm unit 20 justifies several rule checks per image. Dash’s music companion, Starfield/SID Symphony and Flock/Onslaught justify separate player/display schedules and latency measurements. Use interpolation only for a concrete presentation need, without changing authoritative collision state. |
| Observable understanding | Run a fixed input schedule with added drawing cost; report game-state updates, displayed frames and input-to-state delay separately. Explain why one render per two simulation steps does not mean one collision check per two steps. |
| Connections | Foundations `from-source-to-silicon/unit-05`; Maths fixed-point applications; Vault `techniques/fixed-point-math` and `double-buffering`; patterns `cross-platform/input/edge-detection`, `physics/fixed-point-math`, Amiga `assembly/framework/vblank-game-loop`. |

**Gaps:** explanation — polling is not a deadline guarantee; exercise — measure a named response boundary; topic — bounded catch-up, interpolation and latency budgeting for later games. Follow the timing plan rather than introducing all four clocks and interrupt machinery in the first movement lesson.

## 6. Perception and game feedback

**Existing:** Bright Spark combines an asterisk, brightness and sound; Night Patrol marks visible cells. Starfield and Dash distinguish cues and outcomes; Flock changes pitch and articulation for events. Existing grace-window/ending-dwell patterns discuss communicating rules, with assumptions that need review.

| Progression question | Concrete placement and teaching |
|---|---|
| First problem and prerequisites | The player cannot tell what happened or which action is available. Need an event and its intended meaning; musical or artistic expertise is not required. |
| Smallest useful solution | Give one important event a readable visual cue and, where appropriate, a distinct short sound. Compare alternatives with one property changed. Preserve an alternative when sound or colour is unavailable. |
| Later need | Night Patrol units 05–08 connect warning and visible threat; Starfield/Dash ending and protection cues connect feedback to rules. Flock retriggers and the later audio arrangements motivate competing cues, silence, priority and fatigue. |
| Observable understanding | Ask someone to identify the event before explaining it, then test the cue during busy play and with sound muted. Distinguish “louder/more animated” from “more informative”; explain why an alert masks another cue. |
| Connections | Foundations decisions/state; Craft Game Feel, Game Design and Sound and Music; Vault `techniques/sprite-animation` and sound-driver context; patterns `cross-platform/physics/grace-window`, `rendering/blink-on-a-clock`, `framework/ending-dwell`. |

**Gaps:** explanation — implementation correctness does not establish communicative success; exercise — cue comparison under competition and without one sensory channel; topic — a systematic feedback-priority/accessibility review in later integration. Do not equate player perception with the guard’s Game AI perception; connect them when readable behaviour is the actual question.

The [state, lifecycle and recovery progression](experiments/state-lifecycle-and-recovery.md) connects state ownership, transition entry/exit, pause domains and repeated restart to these threads. Bright Spark 07 has a local replay exercise; later game fault fixtures and environment-specific cleanup remain proposed.

The [existing-code revisit progression](experiments/working-with-existing-code.md) applies these threads to saved projects. Sonar 09 has a local baseline/trace/change exercise; later refactor comparisons reuse the actual Tail Chase, Starfield, Dash and Flock checkpoints.

## 7. Abstraction and portability

The [abstraction and portability progression](experiments/abstraction-and-portability.md) owns the detailed contract, two-target input exercise and sound-completion mismatch. Foundations Structure 02/03 and the sound comparison have local prose exercises; machine fixtures remain proposed.

**Existing:** Foundations names routines and parameters; games separate rules, drawing and sound to varying degrees. Cross-platform patterns reuse state-machine, edge-detection and sequencer ideas. From Source to Silicon unit 04 contained misleading universal claims about diagnostics and portability; it is corrected locally in this pass.

| Progression question | Concrete placement and teaching |
|---|---|
| First problem and prerequisites | Two callers repeat the same job, or changing a drawing routine accidentally changes a rule. Need one working concrete routine, parameters and its observable result. |
| Smallest useful solution | Name a job and its contract: for example “draw this cell” or “request this cue”. Keep the implementation specific and inspectable. Do not start by inventing a universal engine or hardware abstraction layer. |
| Later need | Compare Crates’ board/rules with the planned NES Crate Escape only when that project is briefed. Compare existing Starfield, Dash and Flock phrase data after each implementation is understood. Share a trace or data schema only where its meanings and timing contracts match. |
| Observable understanding | Sort a small program into transferable rule, representation assumption and hardware operation; port one rule using identical test cases, then explain why input/display/audio code differs. Reusing an instruction set is not proof that a whole binary runs on another computer. |
| Connections | Foundations `structure/unit-02`, `unit-03`, `from-source-to-silicon/unit-04`; Vault `techniques/memory-mapping`; patterns `cross-platform/framework/state-machine` and `audio/making-a-sound`. Review universal “same everywhere” wording before using a pattern as evidence. |

**Gaps:** explanation — algorithm, source and executable portability; exercise — contract comparison across two existing implementations; topic — adapters and data-format versioning only after a real second consumer or incompatible format appears. Independent system entry remains intact.

## 8. Performance headroom and graceful degradation

**Existing:** Meteor Storm unit 12 flags pool overflow and safely refuses an out-of-capacity spawn; unit 20 measures a budget. Audio work exposes competing channel demands. These are beginnings, not a complete headroom or degradation policy.

| Progression question | Concrete placement and teaching |
|---|---|
| First problem and prerequisites | A bounded resource is full or a busy scene misses a required deadline. Need a measured baseline, live/capacity distinction and the game’s essential rules. |
| Smallest useful solution | Detect the limit, remain within bounds and report it. In Meteor Storm’s pool experiment, refusing a spawn is memory-safe but can change difficulty; do not silently ship it as an equivalent optimisation. Keep the flag observable. |
| Later need | Meteor Storm’s profiling companion establishes normal/busy margins. C64 Maelstrom, NES Thunder Run and Amiga Onslaught can justify reserving time/capacity and dropping decorative requests. Starfall can prefer a warning over an optional musical part, using the audio ownership policy. |
| Observable understanding | Replay a worst-observed scene plus a controlled burst, state the margin and count dropped/deferred requests. Compare normal and fallback output: scoring, collision, essential warnings and input handling must retain their promised behaviour. Explain any deliberate design change. |
| Connections | Foundations decisions and finite representations; Vault `techniques/memory-management`, `sprite-flicker` and checked sound-driver context; patterns `cross-platform/framework/three-caps` and state-machine. A general overload-policy pattern is a proposed extraction after a real game demonstrates it. |

**Gaps:** explanation — average speed and safe capacity are not headroom; exercise — controlled resource pressure with an explicit fallback; topic — prioritised degradation and bounded recovery as a recurring design responsibility. Avoid an arbitrary “20% spare” rule, silent lost gameplay events or unlimited catch-up queues. Reserve a measured margin for a named burst and revise it with evidence.

## Prerequisite order and system differences

Use this order within a thread: **concrete event/data → one routine → observable state → bounded resource or clock → measured pressure → justified refinement**. Explain essentials locally. Foundations links are optional depth, not attendance requirements.

- Do not teach queues before two requests can conflict, interrupts as a music scheduler before a player update is understood, or double buffering before a reader has seen who reads and writes one buffer.
- Do not teach compression before a representation can be inspected, caching before repeated work is measured, portability layers before comparing concrete interfaces, or fallback policies before defining essential behaviour.
- Spectrum beeper consumes CPU waveform time; later AY introduces different ownership. C64 raster/CIA and shared SID controls differ from NES NMI/PPU transfers and unequal APU channels. Amiga DMA, Chip RAM and Copper coordination require their own contracts. Reuse questions and evidence formats, not register code or an identical architecture.
- Preserve the current beginner routes and the agreed Craft module homes. Advanced buffering, streaming, sample interrupts, general allocators, adapters and host profiling remain later depth. The four local Game Feel lessons and planned later games retain their actual review/implementation status.

## Prioritised implementation sequence

[Current work](../work.md#curriculum-implementation-queue) owns the consolidated execution order and completion criteria. Its lettered checkboxes are independently reviewable delivery chunks; the C numbers group related work, not indivisible releases. It combines these threads into bounded game tasks: Bright Spark first, prerequisite accuracy repairs, then Crates, Meteor Storm, Flock and Starfield companions, followed by targeted transfer work. The detailed progression documents retain prerequisites and later possibilities; they are not competing task queues.

Local prose improvements are authored, not evidence that the runnable companions or native trials are complete. Preserve the current game lineup, independent entry routes and deferred BASIC performance scope. There is no requirement to finish every progression before a useful lesson can ship.

Further audit remains: neighbouring From Source to Silicon units may share the over-broad “translation means speed” framing; shared audio patterns and Vault articles need source/voice review; no systematic learner-facing bandwidth, publication-race or degradation exercise is yet claimed. Their locations and entry conditions are above. There is no requirement to finish all eight threads before the next game lesson can ship.
