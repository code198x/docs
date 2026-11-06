"""Guard the content queue's references to both queues and its status rules."""

import csv
import tempfile
import unittest
from pathlib import Path

import check_vault_candidates
from check_content_candidates import FIELDS, ROOT, load_queue

TOOL_ISSUE = "https://github.com/emu198x/emu198x/issues/12"


class QueueTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "plans").mkdir()
        (self.root / "plans" / "plan.md").write_text("plan\n", encoding="utf-8")
        self.vault = self.root / "vault.csv"
        vault_row = dict.fromkeys(check_vault_candidates.FIELDS, "")
        vault_row.update(
            id="VC-0001",
            subject="Multicolour",
            category="techniques",
            status="needs-triage",
            why="Lessons mention it.",
            link_from="techniques/raster-effects",
        )
        self.write(self.vault, check_vault_candidates.FIELDS, vault_row)
        self.source = self.root / "content.csv"
        self.row = dict.fromkeys(FIELDS, "")
        self.row.update(
            id="CC-0001",
            surface="production",
            subject="A demo",
            system="sinclair-zx-spectrum",
            why="The pilot.",
            status="needs-triage",
        )

    def write(self, path: Path, fields: list[str], *rows: dict[str, str]) -> None:
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def load(self, *rows: dict[str, str]) -> list[dict[str, str]]:
        self.write(self.source, FIELDS, *rows)
        return load_queue(self.source, self.vault, self.root)

    def row_with(self, **changes: str) -> dict[str, str]:
        return {**self.row, **changes}

    def rejects(self, message: str, *rows: dict[str, str]) -> None:
        with self.assertRaisesRegex(ValueError, message):
            self.load(*rows)

    def test_the_real_queue_validates_against_the_real_vault_queue(self) -> None:
        rows = load_queue(ROOT / "content-candidates.csv", ROOT / "vault-candidates.csv")
        self.assertTrue(rows)

    def test_from_may_cite_either_queue_and_a_docs_file(self) -> None:
        later = self.row_with(id="CC-0002", subject="An article", surface="from-the-metal")
        rows = self.load(self.row_with(**{"from": "VC-0001;CC-0002;docs:plans/plan.md"}), later)
        self.assertEqual(len(rows), 2)

    def test_from_naming_a_missing_vault_candidate_fails(self) -> None:
        self.rejects("unknown candidate in from: VC-0002", self.row_with(**{"from": "VC-0002"}))

    def test_from_naming_a_missing_content_candidate_fails(self) -> None:
        self.rejects("unknown candidate in from: CC-0009", self.row_with(**{"from": "CC-0009"}))

    def test_from_cannot_cite_itself(self) -> None:
        self.rejects("cannot come from itself", self.row_with(**{"from": "CC-0001"}))

    def test_from_naming_a_missing_docs_file_fails(self) -> None:
        self.rejects("missing docs file", self.row_with(**{"from": "docs:plans/nope.md"}))

    def test_from_rejects_an_unknown_form(self) -> None:
        self.rejects("invalid from reference", self.row_with(**{"from": "lesson 4"}))

    def test_a_production_needs_its_system(self) -> None:
        self.rejects("needs its system", self.row_with(system=""))

    def test_an_unknown_surface_fails(self) -> None:
        self.rejects("unknown surface", self.row_with(surface="vault"))

    def test_triage_precedes_the_work_issue(self) -> None:
        self.rejects(
            "triage must precede",
            self.row_with(issue="https://github.com/code198x/website/issues/1"),
        )

    def test_work_in_progress_needs_its_issue(self) -> None:
        self.rejects("needs its issue URL", self.row_with(status="in-progress", triage_notes="Agreed."))

    def test_a_blocked_item_names_the_tool_issue_it_waits_on(self) -> None:
        self.rejects("needs the tool issue", self.row_with(status="blocked", triage_notes="Waits."))

    def test_only_a_blocked_item_names_a_blocking_issue(self) -> None:
        self.rejects("only a blocked item", self.row_with(blocked_by=TOOL_ISSUE))

    def test_a_blocking_issue_must_be_a_family_tool_issue(self) -> None:
        self.rejects(
            "invalid tool issue URL",
            self.row_with(status="blocked", triage_notes="Waits.", blocked_by="https://example.com/1"),
        )

    def test_several_items_can_wait_on_one_tool_issue(self) -> None:
        blocked = {"status": "blocked", "triage_notes": "Waits.", "blocked_by": TOOL_ISSUE}
        rows = self.load(
            self.row_with(**blocked),
            self.row_with(id="CC-0002", subject="Another demo", **blocked),
        )
        self.assertEqual(len(rows), 2)

    def test_numeric_ids_cannot_collide(self) -> None:
        self.rejects("duplicate ID", self.row, self.row_with(id="CC-00001", subject="Other"))

    def test_resolved_coverage_needs_website_paths(self) -> None:
        self.rejects("needs website paths", self.row_with(status="published", triage_notes="Done."))

    def test_an_empty_queue_fails(self) -> None:
        self.rejects("must not be empty")


if __name__ == "__main__":
    unittest.main()
