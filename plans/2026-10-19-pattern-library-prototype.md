# First Pattern Library connections prototype

Approved brief: input reading, press detection and sound triggering, plus one study-derived technique. Show how they fit before expanding the catalogue. Extend the incumbent Pattern Library identity and layouts; prepare an unpublished draft for review, not deployment or a global migration.

1. Audit the existing four-machine readers, cross-platform edge-detection explanation and executed C64 note trigger. Preserve exact entry URLs, authorship and evidence status. Choose target selection plus legal-neighbour choice as an original, simplified example motivated by the Pac-Man study.
2. Build an isolated /catalogue/pattern-library/ preview in the website with four conceptual technique records, validated links to current collection entries and explicit implementation/evidence summaries. Show task search, machine/language discovery, next-step connections, and dedicated technique pages. Keep the current public directory and pattern schema untouched; exclude preview routes from the sitemap and mark noindex.
3. Add one bounded browser experiment showing input samples → new press → one sound event, plus a step-through pursuit example. Use original geometry and browser code, not a historic game's assets or a claimed hardware implementation. Audio starts only on explicit activation; provide visual feedback, mute and keyboard/touch controls, no timing or sound-fidelity claims. Baseline reading/links must work without JavaScript.
4. Verify relation resolution, old URLs, multi-machine/language presentation, empty/filter state, keyboard use, transition/held-input cases, deterministic legal movement and browser sound scheduling. Test actual wiring as well as the model. Build, then inspect desktop and phone together, repair identified defects in one batch and confirm once. Run the skill's mechanical detector and required finish review. No new dependencies.
5. Push draft PRs, save portable working previews and desktop/phone screenshots in the chat outputs folder, and explain what is a prototype versus an existing implementation. Keep deployment and expansion for the owner's review. Remove task-owned worktrees/builds/processes after preserving remote commits and deliverables.

Expected website files: src/data/pattern-techniques.ts; src/lib/pattern-techniques.ts and a focused invariant test; src/components/patterns/TechniqueDirectory.astro, TechniqueExperiment.astro; src/scripts/pattern-experiment.ts; src/styles/pattern-prototype.css; src/pages/catalogue/pattern-library/[...technique].astro; astro.config.mjs (precise preview exclusion); tests/pattern-prototype.spec.ts. Verify current paths before edits; simplify where existing components serve the job.

## Code-led revision

The owner clarified that the prototype must show the library itself: reusable machine-specific code, clear calling instructions and examples of fitting routines together. Browser demonstrations become optional supporting material. The owner explicitly approved the specification clarification above.

1. Reuse the existing task/technique routes, directory and visual system. Put machine choice, maintained listings and caller contracts ahead of interactive examples. Show source/copy controls, inclusion, initialisation, update calls and onward connections. Preserve existing public article URLs.
2. Keep maintained routines in code-samples. Reuse checked C64 joystick/SID, Spectrum beep and Amiga sample routines. Add bounded reader/edge/caller material where needed, with explicit assembled versus executed status; include a complete C64 input-to-sound program and an actual study-derived local-turn routine. No dependencies or schema migration.
3. Verify assembled sources and the composed C64 behaviour, held/released/repressed controls and resource ownership. Exercise code copying, machine navigation, links, no-JavaScript reading, keyboard access and desktop/phone layouts. Build opt-in and default production configurations, and retain the opt-in publication guard.
4. Update the existing draft PRs and add a linked sample PR. Export a revised portable code-first review, run required fresh visual/documentation reviews, preserve verified remote commits, then clean task worktrees and processes. No merge or deployment.

## Code-first review evidence

The prototype now renders maintained machine code and caller contracts before optional interactive support. Seventeen review routes cover the index, four technique pages and machine variants of the three input/sound techniques. The existing public directory, schema and URLs remain in place. The owner approved the binding specification clarification.

The C64 has a complete caller; other machines have assembly-checked integration fragments and explicitly retain that boundary. An original 6502 target/local-turn implementation replaces the earlier browser-only demonstration as the study-derived code example. The sample source recipe records 14 C64 control stages, actual SID control writes, gate duration and 58 chooser cases in VICE. A deliberate held-state mutation confirms the retrigger check detects the regression. No original-hardware or unexecuted-machine claims are made.

Verification: all four machine combinations assemble/link; the Python recipe is Ruff clean. The website has 252 passed unit tests, 9 prior skips, and 26 passed desktop/phone browser checks, including all review routes, clipboard copying, machine-preserving connections, exact viewport widths, no-JavaScript reading and Axe. One shared listing-helper correction keeps vertically scrolling code keyboard-accessible. The existing Amiga joystick article's reversed Fire-button table is corrected against the hardware manual.

Nine captures cover library, C64 code and pursuit at desktop, 390px and 320px. The fresh visual review returned `ship` with no material fixes. The detector returned no findings. The portable 17-page review and source archive preserve the include layout; local-file navigation and both supporting experiments were exercised without browser errors. Draft changes await owner review; nothing is merged or deployed.

## Execute the remaining machine combinations

The owner requested running and verifying the Spectrum, Amiga and NES examples before merge. Keep reusable routines and caller fragments, and add complete bootable callers so the whole path is observable.

1. Add demo.asm and Makefile for each machine beside input.inc, presses.inc and use.inc. Include maintained routines rather than copies. Initialise the machine, writable state, update timing and sound resources explicitly. Show held/new input and trigger counts visually where practical.
2. Add a bounded verification recipe in scripts/ using the existing Emu198x MCP paths. Run the Spectrum 48K caller, boot an A500 OCS PAL ADF, and boot an NTSC NROM cartridge. Apply input through emulator key/controller events; check guest-held masks, press masks, event counts, audio start/stop and continuing updates. Check simultaneous input, holding, release/repress and entry state. Capture sound and actual output; keep emulator versus hardware boundaries explicit.
3. Prove regression checks can fail, record source/binary/emulator hashes and exact configurations, and keep generated artefacts in ignored build directories. Reuse existing verification helpers where appropriate. No dependencies added and no emulator source changes planned. Temporary native emulator builds will be removed after evidence is retained.
4. Update code-first website contracts, maintained caller listings and execution labels to match observations. Rebuild and run relevant unit/browser checks. Refresh the portable review and sample archive, push updated draft PRs and clean task worktrees/processes. Merge only after the verification condition is satisfied and the draft review state is resolved; retain the prototype publication boundary unless separately approved.

## Remaining-machine execution outcome

All three complete callers run in Emu198x: a 48K PAL Spectrum from snapshot and fresh ROM tape load (0.32.5); NTSC NROM from cartridge reset (0.34.2); A500 OCS PAL with Kickstart 1.3 from a cold ADF boot (0.34.2). The records identify library source, binary and emulator hashes, and the Amiga firmware hash without distributing firmware.

Spectrum checks 39 input stages, including all 32 QAOP/Space masks; NES checks 263 stages, including all 256 controller masks. Amiga checks 25 stages, covering all nine normal stick positions with/without Fire and the held/released/repressed sequence. Its input adapter resolves opposing directions before the port read, so those states are outside the matrix. Guest per-bit edge counters allow the ordinary Amiga caller to run on its full native clock.

Five audio windows per machine check release, press, hold, stop and repress. Capture analysis checks a real waveform and the caller’s expected pitch, not only register writes. The update counter must advance during each window. A new press creates one event, holding creates none, and release/repress creates the next. A deliberately cleared history while the action remains held produces an extra event and the same guard rejects it. This is labelled diagnostic intervention; positive input cases use normal emulator events. Screenshots are captured before that intervention.

The beeper is a short blocking click; holding it remains silent after that click. NES pulse and Paula playback continue after the call and stop on release. Amiga recordings allow the observed filter tail to settle before the strict silence check; this is not an instantaneous-mute or original-hardware claim. The actual native-frame windows and update counts remain in the receipts; no host-capture latency or exact FPS claim is inferred from them.

Each machine folder now contains demo.asm and a Makefile alongside the reusable routines and fragment. The website keeps the fragment central and offers the complete caller as an additional disclosure, with matching run instructions and a machine-specific evidence link. Existing public directory and prototype publication boundaries stay intact.


CI exposed integration fragments named as standalone assembly programs. These are now use.inc files, still assembled through their check.asm wrappers and complete callers; no build checks were disabled. NES sources use the repository’s established nintendo-entertainment-system folder while website machine URLs keep nintendo-nes. Native execution and C64 regression recipes were rerun after the corrections, and source PR #108 passes all required CI checks.

The complete-caller disclosure exposed a long build command overflowing a phone viewport. Allowing that inline command to wrap fixes the cause; the expanded-caller browser check now measures document overflow too. The 17-page portable review, runnable media and matching source archive include the verified callers. No firmware is distributed.
