# Foundations publication readiness

The five most recently changed Foundations units are published and pass the
selected live checks. The public first-session pack remains usable for inviting
parents, teachers and learners. No product blocker was reproduced in this pass;
no additional lesson change is proposed.

This is a bounded readiness snapshot on 16 October 2026 under
[#114](https://github.com/stevehill1981/198x/issues/114),
[#115](https://github.com/stevehill1981/198x/issues/115) and
[#124](https://github.com/stevehill1981/198x/issues/124). It does not certify the
whole curriculum or establish educational effectiveness. All three parents stay open.
The [plan](../../plans/2026-10-16-publication-readiness.md) records the scope.

## Publication and scope

Approved [website #764](https://github.com/code198x/website/pull/764) and
[docs #90](https://github.com/code198x/docs/pull/90) merged by rebase. Website main
is `405c0594d30af56ecdfdc1ee4b6c119dead20ab7`; docs baseline is
`eea9f55ae490653a8d3e5baa88a75f2c7c7649a3`.
The [normal deployment](https://github.com/code198x/website/actions/runs/38882964948)
completed successfully. Its [retained result](deployment.json) identifies that
website revision. Actual browser responses and interactions below supply the
publication evidence; deployment success alone does not establish it.

We used the existing committed verification scripts against
`https://code198x.com`, with installed headless Chrome 155.0.8059.80 and
1440×900 / 390×900 CSS viewports. No package was installed or updated.
[Identities](identities.json) retain source/verifier/package-lock hashes and the
accepted fixed-point model identity. Lesson response SHA-256 values are retained
in the individual browser records. These are observed HTTP identities, not a
proof that every deployed asset matches a local build. Guide checks record HTTP
success through assertions but do not retain guide response hashes.

| Live page | Fresh result |
| --- | --- |
| [Compound conditions](https://code198x.com/foundations/decisions/unit-04/) | Numeric-domain/grouping wording, two independent predictions and optional support/Back route pass at both widths: six behaviour groups. |
| [Counted loops](https://code198x.com/foundations/repeating/unit-01/) | Inclusive whole-number range, empty-body boundary, two keyboard predictions and optional support/Back route pass: six groups. |
| [Output](https://code198x.com/foundations/basics/unit-03/) | Exact literal/arithmetic output, missing-space repair, four keyboard reveals and two support/Back journeys pass: six groups. |
| [Interpreter trace](https://code198x.com/foundations/from-source-to-silicon/unit-02/) | Original 1000 output and selected rows agree; numeric cells remain intact, predictions and support/Back pass: six groups. |
| [Fixed-point state](https://code198x.com/foundations/working-the-bits/unit-05/) | Accepted-model table and original outputs agree; separate hint, answer, variation and both support/Back routes pass: ten groups. |
| [Try Code198x](https://code198x.com/try/) and five companion pages | All twelve page/viewport cases pass layout/scoped scans; keyboard discovery reaches BASIC and assembly lessons, parent/teacher guidance, the session sheet and its print action: two groups. |

There are **ten lesson/viewport cases**, **twelve guide/viewport cases** and
**36 behaviour groups**. A group contains several assertions and is not a count
of learners or validated learning objectives. The guide run uses `pages` mode;
it does not rerun machine editing, execution, errors or tape recovery. Earlier
[native Safari evidence](../2026-10-first-session-operability/REPORT.md),
[embedded BASIC evidence](../2026-10-embedded-basic/REPORT.md) and
[latency evidence](../2026-10-embedded-latency/REPORT.md) retain their own scope.

## Readability and access observations

No document overflow, page errors or scoped axe violations were observed in
these runs. The four-line narrow compound-condition contrast uncertainty and
one-line narrow fixed-point uncertainty remain explicit in the raw records.
Fresh probes of the actual code colours at horizontal scroll endpoints measure
at least **16.8168:1** across ten samples. Those probes qualify those text/background
pairs; they do not resolve every accessibility requirement. Other selected
lesson scans and the guide scans report no incomplete results.

We visually inspected selected retained narrow answer captures for compound
conditions, loops and output, the narrow interpreter table, the public guide
and the fixed-point table. This is a focused publication inspection, not a
new whole-site design review. The shared table fix keeps numbers such as 1000
on one line. Native screen readers, physical touch and audio were not exercised.

## Remaining work

The [current open issue snapshot](open-findings.json) has one website follow-up:
[website #749](https://github.com/code198x/website/issues/749), broader first-session
operability. Its Safari route has earlier evidence; VoiceOver remains skipped
at the user's request, and physical touch remains untested. Those are limits,
not newly reproduced product defects. We keep #749 open and do not claim
cross-platform accessibility from viewport checks or scanner results.

No learner is available yet. Understanding, retention, unaided transfer and
usefulness to a parent or teacher remain unobserved. The public
[guide pack](https://code198x.com/try/) and existing
[observation sheet](../../guides/first-session/session-observations.md) are ready
for the first trial. That is the next evidence that can establish whether the
technical/editorial improvements help learners. The pack needs no further
expansion before that trial.

The docs snapshot also contains separate discovery and future-machine work.
Those issues do not establish blockers in this sampled Foundations release.
The [objective map](../2026-10-foundations-objectives/MAP.md) and
[coverage map](../2026-10-foundations-coverage.md) remain the source of scope and
known gaps; this check adds no new full-body review, native execution or proof
of every example. Prefer a reproduced failure or a learner observation over
another exercise added to keep the audit moving.

## Retained checks

[Run results](runs.json) preserve commands, exit codes and console output for
seven successful verifier invocations. The browser JSON and captures stay in
the corresponding lesson/guide folders. The fixed-point browser verifier was
also run against a deliberately incorrect accepted table: it failed on the live
rendered values, retaining its [failed record](known-red/browser.json) and
[nonzero rejection](known-red/rejection.json). This is a harness control,
not a failure in the published lesson.

Run `python3 audit/2026-10-publication-readiness/verify.py --website PATH`
from the docs repository to check source/input identities, positive coverage,
rendered model rows, bounded probes, deployment identity and manifest hashes.
The verifier also rejects a record with one viewport removed.
[Validation](validation.json) and [SHA256SUMS](SHA256SUMS) retain the result
and evidence integrity. We did not repeat the production build or 237 repository
tests here; their successful pre-merge results remain in the
[accepted fixed-point report](../2026-10-fixed-point-state/REPORT.md).
