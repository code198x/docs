# Timing and interrupts — focused curriculum changes

**Status:** Source-reviewed implementation plan, not implemented lessons or measured new results. Applies the [audio progression](audio-progression.md) and [curriculum specification](../curriculum.md). Audio is one reason to coordinate work; input, simulation and drawing remain equally important. Keep the queued Bright Spark change small.

## Review findings and concrete changes

Locations below are relative to website `src/content/curriculum/`. Read the lesson and its maintained sample together before changing it. Catalogue placements for later games retain the provisional status recorded in the audio progression.

| Existing location | Finding from source review | Focused change |
|---|---|---|
| `sinclair-zx-spectrum/assembly/meet-assembly/unit-07.mdx` | Already distinguishes display frames, movement opportunities and actual moves. It names the stock ROM IM 1 contract and register preservation. | Retain this accessible movement example. Explain that a long iteration can miss the next opportunity; one return from HALT is not evidence that no intervening time was lost. No player engine prerequisite. |
| `sinclair-zx-spectrum/assembly/meteor-storm/unit-06.mdx`, units 07–08 and 20 | IM 2 begins with a short counter handler; later lessons separate simulation/rendering and compare measured frame deltas. | Keep the small handler. Add a diagram of request, acceptance, handler and resumed work; count handler cost in the budget. Use unit 20’s existing recording method for a bounded overload companion. |
| `sinclair-zx-spectrum/basic/bright-spark/unit-02-give-a-choice-a-signal.mdx`, unit 04 | The cue already separates BEEP duration, PAUSE and other work. | Implement the queued pitch/duration comparison first. Refer to timing through cue boundaries, without introducing interrupt setup in BASIC. |
| Spectrum Gloaming unit 18, The Long Night unit 08, Shadowkeep unit 18 | CPU-owned tone generation and input polling offer an audible contrast to hardware voices; chunk-count duration can depend on pitch. | After tracing the existing note update, compare delayed note starts with disturbed waveform edges. Correct duration/pitch coupling before calling this a reliable musical clock. Starfall’s later AY player supplies the hardware-generated contrast. |
| `commodore-64/assembly/starfield/unit-17.mdx` | Existing `jingle_tick` gives a concrete duration counter and note change; describing its work as “twice per note” hides per-update work and register writes. | Trace an ordinary tick, a note change and a rest; count them separately. Call the understood routine from a simple paced loop before moving it into an IRQ in planned SID Symphony. |
| `nintendo-entertainment-system/assembly/meet-the-machine/unit-09.mdx` | Claims of perfect once-per-frame behaviour and a universally safe screen-update slot are too broad. Its sample changes A without saving it, harmless only for the idle main loop used there. | Correct the prose and narrow the graphics claim. Either preserve A or explicitly teach the idle-loop restriction before any useful main work; preserve all clobbered A/X/Y when that work is added. Keep the early example as a bounded display notification. |
| NES introduction unit 10; Dash units 05, 11 and 17 | Unit 10 suggests the input loop belongs in NMI; Dash’s phrase update is a later, concrete explanation of music state. | Separate input/game work from the short display handler. Trace Dash’s music update before teaching its interrupt scheduling; distinguish NMI from the APU’s internal frame sequencer. Use planned Thunder Run for the measured combined deadline exercise. |
| `commodore-amiga/assembly/meet-the-machine/unit-09.mdx` | The example polls the beam; it is not an interrupt handler. Prose blurs vertical blank with a whole frame and treats 50 frames as exactly one second. Its leave-line wait prevents repeated work on one line only while work remains short. | Label polling explicitly, qualify nominal timing, and draw the smaller blanking interval inside a full frame. Show how a long job can miss the polled line or the next frame. Avoid presenting this loop as universal. |
| Amiga Flock units 11 and 17 | `soundtick` and `tunetick` already make the per-update work inspectable. | Explain their order and shared state first. Add a small load comparison, then introduce a vertical-blank service; planned Onslaught supplies CIA-clock and audio-block extensions. |

The NES introduction units 09–10 accuracy repair is implemented locally (C02a, accepted): rendering-disabled scope, bounded transfer windows, register preservation and main-loop responsibilities are explicit. Its NTSC sample checks are recorded with the code. The Amiga introduction unit 09 prose repair is also implemented locally (C02b, ready for review): polling, combined VPOSR/VHPOSR reads, Copper consumption, a schematic frame/blanking distinction and a missed-update prediction are explicit. Its sample is unchanged. A roughly twelve-second PAL A500 emulator recording now demonstrates the colour cycle; it does not measure deadline behaviour or establish original-hardware accuracy. These are separate bounded edits, not reasons to rewrite their entire modules. The later interrupt/audio companions should recall earlier hardware notifications without assuming that early exposure explained a music player.

## Establish the clocks before changing the scheduler

We first single-step a tiny player in the main program: count down a duration; when it expires, read a note or rest; update its sound state; return. Display the index, remaining count and whether a register write occurred. Only then ask what should call it regularly and how interrupts could help. Explain a routine that returns before introducing a handler that interrupts another routine.

| Clock or schedule | What it controls | What it does not establish |
|---|---|---|
| Display refresh | The display’s repeating scan/frame | How often simulation or music must advance |
| Game updates | Input decisions, movement and game rules | Waveform pitch or permission to write every graphics register at any time |
| Musical player updates | Note events, envelopes and effect steps | The audio oscillator/sample rate; a tick may do nothing audible |
| Audio waveform/sample timing | Oscillator edges, or samples delivered to the output | Musical phrase length or the game’s frame deadline |

Use nominal rates for the first calculation: `1000 / 60 ≈ 16.67 ms` per frame and `1000 / 50 = 20 ms`. A six-update note lasts `6 / 60 = 0.100 s` or `6 / 50 = 0.120 s`. Unchanged data played at 60 instead of 50 updates/second runs **20% faster** (`60/50 = 1.2`); its duration is **one sixth shorter**, not 20% shorter. Frame-stepped envelopes, arpeggios and vibrato also run faster unless independently scheduled.

Keep the pitch registers unchanged in this first experiment. It changes duration and effect speed, not intentionally the base pitch. A real regional machine change can also change hardware clocks, and hence tuning: that needs a separate pitch-table/rate comparison. “PAL” and “NTSC” alone are not sufficiently precise configuration descriptions.

For precision, derive time from the named machine and mode. As one checked example, the stock 48K PAL Spectrum has 69,888 T-states per frame at nominal 3.5 MHz: about 19.968 ms and 50.0801 Hz. Do not copy that timing to a 128K Spectrum. C64 VIC revisions differ; NES NTSC rendering can alternate frame lengths; Amiga display modes and interlace affect the schedule. Record actual clocks, mode and emulator configuration before setting thresholds. The introductory arithmetic is not an exact hardware timing table.

## What an interrupt does — and what it costs

An event requests service. The CPU accepts it under its architecture’s rules, saves its automatic return state, enters a handler, and eventually resumes. Acceptance is not instantaneous: instruction completion, masking, another handler and bus/DMA delays can contribute. Distinguish request-to-entry latency, handler execution time and the delay until the actual sound/register update. A handler that only sets a flag still leaves main-loop dispatch latency.

A frame budget includes useful main work, interrupt entry/exit, explicit register saves/restores, acknowledgement, handler work and relevant bus stalls. Do not count handler work twice when comparing an elapsed whole-frame trace with the sum of measured sections. A 20 ms frame is not a 20 ms safe graphics-write window. State the deadline for each operation: prepared game state, a PPU transfer, an audio event or a sample-block handover can have different deadlines.

The first handler has one bounded job and no waits, allocation, unbounded table parsing or nested interrupts. Later a proven short music update may run there; rendering, decompression and long searches stay in separately budgeted work. A timer or NMI cannot create CPU time, and pending interrupt state is generally not a queue counting every missed event.

### Hardware contracts to teach at the point of use

| Target and mechanism | Return state, acknowledgement and limits |
|---|---|
| Spectrum frame interrupt, first through ROM IM 1 | The ULA supplies a finite maskable interrupt pulse, not a software-cleared VIC-style status latch. A masked pulse can be missed. The Z80 saves the return PC, not the general registers. The ROM has its own preservation and system-variable contract; retain the existing lesson’s named ROM/IY/stack assumptions. |
| Spectrum private IM 2, later AY playback | IM 2 changes dispatch, not the frequency of the frame signal. Establish stack/vector memory before enabling; save every register/flag the handler changes and restore it. RETI does not by itself re-enable maskable interrupts; explain the existing EI/RETI sequence and EI’s delayed acceptance. Do not invent an AY-generated music interrupt. |
| C64 VIC-II raster IRQ | Configure raster compare and enable only owned sources. Identify pending sources; clear handled VIC flags by writing ones to their bits in `$D019`. CPU IRQ entry saves PC/status, not A/X/Y. Save clobbered registers and use RTI for a direct handler; ROM-dispatched handlers have a different prologue/exit contract. Raster position gives a display reference, not free or zero-latency service. |
| C64 CIA timer IRQ | CIA1 feeds IRQ; CIA2 feeds NMI, so choose CIA1 first. Timer underflow can pace music independently of raster position. Reading ICR returns and clears pending source flags: read once into a saved value, dispatch all relevant owned bits, and distinguish this from writing the interrupt mask. Account for KERNAL/timer ownership rather than silently replacing services. Timer settings depend on the source clock. |
| NES VBlank NMI | PPUCTRL bit 7 enables the VBlank NMI output; the CPU responds to its edge. SEI masks IRQ, not NMI. CPU entry saves PC/status; software saves clobbered A/X/Y and returns with RTI. There is no VIC-style NMI acknowledgement write: reading PPUSTATUS clears the VBlank flag and resets the address-write latch, with timing side effects. Do not poll it casually around VBlank or toggle NMI enable there in the beginner program. Keep normal rendering-time transfers inside the bounded VBlank window, or use an explicitly taught rendering-disabled/special technique. |
| Amiga vertical blank | Custom-chip VERTB is a level-3 source, sharing that level with other sources. In a direct takeover handler, inspect pending/enabled sources and clear only serviced INTREQ bits using its set/clear convention. 68000 exception entry saves SR/PC, not working D/A registers; preserve those used and return with RTE. The CPU interrupt mask and higher-priority activity affect entry. Under Exec, use the interrupt-server contract rather than installing a competing raw handler. |
| Amiga CIA timers and audio interrupts | CIAA is routed via PORTS/level 2; CIAB via EXTER/level 6. Service CIA ICR and the associated custom-chip request under a single owner; reading ICR clears its latched flags. Use resource ownership under the OS. Audio-channel block interrupts are level 4 and can support buffer/loop handover when needed; they are not one interrupt per output sample. DMA streams samples without a CPU handler for each one. |

For Amiga, do not mix an Exec callback’s exit convention with a hardware vector handler’s RTE. For C64, similarly distinguish the KERNAL vector route from a fully owned hardware IRQ vector. Each runnable checkpoint must say which environment it uses and restore or terminate it according to that environment.

### Shared state, introduced in two small steps

The [scheduling and ownership plan](scheduling-ownership-headroom.md) develops
this into explicit publication, backpressure and overload contracts, with
controlled exercises and target-specific critical-section limits.

First publish one byte: main code writes an effect identifier, then the handler consumes it. Define what happens to two requests before consumption and avoid a read/clear race; a mailbox is not a queue. Next show a two-byte pointer or multi-field instrument request interrupted halfway through. The symptom is a mixed old/new value, not mysterious random music.

Use one owner for sound registers. Fill an inactive request buffer and publish it with a final atomic index/ready operation, with explicit producer/consumer ownership so the producer cannot overwrite an unread buffer. Alternatively use a short justified critical section for maskable interrupts; count its latency cost. **SEI cannot protect shared data from NES NMI.** A flag alone does not make multi-byte data consistent, and a byte counter can wrap. Make the deliberately bad version deterministic through an instrumented interleaving, then remove that instrumentation for the repaired timing measurement.

## Four controlled experiments

Use the [profiling progression](profiling-progression.md) for tool availability,
machine-appropriate markers, before/after evidence and the separation between
guest timing and host-emulator cost.

Use the audio progression’s short original study and a simple moving marker. Keep source/data, target configuration and event schedule identical except for the named variable. Offer restart and a bounded end to every fault. Display requested versus serviced events and timestamps; do not promise a particular audible glitch in advance.

| Experiment | Implementation and prediction | Evidence and repair |
|---|---|---|
| 1. Change update rate | Run the same six-tick events at nominal 50 and 60 player updates/second while keeping waveform pitch configuration fixed. A host listening model can make the arithmetic exact; label it as a model. A target version derives achievable rates from its actual clock and reports rounding. Initially leave envelopes/effects off, then repeat with one effect. | Compare note-onset intervals and total phrase length, then vibrato or envelope speed. Expect the nominal 100/120 ms contrast. A regional machine switch is a separate experiment because it may also change tuning. |
| 2. Separate tempo from display | Keep event durations in musical/time units. For a low-cost first repair, accumulate elapsed frame time into musical phase and emit a bounded number of due player steps. A 50-step/sec player sampled at 60 display frames will skip some calls; explain frame-sized jitter rather than calling it perfectly punctual. Later use a C64/Amiga CIA timer when finer timing earns its cost. | Compare phrase duration at both display rates and plot event spacing. State rounding, accumulator width, wrap handling and catch-up limit. Multiple register writes at one instant do not recreate events whose deadlines were missed. Select a backlog policy: skip obsolete decoration, resynchronise from musical time, or report overrun; never an unlimited catch-up loop. |
| 3. Exceed a budget deliberately | Add one bounded calibrated workload to main dispatch; separately add a bounded handler delay. Increase only one until a chosen deadline is missed. Never make the first failure an infinite IRQ storm. Log request/entry/update/exit where the tool supports them, plus animation commits. | Hardware audio may hold the previous pitch/level, continue its envelope, expire a length counter or keep streaming a sample. The result might be only a late new note or uneven animation. For a beeper companion, delay a waveform edge: a changed period/gap can alter the sound directly. Distinguish measured outcomes from expectations. |
| 4. Repair and compare | Remove the artificial load as a control, then keep equivalent useful work and move it out of the handler, split/defer drawing, precompute a value or reduce redundant writes as justified. For tempo drift, repair the scheduler rather than making the whole program faster. | Replay the same event schedule and heavy scene. Compare maximum observed lateness, missed deadlines, handler time, note intervals and game response. Verify musical articulation, register state and output as well as speed. State the tested bounds; one clean run is not a proof of all cases. |

The scheduler can keep average tempo while still producing uneven events. Teach that distinction audibly. A display-synchronised scheduler is acceptable when its measured jitter fits the design; timer-driven playback is an earned refinement, not a mandatory badge of correctness. Spectrum frame interrupts and NES NMI do not by themselves provide an arbitrary finer-rate timer.

## Manageable placement and implementation order

1. **Accuracy edits:** revise NES introduction units 09–10 and Amiga introduction unit 09, including the actual harness preservation contract. Keep them short and visual; do not move a whole audio course into the machine introduction.
2. **First audio timing checkpoint:** after the queued Bright Spark comparison, add a focused companion to Dash unit 17. Trace the existing `tune_tick` in main code, expose the six-update countdown, compare rates and implement the bounded accumulator. Keep its pulse voice, existing game and accepted source as the baseline. A browser model explains exact 50/60 arithmetic; native evidence is separately labelled.
3. **First interrupt/audio checkpoint:** reuse the same understood Dash update under a bounded NMI/main handoff, with explicit register preservation and transfer budget. Inspect a main-loop delay and a separate handler delay. No DPCM, advanced effects or new music engine in this checkpoint.
4. **Reuse the investigation, not the handler:** Starfield unit 17 → SID Symphony for raster/CIA comparison; Flock units 11/17 → Onslaught for vertical blank/CIA and later block handover; existing Spectrum beeper companions → Starfall for AY, linked back to Meteor Storm’s budget measurements. Each explains its own hardware contract locally.

These placements are proposed implementation work, not approval of a new game order. Beginners need one sound, one table, one countdown and one clock first. IM 2, timer ownership, regional tuning, shared multi-field state and sample interrupts are later questions that arise from real requirements.

## Verification sources and limits

Reviewed local manufacturer/reference material and the named lesson/sample sources establish the contracts above. Hardware review is distinct from running the proposed exercises. No new cycle budget, target execution result or cross-region success is claimed.

- Zilog, [*Z80 CPU User Manual*, UM008011-0816](https://www.zilog.com/docs/z80/um0080.pdf), “Interrupt Request/Acknowledge Cycle”, “Interrupt Enable/Disable”, “CPU Response”, IM 1/IM 2, EI and RETI entries. Chris Smith, *The ZX Spectrum ULA: How to design a microcomputer*, chapters 10–11 (clocks/video timing, pp. 95–100 for the frame table) and chapter 21, pp. 223–228 (ULA interrupt generation). Smith is original hardware analysis, distinct from the CPU manufacturer's specification.
- MOS Technology, *6567 VIC-II Preliminary Data Sheet*, “Raster Register” and “Interrupt Register”: raster compare and write-one-to-clear status; *6526 CIA Data Sheet*, “Interrupt Control Register” and timer sections: read-to-clear flags, separate write mask and timer underflow. The family holds the original VIC scan/transcription and a recreated CIA datasheet; verify register diagrams against the scan before publishing new register-level examples. Commodore, *Commodore 64 Programmer’s Reference Guide*, memory maps and interrupt/ROM routines, supplies the machine wiring and KERNAL context.
- NESdev’s preserved public PPU research pages: [NMI](https://www.nesdev.org/wiki/NMI), [PPU registers](https://www.nesdev.org/wiki/PPU_registers), [PPU frame timing](https://www.nesdev.org/wiki/PPU_frame_timing), and their hardware-test evidence. The local archived text was inspected because live retrieval failed. These are public hardware research, not Nintendo manufacturer documentation; do not substitute restricted internal documents in public teaching. Test the proposed handler on the named PPU/CPU configuration and inspect the NMI register-save path before using it with active main code.
- Commodore-Amiga, *Amiga Hardware Reference Manual*, second edition: chapter 5 “Audio Hardware”; chapter 7 “System Control Hardware”, pp. 211–216 (interrupt controls, priorities and request bits); appendix F, 8520 ICR/timers. Motorola, *M68000 User’s Manual*, exception processing and RTE, governs CPU entry/return; the Amiga manual defines source routing and acknowledgement. The local Amiga manual’s request registers and priority table were inspected; an OS-hosted version additionally needs the documented Exec/cia.resource service contract before implementation.

Before a checkpoint is complete, retain the actual source, machine/region/mode, event schedule, instruction or trace accounting, measured note boundaries and before/after output. Run a counter/register sentinel through the interrupted main code to detect preservation errors. Check that normal playback restores silence and state after a fault, and that graphics transfers stay within their own window. Cite exact source sections in learner pages; use accessible British English and “we”, and make diagnosis a shared investigation.

## NES collect-cue correction

C02c is implemented locally, ready for review. Dash unit 11 distinguishes the
length and linear gates, delayed reload and independent APU timing. Its original
cue is preserved; the longer-note exercise changes the length index as well as
the linear reload. The [isolated counter fixture](../../../code-samples/nintendo-entertainment-system/assembly/dash/unit-11/verification/README.md)
records NTSC/PAL results and the emulator's separate held-output limitation.
No subjective listening or original-hardware verification is claimed.

## NES game-over transfer budget

C02d is implemented locally, ready for review. Dash unit 14 replaces its partial
estimate with a full handler count and a prediction about the later one-shot
path. The [NTSC handler fixture](../../../code-samples/nintendo-entertainment-system/assembly/dash/unit-14/verification/README.md)
checks the unchanged assembled paths, DMA stalls and return before pre-render.
It measures guest time including stalls, separately from interrupt-entry latency
and host execution time. Controlled state injection is not a play-through;
PAL, original hardware and a separate learner trial remain unverified.


## Dash player-rate diagnosis: C09a

Implemented locally in Dash unit 17, with the small companion at
`code-samples/nintendo-entertainment-system/assembly/dash/unit-17/tempo/`.
The existing source's SHA-256 is pinned in the script and results. Its title
phrase is parsed directly; a countdown model is compared with an independent
cumulative-duration oracle. All 27 events agree in update index and period.
The 286-update phrase takes 5.72 seconds at exactly 50 updates/s and
4.766667 seconds at exactly 60. The six-update rest at update 96 ends at 102,
so it lasts 120 or 100 ms respectively.

Two fixed-gain, ideal-pulse listening files and complete requested/service CSVs
support prediction, folded help and a muted numerical comparison. Service is
instantaneous by model construction; these are not measured game deadlines.
The fixed pitch reference isolates tempo from regional tuning. WAV lengths,
non-zero signal and clipping limits are checked; a learner listening review
remains separate. The model excludes CPU/APU execution, analogue output,
missed notifications and gameplay. It stops at the first loop boundary rather
than implementing a replacement music engine.

The lesson locates the player call in main code after input reading and recalls
NMI notification without suggesting simultaneous CPU threads or punctuality by
interrupt alone. It distinguishes a sustained old hardware note from waveform
corruption. Native service-latency evidence remains follow-on work. C09b owns
the bounded tempo scheduler, with event jitter/backlog limits and native
regressions; C09c/d own shared-state and notification hazards. The ordinary
game instructions/data and ROM, difficulty and concurrent WASM work are preserved.
A two-line source/snippet comment about note writes was corrected; stripping
comments confirms identical code. The 2,468-page site builds and both listening
models enter playback in the browser; the folded comparison table opens.


## Dash bounded musical phase: C09b

Implemented as a companion at `dash/unit-17/tempo/scheduler/`, with a unit 17
prediction, trace and listening exercise. The actual assembly routine accepts
1–6 units of 1/300 second, retains phase 0–5, and performs at most one player
update. Out-of-contract input explicitly faults and stops the experimental
music. A new phrase resets phase, first-service state and fault. Caller-supplied
time is a contract, not a hardware measurement or missed-notification detector.

The exact-rate model retains the C09a phrase and pitch settings: target 5.72 s,
serviced at 5.72 s with 50 opportunities/s or 5.733333 s with 60. Greatest event
lateness in this phrase is 13.333 ms. CSVs preserve requested/service times;
model audio is labelled separately from native evidence.

Native NTSC runs use the actual player with generated, instrumented wrappers:
every-opportunity service versus five-of-six requests. This is the same machine
with two deliberately different cadences, not evidence of a PAL clock. All 28
recorded events, including next-loop onset, match their independent schedules;
corresponding events differ by at most one opportunity. Injecting an elapsed
value of 30 stops music and sets the diagnostic flag; its audio is zero after
four seconds. Short Start/movement/jump input regressions match selected
baseline state. One playing NMI path completes at scanline 247, with preserved
registers, taking 718/719 cycles including DMA and excluding entry latency.
This is not a new worst-case budget or complete playthrough. Instrumentation
changes layout/time; ordinary samples and ROM remain unchanged. `native-results.json`
and `model-results.json` identify the evidence. C09c/d retain ownership of
shared-state and notification hazards, which this scheduler does not solve.
