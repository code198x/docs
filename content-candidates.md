# Content candidate queue

Work the content factory has found for surfaces other than the Vault: patterns, From the Metal articles, system profiles, productions (games, demos and tools), progressions and tracks. Vault entries keep their own queue, the [Vault candidate backlog](vault-candidates.md). The [content factory plan](plans/2026-11-06-content-factory.md) explains how the two fit together.

The records are in [content-candidates.csv](content-candidates.csv). A candidate earns work by helping a reader of something that already exists, as in the Vault backlog. Recording a candidate is not a commitment to make it: productions and tracks still need an agreed brief.

## Columns

| Column | Meaning |
|---|---|
| `id` | `CC-0001` onwards. Never reused. |
| `surface` | `from-the-metal`, `pattern`, `system-profile`, `production`, `progression` or `track`. |
| `subject` | What the work is about, unique on its surface. |
| `system` | The website's system slug. Required for a system profile, production or track. |
| `models` | Semicolon-separated model slugs a production must run on, once its brief names them. |
| `why` | What the work offers a reader. |
| `from` | Semicolon-separated sources of the demand: a Vault candidate (`VC-0123`), another content candidate (`CC-0004`), a file in this repository (`docs:specifications/recurring-progressions.md`) or in the website (`website:src/content/curriculum/...`). |
| `status` | `needs-triage`, `ready`, `in-progress`, `blocked`, `covered`, `published` or `deferred`. |
| `triage_notes` | Required once a candidate leaves `needs-triage`. |
| `covered_by` | Semicolon-separated website `src/` paths, required for `covered` and `published`. |
| `issue` | The work's issue in code198x/website, docs or code-samples. Required for `in-progress`; not allowed before triage. |
| `blocked_by` | For `blocked` only: the issue in a family tool repository the work waits on. Several candidates can share one. |

## Validate

Run from this repository with Python 3.13 or later:

```sh
python3.13 scripts/check_content_candidates.py
python3.13 scripts/check_content_candidates.py --website ../website --surface production
PYTHONDONTWRITEBYTECODE=1 python3.13 -m unittest discover -s scripts -p 'test_*.py'
```

The checker reads the Vault backlog too, so every `VC-` reference must name a real Vault candidate. With `--website`, it also checks systems and paths. The Queues workflow runs both queues' checkers and all the tests on every pull request.
