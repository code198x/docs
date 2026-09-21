# Maths for Games — coverage and teaching direction

Apply [curriculum design](curriculum.md) and [The Craft coverage map](craft-coverage.md).
The user agreed a substantial mathematical treatment with visible game
applications, especially geometry, trigonometry, matrix algebra, coordinate
spaces and fixed-point calculation. This specification defines coverage; it
does not set a compulsory order, unit count or claim that topics are authored.

Dice Roller's five probability lessons are published. The broader routes below
are for development. Readers can enter at a useful problem without first
completing probability, Foundations or a system track.

## Teaching method

Make the geometric or numerical meaning visible, explain the relationship, work
through the arithmetic and apply it. Notation and algebra are part of the
teaching, not obstacles to omit. A reader should be able to explain where an
answer comes from without operating an interactive control.

State units, ranges, axis directions, handedness and conventions. Explain
negative values, fractions, degrees and radians where needed. Separate the
mathematical model, its discrete numerical implementation and its rendered
appearance. Qualify machine-cost claims by processor, language and workload.

## Connected routes

| Route | Mathematical coverage | Tangible outcomes |
|---|---|---|
| Geometry, aiming and motion | Coordinates, triangles, Pythagoras, sine, cosine, tangent, inverse trig, atan2, vectors, magnitude, normalisation, dot and cross products | Aim a projectile, place objects in a ring, orbit, pursue and reflect motion |
| Measurement and contact | Lines, rays, segments, planes, parametric/vector equations, simultaneous equations, projections, nearest points, intersections and barycentric coordinates | Range and sight tests, triangle containment, collision detection, reflection and sliding |
| Transformations and viewing | Basis axes, matrices, composition, inverses, homogeneous coordinates, pivots, local/world/view spaces, orthographic and perspective projection | Rotate a shape, move a camera, build and view a cube |
| Curves and surfaces | Cartesian and parametric forms, interpolation, Bézier curves, derivatives, gradients, tangents, normals, arc length, partial derivatives, sweeps, revolutions and patches | Follow a curved track, construct a sphere, orient and light a surface |
| Time, waves and patterns | Discrete updates, velocity, acceleration, relative motion, timestep effects, damping, springs, frequency, phase, wrapping, symmetry and noise | Predict a landing, loop a world, create oscillation and terrain patterns |
| Chance and decisions | Counts, shares, distributions, expected value, weighted choices, independence, conditional probability, reproducible seeds, correlation and shuffle bags | Compare experiments, design encounters, express uncertainty and score actions |
| Discrete models for AI | Logic, graphs, weighted paths, costs, heuristics, search trees, evaluation and optimisation | Explain route choice, utility scores and the mathematical assumptions behind a decision |

Numerical methods run through every route. Sampling and aliasing connect images,
sound and movement; colour arithmetic includes interpolation, blending,
linear-light versus gamma-encoded values and palette quantisation. Coordinate
and rotation conventions must be explicit rather than inferred from a diagram.

These routes share explanations without becoming one long prerequisite chain.
Collision detection and response are distinct questions. A vector towards a
target is not a route around obstacles. Equal curve-parameter steps generally do
not cover equal distances. Probability and perceived fairness are related but
not interchangeable.

## Matrices, coordinate spaces and 3D

Give matrix algebra substantial coverage. Begin with vectors and basis axes,
then show what a matrix does to the axes, one point and a whole shape. Connect
each term of matrix–vector multiplication to the transformed result. Explain
matrix–matrix multiplication as composition and demonstrate non-commuting order.
Declare row/column-vector and multiplication conventions consistently.

Distinguish the stages:

1. Local coordinates describe geometry relative to the object's own origin.
2. A model transformation places it in world coordinates.
3. A view transformation expresses the world relative to the camera.
4. Projection maps that view towards a two-dimensional picture; perspective
   requires the perspective division to be explained explicitly.
5. A viewport mapping places the picture in screen pixels with named axis directions.

Coordinate-space changes and projection are different operations. Explain camera
transforms through inverses, including why moving the camera right shifts the
view of the world left. Rotate around local and world origins to expose the
importance of pivots and transformation order. Homogeneous coordinates explain
how translation joins scaling and rotation in a common representation; distinguish
points from directions and introduce homogeneous scale and points at infinity
when their geometric purpose is clear.

A wireframe cube is a useful early outcome: vertices and edges, axis rotations,
composition, orthographic/perspective views and an independently moving camera.
Develop faces, normals, back-face culling, dot-product lighting, depth and
near-plane clipping as further questions. Relate one-, two- and three-point
perspective to orientation and vanishing points rather than presenting three
unrelated tricks.

Construct spheres through angular parameters and examine pole crowding. Continue
with cylinders, surfaces of revolution and piecewise patches. Derivatives explain
curve tangents; partial derivatives and vector products explain surface tangents
and normals. Explore continuity at joins and approximate arc-length travel.
Euler-angle limitations and quaternions are later extensions when orientation
and interpolation provide a concrete reason for them.

## Fixed point and numerical reliability

Foundations explains what fixed-point representation means. This module explains
how to calculate with it; system tracks show instructions, storage and measured
costs on the named target. Reintroduce enough locally to permit independent entry.

For each relevant application:

- Choose and state the scale, signedness, storage width, useful range and precision.
- Show encoding and decoding; distinguish stored integers from represented values.
- Track scales through addition, multiplication and division. State intermediate
  widths and rescaling points, not just the final variable type.
- Explain rounding, including negative values, and show where truncation loses
  information. Preserve fractional position separately from its drawn pixel.
- Check overflow, tiny divisors, zero-length vectors, nearly parallel geometry and
  degenerate shapes. Explain tolerances in the chosen units and precision.
- Compare exact-model results with approximations: sine tables, quantised angles,
  approximate distances and accumulated matrix or movement error.

Use examples such as a direction vector, rotating cube, perspective divide or
curve calculation to expose range–precision trade-offs. Show wobble, drift or
changed contact decisions when they occur. Fixed point is not universally faster
or more accurate; choose it for a stated implementation reason.

## Reference and coverage provenance

The user supplied the contents of *Computer Graphics: Mathematical First Steps*,
Patricia A. Egerton and William S. Hall (Prentice Hall Europe, 1998), ISBN
9780135995723. Its three parts cover vector algebra for points, lines and curves;
matrix algebra for transformations; and differentiation for curves and surfaces.
Use it as a coverage reference, not a prescribed chapter order or text to copy.
Only the supplied contents and bibliographic identity have been reviewed here;
chapter explanations, exercises and appendices have not been assessed.

The contents establish useful prompts for coverage: scalar/vector products,
parameterised geometry, homogeneous vectors, viewing, perspective, tangents,
interpolation, sweeps, revolutions and surface patches. Consult the actual text
before citing a chapter for a mathematical claim. Game probability, AI decisions,
fixed-point practice and numerical robustness also need deliberate treatment.

## First experiment and existing trial

The [aiming prototype](experiments/aiming.md) now implements the first angle,
triangle, sine/cosine, atan2 and fixed-point investigation locally for review.
Its six authored website lessons and overview are published and live-verified
in website PR #445.

The initial proposed experiment was a point moving around a circle, with adjustable
angle and radius, visible horizontal/vertical projections and a right triangle.
Explain sine and cosine, degrees/radians, signs across quadrants and the resulting
coordinates. Then apply the same relationship to aiming, rings and rotation,
with a scaled-integer comparison. Choose a bounded first teaching slice before
adding every application to one interface.

The one-dimensional docking trial remains a small supporting experiment at
`code-samples/craft/maths-for-games/reach-the-dock.html`. The user found it
explanatory but unexciting; it does not define the subject's opening or scope.
It updates velocity by -1, 0 or +1 before adding velocity to position each tick.
From rest at zero, three right burns, five coast ticks and three left burns stop
at position 24. Browser checks passed coasting, braking, reversal, docking,
overshoot, reset and keyboard operation at narrow and wide layouts. This is a
host-side teaching model, not evidence of native-machine performance.

Keep complex-number methods, Fourier analysis and advanced constraint solvers as
possible extensions. Introduce numerical integration through practical timestep
questions; a full treatment can follow if an application warrants it. The scope
map should support useful entry routes, not an obligation to exhaust mathematics.
