# Compound conditions and numeric domains

After approved website #753/docs #84 merge, continue umbrella #114 with
Foundations Decisions unit 4. Preserve independent system entry and current
architecture; no dependencies or whole-course rewrite.

1. Read unit 4, current pseudocode rules, earlier Boolean/state evidence and the
   linked Meet BASIC range check. Pin source/tool identities. Establish whether
   intervals, numeric input and whole-number validity are distinguished before
   changing wording. Search existing issues before filing concrete findings.
2. Retain a bounded exact-rational model in
   `audit/2026-10-compound-conditions/verify-conditions.py`: inclusive endpoints,
   fractions inside/outside, wrong AND/OR, NOT/equivalence and grouped shooting
   guards. Reject empty case sets and deliberate wrong variants. This model is
   not execution of a shared pseudocode language.
3. Adapt the existing ROM-backed audit driver for actual Sinclair BASIC checks
   of the selected expressions and grouping. Record machine/tool/ROM/fixture
   identities and actual output; no result injection, missing transcript cannot
   pass. Keep numeric expression acceptance separate from typed-input parsing.
4. If a source gap is confirmed, file a bounded finding and correct only website
   `src/content/curriculum/foundations/decisions/unit-04.mdx`. State the local
   numeric domain, distinguish interval from whole-number validation and add a
   useful prediction/repair explanation. Link existing optional machine teaching.
5. Prepare independent learner prompts and assessor notes. No learner is available;
   record effectiveness unknown. Retain source/native/model/browser outcomes and
   failures separately in `REPORT.md`, update coverage/README and per-unit map by
   linking the new evidence without rewriting its baseline snapshot.
6. Reuse installed assets in the isolated website checkout. Run required build/
   repository checks and affected-page desktop/narrow checks with existing tools.
   Use explicit semicolons in verification JS. Verify known-red controls, exact
   results, links, prose and hashes. Push draft PRs, update #114, verify remote
   retention and clean all task worktrees, processes and disposable assets.
