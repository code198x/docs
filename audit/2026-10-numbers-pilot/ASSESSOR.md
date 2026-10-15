# Numbers and representation: assessor notes

No learner trial has occurred. Keep this sheet away from the learner prompts.
Technical execution and accurate prose are necessary checks, not learning outcomes.

Ask the learner to think aloud. Note prior experience and chosen entry route,
first prediction, actual action, observed output, revised explanation and any
prompting. Record tool failures separately from conceptual mistakes. Allow an
honest “I do not know”; do not supply a missing concept during the first attempt.

| Task | Evidence to listen for | Answer or check |
| --- | --- | --- |
| 1 | Maximum versus count, including zero | 65535; 65536 patterns. |
| 2 | Addresses versus physical RAM | 65536 possible byte addresses; memory map/configuration needed. ROM, unmapped addresses or bank switching prevent inferring RAM size. Do not require all three examples. |
| 3 | Interpretation, not a tag in the byte | Unsigned 255; signed −1; same bits. |
| 4 | Carry and signed overflow distinguished | 10000000; unsigned 128; signed −128; no carry; signed overflow. |
| 5 | Language representation does not inherit a byte limit | Spectrum BASIC prints 256 and 65536, with normal completion. Record a failed keyboard entry as a tool/instruction observation. |
| 6 | Representation transfer and discovery | Eight ink pixels with the starting white-on-black attribute; same bits could instead be interpreted numerically. Record finding the link, editor use and return separately. |
| 7 | The signed range is narrower at the positive end | +128 fits unsigned but exceeds +127 signed. |
| 8 | Creation with a consistent pattern across three readings | Accept any eight-bit pattern with correct numeric interpretations and pixel order. If ink and paper are equal, the stored pattern can be invisible; accept a supported explanation. |

For tasks 1–4 and 7–8 record independent / after rereading / after a prompt /
not demonstrated. For tasks 5–6 record successful execution separately from
explanation. Do not combine these into a numerical effectiveness score from one
learner. Save anonymous observations without invented people, quotations or results.

Hypotheses: the new distinctions may prevent conflating storage width with every
language's arithmetic and address range with fitted memory. The optional link may
help transfer the same-bits/different-meaning idea. Neither hypothesis is verified.

If a consistent difficulty appears, file a deduplicated issue with exact task,
first response, observed navigation or output, prompts given and source revision.
Keep umbrella #114/#115/#124 open until their broader evidence requirements are met.
