# Decision: System-rooted URLs with an explicit track segment

## The decision

Canonical URL pattern — system at the root, **track always explicit**:

```
/{system-slug}/                                       system landing
/{system-slug}/{track-slug}/                          track overview
/{system-slug}/{track-slug}/{module-slug}/            module landing
/{system-slug}/{track-slug}/{module-slug}/unit-{NN}/  unit page
```

- **Track is in the URL** on every system, including single-track ones
  (e.g. `/nintendo-entertainment-system/assembly/`). No bare module URLs.
- **No `/curriculum/` or `/learn/` prefix** — the system slug is the root.
- **`{module-slug}` is a bare identity** — no `game-NN-` prefix. Ordering is the
  module catalogue's array position, not anything encoded in the slug. Renaming
  *and* re-ordering are now free (re-ordering is a data edit, no redirect needed).
  This supersedes the original `game-{NN}-{game-slug}` slug form — see
  [modules-not-games.md](modules-not-games.md). Shipped pre-module URLs keep
  working via redirects in `astro.config.mjs`.
- Unit is `unit-{NN}` — number only, no slug. Titles change; numbers are stable.
  Matches the existing Astro `[...slug].astro` routing.

## Why

- **Track-in-URL.** The track is a real fork (gentle BASIC/HLL vs flagship assembly)
  and belongs in the address. Keeping it on single-track systems too means a system
  gaining a second track later doesn't break the first's URLs, and the whole fleet
  stays consistent.
- **System-rooted, no prefix.** Shorter, more readable, survives reorganisation, and
  `/{system}/` is the QR-code entry point printed on flyers and t-shirts.

## Status of the spec

Supersedes the v2.1 in-repo IA spec, which still uses `/curriculum/{platform}/` and
`/learn/{platform}/game-NN-slug/unit-NN-slug/` (with a unit slug, no track segment).
The current pattern is track-explicit with bare module slugs:
`/sinclair-zx-spectrum/basic/lucky-number/unit-03/`. The design-exploration
wireframes that drop the track segment are wrong; the bare-slug part they showed
(`.../lucky-number/unit-03/`) is now correct, but the track must be present.

## Drift triggers

- A unit or module URL without a `{track-slug}` segment.
- Re-introducing `/curriculum/` or `/learn/`.
- Adding a descriptive slug to `unit-{NN}`.
- Re-introducing a `game-{NN}-` prefix on a module slug, or treating slug position as
  the source of order — order is catalogue data (see modules-not-games.md).

## Anchored in

- [systems-not-platforms.md](systems-not-platforms.md)
- [Information architecture](../specifications/information-architecture.md) — site URL structure (v2.1; v3 reconciliation pending)

## Log

| Date | Event |
|---|---|
| 2026-05-29 | Track-in-URL reaffirmed; full system-rooted pattern recorded. |
| 2026-06-01 | `game-{NN}-` slug form dropped for bare module slugs (modules-not-games.md). Track-in-URL unchanged. |
