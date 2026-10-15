# Pseudocode

Foundations teaches concepts using a shared notation, independently of any machine or language. Use this grammar consistently; extend it only when an example needs an explicit new convention. It is explanatory notation, not an implemented programming language or a promise that an example runs in an emulator.

Diagrams, traces, counters and worked examples keep it concrete. System tracks explain their own syntax and representation locally, including differences from this notation.

```text
# a comment runs to the end of the line

LET score = 0                        assignment
LET alive = TRUE                     a box holding yes or no
LET score = score + 10               a box updated from its own value

SHOW "Score: ", score                output; the comma joins and adds nothing
ASK "Your name? " INTO name          input

IF guess = 7 THEN SHOW "Correct!"    one-line form, no second path
IF guess = 7 THEN … END              block form
IF … THEN … ELSE … END               two paths
IF … THEN … ELSE IF … THEN … END     a chain, closed once

FOR i = 1 TO 10 … END                counted loop
FOR EACH score IN scores … END       over a list
WHILE lives > 0 DO … END             test at the top
REPEAT … UNTIL guess = 7             test at the bottom

DEFINE divider … END                 a job with a name
DEFINE double(n) … RETURN n * 2 … END a job given a value, giving one back
CALL divider                         do the job
CALL draw(10, 5)                     do the job, with values
LET x = double(5)                    use what it hands back

LET secret = RANDOM 1 TO 10          a value you cannot predict

SHOW 7 / 2                           3.5, the whole answer
SHOW ROUND DOWN (7 / 2)              3, how many whole ones fit
SHOW 7 REMAINDER 2                   1, the part left over
SHOW ROUND 3.7                       4, the nearest whole number

SHOW CODE "A"                        65, the number a character is stored as
SHOW CHARACTER 65                    A, the other way round

SHOW BIN 1111                        a number written in binary
SHOW HEX FF                          a number written in hex
a BITAND b   a BITOR b   a BITXOR b  the bit tools, column by column
BITNOT a                             every bit flipped
a SHIFTLEFT 1   a SHIFTRIGHT 1       the whole row slid sideways

LET scores = [10, 20, 30]            a list
LET first = scores[1]                one item, counting from 1
LET scores[2] = 99                   change one item
APPEND 40 TO scores                  grow it
LENGTH(scores)                       how many

+ - * /        = <> < > <= >=        AND OR XOR NOT
(2 + 3) * 4                          brackets: work this out first
```

The right-hand annotations above explain the notation; they are not program text. Use `#` for comments in examples.

- `LET` assigns; `=` in a condition compares. Explain the distinction when it first matters. Assigning a comparison stores its current Boolean answer, not a live expression; later operand changes do not update the saved value. Reassign when a fresh answer is required, and state when a deliberately latched flag resets.
- `SHOW` joins its comma-separated values without inserting spaces. `+` is arithmetic. Put a wanted space inside the quoted text.
- State an ASK example’s input contract where it matters: submission, text or numeric values, spaces, empty input and validation. Basics’ name example submits a line of text with Enter, keeps spaces and accepts empty text; this local convention is not a promise of identical target-language input or numeric conversion.
- `FOR` ranges and `RANDOM` ranges include both ends. `/` keeps a fractional quotient in this notation; target division and precision rules need their own explanation. Multiplication and division precede addition and subtraction; equal-priority operations in these two groups work left to right. Brackets choose the grouping.
- `ROUND DOWN` is floor: the greatest whole number no larger than the input, including for negatives. Introductory `REMAINDER` examples use non-negative whole inputs and a positive whole divisor: original = quotient × divisor + remainder, with quotient = floor(original / divisor) and 0 ≤ remainder < divisor. State a convention before extending to negative inputs.
- `ROUND` means nearest whole number. Working It Out chooses the higher number for non-negative halfway values. State the input range and halfway policy where they matter; do not assume a target language shares that policy.
- A named job has its own names. Parameters receive copies of values; do not imply a particular machine's reference or allocation behaviour. `RETURN` supplies a result, unlike Sinclair BASIC's return from `GO SUB`.
- Lists start at 1. A valid index is a whole number from 1 through `LENGTH(list)`; an empty list has no valid index. Introductory `FOR EACH` examples keep the list size fixed. A target language's indexing, mutation during iteration, storage limits and allocation need their own explanation.
- `AND`, `OR`, `XOR` and `NOT` combine truth values. `XOR` is true when exactly one Boolean operand is true. Comparisons bind before `NOT`, then `AND`, then `OR`; use explicit brackets when mixing `XOR` with other operators. Truth-table equivalence assumes the same current Boolean input values; it does not establish target-language numeric representation, operand evaluation effects or execution cost. The `BIT` operations work on number representations. State the bit width, signedness, overflow and shift conventions when used; an unbounded `BITNOT` is not a useful machine model.
- `BIN` and `HEX` mark the base of a numeric literal; they do not allocate storage or choose its width. Leading zeros preserve the value. State unsigned/signed interpretation and a chosen field width before making storage-range claims.
- `CODE` and `CHARACTER` examples must name the character encoding where it matters. Character codes are not universal across machines.
- Block `IF`, `FOR`, `WHILE` and `DEFINE` close with `END`; `REPEAT` closes with `UNTIL`. Indent bodies. Do not infer BASIC line numbers or syntax from familiar keywords.

The grammar being available does not establish which constructs have been taught. Read the actual lesson before relying on its coverage. See [Curriculum design](curriculum.md) and [Unit guidance](unit.md).
