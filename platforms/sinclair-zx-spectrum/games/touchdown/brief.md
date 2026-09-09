# Touchdown — Brief

**Status:** Scope agreed on 9 September 2026; six-stage playable prototype implemented for review; lesson breakdown pending.
**System / track:** Sinclair ZX Spectrum / BASIC.
**Route:** After the published Meet BASIC and Bright Spark opening. Volley is the published intervening game; see [current work](../../../../work.md#next-output). Use the game identity rather than an inherited numbered slot.
**Target:** Stock 48K Spectrum, PAL timing, Sinclair BASIC, keyboard input, tape save/load. No expansion required.

Apply the [project charter](../../../../PROJECT.md) and [game-brief specification](../../../../specifications/brief.md).

## Experience and agreed scope

Land a small craft on a clearly marked pad within one fixed screen of uneven terrain. Gravity keeps the craft falling while the player decides when to thrust and how to move sideways. Fuel is limited. Reaching the pad and arriving gently must both matter: the landscape participates in the challenge.

A fixed starting situation lets players learn from repeated attempts. Each attempt ends in a safe landing or a collision, followed by a quick retry option. Fuel exhaustion stops the engine; it does not automatically end the attempt, because coasting to safety should remain possible. Give a clear result explaining the outcome and a way to leave the game.

The moving lander and landscape carry the experience. A compact instrument panel supplies fuel and descent speed; the craft's position makes altitude apparent. The finished game includes readable instructions, responsive controls, visible thrust, understandable collision and landing feedback, and a repeatable play cycle.

Start with direct sideways movement alongside vertical thrust. Horizontal momentum is an experiment, not a requirement. Prototype the controls and display on the target before choosing movement increments, landing thresholds, fuel quantities or terrain detail. In particular, establish how sideways control and thrust can work together.

Scrolling, multiple screens and procedural terrain are outside the initial scope. There is no fixed line limit or lesson count. A single carefully designed landing site should fulfil the complete-game promise.

## Learning role

Bright Spark waits for the player's response; Touchdown updates the world while the player decides. Introduce a continuous game loop, position and velocity, gravity and thrust, resource limits, screen coordinates and collision rules through visible consequences.

Explain the maths locally: speed changes altitude; gravity and thrust change speed. Distinguish the simulation's position from its rounded screen position. Construct the craft and landscape with the reader, explaining their representation and how the same terrain data supports drawing and contact checks.

Reinforce variables, conditions, loops, input, arrays where useful, screen placement and small reusable routines. Explain syntax at its first local use and provide enough recall for readers arriving from elsewhere. Neither Foundations nor attendance at earlier games is a prerequisite. Shared maths, design and pattern explanations can offer depth without supplying essential missing instructions.

## Graphics, sound and content

Create a small custom-character lander, a visible flame and a readable landing pad within uneven terrain. Teach how the character is drawn and represented. Select terrain representation through the prototype; favour a form whose rendering and collision behaviour readers can understand together.

Erasing and redrawing the craft must preserve the landscape and instruments. Keep craft, flame, ground and pad distinguishable without relying on colour alone. The ground and instruments must agree with the model at contact.

Use concise thrust and outcome sounds where they help. Check their effect on the update rate and controls before adopting them. Instruments remain legitimate play information; landing by colour and sound alone is not an acceptance condition. Decorative stars and elaborate explosions are optional later refinements, not initial requirements.

Create original teaching assets and retain their editable data with the maintained samples. Historical comparisons and Vault links can be added after checking their sources; they are not required to establish the mechanic.

## Runnable development sequence

These are prototype stages, not an agreed lesson count. Split or combine them according to what the working program demonstrates.

| Stage | Inspectable or playable result | New idea and changes | Check |
|---|---|---|---|
| Falling craft | A visible craft descends towards flat ground | Position, screen coordinates, erase/redraw and an updating loop | Old positions clear; craft stays within the display; contact ends the descent |
| Gravity and thrust | The player can brake the fall | Velocity, acceleration and input within the loop | Released and held thrust produce understandable movement; safe and hard contact differ |
| Limited fuel | Burns consume a visible reserve | Resource state and conditional thrust | Fuel never becomes negative; an empty tank disables thrust but permits continued flight |
| Reach the pad | Sideways control makes alignment matter | Horizontal position, screen boundaries and a landing region | Thrust and steering are usable together; edge and off-pad contact have explicit rules |
| Shape the site | Uneven terrain changes the approach | Terrain data, drawing and collision | Visible terrain matches contact; the craft cannot skip through ground between updates |
| Finish and retry | A complete landing challenge with final craft, flame, instruments and sound | Feedback, instructions, results, reset and exit | A full attempt explains its outcome; retry restores all state and remains responsive |

Introduce readable provisional graphics from the beginning and develop the final assets alongside the rules they communicate. Avoid a large unexplained graphics replacement at the end.

## Prototype and verification

The first deliverable is a playable prototype establishing whether steering towards a pad while managing descent and fuel feels responsive in 48K BASIC. Record the actual source, conversion/build command, emulator version, ROM/target configuration, controls and timing observations. Use the established sample and capture workflow after checking it still applies; no new execution is claimed by this brief.

Check at least:

- Safe landing is achievable, repeatable and requires a meaningful approach.
- Excessive descent speed, terrain contact and off-pad contact produce consistent results; define pad-edge and craft-footprint rules explicitly.
- Held, tapped, released and combined controls behave predictably, including during sounds and retry transitions.
- Screen edges, ascent above the play area, empty fuel and movement across more than one terrain position cannot produce invalid coordinates or missed collisions.
- Redrawing restores scenery; flame and instrument updates leave no debris or misleading values.
- A complete play cycle includes safe landing, crash, fuel exhaustion, retry and exit. Retry resets movement, fuel, graphics and input state.
- Saving and loading in a fresh session preserves a playable starting program.

Use actual execution for captures. Separate scripted rule checks from human observations of responsiveness, readability, sound and enjoyment. Record unverified hardware or native-input claims honestly. If the full scene is too slow, first simplify drawing and tune the update work while preserving the agreed moving craft and meaningful landscape. A substantive scope change requires discussion.

After the prototype, specify maintained runnable checkpoints and reviewable lessons. Keep detailed keyword-entry help optional and use the shared question presentation for authored prompts and explanations.

## Implementation locations and next output

Existing material is evidence to inspect, not implementation of this agreed replacement:

- Website catalogue: `website/src/content/modules/sinclair-zx-spectrum/basic.yaml`.
- Existing lessons: `website/src/content/curriculum/sinclair-zx-spectrum/basic/touchdown/`.
- Sample area: `code-samples/sinclair-zx-spectrum/basic/touchdown/`.

With Volley published, the next Touchdown work is to inspect the existing lessons and samples, build and play the bounded prototype, record configuration-specific findings, then derive the lesson/checkpoint breakdown. Separate constant-speed falling from acceleration; establish vertical landing before sideways movement, then a pad on flat ground before uneven terrain. Teach custom-character construction in a distinct, understandable step. Preserve published URLs when replacement lessons are eventually published.
