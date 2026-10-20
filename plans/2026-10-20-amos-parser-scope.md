# AMOS parser scope and release research

Research and proposal only. Cover the AMOS family and release differences;
consider Blitz afterwards. Do not implement a parser or choose a tool owner.

1. Inventory every maintained AMOS source at a pinned samples revision; separate
   the new Bank or Risk stages from older meet-amos material. Record hashes,
   command candidates, expression/control syntax and embedded languages without
   calling a textual inventory a syntax check.
2. Consult original Creator, Easy, Professional and compiler manuals, published
   source and update notes. Record edition/release evidence, unknowns and
   representative compatibility probes with precise source locations.
3. Draft `platforms/commodore-amiga/amos/parser-scope.md`: plain-text boundary,
   version/extension profiles, staged delivery and acceptance criteria. Keep
   tokenised files, AMAL and Interface distinct, with later Blitz investigation.
4. Retain a reproducible inventory under `audit/2026-10-amos-parser-scope/`.
   Check determinism, non-empty counts, source hashes, links, JSON and prose.
5. Commit, push and open a proposal PR. Verify remote retention and remove both
   temporary worktrees. Preserve unrelated dirty work in the main checkout.

Task worktrees: `/private/tmp/198x-amos-parser-scope` (docs) and
`/private/tmp/198x-amos-parser-samples` (read-only samples). No dependencies,
new repositories, emulator sessions or public lesson changes are needed.

## Outcome

The proposal covers original AMOS product lines, release and component identity,
supplied/third-party extensions, later branches and the method for Blitz and
other languages. The initial release ledger is explicitly incomplete.

The pinned text inventory covers 62 files (45 Bank or Risk, 17 meet-amos).
Source hashes and deterministic regeneration pass; changed-record and empty
selection controls fail as intended. JSON, links, privacy, Python lint/format and
prose checks pass. Proper-name “Easy” suggestions are retained as false positives.
No language parser, release-compatibility execution or new dependency was added.
