# Interpreter traces: what we counted

From Source to Silicon unit 2's original accumulator and selected trace are
correct. This slice adds a changed-start prediction, an explanation of what the
trace can establish, and local recall of assignment, loop bounds and output.
[Website #760](https://github.com/code198x/website/issues/760) tracks this bounded
understanding gap and the unmeasured claim about unnoticed interpreter cost.

Six finite host traces and **eight fresh ROM BASIC runs** pass. The original
1000 result and table remain intact. [Independent tasks](LEARNER-TASKS.md) and
[assessor notes](ASSESSOR.md) prepare a learner trial. No learner is available:
effectiveness, retention and unaided transfer remain unknown. #114/#115/#124 stay
open.

## Scope and sources

The [plan](../../plans/2026-10-16-interpreter-trace-pilot.md) bounds this work.
Approved website #759 and docs #87 merged first. Their resulting baselines are
`0814f1e482ebdaa0aeae8dc6799e2d5f2aeca3b0` and
`f18a83c39183481cb5abdbefe79b4708f5c0f911`.
[Identities](identities.json) retain sources, specifications, prior evidence,
installed packages, UI pin and tool hashes. No dependency was added or installed.

[Curriculum design](../../specifications/curriculum.md),
[unit guidance](../../specifications/unit.md) and
[pseudocode](../../specifications/pseudocode.md) require enough local explanation
to enter independently and distinguish paper reasoning from target execution.
The current loop uses an inclusive fixed range and updates a named value. Its
selected table omits loop-control work and already says it is not a processor
instruction count. We add an independent opportunity to apply that distinction.
The statement that this cost usually goes unnoticed had no named workload or
measurement; the opening now introduces the paper trace directly.

The earlier [source/translation pilot](../2026-10-source-silicon-pilot/REPORT.md)
read all five units, ran two short BASIC programs and retained stored token
records. Its learner tasks already ask about interpreter/token roles. This
follow-up adds changed-start/bound/increment tracing and an independent check of
which quantities the trace supplies. Earlier results remain earlier evidence;
the [full per-unit map](../2026-10-foundations-objectives/MAP.md) keeps its immutable
baseline. Open/closed interpreter and trace searches found related completed
work, but no matching unit-2 changed-bound prediction finding.

Sinclair Research's *ZX Spectrum BASIC Programming* (1982),
[chapter 14](https://worldofspectrum.org/ZXBasicManual/zxmanchap14.html), explains
keyword tokens. [Chapter 24](https://worldofspectrum.org/ZXBasicManual/zxmanchap24.html)
explains ROM/RAM and the stored BASIC line records.
[Appendix A](https://worldofspectrum.org/ZXBasicManual/zxmanappa.html) gives the
codes used in the checks: LET 241, FOR 235, NEXT 243 and PRINT 245. The same byte
can have a different role when used as a Z80 opcode; a token in a BASIC record
is not thereby a processor instruction to perform that BASIC operation.

## Finite model and native observations

[verify-trace.py](verify-trace.py) checks six [finite models](model-trace.json):
1000 and three visits from zero, three visits from ten, no visits, one visit and
three additions of two. Each enumerated trace must agree with an independent
count and the formula `initial + visits * increment`, including every partial
sum. The changed-start case reaches 11, 12, 13. The wrong reset policy reaches
11 instead of 13. These are selected whole-number paper models, not a new
pseudocode runtime or proof over arbitrary loops.

The [native record](native-trace.json) retains all 24 screen rows, numbered source
fixtures and parsed stored program bytes before and after each RUN. Programs are
entered through the actual ROM keyboard editor using the maintained transport.
NEW must return to its positive ready state before installing the next program.
No source/result memory injection or ROM patch is used. Length-checked reads
preserve complete line records and ROM identity. Normal completion, exact full
output and unchanged program records are required. The emulator closes and its
exit is checked on success and failure.

Six programs display the model's final results: 1000, 3, 13, 10, 16 and 11.
A seventh run repeats the unchanged three-visit program without NEW or re-entry;
it again displays 13 because its initial assignment runs again. The eighth adds
PRINT inside the short loop and displays 11, 12, 13, then FINAL 13. The
[short-result capture](question.png) and [instrumented capture](instrumented.png)
were visually inspected. Adding output changes the program; that instrumented
run supplies selected state observations, not the original program's timing.

The [wrong-reset fixture](known-red/wrong-reset.bas) deliberately resets inside
the body. Its actual 11 is retained in the
[failed transcript](known-red/native-trace.json); the
[rejection](known-red/rejection.json) has a nonzero exit against the intended 13.
The control changes an actual program rather than only changing an expected value.

Stored-byte equality observes the selected program area. It does not trace the
processor's instruction fetches, prove every internal interpreter step or
establish the cost attributable to interpretation. We make no speed comparison,
CPU instruction count, physical timing or original-hardware claim.

## Narrow trace repair

[Website #761](https://github.com/code198x/website/issues/761) records a reproduced
rendering defect found during this slice. At 390px, inherited arbitrary word
breaking splits the 1000 visit/result into separate 10/00 lines and breaks the
headings mid-word. The [layout capture](trace-layout-observation.png) and
[geometry](trace-layout-observation.json) show that state. The existing wrapper and global block-style table both shrink to
about 358px, leaving no horizontal overflow to scroll.

The [failed narrow check](browser-narrow-trace-failure.json) rejects that state.
We restore natural table display and normal word wrapping inside TraceTable,
keeping any needed overflow in its existing wrapper. A labelled, focusable region gives
keyboard access to that scroll area, following the existing accessible-table
convention. General tables and page layouts are unchanged.

[Before](tables-before.json) and [after](tables-after.json) records cover all
seven authored consumers at 1440px and 390px: fourteen table/viewport cases.
Their cell contents agree. All fourteen authored cases now fit at their tested
widths without splitting numbers. A labelled temporary 80-digit cell supplies a
positive overflow control: the same region scrolls by keyboard to the final
column. That synthetic content is restored before the authored capture. After checks require normal table sizing and
word wrapping, no document overflow, keyboard access to the final column where
scrolling is needed, and scoped trace accessibility scans. This is a component
repair with checks across its actual consumers, not a new teaching architecture.

## Final results

The final production build and all **237 tests in 32 files** pass. Chrome
155.0.8059.80 passes the two interpreter viewports, four keyboard answer
reveals and two support-link/Back journeys. All fourteen table/viewport cases
preserve their cells, expose visible focus, and pass scoped trace axe scans.
Neither the interpreter's closed/revealed main-content scans nor the trace scans
report a violation or incomplete result. No document overflow or page errors
were observed. All fourteen final table captures, four answer captures and the
two native captures were visually inspected. The detector reports no findings.

Every authored trace fits at the tested widths after normal word wrapping;
numeric cells no longer split across lines. The explicitly synthetic overflow
control confirms actual keyboard scrolling to the last column when needed.
The build retains an existing Pagefind Classic UI notice; sandbox-denied mise
tracking links do not prevent the checks from completing.

## Website checks and limits

The proposed unit uses two existing Question disclosures. One predicts the
changed-start case; the other separates source updates, machine instructions and
measured time. The optional link goes to “Doing It Again”, which explains its
own loop rule. No earlier attendance, target setup, new component or page layout is
required. Independent prompts use fresh values rather than the revealed answer.

[Website results](website-results.json) retain the final production/repository
check outcomes. [Browser results](browser.json) retain wide/narrow exact output
and selected table cells, single-line numeric cells, keyboard answer reveals,
the optional support link and Back. Readable answer and trace captures were
inspected. Scoped axe results, incomplete records and any qualifications belong
to those declared pages and states, not a whole-site accessibility claim.

The initial browser attempts remain labelled separately. The
[first assertion](browser-closed-answer-failure.json) looked for “initialise” in
visible text while that explanation was correctly closed. It now checks the
visible local recall. The [second assertion](browser-support-title-failure.json)
assumed the support lesson's title and wording. Source review established
“Doing It Again” and “whole numbers”; the link label and check now use those.
Those two failed harness assertions are not passing observations or target failures.
The first table-level repair still encountered the
[stronger cell rule](browser-table-rule-failure.json); we then traced
`design-rollout.css` applying arbitrary wrapping directly to cells. The final
component override applies to the cells as well as natural table display.
The [initial comparison](tables-before-incomplete.json) included a closed trace
inside Basics unit 4's answer and therefore supplied no visible baseline for
that table. Its [focus failure](tables-hidden-trace-failure.json) exposed this
harness gap. We now open ancestor disclosures and require positive dimensions
before checking a table. We rebuilt the original component and repeated the
complete before comparison; the incomplete initial captures remain labelled
`initial-` and are not accepted visual evidence. A subsequent
[scroll expectation](browser-scroll-expectation-failure.json) still required
horizontal movement even though the repaired interpreter table fits. The final
check requires every numeric cell to occupy one line and tests overflow only
when it exists; the separate synthetic control positively exercises scrolling.

[Evidence validation](validation.json) checks baseline/proposed identities,
model formulas, complete native records, fixture hashes, repeat-run equality,
browser checks and local links. Wrong source hashes and missing screen rows
must fail. Run [verify-evidence.py](verify-evidence.py) with
`--website PATH_TO_WEBSITE_REPO`. The [design detector](design-detector.json) supplies a final mechanical check
of the changed UI. The [manifest](SHA256SUMS) retains all evidence
hashes. Green evidence checks do not substitute for a learner trial.

Physical touch, screen readers, other BASIC dialects, arbitrary bounds or counter
mutation, instruction counts and performance remain untested. Existing packages
and generated build assets were reused in isolated checkouts; unrelated work was
preserved.

## Next bounded work

Observe the prepared learner tasks when a learner is available. Meanwhile return
to the per-unit evidence map and choose the next objective with an observable
reasoning gap. Reuse accepted technical evidence where it answers the same
question; another passing run alone does not deepen understanding. Keep the
published first-session pack small and available to parents and teachers.
