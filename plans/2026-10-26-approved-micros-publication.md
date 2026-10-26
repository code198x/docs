# Publish the approved early British micros

Owner approved the MK14, Grundy NewBrain and Acorn Atom entries on 26 October 2026.

1. Set `reviewed: true` in the three `src/content/vault/systems/` entries in website PR #1233; retain AI provenance. Verify the exact diff and content checks, then commit and push.
2. Complete required PR checks and merge by rebase. Verify all three production pages, photographs, incoming links and sitemap inclusion.
3. Update VC-0003, VC-0004 and VC-0005 in `vault-candidates.csv` to published only after live verification. Validate the whole backlog against the website and run the checker regressions. Merge docs PR #265 by rebase and close the writing issues.
4. Remove temporary worktrees after checking clean files and retained remote commits.
