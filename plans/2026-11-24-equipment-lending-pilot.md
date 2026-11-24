# Pilot plan: where is the kit, and is it available?

**Status:** draft for review. The technical examples were reproduced; this is not a learner trial or a published lesson.

One optional bridge for [the cross-era CRUD pilot](https://github.com/stevehill1981/198x/issues/163) and a candidate data/I/O example for [the concept map](https://github.com/stevehill1981/198x/issues/162). A fictional equipment desk needs to find a tag and avoid promising the same kit twice. Use index cards, then Sinclair ZX Spectrum BASIC, then local, in-memory SQLite. All equipment and names are invented. This is not a proposal for a database, new dependency or service in 198x or its semantic web work. No web framework or employer system is involved.

## 1. Predict with eight cards; inspect the Spectrum

Lay out `A01` through `A08` in order. Beside each tag put `---` (available), except `A08`, which has the borrower code `JOE`. Predict how many tags a forward search compares for `A01`, `A08` and absent `A09`. If moving `A08` forward saves work for that tag, what happens to the tags moved back and to absent tags? This part can be done entirely on paper.

Use an idle 48K Spectrum or an already prepared emulator. [Meet BASIC Unit 2](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-02-remember-and-save/) introduces the ROM editor and tape controls; the [Sinclair BASIC manual, Chapter 12](https://worldofspectrum.org/ZXBasicManual/zxmanchap12.html) explains fixed-length string arrays and slices. The layout is eight rows with six characters each: three for tag and three for borrower. The 48 character positions exclude array metadata, the program and other variables. Fixed-width fields simplify offsets but cannot represent every useful name; overlong assignments are truncated.

```basic
10 DIM a$(8,6)
20 FOR i=1 TO 8
30 LET a$(i)="A0"+STR$ i+"---": NEXT i
35 LET a$(8,4 TO 6)="JOE"
40 INPUT "Asset tag? ";k$
50 FOR i=1 TO 8
60 IF a$(i,1 TO 3)=k$ THEN GO TO 110
70 NEXT i
80 PRINT "NOT FOUND AFTER ";i-1;" CHECKS"
90 STOP
110 PRINT a$(i,4 TO 6);" AFTER ";i;" CHECKS"
```

Run once per tag. Observed: `--- AFTER 1 CHECKS`, `JOE AFTER 8 CHECKS`, and `NOT FOUND AFTER 8 CHECKS`. The final `STOP` message is deliberate on the missing path. `NEXT` has already stepped beyond row 8, so the miss reports `i-1`. These are comparisons, not timing.

At the prompt after a run, enter `LET a$(8,4 TO 6)="PAT"` and then `GO TO 40`. `A08` now gives `PAT AFTER 8 CHECKS`. Another `RUN` would replace the array with the exercise fixture. That is useful for a reset but wrong for keeping an edit.

**Optional storage check.** Save the array by itself with `SAVE "loans" DATA a$()` ([Sinclair BASIC manual, Chapter 20](https://worldofspectrum.org/ZXBasicManual/zxmanchap20.html)). In the rehearsal, the ROM produced a 78-byte TAP: 19-byte header block and 55-byte data block, plus two two-byte block lengths. The data block holds the 48 characters, five dimension bytes, a flag and a checksum. Change the borrower to `ZZZ` and confirm it with `GO TO 40`. Then mount the saved image, enter `LOAD "loans" DATA a$()` and start tape playback. The ROM reports `0 OK`; `GO TO 40` then reports `PAT AFTER 8 CHECKS` for `A08`, without reinitialising or replacing the program. The two recorded saves had matching SHA-256 `6f25bc77dc3440d2a13c59d6deea4d30912575db4bb25f278b4fc2d2e3deb795`. No tape or ROM bytes are included in this plan.

**Technical rehearsal:** Emu198x Spectrum 0.48.5, Linux x86-64, `spectrum_issue3_48k` (PAL), with a separately supplied stock 48K ROM (SHA-256 `d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`). Released executable SHA-256 `ca91b6aaac56b07808a104e8d1968fb9c6552cf660ed900e69c370563e455e7f`. The listing (SHA-256 `c5d1d93dc0647a868a1738cd56faf22f4ef80cff50ef83cdb515754a96a4c74d`, LF with final newline) was entered through the ROM keyboard, without injecting bytes. All eleven line numbers were confirmed in RAM before execution. No physical machine or analogue-cassette claim.

## 2. Ask SQLite the same kind of question

Open `sqlite3 :memory:` or another local SQLite client in autocommit mode, as the shell is by default. Keep the same session for the whole exercise. Run the setup once; repeat the same two queries in each pass.

```sql
CREATE TABLE gear(asset_tag TEXT NOT NULL PRIMARY KEY, site TEXT NOT NULL, borrower TEXT);
CREATE TABLE checkout_log(asset_tag TEXT NOT NULL, borrower TEXT NOT NULL);
WITH RECURSIVE seq(n) AS (VALUES(1) UNION ALL SELECT n+1 FROM seq WHERE n<8192)
INSERT INTO gear
SELECT printf('A%05d',n),printf('S%02d',n%16),NULL FROM seq;

EXPLAIN QUERY PLAN
SELECT asset_tag FROM gear WHERE site='S07' ORDER BY asset_tag LIMIT 5;
SELECT asset_tag FROM gear WHERE site='S07' ORDER BY asset_tag LIMIT 5;
```

Predict whether ordering alone lets the engine skip the other sites. Compare before either added index, after `CREATE INDEX gear_site_tag ON gear(site, asset_tag);`, and after also adding `CREATE INDEX gear_site ON gear(site);`. An SQLite shell that supports `.stats vmstep` can show work for the `SELECT` itself, not for the explain statement. See SQLite’s [plan guide](https://www.sqlite.org/eqp.html) and [statement counters](https://www.sqlite.org/c3ref/c_stmtstatus_counter.html).

| Condition | Plan observed in SQLite 3.46.1 | Virtual-machine steps |
| --- | --- | ---: |
| Primary-key index only | Scan in asset-tag index order until the limit | 308 |
| Composite index | Search the covering index for `site=?` | 32 |
| Also add site-only index | Same covering search | 32 |

All three return `A00007`, `A00023`, `A00039`, `A00055`, `A00071` in that order. Counts came from `sqlite3_stmt_status(..., SQLITE_STMTSTATUS_VM_STEP, 0)` for each fresh, completed statement in the local SQLite 3.46.1 library. Python’s SQLite 3.53.1 independently returned the same rows and plan structure. Exact text and counters can vary. Steps are not elapsed time, disk reads, or evidence that the first query examined all 8,192 rows. The extra site-only index did not help this query but still consumes space and adds work when its keys change.

## 3. Change availability without losing correctness

Predict whether the second checkout overwrites the first. Check `changes()` immediately after each update. Then update and log a different item inside one transaction. The log insert is only for this fixed fixture after confirming the update affected one row; an application must check that result before logging success.

```sql
UPDATE gear SET borrower='ADA' WHERE asset_tag='A00007' AND borrower IS NULL;
SELECT changes();
UPDATE gear SET borrower='BOB' WHERE asset_tag='A00007' AND borrower IS NULL;
SELECT changes();
SELECT borrower FROM gear WHERE asset_tag='A00007';

BEGIN;
UPDATE gear SET borrower='KIM' WHERE asset_tag='A00023' AND borrower IS NULL;
SELECT changes();
-- Continue in this fixture only if changes() is 1.
INSERT INTO checkout_log VALUES ('A00023','KIM');
SELECT borrower, (SELECT count(*) FROM checkout_log)
  FROM gear WHERE asset_tag='A00023';
ROLLBACK;
SELECT borrower, (SELECT count(*) FROM checkout_log)
  FROM gear WHERE asset_tag='A00023';
```

Observed: `1`, `0`, `ADA`; the second asset gives `1`, then `KIM, 1` inside the transaction and `NULL, 0` after rollback. See SQLite’s [changes counter](https://www.sqlite.org/c3ref/changes.html) and [transaction rules](https://www.sqlite.org/lang_transaction.html). This proves a guard and rollback on one connection, not simultaneous writers, busy handling, disk durability or production readiness.

The array makes fixed storage and scan work visible. SQLite can choose an access path, enforce a unique tag and undo related writes together. This is a slice of CRUD (create/read/update), not a full application. Returning an item is not deleting it from a catalogue.

## Extension and learner check

Without the answer key, ask the learner to design a return operation that leaves the kit in the catalogue and cannot return an item checked out to someone else. Have them predict and test a second return. Ask why the site-only index did not help, and what new workload might change the answer. Comparing repeated point queries with a single batch, including statement count and how many rows the client keeps, is an optional unmeasured extension.

For a later, consenting learner, record the prediction before showing the result, what evidence they use to explain it and what type of help they request. Offer paper or a prepared disposable emulator. Keep identifying details out of any shared record. Editorial review, learner trial and curriculum placement remain pending; leave #163 open.
