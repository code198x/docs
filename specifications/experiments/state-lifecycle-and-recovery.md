# Game state, lifecycle and recovery

**Status:** Source-audited progression with one local lesson addition: Bright Spark unit 07's state-ownership and repeated-replay exercise. No game code, pause system, loader or operating-environment restoration has been implemented in this pass. Later fault fixtures and transitions below are proposals. Scope: Spectrum, C64, NES and Amiga; no new standalone module.

Build on [abstraction contracts](abstraction-and-portability.md), [scheduling and ownership](scheduling-ownership-headroom.md), [testing and diagnosis](testing-and-diagnosis.md), [feedback](timing-and-player-feedback.md) and [data validation](data-memory-tools.md). The [timing plan](timing-and-interrupts.md) owns hardware interrupt contracts. This plan owns the teaching order for state lifetime, transitions and recovery, rather than a new state-machine framework.

## Existing evidence and gaps

Paths refer to website `src/content/curriculum/` and matching code-samples projects.

| Inspected location | Existing implementation/teaching | Gap or action |
|---|---|---|
| Spectrum BASIC Bright Spark 07, `opening/unit-07/steps/step-02.bas` | Title, success/failure, release-filtered replay, explicit empty order/count reset and saved-game reload | Local ownership table and three successive replay paths added. This strengthens an existing working route; it does not introduce replay. |
| Spectrum BASIC Touchdown 04 | Title/flight/result, common attempt setup, release before/after choices, quit to BASIC; repeated GO SUB calls are completed before retry | Reuse its transition trace. Later pause work must distinguish stopping movement from stopping every relevant countdown. Fuel appears in unit 05, not this checkpoint. |
| Spectrum BASIC Crates 08; Meteor Storm 12 | Invalid maps stop before play; full pool is detected and spawn refused | Existing validation/refusal is not automatic recovery. Distinguish correction/reload from a safe but gameplay-changing fallback. |
| C64 Starfield 17 `steps/step-04.asm` | `enter_title`/`enter_game`, title music/laser handover; game entry restores sprite pointers after screen clearing, enemy count, score, lives, wave and timers | Excellent coordinated-entry example. Later isolate one missing reset or sound handover and inspect the second game. A timed UI lock is not necessarily a fresh-press rule. |
| NES Dash 14 `dash.asm` | `game_over`/`game_over_drawn`; main waits on NMI flag then skips gameplay when game over; NMI still handles display work | Do not call this a complete title/restart/pause implementation. Develop a small replay entry only after the timing and handoff corrections; separate main state from ongoing handler work. |
| Amiga Flock 11 `flock.asm` | Main advances input, traffic, collision, sound and sprites; mouse button branches to `.halt`, a loop | A halted CPU game loop is not an OS return or proof that DMA sound stopped. Later lifecycle work needs explicit sound/DMA ownership and the intended launch environment. |
| Shared state-machine pattern | Local C03c correction: one transition per update, death-before-pause priority, entry/exit and pause policy, held-input trace | Logic-model checks pass; machine implementation and learner trial remain separate. See the verification section below. |

The main gaps are explanations and controlled exercises around existing state. Interacting state machines and transactional loading/recovery are later topics where a real game earns them, not requirements for the first BASIC program.

## Staged progression

| Stage and placement | Prerequisites / smallest useful solution | Learner outcome |
|---|---|---|
| 1. Explicit initialisation: early Meet BASIC → Bright Spark | Variables and instruction order. Identify each value read before play and the assignment that establishes it. | Explain why a fresh run can work while replay fails; do not rely on leftover RAM or an emulator's reset values. |
| 2. Named phases: Bright Spark 07, Touchdown 04; Starfield title/play/result | Branches, calls and input reads. Draw the existing control-flow phases before adding a state byte or dispatch table. | Trace allowed title → play → result → replay/quit paths and ignored inputs; distinguish restarting the game from resetting the machine. |
| 3. Entry/exit work: Starfield 17; Bright Spark replay | Routine contracts and side effects. One named entry routine coordinates the actual required assignments, graphics and sound handover. | Predict second-entry state; trace why clearing a screen before restoring sprite pointers matters in the inspected C64 source. |
| 4. Pause/restart/level changes: later Dash, Flock and actual wave/room changes | Known update responsibilities, clocks and input edge/release rules. Add one transition with a written policy for each subsystem. | Show that paused simulation stays frozen, resume does not replay a held pause request, and a new level preserves only intended session state. |
| 5. Interacting state: later Starfield waves/enemy behaviour, Dash protection/animation, Flock cue player | Understand each small state machine separately. Keep application phase, object behaviour and sound playback distinct; specify which updates/events are permitted together. | Explain why a playing enemy cannot move during application pause, while a permitted menu cue may finish. Use an explicit transition priority, not a product of every possible state combination. |
| 6. Failed operations: Crates validation, Meteor pool; later authored-data loading | Valid/invalid input, owned storage and a reliable failure report. Report failure before exposing partial state; choose a specific retry, cancellation or refusal path. | Distinguish recoverable external failure from an internal invariant violation. Demonstrate that retry does not duplicate resources or preserve half-loaded data. |
| 7. Repeated transition stress: all four at their appropriate checkpoints | Reproduction and state inspection. Retain a short expected-state table and run unusual legal sequences several times. | Demonstrate first start, repeated restart and failure/retry outcomes; justify invalid transitions being ignored or diagnosed. |

Simple branches and routines are enough initially. Separate entry from per-update work because the jobs differ, not because a framework demands callbacks. A transition touching several systems can remain a short explicit routine whose order we can trace.

## Which lifetime owns this state?

| Lifetime | Example / owner | Reset or preservation question |
|---|---|---|
| Object | Enemy position, active flag, animation phase, local cooldown | Reset on spawn/reuse; remove from active work before reusing its slot. Does an old cooldown survive accidentally? |
| Level/wave | Room grid, remaining targets, wave spawn schedule | Initialise when that level begins; decide what a retry reconstructs. Starfield's wave progression is different from a whole new game. |
| Play session | Lives, score, current level, Bright Spark order/count | Reset for a new game; preserve only deliberately across levels. Do not erase score just because the scene changes. |
| Application | Chosen options, loaded shared assets, title state; future session-best score if implemented | Preserve across new games only where a feature requires it; release resources on a genuine application exit. These examples are not claims that every game has settings or a high score. |
| Presentation/service state | Active cue, DMA reader, pending display request, held-input history | Name its owner and lifetime explicitly. It may outlive a simulation object unless the transition cancels or completes it. |

For Bright Spark the configured cap is assigned again on each replay; it is not a saved preference system. Scope is a design meaning, not necessarily a language variable scope. A single global BASIC variable can represent one attempt's state if every entry resets it correctly.

## Transition contracts and controlled failures

For each new transition record: current state, event/condition, destination, entry/exit work, preserved state and rejected/conflicting requests. Check entry once, not once per display refresh. Define a winner when two requests occur in one update—for example, accepted death must not be overwritten by a subsequent pause test. Decide when the new state becomes visible to interrupt handlers using the existing handoff plan.

| Exercise / actual home | Isolated provocation and prediction | Repair and regression evidence |
|---|---|---|
| **Local: Bright Spark 07** | Temporarily use the existing cap=2 test; fail/replay, win/replay, fail/hold-r/release/replay. Predict order length, count and panel state before each entry. | One item, zero completed rounds, resting board, release gate respected. Restore cap=16 and matching instructions. Same random first item is allowed. Source unchanged; native execution of this new exercise is not claimed. |
| Touchdown 04 → 05 | In a labelled copy, bypass attempt setup on retry; predict the inherited position/velocity. Separately hold start/retry keys. | Restore entry path; repeat safe and hard landing paths, then fuel reset once fuel exists. Check call/return balance and clean release before BASIC exit. |
| Starfield 17 | Omit only `enemy_count` reset in a controlled checkpoint after reaching a later wave; separately omit title/laser handover. | Inspect count=3, lives=3, score=0, wave=1 and inactive bullet at new game entry. Sound state must match its new owner. Do not reset away a symptom elsewhere in the loop. |
| Starfield title/result or later Dash retry | Hold the transition button across screens; contrast a dwell timer with a release/new-press requirement. | Explain the intended acceptance rule. Test fast taps, held input and repeated release/press without silently changing the game's current policy. |
| Later Dash pause; Flock traffic/sound | Freeze main movement but deliberately leave one gameplay countdown or handler-owned simulation update advancing. Compare state before/after pause. | Gate the correct update responsibilities. Choose independently whether music finishes, pauses or stops; verify resume preserves positions, timers and event counts without a catch-up burst. |
| Crates 08 → validated converter | Reject malformed room data; repeat with corrected input. Later loader fixture fails after one partial allocation/read. | Never publish a partial room as playable. Release only resources actually acquired, retain a valid previous state where designed, and report why loading failed. |
| Meteor Storm 12 | Force pool exhaustion using the existing bounded fault; request repeated starts after restoring capacity. | Bounds remain safe, required hazard policy is explicit, old active slots/events do not leak into a new run. Refusal alone is not equivalent gameplay. |
| Later Flock/Onslaught application exit | A separate environment-specific fixture leaves a sound or display reader active at exit. | Verify ownership completion before releasing memory and restore the named environment. Do not run an unbounded dangling-DMA fault in the normal game. |

Test unusual **legal** paths (pause/resume/restart, lose/retry/win/retry, load failure/cancel/retry). For an illegal request such as restart during a protected load commit, state whether it is deferred, rejected or a development error. Repeating entry should either be explicitly safe or guarded; do not assume all initialisation routines are idempotent.

## Pause and recovery are policies

A pause table should name simulation, object timers, animation, input, UI, music, effects and display servicing. “Freeze gameplay; keep resume input and required display service alive” can be sensible; stopping interrupts globally is not a pause design. Record elapsed-time handling so resume does not automatically simulate the pause or replay every skipped sound. Display work that continues must not mutate authoritative gameplay by accident.

A development assertion says an internal promise was broken. In a controlled build it can record the state and stop at a safe diagnostic point. Runtime recovery handles an expected failure such as malformed external data, an unavailable optional channel or a failed read. It reports a reason and leaves a defined state. Silently clamping a corrupt index or repeatedly restarting to hide a fault is neither diagnosis nor honest recovery.

For later loading: keep the old valid state while preparing the replacement where memory permits; validate and publish once complete. If both cannot coexist, use an explicit loading/error screen and an understood retry path. Track which allocations/resources succeeded and undo only those, in a safe dependency order. Recovery may mean asking for corrected data or returning to a menu; it need not invent a playable fallback. No dynamic loader is claimed in an embedded-data game.

## Hardware restoration and operating environments

Returning to a title is not returning to an operating environment. Verify the exact launch/exit contract before teaching a cleanup recipe:

- **Spectrum BASIC:** Bright Spark ends with STOP; Touchdown waits for Q release before its final stop. These are source-observed paths, not restoration of arbitrary machine-code takeover state. A later assembly-to-BASIC return must preserve the actual caller/stack, interrupt and ROM assumptions and be tested through that launch route.
- **C64:** Starfield's `enter_title`/`enter_game` restore game-owned display/SID state, not the entire KERNAL environment. A future SYS return requires an audit of memory mapping, stack, vectors, enabled interrupt sources and display/audio ownership against the actual startup and ROM contract. Do not label a title transition an OS cleanup.
- **NES:** Dash is a cartridge program. A new game is an application transition, not return to a desktop. Keep NMI/PPU and audio contracts valid across transitions; resetting game variables does not automatically clear pending transfer or sound state. The timing plan owns permitted PPU windows.
- **Amiga:** inspected Flock 11 branches forever at `.halt`; it does not restore Workbench. Separate boot/takeover and Exec-hosted designs. The latter must honour library/resource ownership and release only after hardware readers no longer use the storage. Restoring a saved view or freeing a Copper list is not safely interchangeable in order.

Verification sources: the actual samples named above; Commodore, *Amiga ROM Kernel Manual*, volume 1 (1985), Graphics Primitives pp. 2-30–2-32, demonstrates restoring the prior view/closing the library and explicitly warns against freeing a Copper list still in use; *Amiga Hardware Reference Manual*, second edition, DMA and interrupt-control chapters describe the readers that outlive ordinary CPU work. Existing timing-plan Zilog/MOS/Commodore and public NES references remain authoritative for target-specific interrupt/display contracts. These checks establish constraints, not a tested universal cleanup sequence. Each later return-to-environment fixture needs configuration-specific execution evidence.

## Next work and completion

1. **Authored locally:** Bright Spark 07 ownership/repeated-replay exercise, with a recoverable temporary cap and expected observations. No new checkpoint or native run claimed.
2. **Next lifecycle companion:** a Starfield 17 state-entry table plus one missing-enemy-count-reset fixture, after the already queued Bright Spark native work. Compare entry state at the first and third game; test title/laser handover separately rather than combining faults.
3. The shared state-machine pattern now has a checked illustrative transition model (C03c, below). Apply it to the later checked-game companion without claiming the model itself implements that game’s hardware handover.
4. Dash replay/pause follows its timing corrections; Flock lifecycle/cleanup requires a named launch environment. Loader rollback follows an actual loader requirement. These remain future work, not implementations implied by this plan.

Completion means the learner can identify ownership/lifetime, predict a transition's preserved/reset state, reproduce a lifecycle fault, repair its cause and repeat the transition without leaking state or resources. A fresh first start alone is insufficient evidence.


## Shared state pattern correction

C03c is authored locally, ready for review in
`website/src/content/patterns/cross-platform/framework/state-machine.mdx`.
It preserves direct, machine-specific implementation and uses a small sequential
model rather than adding a common engine. The incomplete jump-table excerpts are
replaced by guidance on dispatch, valid indices and call/return contracts; choosing
a table remains a later measured implementation decision.

The explicit policy completes one gameplay update before considering pause;
death wins if both conditions occur. A new state's handler runs next update.
Title → Playing initialises a session, while Paused → Playing preserves it.
Entry/exit owns audio requests and screen preparation; actual hardware scheduling
and shared-state publication are delegated to the target implementation.

Author checks on 22 September 2026 used a Python translation of the decision
rules, not an assembled game. All 32 combinations of four states and three
Boolean conditions (Fire edge, Pause edge, dead) matched the transition table.
Invalid state 99 was rejected. Repeated Game Over updates produced only one
result-cue request, on entry, after simultaneous death and Pause.

The published eight-update trace was executed with Fire bit 0 and Pause bit 1,
normalised held samples `[1, 1, 0, 1, 2, 2, 0, 2]`, seeded previous input zero,
starting in Game Over. Edges use `held & ~previous`. State results:

`Title, Title, Title, Playing, Paused, Paused, Paused, Playing`.

The diagnostic session began at score 7, timer 12, enemy position 40. New-game
entry set score 0, timer 12 and enemy position 40 exactly once at update 4.
Each Playing update decremented the timer and advanced the enemy once: update 5
left timer 11 and position 41; updates 6–8 preserved both. Resume did not run the
fresh-session initialiser or simulate the paused interval.

These checks establish the illustrative logic and stated entry responsibilities,
not physical input timing, working sound pause/resume, interrupt atomicity or
four-system execution. The learner is asked to predict the conflicting requests
before opening the explanation. A separate learner trial is pending. The Starfield restart companion below implements one bounded follow-up; other
Dash/Flock lifecycle exercises above remain proposed work.

## Starfield restart investigation: C07a

Authored in `commodore-64/assembly/starfield/unit-17.mdx`, with samples in
`code-samples/commodore-64/assembly/starfield/unit-17/restart/`. It uses the
step-04 source, leaving the ordinary game untouched. Learners predict first,
second and third entry state, reproduce one omitted `sta enemy_count`, follow
its lifetime with graduated hints, and restore the store before spawning.

The fixture explicitly sets the first count to three once, invokes real
`enter_title`/`enter_game` routines, and calls `advance_wave` five times between
entries. Non-zero score, one life, an active bullet and seven kills are declared
guest setup writes. This makes the first faulty entry appear correct without
claiming a cold machine supplies that value. Entry records cover count, both
score bytes, lives, wave, kills, speed, bullet-active and sprite-enable bits.

Native PAL verification on 22 September 2026 gives baseline/repair 3,3,3 and
fault 3,6,6, while the other eight bytes reset as expected. All three displayed
counts are also checked; repaired and baseline PRGs match byte for byte. Exact
source/program/emulator hashes and reproduction instructions live beside the
fixture. The 2,468-page website build passes. This is a controlled routine test,
not joystick playthroughs, audio handover, random-sequence validation or original
hardware evidence. C07b/C07c remain separate randomness tasks.
