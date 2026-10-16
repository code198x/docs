"""Check delivered listings and experiment inputs; this is not a runtime emulator."""
from __future__ import annotations

import argparse
import hashlib
import json
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


def separated(rows: list[tuple[int, int]]) -> None:
    assert rows and all(shown != drawn for shown, drawn in rows), 'Display and drawing must differ'


def verify(website: Path, samples: Path) -> dict[str, object]:
    root = Path(__file__).parent
    identities = json.loads((root / 'source.json').read_text())
    for kind, checkout in [('website', website), ('code-samples', samples)]:
        for name, digest in identities[kind]['files'].items():
            assert hashlib.sha256((checkout / name).read_bytes()).hexdigest() == digest, name
    sample = samples / 'commodore-amiga/blitz/meet-blitz/unit-05/many.bb2'
    code = sample.read_text()
    driver = json.loads((sample.parent / 'capture/many.script.json').read_text())
    assert [s['text'] for s in driver if s.get('action') == 'type_string'] == [code]
    statements = [s.strip() for s in code.splitlines() if s.strip() and not s.lstrip().startswith(';')]
    assert statements[:2] == ['VWait 100', 'BLITZ']
    assert statements.index('Show db') < statements.index('db = 1-db') < statements.index('Use BitMap db') < statements.index('Cls 0')
    fixture = lambda name: (root / 'runtime' / f'{name}.ab3').read_text().split('; /XTRA\n', 1)[1]
    assert fixture('many') == code
    plain = code.replace('Circle x, y, 7, 2+i/20', 'Circle x, y, 7, 2')
    assert fixture('plain') == plain
    assert fixture('crowd') == plain.replace('To 79', 'To 199')
    assert fixture('frozen') == code.replace('t = t + 0.04', 't = t + 0')
    assert fixture('slow') == code.replace('t = t + 0.04', 't = t + 0.01')
    for name in ['old', 'many', 'plain', 'crowd', 'frozen', 'slow']:
        log = (root / 'runtime' / f'{name}-compile.txt').read_text()
        expected = 20 if name == 'old' else 21
        assert f'{expected} line(s) compiled, 0 errors.' in log, name
        assert '=== Compiling finished.' in log, name
    amos = (samples / 'commodore-amiga/amos/meet-amos/unit-05/loop.amos').read_text()
    asc = lambda name: (root / 'runtime' / f'{name}.asc').read_text()
    assert asc('p') == amos
    assert asc('bug') == amos.replace('To 5', 'To 10')
    assert asc('ten') == asc('bug').replace('Locate 10,12', 'Locate 10,16')
    assert asc('down') == amos.replace('For N=1 To 5', 'For N=5 To 1 Step -1')
    assert asc('rows') == asc('down').replace('Locate 10,4+N', 'Locate 10,10-N')
    # A reasoning check, independently of the native picture observations.
    forward = {4+n: n for n in range(1, 6)}
    reverse = {4+n: n for n in range(5, 0, -1)}
    assert forward == reverse
    assert [n for row, n in sorted((10-n, n) for n in range(5, 0, -1))] == [5, 4, 3, 2, 1]
    shown_drawn = [(0, 1), (1, 0), (0, 1)]
    separated(shown_drawn)
    try:
        separated([(0, 0), (0, 0)])
    except AssertionError:
        pass
    else:
        raise AssertionError('Missing-toggle control was accepted')
    routes = []
    for track, module in [('amos', 'meet-amos'), ('blitz', 'meet-blitz')]:
        route = f'/systems/commodore-amiga/{track}/{module}/unit-05/'
        html = (website / 'dist' / route.lstrip('/') / 'index.html').read_text()
        page = Page(html)
        delivered = ''.join(page.text)
        assert html.count('data-question') == 3, route
        assert delivered.count('Show the explanation') == 3
        for href in page.links:
            path = urlsplit(href).path
            if path.startswith('/systems/commodore-amiga/'):
                target = website / 'dist' / path.lstrip('/')
                assert target.is_file() or (target / 'index.html').is_file(), href
        # The complete maintained listing must reach the built page in order.
        listing = amos if track == 'amos' else code
        cursor = 0
        for line in listing.splitlines():
            if line.strip():
                cursor = delivered.index(line.strip(), cursor) + len(line.strip())
        if track == 'amos':
            assert 'Done!number 8' in delivered and 'Locate 10,10-N' in delivered
        else:
            assert 'right-Amiga+#' in delivered and 'To 199' in delivered
            assert 'Left-click' in delivered
        routes.append(route)
    return {'sourceHashes': 'pass', 'capturePayload': 'pass', 'experimentInputs': 'pass',
            'builtListingsAndLinks': 'pass', 'questionsPerLesson': 3,
            'bufferReasoningControl': 'rejected', 'routes': routes}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--website', type=Path, required=True)
    parser.add_argument('--samples', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.website, args.samples), indent=2))
