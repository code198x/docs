# Observe retained-state reasoning

Use the [learner tasks](LEARNER-TASKS.md). No learner trial has run. Record starting
experience, first prediction, explanation, repair, variation and assistance.
Do not supply the missing concept while recording an independent answer.

| Update | Stored position | Full pixels | Drawn coordinate |
| --- | --- | --- | --- |
| 1 | 128 | 0.5 | 0 |
| 2 | 256 | 1 | 1 |
| 3 | 384 | 1.5 | 1 |
| 4 | 512 | 2 | 2 |

The changed version draws 0 each time. After every drawing it keeps stored zero,
so the next update starts from zero again. Its first stored-state difference
occurs after drawing update 1: it retains 0 instead of 128. The first visible
difference occurs at update 2. A correct first picture cannot distinguish the
policies; reading the retained state can reveal the fault earlier.

Removing the added assignment preserves the fractional state. A separate named
drawing coordinate is also a valid repair if it does not replace position.
Changing the initial position or rounding the step down to zero does not repair
the stated half-pixel movement rule.

At step 64 the stored positions are 64, 128, 192 and 256: full positions 0.25,
0.5, 0.75 and 1, with drawings 0, 0, 0, 1. Losing the retained fraction draws
zero throughout. A learner should explain the accumulation, not only repeat the
four supplied values.

The optional next sum after 65535 is 65663, outside the chosen unsigned 16-bit
range. The machine/language or application must define what happens; do not
accept an unexplained universal wrap or saturation rule. The finite model
rejects out-of-range cases rather than silently choosing either behaviour.

Mark each objective as independent / after a hint / after explanation / not yet
shown. Keep state reasoning separate from arithmetic slips or operating a tool.
No pass score, timing target or prerequisite course is added. A later fresh case
could probe retention, provided its delay and help are recorded. Do not infer
learning from the passing model or one successful copied trace.
