# Decision: "Systems", not "Platforms"

## The decision

The structural term across the site is **system**, not **platform**. That fixes:
the nav item ("Systems"), the fleet index URL (`/systems/`), the content-collection
key, the directory name, and component names (`SystemCard`, `SystemMotif`,
`SystemStripe`).

Editorial prose may use "platform" wherever it reads better. Only the *structural
vocabulary* is fixed to "system"; sentences are free.

## Why

- **Period-correct.** In 1985 the playground question was "what system have you
  got?"; Crash reviewed systems. The project's premise is period authenticity down
  to the primary sources — using the era's own word is free authenticity.
- **Fits the scope.** The fleet spans home computers, consoles, handhelds,
  single-board kits, and eventually calculators and oddities. "Platform" technically
  covers them; "system" wears all of them naturally. A Vectrex or KIM-1 is a
  "system" — calling it a "platform" sounds modern.
- **Dodges modern tech-speak.** "Platform" reads 2010s SaaS (PaaS, platform teams,
  social platforms). "System" reads 1980s. For a brand at pains not to sound like a
  startup, the connotation matters.

Cost: "platform" is marginally more familiar to a modern dev skimming. Mitigated
because prose may use it; only structure is fixed. No SEO difference — both terms
are searched.

## Status of the spec

The in-repo IA spec `specifications/information-architecture.md` is still v2.1 and
uses "platform" throughout. The v3 draft (pending merge from the website-design
work) adopts "system" as the structural term. This record is binding until v3 lands.
The wireframes from the design exploration (`PlatformMotif`, `/platforms/`, nav
"Platforms") are on the losing side and must be renamed when productionised.

## Drift triggers

- Naming a nav item, URL segment, collection key, or component "platform…".
- A page that puts the fleet at `/platforms/`.

## Anchored in

- [system-url-structure.md](system-url-structure.md)
- [Information architecture](../specifications/information-architecture.md) — site URL structure (v2.1; v3 reconciliation pending)

## Log

| Date | Event |
|---|---|
| 2026-05-29 | Confirmed after going back and forth — "system" is the structural term. |
