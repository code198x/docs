# Timing and player feedback

**Status:** Source-audited progression with local lesson additions to Bright Spark unit 04, Touchdown unit 05 and Game Feel unit 01. These are authored comparisons and explanations, not new runtime features or completed native listening/latency trials. Later experiments remain proposed. Current systems: Spectrum, C64, NES and Amiga.

The [timing/interrupt plan](timing-and-interrupts.md) owns clock arithmetic and hardware contracts. [Audio](audio-progression.md) owns instruments, arrangement and playback; [profiling](profiling-progression.md) owns measurements; [scheduling](scheduling-ownership-headroom.md) owns handoffs and overload decisions; [diagnosis](testing-and-diagnosis.md) owns predictions and regression evidence. This plan connects those mechanisms to the information and response a player experiences. It adds no universal loop architecture or new standalone module.

## Existing coverage and gaps

Paths below are relative to website `src/content/curriculum/`; sample paths use the matching system/game in code-samples.

| Inspected location | Existing teaching | Gap / local improvement |
|---|---|---|
| Spectrum BASIC Bright Spark 02/04 and unit 04 `opening/.../steps/step-02.bas` | Distinct pitches, digit/asterisk/brightness, CPU-blocking BEEP, interruptible PAUSE, input checks before cues and after the last | Unit 04 now compares 0.15 and 0.45 second notes, no-key rhythm and held-q response, prediction before explanation, muted observation and explicit restoration. The larger unit 02 pitch/fault/native-verification task remains open. |
| Spectrum BASIC Volley 05 | Candidate position, resolve contact, commit state, then draw | Later event-to-cue exercise can use the confirmed return/miss decision; do not trigger a hit from proximity or speculative contact. |
| Spectrum BASIC Touchdown 05 | One `burn` decision drives fuel, velocity and flame; final fuel unit still fires; empty tank can coast | Local prediction/interpretation exercise distinguishes accepted input, unavailable thrust and failure. No warning sound is added. |
| Craft Game Feel 01/02/04 | Fixed 1/60-second comparison, same recorded input, inspect-one-update; immediate response versus acceleration/reversal | Unit 01 now names its fixed simulation step and separates it from display/input/audio rates. Its browser model is not a regional retro-hardware measurement. Existing local review status is unchanged. |
| C64 Starfield 17 | Title/laser handover, ending dwell, deterministic parked-player comparison and full-width enemies | Add feedback experiments after tracing events; frame countdowns and envelope settings answer different timing questions. |
| NES Dash 11, with timing plan's 14/17 audit | Collect event updates state and requests triangle audio; pulse jump cue; later timing/transition work | Strong claims that a note necessarily feels rewarding need listening evidence. Unit 11's triangle gating, linear-counter duration and nominal frame-derived explanations need hardware review before reusing them as an envelope recipe. Do not transplant a SID amplitude-envelope exercise to triangle. |
| Amiga Flock 11/17 in audio/scheduling audit | Sound request, countdown, half-time pitch change, retriggers and phrase updates | Compare perception of replacement and repeated cues after understanding existing ownership. Samples and software updates are distinct from a SID envelope generator. |

Most gaps are comparisons and explanations, not absent mechanisms. Input-to-output timing measurement and a repeatable feedback review are later teaching responsibilities. Preserve independent entry routes: recall the relevant distinction locally rather than require Foundations or every earlier system game.

## Six clocks, introduced when they matter

| Timing concept | Question we ask | First useful distinction |
|---|---|---|
| Display refresh | When does the display scan or present another picture? | A refreshed picture need not contain a new simulation state; permitted graphics-transfer windows are smaller and machine-specific. |
| Input sampling | When does the program observe the control? | A press after the last sample waits; a short press between samples may be missed. Held input and an accepted action are different. |
| Simulation updates | When do rules, position, collision and score advance? | A step's movement and timers have meaning relative to its chosen update rate. Faster drawing alone should not award more score or advance more collisions. |
| Animation timing | When does artwork or a visual cue change? | A walk cycle can advance every few updates; changing its pace need not change position. If an attack frame defines a hit window, that is an explicit gameplay contract and cannot be varied as decoration. |
| Musical/effect updates | When does the player service a note, duration, arpeggio or software envelope? | An event countdown measures player updates, not necessarily screen frames or milliseconds. |
| Sound generation | When are waveform edges or sample values produced? | CPU-driven Spectrum beeper edges require CPU time. SID/APU/AY/Amiga hardware can generate output between software updates, under their different contracts. A late note request differs from disturbing an already generated waveform. |

These are responsibilities, not a demand for six independent timers. Begin with sequential code or a simple frame-driven loop. Draw a short schedule before introducing an accumulator, timer, interrupt, buffered input or deferred rendering. Choose the smallest change that meets the actual game's need. Neither variable delta time nor a modern fixed-update/interpolated-render loop is the default prescription for all four systems.

At nominal 50 and 60 updates/second, six updates last 120 and 100 ms respectively. If movement is two pixels per update, that gives 100 and 120 pixels/second. The unchanged sequence runs 20% faster at 60; nominal 60 Hz frames are about 16.67 ms, nominal 50 Hz frames 20 ms. Animation, protection and software effects can change too. Actual model/mode clocks, integer rounding and audio tuning require the timing plan's separate checks. Do not promise exact PAL/NTSC conversion by scaling one number.

## From a press to information

Trace: **physical action → sampled input → accepted/rejected action → changed game state → prepared picture/sound request → visible/audible result**. A sound may begin before the next picture is scanned; a draw call is not a measured photon, and a register write is not a measured sound at the listener. Emulator host buffering and output devices add their own latency. Guest traces establish guest boundaries; an end-to-end measurement needs a separately described method.

Use the same accepted event to drive rule changes and feedback. Touchdown's last burn should move the craft and show a flame even though fuel has just reached zero. Volley's return sound belongs after the collision rule accepts contact. A denied action should not reuse the success cue merely because the key was read. No new generic event bus is needed to explain this.

Give each cue an intended meaning before choosing an effect:

- **Success:** confirm the accepted event and resulting progress; do not celebrate an unaccepted request.
- **Damage:** identify a lost life or changed state, and explain any temporary protection separately.
- **Danger:** warn early enough to act; it is not evidence that damage already occurred.
- **Unavailable action:** explain a resource or rule limit without implying failure of the whole attempt.

A technically correct effect can be weak because its start is hard to notice, confusing because it resembles another event, or late because servicing follows long blocking work. Louder, longer or more animated does not automatically mean more informative. An exaggerated animation may communicate weight while making exact collision boundaries harder to judge: name that trade-off.

## Staged comparisons in existing games

Each row is a bounded proposed experiment unless labelled local. Reset to the same state/input sequence, predict, compare one change, describe information gained/lost, restore, then check the relevant rule. Use the diagnosis method without turning every playtest into a large test harness.

| Placement and prerequisite | Controlled comparison | Outcome and checks |
|---|---|---|
| **Local: Bright Spark 04**, after cue subroutines and input reads | Change only BEEP duration 0.15 → 0.45, holding pitch/order constant. Compare no-key rhythm separately from held-q response; repeat muted. | Explain that the same number changes note length, highlight length and when input is next checked. Report perceived differences without claiming exact human key timing. Restore 0.15 and verify final-panel quit/rest. |
| Bright Spark 02/04, existing queued audio task | Separate pitch-only and duration-only trials; the already proposed missing-note-assignment fault. Then use a stored repeated panel to examine the return-to-rest gap. | Identify panel/order without colour or sound alone; distinguish repeated events from one sustained cue. Native audible and timing evidence remains to gather. |
| **Local: Touchdown 05**, after fuel and `burn` | Predict last paid burn versus next held-key update. Compare flame, fuel and motion; ask a learner to explain unavailable thrust versus a finished attempt. | Explain why a key-driven flame would mislead. Preserve safe coasting and retry state; feedback must reflect accepted simulation state. |
| Volley 05 → final game; Game Feel 01–04 | Later isolate delayed presentation of an accepted return versus delayed sampling in two separate fixtures. In the Craft model, retain identical input and movement rules when varying a presentation delay. | Distinguish input delay, intentional acceleration and late drawing. These are proposed fixtures; existing MovementExperiment has no assumed delay control. Verify rally rules/state remain unchanged in presentation-only case. |
| Starfield 17, after SID ownership | Compare one attack/decay setting with pitch and event schedule fixed, then restore. Separately compare result dwell lengths. | Describe immediate onset versus softness and whether the result is understood before retry. Measure register/event timings separately from perceived onset; preserve laser restoration and state transitions. |
| Dash 11/14/17, after APU factual review | Remove only the collection sound in an isolated comparison, retaining coin removal/score; later delay just its request by a bounded amount. Compare jump plus collection with either alone. | Identify collection when muted and explain a delayed cue that seems attached to the next action. Preserve one collection/one score event. Use pulse/noise or the appropriate sample/software technique for envelope experiments; do not invent triangle volume control. |
| Flock 11 → 17, after sound ownership | Reverse closely spaced request order; later compare a bounded repeat policy with every-update retriggering in a fixture. Change a sample attack separately from countdown/pitch, when sample preparation is taught. | Explain interrupted articulation, lost cues or masking. Compare same-priority/tie outcomes; no repeated rule events generated merely to repeat feedback. Keep accepted/rejected diagnostics from the scheduling plan. |
| Later animation integration: Dash/Thunder Run, Flock/Onslaught | Change decorative frame duration while holding simulation/collision state fixed; separately introduce an intentionally conflicting success/damage cue in an isolated fixture. | Name the actual rule and the misleading signal. Repair the cue mapping; test frame-linked gameplay windows separately rather than assuming animation is always cosmetic. Later module placement requires its agreed brief. |
| Meteor Storm 20; later regional audio companions | Reuse the bounded slow-path fixture and 50/60 player-rate comparison, not a new benchmark. Track input sample, simulation event, presentation and note request boundaries. | Distinguish lost updates, repeated pictures and late service; preserve course events/collisions. State which deadlines slipped and what the player noticed. |

For “remove a cue”, retain another clear route to essential information. For “delay”, use a short bounded fixture, not a shipped disadvantage. For conflicting cues, explain the conflict afterwards and restore the accepted mapping. Do not introduce intense flashing to demonstrate that it is unpleasant.

## Busy scenes, missed updates and repetition

A once-per-loop countdown slows when that loop misses its expected opportunity. Hardware audio may sustain its prior state; CPU beeper generation can fail differently. A repeated picture does not alone prove the simulation stalled, nor does smooth music prove input is being serviced. Use the profiling plan to expose the named boundary.

If a later game needs recovery, choose explicitly among optimising required work, reducing optional presentation, deferring preparation, or a bounded scheduling change. Catch-up can bunch sound requests and repeat feedback; skipping authoritative simulation can lose hazards and collisions. Preserve essential state/events and document any deliberate slow-motion or pause policy. A catch-up limit needs an overload policy, not silent deletion of elapsed game work.

Repeated damage during contact, held-key “unavailable” warnings and musical channel stealing ask related but different questions. Decide whether a cue represents a transition, each accepted event, a continuing state or a reminder. Coalescing optional reminders can be sensible; it must not coalesce away separate score or damage events. A quiet or omitted echo may leave a warning clearer. Tie rules and deterministic input schedules help reproduce what the player heard.

## Proportionate accessibility and creative judgement

Use existing digits, shapes, positions, text and state changes alongside sound/colour. Test important events with sound muted and ask whether colour alone carries a distinction. Keep contrast and stable landmarks readable. Where flashing, shake or dense repeated effects are introduced later, provide an avoidable/reduced version while preserving the information and rules. Do not claim formal accessibility compliance from these small checks.

Ask “What happened?”, “What could we do next?” and “Which cue told us?” before explaining the intended answer. Record both state/timing evidence and a person's description; preferences can differ. A cue that works alone must also be tried during the named busy scene. Describe the trade-off and choose for the intended action, rather than treating one person's favourite envelope as universal.

Connect backwards to Foundations state/decisions and Game Feel controls; use the existing blink-on-a-clock, grace-window, ending-dwell and input-edge patterns only after checking their assumptions against the actual game. Vault animation/audio context supplies sourced precedent, not proof of what a player perceives.

## Next bounded work and v1 boundary

1. Local prose/comparisons above are authored; working samples remain unchanged. Check arithmetic, links and MDX; do not claim performed native hearing or input-latency measurement.
2. Complete the already queued Bright Spark unit 02 pitch/duration/fault companion and its named 48K PAL native listening/cue-boundary checks. Include the unit 04 comparison in that trial; the local lesson addition does not close the broader task.
3. Review Dash unit 11 APU claims against authoritative/public hardware references before developing its sound-removal/delay companion. The review is actionable work at that exact lesson and sample, not a claim that its timing account has been corrected.
4. Add one Starfield or Flock event comparison alongside the existing ownership task, then reuse Meteor Storm's profiling fixture. More capable scheduling and regional correction wait for the actual requirement and prerequisite lessons.

V1 needs no universal event framework, synchronisation engine, latency dashboard, variable-delta conversion or four replacement audio drivers. Completion of each later exercise means the learner can connect an implementation change to a predicted timing/information change, explain the observed feeling, and show that the game's promised rules survived.
