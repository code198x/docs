# Numbers and representation: learner tasks

This trial has not been run with a learner. Use these prompts without the assessor
notes. Write predictions before opening a lesson answer or running an experiment.
You may use the lessons; record where you needed help. There is no time target.

## Starting point

Choose Foundations, BASIC or assembly as your entry. Tell the observer which you
have used before. BASIC does not require assembly or Foundations; assembly does
not require BASIC. You can stop if a tool or instruction is unclear.

For Foundations, read Counting in Twos units 1–2 if binary or hex is unfamiliar,
then units 3–4. For BASIC, use Meet BASIC's keyboard guidance before entering
commands. For assembly, the byte-and-pixels lesson supplies its complete program
and explains bits, its byte directive and the screen address locally.

## Predict and explain

1. A two-byte unsigned value has every bit set. Write its value and the number of
   different patterns two bytes can hold. Explain why those numbers differ.
2. A machine uses byte addresses 0 to 65535. What can you conclude about its
   address range? What would you need to learn before saying how much RAM it has?
3. Read `11111111` as an unsigned byte and as a signed two's-complement byte.
   Did the bits change? Explain the change in meaning.
4. Keep only one result byte for 127 + 1. Predict its bits, unsigned value and
   signed value. Would there be a carry out of the byte? Would signed overflow occur?

## Change and check

5. In BASIC, enter `LET n=255`, `LET n=n+1`, then `PRINT n`. Predict first. Try
   starting with 65535 instead. Explain any difference from keeping a single byte.
   Record the actual output and report, even if it differs from your prediction.
6. Follow the optional assembly link from Foundations unit 4. In the byte-and-pixels
   experiment, predict what `%11111111` will draw, change the pattern and run it.
   Explain why these bits can make a picture rather than a negative number. Use
   browser Back to return and identify the sentence that connects the two ideas.

## Find a fault and make an example

7. Someone says, “127 + 1 fits in a byte, so there cannot be signed overflow.”
   Find the assumption that went wrong. Give the byte's unsigned and signed readings.
8. Draw a byte pattern of your own. Give its unsigned value, signed value and
   intended ink/paper row. Explain what a program must know to use it each way.

Record your first answers, edits, observed results and explanations separately.
The observer may clarify the task, but should not coach an answer.
