# Scheduling, ownership and headroom

**Status:** Focused progression with local lesson improvements and bounded native ownership/scheduling companions; further applications remain proposed. No general scheduler or queue is implemented. Current scope is Spectrum, C64, NES and Amiga.

This develops [recurring progressions](../recurring-progressions.md) through the existing [audio](audio-progression.md), [timing/interrupt](timing-and-interrupts.md), [profiling](profiling-progression.md) and [data/memory](data-memory-tools.md) work. Those plans own hardware setup, capture tools and asset lifetimes; this plan owns the ordering of scheduling concepts and the decisions made when work conflicts or exceeds capacity. It introduces no new standalone module or common engine framework.

## Existing evidence and immediate edits

The audit inspected Flock unit 11's full `playsound`/`soundtick` implementation and call sites; Dash unit 14's main/NMI code; Meteor Storm unit 12's pool lesson; and the existing timing/resource plans. Website paths are relative to `src/content/curriculum/`; samples use the matching `code-samples/<system>/assembly/<game>/` paths.

- **Amiga Flock unit 11, local prose edit:** replaces “newest wins is correctness” with an explicit replacement policy. A worked baa/bleat conflict traces actual period, timer, halfway and volume values; reversing the request order changes the surviving cue. It distinguishes hardware voices from separate playback state and removes the claim that DMA sound costs nothing. This is an authored trace exercise, not a new priority implementation.
- **Spectrum Meteor Storm unit 12, local question:** distinguishes safe refusal of a spawn from preserving the game. The existing one-slot experiment consumes a failed spawn's event, so its missing hazard changes the challenge. No game code changed.
- **NES Dash unit 14, existing source:** NMI preserves A/X/Y, performs OAM/HUD/text work and sets `nmi_flag`. Main waits for the flag then clears it. This is a useful simple handshake, not a count of all elapsed frames. NMI can occur between main's read and clear, so the later overload exercise must expose the lost-notification case rather than describe the flag as a reliable backlog.
- **C64 Starfield unit 17, existing audio audit:** title music and the laser share a voice with explicit instrument handover. SID Symphony remains the later proposed home for an interrupt-driven player and arbitration.

## Seven stages, each earned by a game problem

| Stage | First concrete problem and prerequisites | Smallest useful solution and outcome | Later application |
|---|---|---|---|
| 1. Predictable sequential work | Flock has several sound-triggering events before `soundtick`; Starfield and Dash have small phrase updates. Need routine calls, state and a trace. | Write the order of calls and state changes. Predict which request is last and what the next tick reads. No interrupts or queue yet. | Spectrum beeper note/input alternation; Meteor Storm simulation then drawing. |
| 2. Explicit ownership | Two callers configure one channel or reuse one buffer. Need the resource's lifetime and current reader/writer. | One playback routine owns the channel settings and its countdown; callers supply a complete request. State who may replace it and when it becomes free. | Starfield title/laser restoration, Flock per-channel state, later AY shared envelope/noise and SID shared filter controls. |
| 3. Requests, priorities and interruption | An incidental cue can replace a warning or achievement. Need two distinguishable events and the existing replacement policy. | Add only a priority, tie rule and end condition. Record accepted/replaced/rejected requests. Compare immediate replacement with a bounded queue or dedicated channel; choose for the game. | Dash collect/jump/damage cues, Flock pen/hop/loss cues; later music channel stealing in Starfall, SID Symphony, Thunder Run and Onslaught. |
| 4. Safe transfer between contexts | Main prepares a multi-field request while a handler may read it. Need the player update, interrupt pre-emption and one owned resource. | First publish one event identifier; then demonstrate inconsistent fields. Use a bounded single-producer/single-consumer handoff with a complete payload and final publication byte, or a justified target-specific critical section. | Dash main/NMI graphics or sound requests; C64 CIA/raster player; Spectrum IM 2/AY; Amiga main/timer or DMA buffer handoff. |
| 5. Bounded and deferred work | Drawing/preparation delays input or makes the handler miss its transfer window. Need measured costs and a resumable job. | Keep the handler short; prepare outside it, transfer only a bounded amount at the allowed time, retain a progress cursor. Bound each work item as well as the number of items. | Dash PPU updates, Meteor Storm drawing preparation, later C64 screen updates, Amiga asset preparation. |
| 6. Worst-case budgets and headroom | A busy update contains more work than the average one. Need representative workloads, deadline and instrumentation overhead. | Account for simultaneous note changes, collision/HUD work, interrupts and relevant DMA/contention. Reserve time/capacity for a named burst; distinguish maximum observed from a justified bound. | Meteor Storm boosted busy course; planned C64 Maelstrom, NES Thunder Run and Amiga Onslaught integration. |
| 7. Deliberate overload policy | Even a bounded queue/pool may fill. Need essential game behaviour and a visible overload signal. | Decide what can be deferred, coalesced, simplified, replaced or dropped; state recovery and count every discarded request. Test rule correctness and feedback under the policy. | Optional decoration and echo can yield to important cues; hazards, score events and simulation updates cannot silently disappear. |

A small routine may combine some stages, but the explanation must not skip the motivating conflict. Headroom is not a fixed percentage to copy across machines. Reserve a measured margin for the workload the game promises to absorb.

## Pre-emption and atomicity without imaginary CPU threads

On these introductory single-CPU programs, main code and its interrupt handler do not execute CPU instructions simultaneously. An interrupt can suspend main, run the handler and then return. The problem is **interleaving**: the handler may observe state after one instruction of a multi-instruction update but before the next. DMA and other chips can operate independently, so a CPU critical section does not freeze every hardware reader.

Start with a paper trace: main wants to change a request from `(old pointer, old duration)` to `(new pointer, new duration)`. Pause after the pointer changes; let the handler inspect it. The mixed pair never existed as an intended request. Then run a diagnostic fixture with that interleaving deliberately arranged; do not rely on a rare accident during play to teach it.

**Atomicity is relative to the observer.** On a 6502, a completed single-byte store can publish a selector to an interrupt handler; a sequence of byte stores is not one atomic update. A `read → decide → clear` sequence is also not atomic merely because its variable is one byte. Do not generalise this into “every CPU instruction is atomic to all devices” or “every multi-byte value is unsafe”: check the actual instruction, CPU and reader. Use ordinary RAM for this first example, not a device register with read/write side effects.

### A bounded handoff before a queue

One main-code producer and one handler consumer can begin with a single slot:

1. Main waits until the slot is **empty**; it does not overwrite a ready request.
2. While empty, main fills the payload. The handler ignores an empty slot.
3. Main publishes ready using a final single-byte store; the payload is now immutable to main.
4. The handler copies/accepts the complete request and marks the slot empty only when it no longer needs that storage.

If the request contains a pointer to data used later by DMA, playback or a deferred transfer, accepting the request does not free that pointed-to data. Define a separate completion/ownership transition. Do not accidentally treat a copied pointer as copied content.

This protocol assumes one producer, one non-reentrant consumer and a verified atomic publication operation for the target. It is not a general multi-producer queue. Define backpressure: when the slot is occupied, main must defer or explicitly reject/coalesce an eligible request. A one-slot example should expose that limit before a larger queue is proposed.

### Critical sections have a timing cost

| Target | Suitable teaching example and limit |
|---|---|
| Spectrum | IM 1 frame pacing before private IM 2. A short DI-protected update can prevent a maskable frame handler observing intermediate RAM state, but a ULA interrupt pulse can be missed while disabled. Explain entry assumptions and how the previous interrupt-enable contract is restored; never use unconditional EI as a universal exit. Beeper edge generation and input sampling can have different deadlines. |
| C64 | Use CIA1/raster IRQ first. A short SEI-protected update can exclude that IRQ, but not CIA2 NMI. Preserve the intended interrupt-enable state, service pending sources correctly, and measure the delayed music/raster update. Pending flags do not count an unlimited number of underflows. |
| NES | NMI is not masked by SEI. Use a complete-buffer/publication protocol for main/NMI transfer. Turning PPU NMI enable off is not a generic lock: it changes display notification and has edge/timing consequences. Keep PPU transfers bounded within their permitted window. |
| Amiga | In the named 68000 takeover environment, raising the CPU interrupt mask can exclude specified levels; a higher-priority interrupt and independent DMA remain distinct concerns. Restore the previous SR/mask contract. Under Exec, use the documented system/resource protocol instead of borrowing raw takeover code. Keep sample/display storage alive until the hardware reader is finished. |

The [timing plan](timing-and-interrupts.md#verification-sources-and-limits) records the authoritative Zilog, MOS, Commodore-Amiga and public NES hardware research used for these contracts. Additional checks here inspected Motorola's *M68000 User's Manual* §6.2.5 (saved SR/PC and exception processing) and MOS's *MCS6500 Microcomputer Family Programming Manual* interrupt/SEI sections. A particular code snippet needs its own mask, register-preservation, acknowledgement and return contract checked before publication. No fabricated common “disable all interrupts” helper belongs in the shared explanation.

## Controlled exercises and repairs

Use the profiling plan's supported guest tools, short RAM logs and machine-appropriate visual markers. Label any forced interleaving as an experimental fixture. Preserve the baseline, allow reset and cap the fault run. Record request time, acceptance/service time, completion, reason for replacement/rejection, queue occupancy and deadline misses where applicable. Host elapsed time is not guest latency.

| Existing location | Provocation and observation | Repair and evidence |
|---|---|---|
| Flock unit 11, then 17 | Existing local trace reverses baa/bleat order; next runnable checkpoint schedules hop and pen/loss requests close together. Inspect `sndtimer`, `sndhalf`, `sndper2` and accepted cue. | Compare current last-call policy with a single priority rule and deterministic tie-break. Retain a high-priority cue against a later incidental cue; verify release, next request and retry. Do not create a general mixer. |
| Starfield unit 17 → SID Symphony | Deliberately omit instrument restoration in a separate checkpoint, then add an effect during a musical note. Log music position and hardware owner. | Restore the instrument/state contract. Compare advancing music silently with pausing its part; choose explicitly. A skipped musical note may be acceptable, but document the audible loss. |
| Dash unit 14/17 → Thunder Run | At a diagnostic boundary, arrange NMI between two request stores; separately arrange it between main's flag read and clear. Inspect the mixed payload or lost notification. | Use the one-slot publication protocol for payloads; use a counter/sequence comparison with wrap rules if elapsed updates must be counted. Do not blindly replace all event flags with counters. Verify full/empty and wrap cases. |
| Dash graphics transfer | Prepare a bounded update list, then force one list beyond the permitted transfer work. Capture how late the final transfer would occur; stop the fault safely. | Cap transfer work, retain the cursor, prepare data outside NMI and define when the picture may become visible. Deferred visual work must not expose half-published state. Do not treat a whole frame as a safe PPU window. |
| Meteor Storm unit 12/20 | Existing one-slot fault exposes lost hazards. The profiling companion adds bounded expensive preparation on a busy boosted update. Compare update, input and drawing boundaries. | Restore adequate capacity; remove/reuse redundant preparation or defer optional work. Keep collision and course events intact. A change that omits hazards is a changed game, not an equivalent optimisation. |
| Flock → Onslaught | Add bounded preparation work between input opportunities; later publish a new sample/buffer while the old reader still needs it in an isolated fixture. | Split preparation into resumable bounded chunks, keep input serviced, and release old storage only after completion. Verify sample continuity and buffer lifetime, not only average frame time. |

Graphics-window ownership and channel ownership share questions—who may write, when, and what happens to a conflicting request—but not one implementation. A sound can replace another immediately by design; a partially transferred picture or sample buffer may need a completion boundary. Keep those differences visible.

## Decide what degrades before the game is busy

| Candidate policy | Appropriate example | Consequence to explain and check |
|---|---|---|
| Delay | Non-urgent asset preparation or a cosmetic HUD refresh | The result arrives later; retain a bound and a visible loading/ready state when needed. An indefinitely growing backlog is not a repair. |
| Coalesce | Several requests to display the newest score | The displayed intermediate values may be skipped, but every scoring event must still update authoritative state. “Set score display” differs from “award points”. |
| Simplify | Fewer decorative particles or a cheaper non-essential animation | Preserve gameplay geometry and readable feedback; state the visual trade-off. |
| Replace/drop | Quiet echo or an incidental footstep yields to an important cue | A musical role or cue disappears; preserve an alternative for essential information and count dropped requests. |
| Refuse or change scope visibly | Required work cannot meet the promised budget | Reduce authored workload, show a deliberate pause/loading transition where the game permits it, or revise the design. Do not silently discard simulation steps, collisions, required hazards or important events. |

Write a fixed priority/tie rule and record it with the event schedule. Choose decisions from guest state or recorded workload limits, not accidental host speed. A policy based on a variable deadline measurement can change outputs between runs; record the decisions for replay or use a deterministic work cap when reproducibility is required. Optional visuals can still affect perception, so test that the player can recognise the same hazards and outcomes.

A busy-scene trial must include simultaneous costly paths, not only many cheap objects: new notes, effect requests, HUD change, active collisions, transfer/row changes and relevant DMA. Measure handler overhead and instrumentation. Reserve headroom for a specified burst and check recovery after it. A bounded queue still needs a policy when full; include queue high-water mark and dropped/deferred counts in the result. Average performance alone does not establish reliability.

## Bounded implementation order

1. **Local lesson edits complete:** Flock unit 11's state/priority trace and Meteor Storm unit 12's memory-safety-versus-rules question. Game code unchanged; not published.
2. **C06a companion authored:** Flock unit 11 now links two generated native variants using the original sound setup: latest-wins and strictly-higher-priority-wins. The controlled pairs are hop→pen, pen→hop and pen→pen. Counts distinguish accepted/rejected requests even when same-update replacement is not audibly separable. The ordinary game stays unchanged; C06b now provides the spaced-request comparison described below.
3. **Then one real context handoff:** Dash units 14/17, after the timing plan's introduction corrections and understood player update. Demonstrate payload publication and the flag read/clear limitation separately; no DPCM or general task system yet.
4. **Measured headroom:** use the existing Meteor Storm profiling task and its fixture before adding another benchmark. Extend the same evidence method to SID Symphony, Thunder Run and Onslaught only as their agreed game requirements develop.

Larger work remains in the named lesson/sample locations: bounded transfer lists, timer-driven ownership, DMA completion, and deliberate degradation. Completion means a learner can identify the owner, trace the interruption, predict the overload decision and demonstrate that the repair preserves the promised game behaviour—not merely that the program runs faster.

## Flock ownership companion: C06a

Sample location: `code-samples/commodore-amiga/assembly/flock/unit-11/ownership/`.
`prepare.py` checks the unit-11 baseline hash and generates inspectable sources;
`requestsound.asm` contains the narrow priority guard; `experiment.asm` supplies
three fixed request pairs. Both variants keep the original `playsound` hardware
setup. The timer's existing stop path also clears the priority. Gameplay updates
are replaced only in this isolated fixture; the bottom-right digits show accepted
and rejected counts, not points. The request API is main-loop-only, with positive
durations and priorities 1/2. It is not a shared-state interrupt solution.

The lesson asks for predictions, provides a folded hint and comparison, and asks
learners to justify a tie policy. It distinguishes losing a feedback request from
losing a game event and notes that two accepted requests may not both be heard.
The fixture updates sound before making requests; the original whole-hop trace
updates it afterwards. Neither ordering is hidden behind a common event model.

C06b adds `prepare.py --spaced`, using the same ownership/player routines.
Eleven records per policy check interruption, repeated equal-priority requests,
low-priority acceptance after expiry (including a request in the expiry update),
and an original pen cue followed by release. The timer is never forcibly reset
between groups. C06a source hashes still match. Both new variants pass native
A500 PAL/Kickstart 1.3 checks; `spaced-results.json` stores exact identities.

Unit 11 embeds two four-second native recordings, trimmed without gain changes
or rearrangement. `extract_audio.py` and `audio-excerpts.json` preserve the sample
bounds and hashes. Signal/clipping/tail checks pass; subjective clarity is left
for listening review, not inferred from state checks. A muted prediction table
and folded explanations separate software retriggering from any promise about
sample phase. The lesson links back to its whole-hop trace and forward to unit
17's title/game audio handover. Original game, WASM integration and mixer design
are unchanged. These captures are not exact frame-timing or hardware-fidelity
measurements.

Verification: both generated variants passed native Emu198x Amiga 0.25.0 cold
ADF boots on A500 PAL/Kickstart 1.3. All three guest-written records match timer,
priority, accepted/rejected counts and later period; ownership is zero after
completion. Exact hashes and limits are in the companion's `results.json`.
The website build (2,468 pages) and rendered optional section also pass. These
are configuration-specific state checks, not subjective listening, complete
sprite/gameplay regression coverage or original-hardware evidence.


## Dash complete-request handoff: C09c

Implemented locally at `code-samples/nintendo-entertainment-system/assembly/dash/unit-17/handoff/`,
with the learner investigation in unit 17. The original player runs in main;
the fixture is a deliberately new main-to-NMI period request, not evidence that
ordinary Dash already has this fault. It replaces gameplay dispatch with a
six-stage diagnostic while preserving the title handler/display work.

The producer deliberately waits for a real NMI between low/high stores. Publishing
ready too early delivers `$01D5`; publishing after both writes ignores the
unfinished slot, then delivers `$00D5`. The consumer releases only after its
last payload read. Full returns carry set without changing the pending pair;
the caller retains and retries the refused request. Empty performs no period
writes and consumed requests do not repeat. This contract assumes one producer,
a non-reentrant consumer and ordinary RAM, not a generic concurrent container.

Native NTSC results record actual handler-entry payloads and A values at pulse
period stores, six stages per version and identical cold repeats. A/X/Y and
stack checks pass. Instrumented title handler costs are 864–865 cycles empty,
895 consuming, including DMA; all measured returns are on scanline 248. Entry
latency is excluded and logging has overhead. This is not a worst-case game
budget, PAL or original-hardware evidence. The baseline rebuild matches its
maintained ROM; ordinary game and WASM files are unchanged.

The lesson asks for predictions before explanations, distinguishes pre-emption
from simultaneous CPU threads, explains why SEI does not mask NMI, and asks
where a pointer's lifetime would extend beyond mailbox release. The actual
consumer applies one request without waiting. No general queue, music-player
migration or notification-counter change is included. C09d remains the next
independent read/clear-notification investigation.
