# Bits and shifts pilot

Fifth bounded slice for umbrella #114, #115 and #124, authorised after the numbers
pilot. Limit public edits to Foundations Working the Bits units 1–2 and a bounded
browser verifier. No learner is available; do not claim educational validation.

Baselines: website 1a419f5806eb73e522dc4ccd8628824c2ff76e5c; docs
e053dc3082864d130ded437a39f1fc6e967db753. Preserve unrelated checkout work by
using isolated worktrees, copied existing packages and the pinned UI kit.

1. Read `src/content/curriculum/foundations/working-the-bits/unit-01.mdx` and
   `unit-02.mdx`, the pseudocode contract, relevant BASIC conditions and assembly
   byte/pixels material. Source-check masks, unary complement, logical versus
   arithmetic right shifts, carry and speed claims against Zilog UM008011-0816
   instruction entries and Spectrum manual Conditions. Deduplicate finding issues.
2. Prepare `audit/2026-10-bits-shifts-pilot/verify-bits.py` and a small native audit
   fixture. Check actual ROM BASIC AND/OR/NOT semantics separately from Z80 masks;
   assemble/load actual Z80 AND/OR/XOR/CPL, SLA/SRL/SRA and ADD cases. Assert
   unaffected bits and XOR reversal, shift boundaries and carry; derive expected
   results independently. Timing statements are manual evidence unless measured.
3. Correct confirmed errors only: bit-logic operand count and complement example;
   explicit eight-bit unsigned zero-fill shifts; bounded multiply/divide claims;
   processor-dependent speed. Add closed predictions and an optional existing
   byte/pixels connection without requiring BASIC or assembly attendance.
4. Create REPORT, LEARNER-TASKS and ASSESSOR under that audit folder: prerequisite
   map, prediction/explanation/modification/diagnosis/creation, separate answers,
   configuration identities and pending learner outcomes. Do not introduce public
   runnable samples outside code-samples; the native fixture is audit tooling.
5. Add `scripts/verification/bits-shifts-pilot.mjs`. Capture unchanged live pages;
   confirm the corrected-state verifier rejects each old page. Build production,
   run repository checks, verify both revised pages at 1440×900 and 390×900 with
   scoped axe, keyboard prediction, optional link and browser Back. Reuse the
   maintained live byte/pixels verifier for the linked execution surface.
6. Push focused paired draft PRs, link confirmed findings and parent issues,
   retain evidence hashes and clean up after verifying remote commit retention.

No dependencies, shared layouts, language interpreter, floating/fixed-point lesson
rewrite or original-hardware qualification. Keep up to five prioritised findings;
report source, execution, automated UI and learner evidence separately.
