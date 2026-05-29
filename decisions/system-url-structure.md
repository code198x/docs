# Decision: System-rooted URLs with an explicit track segment

## The decision

Canonical URL pattern — system at the root, **track always explicit**:

```
/{system-slug}/                                              system landing
/{system-slug}/{track-slug}/                                 track overview
/{system-slug}/{track-slug}/game-{NN}-{game-slug}/           game landing
/{system-slug}/{track-slug}/game-{NN}-{game-slug}/unit-{NN}/ unit page
```

- **Track is in the URL** on every system, including single-track ones
  (e.g. `/nintendo-entertainment-system/assembly/`). No bare game URLs.
- **No `/curriculum/` or `/learn/` prefix** — the system slug is the root.
- `game-{NN}-` is zero-padded and reflects canonical order. Renaming a game is free;
  re-ordering needs a redirect (deliberate friction — think before re-ordering).
- Unit is `unit-{NN}` — number only, no slug. Titles change; numbers are stable.
  Matches the existing Astro `[...slug].astro` routing, so no migration cost.

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
The v3 draft embodies this pattern. The design-exploration unit wireframes are wrong:
they show `/sinclair-zx-spectrum/lucky-number/unit-03/`, dropping the track and
`game-NN-` segments. Productionised ribbons must read
`/sinclair-zx-spectrum/basic/game-02-lucky-number/unit-03/`.

## Drift triggers

- A unit or game URL without a `{track-slug}` segment.
- Re-introducing `/curriculum/` or `/learn/`.
- Adding a descriptive slug to `unit-{NN}`.

## Anchored in

- [systems-not-platforms.md](systems-not-platforms.md)
- [Information architecture](../specifications/information-architecture.md) — site URL structure (v2.1; v3 reconciliation pending)

## Log

| Date | Event |
|---|---|
| 2026-05-29 | Track-in-URL reaffirmed; full system-rooted pattern recorded. |
