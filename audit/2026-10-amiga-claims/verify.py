"""Check retained source identities, sample ordering and built lesson delivery."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, html: str) -> None:
        super().__init__()
        self.words: list[str] = []
        self.links: list[str] = []
        self.styles: list[str] = []
        self.feed(html)

    def handle_data(self, data: str) -> None:
        self.words.append(data)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        href = values.get('href')
        if href:
            self.links.append(href)
            if tag == 'link' and values.get('rel') == 'stylesheet':
                self.styles.append(href)


def require_wait(source: str) -> None:
    statements = [line.strip() for line in source.splitlines()
                  if line.strip() and not line.lstrip().startswith(';')]
    assert statements[:2] == ['VWait 100', 'BLITZ'], 'Disk-settling wait must precede BLITZ'
    assert statements.count('VWait 100') == 1


def verify(website: Path, samples: Path) -> dict[str, object]:
    evidence = Path(__file__).parent
    identities = json.loads((evidence / 'source.json').read_text())
    for kind, root in [('website', website), ('samples', samples)]:
        for name, digest in identities[kind]['changedFiles'].items():
            assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
    source_path = 'commodore-amiga/blitz/meet-blitz/unit-02/blitzmode.bb2'
    source = (samples / source_path).read_text()
    require_wait(source)
    for probe, sample in [('blitzmode.ab3', source_path),
                          ('types.ab3', 'commodore-amiga/blitz/meet-blitz/unit-03/types.bb2')]:
        fixture = (evidence / 'probes' / probe).read_text().split('; /XTRA\n', 1)[1]
        assert fixture == (samples / sample).read_text(), f'Probe differs from maintained source: {probe}'
    driver = json.loads((samples / Path(source_path).parent / 'capture/blitzmode.script.json').read_text())
    payload = [item['text'] for item in driver if item.get('action') == 'type_string']
    assert payload == [source], 'Capture payload differs from maintained sample'
    try:
        require_wait(source.replace('VWait 100\nBLITZ', 'BLITZ\nVWait 100'))
    except AssertionError:
        pass
    else:
        raise AssertionError('Wrong-order negative control passed')
    routes = []
    for track, module in [('amos', 'meet-amos'), ('blitz', 'meet-blitz')]:
        for suffix in ['', '/unit-01', '/unit-02', '/unit-03']:
            routes.append(f'/systems/commodore-amiga/{track}/{module}{suffix}')
        routes.append(f'/systems/commodore-amiga/{track}/getting-started')
    results = []
    for route in routes:
        path = website / 'dist' / route.lstrip('/') / 'index.html'
        html = path.read_text()
        page = Page(html)
        text = ''.join(page.words)
        assert text.strip(), route
        scope = re.search(r'<header\b[^>]*\b(data-astro-cid-[\w]+)', html)
        assert scope, f'Header scope missing: {route}'
        css = '\n'.join((website / 'dist' / href.lstrip('/')).read_text() for href in page.styles if href.startswith('/'))
        assert f'.site-header[{scope[1]}]' in css, f'Linked header CSS missing: {route}'
        assert '.site-header[data-astro-cid-negativecontrol]' not in css
        for href in page.links:
            url = urlsplit(href)
            if url.path.startswith('/systems/commodore-amiga/'):
                target = website / 'dist' / unquote(url.path).lstrip('/')
                assert target.is_file() or (target / 'index.html').is_file(), (route, href)
        if route.endswith('blitz/meet-blitz/unit-02'):
            assert text.index('VWait 100') < text.index('BLITZ')
            assert 'right-Amiga+#' in text and 'QAmiga' in text
        if route.endswith('blitz/meet-blitz/unit-03'):
            assert 'OverflowCheck = 0' in text and '−2,147,483,648' in text
        if route.endswith('amos/meet-amos/unit-03'):
            assert 'DISTANCE#' in text and 'real-number variables' in text
        results.append({'route': route, 'content': 'pass', 'linkedHeaderCSS': 'pass', 'amigaLinks': 'pass'})
    return {'routes': results, 'sourceIdentities': 'pass', 'capturePayload': 'pass',
            'waitOrder': 'pass', 'wrongOrderNegativeControl': 'rejected',
            'browserVisual': 'not performed', 'runtime': 'not performed'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--website', type=Path, required=True)
    parser.add_argument('--samples', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.website, args.samples), indent=2))
