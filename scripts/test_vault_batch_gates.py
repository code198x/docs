"""Plant each fault a Vault batch can carry and check its gate fails."""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import vault_batch_gates as gates

ENTRY = """---
ai_generated: true
reviewed: false
title: "Spacewar!"
---
Spacewar! ran on the [PDP-1](/vault/systems/pdp-1).
"""
EXISTING = """---
ai_generated: true
reviewed: true
title: "PDP-1"
---
The PDP-1 ran Spacewar! at MIT.
"""


class GateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.site = Path(self.temp.name)
        self.git("init", "-q", "-b", "main")
        self.write("src/content/vault/systems/pdp-1.mdx", EXISTING)
        self.git("add", ".")
        self.git("-c", "user.name=t", "-c", "user.email=t@example.com", "commit", "-q", "-m", "base")
        self.base = self.git("rev-parse", "HEAD").strip()
        self.write("src/content/vault/games/spacewar.mdx", ENTRY)
        self.write(
            "src/content/vault/systems/pdp-1.mdx",
            EXISTING.replace("ran Spacewar!", "ran [Spacewar!](/vault/games/spacewar)"),
        )
        self.triage = [{"id": "VC-2076", "decision": "write", "path": "games/spacewar", "notes": "Scoped."}]
        self.claims = [{"entry": "games/spacewar", "claim": "Ran on the PDP-1.", "evidence": ["DEC manual", "Graetz 1981"]}]

    def git(self, *args: str) -> str:
        return subprocess.run(["git", *args], cwd=self.site, capture_output=True, text=True, check=True).stdout

    def write(self, relative: str, text: str) -> None:
        path = self.site / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def scope(self) -> list[str]:
        return gates.check_scope_and_preservation(self.site, self.base, "docs/reviews/batch", ["games/spacewar"])

    def test_a_clean_batch_passes_the_local_gates(self) -> None:
        self.write("docs/reviews/batch/triage.json", json.dumps(self.triage))
        self.assertEqual(gates.check_triage(self.triage, ["VC-2076"]), [])
        self.assertEqual(gates.check_entries(self.site, self.base, ["games/spacewar"]), [])
        self.assertEqual(gates.check_claims(self.claims, ["games/spacewar"]), [])
        self.assertEqual(gates.check_incoming(self.site, ["games/spacewar"]), [])
        self.assertEqual(self.scope(), [])

    def test_triage_must_cover_exactly_the_batch(self) -> None:
        self.assertRegex(gates.check_triage(self.triage, ["VC-2076", "VC-0142"])[0], "VC-0142: needs exactly one")
        self.assertRegex(gates.check_triage(self.triage * 2, ["VC-2076"])[0], "found 2")
        bad = [{"id": "VC-2076", "decision": "maybe", "notes": "?"}]
        self.assertRegex(" ".join(gates.check_triage(bad, ["VC-2076"])), "unknown decision")

    def test_a_draft_must_be_new_marked_and_unreviewed(self) -> None:
        self.write("src/content/vault/games/spacewar.mdx", ENTRY.replace("reviewed: false", "reviewed: true"))
        self.assertRegex(gates.check_entries(self.site, self.base, ["games/spacewar"])[0], "reviewed: false")
        self.write("src/content/vault/games/spacewar.mdx", ENTRY.replace("ai_generated: true\n", ""))
        self.assertRegex(gates.check_entries(self.site, self.base, ["games/spacewar"])[0], "ai_generated")
        self.assertRegex(gates.check_entries(self.site, self.base, ["systems/pdp-1"])[-1], "already exists")

    def test_every_claim_has_sources_and_one_source_is_declared(self) -> None:
        one = [{**self.claims[0], "evidence": ["DEC manual"]}]
        self.assertRegex(gates.check_claims(one, ["games/spacewar"])[0], "mark it single_source")
        self.assertEqual(gates.check_claims([{**one[0], "single_source": True}], ["games/spacewar"]), [])
        self.assertRegex(gates.check_claims([], ["games/spacewar"])[0], "no claims")
        self.assertRegex(gates.check_claims([{**self.claims[0], "evidence": []}], ["games/spacewar"])[0], "at least one source")

    def test_a_draft_needs_an_incoming_link(self) -> None:
        self.write("src/content/vault/systems/pdp-1.mdx", EXISTING)
        self.assertRegex(gates.check_incoming(self.site, ["games/spacewar"])[0], "no incoming link")

    def test_existing_entries_may_only_gain_links(self) -> None:
        self.write(
            "src/content/vault/systems/pdp-1.mdx",
            EXISTING.replace("ran Spacewar! at MIT", "ran [Spacewar!](/vault/games/spacewar) at Harvard"),
        )
        self.assertRegex(self.scope()[0], "changed beyond adding Vault links")
        self.write("src/content/vault/systems/pdp-1.mdx", EXISTING.replace("reviewed: true", "reviewed: false"))
        self.assertRegex(self.scope()[0], "changed beyond")

    def test_a_batch_stays_inside_the_vault(self) -> None:
        self.write("src/pages/index.astro", "changed")
        self.assertRegex(self.scope()[0], "outside what a Vault batch may change")
        self.write("src/content/vault/games/extra.mdx", ENTRY)
        self.assertIn("src/content/vault/games/extra.mdx: a new entry with no triage record", self.scope())

    def test_the_link_control_must_fail_then_recover(self) -> None:
        entry = self.site / "src/content/vault/games/spacewar.mdx"
        before = entry.read_bytes()

        def honest(command: list[str], cwd: Path) -> subprocess.CompletedProcess:
            broken = gates.CONTROL in entry.read_text(encoding="utf-8")
            return subprocess.CompletedProcess(command, int(broken), "", "")

        self.assertEqual(gates.link_control(self.site, "games/spacewar", honest), [])
        self.assertEqual(entry.read_bytes(), before)
        always_green = lambda command, cwd: subprocess.CompletedProcess(command, 0, "", "")
        self.assertRegex(gates.link_control(self.site, "games/spacewar", always_green)[0], "passed with a planted")
        self.assertEqual(entry.read_bytes(), before)

    def test_built_drafts_are_noindex_and_out_of_the_sitemap(self) -> None:
        self.write("dist/vault/games/spacewar/index.html", '<meta name="robots" content="noindex">')
        self.write("dist/sitemap-0.xml", "<loc>https://code198x.org/vault/systems/pdp-1/</loc>")
        self.assertEqual(gates.check_built(self.site, ["games/spacewar"]), [])
        self.write("dist/sitemap-0.xml", "<loc>https://code198x.org/vault/games/spacewar/</loc>")
        self.assertRegex(gates.check_built(self.site, ["games/spacewar"])[0], "in the sitemap")
        self.write("dist/vault/games/spacewar/index.html", "<meta>")
        self.assertRegex(gates.check_built(self.site, ["games/spacewar"])[0], "lacks noindex")


    def test_a_skipped_release_check_is_never_mistaken_for_a_pass_or_a_usage_error(self) -> None:
        self.assertNotIn(gates.INCOMPLETE, {0, 1, 2})

    def docs_repo(self) -> tuple[Path, str]:
        docs = Path(self.temp.name) / "docs-repo"
        docs.mkdir()
        run = lambda *a: subprocess.run(["git", *a], cwd=docs, capture_output=True, text=True, check=True).stdout
        run("init", "-q", "-b", "main")
        (docs / "vault-candidates.csv").write_text("id,subject\nVC-0001,PDP-1\n", encoding="utf-8")
        run("add", ".")
        run("-c", "user.name=t", "-c", "user.email=t@example.com", "commit", "-q", "-m", "base")
        return docs, run("rev-parse", "HEAD").strip()

    def test_nothing_the_batch_adds_may_name_a_private_path(self) -> None:
        docs, docs_base = self.docs_repo()
        self.assertEqual(gates.check_private(self.site, self.base, docs, docs_base), [])
        # Triage notes in the queue are checked too, in the docs repository.
        with (docs / "vault-candidates.csv").open("a", encoding="utf-8") as queue:
            queue.write("VC-0002,Read in reference/by-system/dec\n")
        self.assertRegex(gates.check_private(self.site, self.base, docs, docs_base)[0], "^docs vault-candidates.csv:3")
        (docs / "vault-candidates.csv").write_text("id,subject\nVC-0001,PDP-1\n", encoding="utf-8")
        for text in (
            "Read /Users/someone/Projects/198x/reference/by-system/pdp-1/manual.pdf",
            "Source: reference/_raw-extracts/dec/pdp-1.txt",
            "Checked with knowledge.py and facts.sqlite",
            "Copied from /Volumes/Data/Library",
            "See reference/known-unknowns.md",
        ):
            with self.subTest(text=text):
                self.write("docs/reviews/batch/REPORT.md", text + "\n")
                hits = gates.check_private(self.site, self.base, docs, docs_base)
                self.assertTrue(hits)
                self.assertTrue(all(h.startswith("website docs/reviews/batch/REPORT.md:1:") for h in hits), hits)

    def test_a_changed_file_is_read_whatever_the_diff_prefixes(self) -> None:
        # diff.mnemonicPrefix writes "+++ w/file"; the gate must still see the file.
        for setting in ("false", "true"):
            with self.subTest(mnemonicPrefix=setting):
                self.git("config", "diff.mnemonicPrefix", setting)
                self.write("src/content/vault/systems/pdp-1.mdx", EXISTING + "From /Users/x/library\n")
                self.assertEqual(len(gates.check_private(self.site, self.base, self.site, self.base)), 2)

    def test_vault_reference_paths_and_older_text_are_allowed(self) -> None:
        self.write(
            "docs/reviews/batch/REPORT.md",
            "Linked from [ports](/vault/reference/zx-spectrum-hardware-ports) and reference/zx-spectrum-hardware-ports.\n",
        )
        self.assertEqual(gates.check_private(self.site, self.base, self.site, self.base), [])
        # A private path already on the base branch isn't this batch's to answer for.
        self.write("src/content/vault/systems/pdp-1.mdx", EXISTING + "Old note: /Users/x/y\n")
        self.git("add", ".")
        self.git("-c", "user.name=t", "-c", "user.email=t@example.com", "commit", "-q", "-m", "older")
        later = self.git("rev-parse", "HEAD").strip()
        self.write("src/content/vault/systems/pdp-1.mdx", EXISTING + "Old note: /Users/x/y\nNew line.\n")
        self.assertEqual(gates.check_private(self.site, later, self.site, later), [])
        self.write("src/content/vault/systems/pdp-1.mdx", EXISTING + "Old note: /Users/x/y\nNew: /private/tmp/z\n")
        self.write("src/content/vault/systems/pdp-1.mdx", EXISTING + "Old note: /Users/x/y\nOne.\nTwo /private/tmp/z\n")
        self.assertRegex(gates.check_private(self.site, later, self.site, later)[0], r"pdp-1\.mdx:9: ")
        self.write("src/content/vault/systems/pdp-1.mdx", EXISTING + "Old note: /Users/x/y\nNew: /private/tmp/z\n")
        # Reported at the file's own line, not its place among the added lines.
        self.assertRegex(gates.check_private(self.site, later, self.site, later)[0], r"pdp-1\.mdx:8: private path '/private/tmp/'")

    def test_scan_checks_text_that_never_reaches_a_branch(self) -> None:
        body = self.site / "pr-body.md"
        body.write_text("Sources were read in /Users/someone/Projects/198x/reference/by-topic\n", encoding="utf-8")
        script = Path(gates.__file__)
        result = subprocess.run(["python3", str(script), "--scan", str(body)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stdout)
        body.write_text("Sources are cited in each entry.\n", encoding="utf-8")
        result = subprocess.run(["python3", str(script), "--scan", str(body)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_web_addresses_are_not_private_paths(self) -> None:
        lines = gates.numbered("Source: https://www.donhopkins.com/home/catalog/simcity/\nSee example.org/Users/guide and x.net/Volumes/1\n")
        self.assertEqual(gates.private_hits(lines, "f"), [])
        for path in ("/home/steve/notes", "(/Users/x)", "`/Volumes/Data`", "path=/private/tmp/x"):
            with self.subTest(path=path):
                self.assertTrue(gates.private_hits(gates.numbered(path), "f"))

    def test_the_queue_cites_unpublished_drafts_by_candidate_id(self) -> None:
        docs, _ = self.docs_repo()
        triage = [{"id": "VC-2076", "path": "games/spacewar"}]
        (docs / "vault-candidates.csv").write_text(
            "id,link_from,covered_by\nVC-0001,systems/pdp-1;candidate:VC-2076,\n", encoding="utf-8"
        )
        self.assertEqual(gates.check_planned_links(docs, ["games/spacewar"], triage), [])
        (docs / "vault-candidates.csv").write_text(
            "id,link_from,covered_by\nVC-0001,systems/pdp-1;games/spacewar,\n", encoding="utf-8"
        )
        self.assertEqual(
            gates.check_planned_links(docs, ["games/spacewar"], triage),
            ["VC-0001: link_from names unpublished games/spacewar; use candidate:VC-2076"],
        )

if __name__ == "__main__":
    unittest.main()
