# Embedded BASIC stored-value qualification

After approved docs #80 merge, address website #747. Keep original docs
README/work and website review files intact. Use isolated docs and website
worktrees. No dependencies or product changes unless a defect is reproduced.

1. Read retained supplemental failure, current lesson, listing/machine/runner and
   existing browser checks. Establish whether the discarded harness survives;
   distinguish an exact reproduction from a reconstructed observation failure.
2. Add `scripts/verification/embedded-basic-values.mjs` in the website worktree.
   Exercise the live maintained unit 2 editor and real bundled-ROM machine with
   ONE/ONE/TWO, immediate wrong m$ command and repair, rerun, machine restart,
   source reset and original greeting. Use observable machine text and canvas
   evidence rather than startup status or a fixed sleep as the completion signal.
3. Capture an early empty/incomplete observation if reproducible and require
   full nonempty expected rows before success. Retain negative controls, exact
   browser/viewport/base URL, source/response asset identities, screenshots and
   failures in `audit/2026-10-embedded-basic/`. No fabricated historical cause.
4. Run bounded desktop browser checks, inspect screenshots and validate evidence.
   Verify explicit JS semicolons, syntax and affected checks. Do not claim mobile,
   assistive technology, latency, learner effectiveness or every browser works.
5. Push website verifier and docs evidence as reviewable draft PRs; update #747
   and parents without closing the umbrellas. Verify remote refs, stop task-owned
   browser/server processes and remove only inspected finished task worktrees.
