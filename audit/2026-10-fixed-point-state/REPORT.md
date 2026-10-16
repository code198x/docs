# Fixed-point state between drawings

Working the Bits unit 5 now offers one optional paper experiment that connects
retained fractional state with repeated updates and whole-pixel drawing.
[Website #763](https://github.com/code198x/website/issues/763) tracks the addition.
The original decoding and addition examples remain correct and unchanged.

Approved docs #89 merged first at
`a8ab271187c09001624a470a1eb4dc45b106300d`; website baseline is
`d0de348ba750cac17bfd7757a217e5b37eb28042`.
The [plan](../../plans/2026-10-16-fixed-point-state-pilot.md) bounds this work.
[Identities](identities.json) retain the lesson, verifier, guidance, accepted model,
prepared-task and installed build-input hashes. No dependency was added or installed.

## What readers can investigate

The correct listing keeps `position` at scale 256 and extracts a separate `pixel`
for drawing. Four half-pixel updates keep stored 128, 256, 384, 512; full positions
0.5, 1, 1.5, 2; and drawn coordinates **0, 1, 1, 2**.

The labelled fault adds one assignment after SHOW, before END, replacing the
position with its whole drawing coordinate at scale 256. It then draws
**0, 0, 0, 0**. The first drawing matches, but retained state differs after update 1
and visible output differs at update 2. Removing that assignment repairs the
stated movement rule. The quarter-step variation draws **0, 0, 0, 1**.

Local recall explains assignment, output, the four inclusive loop visits and
whole-part extraction for these nonnegative values. A separate hint can be
opened before the answer; the Question explanation remains closed until requested.
The new loop-practice link and existing BASIC conversion link remain optional.
No target-language installation, new runtime, layout or prerequisite course is added.

The examples fit the declared unsigned 16-bit storage. The prose requires a
range decision for larger sums rather than silently assuming wrapping or stopping.
The trace counts updates, not time; no smoothness or speed claim is made.

## Model and learner evidence

The accepted [queue model](../2026-10-foundations-evidence-queue/models.json)
already supplies six finite integer/exact-rational traces and three positive
range rejections. We freshly called its retained trace/validation functions for
all six cases and compared them with those accepted results:
[recheck](model-recheck.json). This checks selected paper arithmetic, not arbitrary
pseudocode execution or every possible numeric domain.

The same accepted verifier's wrong-policy mode runs separately and exits nonzero;
[the actual wrong trace](known-red/wrong-trace.json) and
[rejection](known-red/rejection.json) retain that result. The first drawing's
agreement and second drawing's divergence remain explicit. The earlier fractions
pilot's ROM/Z80 observations remain earlier evidence; this slice adds no target
claim requiring another native run.

Use the existing [learner sheet](../2026-10-foundations-evidence-queue/LEARNER-TASKS.md)
and [assessor notes](../2026-10-foundations-evidence-queue/ASSESSOR.md); we do not
copy them into another competing pack. The public listing names its drawing
coordinate `pixel`; the sheet's inline extraction has the same state contract.
No learner has tried the task. Effectiveness, retention and unaided transfer stay
unknown; #114/#115/#124 remain open.

## Final results

The final production build and all **237 tests in 32 files** pass. Chrome
155.0.8059.80 passes the 1440×900 and 390×900 page checks: six keyboard
disclosure opens and four support-link/Back journeys, ten behaviour groups in all.
Original output and model-derived table rows agree; numeric cells stay on one
line and headers use normal word wrapping. No document overflow, page errors or
scoped axe violations were observed.

At 390px, axe leaves one listing line's contrast incomplete in both answer states
because it is clipped by its horizontal viewport. The raw incomplete record is
retained. The [bounded probe](contrast.json) measures the actual text/background
pair at both scroll endpoints: **16.8168:1**, above 4.5:1. This
qualifies those text colours, not all accessibility requirements. Wide/narrow hint,
table, reasoning and quarter-step captures plus both listing endpoints were
visually inspected. The final detector reports no findings.

## Build, browser and evidence checks

[Website results](website-results.json) retain the production build and repository
check outcomes. [Browser results](browser.json) compare the rendered four-row
table against the accepted model, preserve the original two output panels and
check numeric cells stay on one line. Keyboard checks open the independent hint,
prediction explanation and quarter-step answer, then follow both support links
and return at wide/narrow widths. Scoped axe records include incomplete results;
they do not establish whole-site access or screen-reader usability.

Visual review of the [first narrow table](before-table-390.png) found split
header words despite correct values and a passing automated scan. We reused the
existing TraceTable component, whose normal cell wrapping keeps labels intact.
The [initial browser record](browser-before-table-fix.json) remains separate;
the final check also requires normal header wrapping. Readable hint, table,
reasoning and variation captures are retained. The
[design detector](design-detector.json) records the final mechanical scan of the
changed lesson. Existing Pagefind Classic UI notices and sandbox-denied mise
tracking links do not prevent the local checks from completing.

[Evidence validation](validation.json) checks source/build/model identities,
complete rendered rows, selected explanations, wrong-policy rejection and local
links. A wrong source hash and a changed rendered cell must fail. Run
[verify-evidence.py](verify-evidence.py) with `--website PATH_TO_WEBSITE_REPO`.
[SHA256SUMS](SHA256SUMS) covers the retained evidence.

Next, verify approved publication and prioritise reproduced blockers over further
exercise expansion. The public first-session invitation remains available; run
the prepared learner trial when someone is available.
