# Eight by One (working title)

**Status:** proposal, for Steve's approval. Nothing is built until it is agreed.
**Kind:** demo (see [What makes a finished demo](../../../../PROJECT.md#what-makes-a-finished-demo))
**Target:** ZX Spectrum, assembly; runs on the 48K, 128K and +2, +2A and +3, and Pentagon 128
**Queue:** CC-0001; its explainer is CC-0002 (multicolour, From the Metal)
**Implementation state checked in:** the website module catalogues (`src/content/modules/sinclair-zx-spectrum/`), the code-samples Spectrum assembly tree and its executable proofs (`_capture/verify.py`), and the content queue.

## Experience and scope

A short party-standard demo, about two to three minutes, built around one idea: the Spectrum's colour rules can be broken by racing the beam. The machine stores one ink and one paper colour for each 8×8 cell. Rewriting a cell's attribute between scan lines, in step with the picture being drawn, gives every line of the cell its own colours: cells 8 pixels wide and 1 line tall. That is where the title comes from.

The viewer watches, rather than plays. A demo is finished when it runs from loading to its end screen as one deliberate production: parts that belong together, music that carries them, transitions rather than cuts, and an end. It is not one effect on a loop.

Parts, in order:

| Part | What the viewer sees | Why it is here |
|---|---|---|
| Loading | A loading screen while the tape loads, then a short title | Every Spectrum production starts here; it sets the tone |
| Multicolour | A picture or logo in colours the Spectrum can't normally show together, then the same picture with the trick switched off, so the difference is plain | The centrepiece, and the timing that differs between models |
| Border | Colour bars in the border, moving with the music | Racing the beam where the picture isn't: the same timing, a simpler canvas |
| Scroller | Greetings and credits scrolling over the music | Pacing and a breather; the part most demos had |
| End | An end screen, and the demo stops cleanly | A finished production ends; the verify reads its end marker |

Music is an original three-channel AY tune on the 128K, +2, +2A, +3 and Pentagon. The 48K has no AY chip, so it runs the same parts in silence, or with a short beeper motif if the timing allows; the brief doesn't promise beeper music.

Deliberate exclusions: no 3D, no sampled speech, no disk loading, no Interface 1 or other peripherals, and no effects borrowed from published demos. Design risks: multicolour on the contended 48K and 128K leaves little time for anything else in that part, so the music player's timing must be planned with it; and the +2A and +3 contend memory differently from the 128K.

Nearest existing material: no Code198x demo exists yet. The Spectrum assembly ladder proposes multicolour as a later rung ("attribute changes per scanline beyond the 8×8 limit", marked "needs source"); this demo is a production, not that lesson, but its evidence feeds both.

## Learning and connections

The demo is the production-line pilot first (content factory plan, step 9). As a later track step it would introduce racing the beam: counting T-states against the picture, memory contention, and per-model timing. It reinforces attributes, port `$FE` for the border, and interrupt-driven timing. It feeds the From the Metal article on multicolour (CC-0002) and the step 11 walk on Spectrum multicolour. Vault connections: `hardware/ula`, `hardware/ay-3-8912`, `techniques/raster-effects` and `techniques/attribute-aware-design`. There is no Vault entry on multicolour itself yet; step 11 of the plan writes one, and it becomes a link only once it exists.

## Target and tools

Runtime: an unexpanded ZX Spectrum 48K, 128K, +2, +2A or +3, or a Pentagon 128, on a PAL television, loading from tape. Development: Asm198x (Z80, the dialect the current Spectrum lessons use), producing a tape image; Emu198x's Spectrum runner for every check, headless, on each named model; Build198x where it converts graphics.

Timing differs by model, and the demo's correctness depends on it:

| Model | Frame | Line | Contention | Source |
|---|---|---|---|---|
| 48K | 69,888 T-states | 224 T-states | yes | Chris Smith, *The ZX Spectrum ULA* (2010), chapter 11 |
| 128K, +2 | 70,908 T-states | 228 T-states | yes | Chris Smith, chapter 24, to be checked against the chapter |
| +2A, +3 | 70,908 T-states | 228 T-states | yes, a different pattern | to be sourced |
| Pentagon 128 | 71,680 T-states | 224 T-states | none | to be sourced from a primary account |

The demo detects its model at start-up and uses the timing table for it. Values marked "to be sourced" are confirmed from a source and by measurement in the emulator before any part depends on them.

## Graphics, sound and content

Graphics: an original logo or picture designed for multicolour, prepared with Build198x or a small converter, and an original font for the scroller. The picture is chosen to show what 8×1 colour cells make possible, not to imitate a known demo's art.

Sound: an original AY tune, about two minutes, written by an agent in a tracker format the demo's player can read; Steve listens and approves or rejects it as part of reviewing the demo. Credits name every contributor, human and agent, as the project's AI disclosure requires.

Scroller text: greetings to the Spectrum scene in general terms, and the credits. No named greetings to real groups without their agreement.

## Runnable development sequence

| Stage | Inspectable result | New idea | Changes | How to check it |
|---|---|---|---|---|
| 1. Multicolour proof | One multicolour logo, stable on the 48K | Racing the beam with a timing table | Effect code, logo | Reference capture on the 48K; repeat runs match |
| 2. All models | The same logo on all four models | Model detection, per-model timing | Timing tables | Per-model reference captures; a deliberately mistimed table fails only on its model |
| 3. Border | Border bars | The same timing in the border | Border routine | Per-model captures |
| 4. Music | The tune playing through the parts | An interrupt-driven AY player beside timed effects | Player, tune | Audio capture; Steve listens |
| 5. Scroller and transitions | The parts joined with transitions | Pacing, a part sequencer | Sequencer, font, text | The whole demo runs to its end on every model |
| 6. Loading and end | Tape loading screen, end screen and end marker | Packaging | Loader, end | Loads from tape; end marker reached within the frame budget on every model; Steve watches it |

Stage 6 fulfils the finished-demo promise.

## Verification and finishing

The production record extends the existing executable proof (`_capture/verify.py` and its `proof.*.json` manifests): pinned tool revisions, a build that assembles identically twice, and then, for each named model, a run that reaches the demo's end marker within a frame budget, reference captures of each timed part that match, and a second run that matches the first. One `verify` command runs all of it and exits non-zero on any failure. Before relying on it, a deliberately mistimed effect must fail on the model it breaks and pass on the others.

A screenshot can't prove timing by itself: the captures are taken at frames chosen inside each timed part, and Steve watches the finished demo on at least one model. Emulator gaps found on the way are recorded as tool issues through the content factory's blocked-work process (step 6), not worked around silently. Emulator results are not original-hardware results; a hardware check is welcome but not promised.

Packaging: a tape image with a loading screen, the credits in the scroller and on the end screen, and a short page describing the demo and the models it runs on.

What would change this recommendation: if multicolour leaves no time for the AY player on the 48K and 128K, the multicolour part runs without music, and the brief says so.
