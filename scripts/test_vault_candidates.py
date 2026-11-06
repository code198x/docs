"""Guard loss of candidates and accidental promotion before triage."""

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from check_vault_candidates import FIELDS, check_wants, demand, load_backlog, load_lesson_wants


class BacklogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "candidates.csv"
        self.row = dict.fromkeys(FIELDS, "")
        self.row.update(
            id="VC-0001",
            subject='A title, with "quotes"',
            category="games",
            status="needs-triage",
            why="An existing article needs context.",
            link_from="games/example",
        )

    def write(self, *rows: dict[str, str]) -> None:
        with self.source.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)

    def test_csv_preserves_commas_quotes_and_unicode(self) -> None:
        self.row["why"] = "A reader’s question, with two lines.\nSecond line."
        self.write(self.row)
        self.assertEqual(load_backlog(self.source), [self.row])

    def test_empty_backlog_is_not_success(self) -> None:
        self.write()
        with self.assertRaisesRegex(ValueError, "must not be empty"):
            load_backlog(self.source)

    def test_same_name_in_different_categories_is_distinct(self) -> None:
        self.write(self.row, self.row | {"id": "VC-0002", "category": "groups"})
        self.assertEqual(len(load_backlog(self.source)), 2)

    def test_duplicate_ids_and_subjects_are_rejected(self) -> None:
        for changes, message in [
            ({"subject": "Another name"}, "duplicate ID"),
            ({"id": "VC-00001", "subject": "Another name"}, "duplicate ID"),
            ({"id": "VC-0002"}, "duplicate subject"),
        ]:
            with self.subTest(changes=changes):
                self.write(self.row, self.row | changes)
                with self.assertRaisesRegex(ValueError, message):
                    load_backlog(self.source)

    def test_a_blocked_candidate_names_the_tool_issue_it_waits_on(self) -> None:
        blocked = {"status": "blocked", "triage_notes": "Needs a capture."}
        tool = "https://github.com/emu198x/emu198x/issues/12"
        for changes, message in [
            (blocked, "needs the tool issue"),
            (blocked | {"blocked_by": "https://example.com/issues/1"}, "invalid tool issue URL"),
            ({"blocked_by": tool}, "only a blocked item"),
        ]:
            with self.subTest(changes=changes):
                self.write(self.row | changes)
                with self.assertRaisesRegex(ValueError, message):
                    load_backlog(self.source)
        self.write(self.row | blocked | {"blocked_by": tool})
        self.assertEqual(load_backlog(self.source)[0]["status"], "blocked")

    def test_incomplete_transitions_are_rejected(self) -> None:
        for changes, message in [
            ({"status": "ready"}, "needs notes"),
            (
                {"issue": "https://github.com/code198x/website/issues/1"},
                "triage must precede",
            ),
            ({"status": "in-progress", "triage_notes": "Scoped"}, "needs its issue"),
            (
                {"status": "covered", "triage_notes": "Found coverage"},
                "needs entry paths",
            ),
            (
                {"status": "published", "triage_notes": "Verified live"},
                "needs entry paths",
            ),
        ]:
            with self.subTest(changes=changes):
                self.write(self.row | changes)
                with self.assertRaisesRegex(ValueError, message):
                    load_backlog(self.source)

    def test_issue_urls_cannot_point_to_prs_or_another_repo(self) -> None:
        for url in [
            "https://github.com/code198x/website/pull/1",
            "https://github.com/code198x/docs/issues/1",
        ]:
            with self.subTest(url=url):
                self.write(
                    self.row
                    | {"status": "ready", "triage_notes": "Scoped", "issue": url}
                )
                with self.assertRaisesRegex(ValueError, "invalid website issue"):
                    load_backlog(self.source)

    def test_issue_cannot_be_assigned_twice(self) -> None:
        ready = self.row | {
            "status": "ready",
            "triage_notes": "Scoped",
            "issue": "https://github.com/code198x/website/issues/1",
        }
        self.write(ready, ready | {"id": "VC-0002", "subject": "Another subject"})
        with self.assertRaisesRegex(ValueError, "issue already assigned"):
            load_backlog(self.source)

    def test_website_check_requires_real_referring_and_covered_entries(self) -> None:
        self.write(self.row)
        with self.assertRaisesRegex(ValueError, "directory does not exist"):
            load_backlog(self.source, self.root)
        vault = self.root / "src/content/vault/games"
        vault.mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "missing link_from"):
            load_backlog(self.source, self.root)
        (vault / "example.mdx").write_text("Existing entry", encoding="utf-8")
        covered = self.row | {
            "status": "covered",
            "triage_notes": "Found existing coverage",
            "covered_by": "games/existing",
        }
        self.write(covered)
        with self.assertRaisesRegex(ValueError, "missing covered_by"):
            load_backlog(self.source, self.root)
        (vault / "existing.mdx").write_text("Existing coverage", encoding="utf-8")
        self.assertEqual(load_backlog(self.source, self.root), [covered])

    def test_filter_cannot_hide_invalid_rows(self) -> None:
        self.write(
            self.row,
            self.row | {"id": "VC-0002", "category": "groups", "status": "unknown"},
        )
        result = subprocess.run(
            [
                sys.executable,
                str(Path(__file__).with_name("check_vault_candidates.py")),
                "--file",
                str(self.source),
                "--category",
                "games",
                "--limit",
                "1",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown status", result.stderr)
        self.assertNotIn("PASS", result.stdout)

    def test_website_check_accepts_a_concrete_study_page(self) -> None:
        (self.root / "src/content/vault").mkdir(parents=True)
        study = self.root / "src/pages/vault/studies/simcity/index.astro"
        study.parent.mkdir(parents=True)
        study.write_text("<h1>SimCity</h1>", encoding="utf-8")
        row = self.row | {"link_from": "studies/simcity"}
        self.write(row)
        self.assertEqual(load_backlog(self.source, self.root), [row])

    def test_study_route_does_not_validate_another_missing_page(self) -> None:
        (self.root / "src/content/vault").mkdir(parents=True)
        routes = self.root / "src/pages/vault/studies"
        routes.mkdir(parents=True)
        (routes / "[...page].astro").write_text("Dynamic route", encoding="utf-8")
        self.write(self.row | {"link_from": "studies/missing"})
        with self.assertRaisesRegex(ValueError, "missing link_from"):
            load_backlog(self.source, self.root)

    def test_planned_source_can_refer_to_a_later_candidate(self) -> None:
        vault = self.root / "src/content/vault/games"
        vault.mkdir(parents=True)
        (vault / "example.mdx").write_text("Existing entry", encoding="utf-8")
        planned = self.row | {"link_from": "candidate:VC-0002"}
        parent = self.row | {
            "id": "VC-0002",
            "subject": "A planned theme",
            "category": "culture",
        }
        self.write(planned, parent)
        self.assertEqual(load_backlog(self.source, self.root), [planned, parent])

    def test_planned_source_requires_an_existing_candidate_identity(self) -> None:
        self.write(self.row | {"link_from": "candidate:VC-9999"})
        with self.assertRaisesRegex(ValueError, "unknown planned source candidate"):
            load_backlog(self.source)

    def test_planned_source_cannot_refer_to_itself(self) -> None:
        self.write(self.row | {"link_from": "candidate:VC-0001"})
        with self.assertRaisesRegex(ValueError, "own planned source"):
            load_backlog(self.source)

    def test_candidate_is_not_evidence_of_existing_coverage(self) -> None:
        self.write(
            self.row
            | {
                "status": "covered",
                "triage_notes": "Claimed coverage",
                "covered_by": "candidate:VC-0002",
            },
            self.row | {"id": "VC-0002", "subject": "Another subject"},
        )
        with self.assertRaisesRegex(ValueError, "only allowed in link_from"):
            load_backlog(self.source)

    def test_malformed_planned_source_ids_are_rejected(self) -> None:
        for reference in [
            "candidate:VC-2",
            "candidate:VC-abcd",
            "candidate:VC-0002/extra",
        ]:
            with self.subTest(reference=reference):
                self.write(self.row | {"link_from": reference})
                with self.assertRaisesRegex(ValueError, "invalid planned source"):
                    load_backlog(self.source)

    def test_planned_sources_do_not_hide_missing_existing_pages(self) -> None:
        vault = self.root / "src/content/vault/games"
        vault.mkdir(parents=True)
        (vault / "example.mdx").write_text("Existing entry", encoding="utf-8")
        self.write(
            self.row | {"link_from": "candidate:VC-0002;games/missing"},
            self.row | {"id": "VC-0002", "subject": "A planned theme"},
        )
        with self.assertRaisesRegex(
            ValueError, "missing link_from entry: games/missing"
        ):
            load_backlog(self.source, self.root)

    def test_filter_cannot_hide_an_unknown_planned_source(self) -> None:
        self.write(
            self.row,
            self.row
            | {
                "id": "VC-0002",
                "subject": "Another subject",
                "category": "people",
                "link_from": "candidate:VC-9999",
            },
        )
        result = subprocess.run(
            [
                sys.executable,
                str(Path(__file__).with_name("check_vault_candidates.py")),
                "--file",
                str(self.source),
                "--category",
                "games",
                "--limit",
                "1",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown planned source candidate", result.stderr)
        self.assertNotIn("PASS", result.stdout)

    def test_malformed_columns_are_rejected(self) -> None:
        self.write(self.row)
        original = self.source.read_text(encoding="utf-8")
        self.source.write_text(original.rstrip() + ",unexpected\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "missing or extra fields"):
            load_backlog(self.source)

    def website_fixture(self) -> None:
        """A website with two Vault entries (one reviewed) and two lessons."""
        vault = self.root / "src/content/vault/games"
        vault.mkdir(parents=True)
        (vault / "example.mdx").write_text("---\nreviewed: false\n---\nEntry", encoding="utf-8")
        (vault / "other.mdx").write_text("---\nreviewed: true\n---\nEntry", encoding="utf-8")
        self.lessons = self.root / "src/content/curriculum/core-micro/basic/game"
        self.lessons.mkdir(parents=True)
        self.lesson("unit-01.mdx", "")
        self.lesson("unit-02.mdx", "")

    def lesson(self, name: str, wants: str) -> None:
        (self.lessons / name).write_text(f"---\ntitle: Lesson\n{wants}---\nBody", encoding="utf-8")

    def test_no_referrers_score_zero_and_planned_candidates_count_nothing(self) -> None:
        self.assertEqual(demand(self.row | {"link_from": ""}), 0)
        self.assertEqual(demand(self.row | {"link_from": "candidate:VC-0002"}), 0)

    def test_wants_are_read_in_flow_and_block_form(self) -> None:
        self.website_fixture()
        self.lesson("unit-01.mdx", "wants: ['VC-0001', games/example]\n")
        self.lesson("unit-02.mdx", "wants:\n  - VC-0001\n")
        self.assertEqual(
            load_lesson_wants(self.root),
            {
                "VC-0001": {"core-micro/basic/game/unit-01", "core-micro/basic/game/unit-02"},
                "games/example": {"core-micro/basic/game/unit-01"},
            },
        )

    def test_each_wanting_lesson_weighs_more_than_an_entry(self) -> None:
        row = self.row | {"link_from": "games/example;games/example"}
        wants = {"VC-0001": {"a/b/unit-01"}}
        self.assertEqual(demand(row), 1)
        self.assertEqual(demand(row, wants), 3 + 1)

    def test_demand_follows_the_lesson_and_nothing_is_deleted(self) -> None:
        self.website_fixture()
        self.write(self.row)
        self.lesson("unit-01.mdx", "wants: [VC-0001]\n")
        self.assertEqual(demand(self.row, load_lesson_wants(self.root)), 3 + 1)
        self.lesson("unit-01.mdx", "")
        self.assertEqual(demand(self.row, load_lesson_wants(self.root)), 1)
        self.assertEqual(load_backlog(self.source), [self.row])

    def test_a_lesson_cannot_want_an_unknown_candidate(self) -> None:
        self.website_fixture()
        self.write(self.row)
        self.lesson("unit-02.mdx", "wants: [VC-0042]\n")
        with self.assertRaisesRegex(ValueError, "unit-02 wants unknown candidate VC-0042"):
            check_wants(load_backlog(self.source), load_lesson_wants(self.root))
        result = self.run_checker("--website", str(self.root))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown candidate VC-0042", result.stderr)

    def test_shortlist_ranks_a_wanted_candidate_above_more_links(self) -> None:
        self.website_fixture()
        many_links = self.row | {"subject": "Many", "link_from": "games/other;games/example"}
        wanted = self.row | {"id": "VC-0002", "subject": "Wanted", "link_from": "games/example"}
        self.write(many_links, wanted)
        self.lesson("unit-01.mdx", "wants: [VC-0002]\n")
        result = self.run_checker("--website", str(self.root), "--limit", "2")
        self.assertEqual(result.returncode, 0, result.stderr)
        ranked = [line.split()[0] for line in result.stdout.splitlines() if line.startswith("VC-")]
        self.assertEqual(ranked, ["VC-0002", "VC-0001"])

    def test_wanted_reviews_separates_review_demand_from_satisfied_wants(self) -> None:
        self.website_fixture()
        self.write(self.row)
        self.lesson("unit-01.mdx", "wants: [games/example, games/other]\n")
        result = self.run_checker("--website", str(self.root), "--wanted-reviews")
        self.assertEqual(result.returncode, 0, result.stderr)
        review, satisfied = result.stdout.split("reviewed entries lessons still only want")
        self.assertIn("games/example", review)
        self.assertNotIn("games/other", review)
        self.assertIn("games/other", satisfied)
        self.assertNotIn("games/example", satisfied)

    def run_checker(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(Path(__file__).with_name("check_vault_candidates.py")),
             "--file", str(self.source), *args],
            capture_output=True, text=True, check=False,
        )

    def test_scope_names_a_region_or_a_decade(self) -> None:
        for scope, message in [
            ("Region:USSR", "invalid scope"),
            ("region:ussr;region:ussr", "duplicate scope"),
            ("period:1965", "invalid scope"),
            ("era:early", "invalid scope"),
        ]:
            with self.subTest(scope=scope):
                self.write(self.row | {"scope": scope})
                with self.assertRaisesRegex(ValueError, message):
                    load_backlog(self.source)
        good = self.row | {"scope": "region:east-germany;period:1960s"}
        self.write(good)
        self.assertEqual(load_backlog(self.source), [good])

    def test_lanes_select_world_computing_and_early_subjects(self) -> None:
        rows = [
            self.row | {"id": "VC-0001", "subject": "Soviet", "scope": "region:ussr"},
            self.row | {"id": "VC-0002", "subject": "British", "scope": "region:uk"},
            self.row | {"id": "VC-0003", "subject": "Early", "scope": "period:1960s;region:us"},
            self.row | {"id": "VC-0004", "subject": "Unscoped"},
        ]
        self.write(*rows)
        for lane, expected in [("world", ["VC-0001"]), ("early", ["VC-0003"])]:
            with self.subTest(lane=lane):
                result = self.run_checker("--lane", lane)
                self.assertEqual(result.returncode, 0, result.stderr)
                shown = [line.split()[0] for line in result.stdout.splitlines() if line.startswith("VC-")]
                self.assertEqual(shown, expected)

    def test_world_lane_takes_regions_in_turn(self) -> None:
        def row(n: int, region: str, refs: int) -> dict[str, str]:
            sources = ";".join(f"games/source-{i}" for i in range(refs))
            return self.row | {
                "id": f"VC-{n:04}", "subject": f"S{n}", "scope": f"region:{region}", "link_from": sources,
            }
        self.write(
            row(1, "japan", 5), row(2, "japan", 4), row(3, "japan", 3),
            row(4, "poland", 2), row(5, "ussr", 1),
            row(6, "uk", 9),  # not in the world lane at all
        )
        result = self.run_checker("--lane", "world")
        self.assertEqual(result.returncode, 0, result.stderr)
        shown = [line.split()[0] for line in result.stdout.splitlines() if line.startswith("VC-")]
        # Round one takes each region's strongest, strongest region first.
        self.assertEqual(shown, ["VC-0001", "VC-0004", "VC-0005", "VC-0002", "VC-0003"])


if __name__ == "__main__":
    unittest.main()
