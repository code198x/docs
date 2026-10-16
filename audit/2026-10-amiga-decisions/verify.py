"""Verify source delivery and retained native parity output, not learner outcomes."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


class Page(HTMLParser):
    def __init__(self, source: str) -> None:
        super().__init__()
        self.text: list[str] = []
        self.links: list[str] = []
        self.feed(source)

    def handle_data(self, data: str) -> None:
        self.text.append(data)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        href = dict(attrs).get('href')
        if href:
            self.links.append(href)


def verify_wait(source: str) -> None:
    statements = [s.strip() for s in source.splitlines() if s.strip() and not s.lstrip().startswith(';')]
    assert statements[:2] == ['VWait 100', 'BLITZ'], 'Wait must precede BLITZ'


def verify(website: Path, samples: Path) -> dict[str, object]:
    root = Path(__file__).parent
    source = json.loads((root / 'source.json').read_text())
    for kind, checkout in [('website', website), ('code-samples', samples)]:
        for name, digest in source[kind]['files'].items():
            assert hashlib.sha256((checkout / name).read_bytes()).hexdigest() == digest, name
    sample = samples / 'commodore-amiga/blitz/meet-blitz/unit-04/loop.bb2'
    code = sample.read_text()
    verify_wait(code)
    driver = json.loads((sample.parent / 'capture/loop.script.json').read_text())
    assert [s['text'] for s in driver if s.get('action') == 'type_string'] == [code]
    assert (root / 'runtime/bars.ab3').read_text().split('; /XTRA\n', 1)[1] == code
    assert (root / 'runtime/stripes.ab3').read_text().split('; /XTRA\n', 1)[1] == code.replace('If x = 5 Then c = 5', 'If (x MOD 2) = 0 Then c = 5')
    assert (root / 'runtime/colourbug.ab3').read_text().split('; /XTRA\n', 1)[1] == code.replace('  For x = 0 To 9\n    c = 2', '  c = 2\n  For x = 0 To 9')
    assert (root / 'runtime/branch.amos').read_bytes() == (samples / 'commodore-amiga/amos/meet-amos/unit-04/branch.amos').read_bytes()
    try:
        verify_wait(code.replace('VWait 100\nBLITZ', 'BLITZ\nVWait 100'))
    except AssertionError:
        pass
    else:
        raise AssertionError('Broken wait-order control was accepted')
    output = (root / 'runtime/parity.txt').read_text().splitlines()
    assert output[0] == 'DECISIONS-PARITY-20261016'
    rows = [tuple(map(int, re.fullmatch(r'(\d+) old=(-?\d+) remainder=(\d+)', line).groups())) for line in output[1:]]
    assert [r[0] for r in rows] == list(range(10))
    assert all(old == -1 and remainder == x % 2 for x, old, remainder in rows)
    assert sum(remainder == 0 for _, _, remainder in rows) == 5
    routes = []
    for track, module, count in [('amos', 'meet-amos', 2), ('blitz', 'meet-blitz', 3)]:
        route = f'/systems/commodore-amiga/{track}/{module}/unit-04/'
        html = (website / 'dist' / route.lstrip('/') / 'index.html').read_text()
        page = Page(html)
        text = ''.join(page.text)
        assert html.count('data-question') == count, route
        assert text.count('Show the explanation') == count
        for href in page.links:
            path = urlsplit(href).path
            if path.startswith('/systems/commodore-amiga/'):
                target = website / 'dist' / path.lstrip('/')
                assert target.is_file() or (target / 'index.html').is_file(), href
        if track == 'blitz':
            assert '(x MOD 2) = 0' in text and 'right-Amiga+#' in text
            assert text.index('VWait 100') < text.index('BLITZ')
        else:
            assert 'LIVES=-1' in text and 'Restore' in text
        routes.append({'route': route, 'questions': count, 'amigaLinks': 'pass'})
    return {'sourceHashes': 'pass', 'capturePayload': 'pass', 'runtimeFixtures': 'pass',
            'wrongWaitControl': 'rejected', 'nativeParityRows': len(rows),
            'oldExpressionTrueCount': 10, 'remainderZeroCount': 5, 'routes': routes}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--website', type=Path, required=True)
    parser.add_argument('--samples', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.website, args.samples), indent=2))
