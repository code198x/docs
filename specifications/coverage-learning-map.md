# Coverage and Learning Map

We map what Code198x teaches, how we know, and where we might develop it next.
Current material and intended depth are separate records. Neither a topic name,
an approved module nor a large catalogue establishes mastery.

Apply the [charter](../PROJECT.md), its admission test and
[curriculum design](curriculum.md). The current charter says **Play · Build ·
Understand**; the earlier conversation and issues #277/#278 use **Learn. Build.
Understand.** This map applies the current charter without renaming those issues
or treating their investigations as adopted curriculum changes. BASIC and
assembly remain independent entry points. Historical-machine understanding,
creative work and investigation are worthwhile without a compulsory game outcome.

## Authority and scope

This specification owns the cross-curriculum taxonomy, record format and rules
for assessing coverage. The [5 November baseline](../audit/2026-11-05-coverage-learning-map.md)
owns the first representative inventory and gap register. It samples Spectrum
BASIC/assembly, Maths for Games, The Craft, Pattern Library and Vault; it does not
classify the entire site or certify the sample's complete teaching quality.

Keep existing authorities:

- [Craft coverage](craft-coverage.md) owns the seven agreed module homes.
- [Maths for Games](maths-for-games.md) owns mathematical scope and direction.
- [Recurring progressions](recurring-progressions.md) owns cross-game threads;
  its linked experiments own their detailed outcomes and constraints.
- [Pattern Library](pattern-library.md) and [Vault](vault.md) own their delivery
  and source standards. Their catalogues are different kinds of coverage.
- The website owns lesson bodies and navigation; code-samples owns maintained
  runnable sources and verification recipes. Docs owns teaching specifications.
- [Current work](../work.md) and existing issues own delivery priorities. The
  domain list below creates no new module, prerequisite, track or tooling project.

## Knowledge domains

Domains are analytical tags, not proposed navigation. A subject can have several
tags but one primary teaching home. Importance, depth and urgency are separate.
The roles below describe the map's relationship to the current mission; adjacent
subjects still require the charter's admission test before commissioning.

| Domain | Role | Representative subjects | First-pass evidence or boundary |
| --- | --- | --- | --- |
| Programming | Core | Languages, algorithms, representation, decomposition | BASIC strings and state; Z80 instructions/routines (B1–B2, A1) |
| Computing systems | Core | CPU, memory, display, timing, interfaces | Spectrum byte/display and timing investigations (A1–A2) |
| Mathematics | Core | Probability, geometry, numerical methods | Counts/shares, aiming and integer-grid drawing (M1–M2) |
| Game development | Core | Rules, behaviour, levels, feedback, playtesting | Bright Spark, Meteor Storm and Game Feel (B2, A2, C1) |
| Creative production | Core | Images, fonts, animation, sound, narrative | Glyph mathematics and Meteor Storm assets; shared modules remain planned (M2, A2, C1) |
| Software engineering | Core | Debugging, testing, contracts, profiling, shipping | Fault diagnosis, cold tape delivery and bounded library contracts (A1–A2, P1) |
| Physical computing | Adjacent | Electronics, sensors, feedback, robotics | Gate models have separate Foundations evidence; no physical robotics course established in this sample |
| Production and business | Adjacent | Costs, teams, manufacturing, publishing, rights | Budget Games context exists; #278 owns syllabus/pilot investigation (V1) |
| History and society | Cross-cutting | People, culture, industry, geography, ethics | Vault distribution history sampled; worldwide balance not assessed (V1) |
| Research and preservation | Cross-cutting | Sources, provenance, verification, reverse engineering | Cited manuals, preserved execution records and research audits; presence does not establish a taught archival-method sequence (A1, V1, T1) |

IDs refer to the baseline, not separate content to author. The map can show
connections beyond games without promising a comprehensive degree in every
connected discipline or general modern framework tutorials.

## Coverage records

For each bounded subject, retain:

1. Stable ID, question/outcome, domain tags, primary home and intended audience.
2. Current authored coverage: exact lesson/source paths, repository revisions,
   inspected portions and explicit exclusions. Say **not established in this
   sample**, rather than declaring absence across the ecosystem.
3. Evidence: source review, build, native execution, browser operation, historical
   source checking and learner observations separately. Name configuration,
   source/tool/firmware identities, cases, date, results and limitations for
   execution. Label retained evidence as retained; do not imply a fresh rerun.
4. Observed teaching affordances: prediction, construction, explanation,
   experimentation, diagnosis and independent adaptation. These are opportunities
   the material provides, not measured learner achievements.
5. Quality assessment across the six dimensions below, with supporting evidence
   and unknowns. Do not infer accuracy from a `reviewed` flag or learning from CI.
6. Target depth and its decision status (existing direction, proposed or deferred),
   independent of current coverage. Link the specialist scope that governs it.
7. Connections: source → destination, the useful shared idea, changed assumptions,
   and whether the actual learner-facing link or only a potential bridge exists.
8. Gap kind, impact, next bounded action, priority rationale, owning repository
   and existing issue. Reuse a ticket before creating another.

Use **authored**, **source-reviewed**, **built**, **executed in named configuration**,
**live-checked**, and **learner-observed** as independent evidence labels. They are
not a universal ladder: historical prose does not need native execution, while
native execution does not verify the prose's historical claims. A verification
script's existence establishes a recipe, not a passing result.

## Depth targets

These labels describe desired material, not learner rank, prerequisites or a
completion percentage. Assign them to bounded subjects, never whole repositories.

| Depth | Intended material | Evidence needed before claiming that depth is delivered |
| --- | --- | --- |
| 1 — Reference | Accurate context and routes for further investigation | Reviewed explanations and checkable sources for the stated boundary |
| 2 — Applied understanding | Explained demonstrations and small experiments | Worked reasoning, runnable/inspectable examples where relevant and useful changes to try |
| 3 — Working competence | Connected lessons enabling independent adaptation | Coherent local support, varied applications and reviewed independent tasks; learner outcomes still require observation |
| 4 — Deep mastery | Advanced coverage, competing approaches and independent investigation | Explicit advanced scope, varied constraints, rigorous qualification and substantial independent work; no blanket certification from lesson count |

Initial planning targets are **proposals**, except where a specialist
specification already agrees direction. No numerical depth is assigned to current
coverage in this first pass: a small sample cannot substantiate a whole strand's
ceiling.

| Bounded subject | Proposed target | Decision boundary |
| --- | --- | --- |
| Spectrum representation, routines and diagnosis | 3, with selected 4 investigations | Existing deepening direction; this number does not approve a new lineup |
| Aiming, grid drawing and fixed-point reasoning | 3 | Broader maths direction already agreed; matrix/3D/curve coverage remains development work |
| Controls, response and deliberate feedback choices | 3 | Use Game Feel's existing sequences; do not infer every sequence is authored |
| One reusable machine/language capability | 2–3 | Apply Pattern Library contracts and #117; advanced variants separately scoped |
| Budget publishing context | 1 | Existing Vault context; historical claims still need source checking |
| One production-economics worksheet | 2 | Candidate under #278, not an approved course |
| Analogue-to-code design connection | 2 | Candidate under #277, with accessible physical/digital alternatives |
| Physical robotics and comprehensive rendering course | Unset/deferred | Investigation first; this audit commissions neither |

## Quality and learning

Assess **breadth** (concepts actually addressed), **depth** (reasoning and scope),
**accuracy** (technical/historical evidence), **practicality** (reproduction and
adaptation), **transferability** (applications and changed constraints), and
**educational effectiveness** (observed understanding).

Record a short judgement and limits for each dimension; avoid a composite score.
A lesson with a good explanation may lack execution evidence. An executed routine
may lack a usable explanation. A structured review can identify teaching risks,
but only observed learner work can establish the corresponding learning outcome.
Use existing learner packs and assessors before adding another assessment system.

## Connections and sequencing

Prefer optional routes through existing material: BASIC storage ↔ Foundations
assignment ↔ assembly memory; aiming ↔ projectile contracts; grid maths ↔ glyph
placement; controls ↔ game feedback; finished tape ↔ distribution history.
The baseline distinguishes existing links from editorial candidates. Explain
historical-to-modern transfer through a concrete principle and changed constraints;
a superficial analogy is insufficient. #277 owns the reviewed bridge pilot.

## Maintenance and tracking

Refresh affected records when lessons, catalogues, samples, verification or
specialist scope change. Record a new revision and inspect changed bodies before
promoting a claim. Keep dated audits as bounded evidence; the latest applicable
record must be linked here. Do not silently carry old execution claims onto new
sources or overwrite a good inventory after an empty/failed query.

Check counts from tracked Git trees and keep index pages separate from units.
No percentage-complete report is valid without an agreed denominator and quality
criteria. Reconcile discrepancies with current sources rather than copying stale
counts from planning prose. Prioritise incorrect explanations and misleading
status before new coverage; then improve connections and review a small pilot.

Coordinate with [#277](https://github.com/code198x/docs/issues/277),
[#278](https://github.com/code198x/docs/issues/278),
[discovery #10](https://github.com/code198x/docs/issues/10),
[Pattern Library #117](https://github.com/code198x/docs/issues/117), existing
Craft coverage and the Foundations audit. [Tracking issue #279](https://github.com/code198x/docs/issues/279) owns bounded
reconciliation and follow-up decisions, not completion of all target depths.
