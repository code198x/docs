# Foundations: complete objective and prerequisite inventory

We have read and mapped all **39 authored units and ten module overviews** at
website revision `2b9905262dcb7261314b6ef6490db7b8a5c803ed`. The
[per-unit map](MAP.md) names each unit's goals, knowledge used, local recall and
optional support. This completes the per-unit source inventory gap identified in
[the umbrella reconciliation](../2026-10-education-reconciliation/REPORT.md).
It does not establish that every objective is accurate, every example executes,
or that learners can transfer the ideas unaided. Umbrella
#114 remains open.

## Source and method

The [plan](../../plans/2026-10-16-foundations-objective-map.md) bounds this review.
Docs baseline is `8e5c619167ffbb745b9da926d8d45823356f5b83`, after the approved
Safari evidence merged in [docs #83](https://github.com/code198x/docs/pull/83).
We used immutable Git source, not a claim about today's deployed pages.

[The records](units.json) separate each lesson's own learning-summary text from
reviewer synthesis. They retain titles, paths, source hashes, opening excerpts,
explicit Question/disclosure prompts and authored Markdown links. The baseline catalogue text and hash are retained too.
We read the
complete bodies; metadata and headings alone did not establish the goals or
knowledge used. Reviewer support suggestions identify helpful explanations,
not required attendance or a new sequence. Some point to a later module because
the concept appears earlier in an example; this is not a course dependency graph.

The review follows [curriculum design](../../specifications/curriculum.md),
[unit guidance](../../specifications/unit.md) and
[pseudocode](../../specifications/pseudocode.md). Shared examples remain teaching
notation. The same spelling does not prove identical target-language rules.
BASIC and assembly remain independent entry points.

## What the map adds

| Evidence | Result | Boundary |
| --- | --- | --- |
| Exact authored source set | 39 units, ten overviews | Inventory complete for this revision; future units require refresh |
| Per-unit goals and entry knowledge | All 39 mapped | Reviewer interpretation, with the original learning summaries retained |
| Local recall and optional support | All 39 reviewed | A short recall is not evidence that a beginner has enough explanation |
| Explicit Question/disclosure markup | Present in 35 units | Markup presence is not assessment quality; ordinary prose can also ask a question |
| Examples executed in this slice | Not rerun | Existing pilot runs keep their own source, input and environment limits |
| Actual learner outcomes | Unknown | No learner available; no completion, retention or transfer claim |

Four units have no explicit Question/disclosure prompt: Basics 3, Decisions 4,
Repeating 1 and From Source to Silicon 2. They contain worked examples and
troubleshooting. This is a useful selection aid for a future understanding check,
not a defect count or a reason to impose a question after every unit.

The [existing coverage map](../2026-10-foundations-coverage.md) retains the relevant
pilots: sequence/input and stored values; arithmetic; decisions/boundaries and
saved state; Boolean tables; loop progress/exits; structure; binary/hex and signed
numbers; bits/shifts, characters and fractions; gates/adders; and translation.
Their model, native and browser checks remain sampled evidence. We do not turn
module-level report links into a claim that every goal in the new map was tested.
The [probability pilot](../2026-10-probability-pilot/REPORT.md) separately maps the
eleven published Maths for Games units; they are not extra Foundations units.

## Finding: summaries retained claims corrected in the lessons

[Website #752](https://github.com/code198x/website/issues/752) owns a bounded
summary correction. All-state Working the Bits/overview searches found the
completed unit findings, but no open summary finding.

The Working the Bits overview still requires finishing Counting in Twos and
Decisions. Its shape list calls shifting the machine's fastest multiply and says
floating-point can never be exact. The actual revised units separate Boolean and
bitwise jobs, qualify shift speed, and distinguish exact binary fractions from
rounded ones. The root cause is a scope gap: the earlier
[#705](https://github.com/code198x/website/issues/705) and
[#708](https://github.com/code198x/website/issues/708) corrections addressed the
unit bodies while these overview statements remained.

The Foundations catalogue's From Source to Silicon entry also says translation
timing decides whether a game keeps up, and contrasts source text with numbers
that run. Its revised lessons explicitly separate instruction/data roles and
qualify performance by implementation and workload. The correction changes only
that entry's tagline/skills and the Working the Bits overview. All module order
and requires data stay as authored. Catalogue relationships do not become learner
attendance requirements through this review.

The proposed overview names knowledge used, links optional support, and summarises
the five actual lesson contracts. It introduces no new hardware claim, runtime,
representation, dependency or architecture. The retained map describes the
**baseline**, including the old overview; the proposed summary change does not
silently rewrite that source snapshot.

## Verification and limits

[verify.py](verify.py) checks the complete Git source set, source hashes, exact
objective/prompt excerpts and their line numbers, authored links, support targets
and document links. Run it with `python3 verify.py --website PATH_TO_WEBSITE_REPO`.
Its [validation record](validation.json) includes deliberate missing-unit,
wrong-hash, invented-excerpt and unknown-support rejections. These checks can fail;
they do not mechanically certify the reviewer's interpretation or teaching quality.

The separate [website verification record](website-validation.json) records the
production/content checks and generated overview inspection for the proposed fix.
The final build verifies the shared frame on 2459 public pages; all 237 tests
pass, including prepared decoder checks. Catalogue structure comparison confirms
that only the selected tagline/skills change. The generated overview contains
the qualified wording and its three support links resolve to built pages. The
same wording check rejects the baseline overview.

An initial artifact assertion expected the catalogue tagline on the Foundations
landing page and failed. Inspection showed its cards use overview descriptions;
we corrected the assertion. The catalogue edit is a metadata correction, not
evidence that this landing page displayed the stale tagline.
The initial isolated build lacked the prepared player catalogue and failed with
`Could not resolve '../../public/emulators/catalog.json'`. A later build reached
an endpoint but lacked the sibling sample path: `ENOENT` for
`code-samples/_capture/crash-live/typein-198x-c64.bas`. The first full check also
failed with `ERR_MODULE_NOT_FOUND` for the unprepared NES WASM assembler.
We reused the existing generated assets and documented sample/decoder path
settings; no dependency or product code was changed to work around these failures.
These were checkout preparation failures, not passes or diagnosed lesson defects.

No new native/browser execution, screen-reader, physical-device or learner trial
is claimed. The summary edit does not change layout or machine behaviour. Prior
Safari save/reopen evidence remains in its
[own report](../2026-10-first-session-operability/REPORT.md), with VoiceOver skipped
at the user's request and physical touch untested.

## Next bounded work

Directly audit Decisions unit 4's compound-condition examples across their stated
numeric domains. Distinguish an inclusive numeric interval from whole-number input
validation, use cases that separate AND from OR and expose grouping mistakes, and
prepare one independent prediction/repair check. Existing Boolean tables and the
native BASIC operator contrasts are starting evidence; verify each claimed
transfer against its actual target contract. This is a candidate investigation,
not a claim that accepting a fraction is already a bug.

Keep learner observation separate. No source inventory, sample execution or
prepared assessment closes #114/#115/#124 on its own.
