"""Guard how a Vault batch is chosen: the lanes' share, demand order and named lists."""

import unittest

from check_vault_candidates import FIELDS
from next_vault_batch import choose, named


def row(number: int, scope: str, refs: int = 0, status: str = "needs-triage") -> dict[str, str]:
    return dict.fromkeys(FIELDS, "") | {
        "id": f"VC-{number:04d}",
        "subject": f"Subject {number}",
        "category": "games",
        "scope": scope,
        "status": status,
        "why": "A reason.",
        "link_from": ";".join(f"games/ref-{number}-{n}" for n in range(refs)) or "games/example",
    }


class ChooseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rows = [
            row(1, "region:uk;period:1980s", refs=9),
            row(2, "region:us;period:1980s", refs=8),
            row(3, "region:us;period:1990s", refs=7),
            row(4, "region:japan;period:1980s", refs=3),
            row(5, "region:japan;period:1990s", refs=2),
            row(6, "region:ussr;period:1980s", refs=1),
            row(7, "region:us;period:1960s", refs=1),
            row(8, "region:uk;period:1980s", refs=20, status="published"),
            row(9, "region:uk;period:1980s", refs=19, status="in-progress"),
            row(10, "region:us;period:1980s", refs=6, status="ready"),
        ]

    def ids(self, size: int) -> list[tuple[str, str]]:
        return [(r["id"], why) for r, why in choose(self.rows, size)]

    def test_a_third_comes_from_the_lanes_taken_in_turn(self) -> None:
        # Six rounds up to two lane picks: world first, then early; four by demand.
        self.assertEqual(
            self.ids(6),
            [
                ("VC-0004", "world"),
                ("VC-0007", "early"),
                ("VC-0001", "demand"),
                ("VC-0002", "demand"),
                ("VC-0003", "demand"),
                ("VC-0010", "demand"),
            ],
        )

    def test_the_world_lane_rotates_regions(self) -> None:
        # Japan ranks higher, but the USSR gets the second world place.
        self.rows = [r for r in self.rows if r["id"] != "VC-0007"]
        self.assertEqual(self.ids(9)[:3], [("VC-0004", "world"), ("VC-0006", "world"), ("VC-0005", "world")])

    def test_only_waiting_work_is_chosen(self) -> None:
        chosen = {i for i, _ in self.ids(20)}
        self.assertNotIn("VC-0008", chosen)
        self.assertNotIn("VC-0009", chosen)
        self.assertIn("VC-0010", chosen)
        self.assertEqual(len(chosen), 8)

    def test_empty_lanes_leave_the_whole_batch_to_demand(self) -> None:
        self.rows = [r for r in self.rows if r["id"] in {"VC-0001", "VC-0002", "VC-0003"}]
        self.assertEqual([why for _, why in self.ids(3)], ["demand"] * 3)

    def test_a_named_list_keeps_its_order_and_rejects_unavailable_work(self) -> None:
        self.assertEqual([r["id"] for r, _ in named(self.rows, ["VC-0006", "VC-0001"])], ["VC-0006", "VC-0001"])
        for ids, message in [
            (["VC-0099"], "unknown candidate"),
            (["VC-0008"], "published, not waiting"),
            (["VC-0009"], "in-progress, not waiting"),
            (["VC-0001", "VC-0001"], "appears twice"),
        ]:
            with self.subTest(ids=ids), self.assertRaisesRegex(ValueError, message):
                named(self.rows, ids)


if __name__ == "__main__":
    unittest.main()
