# Amiga opening claims (#767)

Approved scope: both module introductions and units 1–3, following the qualified first greetings. Preserve sample behaviour and independent language entry points.

1. Read the eight MDX pages under `src/content/curriculum/commodore-amiga/{amos/meet-amos,blitz/meet-blitz}/` and primary AMOS/Blitz references. Retain exact old claims and locators in `audit/2026-10-amiga-claims/REPORT.md`.
2. Move the unit-2 VWait before BLITZ in the maintained sample and matching capture typing payload: the primary manual requires the disk-settling wait before disabling the OS. Keep its rendered result unchanged. Correct unsupported performance, numeric-safety and universal OS claims in those pages. Carry the qualified PED import/compile controls into Blitz units 2–3. Verify each changed claim against its source; avoid timing claims without benchmarks.
3. Attempt selected numeric and graphics runtime checks on the named FS-UAE/AmiBlitz configuration using already authorised tools/media. Bound attempts; record failures/skips honestly. Do not add dependencies.
4. Build the website, inspect changed rendered routes at desktop/phone widths where browser access permits, and check source inclusion and internal links. Retain results and limits in the report.
5. Commit and push separate website/docs changes, open paired review PRs and update #767/#116. Preserve unrelated main-checkout changes. Remove disposable worktrees/caches/processes once their commits are verified on remote refs.
