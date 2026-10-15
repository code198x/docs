# Character codes pilot

Seventh bounded curriculum slice for umbrella #114/#115/#124, authorised after
merging the decimal-conversion investigation. No learner is available; keep
educational outcomes pending. Preserve independent BASIC and assembly entry.

Baselines: website 0a43c77f0a7493565d386bff43bac9e8e3694ef0; docs 7585b3bec20b89679b46f24e3893225f700b2cb1.
Use isolated worktrees and copies of existing installed tooling/UI kit; preserve
unrelated work. No dependency, shared-layout change or new interpreter.

1. Inspect Working the Bits unit 3, the shared CODE/CHARACTER notation, Spectrum
   BASIC chapter 14 and its character table. Check encoding assumptions, single
   digit versus whole string, numeric conversion validity and ASCII case masks.
   Inspect existing cross-machine explanations without qualifying an unrun system.
   Deduplicate and file confirmed findings in the owning website repository.
2. Add `audit/2026-10-character-codes-pilot/verify-characters.py` and an audit-only
   Z80 fixture. Execute actual ROM CODE/CHR$ and digit/whole-string observations;
   test actual OR/AND ASCII case masks at A/Z/a/z, digit and punctuation boundaries.
   Assert range validation and unaffected bits independently. Record tool/ROM/source
   identities and distinguish character codes from numeric values and glyphs.
3. Correct only `src/content/curriculum/foundations/working-the-bits/unit-03.mdx`:
   explicit ASCII convention, one-digit validation, bounded case conversion and
   accurate non-letter behaviour. Add closed predictions and an optional existing
   BASIC string connection and existing Vault PETSCII-chart comparison without
   making prior attendance mandatory. The C64 comparison is source-checked, not
   execution-qualified in this Spectrum slice.
4. Prepare REPORT, LEARNER-TASKS and ASSESSOR in the audit folder. Cover prediction,
   explanation, modification, diagnosis and creation; keep answers separate and
   record all unknown/failed/skipped outcomes without invented learner evidence.
5. Add `scripts/verification/character-codes-pilot.mjs`: live baseline, a verifier
   that rejects the old claim, production build and repository checks, then the
   proposed page at 1440×900 and 390×900. Check keyboard disclosures, optional link
   and Back, overflow and scoped axe; inspect actual rendered captures.
6. Push focused paired draft PRs, update findings and parent issues, verify remote
   retention/evidence hashes and clean task processes, worktrees and copied builds.

No Unicode survey, new system on-ramp, full keyboard browser execution retrofit
or unrelated editorial rewrite. The ROM investigation is already merged/resolved;
use observed results and original-source encoding contracts rather than generalising
from a machine's advertised character-set name.
