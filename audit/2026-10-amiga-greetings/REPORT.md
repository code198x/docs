# First Amiga language greetings: bounded runtime trial

AMOS Professional 2.00 and AmiBlitz v3.13.0b both completed a bounded greeting,
edit, syntax-error and repair loop on the named configuration. AmiBlitz required
plain-text `.ab3` import and **RuntimeDebug=0** to show the greeting while
waiting for a click. **This qualifies the first greeting route only.**
[Docs #94](https://github.com/code198x/docs/issues/94),
[website #766](https://github.com/code198x/website/issues/766) and
umbrella #116 track the paired
lesson corrections and the remaining wider review.

## Method and identities

On 16 October 2026, manual keyboard entry and visual inspection used the native
FS-UAE 3.2.35 macOS app. The machine was PAL A1200, 68020, no FPU/MMU/JIT,
2 MB chip and 8 MB fast RAM. Kickstart was A1200 3.1 rev 40.68; Workbench was
3.1 rev 40.42. Existing local media were copied into the isolated workspace.
The AmiBlitz IDE additionally requested the matching Fonts disk, then opened
when its copy was mounted in DF1. A host directory was mounted as Tools.

[Preflight identities](preflight.json) distinguish the initially inspected
Homebrew CLI binary from the **native app binary actually used**, and hash the
ROM/Workbench/runtime inputs. [Log excerpts](emulator-log-excerpts.txt) confirm
the active CPU and RAM. [Acquisition](acquisition.json) records the two official
archives, pinned revisions/releases, sizes and SHA-256 hashes. Both language
downloads were explicitly approved as isolated test dependencies. No system
installation, additional package or licensed-media download was performed.

The AMOS repository is pinned at
[533b4b1](https://github.com/AOZ-Studio/AMOS-Professional-Official/tree/533b4b1f5acd604814513f78e02c7b4796cb0531).
The splash identified AMOS Professional Version 2.00. AmiBlitz came from its
[official v3.13.0b release](https://github.com/AmiBlitz/AmiBlitz3/releases/tag/v3.13.0b).
The fresh retry splash identified **AmiBlitz3 V3.13.0 (24.06.2026) Build 3654**;
the runtime debugger identified **RED Debugger 3.11.4**. Keep the archive release
and displayed IDE version distinct. No redistribution right for unrelated disk images
is inferred from a source licence.

[Source identities](source.json) bind the retained [AMOS](inputs/hello.amos) and
[Blitz](inputs/hello.bb2) listings to the inspected sample revision. AMOS was
manually entered and checked on screen. Blitz was first manually entered, then
loaded from an exact host copy after input/control mistakes. This is manual
configuration-specific evidence, not an automated source-to-runtime assertion.
Screenshots were inspected in the session; no screenshot files were retained.

## AMOS: observed loop

Launching `Tools:AMOS/AMOSPro` directly from Workbench produced **Cannot find
AMOS.library.** The pinned loader source `+B.s` searches
`APSystem/amos.library` relative to its current directory. The retained
[two-line script](inputs/start-amos) changes directory before launch; that
route opened the editor. It is a file-folder distribution, not a bootable ADF.

F1 on the three maintained lines displayed **Hello from AMOS!** on orange.
A key at `Wait Key` produced **End of program at line 3.**, offering
**Direct mode [ESC]** and **Editor [RETURN]**. Return restored the editor.
Changing the string to **Edited Hello from AMOS!** and pressing F1 displayed
those words.

Deleting the closing quote did **not** cause a syntax error. F1 still displayed
the edited greeting, and the quote reappeared in the editor. A trailing `+`
after the closing quote did produce the red **Syntax error.** status. Removing
that `+` and pressing F1 restored **Edited Hello from AMOS!**. This is a useful
negative and recovery check; an unclosed-quote exercise would not test that
behaviour on this version.

## AmiBlitz: first attempt boundary

The retained [launcher](inputs/start-blitz) uses `-PED` and adds the package's
Libs drawer to LIBS:. Without `-PED`, shell launch printed CLI help. With it,
the IDE requested Fonts; adding the existing matching Fonts disk let PED open.
The upstream release README states a 68020, 8 MB RAM for small work (12 MB for
serious development), 35 MB disk, Workbench 2.1 or 2.04 with locale.library, and
the included wizard.library. These are IDE requirements, not output requirements.
The bundled guide has older, different disk/OS wording; the release README
is the requirements source for this trial.

The lesson's right-Amiga+X **cut the current line**. Source inspection at
[pinned PED.ab3](https://github.com/AmiBlitz/AmiBlitz3/blob/5dd815f880d72c5285b380ef3ddebfa5766d0626/Sourcecodes/Amiblitz3/PED/PED.ab3#L14116)
corroborates Cut on X and Compile & Run on #. After loading the exact maintained
file and visually checking all four lines, right-Amiga+# changed the status
to **Compiling…**. The next screenshot failed with
`Computer Use server error -10005: cgWindowNotFound`. App rebinding failed with
the same error while the emulator process remained present. That does not
establish whether the guest, emulator or capture connection caused the loss.
That first attempt established no successful compile, greeting, edited output or
fault/repair pass.
Further blind UI retries stopped at this boundary.

## AmiBlitz: fresh retry on 16 October

The [retry observations](retry/observations.json) retain identical archive,
emulator, media and runtime hashes. Window capture remained available throughout;
the suggestion that lunch caused the earlier loss remains a hypothesis.

Loading the maintained ASCII `hello.bb2` displayed all four lines, but compiling
reported **Garbage at the end of line** and **Hint: Maybe some unwanted
characters pending?** on the first `NPrint`. The release's bundled
`Docs/AmiBlitz3.guide`, FILEFORMAT and SMARTTOKENIZATION sections, distinguish
tokenized binary `.bb2` from plain-text `.ab2`/`.ab3` input. Copying the exact
same bytes to [hello.ab3](retry/inputs/hello.ab3) and loading that file gave
highlighted keywords and a successful compile. This diagnoses the import error;
it does not justify renaming genuine binary BB2 files. An extra Return after
loading inserted a blank first line, placing the first statement on line 2.

Right-Amiga+# built the executable, then a blank Sourcecode View appeared.
After a left click, output showed **Hello from Blitz!**, **Compiled, not
interpreted.**, **Program terminated.** and **Press <ENTER> to return to the
IDE ...**. Return restored the source listing. Editing the first string in PED
to **Edited Hello from Blitz!**, compiling again and clicking showed the edited
output and the same termination prompt. The output while waiting at `MouseWait`
was not observed, so this does not establish the intended waiting-state display.
The cause of the blank view/output handoff remains unresolved.

Appending `+` after the first string's closing quote and compiling produced
**Syntax error!** with the actual failing line in the Compile Error requester.
Return then BackSpace, Escape and Space did not visibly dismiss it or establish
a repair. The bounded trial stopped there. **No recovered rerun or complete
Blitz edit/error/repair loop is claimed.** Host-prepared edited/fault files were
not used as substitutes for that missing observation.

## AmiBlitz: recovery and visible waiting output

The [recovery observations](recovery/observations.json) record a fresh session
with matching runtime/media hashes. Launching the plain-text script directly
reported **file is not executable** and **failed returncode 10**. From a fresh
Workbench session, **Execute Tools:start-blitz** opened PED. Use the explicit
`Execute` command; subsequent keys in the first failed launch had gone into its
output window, so that attempt was reset.

A trailing `+` produced **Syntax error!**. **Left-Amiga+V** dismissed the Compile
Error requester, restoring the affected source line. Removing the plus and
rerunning restored the baseline output after a click. PED's pinned
[error handler](https://github.com/AmiBlitz/AmiBlitz3/blob/5dd815f880d72c5285b380ef3ddebfa5766d0626/Sourcecodes/Amiblitz3/PED/PED.ab3#L10969)
uses the [error include's EasyRequestArgs](https://github.com/AmiBlitz/AmiBlitz3/blob/5dd815f880d72c5285b380ef3ddebfa5766d0626/Sourcecodes/Includes/error.include.ab3#L223)
with an OK gadget. The shortcut agrees with the
[AmigaOS requester documentation](https://wiki.amigaos.net/wiki/Intuition_Requesters).
It is not a generic Load shortcut: in the file picker, Left-Amiga+V selected
Volumes during this trial. Loading succeeded with the correct Drawer/File
fields and Return.

The retained [plain-console fixture](recovery/plain.ab3) prepends a minimal XTRA
header to the unchanged four maintained statements. The bundled FILEFORMAT
section documents the header and `RuntimeDebug` field. Loading it hid the
header and changed PED's D indicator to dark. Compile & Run then opened
**AmiBlitz3 Console Output** showing both greeting lines **before any guest
click**, unlike the debugger-enabled runs. The emulator menu was opened and
closed for inspection without sending a click to the guest. This isolates a
usable source configuration; it does not establish the internals of the
previous blank-view behaviour.

A left click produced **Program terminated.** and **Press <ENTER> to return to
the IDE ...**; Return restored PED. Editing the first string in PED produced
**Edited Hello from Blitz!** while waiting, with the second line unchanged.
Appending `+` gave the real syntax error again, dismissed with Left-Amiga+V.
The first repair attempt cleared the first line and the next run showed only
the second output line. Inspection caught this: it is a failed edit, not a
pass. Shift-like input had also produced an uppercase, punctuated filename;
a stuck qualifier is a hypothesis, not a diagnosed guest bug. After releasing
both shift modifiers and retyping the corrected first line in PED, visual
inspection confirmed all four statements. The rebuilt program displayed both
expected lines while waiting, then returned through click and Return to PED.
No host-prepared edited program replaced this in-editor recovery.

## Harness limits and next action

[Observation records](observations.json) include failures as well as passes.
Long host typing calls dropped characters, so text was entered in small chunks
and visually checked. Default keyboard joystick mapping consumed AMOS arrow
keys; No host device restored them. Host End opened Amiga Help. AmiBlitz
navigation/requester attempts also produced unwanted source edits and one
**No file handle set!!** request; those were discarded before loading the exact
sample. The first LHA extraction failed on a French directory name; a fresh
extraction using the already-installed 7z completed with “Everything is Ok”.

The paired website draft can now name both runtime configurations and the
observed launch/import/compile/return/error-repair steps. The Blitz route uses
plain-text `.ab3` with the tested header, PED and right-Amiga+#. Original Blitz
BASIC 2/Ted and whole-course AmiBlitz compatibility remain untested. The earlier
failed attempts remain in the observation records; the final route does not
qualify those other configurations.

Only the baseline, string edit and stated fault/recovery are qualified for
each language on its recorded configuration. No save/reopen, second-Print extension, later unit, timing, audio,
assistive-technology, physical-touch or original-hardware claim follows. No
learner was available; understanding, retention and unaided transfer remain
unknown. The parent education issues remain open.

The [follow-up validation](recovery/validation.json) records the clean 2,459-page
production build and generated-page checks. The setup page reported no horizontal
overflow at 1,440 px. Browser screenshot/CDP timeouts prevented completing the
new wide/narrow visual and click-through review; earlier AMOS browser checks do
not qualify the new Blitz pages. Keep the paired website PR in draft until that
review is completed.
