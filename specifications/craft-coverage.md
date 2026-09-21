# The Craft — module responsibilities and coverage

Apply [curriculum design](curriculum.md). This map records agreed direction and
module boundaries. It is not a published catalogue, lesson count or
commitment to complete every topic before another system game can be written.

## Direction and status

The user considers the revised Spectrum BASIC curriculum a solid basis, while
recognising that further concepts could earn a place. Develop the shared subjects
and review the Z80 assembly opening rather than fill every remaining BASIC
proposal. Assembly remains an independent entry route; performance comparisons
and ports are separate choices.

Maths for Games should develop geometry, trigonometry, vector and matrix algebra,
3D, curves and surfaces as well as probability, with recurring fixed-point
applications. The [maths coverage specification](maths-for-games.md) owns that
scope and the relationship to the graphical-mathematics reference supplied by
the user.

The seven modules below are agreed homes within The Craft. Public overviews
distinguish available lessons, outlines and prototypes from planned modules.
Agreement on a home does not mean its lessons exist or have been approved.

| Module | Status | Central responsibility |
|---|---|---|
| Maths for Games | Existing module; broader direction agreed | Explain mathematical relationships and their use in games, including numerical representations and approximations |
| Game AI | Separate module within The Craft agreed; lessons not authored | Explain how entities perceive, remember, decide, move and coordinate |
| Game Feel | Broader outline and movement prototype in local review | Controls, responsiveness, anticipation, feedback, forgiveness and the moment-to-moment experience |
| Game Design | Agreed module; lessons not authored | Rules, goals, choices, resources, challenge, levels and progression; why a functioning game is interesting |
| Game Data and Algorithms | Agreed module; lessons not authored | Represent game worlds and entities; compare operations, algorithms and their costs |
| Graphics and Animation | Agreed module; lessons not authored | Create images and animation; connect pixels, sprites, tiles, palettes, fonts and rendering to the intended result |
| Sound and Music | Agreed module; lessons not authored | Create effects and music through rhythm, melody, synthesis and arrangement, connected to hardware facilities |

Cameras, collision, physics and procedural generation begin as connected
sequences in these modules. Give one a separate home only when developed
material and reader navigation warrant it. These boundaries do not impose a
single course order.

## Game AI

The organising question is: **how does an entity perceive its situation and
choose what to do?** Explain behaviour and decision-making early. Machine
learning is not a prerequisite and is not part of the initial commitment.

| Area | Coverage | Possible experiment |
|---|---|---|
| Patterns and states | Patrols, reactions, states, transitions and timing | Change when a guard pauses, looks around and resumes its route |
| Perception and knowledge | Sight, hearing, limited knowledge, memory and belief | Hide after being seen; compare pursuit of the current position with search around the last sighting |
| Movement and navigation | Pursuit, escape, steering, avoidance, graphs and pathfinding | Put a wall between a pursuer and its target and compare movement with route finding |
| Action selection | Conditions, priorities, utility scores, weighted choices and stability of decisions | Inspect the competing scores for attacking, retreating and seeking cover |
| Looking ahead | Game trees, evaluation, minimax, pruning and bounded search | Compare immediate and future consequences in a small board game |
| Coordination | Separation, flocking, shared information, roles and cooperation | Compare independent pursuers with entities that spread out or share a sighting |
| Behaviour design and debugging | Visible intentions, predictability, deliberate mistakes, fairness and inspectable decisions | Show the current state, known facts and reason for a decision while changing one rule |

Supporting mathematics includes graphs and weighted paths, logic, scoring and
normalisation, conditional probability, heuristics and optimisation. Teach the
meaning of costs and estimates before using an algorithm's name as an
explanation. Distinguish an entity's information from the game's complete state.

Night Patrol, Three in a Row and a moving pursuer offer applications, not
mandatory prerequisites or a settled lesson sequence. No new behaviour is
claimed to exist in those published games by naming it here.

## Boundaries and connections

- Foundations explains general programming concepts and basic representations:
  lists, decomposition, tracing, and further queues, trees or other structures
  when developed. It must not become an indefinitely expanding prerequisite.
- Maths for Games explains vectors, geometry, graph costs, probabilities and
  scoring relationships. Game AI explains how those tools produce behaviour.
- Game Data and Algorithms compares game-specific representations and
  operations: entity pools, grids, sparse worlds, spatial queries, routes,
  events, undo histories and storage. AI owns the behavioural purpose of a
  navigation algorithm; neither module needs to duplicate the other's sequence.
- Game Design examines choices and overall structure; Game Feel examines
  how actions and consequences are communicated and experienced moment by moment.
- Maths explains projection and lighting calculations. Graphics and Animation
  explains how geometry becomes an image, including rasterisation and
  interpolation. System tracks implement these within named machine constraints.
- Shared graphics/audio principles connect to [graphics and audio](graphics-and-audio.md).
  Assets should be taught and created, not merely supplied.

Every lesson explains its immediate essentials locally. Cross-links offer a
reason to explore deeper material and work in both directions where useful.
Do not require completion of Maths for Games before starting Game AI.

## Authoring approach and next work

Use a visible question, inspectable experiment, worked calculation and practical
application. Introduce notation with its meaning; do not replace mathematical
substance with controls that hide the calculation. Paper models, diagrams and
pseudocode remain valid alongside interaction.

Maths for Games now has six locally integrated aiming lessons alongside the five
published probability lessons. Its overview distinguishes available sequences
from further planned explorations. The Craft overview uses the agreed seven-module
map without linking to empty modules.

Game Feel uses play, compare, explain. Its planned sequences are controls and
response; jumping and forgiveness; impact and feedback; cameras and attention;
readability and anticipation; and failure and recovery. The movement playground
compares three ships under identical input and top speed with different
acceleration and braking rules. It is a local browser prototype, not a completed
lesson sequence or evidence of target-machine performance. Existing patterns for
blinking, protection and input gates remain examples, not universal prescriptions.

Accessibility, debugging and performance recur where they affect decisions.
Physics, collision, cameras, procedural generation and level design develop within
the relevant modules before any case for separate navigation is considered.

Next review the movement experience with the user, then develop granular teaching
experiments. Game AI's first proposed experience remains perception, memory and
decisions. No publication is authorised by these local changes.
