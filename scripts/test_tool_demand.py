"""Guard the ranking of tool issues and the block and unblock round trip."""

import csv
import tempfile
import unittest
from pathlib import Path

import check_content_candidates as content
import check_vault_candidates as vault
from tool_demand import Queue, block, blockers, check_issues, unblock

EMU = "https://github.com/emu198x/emu198x/issues/12"
ASM = "https://github.com/asm198x/asm198x/issues/7"
TODAY = "2026-11-06"


def issues(**states: dict) -> callable:
    """A fake GitHub: issue URL → the fields `gh api` would return."""
    known = {EMU: {"state": "open"}, ASM: {"state": "open"}} | {
        url: state for url, state in (({"emu": EMU, "asm": ASM}[k], v) for k, v in states.items())
    }

    def lookup(url: str) -> dict:
        if url not in known:
            raise LookupError(f"{url}: Not Found")
        return known[url]

    return lookup


class ToolDemandTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.vault_file = root / "vault.csv"
        self.vault_row = dict.fromkeys(vault.FIELDS, "") | {
            "id": "VC-0001",
            "subject": "Multicolour",
            "category": "techniques",
            "status": "blocked",
            "why": "Needs a capture.",
            "link_from": "techniques/raster-effects;systems/pentagon",
            "triage_notes": "Scoped.",
            "blocked_by": EMU,
        }
        self.write(self.vault_file, vault.FIELDS, [self.vault_row])
        self.content_file = root / "content.csv"
        self.content_rows = [
            dict.fromkeys(content.FIELDS, "")
            | {
                "id": f"CC-000{n}",
                "surface": "production",
                "subject": f"Demo {n}",
                "system": "sinclair-zx-spectrum",
                "why": "The pilot.",
                "status": "blocked",
                "triage_notes": "Scoped.",
                "blocked_by": url,
            }
            for n, url in ((1, EMU), (2, ASM), (3, ASM))
        ]
        self.content_rows[0]["issue"] = "https://github.com/code198x/website/issues/1"
        self.write(self.content_file, content.FIELDS, self.content_rows)

    def write(self, path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    def content_queue(self) -> Queue:
        queue = Queue(
            self.content_file,
            content.FIELDS,
            lambda: content.load_queue(self.content_file, self.vault_file, self.content_file.parent),
        )
        queue.load()
        return queue

    def rows(self) -> list[dict[str, str]]:
        return vault.load_backlog(self.vault_file) + self.content_queue().rows

    def test_issues_rank_by_items_blocked_then_vault_demand(self) -> None:
        rows = self.rows()
        # Two items each: the tie falls to the Vault demand behind them (two linking entries).
        ranked = blockers(rows)
        self.assertEqual([(b.url, b.items) for b in ranked], [(EMU, ["VC-0001", "CC-0001"]), (ASM, ["CC-0002", "CC-0003"])])
        self.assertEqual([b.demand for b in ranked], [2, 0])
        # More items beat more demand.
        ranked = blockers([rows[0], rows[2], rows[3]])
        self.assertEqual([(b.url, len(b.items)) for b in ranked], [(ASM, 2), (EMU, 1)])

    def test_a_missing_issue_or_a_pull_request_fails_the_check(self) -> None:
        found = blockers(self.rows())
        check_issues(found, issues())
        with self.assertRaisesRegex(ValueError, "CC-0002, CC-0003: blocking issue not found"):
            check_issues(found, lambda url: issues()(url) if url == EMU else issues()("nowhere"))
        with self.assertRaisesRegex(ValueError, "is a pull request"):
            check_issues(found, issues(emu={"state": "open", "pull_request": {"url": "…"}}))

    def test_closing_an_issue_returns_its_items_to_work(self) -> None:
        queue = self.content_queue()
        released, unresolved = unblock(queue.rows, issues(emu={"state": "closed", "state_reason": "completed"}), TODAY)
        self.assertEqual((released, unresolved), (["CC-0001"], []))
        row = queue.rows[0]
        # Work with an issue goes back in progress; the note demands a re-run.
        self.assertEqual((row["status"], row["blocked_by"]), ("in-progress", ""))
        self.assertIn("Run the item's gates again", row["triage_notes"])
        queue.save()
        self.assertEqual(self.content_queue().rows[0]["status"], "in-progress")

        rows = vault.load_backlog(self.vault_file)
        unblock(rows, issues(emu={"state": "closed", "state_reason": "completed"}), TODAY)
        self.assertEqual(rows[0]["status"], "ready")

    def test_open_or_unfixed_issues_keep_items_blocked(self) -> None:
        for state in ({"state": "open"}, {"state": "closed", "state_reason": "not_planned"}, {"state": "closed", "state_reason": "duplicate"}):
            with self.subTest(state=state):
                queue = self.content_queue()
                released, unresolved = unblock(queue.rows, issues(asm=state, emu=state), TODAY)
                self.assertEqual(released, [])
                self.assertEqual(len(unresolved), 0 if state["state"] == "open" else 3)
                self.assertTrue(all(row["status"] == "blocked" for row in queue.rows))

    def test_a_failing_rerun_puts_the_item_back_with_a_note(self) -> None:
        queue = self.content_queue()
        unblock(queue.rows, issues(emu={"state": "closed", "state_reason": "completed"}), TODAY)
        block(queue.rows, "CC-0001", EMU, "Still drops a frame on the 128K.", TODAY)
        queue.save()
        row = self.content_queue().rows[0]
        self.assertEqual((row["status"], row["blocked_by"]), ("blocked", EMU))
        self.assertTrue(row["triage_notes"].endswith(f"Blocked on {TODAY} by {EMU}: Still drops a frame on the 128K."))

    def test_blocking_needs_a_reason_and_live_work(self) -> None:
        queue = self.content_queue()
        with self.assertRaisesRegex(ValueError, "say why"):
            block(queue.rows, "CC-0001", EMU, "", TODAY)
        queue.rows[1] |= {"status": "deferred", "blocked_by": ""}
        with self.assertRaisesRegex(ValueError, "not deferred"):
            block(queue.rows, "CC-0002", EMU, "Waits.", TODAY)

    def test_a_save_that_fails_validation_restores_the_file(self) -> None:
        queue = self.content_queue()
        before = self.content_file.read_bytes()
        queue.rows[0]["blocked_by"] = "https://example.com/1"
        with self.assertRaisesRegex(ValueError, "invalid tool issue URL"):
            queue.save()
        self.assertEqual(self.content_file.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
