# Connections and placement for the Spacewar! pilot

**Status: authoring proposal, 18 October 2026.** The first study is agreed; site placement and the teaching experiments below are not implemented or published. [The charter](../../PROJECT.md) remains authoritative. Start with [the draft](study.md), not a new navigation commitment.

## Existing destinations worth connecting

Checked against the website's main branch during this pass. These are potential editorial links, not a claim that each source has been exhaustively re-reviewed.

| Destination | Purpose and boundary |
|---|---|
| [Game Feel](https://code198x.com/craft/game-feel/) and [the movement playground](https://code198x.com/experiments/game-feel/) | Existing controls-and-response material can help separate an input, a change of velocity and the resulting movement. The study now includes the control-to-motion chain and contrasts input signals and possible mappings. The existing one-dimensional capped-speed experiments are not a Spacewar physics model. Explain that difference rather than claim they reproduce the duel. |
| [Maths for Games](https://code198x.com/craft/maths-for-games/) | The illustrated study now links directly to the published coordinates (unit-06) and fractional-velocity (unit-11) lessons, after explaining velocity and acceleration locally. A full gravitational-orbit derivation is not established by that coverage. |
| [The Craft](https://code198x.com/craft/) and [its coverage map](../../specifications/craft-coverage.md) | Compare design choice and moment-to-moment experience. Game Design is an agreed home with lessons still to develop; do not invent a missing lesson link. |
| [Thrust in the Vault](https://code198x.com/vault/games/thrust/) | A later vintage comparison for control, gravity and inertia. Similarities are a comparison opportunity; establish an influence separately before asserting a direct lineage. Read the existing entry rather than duplicate it. |
| [Finishing and delivering](../../specifications/experiments/finishing-and-delivering.md) | A production-teaching connection: define an experience, distinguish required work from additions, provide instructions and test a handover. Historical distribution by program exchange needs its own treatment; it is not a retail launch. |
| [Graphics and audio](../../specifications/graphics-and-audio.md) | Connect silhouette, motion cues and the physical playing arrangement to intended experience. The pilot does not establish historical audio behaviour. |
| [Vault specification](../../specifications/vault.md) | Owns historical evidence, credit, responsible interpretation and article review. A study can refer to canonical entries without making those entries about Code198x. |

The existing [Game Design](https://code198x.com/vault/design/game-design/), [Game Loop](https://code198x.com/vault/techniques/game-loop/), [Analogue Control](https://code198x.com/vault/hardware/analog-control/), [Trackball](https://code198x.com/vault/hardware/trackball/), [Steering Wheel](https://code198x.com/vault/hardware/steering-wheel/), [Light Gun](https://code198x.com/vault/hardware/light-gun/) and [Physics Engines](https://code198x.com/vault/technologies/physics-engines/) entries provide canonical context. The control comparison now links those device entries rather than proposing duplicate biographies of the hardware. Game Design is already a sourced historical article about designers' practice; the pilot's applied questions belong in complementary explanations, not a replacement history.

Spacewar! already has candidate VC-2076 in vault-candidates.csv with incoming-link leads. The [named-subject audit](vault-audit.md) records the new cultural leads and the existing people, organisations and game candidates to reuse. The [standing study approach](../../specifications/game-studies.md) makes this outward investigation part of every study. Issue #394 is closed and concerns PDP systems catalogue coverage, not this study. Title/filename, candidates and GitHub issue searches were checked before choosing companion scope; search results are not proof against every possible alias. No new issue batch or duplicate Spacewar candidate is added.

## Companion drafts now written

| Draft | Gap it addresses | Relationship to existing material |
|---|---|---|
| [Shooting from a moving ship](companions/shooting-from-a-moving-ship.md) | Inherited launch velocity and interception, with checked stationary- and moving-target calculations | Builds on published coordinates, triangle, angle and fixed-point velocity lessons. Does not replace them or claim they already teach interception. |
| [What makes a duel worth another go?](companions/designing-a-duel.md) | Resource limits, commitment, risk, feedback and counterplay explained through actual Spacewar rules | An applied design explanation alongside the historical Game Design article and existing Game Feel experiments. Not a new course lineup or a universal design formula. |

Both are readable drafts linked from the study; publication home and a further editorial pass remain open. Existing website articles are linked, not silently overwritten or marked reviewed. Specific expansion proposals are now concrete text rather than only backlog suggestions.

## Later investigation candidates — interactive work deferred

- **Input and continuing motion:** predict a release outcome, observe it and compare the capped-speed Game Feel model with the chosen Spacewar configuration. Do not transfer frame counts or units between them without a defined conversion.
- **Aiming while moving:** draw the next moment from a recorded state before running it. Distinguish ship motion, launch direction and the opponent's possible response. No new runnable physics tool is commissioned here.
- **Visible and audible information:** ask what the other player can infer from display cues and the controls themselves. Compare physical arrangements only when actual equipment is available; a keyboard can introduce its own rollover limits and sounds.
- **Design through iteration:** compare one documented early rule or presentation change with its stated purpose, and test whether present-day participants experience the proposed effect. Historical testimony and present-day observations remain separate.
- **Reaching an audience:** compare what a demonstration, a shared program tape and a packaged retail game ask of their audience. Elite and Monty may later provide retail contrasts; those chapters are not written by this pilot.

The following extensions remain candidates; the two static companion drafts above are the bounded work completed in this pass. Interactive examples are held back at the owner’s request. These extensions could serve existing Craft homes. A design claim should become a lesson only when the comparison, limits and reader outcome are clear. None is a new prerequisite or a reason to retrofit every system course.

## Where might studies live?

| Option | Advantage | Question to settle |
|---|---|---|
| A study associated with a Vault game entry | Starts from an existing subject and gives a natural historical link | How will we keep guided investigation distinct from the canonical encyclopaedia entry and avoid duplicated claims? |
| A linked sequence within The Craft's Game Design home | Makes practical design questions and application prominent | Can a reader arrive for the cultural or production history without being funnelled through a course? |
| A distinct Studies collection, linked from both | Gives whole-game investigations an identity that can cross subjects | Do several finished studies justify a new collection and its maintenance/navigation cost? |

**Working recommendation:** keep the content portable in the documentation repo until the pilot has been read and tried. Then choose its site home from the actual experience. No proposed URL, schema, top-level navigation label or new category is adopted by this record. Existing Vault/Craft pages can eventually provide entry points regardless of the storage choice.

## Lives, local circumstances and routes of exchange

The [standing approach](../../specifications/game-studies.md#lives-constraints-and-place) now covers changing people, specific constraints and their costs, local circumstances and exchange. The pilot follows Russell's account of railways/electronics and theatre, Japanese films reaching a Massachusetts group, the club's controller materials and later Stanford play. These additions explain particular people and settings; they do not establish that a trauma caused a game, that a nation had one outlook or that international exchange inevitably made games alike.

Existing VC-2870 (Russell), VC-2889 (TMRC), VC-2893 (Stanford), VC-2896 (Toho) and VC-2897 (Rolling Stone) receive more precise research leads. Retained funding, shared-access and wartime-context candidates on PR #101 remain the theme homes. Tolkien's name in Brand's report also earns a coverage check and a bounded candidate lead, distinct from the existing Lord of the Rings/Shadows of Mordor game row. No issue batch, regional category or revised delivery order follows from these additions.

Later studies can ask what changed through import, localisation, licensing, migration, copying, new networks and changing markets. They need their own evidence, including local sources and language limits. The Spacewar evidence does not support filling a country-by-country comparison of Japan, Britain, Europe, the USA, South America and the Soviet bloc; it supports the specific journeys described here.

## Further static reading and visual treatment

The combined play situation brings movement, aiming and resources together before the ending sequence; alternative input mappings extend the controller discussion. A dated institutional price-list summary adds a concrete machine-access question without asserting MIT's purchase cost. Existing PDP-1, DEC and access/funding candidates remain the relevant research records; no additional candidate batch is required.

The website draft demonstrates reusable article-opening, figure and pull-quote structures in a development-only catalogue route, not an agreed new top-level Studies home. The canonical study is synced at a recorded revision. The original header artwork is labelled as illustration; game captures and explanatory diagrams retain their existing identities and credits.
