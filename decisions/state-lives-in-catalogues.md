# Decision: Project state lives in the catalogues and git, not in prose

> **STATUS: Accepted 2026-06-08.** What is shipped / in-progress / planned is read from
> the website module **catalogues** (`website/src/content/modules/<platform>/<track>.yaml`
> `status:` fields), the per-module `units.yaml`, the unit MDX / `.bas` files, and git
> history — never from a hand-maintained prose status doc. Planning prose is history and
> intent, not a live status claim.

## Why

Hand-maintained status mirrors rot. A second copy of "what's done" is only ever as fresh
as the last manual sync, and a *wrong* status doc is worse than none — it actively
misleads. On 2026-06-08 three separate prose sources each asserted work was pending that
had in fact shipped: the (now deleted) `tracker/revamp.md` status tables, the
`**Status:**` lines on game briefs (all reading "draft" on shipped games), and a stale
"Starfield awaiting DoD pass" note in the C64 assembly skeleton. State is data; it belongs
where it is queried, not retyped into prose.

## The rule

- **Authoritative for state:** `modules/*.yaml` `status:` + `units.yaml` + the shipped
  files + git log. Query these to answer "is X done?"
- **Prose carries what can't be derived:** decisions (the *why*), reference (hardware /
  language facts), briefs (design intent), and `log.md` (timestamped history — true at its
  date, not a live claim).
- **Don't reintroduce a status-mirror layer.** No `Status:` lines in briefs, no per-game
  status tables in trackers, no "awaiting pass" notes for shipped work. If a one-page
  status view is ever wanted, *generate* it from the catalogues — don't hand-keep it.

## Done 2026-06-08

- Deleted `tracker/revamp.md` — its durable content (governing principle, cut hierarchy,
  Definition of Done, locked decisions) already lives in `decisions/`
  (`curriculum-structure`, `october-2026-launch-spec`, `commercial-bar-revamp`).
- Stripped `**Status:**` lines from all 26 game briefs.
- Removed the stale DoD-pass note from `platforms/commodore-64/assembly-skeleton.md`.
- This record + a banner in `index.md` declare the source of truth.
