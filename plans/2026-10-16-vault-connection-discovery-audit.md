# Vault connection and reading-path audit

Audit the existing Vault at the current website main revision before proposing new discovery work. This task records gaps; it does not redesign the interface or publish content.

1. Inspect current Vault specifications, discovery components, article templates, backlink indexing, existing issue outcomes and candidate tracking. Preserve unrelated repository work.
2. Inventory authored article-to-article links across every Vault entry, distinguishing article-body links from citations and runtime navigation. Inspect representative music, people, wartime and regional-history journeys; do not equate an asymmetric link with a defect or an absent article with a missing backlink.
3. Inspect the live homepage, category and article discovery surfaces at desktop and phone widths. Check representative links and search outcomes. Record the deployment evidence separately from the source revision, since a source tree does not prove a deployment.
4. Run the existing link checker and focused discovery tests, including their failure cases. Use the scoped Impeccable diagnostic scan as supplementary evidence; unrelated styling findings are outside this task.
5. Record a bounded evidence report in `audit/`, then reuse existing issues where applicable and create appropriately scoped, linked tasks for verified cross-link/discovery gaps and editorial reading paths. Keep candidate-only subjects and existing biography/theme work out of duplicate commissions.
6. Read created/updated issues back, commit and push the report/plan to the existing tracking pull request, and remove temporary worktrees, downloads and task-owned browser processes after confirming the commit exists on the remote.

## Execution

The report is `audit/2026-10-16-vault-connections.md`. The source inventory covered 1,485 entries; the live browser checked eight routes at both widths and five title queries per width. Link validation and all eight discovery tests passed. The supplementary detector returned no findings.

Created website tracker #796 with native children #797 (editorial repairs), #798 (two initial paths) and #799 (incoming suggestions, explicitly an undecided idea). Reused #781 for the women's theme and added a reciprocal discovery-tracker reference. Read issue state, bodies and native relationships back. No article, category or interface was changed.
