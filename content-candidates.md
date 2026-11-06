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

## Blocked work

When work can't be done because a family tool can't do something yet, the item stays in its queue as `blocked`, and `blocked_by` names an issue in that tool's own repository. The Vault backlog works the same way. The factory doesn't change the tools: the tool's own session fixes it, under its own decisions and review.

The tool issue states the symptom, not a guessed cause. It gives a repeatable case, such as the production's script or the listing with its expected result, and lists the items waiting on it. Before opening one, search the tool's open and closed issues and reuse a match; several items can share an issue. A machine or CPU no tool supports yet follows the umbrella workflow for adding one, and names the support surface it needs.

`scripts/tool_demand.py` reads both queues:

```sh
python3.13 scripts/tool_demand.py --website ../website   # tool issues, most blocking first
python3.13 scripts/tool_demand.py --check-issues         # every blocker is a real issue on GitHub
python3.13 scripts/tool_demand.py --unblock              # dry run; add --apply to write
python3.13 scripts/tool_demand.py --block CC-0001 --by https://github.com/emu198x/emu198x/issues/123 --note "Still drops a frame on the 128K."
```

The report ranks tool issues by how many items each one blocks, then by the Vault demand behind those items. It is the list to hand a tool's session.

`--unblock` asks GitHub about each blocker. An item whose issue closed as completed goes back to `in-progress` if it has a work issue, or `ready` if not, with a dated note saying its gates must run again. An issue closed as not planned or as a duplicate leaves its items blocked and is reported: they need a decision or the surviving issue. The script doesn't check that the fix has been released, so run the gates against the released tool. If they still fail, `--block` puts the item back with a note saying what failed.

`--check-issues` fails if a blocker names a missing issue or a pull request. The Queues workflow runs it on every pull request.
