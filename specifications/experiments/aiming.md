# Maths for Games — aiming experiment

**Status:** Implemented locally for user review. No lessons or site routes are
published by this work. The user authorised a playable prototype following the
agreed geometry, trigonometry and fixed-point direction.

Source: `code-samples/craft/maths-for-games/aiming/`. Its README owns launch and
verification instructions and the model's mathematical contract.

A point shot leaves the origin towards a stationary target. Angle changes expose
sine/cosine components and a triangle enlarged to the target's distance. The
backwards calculation uses atan2, including quadrant signs, radians and a
normalised degree angle. Six targets include a vertical direction and all four
quadrants. A companion shot quantises velocity at scales 4, 16 or 256 and keeps
fractional position by accumulating integers at the same scale.

The opening target at 32.8° and distance 220 demonstrates the distinction between
aiming and representation: the reference hits, scale 4 misses by 8.41 units from
the target centre, and scale 256 hits. The hit radius is 5. Contact is checked
along movement segments, not just sampled endpoints. The result separately names
closest target distance and separation between the two paths at the final tick.

The interface supports pointer aiming, native keyboard controls, explicit fire,
replay, reset, triangle visibility and instant trajectories for reduced motion.
Five model tests and browser interaction/accessibility/layout checks pass.
Desktop and mobile screenshots were inspected. The simulation uses host-side
arithmetic; it is not evidence about any retro CPU's speed or overflow behaviour.

The next decision is whether this makes the mathematical relationships useful
and engaging enough to support lesson authoring. Review the amount shown at once,
how clearly the triangle connects to movement, and whether fixed-point comparison
should be a separate teaching step. Matrices, local/world transforms, gravity and
moving-target interception remain outside this bounded prototype.
