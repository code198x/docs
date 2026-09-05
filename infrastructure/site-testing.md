# Website validation

The website's `package.json`, `vitest.config.ts`, `playwright.config.ts` and workflow files own the executable checks. Run commands inside the website repository.

| Command | Purpose |
|---|---|
| `npm test` | Vitest unit tests under `src/` |
| `npm run build` | Unit/content checks, Astro build and Pagefind indexing |
| `npm run test:e2e` | Playwright browser checks |
| `npm run test:a11y` | Representative axe accessibility checks |
| `npm run test:a11y:sweep` | Explicit full built-site accessibility audit |
| `npm run prose:check` | Advisory prose style and readability checks; requires the configured Vale tooling |
| `python3 -m unittest discover -s scripts -p 'test_discord_*.py'` | Offline announcement payload regression checks |

The regular Playwright configuration starts the development server when needed and defines desktop and mobile projects. The full accessibility sweep serves the production build on a separate port; it is a deliberate broader audit, not required for every wording change. Check the configuration for current ports and environment switches.

Native-image tests and builds require generated Play198x WebAssembly. Use the documented build script and configured workspace; a missing decoder is an environment prerequisite, not evidence of a page regression. Report failed checks and their concrete cause rather than claiming validation from a partial run.

For visual or interactive changes, inspect the affected pages in light and dark themes, at narrow and wide widths. Check keyboard focus, readable contrast, overflow, reduced motion and alternatives to colour or audio cues. Automated accessibility tests support this inspection; they cannot establish that an explanation is understandable.

The accessibility baseline records known findings. Do not add entries merely to make a check pass. Use the existing theme-aware ink helpers and design tokens rather than raw platform colours for small text.

Use targeted tests during development and the required build before publication. Broaden testing when changed behaviour or a failure warrants it. Do not repeat a full-site audit for an unchanged low-impact edit.
