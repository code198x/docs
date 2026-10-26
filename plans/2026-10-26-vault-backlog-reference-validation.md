# Repair Vault backlog reference validation

## Cause and agreed scope

`--website` assumes every Vault page is `src/content/vault/<category>/<slug>.mdx`. The published SimCity study instead has a concrete Astro route at `src/pages/vault/studies/simcity/index.astro`. The checker stops at the first error, hiding two incorrect hardware references and intentionally planned referring pages.

The owner approved using `candidate:VC-...` in `link_from` for planned sources. Keep the current CSV columns. These are candidate relationships, not reserved URLs or evidence of publication. Existing-page references and `covered_by` remain strict.

## Work and verification

1. Reproduce the current CLI failure against a clean current-main website checkout; enumerate all missing source paths. Inspect the actual study route and candidate records before changing anything.
2. Update `scripts/check_vault_candidates.py` to recognise concrete study route files, validate planned source IDs against the complete backlog, reject unknown/self references and reject candidate references in `covered_by`. Never accept an arbitrary missing page or a generic dynamic route as proof of existence.
3. Add regressions in `scripts/test_vault_candidates.py` for the real study-route shape, forward candidate references, unknown IDs, missing pages and sources hidden by filters. Run new cases against the old checker first to prove the reproduction.
4. Update `vault-candidates.csv`: retain every record, status and reason; replace only positively identified planned sources with their existing stable IDs and correct `hardware/sid` to the verified `hardware/sid-chip`. Preserve intended future-link locations in notes. Document the syntax in `vault-candidates.md`.
5. Run all regression tests, schema validation and the full `--website` check; check filtered validation still rejects invalid records. Confirm the record count and all identities/statuses are unchanged. No site build is needed because no website content or implementation changes.
6. Commit and push the fix, open a PR with the cause and verification evidence, and clean both temporary worktrees after confirming retained commits. Preserve unrelated original-checkout work.

## Audited references

- `studies/simcity`: 20 references; actual static study route exists.
- `hardware/pokey`: VC-2909; planned chip entry already has candidate VC-0152.
- `hardware/sid`: VC-2909; existing canonical entry is `hardware/sid-chip`.
- `culture/women-in-computing`: 12 references; notes and writing issues explicitly describe a commissioned, unwritten theme. Reuse its existing candidate VC-2826.
- `culture/the-terminator`: VC-2841; notes explicitly identify the proposed film entry. Reuse VC-2833.

## Verification results

- Reproduced the original failure verbatim: `FAIL: VC-0493: missing link_from entry: studies/simcity`.
- The new regression cases failed against the original checker: the 17-test run reported four failures and two errors. After implementation and two further strictness cases, all 19 tests pass.
- The full website-backed checker now passes all 2,941 records. A filtered people/needs-triage run still validates the whole input before displaying its three requested results.
- Confirmed the live SimCity study returns 200 with a SimCity heading; its actual source is `src/pages/vault/studies/simcity/index.astro`. The backlog's 20 SimCity references remain intact.
- Independently compared old and new CSV records: count, order, IDs, subjects, categories, statuses, reasons, covered paths and issue URLs are identical. Fourteen records change only referring-source values and contextual notes. All fourteen planned references resolve to existing candidate identities; the old proposed paths remain in notes. The SID correction points to a checked existing file.
- `ruff check`, `ruff format --check` and `git diff --check` pass. Initial naming/formatting diagnostics were corrected; no lint rules or checks were disabled.
- No website source, rendered content, dependencies or CSV columns changed. No site build is claimed or needed for the validator-only change.
