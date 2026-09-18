# Code198x: purpose and direction

> You can understand the machine—and use that understanding to make things.

Code198x is developing a comprehensive games development and programming curriculum. Vintage computers give us environments small enough to understand how the pieces work together: how a variable is represented, how a loop executes, how pictures and sound become data, and how a program communicates with hardware.

We explain both how and why. Opening an abstraction should also explain why people built it, what it makes easier and what it costs. Readers should become comfortable moving between levels of detail and choosing the right one for a task. That understanding should remain useful when they return to modern hardware, languages and tools.

The purpose is understanding, creation, investigation and informed choice. Historical practice provides evidence and possibilities; it does not require us to reproduce old games or stop at original hardware configurations.

## Audience and voice

We write for children, parents and teachers, while respecting adults and experienced programmers. Clear explanations make the material accessible; childish language and assumed prior attendance do not.

The early layers take an Usborne-style approach: approachable, concrete, economical and inviting. Technical depth can grow without changing that respect for the reader. Use British English and “program” for computer software. The detailed editorial standard is [Writing voice](specifications/writing-voice.md).

## Scope across systems

The family covers computing from the 1960s through the early 2000s, with the 1970s and 1980s at its centre of gravity. Coverage is worldwide. Cultural, geographic, commercial, state-supported, socialist-bloc, kit, DIY and hobbyist-import contexts can explain different engineering choices and experiences.

Consider period, cultural and geographic coverage, support surface, form factor and role, and distribution or political-economic context when choosing a subject. A home computer, console, handheld, kit or workstation need not teach the same things.

Name the support surface precisely. Curriculum coverage, an emulator that boots a variant, and an assembler that supports its CPU are different capabilities. A system's presence in the Vault or systems directory does not prove any of them.

The Spectrum is our first re-specification focus, not the destination every learner should choose or the template other systems must follow. C64, Amiga and NES tracks already provide other approaches. Wider systems enter through a concrete teaching purpose, not through a requirement to duplicate every existing game or language route.

Use BASIC or FORTH where the machine provides an appropriate environment. Where it does not, begin with assembly. C and C++ may become relevant later; they are not the present track-development priority.

## A connected curriculum

- **Lessons** guide readers through making things in meaningful stages.
- **Foundations** develops language-neutral programming concepts in pseudocode, including representation and reasoning about execution.
- **Maths for Games** develops mathematical tools through game problems, without becoming an upfront prerequisite course.
- **The Craft** develops game design, behavioural intent and practical game-making judgement in a language-neutral way.
- **System tracks** implement those ideas in concrete languages, tools and hardware.
- **The Vault** supplies encyclopaedic historical, cultural and technical context.
- **The Pattern Library** supplies concrete techniques readers can adapt, with their assumptions and trade-offs.

These are responsibilities, not a mandate to create a top-level module for every subject. [Curriculum design](specifications/curriculum.md) places the shared subjects and explains progression. Existing navigation and authored content are evidence of implementation, not limits on the intended coverage.

## Public presentation and publishing

The website should make its purpose and routes clear to a first-time visitor. Prefer familiar, descriptive navigation labels over invented names. Use “Systems” for the machine directory. Editorial series may have distinctive names, but their introductions and links should explain what readers will find. Review names in context rather than renaming every resource at once.

Use graphical touches to illuminate the subject: verified game captures, readable diagrams, asset studies and small visual experiments. Each should show something worth noticing or making. Preserve the House UI’s clear typography, accessible contrast and space for reading; avoid adding generic retro decoration to every page.

Keep the About page centred on the promise, audience and learning approach. Distinguish current material from intended coverage, explain independent entry points and describe verification honestly. Personal history supports the mission without replacing it.

Publishing includes the curriculum and its supporting editorial pages. Consider **What’s New**, **From the Metal** and **Field Notes** whenever substantial work produces something useful to share. Choose the format to suit the evidence and reader benefit; not every change needs three articles. [Website and publishing workflow](website.md#editorial-updates) defines their responsibilities.

## Entry and progression

Readers may enter from another Code198x system, another language or outside experience. Spectrum BASIC requires neither Foundations nor assembly. Spectrum assembly requires neither BASIC nor Foundations. Shared subjects support readers when relevant.

Distinguish knowledge an example uses from lessons someone must have attended. Explain enough locally to continue, briefly recall a concept and offer a useful link for depth. Avoid both unexplained jumps and repeated full courses inside each track.

Within a game, provide a guided development sequence. Readers are not expected to invent independent projects as a condition of learning. Programs grow understandably; necessary files generally come from preceding work. Explain any supplied code and how it fits before readers must depend on it.

## What makes a finished game

A game should be complete, enjoyable, readable, responsive and deliberately finished for its agreed scope. BASIC games in particular need not meet commercial standards. A single room, a small puzzle or a short session can fulfil a worthwhile promise.

Choose failure and retry behaviour to suit each game. A reachable losing state is not compulsory: puzzles, creative games and exploration projects can provide meaningful decisions and satisfying outcomes without one. Where failure serves the experience, explain its purpose, consequences and recovery. This principle does not automatically remove failure mechanics from existing designs.

Selected later projects can be substantially more ambitious. Their scope must serve their experience and teaching, not match a commercial price tier or feature census. Assembly does not automatically require commercial scale.

Programming, design, graphics, sound and finishing develop together. Appropriate treatment matters more than equal quantities: deliberate silence or a small visual vocabulary can be a design choice. Runnable intermediate stages can be incomplete; a claimed finished game must fulfil its stated scope.

There are no fixed game counts, unit counts or universal language progressions. Historical games can inspire, explain or provide comparisons; a canonical ancestor is not a condition for a new teaching project. Reusing a mechanic across systems is welcome when it makes a useful contrast.

The basis of a [Spectrum performance-revisit thread](platforms/sinclair-zx-spectrum/basic/performance-revisits.md) is agreed: extend existing BASIC games until a chosen experience exposes measurable limits. This thread is deferred while the initial BASIC versions and their teaching sequences take priority. Compare algorithm and representation changes, bounded machine-code helpers and full assembly implementations where evidence warrants them. Specific experiments and ports remain proposals; neither deeper games nor completion of BASIC implies a compulsory move to assembly.

## Threads to keep visible

**Representation and approximation:** numbers, text, images and sound as data; precision, rounding, overflow and sampling.

**Time and coordination:** the CPU, display, sound and peripherals operate on different schedules. Their deadlines and communication shape programs.

**Interfaces and contracts:** routines, asset formats, build tools and devices agree on what data means. Make those agreements visible.

**Experimental reasoning:** predict, observe, explain discrepancies and revise the model. Code, documentation, hardware variants and emulators can all contain surprises or faults.

**Human engineering:** people made these systems under real constraints. Preserve their mistakes, compromises, collaboration and ingenuity without inventing motives or convenient origin stories.

## Present-day relevance

Make specific connections where they illuminate the work: algorithm costs and responsiveness; representation, allocation and data movement; frame and audio deadlines; input latency; bandwidth and buffering; shared-resource scheduling; asset size and decoding; interrupts and asynchronous events; cross-development and deployment targets; debugging and measurement.

Explain the limits. Fewer instructions do not automatically mean less energy, smaller code need not run faster, and an optimisation for one architecture may hurt another. Connect efficiency to what it enables: richer behaviour, smooth animation, better sound, predictable response or opportunities to save energy. Do not add a repetitive relevance sidebar to every lesson.

## Hardware configurations and cross-development

Separate the host used to develop a game from the target required to run it. Explain source, built output, asset conversion, assembly, emulation and transfer. Build-time convenience does not add runtime hardware capabilities.

Teach development on the target, historical cross-development and the modern workflow when relevant. Historical examples must be specific and sourced, including hobbyist and professional practice where evidence permits; workflows evolved during a machine's lifetime.

Original configurations are useful starting points, not permanent limits. For an expansion or modern peripheral, specify what it provides, what the original machine still does, how they communicate, which constraint changes and where the new bottleneck appears. Keep stock, expanded and successor-machine claims distinct.

## Evidence and responsible history

Check technical and historical claims against reliable sources, preferring primary evidence where appropriate. Identify the original publication, author, edition, issue, page, section or other precise locator so a claim can be checked. Public material, including open-source repositories, must cite the original source or relevant public pages, not private research locations or unavailable local collections.

Distinguish proposed design, source-checked claims, code that builds, behaviour checked by execution and behaviour checked only in a named emulator or hardware configuration. Tool or repository existence is not evidence that an execution integration is available.

For people and organisations, distinguish established facts, recollections, disputed accounts, allegations and interpretation. Do not invent dialogue, motives or anecdotes. Acknowledge documented wrongdoing proportionately without sensationalising it or treating technical achievement as an excuse. Use age-appropriate language without concealing relevant facts. Avoid unsupported “first”, “invented by” and single-author origin stories.

## Licensing

Original Code198x prose is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0), permitting reuse and adaptation, including commercial reuse, with the required attribution and notices. [LICENSE.md](LICENSE.md) defines the scope and exclusions. Executable code, media, marks, inherited material and third-party works retain their separate terms; the maintained code-samples repository uses MIT. New original prose contributions use CC BY 4.0 unless another arrangement is explicitly agreed and recorded.

## Current work and authority

The immediate task is to re-specify the ZX Spectrum BASIC and assembly game sequences, then develop the lessons from agreed specifications. Retain, reshape or replace existing choices for their appeal, teaching value and suitability. The [Meet BASIC module direction](platforms/sinclair-zx-spectrum/basic/meet-basic.md) is agreed: a guided introduction through short projects, leading into Bright Spark and Touchdown. All fifteen Meet BASIC lessons are published: Story Builder, Lucky Number, Oracle Stone and the movement experiment. Bright Spark’s seven replacement lessons are published. The [Touchdown scope](platforms/sinclair-zx-spectrum/games/touchdown/brief.md) is agreed: a moving lander, sideways control and thrust, limited fuel, and a landing pad in one fixed screen of uneven terrain. Volley is agreed as the smaller bridge before Touchdown. Its approved eight lessons and module overview are integrated into the website, with verified source checkpoints. The opening is Meet BASIC → Bright Spark → Volley → Touchdown → Sonar: continuous updates and contact precede acceleration, fuel and terrain, followed by turn-based spatial deduction. Touchdown’s approved eleven lessons and overview are integrated, with sixteen verified teaching checkpoints and a separate keyboard diagnostic. The public course distinguishes this opening from earlier games and the optional BASIC reference. Standalone Story Builder, Lucky Number and Oracle Stone lessons are retired in favour of their Meet BASIC replacements, with old URLs redirected by topic. Reflex, Hi-Lo and Quiz Master are retired from Spectrum BASIC. Sonar follows Touchdown: turn-based spatial deduction extends Touchdown’s one-dimensional terrain array into a board. Its [replacement scope](platforms/sinclair-zx-spectrum/games/sonar/brief.md) is one target on an 8×8 grid, remembered near/medium/far clues, distinct-probe counting and random rounds, with no probe limit. The banded prototype was accepted after native play; a larger grid remains an optional extension. The [teaching implementation](platforms/sinclair-zx-spectrum/games/sonar/lessons.md) has eleven executed checkpoints and nine approved lessons published on the website, with legacy URLs redirected by topic. Crates follows Sonar; its [agreed scope](platforms/sinclair-zx-spectrum/games/crates/brief.md) is three original 8×8 push puzzles focused on changing a grid safely, without retaining its former finale role. All three rooms and the revised visual direction are accepted after native play. The [lesson brief](platforms/sinclair-zx-spectrum/games/crates/lesson-brief.md) defines eleven lessons; thirteen [executed teaching checkpoints](platforms/sinclair-zx-spectrum/games/crates/lessons.md) now support that plan. The approved replacement overview and eleven lessons are published after Sonar as game 5, including the textual goal cue, maintained samples and topic-based redirects from the six older lessons. Tail Chase’s [prototype](platforms/sinclair-zx-spectrum/games/tail-chase/prototype.md) is accepted after native play as the next game under development: a continuous moving body grows from four to twelve cells by eating eight foods. Its [teaching progression](platforms/sinclair-zx-spectrum/games/tail-chase/lesson-brief.md) has twelve verified checkpoints and ten approved lessons published after Crates, with a final source identical to the accepted prototype and live publication checks passed. Brick Bash follows Tail Chase with the agreed scope: one pixel-moving ball, a horizontal paddle and eighteen bricks. Its [execution record](platforms/sinclair-zx-spectrum/games/brick-bash/prototype.md) records fourteen scripted checks and native feedback that it works and is surprisingly tough. The user agreed to retain this baseline and develop the [teaching progression](platforms/sinclair-zx-spectrum/games/brick-bash/lesson-brief.md); nine [executed checkpoints](platforms/sinclair-zx-spectrum/games/brick-bash/lessons.md) now support the agreed ten-lesson basis, with the final source identical to the native prototype. The approved overview and ten website lessons are published after Tail Chase as game 7, with live publication checks passed. The user accepted [Drift](platforms/sinclair-zx-spectrum/games/drift/brief.md) after successful native docking with the revised velocity readout. Its [eight-lesson progression](platforms/sinclair-zx-spectrum/games/drift/lesson-brief.md) now has [six executed checkpoints](platforms/sinclair-zx-spectrum/games/drift/lessons.md), preserving the accepted final source. The approved overview and eight website lessons are published after Brick Bash as game 8, with live publication checks passed. The user accepted [Quickstep’s six-lane BASIC baseline](platforms/sinclair-zx-spectrum/games/quickstep/brief.md) after native play: six predictable hazard lanes, one halfway resting strip and one exit. Its [ten-lesson progression](platforms/sinclair-zx-spectrum/games/quickstep/lesson-brief.md) now has eight [executed checkpoints](platforms/sinclair-zx-spectrum/games/quickstep/lessons.md), growing a one-lane crossing into the accepted game. Exact editing transitions and 96 execution check groups pass, with an identical final source. The user-approved overview and ten lessons are published after Drift as game 9. The production build, 44 desktop/mobile browser checks and live publication checks pass. Further BASIC choices and the remaining assembly lineup remain proposals. The agreed current BASIC navigation groups are First programs (Meet BASIC and Bright Spark), Movement and control (Volley and Touchdown), Boards and deduction (Sonar, Crates, Locksmith and Three in a Row), and Worlds that keep moving (Tail Chase, Brick Bash, Drift and Quickstep). They preserve the current order and independent entry. The [remaining-course review](platforms/sinclair-zx-spectrum/basic/course-review.md) assesses six earlier games and eleven inherited proposals; its recommendations are not an adopted lineup. The user selected Locksmith next; its [bounded brief](platforms/sinclair-zx-spectrum/games/locksmith/brief.md) defines a four-digit code over 1–6, repeated digits, exact/other clues and a ten-guess prototype. The user accepted the native trial; its [execution record](platforms/sinclair-zx-spectrum/games/locksmith/prototype.md) records the verified baseline. Its [nine-lesson progression](platforms/sinclair-zx-spectrum/games/locksmith/lesson-brief.md) now has seven [executed checkpoints](platforms/sinclair-zx-spectrum/games/locksmith/lessons.md), with 80 passed check groups and an identical final source. The user-approved overview and nine replacement lessons are published in Boards and deduction after Crates, preserving numeric identities. The production build, 40 desktop/mobile browser checks and live publication checks pass. The user selected Three in a Row for an opponent-design review. Its [source review](platforms/sinclair-zx-spectrum/games/three-in-a-row/review.md) finds a concrete fork that defeats the retained policy. The [proposed prototype](platforms/sinclair-zx-spectrum/games/three-in-a-row/brief.md) focuses on a deliberately fallible opponent with visible move reasons; the user authorised its implementation. The [prototype](platforms/sinclair-zx-spectrum/games/three-in-a-row/prototype.md) is accepted after native play; the user reported that it works well and mostly draws. They authorised the [ten-lesson teaching progression](platforms/sinclair-zx-spectrum/games/three-in-a-row/lesson-brief.md), preserving the accepted difficulty. Eight verified checkpoints now support the user-approved overview and ten replacement lessons, published in Boards and deduction after Locksmith. Production, browser and live publication checks pass.

The website catalogues, lesson files, sample sources and Git establish what exists. A plan is not an implementation, a catalogue entry is not execution proof, and a future subject is not an authored module. The October 2026 launch target and four initial system on-ramps remain planning context, not evidence of completion or a boundary on the curriculum's purpose.

This charter is the current Code198x direction under the family [Principles](PRINCIPLES.md). Specifications explain how to apply it. When intent changes, edit the relevant current document and explain why in the pull request; do not maintain a competing policy or a chain of amendment banners. Git preserves prior decisions. Narrow technical specifications and game briefs must identify their status and cannot silently override this charter.

The user selected [The Caverns](platforms/sinclair-zx-spectrum/games/the-caverns/brief.md) next for a small BASIC exploration prototype. The first trial uses named rooms, directional clues, a fixed patrol with an escape turn on arrival, and three treasures to return to the entrance. The [native game](platforms/sinclair-zx-spectrum/games/the-caverns/prototype.md) is accepted. The user authorised its [ten-lesson progression](platforms/sinclair-zx-spectrum/games/the-caverns/lesson-brief.md), using eight runnable checkpoints and preserving the final source. The approved replacement lessons are published in Hidden worlds, with production and live checks passed. See the [implementation record](platforms/sinclair-zx-spectrum/games/the-caverns/lessons.md).
