"""Guard loss of candidates and accidental promotion before triage."""

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from check_vault_candidates import FIELDS, demand, load_backlog


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
        """A website with two Vault entries and one lesson."""
        vault = self.root / "src/content/vault/games"
        vault.mkdir(parents=True)
        for name in ("example", "other"):
            (vault / f"{name}.mdx").write_text("Entry", encoding="utf-8")
        lesson = self.root / "src/content/curriculum/core-micro/basic/game"
        lesson.mkdir(parents=True)
        (lesson / "unit-01.mdx").write_text("Lesson", encoding="utf-8")

    def test_no_referrers_score_zero_and_planned_candidates_count_nothing(self) -> None:
        self.assertEqual(demand(self.row | {"link_from": ""}), 0)
        self.assertEqual(demand(self.row | {"link_from": "candidate:VC-0002"}), 0)

    def test_lessons_weigh_more_than_entries_and_repeats_count_once(self) -> None:
        row = self.row | {
            "link_from": "lesson:core-micro/basic/game/unit-01;games/example;games/example"
        }
        self.assertEqual(demand(row), 3 + 1)

    def test_lesson_references_are_checked(self) -> None:
        self.website_fixture()
        for changes, message in [
            ({"link_from": "lesson:core-micro"}, "invalid lesson reference"),
            ({"link_from": "lesson:core-micro/basic/game/unit-09"}, "missing lesson"),
            (
                {"status": "covered", "triage_notes": "Found", "covered_by": "lesson:core-micro/basic/game/unit-01"},
                "only allowed in link_from",
            ),
        ]:
            with self.subTest(changes=changes):
                self.write(self.row | changes)
                with self.assertRaisesRegex(ValueError, message):
                    load_backlog(self.source, self.root)
        good = self.row | {"link_from": "lesson:core-micro/basic/game/unit-01;games/example"}
        self.write(good)
        self.assertEqual(load_backlog(self.source, self.root), [good])

    def test_shortlist_ranks_by_demand_not_by_count(self) -> None:
        self.website_fixture()
        many_others = self.row | {"subject": "Many", "link_from": "games/other;games/example"}
        one_lesson = self.row | {
            "id": "VC-0002",
            "subject": "Lesson",
            "link_from": "lesson:core-micro/basic/game/unit-01",
        }
        self.write(many_others, one_lesson)
        result = subprocess.run(
            [
                sys.executable,
                str(Path(__file__).with_name("check_vault_candidates.py")),
                "--file", str(self.source), "--website", str(self.root), "--limit", "2",
            ],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        ranked = [line.split()[0] for line in result.stdout.splitlines() if line.startswith("VC-")]
        self.assertEqual(ranked, ["VC-0002", "VC-0001"])

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
