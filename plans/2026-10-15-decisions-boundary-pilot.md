# Decisions and boundaries pilot

Second bounded slice for umbrella #114, #115 and #124, following the approved
stored-value pilot. Objective: predict which instructions run for below/equal/
above cases, distinguish comparison from assignment, and diagnose a reversed
branch without breaking the zero boundary. BASIC and assembly remain independent
entry routes. No learner is currently available; prepare prompts and keep actual
learner validation pending.

## Baselines and scope

Website baseline: `f219ace5077ce72dedf60f601b30f4581f8b7a31`.
Documentation baseline: `e5864c3fb7224f4b2f8bf6acf3d39f604bd3c725`.
Use isolated linked worktrees to preserve concurrent changes in the normal
checkouts. Record the current samples revision, configured native ROM fingerprint
and actual tool/browser versions with the evidence. Do not use a catalogue's
complete status as proof of understanding.

## Tasks and verification

1. Inspect Foundations `decisions/unit-01.mdx` and relevant earlier input and
   arithmetic pages; compare BASIC
   `meet-basic/unit-05-give-a-useful-clue.mdx` and assembly
   `meet-assembly/unit-08.mdx`. Record prerequisite knowledge, local explanation
   and optional connections in `audit/2026-10-decisions-boundary-pilot/REPORT.md`.
2. Check open and closed issues before filing confirmed conceptual or runnable
   defects in the owning repository. Include exact passages, counterexamples,
   baseline identity, bounded acceptance and umbrella links. Keep untested learner
   impact explicitly hypothetical.
3. Reuse the Lucky Number native verification recipes for comparison examples
   and the maintained live `scripts/verification/guided-debugger.mjs` for actual
   flags, branch, repair and zero-boundary behaviour. Record actual observations
   and failures separately. Do not call PasmoNext upstream Pasmo.
4. Correct only confirmed misconceptions in Foundations' choice lesson, keeping
   examples and explanation consistent. Use existing native disclosure for a
   short prediction task if needed. No new interaction framework or dependency.
5. Prepare separate learner prompts and assessor notes for predict/explain/
   modify/debug/create tasks. Do not require prior BASIC for assembly or prior
   Foundations for either route. Preserve authentic language differences.
6. Build the isolated website, inspect the affected lesson at narrow/wide widths,
   check keyboard reveal, output and overflow, and run appropriate content checks.
   Capture baseline and proposed-result evidence. Separate automated checks,
   technical execution, expert judgement and learner outcomes.
7. Push focused task commits and draft PRs for the correction and evidence pack.
   Link findings and limits from #114/#115/#124. Do not merge or publish the new
   editorial batch until reviewed. Remove temporary worktrees and task-owned
   outputs after verifying their commits on remote refs; preserve durable evidence.

The first pilot's supplemental BASIC browser assertion remains failed harness
evidence. This slice uses the established native BASIC route rather than expanding
that custom harness. Physical mobile, other hosts, screen readers and original
hardware remain unverified unless explicitly exercised and recorded.
