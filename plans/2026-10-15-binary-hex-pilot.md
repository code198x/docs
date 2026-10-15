# Binary and hex conversion pilot

Continue umbrella #114/#115/#124 with Counting in Twos overview and units 1–2.
Preserve unrelated checkouts and the reviewed units 3–4. Record full current main
identities in the report; use isolated worktrees without new dependencies.

1. Read the three pages, HexByteFigure and the Spectrum BASIC manual appendix E.
   Check place values, conversion table, digit grouping, byte range and leading
   zeros. Deduplicate/file confirmed interpretation and assessment gaps.
2. Edit only the overview and units 1–2: distinguish binary digit from physical
   current, value from numeral and chosen width, and unsigned byte from every
   possible byte interpretation. Recall used arithmetic locally; add closed
   prediction questions and a worked conversion in the other direction. Preserve
   correct existing outputs and the F0 diagram; connect optional existing material.
3. Add `audit/2026-10-binary-hex-pilot/verify-conversions.py` with an audit-only Z80
   fixture. Run selected actual ROM BIN literals, then load/execute all 256 byte
   values and compare their eight bit digits and two nibble values with independent
   formatted-number oracles. Read back the loaded code and completion marker.
4. Add `scripts/verification/binary-hex-pilot.mjs` with explicit semicolons. Check
   outputs, table and diagram against independent conversions; keyboard prediction
   and optional-link/Back checks at 1440/390. Retain baseline, known-red and after
   records. Run build, repository checks, Vale/Ruff and semicolon parsing. Inspect
   desktop/narrow captures in one batch, at most one correction/confirmation pass.
5. Write report and separate learner/assessor sheets; update current coverage with
   evidence boundaries and next bounded gap. Push paired drafts, link finding and
   parent issues, verify remote/hash retention and remove temporary tooling,
   symlinks, worktrees and task processes. Do not close parents or claim learners.
