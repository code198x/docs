# Character codes: learner tasks

This trial is prepared but has not been run with a learner. Read [A Letter Is a
Number](https://code198x.com/foundations/working-the-bits/unit-03/) using the pilot
version supplied by the observer. No previous BASIC or assembly lesson is required.
Keep the page's prediction answers closed until you have made your prediction.
The examples use ASCII letters and digits. `SHOW` displays a result; `CODE`
gets a character's code; `CHARACTER` gets the character for a code. These are
teaching notation, not a program to paste into Spectrum BASIC.

1. Before opening either answer, predict `CODE "7"`, then `CODE "7" - CODE "0"`.
   Explain why the answers differ. What would subtracting `CODE "0"` from
   `CODE "A"` tell you about whether A is a digit?
2. Explain the difference between the number 7, the character "7", its ASCII
   code and the shape drawn on screen. If a second machine uses a different
   encoding, what must you check before reusing a code?
3. You receive the strings `"7"`, `"73"`, `"A"` and `""`. Decide which can use
   one-digit subtraction. Write the checks before the subtraction. Spectrum
   BASIC's `CODE` takes the first character, returning 0 for an empty string;
   predict `CODE "73"`. Why does that fail to convert the whole number 73?
4. `BITOR 32` sets the bit worth 32. Predict its result for ASCII `"A"`,
   `"a"`, `"7"` and `"@"`. The page gives their codes. Open the answer and
   diagnose this claim: “If the result changed, the input must be a letter.”
5. Modify the case-conversion idea to accept only ASCII capital letters. State
   what happens at A, Z and the characters just outside their code range.
   How would you convert only lower-case ASCII letters to capitals?
6. Create a small converter in words, a flow chart or code you already know.
   It should accept exactly one ASCII digit and return its numeric value;
   reject empty, longer and non-digit inputs. Give one successful example and
   three rejected examples. Explain why checking the result after subtraction
   is not enough if you never checked the string length.

Optional connections, after the core tasks:

- Follow the stored-greeting link using the keyboard. Identify the quoted text
  and the variable holding it. Explain what makes this a string. Return to the
  character lesson. Running BASIC is optional; its opening explains entry.
- Follow the PETSCII chart link. Find the example that prints A and the example
  that writes A directly into screen memory. Explain why their numbers differ
  and which table each operation needs. Return to the lesson. You do not need
  a C64 or an assembly program for this reading comparison.

Tell the observer where the lesson left you guessing. A wrong prediction is
useful evidence; there is no time target and no requirement to finish everything.
