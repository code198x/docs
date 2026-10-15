# Bits and shifts: assessor notes

No learner trial has occurred. Keep answers separate from the learner prompts.
Record prior experience and chosen entry route. Ask for thinking aloud; note
first prediction, actions, output, revised explanation and help. Preserve “I do
not know”. Separate keyboard/tool trouble from conceptual mistakes.

| Task | Expected evidence |
| --- | --- |
| 1 | AND → 00001010 (10); OR → 11001111 (207); XOR → 11000101 (197); XOR twice → original 11001010 (202). High four bits unchanged; AND preserves bits where its mask is 1, OR/XOR preserve where it is 0. |
| 2 | One input; eight-bit complement is 11110000 (240). A different width changes which positions are complemented. |
| 3 | BASIC prints 202 and 1. Its conditional numeric rules differ from Z80 bitwise instructions. Do not generalise this behaviour to every BASIC dialect or language. |
| 4 | 00001010 (10), outgoing bit 0; 10010000 (144), outgoing bit 1; 00000010 (2), outgoing bit 1. Z80 shifts retain the outgoing bit in carry. |
| 5 | Zero-fill → 01000000 (+64); sign-preserving → 11000000 (−64). The same input bits initially mean −128 when signed. |
| 6 | Eight pixels correspond to 00001010: ink at bit 3 and bit 1 with the original contrasting attribute. Source editing alone is not execution. Record finding the link, editing, running, interpreting output and returning separately. |
| 7 | 400 does not fit in a byte; low eight bits are 144. Correctness comes before speed. Timing depends on processor, instruction sequence and width; manual Z80 timings are not a measured end-to-end benchmark. |
| 8 | Any consistent byte/masks are acceptable: OR mask has 1 at chosen set bit; XOR has 1 at each flip bit. OR twice keeps the set result; XOR twice restores the original. Check unrelated bits remain unchanged. |

For conceptual tasks record independent / after rereading / after prompting /
not demonstrated. For browser tasks record technical completion separately from
explanation. Note whether draft recovery helped or confused the learner. Do not
turn one trial into a numerical effectiveness score.

Hypotheses: explicit width/fill rules may prevent applying unsigned shifts to
signed values; the BASIC contrast may prevent name-based transfer; a real pixel
mask may make unaffected bits easier to explain. All remain unverified.

File a deduplicated issue for repeatable difficulties with exact task, source
revision, first response, actions, observed output and help given. Save anonymous
observations without invented people or quotations. Keep the umbrella issues open.
