# Foundations: full publication and navigation sweep

All **39 authored Foundations units and ten module overviews** pass this bounded
live-publication check at desktop and narrow widths. All authored answer reveals
work in the tested keyboard activation path, and every collected root-relative
or same-page link resolves. No product blocker was reproduced; no website
change is proposed.

This continues [#114](https://github.com/stevehill1981/198x/issues/114) and
[#124](https://github.com/stevehill1981/198x/issues/124), following the approved
[aiming evidence](https://github.com/code198x/docs/pull/92) and
[sample status correction](https://github.com/code198x/code-samples/pull/95).
The [plan](../../plans/2026-10-16-foundations-publication-sweep.md) bounds the work.
The earlier [five-unit readiness pass](../2026-10-publication-readiness/REPORT.md)
retains its separate checks of exact outputs, tables and the public guide pack.

## Source and environment

[Source inventory](source.json) identifies exactly 49 MDX files at website
`405c0594d30af56ecdfdc1ee4b6c119dead20ab7`, with each path, route and SHA-256.
We checked the shared Question component and inventoried both its usages and raw
HTML disclosures. There are **18 Question components and 34 raw disclosures**,
52 authored answer reveals in total. Each of the 39 units has at least one;
that presence is a delivery expectation, not a teaching quota or quality score.

The run used installed headless Chrome **155.0.8059.80**, Node **24.22.0**, and
1440×900 / 390×900 CSS viewports against `https://code198x.com` on 16 October 2026.
No dependency was installed or updated. [Results](live/results.json) retain each
response hash, final URL, HTTP status, viewport, dimensions and opened answers.
The inventory fixes the source expectations; these HTTP identities do not prove
byte-for-byte equivalence between every deployed page and a local build.

## Fresh results

| Check | Outcome | Boundary |
| --- | --- | --- |
| Published page matrix | 98 successful page/viewport cases: all 49 routes at both widths | Successful HTTP, one visible page heading and non-empty main content; not a full prose comparison |
| Question components | Exact source-derived counts on all pages | Counts alone do not validate the question or explanation |
| Authored answer reveals | 104 opens: all 52 at each width | Each closed answer's summary receives focus, then Enter opens non-empty content; not a complete sequential Tab-order audit |
| Document width | No horizontal document overflow in the final revealed state | Individual code/table scrollers and visual quality are not fully audited here |
| Page errors | No uncaught page errors observed | Not an assertion about every resource request or every control state |
| Main-region links | 385 distinct collected URL/fragment combinations pass | Root-relative and same-page links observed on these pages; external and other relative URL forms are outside this check |
| Target requests | 112 distinct requested URLs return successful final responses | Requests follow redirects, including ordinary trailing-slash redirects; these are not 112 distinct curriculum pages |
| Fragment destinations | All 274 HTML fragment references identify an ID or named anchor | Target HTML inspected, not every target page exercised interactively |

The verifier fetches each target body once and checks its referenced fragments.
Raw results retain each link's source pages, requested/final URL, response hash,
status and fragment outcome. Positive route, viewport, disclosure and link counts
must pass; an empty link set cannot become a green result.

## Failed attempt and controls

The first attempt stopped at From Source to Silicon unit 3 with
`Missing/ambiguous authored disclosure: Follow the compiler's output`.
[The retained failed run](initial-run.json) and
[record](initial-typography-mismatch/results.json) are separate from the final pass.
Direct inspection found `Follow the compiler’s output` in the actual page: the
publishing typography uses a curly apostrophe. We normalise straight/curly quote
forms and whitespace for label matching; all words still have to match uniquely.
[The inspected labels](typography-inspection.json) retain the observation.
This was a verifier mismatch, not a missing explanation.

A separate run deliberately expects a Question on the Basics overview where the
source expects none. The real page is rejected with nonzero exit:
[control output](known-red-run.json), [failed record](known-red/results.json).
The evidence validator also rejects a missing route/viewport case and a missing
answer-open record. No product failure is inferred from those controls.

## What remains

The current sampled technical, source and publication evidence is ready for
review. The [coverage map](../2026-10-foundations-coverage.md) and
[per-unit objective map](../2026-10-foundations-objectives/MAP.md) retain the
conceptual scope and limitations. Neither this sweep nor earlier selected
execution runs establish that every objective is correct or every example has
been executed across machines.

Actual learner understanding, retention and unaided transfer remain unknown;
no learner is available yet. The [public guide](https://code198x.com/try/) and
[observation sheet](../../guides/first-session/session-observations.md) remain
ready for a trial. Keep #114/#115/#124 open. This pass adds no contrast/axe,
screen-reader, physical-touch, audio, native-execution or latency qualification.
The prior [Safari report](../2026-10-first-session-operability/REPORT.md) and
[website #749](https://github.com/code198x/website/issues/749) retain the explicit
VoiceOver skip and untested touch scope.

No new issue was filed because no product discrepancy was reproduced. The old
reconciliation's probability, embedded-BASIC and latency follow-ups have already
been delivered; do not reopen them from that dated queue. Prioritise an observed
failure or learner friction before extending the public exercises or guide pack.
Continue independent source/technical work when a specific unqualified claim
provides a useful next question.

## Reproduction

Run `node audit/2026-10-foundations-publication/verify-live.mjs WEBSITE_PATH SOURCE_JSON OUTPUT_DIRECTORY`.
The website checkout supplies its existing Playwright dependency; the script
always checks the public origin. Optional final argument `wrong-count` runs the
intentional failing expectation. The [run record](run.json) preserves command,
exit status and output. The failed count run is not included in successful totals.

Run `python3 audit/2026-10-foundations-publication/verify-evidence.py --website WEBSITE_PATH`
for immutable source identities, complete matrix/disclosure/link coverage,
negative controls, local report links and manifest hashes.
[Validation](validation.json) and [SHA256SUMS](SHA256SUMS) retain the outcome.
No production build or repository test suite was rerun for this evidence-only
change; the approved lesson builds/tests retain their earlier named scope.
