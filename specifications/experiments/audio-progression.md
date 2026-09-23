# Audio — progression through the four core systems

**Status:** Concrete teaching proposal applying the [agreed audio direction](../graphics-and-audio.md#agreed-audio-and-performance-direction). Existing coverage is distinguished below from proposed extensions and provisional later placements. No new lessons or engines are implemented by this plan. Bright Spark is the queued first change.

This document owns the placement of experiments and their practical boundaries. The graphics and audio specification owns policy, scope, voice, historical evidence and future MIDI/PC coverage; [current work](../../work.md#audio-and-performance) owns the next task. We are not adding a competing game lineup or making every system implement one common engine.

## What the existing route gives us

The audit read the system module catalogues and the named lesson/overview sources, not just their availability labels. Catalogue order is useful placement evidence; an inherited “coming soon” page is not an approved design or implemented game.

| Route inspected | Existing teaching to retain | Placement consequence |
|---|---|---|
| Spectrum BASIC: Meet BASIC → Bright Spark → Volley → Touchdown, followed by the revised game groups | Bright Spark unit 02 selects pitch and duration for a visual cue; unit 04 plays the stored sequence. | Begin sound design here. A reader does not need assembly or a new music project. |
| Spectrum assembly: approved Meet Assembly → Meteor Storm; Gloaming, The Long Night and Shadowkeep remain available | Meteor Storm units 06–08 teach interrupts and clocks; unit 20 measures rendering schedules. Gloaming unit 18 introduces a beeper routine. The Long Night unit 08 explores a title tune and input polling; Shadowkeep unit 18 reads a one-voice theme from data. | Use existing beeper work as optional connected investigations, without reinstating the retired compulsory sequence. Starfall is the catalogue’s later 128K/AY home, still a proposal. |
| C64: Meet C64 BASIC and Bleeper; independently Meet the Machine → Starfield | Bleeper units 01–03 connect SID cues to panels and sequence data. Assembly introduction unit 15 triggers a SID voice; Starfield units 05/08 add laser/explosion effects; unit 17 contains a title sequencer and instrument handover. | Extend these first. The catalogue later places SID Symphony after Hornet, then Catacombs and eventually Maelstrom: suitable provisional homes for a player, game integration and combined budgets. |
| NES: Meet the Machine → Dash; later Crate Escape, Fracture Point, Pellet Panic, Fangs for the Memory, Thunder Run | Introduction unit 17 already compares pulse duty at the same pitch. Dash unit 05 explains jump sound, unit 11 a second pulse effect, unit 17 a phrase player and ending cues. | Strengthen existing comparisons rather than repeat the introduction. The catalogue identifies Thunder Run for a music/SFX engine. |
| Amiga: Meet the Machine → Flock; later Exodus, Shatter Point, Copper & DMA, Signal, Ascent, Crypt, Gobble, Wanderer, Onslaught | Introduction unit 18 plays a sample. Flock unit 11 changes waveform and pitch, with one-channel replacement; unit 17 adds a phrase sequencer and unit 18 develops the ending. | Flock supplies early design and ownership experiments. Onslaught is the provisional tracker-integration home. Shatter Point’s “first samples” tagline needs reconciliation because samples already occur earlier. |

The C64 BASIC and Amiga AMOS/Blitz routes remain independent entrances. Bleeper can share the listening questions; AMOS’s existing Meet AMOS unit 15 can link to the sample experiments. The native playback work below belongs to assembly and does not become a prerequisite for those routes.

### Placement evidence and conflicts to resolve at authoring

Source locations in the [website repository](https://github.com/code198x/website/tree/main/src/content) are `modules/<system>/assembly.yaml` (plus Spectrum/C64 BASIC catalogues) and `curriculum/<system>/<language>/<module>/`. Unit numbers above refer to the actual lesson files, not promised unit totals. The four system slugs are `sinclair-zx-spectrum`, `commodore-64`, `nintendo-entertainment-system` and `commodore-amiga`.

Thunder Run’s overview still describes an old mapper-heavy project and a different predecessor, while the current catalogue assigns audio. Onslaught’s overview also has stale ordering and a fixed 256-unit promise. Reconcile these pages when briefing the relevant project; do not inherit those prerequisites or sizes. Starfall and SID Symphony have overview pages but no authored units. Neither their existence nor this mapping settles the whole later game sequence.

Older source explanations also need targeted review: claims that sound hardware makes the player free, that all beeper programs must block in the same way, and that every driver is the same sequencer are too broad. Shadowkeep’s note lengths are currently counts of waveform chunks: do not claim that equal chunk counts already give equal durations at different pitches. Audit the routine and teach the coupling before changing it.

## Three strands, one small passage

Each stage asks three connected questions:

- **Hearing and designing:** what changed, and does it communicate the intended event?
- **Arrangement:** which role matters now, what should leave space, and what is lost when a voice is borrowed?
- **Playback:** which data, state, hardware control and deadline produce that result?

Use a newly authored two-bar study as a comparison fixture: in 4/4, quarter notes `C4 E4 G4 rest | G4 E4 D4 C4`. Start at 120 quarter-note beats per minute for a short, easily counted phrase. Explain pitch names, the rest and bar grouping locally. This is proposed teaching material, not an asserted historically unique melody or a quotation from Solstice. Transpose into a useful range for each target.

First hear the bare line. Later add a short/long articulation contrast; a bass C then G; a C–E–G arpeggio in one gap; one restrained modulation; and a quiet answering repetition. Introduce only one change per comparison and retain a version without it. “Richer” is not automatically better: the final exercise removes parts until the important line is clear again. The beeper version remains a sequential arrangement; hardware voices can later overlap parts. Do not replace an accepted game theme merely to standardise the study.

The study belongs beside the game lesson as an inspectable experiment. Apply its idea immediately to a real cue, title phrase or music/SFX conflict. The Craft’s planned Sound and Music module can explain intervals, articulation and arrangement using the same fixture, without becoming an entry requirement. Link backwards to tables, state, clocks and the existing sequencer patterns; review their assumptions before reuse.

## Playback milestones and dependencies

These are learning milestones, not eight mandatory engine layers. An early game effect may precede a musical data player; integration and measurement begin early and become more demanding later.

| Milestone | Prerequisites to explain locally | Practical proof and audible outcome |
|---|---|---|
| 1. Trigger directly | Routine calls, register or BASIC command, start/stop | Trigger one bounded cue on a game event. Hear its start and end; restore silence safely. |
| 2. Notes, durations, rests | A short table, index, terminator, pitch representation | Play the study from data. Replace a note with a rest without shortening the phrase; diagnose an omitted stop or bad duration. |
| 3. Reliable musical clock | Counters, update ownership, the target’s timing source | Run the same phrase with different drawing loads. Measure note boundaries and missed updates. Separate note duration from the waveform period; distinguish a frame-driven player from the audio hardware’s own clocks. |
| 4. Coordinate voices | Per-voice state and shared clock, where hardware supports voices | Add bass or an answering line, then mute it. Hear harmony and space; document which voice does which job. CPU-synthesised polyphony is a separate beeper investigation, outside v1. |
| 5. Instruments and effects | Base pitch, envelope state, gate/retrigger, reset rules | Change one instrument parameter; add vibrato or a slide without accumulating pitch error. Restore the unmodified instrument on the next note. |
| 6. Patterns and song order | Repeated phrases, independent indices, bounds | Store two small patterns and an order such as A–A–B–A. Compare bytes before/after reuse and decoding time; identical music must survive the representation change. |
| 7. Game effects and ownership | Event requests, priorities, per-voice music state | Trigger a cue during music, inspect the stolen role, reject a lower-priority request, and restore the instrument at the stated musical boundary. Hear what was sacrificed. |
| 8. Time and memory costs | A working baseline and explicit game deadlines | Compare ordinary ticks with row changes, simultaneous effects and sample fetches where relevant. Improve a measured cost, then recheck pitch, rhythm, articulation, input and memory use. |

## Spectrum: beeper first, AY at the 128K

The stock 48K beeper has a CPU-driven output bit, not a bank of hardware oscillators or a volume envelope. Waveform generation consumes timed CPU work. The musical scheduler determines when notes occur; it does not generate their edges for free. Original beeper techniques can combine tasks, but that requires a separate scheduling/synthesis design.

| Existing location / proposed extension | Prerequisites | Exercise and audible outcome | Boundary |
|---|---|---|---|
| Bright Spark BASIC unit 02, then recall in unit 04 | Existing panel cue, `BEEP`, routine parameters | Hold duration fixed and change one panel’s pitch; restore it and change duration. Hear identity versus rhythm, then inspect when input can be accepted. A missing pitch assignment deliberately makes a panel inherit the previous cue. | **First change, v1.** Retain visual equivalents and accepted game behaviour. No custom player or assembly prerequisite. |
| Gloaming unit 18, linked from the existing machine sound explanation | Z80 loops, output port, routine contract | Compare two pulse shapes by redistributing high/low time while preserving the full measured period, including instruction overhead. Hear timbre at nominally fixed pitch. Measure the input gap caused by a longer sound. | Optional assembly v1 investigation. BASIC `BEEP` does not expose a duty knob. No claim of hardware volume control. |
| The Long Night unit 08 and Shadowkeep unit 18 | Existing beeper routine, tables and keyboard polling | Play the study as note/duration/rest data. Compare pitch-dependent chunk timing with durations calculated from elapsed time. Poll at bounded safe points; record response delay and any gaps introduced into the tone. | One sequential voice, interruptible title playback. Preserve the games’ existing phrases; use the study as a separate comparison. |
| Shadowkeep unit 18 companion | Timing-aware note boundaries, pitch table | Start with slow C–E–G notes, then shorten each in turn to make a rapid arpeggio. Add a small alternating pitch offset, then a one-way slide, separately. Hear harmonic suggestion versus buzz, unstable pitch and lost articulation. | Optional deeper 48K study; no simultaneous bass, per-voice ADSR or hardware fade. Diminuendo echo is deferred to AY rather than pretending shorter beeps are quieter. |
| Starfall’s planned 128K opening | Explicit 128K target, AY register access; earlier beeper lesson is optional context | Trigger a tone, then noise; compare fixed amplitude with a software volume contour and the shared hardware envelope. Grow a data phrase into three voice states on one musical clock. | Provisional later placement. AY has fixed square tones, shared noise and a shared envelope generator; no SID-style waveform selector or programmable pulse duty. |
| Starfall’s planned music/game integration | Three roles, tick state, instrument restoration | Melody, bass and alternating arpeggio/percussion roles; quiet repeated notes suggest echo. Let a warning borrow a chosen voice, then restore music. Add two patterns and a short order; profile row/effect updates. | Later bounded AY v1: one short piece, explicit shared-resource policy, one priority rule. Advanced beeper polyphony, sample tricks and general tracker import remain outside. |

AY contour and noise changes may affect more than the currently selected voice. Make that a controlled failure: change the shared envelope for percussion and listen to what happens to the held melody. A per-voice software volume contour is an alternative with an update cost. Compare these choices rather than describing three wholly independent instruments.

## C64: build instruments as well as a SID player

| Existing location / proposed extension | Prerequisites | Exercise and audible outcome | Boundary |
|---|---|---|---|
| Bleeper units 01–03; assembly Meet the Machine unit 15 | BASIC `POKE` or assembly register stores, pitch and gate | Compare triangle, sawtooth and pulse at the same frequency; vary pulse width with frequency fixed. Treat noise separately because it is not a pitched waveform comparison. Shape attack and decay, then compare a recognisable panel cue with a blurred one. | Early v1. BASIC listening work is optional context for assembly. Use the named SID model and moderate output. |
| Starfield units 05 and 08 | Direct voice setup, per-update effect state | Keep the firing event fixed; compare a falling laser pitch with a small vibrato and an excessive one. Shape a short noise explosion. Decide which sound says “shot” and which obscures repeated firing. | Game effects before a music engine. Reset pitch and envelope state on every new effect. |
| Starfield unit 17 companion | Tables, duration counter, state transitions | Use the study to explain notes/rests and a measured clock; play slow then rapid chord tones on one voice. Compare title voice handover with a deliberately unrestored laser envelope. | First-game v1 stops at its small phrase player and explained handover. Do not add a whole soundtrack under combat here. |
| Planned SID Symphony, instrument studies | Three oscillator roles, ADSR and filter routing | Compare unfiltered and low-pass versions with the same notes, then move cutoff. Demonstrate oscillator synchronisation; separately demonstrate ring modulation using the required triangle output and linked oscillator. Change the partner pitch and hear the result. | Deeper studies, one control at a time. The shared filter can affect other routed voices; sync/ring-modulation dependencies constrain the partner’s musical role. These are not free effects on an isolated channel. |
| Planned SID Symphony, arrangement/player | Reliable interrupt tick, per-voice state and event data | Melody/bass/percussion across three voices; alternate bass and chord tones in one voice. Add small vibrato and slides separately. Compose softer answering repetitions using deliberately shaped ADSR articulations, then compare cluttered and sparse versions. Introduce two patterns and an order. | Bounded later v1: one short original piece and a small documented effect vocabulary. No universal SID-file player. SID has no general independent voice-volume register; sustain is not a linear volume knob for an entire note. Check the whole echo envelope, including its attack. |
| Planned Catacombs; later Maelstrom budget revisit | Player, shared filter ownership, IRQ/main-loop contract | Give a warning precedence over a musical role. Compare continuing silent music state with pausing it; select resumption on the next note boundary. Test all voices changing while display work is busy. | One deterministic stealing policy first. Maelstrom is a later integration stress case, not a prerequisite. |

Keep 6581/8580 configuration explicit for filter listening and do not promise identical cutoff sound. Filter sweeps can bury a melody; long release smears rhythm; rapid arpeggios compete with articulation. A modulator oscillator can still have a musical use, but its pitch is now coupled to another sound: explain the arrangement compromise rather than counting it as either automatically free or automatically lost.

## NES: arrange for unequal voices

| Existing location / proposed extension | Prerequisites | Exercise and audible outcome | Boundary |
|---|---|---|---|
| Meet the Machine unit 17 → Dash unit 05 | Pulse registers, timer, gate/length and envelope distinction | Retain the existing same-pitch duty comparison. Compare a short decay with a software-controlled attack followed by decay; distinguish this from the pulse sweep unit. Use the result for the jump cue. | Early v1. Pulse/noise hardware envelopes provide decay, not a SID ADSR generator. |
| Dash unit 11 and damage cue | Two pulse states, event trigger | Compare assigning jump and collection separate pulses with letting a high-priority cue interrupt one. Hear a lost note, then restore the next note’s duty, volume and pitch. | Small deterministic ownership experiment, with visual feedback preserved. |
| Dash unit 17 companion | Its existing period/duration/rest player, main/NMI ownership | Play the study and retain its rests; compare slow and rapid pulse arpeggios. Add restrained software vibrato or a slide, then remove it. Separate sequencer timing from the APU’s internal frame sequencer and from NMI frequency. | First-game v1: one phrase player and ending cues. No requirement to rewrite Dash around a new engine. |
| Planned Thunder Run, arrangement | Separate voice state and a reliable musical tick | Pulse melody and answer; triangle bass; noise percussion. Borrow pulse 2 between harmony and echo, leaving gaps. Compare bass articulation by note length: triangle has no pulse-style duty or volume envelope. Noise controls texture/rate, not an ordinary pitched-note line. | Later v1 core: four generated voices, not four interchangeable instruments. Quiet echo belongs on a pulse with volume control, not a pretend triangle fade. |
| Planned Thunder Run, instruments and structure | Pulse/noise volume updates, base pitches, note start semantics | Add two instrument definitions, limited pitch/volume effects, two patterns and song order. Keep melody clear while a priority effect steals pulse 2 or noise. Compare resuming the music at its next note with restarting the interrupted note. | One piece, one chosen ownership policy and bounded data. No expansion audio, general NSF player or arbitrary tracker compatibility. |
| Thunder Run companion: DPCM study, then budget comparison | ROM layout, sample conversion, DMC control and DMA interactions | Encode one original short percussion sample for DMC playback. Compare it with noise percussion, then vary the available playback-rate setting. Hear changed pitch/duration and encoding texture; measure ROM bytes and CPU fetch costs while reading the controller. | Bounded advanced study, not required by Dash or the initial four-voice player. Include before claiming five-channel integration. No arbitrary PCM stream or freely tunable sample instrument. |

DPCM is the encoded data; DMC is the playback unit. It has discrete rates and address/length constraints, not the pulse envelope/duty interface. Do not treat its DAC level as a normal per-note volume control. Validate sample termination and controller handling on the selected region: DMC DMA can interfere with CPU/controller timing. A faster musical tick does not fix a wrong regional pitch or noise/DMC rate table.

Excess vibrato can hide the melody; repeated high-register writes can change articulation by retriggering pulse phase. A stolen bass or percussion voice may be more damaging than a missing harmony note. Let readers hear those choices rather than hard-code “newest always wins” as musical wisdom.

## Amiga: samples become instruments and arrangements

| Existing location / proposed extension | Prerequisites | Exercise and audible outcome | Boundary |
|---|---|---|---|
| Meet the Machine unit 18 → Flock unit 11 | Chip RAM, sample address/length, period, volume and DMA enable | Compare two equal-length, single-cycle waveforms at the same period; hear a different timbre with the same repetition rate. Then change playback period and hear pitch and duration change for a finite sample. | Early v1. Sample length/loop length matters: preserving the period alone does not preserve the pitch of differently sized waveforms. |
| Flock unit 11 companion | Its `soundtick`, bounded volume state | Shape attack and decay through sample data first, then compare a software volume contour. Choose and inspect a loop boundary; hear a click from a deliberate discontinuity and repair it. Compare a short articulated baa with overlapping retriggers that become a drone. | One channel initially. Paula streams samples; it does not supply a SID ADSR or a universal automatic attack/sustain-loop instrument. Explain the software/DMA handover for an attack followed by a loop. |
| Flock units 17–18 companion | Existing phrase table and sound tick | Play the study with rests and clear note ends. Add one answering part on a second channel; stop it to hear the difference. Compare pitch slide and small period modulation separately. | First-game v1: up to two voices in the optional experiment, with the accepted full game retained as baseline. No full MOD replayer. |
| Planned Onslaught, four-channel arrangement | Sample instruments, per-channel state and musical clock | Assign melody, bass, harmony and percussion; alternate harmony and echo in the fourth channel. Compose diminishing repeats using channel volume, then hear how the tail obscures the next phrase. Put a slow triad and then a rapid arpeggio on one channel. | Four hardware DMA channels, no extra software-mixed channels. Note the fixed stereo channel placement and audition the balance. |
| Planned Onslaught, tracker concepts | Rows, ticks, instrument numbers, per-channel effect state | Build two short patterns and an order; distinguish row advance from per-tick slides/vibrato/volume changes. Compare reused pattern/sample storage with duplication, including decoding and memory costs. | A small documented educational format first. A fixed subset is not a compatible MOD player; full MOD replay remains a later integration with a separately stated format/effect contract. |
| Planned Onslaught, game integration | Player state, event queue and channel ownership | Reserve a channel for effects, then compare borrowing the quietest chosen musical role. A priority cue steals it; music state advances silently and returns on a note boundary. Test row changes with active display DMA and all four audio streams. | One policy, one original piece, a few effects. Explain sample restart/loop state and Chip RAM requirements before optimising. |

A baked-in echo consumes sample memory and repeats whenever that sample is played; a separately scheduled echo consumes a channel or displaces a role. Neither is a free delay effect. Too much modulation of sample playback can make an instrument wobble rather than sing, and transposition changes its spectral character as well as pitch. Let the arrangement leave room instead of solving every conflict by adding channels.

## Clock, ownership and measurement contracts

The [timing and interrupts implementation plan](timing-and-interrupts.md) owns
the detailed lesson repairs, hardware service contracts and four rate/budget
experiments. Trace a playback update before teaching interrupts as its scheduler.
The [profiling progression](profiling-progression.md) supplies the recurring
measurement practice and checked tool boundaries for these investigations.


Begin each target with one named configuration: 48K PAL beeper, then a named 128K AY machine; PAL C64 with a named SID model; NTSC NES for the existing initial pulse experiments; and a named PAL Amiga/Chip RAM configuration. Confirm these against the maintained sample before authoring. Regional portability is a subsequent explicit comparison, not an implied success claim.

Keep musical time distinct from display cadence and oscillator/sample clocks. For example, the proposed 120 BPM study needs half-second quarters; a frame-count representation must account for the actual update frequency. Later compare a fixed frame divider with an accumulator or suitable timer-based schedule. Explain rounding and jitter; do not merely substitute “60” for “50”. Retune pitch/rate tables where needed and measure the resulting note durations separately. On NES, the APU frame sequencer is not the same clock as the game's NMI music tick; on Amiga, a simple vblank study does not establish tracker tempo compatibility.

For hardware audio, choose one routine as the owner of register writes. Main code posts bounded requests; the playback update commits a consistent state. Teach the target’s safe handoff before sharing multi-byte data with an interrupt. For beeper audio, define the CPU-owned sound interval, interrupt behaviour, input polling opportunities and return state instead of copying that hardware-player contract.

The first stealing experiment uses an explicit priority order, a rule for ties and a defined end: a warning can replace a collection cue, which can replace decoration; a lower-priority request cannot restart the warning. The exact musical channel remains a game design choice. Inspect music state and hardware state separately. Compare “pause the musical part” with “continue its clock silently”; select one and show exactly when restoration happens. Shared AY envelope/noise or SID filter resources need ownership as well as channel numbers.

For each implementation, retain source and data sizes, target/emulator configuration, an input/event schedule, before/after audio and a measurement boundary. Period methods include cycle accounting, border/raster markers where supported, and timers. Modern tools include verified cycle traces, debugger views and waveform/note-onset inspection. Account for instrumentation cost; host/browser elapsed time is not emulated CPU cost.

Measure at least idle/held-note ticks, new notes, simultaneous voice changes, loop/order transitions, effect requests and the busiest game state. Include CPU waveform generation for beeper, register/update work for chip audio, and DMA/bus costs for sampled playback. Report worst observed time separately from a proven bound. Define the deadline from the game’s existing frame/input contract before optimising; do not invent a universal music percentage. Try table lookup, fewer redundant writes or compact data only after identifying the cost, and recheck that articulation has not changed.

## Evidence and source work before lesson implementation

Hardware assertions are checked against the family reference library and must cite public original documents precisely in authored lessons. Do not use a curriculum pattern as hardware authority. Useful anchors for this plan are:

- Sinclair, *ZX Spectrum BASIC Programming*, chapter 19, “BEEP”; the Sinclair 128 documentation for machine-specific AY access. Recheck cycle-counted experiments against the actual Z80 source and named memory/interrupt conditions.
- General Instrument, [*AY-3-8910/8912 Programmable Sound Generator Data Manual*](https://map.grauw.nl/resources/sound/generalinstrument_ay-3-8910.pdf), operation sections 3.1–3.5: tone, noise, mixer, amplitude and shared envelope. Its register numbering is octal; translate explicitly before presenting decimal register numbers.
- MOS Technology, *6581 SID datasheet*, “SID Register Description”: voice frequency/pulse width, control bits SYNC/RING MOD, envelope registers and filter controls; available in the [Commodore chip-data archive](https://www.zimmers.net/anonftp/pub/cbm/documents/chipdata/6581.zip). The local manufacturer extract was inspected for modulation dependencies. Claims about model-specific sound require named-model listening evidence as well.
- Commodore-Amiga, *Amiga Hardware Reference Manual*, second edition, chapter 5, “Audio Hardware”: sample storage, period, volume, DMA and channels. Use the original register descriptions when implementing loop handover, not a simplified pattern skeleton.
- NES: the family APU reference separates public experimental documentation from restricted-provenance material. Before authoring the DPCM extension, establish publicly citable register/DMA evidence and execute the sample/controller checks. Do not publish restricted source details or treat the existing sweep workaround as a universal hardware rule. This plan contains no verified new NES implementation.

The Solstice recording remains inspiration under the parent specification. None of the experiments here is attributed to that track. Review Vault entries for sources and review status; update reusable patterns only after the corresponding concrete implementation has been checked.

## First deliverable and v1 completion

Implement the queued **Bright Spark unit 02 companion comparison**, with a short recall in unit 04 if useful. Keep pitch and duration changes separate, retain the visual cue, supply a missing-assignment fault and recovery, and expose cue timing without adding an engine. The default program and accepted game remain the baseline. Inspect and listen on the named 48K PAL target; compare an earlier/new cue, held input, successive panels and restart. If the extra material crowds the existing lesson, keep it as a linked focused experiment.

This establishes the pattern for later work: predict, change, hear, inspect, explain, apply to the game. Delivery order after it is proposed, not newly agreed: one small first-game audio extension on each other system before developing the later players. Do not commission four advanced engines together.

A v1 lesson is ready when its source and target assumptions are explicit, its one-variable comparison is audible, a learner can explain the musical trade-off, its deliberate fault is recoverable, and its timing/memory claim has matching evidence. New engine stages need their own small reviewable checkpoints. The later-system v1 limits above are planning boundaries, not release commitments or claims of existing implementation.


## Shared audio pattern review

C03a corrects `website/src/content/patterns/cross-platform/audio/making-a-sound.mdx`
locally, ready for review. It retains the completion-mismatch exercise and replaces
unsupported hardware rankings and instrument equivalence with explicit costs.
The excerpts are illustrative register/loop fragments, not complete runnable
programs. No curriculum game or machine sample changed.

Source-checked register/state walkthrough, 22 September 2026:

| Fragment | Starting assumptions and resulting state |
| --- | --- |
| Spectrum | Valid stack; supplied delay preserves B. B=50 produces 50 high/low pairs, leaving speaker bit 4 low. Both writes set border/MIC bits to zero. Total loop timing controls pitch; no calibrated note or duration is claimed. |
| NES | APU/interrupt setup supplied; exclusive ownership. $4015=$01 enables pulse 1 and disables others. $4000=$BF selects 50% duty, halted length and constant volume 15; $4001=$08 disables sweep with negate set; $4002/3=$FD/$00 loads timer $0FD and non-zero length. Playback continues until stopped. |
| C64 | I/O visible, other voices silent, SID owned. $D402/3=$00/$08 sets half-cycle pulse width; $D405=$09 sets attack/decay; $D406=$F9 sets sustain/release; $D404 transitions from $00 to $41 for pulse plus gate. Shared filter routing and master volume are explicit. Release uses $40, not an instantaneous-silence promise. |
| Amiga | Custom base and offsets supplied, audio ownership established, channel DMA initially off and modulation disabled. Word-aligned signed sample bytes remain in Chip RAM; length is in words; volume=64; $8201 sets DMAEN/AUD0. Period controls sample rate, not a universal note name. |

Hardware authority is linked in the page: Sinclair BASIC Programming chapter 23,
MOS 6581 register descriptions, NESdev APU/pulse/sweep/DMC hardware research,
and Commodore's Hardware Reference Manual audio chapter. This is source and state
reasoning, not an emulator trace, original-hardware result or subjective listening
trial. The existing caller exercise still contrasts waiting until completion with
returning after starting playback; a separate learner trial remains pending.

The directly linked standalone examples need bounded follow-up, recorded under
C03a in `work.md`. In particular, the Spectrum excerpt's variable repetition count
must not be mistaken for a changing edge delay, and Amiga period 428 does not
establish the pitch of an arbitrary sample. Those pages are not claimed corrected
by this comparison-page change.


## Shared audio presentation review

R4c reviews `patterns/cross-platform/audio/making-a-sound.mdx` after C03a's register/ownership corrections. The conceptual comparison now comes before the assembly; four native disclosures retain each fragment's prerequisites and related links. The core cue-completion question is readable without learning four assembly syntaxes. The prediction separates when a call returns from when the cue ends. Amiga prose now distinguishes the time to traverse a sample block from the overall duration chosen by a looping cue's software player.

The register fragments are unchanged by R4c, and their earlier C03a evidence retains its scope. This pass rechecked the Spectrum port allocation against Sinclair chapter 23, NES sweep-disable/negate behaviour against NESdev's APU Sweep research, and the sample-period relationship against Commodore's Hardware Reference Manual [equal-tempered scale section](https://amigadev.elowar.com/read/ADCD_2.1/Hardware_Manual_guide/node00F0.html). No four-platform assembly, new audio capture, subjective listening or original-hardware test is claimed.

The linked `tune-sequencer` page is covered by the sequencer contract review below, including its frame-rate/write-count/retrigger claims and unbounded sentinel-loop example. The four linked machine audio pages retain the separately listed C03a repairs. This presentation review does not certify those pages or replace their executable checks.

Validation: an isolated Astro build completed all 2,468 pages. Chromium checks passed all five disclosures at 390px and 1280px in light and dark themes (20 combinations), including keyboard activation and no document-level horizontal overflow. Mobile and desktop screenshots were inspected. These checks establish rendered presentation, not native audio behaviour.

## Sequencer contract review

R4e corrects `website/src/content/patterns/cross-platform/audio/tune-sequencer.mdx` and the repeated register-write claim in `website/src/content/curriculum/commodore-64/assembly/starfield/unit-17.mdx`. The pattern links the four actual lesson locations, gives a bounded schematic player in the shared pseudocode notation, and asks for an event trace before revealing it. This is an explanatory alternative, not a replacement engine or a change to game rhythms.

Source review used `code-samples/commodore-amiga/assembly/flock/unit-{17,18}/flock.asm`, `commodore-64/assembly/starfield/unit-17/steps/step-04.asm` and `nintendo-entertainment-system/assembly/dash/unit-17/dash.asm`:

- Flock tests zero before decrementing and returns after the decrement. A duration D produces D + 1 calls between row starts; its loop marker consumes a separate call. Unit 18's stop leaves the pointer on the marker; `soundtick` ends the timed sound. `playsound` loops eight sample bytes, and the title calls `soundtick` after `tunetick`, decrementing a newly installed sound timer in the same update.
- Starfield initialises to one and decrements before testing. Its sounding path writes four SID registers; its rest discriminator is the high frequency byte alone. Its loop assumes a valid first row, and title/game transitions transfer voice 1 and its envelope between music and the laser.
- Dash also initialises to one and decrements first. Duration markers precede note handling; ordinary duration bytes are 1–253. Its immediate loop can hang on malformed LOOP-only data. The byte index and high-byte active flag impose explicit table-placement assumptions. Its sounding path writes four APU registers; playback advances in the main loop after a one-bit NMI notification.

The manufacturer sources checked were Commodore's *Amiga Hardware Reference Manual*, Audio Hardware (waveform repetition and stopping), and MOS Technology's *6581 SID datasheet*, Voice 1 control and envelope descriptions (release and attack from the current envelope level). NES pulse/envelope/sweep claims were checked against NESdev's linked hardware research. Public reference links are on the pattern page. The web mirror of the Amiga manual timed out and the SID PDF was unavailable through the browser tool; their original-source text was consulted instead.

Seven small host-model cases pass: the worked NOTE/rest/NOTE/STOP trace, LOOP-only, empty table, zero duration, excessive duration, missing ending and a valid repeating phrase. Separate source-order countdown sketches give starts 1/3/5/7/9 for decrement-first duration two and 1/4/7 for Flock's test-first order. These establish the explanation's arithmetic, not guest execution, subjective articulation or hardware accuracy. No game source or audio recording was changed; no new native playback or original-hardware test is claimed.

The actual built-in players retain their compact trusted-data assumptions. General loaded-data validation or changes to Flock's rhythm would be separate implementation work with native playback checks. C03a's individual machine-pattern repairs remain queued; this correction does not certify those pages. A learner trial of the new prediction remains pending.

Validation: the isolated Astro build completed 2,468 pages. Both edited routes passed mobile/desktop and light/dark checks (eight combinations), with keyboard access to the prediction answer and no document-level horizontal overflow. The eight internal link occurrences across the two pages resolve in the generated site; mobile and desktop trace screenshots were inspected. Whitespace checks pass.
