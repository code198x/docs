# Published Maths for Games: objectives and prerequisites

We read the eleven authored units at website
`1cb4ec62e675751a0c13006b2bff877cd0ec3f6c`. Their source identities and included
sample files are in [source-inventory.json](source-inventory.json), using samples
`163e74e18e9536fb555ef7319fa08bbc1836542b`.

These are objectives inferred from the actual explanations, instructions and
questions, not a new mandatory course order. “Uses” names knowledge needed for
the task; it does not require prior attendance. Each sequence has independent
entry. Later units within a sequence build on its earlier examples.

| Unit and actual title | Observable objective | Uses; local support and boundary | Maintained implementation |
| --- | --- | --- | --- |
| 01 Roll a die | Explain how scaling, INT and adding one turn a pseudorandom fraction into a face; distinguish one stored roll from another call; count twelve outputs | Whole numbers, multiplication and order; numbered lines, RUN, FOR/NEXT, LET and keyword keys introduced locally; optional Meet BASIC link. No physical randomness claim | `teaching/roll/dice-roller.bas` |
| 02 Keep the tallies | Trace one increment to one array entry; show all six counts sum to n; distinguish array indices from screen coordinates and GO SUB from falling into a routine | Unit 1 program, counts and indexing; DIM, GO SUB/RETURN, row/column conventions and reset explained locally | `teaching/tally/dice-roller.bas`, plus changed-line listing |
| 03 Compare shares | Calculate count/total, convert to percent, explain one-decimal rounding and why rounded shares need not sum to 100; distinguish sample frequency from a fair-model reference | Unit 2 counts, positive total, fractions/division; worked count/total examples, factor 1000 and non-negative rounding explained locally | `teaching/shares/dice-roller.bas`, plus changed-line listing; selected fresh native audit |
| 04 Watch the distribution | Explain why a fixed count's share can shrink; preserve counted rolls on early stop; distinguish rounded percentage from a coarse twenty-cell bar | Unit 3 shares, loop order and subroutines; INKEY$, OR, IF, slices, PRINT footprints, five-percentage-point cells and Q behaviour introduced locally | `teaching/live/dice-roller.bas`, plus changed-line listing |
| 05 Compare experiments | Trace previous/current state, fresh versus accumulated samples, separate n from batch progress, explain display cadence and key release; save and reopen the reusable program | Units 1–4, arrays, conditionals and state; copying before reset, uppercase conversion, limits and saving explained locally with Meet BASIC link. Overlapping samples are not independent experiments | `teaching/finished/dice-roller.bas`, plus changed-line listing |
| 06 Place a point | Locate signed (x,y), calculate displacement as finish minus start; distinguish negative movement from negative position | Addition/subtraction; origin, coordinate order, Δ notation and +Y-up world convention explained locally. Independent entry from probability | Aiming step 1 |
| 07 Measure the triangle | Calculate straight distance with Pythagoras; compare scaled triangles and direction ratios; identify undefined direction at zero distance | Coordinates/signs, multiplication and division; squares, square root and hypotenuse explained locally | Aiming step 2 |
| 08 Turn an angle into movement | Derive signed components using r cos and r sin; apply the same relationship to speed; explain why two full-speed components increase diagonal speed | Right-triangle ratios and angle; anticlockwise +X convention, component signs and degrees examples explained locally | Aiming step 3 |
| 09 Measure angles in radians | Explain arc/radius, convert degrees and radians, and diagnose a trigonometric function given the wrong angle unit | Circle radius, proportion, angle; circumference and conversions shown locally; JavaScript function convention named | Aiming step 4 |
| 10 Find the angle to a target | Subtract launcher position, explain ratio ambiguity versus atan2, predict quadrant and test a shot against the stated contact rule | Displacement and angle units; atan versus atan2, vertical direction, zero-distance boundary and clockwise/anticlockwise equivalence explained locally | Aiming step 5 |
| 11 Keep fractional movement in integers | Encode/decode scaled velocity and position, trace accumulation without discarding fractions, explain precision/range and changed hit results | Components and fractions; scale 4 worked example, signed rounding, widths and finite reference precision explained locally. No native overflow/cost claim | Aiming step 6 |

Probability paths above are relative to
`code-samples/sinclair-zx-spectrum/basic/dice-roller/`. The five complete checkpoints
and exact source transitions are owned by that samples repo, not by MDX. Website
`CodeFromFile.astro` reads those listings at build time.

Aiming steps use `code-samples/craft/maths-for-games/aiming/lessons.html`,
`lessons.mjs`, `model.mjs`, `lesson-content.mjs`, `style.css` and `lessons.css`.
The website's `AimingExperiment.astro` selects steps 1–6, while
`src/pages/experiments/aiming/[file].ts` serves the maintained files and hides the
standalone teaching/navigation chrome in the embed. MDX owns the public teaching
prose. Standalone sample prose is therefore not a second curriculum unit set.

## What this map qualifies

All eleven rows have an inspected lesson, explicit objective, local prerequisite
account and concrete source owner. This is an editorial coverage map. It does not
prove a beginner can follow the local explanations without help.

Only unit 3's maintained shares checkpoint has fresh native execution in this
pilot. Earlier [Dice Roller execution/publication evidence](../../platforms/sinclair-zx-spectrum/games/dice-roller/lessons.md)
and the [aiming release record](../../specifications/experiments/aiming.md) retain
their own configurations and dates. We did not rerun the other four checkpoints,
the six aiming experiments or their browser interactions here. Planned matrices,
3D, probability extensions and other broader maths routes are not counted as
authored units or evaluated objectives.
