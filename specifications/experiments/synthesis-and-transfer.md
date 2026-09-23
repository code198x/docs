# Synthesis and transfer at project milestones

**Status:** Bounded source audit and local exercises in Spectrum Volley unit 05 and Amiga Flock unit 11. These add guided/independent traces and transfer questions; they do not change game samples or claim new native execution. Wider coverage remains proposed. Current systems: Spectrum, C64, NES and Amiga.

Apply [unit question conventions](../unit.md), [curriculum design](../curriculum.md) and the [recurring progressions](../recurring-progressions.md). Use the existing [diagnosis](testing-and-diagnosis.md), [timing/feedback](timing-and-player-feedback.md), [ownership](scheduling-ownership-headroom.md), [portability](abstraction-and-portability.md), [revisit](working-with-existing-code.md) and [delivery](finishing-and-delivering.md) work as material. This plan coordinates occasional synthesis milestones, not a new assessment layer on every lesson.

## Audit: where copying can stand in for understanding

This is a content audit, not a claim about what actual learners understood. Complete listings are valuable recovery points; their presence is not itself a defect. Risk is higher when the only observable task is to enter the given code and see the supplied result.

| Inspected material | Existing strength | Copying risk / action |
|---|---|---|
| Spectrum Meet Assembly 08 and `DebuggerLesson.astro` | Hypotheses, actual stepping, folded repairs, a second fault with less guidance | A model for gradual independence; retain rather than add another test UI. |
| Bright Spark 06/07 and Sonar 09 | Recent prediction, replay and saved-code revisit exercises | Reuse these outcomes at milestones; do not append another near-identical checklist. |
| Volley 05 and `prototype/steps/step-05.bas` | Exact edits and one contact question | The worked contact case omits the earlier input decision. **Local addition:** one input-to-outcome trace with two hints, a contrasting input, and an optional four-cell-paddle variation without an edit recipe. |
| Amiga Flock 11 and `unit-11/flock.asm` | Full source, cue constants and local sound ownership trace | Tweaking a supplied constant can avoid tracing the main loop. **Local addition:** accepted-hop and cooldown-gated traces through input, state, audio update and sprite preparation; an unfamiliar symptom and cross-game comparison. |
| C64 Starfield 17 | Real gameplay flaw, spawn/representation and lifecycle work | Solutions are mostly explained before a learner chooses evidence. Later checkpoint should hide the repair, preserve the baseline and ask for a prediction across reset, spawn and display state. |
| NES Dash 11/14 | Concrete collect/audio sites, main/NMI split and state | Supplied register edits and reward claims do not demonstrate understanding of event-to-output timing. Hardware corrections already queued are prerequisites to a synthesis companion, not material to repeat uncritically. |

Do not expand every early lesson. Prefer one milestone after a useful set of mechanisms exists, then another when the learner encounters a genuinely different responsibility or machine.

## Progression of independence

| Stage | Task and support | Observable evidence |
|---|---|---|
| Guided connection | Follow one supplied state through named boundaries; one hint identifies relevant routines and another narrows the decision. | Learner explains intermediate state and why the observed outcome follows. A correct final number alone is insufficient. |
| Prediction | Change one input/state assumption before execution; retain the same baseline. | Written/spoken prediction names both a changed result and something that should remain unchanged. |
| Explanation | Observe a surprising picture/sound and choose which state to inspect. | Distinguishes wrong rules, wrong presentation and late service; names evidence that would contradict the explanation. |
| Unfamiliar small fault | Isolated labelled variant with one meaningful fault and a reliable reproduction; repair hidden until requested. | Locates the first divergence, repairs the cause, repeats the failure and a formerly passing case. |
| Independent variation | State a goal and constraints without line-by-line edits. Supply recovery source and graduated hints, not an unexplained starter framework. | Working variation plus an explanation of affected responsibilities and meaningful boundary checks. |
| Comparison | Two valid approaches under the same intended game requirement. | Chooses using explicit trade-offs: state, memory, timing, clarity and player feedback, not “newer is better”. |
| Transfer | Apply an idea in another game/subsystem after recalling the local prerequisites. | Identifies what transfers and which representation, ownership or hardware contract must change. |

Do not withhold explanations until a timer expires or a score is reached. A prompt asks for an attempt, then separate native disclosures offer hint 1, hint 2 and reasoning. Readers choose the support they need; a parent/teacher can use the same sequence aloud or on paper. Independence grows through declining scaffolding, not through surprise prerequisites.

## Trace an actual action, not an invented universal pipeline

Use an annotated table, short diagram or recording only where it clarifies a boundary. Include the physical input assumption and where the program samples it; then follow the actual order. Some programs draw before completing another object's simulation, some return before hardware output finishes, and some have no audio at all.

**Volley 05, local trace:** at the sample point take `p=9`, ball `(x,y)=(3,8)`, velocity `(-1,+1)`, `missed=0` and `k$="z"`. The saved input survives PAUSE, paddle moves to rows 10–12, candidate becomes `(2,9)`, contact misses, and the program reaches the result without committing/drawing the rejected candidate. With empty input, the paddle stays at rows 9–11 and the ball returns. This checkpoint is silent. The table is a source-derived paper trace, not a precise end-to-end latency measurement.

**Flock 11, local trace:** assume live game, no squash delay, cooldown zero, sheep y=200, artwork index zero and held Up. `steer` samples/decodes the joystick, moves y to192, sets cooldown6, toggles artwork and requests the baa. Traffic/collision work follows; the stated safe-field case produces no replacement. The same pass's `soundtick` changes the new timer5 to4, then sprite preparation follows. Hardware audio can continue after the call returns. A separate cooldown1 case returns from `steer` without sampling movement input, yet other main-loop work proceeds. No universal “sample every control, update everything, then present” architecture is implied.

**Next C64 companion:** Starfield17 title start through `enter_game`, game-owned SID handover, sprite pointers after screen clear, enemy count and generated positions. Ask which state can still be wrong when the title looks correct. Use the lifecycle/fixed-seed fixtures already planned.

**Next NES companion:** after Dash APU/timing corrections, follow a sampled controller action to movement/collection, score and hidden-coin state, sound request and the actual main/NMI presentation boundary. Mark distinct input, simulation, PPU transfer, visible refresh and audio-generator timing; do not put every operation in NMI merely to draw a tidy diagram.

A host input event, guest read, register write and perceived result are different observations. Preserve the named representation changes (string reading to action, candidate to committed coordinate, logical position to sprite bytes, event to sound parameters). For any measured example, record configuration and evidence; a paper trace proves neither exact sound onset nor hardware accuracy.

## Concrete milestone map and prerequisites

| Milestone | Essential synthesis outcome | Optional variation/transfer; route back |
|---|---|---|
| Meet BASIC toy completion / Bright Spark 07 | Explain input, stored values, displayed result and which state resets on replay. Use existing completion/replay exercises. | Change a cue or prompt while preserving rules. Refresh routine contracts in Foundations Structure 02/03 locally as needed. |
| **Volley 05, local** | Explain why moving down changes a would-be hit into a miss, using source order. | Four-cell paddle: independently align drawing, collision and movement limits. Check both paddle ends and court limits; return to Volley04 for input/paddle work. |
| Sonar 09 / Crates07–08 | Trace input/map data into state and drawing; identify whether a symptom belongs to format, rule or presentation. | Reuse the marker revisit or converter proposal; compare representation costs. Return to the existing map loader and validation lessons. |
| Tail Chase05–06 | Compare preserved body order under shifting and circular storage; trace a wrap and growth separately. | Transfer an owned fixed pool idea to Meteor Storm only after its record layout is understood. No demand to invent memory management. |
| Meteor Storm12/20 | Explain pool refusal versus rule preservation and why a sound/picture can arrive late under load. | Reuse the profiling fixture and preserve event/input order. Return to Meet Assembly08 debugger and timing lessons. |
| Starfield17 | Identify entry-owned state, ninth position bit and sound ownership from one observed outcome. | Diagnose one isolated reset or high-bit fault, then compare two sound handover policies. Return to the relevant routine/representation explanation before the challenge. |
| Dash14/17, proposed | Identify which context owns input/state/output and where a transition or late cue goes wrong. | Extend one lifecycle or layout case after corrected hardware prerequisites. No need to compose music or write a generic queue. |
| **Flock11, local** →15/17 | Trace accepted hop versus cooldown gate, separate movement/artwork/sound state, explain what a return does not complete. | Compare Touchdown's accepted-burn flag; later change a cue/seed policy with explicit cost and ownership. Sound design is optional; speech, a table or muted visual evidence can establish the essential reasoning. |

## Evidence and fairness of the exercise

A learner can demonstrate understanding by explaining, tracing, editing, comparing or diagnosing. Do not require artistic polish, musical composition or untaught probability/algebra when the outcome concerns state or timing. Supply numerical constants and a small starting state. Avoid scoring subjective sound preferences as correct/incorrect; ask what information the cue communicates and what evidence supports that judgement.

For a variation, publish acceptance criteria rather than one mandatory implementation. Volley's longer paddle must agree across drawing/contact/limits, but a learner may choose different readable organisation. Compare two plausible approaches after a first attempt; both can satisfy the game while trading code size or explanatory simplicity.

Use a baseline and a recovery route. Label faulty copies, prepared states and illustrative diagrams. Keep original working samples intact. If a learner needs the explanation, ask them to apply it to one slightly changed case afterwards, not recite the revealed answer. That gives observable transfer without an extra assessment system.

## Wider implementation order

1. **Local now:** two high-value milestones, Volley05 and Flock11, with source-checked traces, separate hints/explanations and optional extension/transfer. No runtime modifications or fresh native execution claimed.
2. Add one C64 Starfield milestone using the already planned lifecycle/randomness fault companion. Avoid combining multiple faults in the first unfamiliar case.
3. Add NES Dash's event trace only after its queued audio/timing corrections. Verify the actual checkpoint order and permitted hardware operations before authoring the diagram.
4. Review the next completed module against this method when it is edited. Reuse existing Bright Spark, Sonar, Tail Chase and Meteor Storm exercises; do not retrofit a quiz into every page or duplicate the native work queue.

Completion of a synthesis exercise means we can see a learner connect the relevant ideas and support an explanation or change with evidence. A copied build, finished screenshot or terminology answer alone does not establish that outcome. This is teaching design, not a claim that learner trials have already validated the new exercises.


## Whole-action review: Volley, Touchdown and Flock

R3 reviews the authored whole-action examples in Volley05, Touchdown05 and Flock11. All changes are lesson edits; the maintained game sources and companion recordings are unchanged.

- **Volley:** the prepared `z` versus empty-reading trace matches the candidate/contact rules. The table now states the exact order in line 126: erase the old top cell, update `p`, then call the paddle drawing routine at 130. Hints precede the explanation; the four-cell paddle remains an optional variation with acceptance criteria.
- **Touchdown:** a prepared two-update trace supplies `y=1000`, `v=10`, `fuel=1`, `r=10` and Space. The last burn yields `burn=1`, fuel 0, velocity 6 and position 1006; the following unavailable burn gives velocity 8 and position 1014. Both map to row 10 while the character changes from `*` to `A`. The explanation follows sampling, accepted action, limits, printing and state commit. A folded hint precedes the comparison; the three-column table keeps both updates visible on a narrow screen. This is source arithmetic, not measured flight evidence.
- **Flock:** the essential hop/cooldown trace now precedes the longer optional ownership experiment. Its six routine calls match `mainloop`; the accepted hop gives Y=192, frame=1, cooldown=6 and timer=4 after the same pass's `soundtick`. The cooldown variant clarifies that no new baa is requested while existing sound work continues. No musical composition or listening judgement is needed to complete the core trace.

Source identities match retained verification baselines: Volley `prototype/steps/step-05.bas`, SHA-256 `d32f75d39d2958546dcef7f0cb7f7cbc4bdc624b269b402e7f174eafce524a19`; Touchdown `teaching/unit-05/steps/step-01.bas`, `70463e96ad3c3fd02be7341d450507f52ec7956cc6e2265c7f5948537698b1eb`; Flock `unit-11/flock.asm`, `71361e15c6cf329ec274dc2959caa76d9dcd8a9c9236625253eec0fbea173cdb`. The two BASIC hashes match their checkpoint records; the Amiga hash matches the ownership companion's pinned baseline.

The review does not claim a new native run of these prepared states, measured physical response, a listening review, original-hardware verification or learner trial. Earlier companion execution evidence keeps its original scope. Local rendering checks and publication approval are separate from those evidence levels.

Local validation passes: 2,468-page Astro build, curriculum routes, template whitespace, lesson links/anchors and source includes. All three pages pass keyboard-operated explanations and page-overflow checks at 390/1280px in light/dark themes (12 combinations). Desktop/mobile captures were inspected; the Touchdown table was narrowed and checked again. These checks are not a complete accessibility audit or publication.
