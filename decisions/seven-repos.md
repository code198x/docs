# Decision: Seven Separate Repositories

## The decision

Code198x uses 7 separate git repos, not a monorepo:

| Repo | Purpose |
|------|---------|
| `website` | Astro 6.x site |
| `code-samples` | Working code per unit |
| `docs` | Specs and curriculum |
| `commodore-64-dev` | Docker + ACME |
| `sinclair-zx-spectrum-dev` | Docker + pasmonext |
| `commodore-amiga-dev` | Docker + vasm |
| `nintendo-entertainment-system-dev` | Docker + ca65 |

## Why

Each Docker toolchain has its own CI pipeline and release cadence. The website, code samples, and docs change independently. Coupling them would mean unrelated changes triggering builds.

## Gotcha

Always check `git status` from the correct directory before committing. The `repo-status` skill checks all 7 repos at once.
