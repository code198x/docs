# Aiming — six-part teaching progression

**Status:** The user approved the aiming prototype and this six-part direction.
Six locally authored teaching pages now have focused experiments, worked examples
and prediction/answer disclosures. They await review in this form. They are not
integrated into the website and have not been approved for publication.

The maintained source is `code-samples/craft/maths-for-games/aiming/`.
Open `lessons.html?step=1` through its documented local server. The accepted
`index.html` playground remains available unchanged. The existing probability
lessons and their published URLs are unaffected.

## Progression and boundaries

| Part | Explain | Reader action and evidence | Controls introduced |
|---|---|---|---|
| Place a point | Origin, ordered coordinates, signs, position versus displacement, world/screen Y | Change one coordinate; predict (120, 90) + (−30, −50) = (90, 40) | X and Y inputs/sliders; point dragging |
| Measure the triangle | Right angle, hypotenuse, Pythagoras, ratios, zero distance | (120, 90) has distance 150; doubling both gives distance 300 with unchanged shares | Same point controls; triangle and distance/ratio readouts |
| Turn an angle into movement | Adjacent/opposite shares; signed sine and cosine; radius versus speed | At 30° and radius 150, point is approximately (129.904, 75); at 90° and speed 3, velocity is (0, 3) | Degree angle and radius; component readouts |
| Measure angles in radians | Arc/radius, π, degree/radian conversion, function input units | π/2 points upwards; angle 1 and radius 100 produce arc length 100 | Radian input and π presets; highlighted arc |
| Find the angle to a target | Target minus source; tangent, atan ambiguity, atan2, quadrant and vertical cases | Predict aim, reveal, then fire; repeat in all four quadrants and on an axis | Aim, single shot, target changes and explicit answer reveal |
| Keep fractional movement in integers | Encoding/decoding, rounding rule, accumulating scaled position, widths and range | The calculated opening shot hits in the reference, misses at scale 4, hits at scale 256 | Precision selector and a second, dashed shot |

Every page explains enough to use its experiment without a programming-language
prerequisite. Mathematics is shown in prose and worked arithmetic, not confined
to an interactive result. Notation, signs, angle units and coordinate conventions
are explicit. Each prediction has an accessible native disclosure with reasoning.

The triangle is enlarged to the chosen distance. Velocity readouts use speed 3
units per tick; the text distinguishes the two. The circle/triangle pages do not
show collision or fixed-point controls. Radians have their own experiment before
atan2 appears. Fixed point uses the accepted shot model with no angle lookup table.
The final page starts with the correct angle to isolate representation error.

## Implementation and checks

`lesson-content.mjs` owns teaching copy; `lessons.mjs` owns the six focused views.
The last two views share the accepted `model.mjs` with the original playground.
Earlier views directly calculate their displayed geometry; they do not simulate
a hidden game. Page navigation is local and query-addressable; unknown step values
fall back to the first page. Reset restores the current experiment's initial state.

The original five model tests pass. `verify-lessons.mjs` exercises the worked
examples, zero direction, both angle units, all six target directions, coarse/fine
contact, resets, input changes during playback and reduced-motion results. Each
page passes axe and fits 390/1280 pixel viewports. Native inputs and sliders provide
keyboard alternatives to pointer geometry. Desktop and mobile captures were
inspected. Evidence is in the samples' `verification/lessons/` directory.

These are host-side mathematical results, not machine-performance or physical
hardware results. JavaScript numbers represent the bounded scaled integers exactly;
no retro overflow behaviour is emulated. The reference is floating point, not
infinite precision. Contact uses movement segments and the target radius of 5.

## Review and integration

Review the six focused pages as a teaching sequence. The next implementation step
is website integration with maintained experiment assets, normal lesson navigation
and Question components, preserving the existing probability URLs. Keep the
independent geometry entry rather than making Dice Roller a prerequisite. Broader
matrices, coordinate transformations, gravity, interception and lookup-table work
remain outside this slice.
