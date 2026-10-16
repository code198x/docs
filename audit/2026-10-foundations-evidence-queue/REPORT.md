# Foundations: the next reasoning task

The four units flagged by the earlier source inventory now have explicit
Question prompts. The next useful slice connects retained fractional state with
repeated updates and whole-pixel drawing, rather than adding more disclosures
to meet a count. [Website #763](https://github.com/code198x/website/issues/763)
records that bounded follow-up. This docs change prepares its paper trial; the
public lesson is not changed in this slice.

Approved website #762 and docs #88 were merged first. Current source identities
are website `d0de348ba750cac17bfd7757a217e5b37eb28042` and docs baseline
`04f4fd048893b130b886d17ed339fa41c4475b6a`. [Identities](identities.json) retain
current guidance, relevant prior reports/tasks, frozen-map and verifier hashes.
The [plan](../../plans/2026-10-16-foundations-evidence-queue.md) bounds this work.

## What the reconciliation establishes

The [immutable objective map](../2026-10-foundations-objectives/MAP.md) and its
[source record](../2026-10-foundations-objectives/units.json) remain unchanged.
They retain the full-body review at `2b9905262dcb7261314b6ef6490db7b8a5c803ed`.
The new [inventory delta](inventory.json) compares exact paths and source hashes
at the current revision: **39 units and ten overviews**, with no added or missing
source files. Four units and one overview differ from that earlier baseline.

| Earlier gap or change | Accepted follow-up | Current source observation |
| --- | --- | --- |
| Basics 3: quoted output and joining | [Output pilot](../2026-10-output-joining/REPORT.md), website #759/docs #87 | Two independent prediction/repair prompts and target-separator distinction |
| Decisions 4: compound questions | [Condition pilot](../2026-10-compound-conditions/REPORT.md), website #755/docs #85 | Numeric interval and grouping prompts with qualified input domain |
| Repeating 1: counted-loop boundaries | [Counted-loop pilot](../2026-10-counted-loops/REPORT.md), website #757/docs #86 | Inclusive/empty-range and body-placement predictions |
| From Source to Silicon 2: interpreter trace | [Interpreter pilot](../2026-10-interpreter-trace/REPORT.md), website #762/docs #88 | Changed-state prediction and source/instruction/time distinction |
| Working the Bits overview summary | [Inventory finding](../2026-10-foundations-objectives/REPORT.md), website #753/docs #84 | Summary wording reflects the qualified representation contract |

All 39 current unit files contain explicit Question/disclosure markers, compared
with 35 at the frozen baseline. That is a discoverability observation, not a
question quota, a quality score or evidence of independent understanding. Ordinary
prose can also pose a question. The delta is not a new full-body review of every
unchanged lesson, a rerun of prior experiments or a claim about live publication.

## Choosing useful work

We read the current bodies of Structure 4, Counting in Twos 3 and Working the
Bits 5, then compared their existing report and learner-task scopes. Their
current source hashes appear in the delta. [Curriculum design](../../specifications/curriculum.md),
[unit guidance](../../specifications/unit.md) and
[notation](../../specifications/pseudocode.md) govern the task. The existing
[synthesis guidance](../../specifications/experiments/synthesis-and-transfer.md)
prefers occasional meaningful connections over another exercise on every page;
its current game milestones are not claimed as Foundations implementations.

| Candidate | What already exists | Disposition |
| --- | --- | --- |
| Diagnose a wrong accumulated total | Structure 4 contrasts intended/broken arithmetic; [Structure task 5](../2026-10-structure-pilot/LEARNER-TASKS.md) already asks for repair and empty/one/several-item checks | Reuse. Another total-replacement task would duplicate accepted work; no new issue. |
| Extend high/low bytes into memory ordering | Counting in Twos 3 combines bytes and explicitly leaves physical order to each machine; [numbers tasks](../2026-10-numbers-pilot/LEARNER-TASKS.md) already separate value, signedness and address range | Defer. A target-owned byte-order experiment belongs with a concrete machine task, not an inferred defect in the shared unit. |
| Keep a fixed-point fraction across updates while drawing whole pixels | Bits 5 correctly separates decoding and extraction; [fractions tasks 3–5/8–9](../2026-10-fractions-pilot/LEARNER-TASKS.md) already cover one move, scale, rounding, diagnosis and representation design | Select. A multi-update contrast adds observable state retention: one correct first drawing can hide the fault, while a later drawing distinguishes it. |

Open/closed fixed-point and fractional-state searches found the completed #708
and #709 corrections, but no matching repeated-update task. Those corrections
remain accepted; we do not describe the current fixed-point example as broken.
#763 names the next optional lesson experiment without creating a new module,
scoring gate, runtime, dependency or prerequisite course.

## Prepared trial and finite checks

The [learner sheet](LEARNER-TASKS.md) recalls scale, storage, drawing, assignment
and the four loop visits locally. It asks for stored/full/drawn positions, an
isolated fault, a repair and a quarter-step variation. Hints and
[assessor reasoning](ASSESSOR.md) remain separate. This is prepared material for
review and an eventual trial, not observed learning or a published exercise.

At scale 256, the half-step run keeps stored positions 128, 256, 384 and 512.
Their full values are 0.5, 1, 1.5 and 2; the drawings are **0, 1, 1, 2**.
The deliberate fault writes the whole drawing coordinate back at scale 256,
losing the fraction. It draws **0, 0, 0, 0**. Both first drawings look right, but
retained state differs after update 1 and visible output differs at update 2.

[verify.py](verify.py) checks six [finite traces](models.json): half, quarter,
one-and-a-half, zero updates, stationary fractional state and the last fitting
stored sum. Enumerated integer updates must agree with independently computed
exact-rational positions and their floors. Three out-of-range updates are
positively rejected, including a second update after a last-fitting first one.
The model rejects those cases rather than choosing a wrap or saturation rule.
These finite observations do not prove every possible width, scale or operation.

The actual wrong-retention model is run in `--wrong-only` mode and must exit
nonzero. [Its trace](known-red/wrong-trace.json) and
[rejection](known-red/rejection.json) retain the lost later move. No target
execution, display, motion smoothness or speed measurement is claimed. The
fractions pilot's ROM/Z80 observations remain earlier, configuration-specific
evidence; repeating them would not answer this new state-retention question.

## Verification and remaining limits

[Retained-evidence checks](validation.json) verify current/frozen source hashes,
exact source sets, model formulas, prompts' numeric expectations and local links.
Missing inventory rows, changed source hashes and discarded fractional state
must be rejected. Run [verify-evidence.py](verify-evidence.py) with
`--website PATH_TO_WEBSITE_REPO`; [SHA256SUMS](SHA256SUMS) records the retained
file identities. Ruff, Vale and whitespace checks apply to this docs/model change.
No website build, browser run or new native execution is needed or claimed here.

All actual learner outcomes remain unknown. A parent or teacher can use the
prepared sheet on paper, recording predictions and help before explanations.
The existing [first-session pack](https://code198x.com/try/) remains the small
public invitation. No new personal details, learner score or supposed success
rate is added. #114/#115/#124 stay open.

Next, review the prepared task and implement #763 as one optional experiment in
Working the Bits unit 5, with a hint, explanation and focused wide/narrow checks.
Reuse the accepted representation evidence. A new target-specific claim would
need its own execution evidence; a new learner claim needs an actual trial.
