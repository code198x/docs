# Coverage and Learning Map — 5 November 2026 baseline

We have substantial authored material and selected preserved technical evidence.
This sample does not establish a complete curriculum, comprehensive subject
mastery or measured learning outcomes. Some planning counts lag the actual files.
The [coverage specification](../specifications/coverage-learning-map.md) defines
how to extend this map without confusing targets with implementation.

Tracking: [docs #279](https://github.com/code198x/docs/issues/279).
The [machine-readable inventory](2026-11-05-coverage-learning-map.json) retains
tracked unit paths and SHA-256 identities for the pinned source anchors.

## Baseline and method

Remote HEADs were checked against the inspected repositories on 5 November 2026:

| Repository | Inspected revision | Scope |
| --- | --- | --- |
| code198x/docs | `17f1e47a65bf59f5d07d2203deb70a81cca92dc5` | Charter, curriculum, Craft/maths/library specifications, recurring progressions and selected existing audits |
| code198x/website | `f3124dc4ce0cba4b9701897ca8057a91e0734bcd` | Track/Craft catalogues, file inventories and selected lesson bodies below |
| code198x/code-samples | `5cd1433580ced8a421e0eba4f6dc95b8937cbb45` | Selected BASIC/Z80 sources, browser models and preserved verification records |
| code198x/scripts | `f859907557cc5a29f308328b668ad82fb988886b` | Tracked tree contains only `.gitignore`; do not infer a working shared script suite from the repository name |

Read the selected prose, sources and retained reports; count tracked files at
these revisions, excluding index pages from lesson counts. This pass performs
no new emulator execution, production build, browser/device review, hardware
trial, financial research or learner trial. Unrelated working-copy additions are
excluded. Pinned links below identify the inspected content. Technical historical
claims cited by a lesson are not independently reverified merely by reading it.

The current charter and October scope exception already permit wider game and
creative connections. The prior conversation is motivation, not implementation
evidence or authority to replace that charter. #277 and #278 remain investigations.

## Representative inventory

| ID / surface | Existing content and evidence | What remains unestablished |
| --- | --- | --- |
| B1 — Spectrum BASIC entry | 15 Meet BASIC unit files. Lesson 2 explains assignment, string names, missing-variable diagnosis, source/tape/snapshot distinctions and save/reopen/edit. It includes a prediction before checking the changed name. Maintained source and the stored-value audit support a bounded route. | Whole-entry teaching quality and beginner comprehension; a saved source, downloaded tape and recovered live machine state are separate outcomes. |
| B2 — BASIC game construction | 7 Bright Spark unit files. Lesson 3 stores choices in a string, separates item position from panel identity, exposes the one-character constraint, predicts concatenation and diagnoses a missing/prepended step. | This inspection does not qualify all seven lessons, all BASIC games or the complete game's polish. |
| A1 — Assembly entry and diagnosis | 8 Meet Assembly unit files. Lesson 8 teaches reproduce → hypothesise → inspect → repair → retest, including ordinary and edge movement. The one-byte source copies `%10101010` to `$4000` and sets `$5800`; the README names stock 48K PAL, loading routes and preserved native results. | A source edit is not a running-state change. Retained native checks do not prove current browser operation, all configurations or independent learner diagnosis. |
| A2 — Assembly game and delivery | 36 Meteor Storm unit files and 36 available catalogue entries. Lesson 36 explains cold-ROM tape loading, complete source/assets/loader, release checks, records' lifetime and bounded modifications. Its retained evidence guide distinguishes checkpoint runs, byte comparisons and later emulator versions. | This pass reads the delivery endpoint, not all 36 bodies or every checkpoint. No fresh release, listening, original-hardware or playtest claim is made. |
| M1 — Maths probability and aiming | Units 01–05 and 06–11 cover counts/shares and aiming. The overview offers independent sequences. Existing probability and aiming audits map objectives and qualify selected boundaries; the maintained aiming model uses signed rounding, finite segments and scaled positions. | Those audits retain their original revisions and limits. They do not qualify all current mathematical objectives or demonstrate learner transfer. Matrices, 3D and surfaces remain planned routes in the current overview. |
| M2 — Maths drawing | Two additional authored units (12–13) explain integer-error lines, clipping, ellipse spans, glyph translation, advance, byte/bit addressing, grid stride and platform-specific storage. Both use worked questions and link reusable machine patterns. | The older eleven-unit objective map does not cover these two units. Linked pattern execution cannot by itself verify the maths lesson's explanation or its learning outcomes. |
| C1 — The Craft | 7 catalogue module homes: Maths and Game Feel are in progress, the other 5 coming soon. Game Feel has 4 authored unit files; lesson 4 explains reversal through signs and a worked 1/60-second update, contrasts the playground rule and suggests an observed stopping task. | Skills in a catalogue are not available sequences. Game Design, AI, Data/Algorithms, Graphics/Animation and Sound/Music have agreed homes; dedicated authored shared sequences are not established by this catalogue/sample. Related system lessons and patterns can already exist. |
| P1 — Pattern Library | 1,038 MDX files in the tracked pattern tree, including indexes where present; not an audited count of independent capabilities. One inspected Spectrum BASIC projectile entry provides include/init/call contracts, bounded input rules, dominant-axis normalisation, a wrong/fixed caller, costs and retained native evidence. | One well-qualified entry does not qualify the library, every machine/language or a complete projectile/game. Missing dedicated entries can be extraction/cataloguing gaps, not missing code. |
| V1 — Vault | 1,621 MDX files in the tracked Vault tree, including indexes where present. Budget Games supplies distribution history, source locators, a contemporary full-price costing and explicit uncertainty. | Page counts and `reviewed` flags do not certify accuracy, geographic balance or depth. The £6.95 costing is described as speculative and has an editorial interpretation of a printing error; it is not a verified £1.99 business model or modern pricing evidence. |
| T1 — Tooling and evidence | The website continuity checker explicitly sets `executionVerified: false`; clean builds and source inclusion are its remit. Samples retain native verifiers and models; Meteor Storm names Asm198x/Build198x and fresh ROM loading. | Tool existence and CI evidence checking do not prove native execution was rerun. Sibling tooling capabilities are not automatic curriculum coverage or promises of support. |

### Inspected anchors

- **B1:** [Meet BASIC lesson 2](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/src/content/curriculum/sinclair-zx-spectrum/basic/meet-basic/unit-02-remember-and-save.mdx); [maintained greeting](https://github.com/code198x/code-samples/blob/5cd1433580ced8a421e0eba4f6dc95b8937cbb45/sinclair-zx-spectrum/basic/meet-basic/opening/unit-02/steps/step-01.bas).
- **B2:** [Bright Spark lesson 3](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/src/content/curriculum/sinclair-zx-spectrum/basic/bright-spark/unit-03-remember-an-order.mdx).
- **A1:** [Meet Assembly lesson 8](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/src/content/curriculum/sinclair-zx-spectrum/assembly/meet-assembly/unit-08.mdx); [one-byte program](https://github.com/code198x/code-samples/blob/5cd1433580ced8a421e0eba4f6dc95b8937cbb45/sinclair-zx-spectrum/assembly/meet-assembly/opening/one-byte.asm); [native evidence](https://github.com/code198x/code-samples/blob/5cd1433580ced8a421e0eba4f6dc95b8937cbb45/sinclair-zx-spectrum/assembly/meet-assembly/opening/verification/evidence/native-results.json).
- **A2:** [Meteor Storm lesson 36](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/src/content/curriculum/sinclair-zx-spectrum/assembly/meteor-storm/unit-36.mdx); [checkpoint evidence guide](https://github.com/code198x/code-samples/blob/5cd1433580ced8a421e0eba4f6dc95b8937cbb45/sinclair-zx-spectrum/assembly/meteor-storm/verification/evidence/README.md).
- **M1:** [Maths overview](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/src/content/curriculum/craft/maths-for-games/index.mdx); [aiming model](https://github.com/code198x/code-samples/blob/5cd1433580ced8a421e0eba4f6dc95b8937cbb45/craft/maths-for-games/aiming/model.mjs).
- **M2:** [integer drawing](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/src/content/curriculum/craft/maths-for-games/unit-12.mdx); [glyph translation](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/src/content/curriculum/craft/maths-for-games/unit-13.mdx).
- **C1:** [Game Feel lesson 4](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/src/content/curriculum/craft/game-feel/unit-04.mdx); [Craft catalogue](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/src/content/modules/craft.yaml).
- **P1:** [Spectrum BASIC aimed projectile](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/src/content/patterns/sinclair-zx-spectrum/basic/physics/aimed-projectile.mdx); [routine](https://github.com/code198x/code-samples/blob/5cd1433580ced8a421e0eba4f6dc95b8937cbb45/sinclair-zx-spectrum/patterns/basic/physics/aimed-projectile/routines.bas); [retained normal run](https://github.com/code198x/code-samples/blob/5cd1433580ced8a421e0eba4f6dc95b8937cbb45/sinclair-zx-spectrum/patterns/basic/physics/aimed-projectile/verification/demo.json); [tool/firmware identities](https://github.com/code198x/code-samples/blob/5cd1433580ced8a421e0eba4f6dc95b8937cbb45/sinclair-zx-spectrum/patterns/basic/physics/aimed-projectile/verification/configuration.json).
- **V1:** [Budget Games](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/src/content/vault/distribution/budget-games.mdx).
- **T1:** [Spectrum continuity/build checker](https://github.com/code198x/website/blob/f3124dc4ce0cba4b9701897ca8057a91e0734bcd/scripts/check-spectrum-samples.mjs).

Related preserved work: [stored-value pilot](2026-10-spectrum-learner-journey/stored-value-pilot/REPORT.md),
[Foundations coverage](2026-10-foundations-coverage.md),
[probability objectives](2026-10-probability-pilot/OBJECTIVES.md),
[aiming boundaries](2026-10-aiming-boundaries/REPORT.md),
[Pattern Library inventory](2026-10-19-pattern-library/README.md) and
[audio evidence](2026-10-10-audio-evidence.md). Their observations apply to their
named revisions and cases. The stored-value report explicitly records pending
learner tasks and a failed supplemental harness; this audit does not promote
those outcomes to passes or claim the pending state describes every later audit.

## Quality assessment

These are judgements about the inspected material, not numerical ratings.

| Slice | Breadth and depth | Accuracy | Practicality | Transferability | Educational effectiveness |
| --- | --- | --- | --- | --- | --- |
| B1–B2 | Concrete storage, representation and lifecycle explanations; two lesson bodies sampled | Source/prose correspondence inspected; prior stored-value checks have narrower scope | Maintained listings, change/predict tasks and save/recover instructions | Actual optional Foundations links; general storage/representation principles | Unknown in this pass; no learner observations collected |
| A1–A2 | Memory, diagnosis and shipping endpoints; middle progression not fully read | Small source inspected and retained native records found; no fresh rerun | Fault cases, explicit load paths and release checklist | Local investigation method and release-state distinction generalise; broader ports unassessed | Unknown; execution success does not establish independent diagnosis |
| M1–M2 | Probability/aiming plus two drawing lessons; broader matrix/curve scope remains target | Preserved selected numerical checks; new drawing prose not independently qualified here | Worked arithmetic, questions, models and linked routines | Explicit links from mathematical relationships to differing machine representations | Unknown; an interactive control is no comprehension measure |
| C1 | Four response lessons; one reversal body read; other shared modules remain direction | Worked rule and changed assumptions explicit; not a numerical or browser rerun | Controlled comparison and proposed stopping playtest | Lesson distinguishes its rule from playground presets | Unknown; suggested playtest is not recorded feedback |
| P1 | One bounded routine with full contract; inventory breadth not semantic coverage | Source implements declared dominant-axis rule; preserved records name tool/firmware hashes | Normal/custom/wrong/repaired paths and cost exclusions | Maths/Craft links exist; Euclidean-speed differences explained | Unknown; no second-user adaptation observed here |
| V1 | Distribution context, not a business course | Primary locators and uncertainty present; originals not independently reread | Useful research starting point; no editable economics exercise established | Natural #278 historical/modern bridge remains proposed | Unknown; no tested economic reasoning task |

## Existing and candidate connections

| Connection | Status and useful distinction |
| --- | --- |
| BASIC storage ↔ Foundations ↔ assembly bytes | BASIC lesson 2 explicitly links Foundations; existing stored-value pilot supplies cross-surface tasks. Named BASIC variables, assembler labels and registers are not interchangeable. |
| Aiming ↔ reusable projectile | P1 actually links Maths/Craft. Its dominant-axis speed rule differs from a Euclidean trigonometric direction; a shared subject does not make these implementations equivalent. |
| Grid maths ↔ native glyph routines | M2 directly links patterns and explains storage/stride/visibility differences. Shared arithmetic does not imply portable hardware contracts. |
| Game Feel ↔ native game response | Candidate comparison: retain units and update rules, then show changed input/timing budgets. The browser playground supplies no native timing evidence. |
| Finished tape ↔ publishing economics | Candidate route from A2 to V1/#278: a loadable tape is one component of a release; manufacture, rights, margins and support need separate evidence. |
| Paper design ↔ glyph bytes or a small game | Candidate #277 pilot using existing assets and lessons, with accessible digital alternatives; no new robotics hardware or full renderer required. |

## Prioritised gaps and owners

Priority is a recommendation for review, not a commitment to implement. Fix
misleading status before expanding scope. Importance of a domain does not decide
its urgency; the smallest next action should resolve a known uncertainty.

| Gap | Kind / priority | Bounded next action and owner |
| --- | --- | --- |
| G1 — Planning counts lag sources | Status / first | Docs: reconcile the maths/Craft eleven-unit wording with units 12–13 and the Meteor Storm 24-lesson wording in the charter with the current 36-unit catalogue. Preserve dated audit counts as historical evidence; do not bulk replace them. Check lesson bodies before stronger status claims. |
| G2 — Drawing lessons outside older objective map | Evidence / next | Docs with website/samples evidence: map units 12–13 outcomes, local knowledge and one representative boundary each. Reuse the maths and Pattern Library audits; distinguish calculation, native routine and learner evidence. |
| G3 — Independent learning remains unmeasured here | Learning evidence / next | Reuse an existing stored-value/diagnosis learner task and assessor, record observed predictions, repair and transfer. Decide human-review/trial scope before claiming effectiveness; no new assessment platform. |
| G4 — Connections remain partly implicit | Editorial experiment / next | #277 owns selection of one analogue/digital pilot and two reviewed historical-to-modern bridges. Reuse B1/A1/M2; name where each analogy stops. Website changes require a bounded agreed design. |
| G5 — Economics depth exceeds authored exercise evidence | Syllabus/pilot / later | #278 owns the source-backed budget worksheet and dated modern comparison. Reuse V1, distinguishing the speculative full-price model from budget facts and hypothetical assumptions. |
| G6 — Wider catalogue is not fully audited | Sampling / deferred expansion | Use #117's capability hierarchy and existing Craft/recurring-progressions work. Select the next machine/language or subject from a concrete question; do not create hundreds of parallel tickets or infer absent code from catalogue gaps. |

This audit changes no learner-facing content or specialist scope. It does not
close #277, #278, discovery #10, Pattern Library #117 or existing Craft work.
The tracking issue should close when this baseline/specification is accepted,
G1–G3 have bounded dispositions and the owners of G4–G6 are linked; it must not
wait for every aspirational depth target to be delivered.
