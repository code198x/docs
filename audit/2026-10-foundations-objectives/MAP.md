# Foundations: per-unit objectives and knowledge used

All 39 authored units at website revision `2b9905262dcb7261314b6ef6490db7b8a5c803ed` appear below.
Goals and knowledge are reviewer synthesis from full lesson bodies. [Source records](units.json)
retain each lesson’s own learning summary, opening, explicit disclosure/Question prompts,
authored links and hash. [The report](REPORT.md) explains findings and limits.

Suggested support names concepts used by an example. It is optional reading,
not required attendance, a new sequence or a dependency graph the learner must complete.
The record separately explains what each page recalls locally. Shared notation
does not promise identical target syntax, numeric rules or hardware behaviour.

## The Basics

| Unit and source | Goal | Knowledge used / local support | Suggested support |
| --- | --- | --- | --- |
| [01: A Program Is Instructions](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/basics/unit-01.mdx#L70) | Trace SHOW; separate displayed words from actions and intention from valid instructions. | Read ordinary words in sequence; no programming course needed. Pseudocode and one-instruction execution are introduced locally. | None |
| [02: One Thing After Another](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/basics/unit-02.mdx#L77) | Predict output order after rearranging a sequence. | SHOW and reading top to bottom. Three complete SHOW lines recall output; unit 1 gives the fuller introduction. | [basics/01](#the-basics) |
| [03: Showing Your Work](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/basics/unit-03.mdx#L60) | Distinguish quoted text from arithmetic; join text and values with explicit spaces. | SHOW, small addition and sequence. The quoted/unquoted pair and comma rule are explained locally. | [basics/02](#the-basics) |
| [04: A Place to Remember](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/basics/unit-04.mdx#L99) | Trace assignment, repeated reads and replacement without rewriting earlier output. | SHOW, names and sequence. LET, reading a name and assignment meaning are introduced locally. | [basics/03](#the-basics) |
| [05: Asking the Player](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/basics/unit-05.mdx#L74) | Trace submitted text, repeated input, empty input and spaces. | Stored values, SHOW and comma joins. ASK submission is defined; comma spacing explicitly refers to unit 3. | [basics/03](#the-basics), [basics/04](#the-basics) |

## Counting in Twos

| Unit and source | Goal | Knowledge used / local support | Suggested support |
| --- | --- | --- | --- |
| [01: Ten Fingers, Two Wires](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/counting-in-twos/unit-01.mdx#L122) | Convert binary and decimal; separate notation, width and unsigned range. | Small whole-number addition and decimal place value. Place values, bit model and byte introduced with worked reverse conversion. | [working-it-out/01](#working-it-out) |
| [02: Four Bits at a Time](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/counting-in-twos/unit-02.mdx#L164) | Group bits from the right into hex; distinguish value from storage width. | Binary places, addition and multiplication. Bit/byte/place values recalled; nibble and hex table introduced locally. | [counting-in-twos/01](#counting-in-twos) |
| [03: Two Bytes Together](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/counting-in-twos/unit-03.mdx#L129) | Combine high/low bytes and distinguish address space from installed memory. | Binary/hex, multiplication and carry. Sixteen-bit places and high-byte weighting explained; relies on BIN/HEX familiarity. | [counting-in-twos/01](#counting-in-twos), [counting-in-twos/02](#counting-in-twos) |
| [04: A Minus With No Minus Sign](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/counting-in-twos/unit-04.mdx#L117) | Interpret signed byte patterns and distinguish carry from signed overflow. | Unsigned bytes, binary places, addition and negative numbers. Signed range and complement mapping introduced with explicit low-byte retention. | [counting-in-twos/01](#counting-in-twos), [counting-in-twos/03](#counting-in-twos) |

## Decisions

| Unit and source | Goal | Knowledge used / local support | Suggested support |
| --- | --- | --- | --- |
| [01: Making a Choice](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/decisions/unit-01.mdx#L120) | Predict conditional output at boundaries without changing the tested value. | Input, stored values and numeric comparison. IF and comparison signs introduced; assignment/comparison distinguished. | [basics/04](#the-basics), [basics/05](#the-basics) |
| [02: One or the Other](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/decisions/unit-02.mdx#L125) | Trace first matching branch, overlapping tests and continuation after END. | IF, comparisons and numeric input. The separate tests are shown in full; valid numeric input explicitly assumed. | [decisions/01](#decisions) |
| [03: A Yes You Can Keep](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/decisions/unit-03.mdx#L142) | Distinguish stored Boolean answers, fresh comparisons, latches and restart resets. | Assignment and IF. TRUE/FALSE, flags and refresh/reset examples explained locally. | [basics/04](#the-basics), [decisions/01](#decisions) |
| [04: Asking Two Things at Once](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/decisions/unit-04.mdx#L106) | Construct complete compound questions and use brackets for grouping. | Boolean comparisons, flags and IF/ELSE. AND/OR/NOT and comparison signs explained; brackets recalled from arithmetic. | [decisions/01](#decisions), [decisions/03](#decisions), [working-it-out/01](#working-it-out) |

## From Source to Silicon

| Unit and source | Goal | Knowledge used / local support | Suggested support |
| --- | --- | --- | --- |
| [01: The Program Is Not What Runs](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/from-source-to-silicon/unit-01.mdx#L140) | Distinguish source, instructions and data; trace an invented instruction stream. | Stored values, addition and doubling. Three routes and the invented machine defined locally; byte notion used. | [basics/04](#the-basics), [working-it-out/02](#working-it-out), [counting-in-twos/01](#counting-in-twos) |
| [02: Translating As You Go](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/from-source-to-silicon/unit-02.mdx#L112) | Explain interpreter/token work and distinguish update rate from display refresh. | Repeated updates, numeric loops and source/instruction distinction. Interpreter recalled; ROM/RAM and tokens introduced; loop control assumed. | [repeating/01](#repeating), [working-it-out/02](#working-it-out), [from-source-to-silicon/01](#from-source-to-silicon) |
| [03: Translating Once](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/from-source-to-silicon/unit-03.mdx#L200) | Compare compilation/assembly; trace valid, invalid and empty toy translations. | Lists, indexed lookup, nested loops, comparisons and Boolean flags. Index origin, matching tables, pending output and latched invalidity explained; constructs span several modules. | [structure/01](#structure), [repeating/01](#repeating), [decisions/03](#decisions), [from-source-to-silicon/01](#from-source-to-silicon), [from-source-to-silicon/02](#from-source-to-silicon) |
| [04: What Speed Costs You](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/from-source-to-silicon/unit-04.mdx#L86) | Separate diagnostics from intention; distinguish algorithm, source and machine-interface portability. | Source/translation, named responsibilities and expected/actual comparison. Small examples explain each responsibility; diagnosis support explicitly linked. | [from-source-to-silicon/01](#from-source-to-silicon), [from-source-to-silicon/03](#from-source-to-silicon), [structure/04](#structure) |
| [05: Put It on the Clock](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/from-source-to-silicon/unit-05.mdx#L115) | Specify comparable work/clocks, inspect deadlines and preserve correctness. | Small averages, loops and measurement units. Invented timing table is self-contained; native inspector route is optional and qualified. | [from-source-to-silicon/04](#from-source-to-silicon), [working-it-out/01](#working-it-out) |

## Gates and the Adder

| Unit and source | Goal | Knowledge used / local support | Suggested support |
| --- | --- | --- | --- |
| [01: The Same Table, Drawn](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/gates-and-the-adder/unit-01.mdx#L126) | Relate gate diagrams to all Boolean rows and distinguish settled model from physical behaviour. | 0/1, table reading and Boolean rules. Bit model and gates introduced; AND/OR/XOR/NOT tables supplied locally. | [truth-tables/01](#truth-tables), [truth-tables/02](#truth-tables) |
| [02: The Half Adder](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/gates-and-the-adder/unit-02.mdx#L126) | Derive half-adder sum/carry and retain the complete numeric answer. | Small sums, binary places, XOR and AND. Binary 1+1 and SUM+2*CARRY explained; gate rules recalled through columns. | [counting-in-twos/01](#counting-in-twos), [gates-and-the-adder/01](#gates-and-the-adder) |
| [03: The Full Adder and the Ripple](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/gates-and-the-adder/unit-03.mdx#L172) | Trace full-adder input carry and a multi-column ripple result with final carry. | Half adders, binary places and eight input combinations. Carry-in starting state and full arithmetic identity stated; static overview distinguished from controls. | [gates-and-the-adder/02](#gates-and-the-adder), [truth-tables/01](#truth-tables) |

## Repeating

| Unit and source | Goal | Knowledge used / local support | Suggested support |
| --- | --- | --- | --- |
| [01: Doing It Again](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/repeating/unit-01.mdx#L85) | Trace inclusive counted loops, counter values, zero/one-pass ranges and body placement. | SHOW, variables and multiplication. FOR/END and counter introduced; assumes familiarity with variable expressions. | [basics/04](#the-basics), [working-it-out/01](#working-it-out) |
| [02: Until You Get It](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/repeating/unit-02.mdx#L156) | Trace post-test repetition and round-stable randomness; distinguish reachable from guaranteed exits. | ASK, numeric comparisons and IF branches. Full guessing example recalled; valid numbers assumed; RANDOM range and waiting explained. | [decisions/02](#decisions), [repeating/01](#repeating) |
| [03: Checking Before You Start](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/repeating/unit-03.mdx#L141) | Choose a pre-test loop and explain progress, misplaced resets and zero-pass behaviour. | Comparisons, decrement and post-test repetition. WHILE explained locally; numeric domain and update rules stated; REPEAT recalled. | [working-it-out/02](#working-it-out), [repeating/02](#repeating) |

## Structure

| Unit and source | Goal | Knowledge used / local support | Suggested support |
| --- | --- | --- | --- |
| [01: A Box That Holds Many](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/structure/unit-01.mdx#L146) | Use list indices, append, length, empty traversal and nested loop counts. | LET, SHOW, loops and small multiplication. LET/SHOW recalled; FOR EACH introduced; counted nested loops rely on the preceding loop concept. | [basics/04](#the-basics), [repeating/01](#repeating) |
| [02: A Job With a Name](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/structure/unit-02.mdx#L141) | Trace definition/call/return control; decide whether shared work should change together. | SHOW and sequence. DEFINE/CALL introduced with a full trace; no parameter knowledge required. | [basics/02](#the-basics) |
| [03: Telling a Job What to Work On](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/structure/unit-03.mdx#L139) | Explain local numeric parameter copies, returned values, effects and caller contracts. | Named jobs, assignment and multiplication. Builds on divider; parameter scope and numeric-copy rule stated; contrasts BASIC locally. | [structure/02](#structure), [basics/04](#the-basics), [working-it-out/01](#working-it-out) |
| [04: When It's Wrong](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/structure/unit-04.mdx#L134) | Reproduce a fault, predict distinguishing evidence, repair and check regressions. | Numeric input, arithmetic, lists and repeated updates. Small broken/fixed programs shown; later tracing example uses FOR EACH from unit 1. | [working-it-out/01](#working-it-out), [working-it-out/02](#working-it-out), [structure/01](#structure) |

## Truth Tables

| Unit and source | Goal | Knowledge used / local support | Suggested support |
| --- | --- | --- | --- |
| [01: True and False](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/truth-tables/unit-01.mdx#L93) | Enumerate Boolean inputs, NOT and reachable versus general table rows. | Yes/no questions and reading a grid. Boolean inputs and the local 0/1 notation introduced; no binary course needed. | [decisions/04](#decisions) |
| [02: Both, Either, Different](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/truth-tables/unit-02.mdx#L105) | Compare AND/OR/XOR and find the distinguishing both-true row. | Boolean input rows and NOT. Four cases and operators explained; game example also uses IF and CALL. | [truth-tables/01](#truth-tables), [decisions/04](#decisions), [structure/02](#structure) |
| [03: Two Guards, One Guard](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/truth-tables/unit-03.mdx#L126) | Prove Boolean equivalence under fixed-input/complement assumptions; detect a stale-flag counterexample. | AND/OR/NOT tables and current versus saved state. Complement assumptions are stated before proof; target evaluation is a separate boundary. | [truth-tables/01](#truth-tables), [truth-tables/02](#truth-tables), [decisions/03](#decisions) |

## Working It Out

| Unit and source | Goal | Knowledge used / local support | Suggested support |
| --- | --- | --- | --- |
| [01: Working It Out](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/working-it-out/unit-01.mdx#L108) | Calculate input-driven expressions with precedence and brackets. | Small arithmetic, numeric input and stored values. ASK and SHOW recalled; numeric input assumed, not validated; operator priorities explained. | [basics/04](#the-basics), [basics/05](#the-basics) |
| [02: A Box That Grows From Itself](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/working-it-out/unit-02.mdx#L84) | Trace read-before-write updates and explain why two assignments do not swap values. | Variables, addition and subtraction. LET is recalled and a trace explains the update order. | [basics/04](#the-basics), [working-it-out/01](#working-it-out) |
| [03: When It Doesn't Divide Evenly](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/working-it-out/unit-03.mdx#L137) | Choose quotient, floor, remainder or nearest rounding; explain their domains. | Division, fractions, ordered numbers and brackets. Floor including a negative example, remainder domain and positive halfway rule are given locally. | [working-it-out/01](#working-it-out) |

## Working the Bits

| Unit and source | Goal | Knowledge used / local support | Suggested support |
| --- | --- | --- | --- |
| [01: Switch by Switch](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/working-the-bits/unit-01.mdx#L152) | Choose masks to keep/set/toggle bits; explain width-dependent complement. | Binary bytes and Boolean questions. Contrasts Boolean and bitwise operators and supplies tables; byte reading assumed. | [counting-in-twos/01](#counting-in-twos), [decisions/04](#decisions) |
| [02: Slide the Whole Row](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/working-the-bits/unit-02.mdx#L110) | Predict width-limited shifts and qualify arithmetic and speed equivalence. | Binary places, unsigned/signed interpretation and division. Eight-bit zero-fill contract stated; signed alternative and target timing contrast explained. | [counting-in-twos/01](#counting-in-twos), [counting-in-twos/04](#counting-in-twos), [working-it-out/03](#working-it-out) |
| [03: A Letter Is a Number](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/working-the-bits/unit-03.mdx#L160) | Distinguish code from quantity and validate ASCII digit/case conversions. | Bytes, ranges, subtraction and masks. Encoding introduced; BITOR setting recalled; ASCII domain restrictions explicit. | [counting-in-twos/01](#counting-in-twos), [decisions/04](#decisions), [working-the-bits/01](#working-the-bits) |
| [04: Numbers That Aren't Whole](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/working-the-bits/unit-04.mdx#L103) | Explain exact binary fractions versus rounding, finite range and display limits. | Fractions, division and binary place value. Fractional binary places explained; no required floating-point implementation exercise. | [working-it-out/03](#working-it-out), [counting-in-twos/01](#counting-in-twos) |
| [05: Nailing the Point Down](https://github.com/code198x/website/blob/2b9905262dcb7261314b6ef6490db7b8a5c803ed/src/content/curriculum/foundations/working-the-bits/unit-05.mdx#L122) | Decode fixed-point, separate whole-part extraction and choose width/scale/rounding. | Fractions, multiplication/division, bytes and shifts. Unsigned 16-bit scale-256 model specified; comparison with unit 4 and scale-10 alternative. | [working-it-out/03](#working-it-out), [counting-in-twos/03](#counting-in-twos), [working-the-bits/02](#working-the-bits), [working-the-bits/04](#working-the-bits) |

## Understanding checks

35 units contain an explicit Question component or disclosure prompt. Four do not:
Basics 3, Decisions 4, Repeating 1 and From Source to Silicon 2. All four still
have worked examples and troubleshooting. Prompt presence is a discoverability
inventory, not a measure of quality or evidence of independent understanding.
A self-check can also be written in ordinary prose; this count does not classify
every sentence as an assessment or impose a question quota.
