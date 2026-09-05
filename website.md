# Website and publishing workflow

This guide connects curriculum authoring to the implementation. The [website repository](https://github.com/code198x/website) owns schemas, components, routes, package versions and deployment. The [code-samples repository](https://github.com/code198x/code-samples) owns executable sources, assets, Makefiles and capture recipes. Read their current files before changing a workflow; this guide is not another status board.

## Content and navigation

System material follows **system → track → module → unit**; shared material follows **section → module → unit**. A module may be a game, teaching module or interval, and a game may span several modules. Bare slugs identify content; ordered catalogue arrays establish sequence.

| Website location | Responsibility |
|---|---|
| `src/content.config.ts` | Collection schemas and accepted metadata |
| `src/content/systems/` | System identity and distinct availability/tool capabilities |
| `src/content/modules/` | Ordered module catalogues, groups and route relationships |
| `src/content/units/` | Unit metadata and availability |
| `src/content/curriculum/` | Authored MDX: module indexes, `unit-NN.mdx` and getting-started pages |
| `src/content/vault/`, `src/content/patterns/` | Encyclopaedic entries and reusable techniques |
| `src/lib/modules.ts` and route helpers | Lookups, counts and derived navigation |

Catalogue status, authored pages, downloadable sources, successful builds and observed execution answer different questions. Do not infer one from another or keep duplicate prose completion totals. `requires` and `suggests` express useful knowledge and routes, not attendance checks.

Unit-page frontmatter currently requires a title and numeric `game` and `unit` fields. Other collections have their own schemas; inspect them instead of maintaining duplicate templates. Layout, neighbours and counts are derived by the website.

Shared routes use `/foundations/{module}/unit-NN/` and `/craft/{module}/unit-NN/`; system lessons use `/systems/{system}/{track}/{module}/unit-NN/`. The Vault uses `/vault/{category}/{slug}/`; patterns use `/patterns/{system}/{track}/{category}/{slug}/`, with cross-platform entries omitting the track. Route code remains authoritative. Preserve published redirects when moving content.

A link should explain why it helps. Keep the essential explanation local and offer deeper shared concepts, context or patterns as useful connections. Fleet badges do not establish emulator, assembler or curriculum support interchangeably.

## Code and artefacts

Include maintained executable listings through `CodeFromFile`. Source paths generally follow `{system}/{track}/{module}/unit-NN/`. Check the component’s language detection when adding a dialect. Pseudocode and labelled schematic fragments can remain in MDX.

Keep meaningful intermediate states using the sample repository’s existing `steps/` convention where appropriate, and use `CodeDiff` to explain changes. There is no fixed line quota. Explain supplied routines and assets before readers depend on them; provide their contracts and provenance.

The website’s `scripts/build-artefacts.sh` builds and stages downloads. Source Makefiles and capture manifests specify individual builds. Record tool versions and target configuration when reporting validation. Keep reproducible source in Git and publish generated outputs through the build path; remove existing tracked binaries only after verifying equivalent builds and downloads.

`AssembleAndRun` currently supplies a Spectrum assembly loop with the family tools. It complements local build instructions and downloads. Browser convenience does not expand target hardware or establish support for another language or system.

## Capture and execution

The manifest-driven runner is [code-samples/_capture/capture.py](https://github.com/code198x/code-samples/blob/main/_capture/capture.py). Its help, implementation and checked-in manifests define supported machines, source formats, timeline actions, binary resolution and output paths. Use that contract rather than a second table of emulator capabilities or hard-coded author-specific paths.

A manifest names the target, source program, output location and sequence of waits, inputs and captures. Keep it and any expanded script with the sample so the result can be reproduced. Frame counts depend on the selected model and video standard. Distinguish cold boot, tape loading, snapshots, direct injection and state-changing setup writes. Identify shortcuts used to reach a test state; do not present them as ordinary playthroughs.

Check the required assembler, emulator, converters, firmware and recording tools before promising a capture. Configure dependencies through the tools’ current options. View images, watch video and listen to sound; a successful script proves neither appearance nor feel. Record what was observed, the source revision, machine configuration and limitations.

## Sources and system facts

This repository specifies teaching and game design. It does not maintain another hardware encyclopaedia, language manual, emulator roadmap or tool-support matrix. Check facts against original manuals, datasheets and other appropriate evidence; check implementation capabilities in the project that owns them. Cite original publications or useful public pages in published material, with precise locators. Do not expose private collection paths.

Useful contextual entries belong in the public Vault; reusable implementations belong in the Pattern Library. Neither replaces evidence for a hardware claim. Name stock, expanded and successor configurations explicitly. Development hosts and transfer tools do not silently change the target.

## Rendering and design

Use the website’s current Astro/MDX rendering path, Sätteri integration and theme-aware highlighting; inspect the package manifest, lockfile and highlighting plugin before changing them. Follow existing family tokens and components rather than the retired HTML mock-ups. Nebula Sans, Literata and JetBrains Mono have distinct interface, reading and code roles; existing editorial templates also use Literata for display headings.

Maintain readable contrast, keyboard focus, narrow-screen layouts and reduced-motion support. Keep decorative motifs away from essential information. Native-image decoding uses Play198x WebAssembly: follow `scripts/build-wasm.mjs` and the website README for its workspace and generated-decoder requirements.

Contributor data for the colophon comes from `scripts/build-colophon.mjs`; updates are reviewed source changes, not network lookups during rendering. Curate tools and typeface credits and do not rank people by commit totals.

Possible teaching components belong in [current work](work.md#website-components) until a lesson demonstrates the need. Existing components and their tests establish what is available.

## Validation

Run checks from the owning repository. Website `package.json` and CI define the supported commands: `npm test`, `npm run build`, `npm run test:e2e`, `npm run test:a11y` and the explicit full-site accessibility sweep. The production build runs unit/content checks, builds pages and indexes them. Decoder-dependent checks need the generated Play198x package. Report skipped or blocked checks accurately.

For visual or interactive changes, inspect affected pages at narrow and wide widths, in both themes where relevant, and check keyboard use and alternatives to colour or sound cues. Existing accessibility baselines record known findings; do not expand them to conceal a regression. Use targeted checks during work and required checks before publication. Prose linting is advisory; editorial judgement remains necessary.

## Discord announcements

The Pages workflow compares the deployed and newly built RSS feeds using `scripts/discord-new-items.py`, then prepares messages with `scripts/discord-payloads.py`. Posting happens only after successful deployment. Release and optional aggregate webhooks are secrets; identical targets are deduplicated, and missing secrets cause a notice without posting.

Preserve absolute feed URLs and resolve relative ones against the site origin. The payload builder validates the origin, shortens fields, and batches against both ten embeds and the combined 6,000-character limit, counting UTF-16 code units conservatively. See [Discord’s embed limits](https://docs.discord.com/developers/resources/message#embed-limits). Five messages remain the per-deployment ceiling; omitted items produce a warning.

Run offline regressions with `python3 -m unittest discover -s scripts -p 'test_discord_*.py'`. The `new-items` artifact retains the full item list and prepared messages for seven days. An offline test proves request construction, not delivery.

This is a feed difference, not a delivery ledger. Later deployments do not replay failed posts. Inspect delivery in each channel before recovery because a partially successful retry can duplicate messages. Old workflow reruns still use old code; use the corrected builder with the retained item list for an authorised recovery. Never expose webhook URLs in source or logs.
