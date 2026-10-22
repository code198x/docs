# Education umbrella: evidence and remaining work

We have delivered sixteen bounded pilots and an integrated journey improvement.
They justify continuing with smaller, evidence-led audits. They do not establish
that learners understand the material, or that the three umbrella issues are complete.
All three remain open. The next bounded slice is the published probability material
in [docs #78](https://github.com/code198x/docs/issues/78).

This reconciliation records the position on 15 October 2026 after approved
[website #745](https://github.com/code198x/website/pull/745) and
[docs #77](https://github.com/code198x/docs/pull/77) merged. Website source is
`4c9f3bbcb27d1386c3930c17b9745cdcc702ac48`; retained docs evidence is
`e2dc71b59be99a1bf0eabb932306a2fe91467e27`. Historical reports describe the
proposed changes and environments at their own dates. References to drafts in
those reports are historical, not the current state of those approved changes.
This reconciliation does not repeat their runtime checks against today's deployment.

## What we counted

[The report registry](report-registry.json) identifies sixteen pilot reports and
five supporting records by path and SHA-256. Each report links its fixtures,
results, sources and limits. A report count is not a count of validated objectives.

[The current source inventory](source-inventory.json) retains titles, second-level
headings and content hashes from the immutable website revision above:

- Foundations: ten module overview files and **39 unit files**.
- Craft / Maths for Games: one overview and **11 unit files**, five probability
  units followed by six aiming units.
- Total: **61 MDX files**. No files were found under `craft/dice-roller` at this
  revision. This inventory does not count a separately hosted experiment as
  another set of curriculum units.

The [Foundations coverage map](../2026-10-foundations-coverage.md) maps selected
technical evidence to all ten modules. Titles and headings are an inventory aid;
they do not replace an objective-by-objective prerequisite audit. The
[Maths for Games specification](../../specifications/maths-for-games.md) separates
published material from broader planned topics. We have not reconciled its eleven
published units against the umbrella criteria in this pilot series. That is a
coverage gap in this review, not a claim that the existing maths has never been tested.

## Acceptance reconciliation

We use **met for the selected scope**, **partial**, **unknown** and **skipped**
explicitly. A selected technical pass cannot close a broader educational criterion.
The parent issues #114, #115 and #124 are private, so their wording is not
retained here; [parent-issues.json](parent-issues.json) identifies the exact text
used by its length and SHA-256.

### #114: shared concepts and transfer

| Requirement | Outcome | Evidence and remaining boundary |
| --- | --- | --- |
| Inventory objectives and prerequisites across Foundations, including game maths | Partial | Ten-module coverage map and 39-unit source inventory; pilot-specific objectives/prerequisites. A complete per-unit objective map and the eleven game-maths units remain unreconciled. |
| Sample and test examples; identify misconceptions and cross-system dependencies | Met for the selected scope | Sixteen pilot reports retain bounded model/native/browser contrasts and findings. Sampling is not exhaustive curriculum or cross-machine qualification. |
| Prototype predict, explain, modify, debug and create assessments | Met for the selected scope | Stored-value and subsequent pilot learner tasks have separate assessor material. Their existence does not establish task difficulty or independent transfer. |
| Separate editorial, technical and actual learner evidence | Met as reporting; learner outcomes unknown | Reports distinguish expert review, execution and prepared learner tasks. No learner observations are retained. |
| Record results with source/version/environment identities and pass/fail/skipped/unknown outcomes | Met for the selected runs | Registry reports link identities and raw results. Older gaps and failed attempts remain gaps; no blanket current-site pass follows. |
| File specific findings without a second implementation plan; link findings, limits and next step | Met for this reconciliation | Existing closed findings remain linked in the pilot reports; the four follow-ups below own fresh work. This report links the remaining boundaries. |

Preserve the separate conceptual and machine routes. We have not agreed a broad
rewrite, a compulsory prerequisite course or a new curriculum structure.

### #115: Spectrum BASIC and assembly pathways

| Requirement | Outcome | Evidence and remaining boundary |
| --- | --- | --- |
| Select one bounded pathway in each language and identify objectives/prerequisites | Met for the selected scope | The stored-value pilot connects optional Basics work to Meet BASIC remember-and-save and Meet Assembly byte-to-pixels; it distinguishes names, addresses and copied values. |
| Reproduce examples on named machines/tools, from source artefact to execution | Partial | Native BASIC checks and assembly build/load/RAM/screen evidence qualify named configurations. Maintained browser assembly checks and later greeting/edit/export checks qualify their own tasks. The exact supplemental BASIC repeated-read/error task did not qualify in the browser. |
| Prepare independent transfer and troubleshooting tasks | Met as preparation | Stored-value learner tasks include prediction, modification, error repair and creation. Later pilots extend the set; no actual unaided completion is recorded. |
| Gather learner evidence where possible; revise friction and lesson contracts | Partial; learner outcomes unknown | Bounded corrections and specification changes are delivered. The owner reports no learner available yet. Expert execution is not evidence of educational effectiveness. |
| Record identities/outcomes, file specific findings, and link reviewed limits/next step | Met for the retained scope | Reports preserve successful runs and failed harness attempts separately. Website #747 owns the remaining exact embedded task; #115 retains learner-trial ownership. |

The [stored-value report](../2026-10-spectrum-learner-journey/stored-value-pilot/REPORT.md)
names native Emu198x Spectrum 0.32.5, Asm198x 0.0.64 and PasmoNext 0.1.3;
PasmoNext is not upstream Pasmo. Its native ROM fingerprint does not establish
the browser ROM identity. The failed supplemental browser observation returned an
empty transcript; we did not count it as a product pass or diagnose a product bug.
The [first-session publication](../../guides/first-session/PUBLICATION.md) later
verified a different greeting/edit/export route, so it does not silently replace
that exact missing result.

### #124: integrated learner journey

| Requirement | Outcome | Evidence and remaining boundary |
| --- | --- | --- |
| Select a journey across concepts, machine lesson, optional reference, running and understanding check | Partial | Original discovery review and stored-value pilot provide real page/task routes and optional Vault connections. Understanding checks are prepared, not observed with learners. |
| Cite pages, browsers, device sizes, tasks, measured results and known limits | Met for named runs; partial across scope | Original journey, pilot and publication reports retain the page/viewport/task evidence. Viewport emulation is not a physical mobile test; embedded latency is unknown. |
| Review navigation, readability, experimentation, media/audio accessibility and embedded latency | Partial | Expert navigation, code/source controls, edit/run/revert/export, narrow layouts and scoped accessibility checks have evidence. Broader assistive technology, touch, audio access and end-to-end latency remain unqualified. |
| Deduplicate findings and report up to five first priorities | Met here | Four bounded follow-ups and the existing learner-trial ownership form the five-item queue below. Resolved findings are not reopened. |
| Deliver one bounded improvement with before/after evidence | Met for delivery | Original journey fixes in website #617 have local/live follow-up evidence. No learner outcome comparison follows from those checks. |
| Preserve site identity and cross-platform accessibility | Partial | Bounded lesson/control fixes preserve the existing site structure. Chromium and scoped scanner results do not establish cross-platform accessibility. |
| Measure outcomes with learners | Unknown | No learner available; first-session prompts and observation sheet are ready. No completion, hint-rate, retention or transfer claims. |

The [original review](../2026-10-spectrum-learner-journey/REPORT.md) and
[fix evidence](../2026-10-spectrum-learner-journey/FIXES.md) cover actual navigation,
editing, diagnostics, export and recovery. Website
[#617](https://github.com/code198x/website/pull/617), merged at
`3484ed4a5592cb4cd8bc50aa4ea9c9a65d0fff12`, addressed the six original findings.
The first-session publication retains mixed local/live origins for part of the
reopen check; it is not a uniform local-origin qualification. Its machine tasks
were desktop interactions. Narrow layout and keyboard checks do not prove touch
operability. The reports name Chromium-based environments and their tool versions;
they do not qualify Safari, physical mobile hardware or screen-reader use.

## Resolved work and evidence limits

The sixteen reports cover stored values; decisions and boundaries; repetition;
numbers; bits and shifts; fractions; character codes; Boolean logic; arithmetic;
structure; binary/hex; gates/adder; source/translation; sequence/input;
ordered decisions/saved state; and repetition progress/exits. The latest pair adds
reachable versus guaranteed exits and progress versus inner reset.

The [decimal investigation](../2026-10-decimal-investigation/REPORT.md) resolved
the observed conversion behaviour as stock-ROM behaviour, with an independent
Fuse comparison. Docs #63 is closed. It is not an outstanding emulator fix, and a
disposable patched-ROM counterfactual is not a shipped correction. The
[Structure contrast follow-up](../2026-10-structure-pilot/contrast-follow-up/REPORT.md)
retains the bounded contrast checks; it is not whole-site accessibility certification.

Successful native runs establish the named inputs, representations and machine
configurations. Model traces are not execution of pseudocode in a shared runtime.
Scoped axe scans do not measure comprehension, audio accessibility or every colour
combination. Repeated pilot checks do not create a learner sample. We have not
measured unaided completion, retention, transfer or educational effectiveness.

## Five next priorities

Order reflects useful next work with available evidence. Reproduced learner or
technical blockers may change it. We keep the existing first-session pack small
until observations justify expanding it.

| Order | Next action and owner | Completion signal |
| --- | --- | --- |
| 1 | [Docs #78: game-maths objectives and one probability boundary](https://github.com/code198x/docs/issues/78) | Map the eleven authored units, select a bounded boundary in units 1–5, retain source/native evidence and independent learner tasks before proposing corrections. This is the next curriculum slice. |
| 2 | [Website #747: exact embedded BASIC task](https://github.com/code198x/website/issues/747) | Reproduce the old observation failure; retain actual repeated reads, replacement, error and successful repair in the maintained browser machine. Missing output must fail. |
| 3 | [Website #748: startup/edit-to-result latency](https://github.com/code198x/website/issues/748) | Define user-visible boundaries and retain repeated cold/warm timings with actual machine success, cache/network/device identities and raw observations. No assumed performance defect or invented budget. |
| 4 | [Website #749: broader first-session operability](https://github.com/code198x/website/issues/749) | Qualify one route on declared browser/input/assistive-technology configurations; record unavailable hardware as skipped and file only reproduced blockers. Coordinate with umbrella #123. |
| 5 | Existing umbrella #115 and #124: uncoached learner trial | Use the [published pack](https://code198x.com/try/) and [observation sheet](../../guides/first-session/session-observations.md) when a learner is available. Record help and prediction/explanation separately from copying or successful execution. |

We searched existing open site/docs issues and targeted all-state searches before
filing. The four [retained follow-up bodies](follow-ups.json) describe evidence gaps,
not speculative product defects. No new teaching-architecture decision is needed
for this queue; a conflict discovered while reading the maths requires consultation
before changing agreed direction. None of these follow-ups closes the parents.

## Reconciliation verification

[The validation record](validation.json) records positive inventory/report counts,
source/report hashes, parent snapshots and new local links. These checks validate
this document's evidence references. They do not rerun the browser/native pilots,
measure latency, or supply missing learner observations.
