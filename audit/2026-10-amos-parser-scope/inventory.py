"""Inventory tracked text samples. This is not an AMOS lexer or parser."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = "commodore-amiga/amos/"
PHRASES = sorted(
    [
        "Screen Open",
        "Screen Copy",
        "Screen Swap",
        "Double Buffer",
        "Bob Update Off",
        "Get Rom Fonts",
        "Set Font",
        "Text Base",
        "Curs Off",
        "Flash Off",
        "Play Off",
        "Play",
        "Wait",
        "Set Envel",
        "Wait Key",
        "Wait Vbl",
        "Clear Key",
        "Key State",
        "End If",
        "End Proc",
        "Get Bob",
        "Amal On",
        "Channel",
        "Hide",
        "Show",
        "Autoback",
        "Dim",
        "Palette",
        "Paper",
        "Pen",
        "Wave",
        "Volume",
        "Cls",
        "Ink",
        "Bar",
        "Box",
        "Gosub",
        "Repeat",
        "Until",
        "If",
        "Else",
        "Randomize",
        "For",
        "Next",
        "Return",
        "End",
        "Print",
        "Locate",
        "Colour",
        "Bob",
        "Amal",
        "Do",
        "Loop",
        "While",
        "Wend",
        "Exit",
        "Procedure",
        "Circle",
        "Draw",
        "Add",
        "Inc",
        "Plot",
        "Text",
        "Boom",
        "Shoot",
        "Bell",
    ],
    key=lambda p: (-len(p), p),
)
FUNCTIONS = [
    "Rnd",
    "Timer",
    "Upper$",
    "Inkey$",
    "Scancode",
    "Str$",
    "Len",
    "Instr",
    "Mid$",
    "Text Base",
    "Physic",
    "Logic",
    "Lowres",
]


def masked(line: str) -> str:
    """Hide quoted text before measuring source words and colon separators."""
    return re.sub(r'"[^"\n]*"', lambda m: " " * len(m[0]), line)


def inventory(repo: Path) -> dict:
    revision = subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()
    subprocess.run(
        ["git", "-C", str(repo), "diff", "--quiet", "HEAD", "--", ROOT],
        check=True,
    )
    paths = subprocess.check_output(
        ["git", "-C", str(repo), "ls-files", "-z", ROOT], text=True
    ).split("\0")
    paths = sorted(p for p in paths if p.endswith(".amos"))
    if not paths:
        raise ValueError("No tracked AMOS samples: refusing an empty inventory")
    files = []
    groups: Counter[str] = Counter()
    all_heads: Counter[str] = Counter()
    for name in paths:
        raw = (repo / name).read_bytes()
        text = raw.decode("utf-8")
        group = (
            "bank-or-risk"
            if "/bank-or-risk/" in name
            else "meet-amos"
            if "/meet-amos/" in name
            else "other"
        )
        groups[group] += 1
        heads: Counter[str] = Counter()
        refs: Counter[str] = Counter()
        unclassified = []
        features: Counter[str] = Counter()
        for number, line in enumerate(text.splitlines(), 1):
            clean = masked(line).strip()
            if not clean or clean.lower().startswith("rem ") or clean.startswith("'"):
                continue
            if re.fullmatch(r"[A-Za-z_][A-Za-z_0-9]*:", clean):
                features["label_lines"] += 1
                continue
            if ":" in clean:
                features["lines_with_statement_separator"] += 1
            if re.search(r"\$[0-9A-Fa-f]+", clean):
                features["lines_with_hex_literals"] += 1
            if re.search(r"\b[A-Za-z_][\w]*[$#]", clean):
                features["lines_with_type_suffixes"] += 1
            if re.search(r"\([^)]*\)", clean):
                features["lines_with_parentheses"] += 1
            for symbol in FUNCTIONS:
                refs[symbol] += len(
                    re.findall(
                        r"(?<![\w$#])" + re.escape(symbol) + r"(?![\w$#])",
                        clean,
                        re.IGNORECASE,
                    )
                )
            for statement in clean.split(":"):
                statement = statement.strip()
                if not statement:
                    continue
                found = next(
                    (
                        p
                        for p in PHRASES
                        if re.match(
                            re.escape(p) + r"(?![\w$#])", statement, re.IGNORECASE
                        )
                    ),
                    None,
                )
                if found:
                    heads[found] += 1
                elif re.match(r"[A-Za-z_][\w]*[$#]?(?:\([^)]*\))?\s*=", statement):
                    features["assignment_candidates"] += 1
                elif re.fullmatch(r"[A-Za-z_][\w]*", statement):
                    features["bare_name_candidates"] += 1
                else:
                    unclassified.append({"line": number, "text": line.strip()})
        all_heads.update(heads)
        files.append(
            {
                "path": name,
                "group": group,
                "sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
                "lines": len(text.splitlines()),
                "statement_head_candidates": dict(sorted(heads.items())),
                "symbol_references_outside_strings": {
                    k: v for k, v in sorted(refs.items()) if v
                },
                "features": dict(sorted(features.items())),
                "unclassified": unclassified,
            }
        )
    return {
        "method": "textual_inventory_not_syntax_validation",
        "source_repository": "https://github.com/code198x/code-samples",
        "source_revision": revision,
        "tracked_amos_files": len(files),
        "groups": dict(sorted(groups.items())),
        "statement_head_candidates": dict(sorted(all_heads.items())),
        "files": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("samples", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = inventory(args.samples)
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    target = Path(__file__).with_name("inventory.json")
    if args.check:
        if not target.exists() or target.read_text() != rendered:
            raise SystemExit(
                "FAIL: recorded inventory differs from the tracked samples"
            )
        print(f"PASS: {result['tracked_amos_files']} tracked samples and hashes agree")
    else:
        target.write_text(rendered)
        print(f"Recorded {result['tracked_amos_files']} tracked text samples")


if __name__ == "__main__":
    main()
