# Publish the approved early British micros

Owner approved the MK14, Grundy NewBrain and Acorn Atom entries on 26 October 2026.

1. Set `reviewed: true` in the three `src/content/vault/systems/` entries in website PR #1233; retain AI provenance. Verify the exact diff and content checks, then commit and push.
2. Complete required PR checks and merge by rebase. Verify all three production pages, photographs, incoming links and sitemap inclusion.
3. Update VC-0003, VC-0004 and VC-0005 in `vault-candidates.csv` to published only after live verification. Validate the whole backlog against the website and run the checker regressions. Merge docs PR #265 by rebase and close the writing issues.
4. Remove temporary worktrees after checking clean files and retained remote commits.

## Verified publication

Website PR #1233 merged by rebase; deployment succeeded. Fresh checks pass: 230 unit tests, accepted type baseline, content/imagery/links, prepared assembler/player checks and a 2,788-page production build. Required GitHub checks pass, including 252 production browser tests and 1,371 development browser tests (25 skipped).

At 390px and 1440px, all three approved articles show reviewed status, decode their photographs and have no horizontal overflow. Production checks confirm reviewed/indexable pages, all three photograph checksums, ten required incoming links and sitemap inclusion.

VC-0003–VC-0005 are published with their stable IDs, article paths, source notes and issue links retained. The merged backlog checker validates the combined 2,943 records; all 19 regression tests pass. The earlier backlog reference corrections remain intact.
