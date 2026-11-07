# System profiles

A system profile tells a reader what a machine can do, what it was used for and where the curriculum could take it. The site catalogues about 160 systems; most have a page with five facts and nothing else. A profile is how a system gains depth without changing its readiness: `tier` stays the single source of truth for curriculum readiness, and only Steve moves a system between tiers. The factory may propose a move with evidence.

Each part of a profile lives on the surface that already does that job, so nothing is written twice.

| Part | Where it lives | Reviewed by |
|---|---|---|
| Capability | `capability` in the system's catalogue entry, `website/src/content/systems/<slug>.yaml`, shown on `/systems/<slug>` | the pull request that adds it |
| Historical use | the Vault entry `systems/<slug>` | the Vault's review process ([Vault](vault.md)) |
| Curriculum hooks | rows in the [content queue](../content-candidates.md) with `system: <slug>` | queue triage |

## Capability

Capability describes one named configuration, because models, memory sizes and regional versions differ. `configuration` names it (for example "Oric Atmos, 48K, PAL"). Eight fields follow, each a short statement for a reader and the sources that support it:

| Field | What it covers |
|---|---|
| `processor` | CPU, clock speed and anything about it a programmer meets, such as a second processor |
| `memory` | RAM and ROM sizes, and what the memory map leaves a program |
| `display` | text and graphics modes, resolution, colours and how colour is assigned |
| `sound` | the sound hardware and its voices or channels |
| `input` | keyboard, joysticks and other controllers it supports as built |
| `storage` | tape, disk or cartridge, and their speeds or capacities where sources give them |
| `expansion` | ports and buses for adding hardware |
| `firmware` | what is in ROM: the built-in language, monitor or operating system |

```yaml
capability:
  configuration: "Oric Atmos, 48K, PAL"
  memory:
    value: "48K of RAM and 16K of ROM; BASIC programs start at #0501."
    sources:
      - "Oric service manual, section 2 (memory map)"
      - "The Oric Atmos Handbook, chapter 9"
```

The rules for sources are the Vault's ([Writing and evidence](vault.md#writing-and-evidence)): cite original, checkable sources such as manuals, service documentation, datasheets and period magazines; give a second, independent source where one exists; and never name a private collection or local path. A field without a source is left out, not guessed. A field missing from a profile is a gap the depth report shows.

## Support surfaces

A profile doesn't restate support. The catalogue's existing flags carry it (`emu198x`, `devReady`, and Asm198x through `cpuArchitecture`; see the umbrella decision on support surfaces). Work on a profile checks each flag the system carries by running the tool: the machine boots in Emu198x, or a program assembles with Asm198x and runs. The pull request records what was run and what it showed. A flag the tool can't back up is reported as a bug in the tool's own repository, not removed quietly, and a profile never sets a flag.

## Depth

Depth is derived, never stored. `npm run systems:depth` in the website reports, for each system:

- its `tier` and support surfaces, unchanged;
- its Vault entry: none, unreviewed or reviewed;
- how many capability fields are present, out of eight;
- how many Vault games, techniques and other entries name it in `platforms`, how many patterns are written for it, and how many lessons it has.

Each missing item is a gap the factory can pick up: a Vault entry goes through the [Vault candidate backlog](../vault-candidates.md), capability and hooks through the content queue.
