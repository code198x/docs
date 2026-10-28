# Record approved Vault publication

The owner approved all batches on 28 October 2026. The five pending batches cover 88 entries; prior attached batches are already merged.

- Match the website's five manifests to retained candidate IDs/issues, without touching unrelated records.
- Keep candidate states in-progress until all 88 live reviewed pages, imagery, canonical routes, links and sitemap are positively verified after deployment.
- Save the exact published paths, source hashes, deployment revision and live results in `audit/2026-10-28-approved-vault-release/`; then mark those rows published and resolve planned referring IDs for published sources.
- Run whole-backlog website-aware validation and all checker regression tests; commit/push the evidence and merge docs PRs #275 through #271 in dependency order.
- Update canonical writing issues only from verified publication. Preserve unrelated checkouts and clean temporary workspaces after verifying remote retention.

GitHub requires its asynchronous API for stacked reviews. Both repositories allow rebase merges only. Use the top PR to merge the full approved chain with an expected head SHA and normal rules; no force pushes or rule bypasses. The website must await its required Browser tests gate. The earlier top-to-bottom folding plan is superseded by this supported native stack operation.
