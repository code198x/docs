# Volley — Brief

**Status:** Proposed specification for review. A smaller game before Touchdown is the preferred direction; this detailed design and the final order await prototype and teaching-stage review.
**System / track:** Sinclair ZX Spectrum / BASIC.
**Working route:** Meet BASIC → Bright Spark → Volley → Touchdown.
**Target:** Stock 48K Spectrum, PAL timing, Sinclair BASIC, keyboard input and tape save/load. No expansion required.

Apply the [project charter](../../../../PROJECT.md), [curriculum design](../../../../specifications/curriculum.md) and [game-brief specification](../../../../specifications/brief.md).

## The game

Keep a ball in play with one vertically moving paddle on the left of a fixed court. The top, bottom and right walls return the ball. The left edge is open except for the paddle. Each successful paddle return adds one to the rally; a miss ends it. Show the result and offer an immediate new rally or exit.

The recurring activity is to read the ball's path, move to intercept it and recover for the next return. A fixed starting serve supports learning through repeated attempts. The score makes improvement visible without requiring a campaign or a target score to finish the game. A complete rally-and-retry cycle is the endpoint.

Use a modest paddle length and fixed ball speed, selected through playtesting. Begin with simple diagonal movement and reflection. Whether this creates an enjoyable challenge is a prototype question: if the trajectory repeats too predictably, do not quietly add spin, acceleration or random deflections. Compare a small, explicitly taught return rule with the simpler version and review its teaching cost before adopting it.

No opponent AI, second player, levels, increasing speed, gravity, fuel or terrain. No custom-character construction is required: build a deliberate court, paddle and ball from readable existing characters. There is no fixed line limit or lesson count.

## Why it sits here

Bright Spark combines stored data, playback, responses and round state. Volley changes one central relationship: the world continues to update while the player acts. Ball movement continues when no key is pressed; input changes the paddle, not whether the program advances.

The new ideas are position changing by a fixed step, direction represented by signed values, boundaries, simple overlap and a consistent input/update/draw cycle. Touchdown can then recall these while introducing changing velocity, limited fuel and meaningful terrain.

Treat this as a hypothesis about progression, not proof supplied by a shorter program. Collision order and redrawing can hide substantial complexity. Trace them locally and split stages when two unfamiliar relationships arrive together. Do not introduce a general game engine, vector library, fractional movement or unexplained starter code.

Recall variables, conditions, repetition, keyboard input and screen placement as needed. Explain syntax and coordinate conventions locally. Readers arriving from outside the preceding games should be able to start without completing Foundations or borrowing an unexplained file from Bright Spark.

## Proposed rules and representation

Use a character-cell court with an instrument row outside the moving area. Start with integer row and column positions and a one-cell ball. Horizontal and vertical direction values express the next step; changing a sign reverses that part of the movement. Explain that screen rows increase downwards before using signed vertical movement.

Represent the paddle by its column, top row and length. Its occupied rows form an inclusive interval. Clamp movement so the entire paddle stays inside the court. Two documented keys move it up and down; holding a key continues movement. Choose the actual keys after checking native keyboard and emulator behaviour. Joystick support and simultaneous-key reading are not needed for this game.

Make the collision convention explicit in the prototype: read input and update the paddle, calculate the ball's candidate position, resolve wall/paddle contact, then draw the resulting state. A return counts only while the ball approaches the paddle. Define which row is tested and how a simultaneous wall-and-paddle contact is resolved; a visible edge hit must agree with the stated rule. One-cell steps keep the first model inspectable, but do not by themselves prove its corner cases correct.

A missed paddle ends the rally before the ball can produce an invalid screen coordinate. Retry resets positions, direction, score and the display; a held answer key must not accidentally start several rallies. A deliberate serve action gives the player time to get ready.

## Graphics, sound and pacing

Teach the court layout and why the ball, paddle and score occupy distinct regions. Select high-contrast characters and colours; collision and results remain understandable without colour or sound. Show how to erase moving objects without damaging walls or leaving fragments of the paddle.

Use silence during ordinary travel. Short return and miss sounds are candidates for feedback, subject to checking their effect on timing and controls. Keep scores legible and updates restrained. Smoothness is judged in the actual 48K BASIC program; fixed movement steps do not imply a measured constant wall-clock speed.

Any pacing delay must be examined under held and tapped input and with sound enabled. Document the actual behaviour rather than calling an arbitrary loop a reliable frame timer. Simplify drawing before introducing a timing system that overwhelms the lesson.

## Runnable development sequence

These are teaching groups to test, not a mandated number of lessons. Each checkpoint must run and support a prediction or explanation before adding another rule.

| Stage | Runnable result | Main new understanding and changes | Check or question |
|---|---|---|---|
| Place and move a ball | A ball crosses a blank play area horizontally and stops at its edge | Position, fixed steps, erase/redraw and a continuous loop | Predict its position after three updates; explain why the old ball disappears |
| Return from a wall | The ball travels back and forth | Signed direction and boundary decisions | Trace the positions around contact; why must direction change only at the boundary? |
| Travel around the court | Diagonal travel reflects from top, bottom and right walls, initially with a temporary left wall | Two coordinates and independent direction changes | Predict a corner bounce; explain which direction changes at each wall |
| Move the paddle | A paddle moves within the court while the ball continues its demonstration | Polling input during updates and clamping a multi-cell object | Compare held, tapped and absent input; why is the paddle's top limit different from its bottom limit? |
| Keep a rally going | Replace the temporary left wall with paddle contact and a miss outcome | Interval overlap, approaching direction and update order | Trace a centre hit, an edge hit and a miss; ensure one contact causes one return |
| Finish and retry | Instructions, serve, rally score, clear result, retry and exit complete the game | Recall counters and state/reset patterns; integrate feedback | Play, miss, retry and exit; check no score, input or screen state leaks into the next rally |

Scoring and retry recall ideas already explained in the opening course, but still need enough local explanation to follow their implementation. Keep detailed keyword-entry help optional. Use the shared question presentation for prompts and explanatory answers; do not make progress depend on a quiz score.

## Prototype and acceptance

Build a bounded prototype before writing replacement curriculum pages. Record exact BASIC sources, conversion/build commands, emulator release, ROM/target configuration, controls and observations. Keep source checkpoints and any original asset data in the sample repository; produce a loadable tape and verify saving/loading through the chosen learner workflow. Host conversion is a development convenience, not a runtime expansion. Check the established workflow before promising particular tools or integration.

Verify:

- Ball motion continues without input, stays within valid coordinates and reflects correctly at each wall and corner.
- Paddle limits account for its full length; redraw preserves court boundaries and leaves no debris.
- Centre and inclusive edge hits return the ball; just-outside hits miss. A return increments the score once and cannot repeatedly reverse a departing ball.
- Held, tapped, unrelated and released keys behave consistently during travel, feedback sounds, serve and retry.
- The full cycle works across several rallies: instructions, serve, returns, miss, result, retry and exit. Fresh-process tape loading produces a playable program.
- Captures come from actual execution. Visual inspection and listening accompany scripted rule checks; record original-hardware and native-input coverage separately.

Human playtesting must answer whether the ball is readable, the paddle responds soon enough, recovery between returns feels fair and another rally is appealing. Test the fixed trajectory for an effortless stationary-paddle strategy and for excessive repetition. A technically correct but dull rally does not meet the brief.

The teaching review must identify the new concepts at each checkpoint, the explanations and traces they need, and what transfers to Touchdown. If satisfactory play requires substantially more physics, timing machinery or collision complexity, reconsider this bridge before confirming the course order. Preserve the smaller teaching role rather than accumulating features by default.

## Sources, connections and current evidence

The existing website catalogue has a coming-soon Volley entry tagged “Paddle physics”. No Volley lesson directory or sample files were found in the inspected curriculum and sample trees when preparing this brief. That catalogue entry does not establish a playable implementation or an approved scope.

Implementation locations:

- Existing catalogue: `website/src/content/modules/sinclair-zx-spectrum/basic.yaml`.
- Intended lesson area: `website/src/content/curriculum/sinclair-zx-spectrum/basic/volley/`.
- Intended sample area: `code-samples/sinclair-zx-spectrum/basic/volley/`.

Potential shared connections are position/direction, the game loop, boundary and overlap checks, readable feedback and retry design. Verify specific authored pages before linking; the local lessons must contain the essential explanations. Extract reusable patterns only from the working game. Historical comparisons are optional and need original, checkable sources; this proposal makes no historical origin claim.

Next output: a review of this brief, followed by the bounded prototype and a checkpoint/concept comparison with Touchdown. No implementation or execution is claimed here.
