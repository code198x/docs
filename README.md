# Code198x documentation

Start with **[PROJECT.md](PROJECT.md)** for the goals, audience, scope and teaching principles. This README is the documentation index. [Current work](work.md) identifies the next bounded tasks and proposals; it does not redefine project policy.

Original prose is licensed under **CC BY 4.0**. See [LICENSE.md](LICENSE.md) for scope, attribution and exclusions; software and third-party material retain their own terms.

## First sessions

The [public first session pack](https://code198x.com/try/) offers independent
Spectrum activities and support for parents and teachers. Its
[maintenance and trial notes](guides/first-session/README.md) explain ownership,
verification and how to add activities after the first learner observations.

## Teaching and authoring

| Guide | Responsibility |
|---|---|
| [Curriculum design](specifications/curriculum.md) | Shared subjects, progression, independent entry and checks for understanding |
| [Recurring progressions](specifications/recurring-progressions.md) | Eight connected learning threads, existing-game placements, gaps and implementation priorities |
| [Data, memory and tools](specifications/experiments/data-memory-tools.md) | Asset representations, small converters, validation, storage and runtime costs |
| [Game brief](specifications/brief.md) | The experience, target, teaching, runnable stages and verification of one game |
| [Unit](specifications/unit.md) | Guided construction, local explanations, questions and publishing checks |
| [Content workflow](specifications/content-creation-workflow.md) | Research, agreement, prototyping, authoring and verification |
| [Writing voice](specifications/writing-voice.md) | Clear British English, audience and responsible historical treatment |
| [Pseudocode](specifications/pseudocode.md) | Shared explanatory notation |
| [Graphics and audio](specifications/graphics-and-audio.md) | Creating, preparing and integrating assets |
| [Audio progression](specifications/experiments/audio-progression.md) | Listening, arrangement and playback milestones placed in the four core system routes |
| [Timing and interrupts](specifications/experiments/timing-and-interrupts.md) | Clock distinctions, hardware contracts, lesson repairs and controlled timing experiments |
| [Scheduling, ownership and headroom](specifications/experiments/scheduling-ownership-headroom.md) | Sequential work, priorities, safe handoffs, bounded work and explicit overload policies |
| [Synthesis and transfer](specifications/experiments/synthesis-and-transfer.md) | Whole-action traces, graduated hints and independent variations at selected milestones |
| [Finishing and delivering](specifications/experiments/finishing-and-delivering.md) | Completion criteria, reproducible packages, handover notes and proportionate release evidence |
| [Working with existing code](specifications/experiments/working-with-existing-code.md) | Rebuild a baseline, trace behaviour, make bounded changes and verify refactors through project revisits |
| [Randomness and reproducibility](specifications/experiments/randomness-and-reproducibility.md) | Seeds, range bias, constrained choices, deterministic scenarios and bounded replay prerequisites |
| [State, lifecycle and recovery](specifications/experiments/state-lifecycle-and-recovery.md) | State lifetimes, transition responsibilities, repeated restart and proportionate failure recovery |
| [Abstraction and portability](specifications/experiments/abstraction-and-portability.md) | Routine contracts, bounded ports and machine-specific trade-offs, including a failed-abstraction exercise |
| [Timing and player feedback](specifications/experiments/timing-and-player-feedback.md) | Input, simulation, presentation and audio timing connected through controlled feedback comparisons |
| [Testing and diagnosis](specifications/experiments/testing-and-diagnosis.md) | Predictions, reproducible faults, boundaries, traces and evidence-led repairs through existing projects |
| [Profiling progression](specifications/experiments/profiling-progression.md) | Game-led measurement practice, verified tool surfaces and separate guest/host investigations |
| [Vault](specifications/vault.md) | Sourced encyclopaedic context |
| [Vault candidate backlog](vault-candidates.md) | Proposed subjects, triage and the handoff to writing issues; [structured records](vault-candidates.csv) |
| [Pattern Library](specifications/pattern-library.md) | Adaptable implementations and their contracts |

[Website and publishing](website.md) connects these specifications to the current schemas, source organisation, capture, testing and deployment. [Game-design material](platforms/README.md) lists the concrete existing designs worth consulting during re-specification.

The [Spectrum Meet BASIC specification](platforms/sinclair-zx-spectrum/basic/meet-basic.md) defines the agreed introduction through short projects and its relationship to the first substantial games.
Its [lesson and source mapping](platforms/sinclair-zx-spectrum/basic/meet-basic-plan.md) identifies reusable material, new checkpoints, verification and route migration work.

The [Spectrum BASIC course review](platforms/sinclair-zx-spectrum/basic/course-review.md) records the agreed navigation groups and recommendations for the remaining games and proposals.

The [Spectrum assembly review](platforms/sinclair-zx-spectrum/assembly/course-review.md) records the approved replacement direction, with source-build and emulator smoke evidence. The [replacement opening](platforms/sinclair-zx-spectrum/assembly/opening.md) and [accepted first game](platforms/sinclair-zx-spectrum/games/meteor-storm/brief.md) establish the route through a separate [introductory module](platforms/sinclair-zx-spectrum/assembly/meet-assembly.md) and the [published game progression](platforms/sinclair-zx-spectrum/games/meteor-storm/lesson-brief.md).

The [Craft coverage map](specifications/craft-coverage.md) defines seven agreed module homes and distinguishes available material from planned lessons. The [Maths for Games specification](specifications/maths-for-games.md) develops geometry, trigonometry, matrix algebra, 3D, curves, probability and fixed-point applications.

The [Foundations audit coverage map](audit/2026-10-foundations-coverage.md) links sampled evidence to the ten modules and records the remaining audit gaps. The [education umbrella reconciliation](audit/2026-10-education-reconciliation/REPORT.md) separates accepted technical evidence, unknown learner outcomes and the next five priorities. The [probability pilot](audit/2026-10-probability-pilot/REPORT.md) maps the eleven published maths units and checks exact counts against rounded shares. The [embedded BASIC follow-up](audit/2026-10-embedded-basic/REPORT.md) qualifies repeated reads, replacement, errors and recovery in the live browser machine. The [latency baseline](audit/2026-10-embedded-latency/REPORT.md) retains five cold/warm trials with complete-result timing boundaries. The [native Safari follow-up](audit/2026-10-first-session-operability/REPORT.md) records selected first-session operation, successful edited-tape save/reopen and the remaining screen-reader/touch gaps.

## Ownership and maintenance

The [website](https://github.com/code198x/website) owns public lessons, catalogues and components. [Code samples](https://github.com/code198x/code-samples) owns runnable sources, assets and verification recipes. Those files establish implementation state; plans and prose counts do not.

Keep one explanation for each responsibility. Update current guidance when a decision changes, remove completed working notes, and preserve superseded material in Git history. Do not keep old site mock-ups, parallel hardware summaries, sibling roadmaps or past implementation handoffs in the active documentation tree.

[PRINCIPLES.md](PRINCIPLES.md) and [MANIFESTO.md](MANIFESTO.md) are inherited family documents, maintained at family level. [AGENTS.md](AGENTS.md) contains repository working instructions; `CLAUDE.md` points to it. These have distinct roles and are not competing project charters.

The [Foundations per-unit map](audit/2026-10-foundations-objectives/MAP.md) inventories
all 39 authored units, their objectives and knowledge used. Its
[source review](audit/2026-10-foundations-objectives/REPORT.md) separates that inventory
from sampled execution and unknown learner outcomes.

The [compound-condition pilot](audit/2026-10-compound-conditions/REPORT.md) checks
Decisions unit 4’s numeric interval and grouping boundaries, with exact-rational
models, actual ROM outputs and independent learner prompts.

The [counted-loop pilot](audit/2026-10-counted-loops/REPORT.md) checks inclusive
ranges, empty bodies and output placement with exact models, fresh ROM programs
and independent learner prompts.

The [output-joining pilot](audit/2026-10-output-joining/REPORT.md) checks literal
versus calculated output, explicit spaces and Spectrum separator transfer, with
finite models, fresh ROM commands and independent learner prompts.

The [interpreter-trace pilot](audit/2026-10-interpreter-trace/REPORT.md) checks
changed starts, bounds and increments, stored BASIC records and the distinction
between source updates, machine instructions and measured time.

The [Foundations evidence queue](audit/2026-10-foundations-evidence-queue/REPORT.md)
reconciles the four earlier prompt gaps and prepares a repeated fixed-point
trial on retained state and drawing coordinates, reusing accepted evidence.

The [fixed-point state follow-up](audit/2026-10-fixed-point-state/REPORT.md) brings
the prepared retained-fraction experiment into the existing lesson, with model,
wide/narrow rendering and keyboard evidence.

The [publication readiness snapshot](audit/2026-10-publication-readiness/REPORT.md)
checks the latest five Foundations changes and first-session guide on the public
site, with remaining learner and accessibility limits stated separately.

The [aiming boundary audit](audit/2026-10-aiming-boundaries/REPORT.md) checks finite
movement, signed rounding and retained state against the maintained game-maths model.

The [full Foundations publication sweep](audit/2026-10-foundations-publication/REPORT.md)
checks all 39 units and ten overviews at wide/narrow widths, every authored answer
reveal and the collected internal links. It does not establish learner understanding.

The [Amiga opening audit](audit/2026-10-amiga-opening/REPORT.md) reviews the AMOS
and Blitz setups and first three lessons, separating maintained source/capture
consistency from unqualified runtime and learner outcomes.

The [first Amiga greetings trial](audit/2026-10-amiga-greetings/REPORT.md) records
AMOS's run/edit/error/repair loop and the incomplete AmiBlitz compilation check.
