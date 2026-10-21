# The Pattern Library

A pattern is a concrete technique a reader can adapt to their own project. It explains a recurring problem, an implementation and the conditions under which that implementation is useful. Lessons provide guided complete experiences; shared modules develop concepts; the Vault supplies context.

## Agreed breadth

The Pattern Library supplies concrete techniques readers can adapt. It covers the small routines needed to get a machine doing something as well as the larger structures that grow from them: reading a key, sampling a joystick, making a sound, drawing a sprite, organising a game loop, and handling more complex behaviour and presentation. A technique does not need to originate in a game study or be an advanced design pattern.

The owner approved this scope and the direction of one conceptual technique linked to distinct implementations on 19 October 2026. Implementation and navigation details still need a bounded prototype and review. Preserve current machine entry points and published URLs; a new conceptual identity must not hide the hardware-specific work. The approved probe expansion covers all 30 machines in the current Emu198x registry, with eventual coverage of every system in the catalogue. This commissions incremental, separately qualified probes, not every routine on every machine or a bulk library rewrite. A probe does not establish a complete curriculum track.

## What belongs here

Select techniques that repay reusable treatment: for example an entity pool, a collision test, a readable opponent state machine, an input routine or a sound-priority policy. Do not turn every fragment into a pattern. A technique may belong to one machine or language; preserving those details is more useful than presenting a falsely universal form.

Each entry explains:

- The problem, a concrete use and when another approach would be preferable.
- An implementation with enough explanation to adapt it.
- Inputs, outputs, state, resource ownership and other contracts.
- Requirements, limits and trade-offs, including relevant timing and memory costs.
- What was built or executed and under which configuration; proposed code is labelled as such.
- Links to lessons showing the technique in a complete game, related patterns and useful conceptual or Vault context.

Compare plausible alternatives. Distinguish measured costs from estimates and avoid unsupported cycle counts or universal performance claims. A shorter listing is not necessarily faster. Explain what an optimisation enables for the player.

## Make it your own

Help readers adapt the routine to their own projects. Where the technique has
useful variations, include a “Make it your own” section with a small maintained
working example. Show the exact parameter, data or caller change, its visible
or measurable result, and how to confirm that it still works. Use CodeFromFile
for runnable code and retain configuration-specific execution evidence.

Explain the editable inputs, data layout and bounds. State the effect on code,
assets, scratch memory and runtime or transfer work where it matters. Prefer a
concrete before-and-after comparison to “experiment with these values”. Do not
add a variation solely to fill a quota.

Distinguish edits that preserve the existing contract from extensions that need
new design and verification. Replacing a glyph inside its allocation differs
from changing a kernel's scanline schedule; more display-list objects need RAM
and DMA bandwidth. Name those boundaries, including resource ownership and
incompatible neighbouring routines. Link advanced alternatives when they exist,
and label unimplemented directions honestly. Keep the original working example
easy to find. Customisations deepen an entry; they do not automatically become
separate patterns or additional coverage claims.

## Common mistakes and their symptoms

Where a failure reveals something useful about the technique, show a small,
verified example alongside the working implementation. Choose recognisable
mistakes rather than filling a quota. Help readers diagnose their own programs:

- Describe what the reader sees, hears or measures, and show a verified capture,
  trace or other suitable evidence when it makes the symptom clearer.
- Explain the cause in terms of the routine's contract and the machine's
  behaviour. Distinguish the observed result from other possible consequences.
- Show the smallest clear correction, using maintained wrong/fixed fragments,
  and explain how to confirm the fix with the working example.

Label deliberately broken code before the listing. Keep it separate from the
reusable implementation and normal download. Use a bounded reproduction that
cannot be mistaken for the recommended routine. Verify that the faulty example
actually ran and produced the stated symptom; a crashed loader or incomplete
call is not evidence of the intended fault. Check the repaired path too.

A still image may hide a timing fault, redundant fetch or intermittent failure.
Say so, and use a measured counter, trace or animation when appropriate. Do not
claim television instability from an emulator still, or generalise one
configuration's behaviour to every machine. Keep the known-good result easy to
find and state the tested tools, configuration and limits with the example.

## Files and schema

Entries live under the website's `src/content/patterns/`. Published routes follow `/patterns/{system}/{track}/{category}/{slug}/`, with cross-platform entries under `/patterns/cross-platform/{category}/{slug}/`.

The current schema requires `title`, `summary`, `platform`, `category` and `difficulty`. Platforms accepted by the loop expansion are `commodore-64`, `sinclair-zx-spectrum`, `commodore-amiga`, `nintendo-nes`, `bbc-micro`, `acorn-electron`, `sega-master-system`, `sega-game-gear`, `sega-sg-1000` and `cross-platform`. Categories are `rendering`, `input`, `audio`, `physics`, `ai` and `framework`; difficulty is `beginner`, `intermediate` or `advanced`.

`taught_in` is an optional string, tags default to an empty array, and optional `evolution` and `related` objects carry neighbouring patterns and Vault links. Check `src/content.config.ts` and current route helpers before authoring these fields. Extending the curriculum to another system may require a deliberate schema change; the current enum does not define the project's ultimate scope.

Runnable code follows [Code samples](../website.md#code-and-artefacts). Schematic pseudocode is labelled and follows the shared [notation](pseudocode.md). Link both ways between a pattern and its lesson where useful. Confirm links and rendered code, and retain machine-specific assumptions rather than hiding them behind a “production-ready” label.

## Independent entry points and progression

Readers can look up one immediate job or follow a useful progression. Explain the local prerequisites and offer onward steps; do not turn the library into another compulsory course. A basic routine can be a complete, valuable entry. Build complexity by showing what a later technique adds, what it assumes and what it costs.

| Area | Small starting jobs | Useful later work |
| --- | --- | --- |
| Input | Read a key or a joystick/controller state; interpret bit masks and active states | Distinguish held/newly pressed/released input, deliberate repeat, action mapping, analogue ranges, buffering and recording |
| Sound and music | Make a beep or tone, trigger and release a note, play a sample | Non-blocking effects, envelopes and noise, voices/channels, sequencing, mixing and streaming where supported |
| Graphics and animation | Place a character or pixel, load a palette, draw or move a sprite | Tiles and maps, animation, scrolling, dirty regions, multiplexing and display-time effects where supported |
| Time and execution | Update a counter, wait for an appropriate event, structure an update loop | Separate clocks, schedule work, handle interrupts, budget work and compare frame-dependent with elapsed-time behaviour |
| Movement and collision | Move within bounds, test a tile or rectangle, represent position and velocity | Fixed-point motion, swept tests, spatial queries, camera relationships and deliberate update order |
| Data and memory | Index a table or grid, represent a small entity, copy a block safely | Pools, queues, compact formats, allocation strategies, compression and data-oriented update choices |
| Behaviour and rules | Test conditions, switch state, choose a target or legal neighbour | Perception and memory, routes, priorities, coordination, search and reusable rule/data representations |
| Storage and tools | Read or write a small format and prepare one usable asset | Loading, banked resources, conversion pipelines, save data, debugging, profiling and measured optimisation |

These are coverage directions, not assertions that all examples exist or work on every machine. Develop a branch when a concrete reader need, lesson, study or hardware capability warrants it. Keep higher-level presentation and production questions connected to useful implementations without forcing them into routine-shaped entries.

## Explain the operation and the intended result

Distinguish the layers without making one a lesser form of content:

- A hardware operation reads or writes a particular interface under stated conditions.
- An adaptable technique solves a recurring problem and identifies its assumptions.
- An implementation realises it on a particular machine, language and toolchain.
- A worked example makes the result visible or audible and shows how to integrate it.

For input, knowing that a button is down differs from deciding that one action should occur. For audio, setting up a voice differs from timing an effect while play continues. Link those jobs explicitly. Different machines may require materially different implementations, expose different capabilities or make the same apparent behaviour cost different amounts. Do not disguise those differences behind generic pseudocode.

The Craft explains intent and judgement: how a control feels, why an opponent anticipates a player, or why delayed feedback is understandable. The library explains adaptable mechanics. System tracks teach their use within growing games; Foundations explains general programming concepts; the Vault supplies historical context. Link where useful rather than duplicating a canonical explanation across all of them.

## Code first, with a route into a project

Usable machine-specific code is the centre of each entry. Show how to include, initialise and call the routine, explain its inputs, outputs, state and resource ownership, and show how it connects to other routines in a small project. Interactive examples support that explanation; they do not replace the reusable implementation.

## Entry contract and evidence

Use the smallest form that serves the job. State the intended result early, name the machine/variant and language, and show the routine or refer to maintained code in code-samples. Explain inputs, outputs, representation, clobbered registers or shared state, memory ownership, timing assumptions and integration obligations where they matter. Address interactions with operating-system routines, interrupts and other users of the same hardware when relevant. Avoid ceremonial fields that add nothing.

Claims about hardware use the project's primary-reference and synthesis workflow. Existing listings are not automatically verified because they resemble a familiar idiom. Distinguish illustrative code, assembled code, observed execution on an identified configuration, and original-hardware checks. Give cost estimates a basis; distinguish estimates from measurements. Small routines need observable outcomes too: one button event rather than repeated events while held, the intended sound while the rest of a program keeps running, or a bounded write that leaves neighbouring data intact.

Do not silently upgrade an entry's evidence status or preserve an obsolete lesson number as proof of coverage. Improve or extend an existing entry before creating another under a different label.

## Discovery and the first prototype

Support both “read this machine's joystick” and “make one press cause one action”. A reader should be able to start from a familiar task without already knowing a technical name. Keep direct machine/language access alongside task-oriented discovery. Basic and advanced work belong in the same library, with useful onward relationships instead of a misleading universal ladder.

Prototype with existing input-state reading, input-edge detection, a basic sound trigger, and one study-derived technique. This deliberately includes routines that have value independently of the studies. Audit existing bodies, relation fields and incoming links first; do not create a second keyboard or joystick article merely to populate a new structure.

Before choosing a schema or migrating the catalogue, demonstrate that readers can find a small hardware operation, reach an appropriate implementation, distinguish it from an illustrative listing, identify a sensible next technique and follow old URLs. Check keyboard access, narrow/wide layouts, searching without JavaScript and representation of more than one machine or language. Keep the existing catalogue usable throughout.

The [accepted study-theme direction](../plans/2026-10-19-study-themes-and-library-scale.md) provides concrete Craft candidates. Approval of this scope does not claim that a new lesson, taxonomy, interface or implementation has shipped, and leaves the charter's current delivery priorities intact.


## Coverage before a complete track

A machine can gain a qualified reusable technique before it has a full curriculum track. Pattern discovery uses actual entries to avoid empty machine facets; a new pattern does not change the system’s curriculum readiness tier. Keep the machine identity explicit and retain the direct machine/language routes.

The [game-loop comparison and qualification notes](../guides/game-loops.md) explain the first slice: four core implementations, a MOS-facing BBC Micro caller, and separate Electron execution of the shared source. Keep code, contracts and records together. A passing example establishes the named workload and startup route, not every facility of its emulator.


## Progression, clocks and presentation

Treat these as separate choices that readers can combine:

- **Progression:** an accepted command, a completed turn, a simulation step or an event changes the game state.
- **Time:** an optional clock measures elapsed time, schedules an event or imposes a deadline. Turn-based games may have timed turns; real-time presentation can accompany an untimed decision.
- **Input:** a blocking command reader, a polled state, a new-press event or buffered input determines when an action is accepted.
- **Presentation:** redraw after a change, animate independently or synchronise display work with a safe hardware boundary.

Do not force a frame wait into an untimed input/output game. Equally, do not describe turn-based games as inherently timer-free. Show how a deadline can cause a turn transition, how an action restarts or preserves that deadline, and how display/audio servicing continues while waiting where needed. State the ordering when an action and expiry coincide.

Probe coverage is incremental. Track every registry machine explicitly, retaining its machine-to-crate join. Separate planned, built, executed and qualified records; retain source, tool and configuration identities and a failing control for each claimed behaviour. Shared CPU or display ancestry does not replace separate execution. Broader catalogue machines remain future targets until a runnable path exists.
