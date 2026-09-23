# Abstraction and portability through game problems

**Status:** Progression and bounded porting proposals, with local Foundations Structure 02/03 edits and a worked mismatch exercise in the cross-platform sound pattern. No common engine, ported game or new hardware adapter has been implemented. Scope: Spectrum, C64, NES and Amiga.

Apply [curriculum design](../curriculum.md), [pseudocode conventions](../pseudocode.md) and the [Pattern Library contract](../pattern-library.md). Runnable machine sources belong in code-samples and lessons include them; schematic pseudocode is not a runnable release. Build on [data and tools](data-memory-tools.md), [timing](timing-and-interrupts.md), [ownership](scheduling-ownership-headroom.md), [diagnosis](testing-and-diagnosis.md) and [feedback](timing-and-player-feedback.md). This plan owns the teaching sequence for deciding what to share, not new implementations of those systems.

## Evidence and gaps

| Inspected material | Existing coverage | Gap and action |
|---|---|---|
| Foundations `structure/unit-02.mdx` and `unit-03.mdx` | Named routines, calls, parameters and returned values | Local edits now explain responsibility beyond reuse, useful duplication, a contract prediction exercise and pseudocode versus real calling conventions. |
| Spectrum Meet BASIC unit 11 | Two actual copies become one heading routine; caller supplies position/colour context | A good direct-first model. Retain it; no generic UI library needed. |
| Bright Spark units 02/04 and sample | `p`/`lit` inputs, renderer scratch variables, selected note, blocking cue and return-to-rest | Use its documented side effects and completion meaning before contrasting a hardware-generated sound. |
| Volley unit 05 and Touchdown unit 05 | Resolve candidates/accepted burn before presenting results | Existing boundary between rules and selected output; later isolate one decision for a table of checks, not the whole game behind interfaces. |
| C64 Starfield 17; NES Dash 11/14; Amiga Flock 11 | Event-driven sound, machine state and resource handling; the prior source audits identify actual routines and hardware review gaps | Compare contracts rather than flattening them into one instrument. Dash audio claims still need the queued source/fixture review. |
| Patterns `cross-platform/audio/making-a-sound`, `input/edge-detection`, `framework/state-machine` | Shared ideas with machine examples | Audio's “same driver everywhere” claim is locally removed and a completion mismatch exercise added. Edge detection needs explicit normalised bits, sampling assumptions and cost review before a runnable port lesson. State-machine hardware separation is already clarified locally. |

Existing architecture is deliberately game-led: direct samples, named responsibilities, specific machine patterns and shared conceptual descriptions. Explanation gaps include state/clobber contracts and completion semantics. Exercise gaps include a second implementation tested against shared cases. The new explicit teaching responsibility is evaluating a failed abstraction. A complete architecture rewrite is not needed.

## Seven stages

| Stage and motivating location | Prerequisite and smallest useful solution | Outcome and later need |
|---|---|---|
| 1. Name a repeated job: Meet BASIC 11; Foundations Structure 02 | Trace sequential work and return. Extract the identical heading, preserving caller position/colour assumptions. | Change one heading and inspect both callers. Explain why two unrelated small jobs might remain separate. |
| 2. State the contract: Foundations Structure 03 → Bright Spark 02 | Values, calls and shared variables. List input, output, changed state, preserved state and when work is complete. | Predict why printing a result does not substitute for returning it. Trace `p`, `lit`, drawing scratch and `note`; later assembly adds clobbered registers/flags and stack balance. |
| 3. Separate one rule from output: Volley 05, Touchdown 05; later Dash collision | Candidate state and conditions. Inspect the hit/miss or accepted-burn decision without rendering it. Feed a fixed case; let the existing renderer/audio consume the result. | Verify an edge contact or final fuel unit on paper, then in the game. No requirement for pure functions everywhere, heap objects or a universal event system. |
| 4. Data instead of repeated decisions: Bright Spark stored order, Crates 07/08; Starfield/Flock phrase data | Read a small list/table and trace its consumer. Share a sequence only when its meaning is stable. | Change an order without changing the cue routine. Explain why identical bytes can have different pitch, duration, tile or address meanings on another machine. |
| 5. Compare a concept: Starfield, Dash and Flock sound; Spectrum beeper then later AY | Understand each concrete implementation first, plus audio/timing fundamentals. Compare one accepted-event request and its lifetime. | Identify the common event meaning and the distinct instruments, budgets, ownership and completion contracts. Do not require four full tracks before making a two-system comparison. |
| 6. Port one small mechanic: input-edge companion after Meet Assembly input and Dash/Flock input | Boolean state, one sample per defined update and known input representation. Implement one newly-pressed rule twice with separate hardware readers; reuse a short input/state table. | Same logical sequence gives the same accepted presses. Explain why this does not prove identical physical latency or key/controller capability. Details below. |
| 7. Keep or change the boundary: Bright Spark cue versus hardware playback; later animation/graphics | A second implementation exposes a mismatch. Compare extending the contract, exposing a capability and separate implementations. | Choose with evidence: required behaviour, explanatory value, code/data size and measured runtime cost. Refusing a generic abstraction is a valid outcome. |

An abstraction earns its place through repeated logic, a clearer responsibility, a second implementation or a useful testing boundary. These are alternatives, not a requirement to wait for duplication in every case. Introduce the name only after the direct work is understandable.

## Contract cards, small enough to inspect

For one actual routine record: **given**, **returns/changes**, **preserves**, **completion**, **cost/limits**. Add ownership/lifetime only where relevant. Do not make beginners fill a long template for every subroutine.

Bright Spark's cue receives `p`, uses the renderer to choose `note`, changes the display and `lit`, waits through sound/restoration/pause, then returns. It is not merely “play pitch”. Flock's sample request sets hardware and software playback state whose later tick matters. Starfield's title/laser handover carries instrument state. Dash input is a controller read followed by interpretation. A familiar operation name does not remove those dependencies.

Foundations' local parameter names are a teaching convention. Sinclair BASIC shared variables and assembly registers/RAM need explicit calling conventions. A returned address also carries lifetime/placement assumptions; copying an address does not copy its content. Connect that case to the data and ownership plans when a game first passes asset pointers.

## A small port with a clear finish line

**Proposed companion:** extend the existing input-edge pattern after its assumptions are corrected, using a Spectrum Meet Assembly-derived isolated input fixture and a Dash-derived NES fixture. Flock supplies a later Amiga comparison; Starfield supplies a later C64 comparison. Do not change the shipped games' held-action rules just to demonstrate edges.

1. State the rule: a press event occurs when the current sampled action is true and the previous sampled action was false. At reset, previous is false. This definition deliberately counts an already-held button at the first sample; another menu may instead initialise from the first reading to require release first.
2. Keep the hardware reader separate. Each target supplies a normalised Boolean for one logical action. Explain its actual key/button mapping, pressed polarity, reads and changed registers. Multiple simultaneous buttons and keyboard rollover are outside this first contract; do not imply equivalent devices.
3. Hand-trace the same sequence before coding:

| Sample | Action held | Previous | New press |
|---|---|---|---|
| 1 | false | false | false |
| 2 | true | false | true |
| 3 | true | true | false |
| 4 | false | true | false |
| 5 | true | false | true |

4. Implement the small state update independently on both targets. Feed the logical sequence at defined update boundaries in an isolated fixture; inspect output/state through the verified debugger facilities. Then exercise each real hardware reader separately. Never label injected logical input as a tested physical controller path.
5. Check reset while held, a long hold, release/repress and an all-released sequence. A press entirely between samples cannot be recovered from those snapshots; no “zero latency” promise belongs in this interface.
6. Compare the rule and its tests, then count actual instruction/data costs including adapter work. Do not transplant the existing pattern's approximate cross-CPU cost table into the lesson. A shared algorithm need not mean shared source, binary or timing.

The core exercise finishes with two small implementations and the same logical traces, not a portable input package. Direct Boolean logic may be clearer than a dispatch table for one action. A later real need for remapping or several controls can justify a larger contract.

## The useful abstraction that becomes awkward

The local [Four Ways to Make a Sound](https://code198x.com/patterns/cross-platform/audio/making-a-sound/) exercise begins with `play_cue(id)` meaning “return when the cue has finished”. Bright Spark's caller then restores the panel and checks input. Ask learners to port it to a routine that starts hardware playback and returns immediately. Predict the panel lifetime before revealing the mismatch.

Evaluate three choices:

| Choice | What it preserves | What it costs or exposes |
|---|---|---|
| Keep a waiting wrapper for this memory game | Existing completion promise and simple caller | Input/other caller work still waits; hardware-generated sound does not make the wrapper non-blocking. |
| Introduce start/completion operations | Caller can do other work while supported playback advances | Explicit active state, service responsibility, cancellation and conflicting-request policy. CPU beeper generation needs actual scheduling work, not just a renamed call. |
| Share only cue meaning; retain separate routines | Each implementation can use its machine's strengths | More than one implementation to explain/test; appropriate where one generic promise would be misleading. |

Review questions: What does “finished” mean? Who advances time? Can another sound interrupt it? Is panel duration tied to sound or its own clock? What information is essential to the player? What evidence would justify a more complex contract? No option automatically wins.

Do not offer universal `waveform`, `attack`, `filter` and `sample` arguments with silently ignored values. Spectrum beeper CPU edges, SID oscillators/envelopes/shared controls, NES channel-specific facilities and Amiga sample channels have materially different meanings and costs. A capability may be exposed where the game can make a useful decision; dozens of capability flags are not a substitute for understanding four implementations. The audio plan owns detailed hardware verification and later AY coverage.

## The same care outside audio

- **Placing an object:** distinguish game position, drawing coordinates and hardware storage. Spectrum software drawing, C64 sprite state, NES prepared OAM/PPU transfers and Amiga sprite/bitplane paths do not promise the same immediate visible result or capacity. Compare actual game routines; do not write an invented universal `draw_sprite` timing guarantee.
- **Animation:** a sequence of artwork indices may be shared, while tile layouts, source bytes and transfer costs differ. Declare whether the index changes decoration or a gameplay hit window. A generic “advance” must name its clock and what happens at the end.
- **Memory:** inspect byte budgets, alignment, placement and reader lifetime at each target. An asset handle hides an address only if someone still honours its hardware constraints. Compact storage can add decoding work before a display deadline.
- **Timing:** identical update counts need not mean identical seconds or pitch. Preserve the chosen game rule and explicitly adapt the schedule; do not force variable delta time or an identical interrupt architecture on every system.

These comparisons reuse the established hardware references in the data/audio/timing plans. New snippets require source checking and execution under a named configuration. Tool source proves a facility, not machine accuracy.

## Implementation order and review

1. **Local now:** Foundations Structure 02 clarifies useful duplication/responsibility; 03 adds the contract prediction exercise. The sound comparison drops its identical-driver claim and adds the completion mismatch exercise. No game code changes.
2. **Next bounded implementation proposal:** correct the input-edge pattern's normalisation, sampling, per-bit Boolean and cost claims, then build the two isolated fixtures above. Also audit the sound pattern's existing illustrative snippets before reusing them: the SID register/waveform comments, setup assumptions and broad channel descriptions need their own hardware review. These are remaining gaps, not silently validated by this prose edit.
3. **Existing priority retained:** Bright Spark native cue work stays first in the active queue. Use its measured blocking contract for the later audio comparison; attach other exercises to existing game work rather than schedule four adapters at once.
4. Promote a checked game technique to the Pattern Library only when its contract and trade-offs are concrete. Link Foundations for concepts and Vault for sourced machine context, without requiring a prerequisite tour of either.

For each abstraction review, ask: What problem did it remove? Which assumptions became less visible? Can we state its inputs/state/completion? What meaningful test became easier? Is an exceptional case distorting the normal one? What is the actual time/space cost? Would two short explicit versions teach and serve this game better? Preserve both behavioural correctness and machine-specific understanding when answering.
