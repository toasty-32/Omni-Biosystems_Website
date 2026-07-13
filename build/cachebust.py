#!/usr/bin/env python3
"""Stamp every /assets/ URL in the built HTML with a short content hash (?v=...).

Idempotent: existing ?v=... stamps are stripped first, then recomputed. Run this
as the LAST step of every build -- if a CSS/JS/media file changes afterwards, the
HTML points at a stale hash and browsers serve cached, wrong assets.
"""
import hashlib, pathlib, re, sys

PUB = pathlib.Path(__file__).resolve().parent.parent / 'public'

ASSET_RE = re.compile(
    r'(src|href)="(/(?:assets|favicon|apple-touch-icon|icon-)[^"?#]*)(?:\?v=[a-f0-9]+)?"'
)

cache = {}
def short_hash(rel):
    if rel not in cache:
        f = PUB / rel.lstrip('/')
        cache[rel] = hashlib.md5(f.read_bytes()).hexdigest()[:8] if f.exists() else None
    return cache[rel]

stamped = 0
missing = set()
for page in sorted(PUB.rglob('*.html')):
    s = page.read_text(encoding='utf-8')
    def repl(m):
        global stamped
        attr, url = m.group(1), m.group(2)
        h = short_hash(url)
        if h is None:
            missing.add(url); return f'{attr}="{url}"'
        stamped += 1
        return f'{attr}="{url}?v={h}"'
    page.write_text(ASSET_RE.sub(repl, s), encoding='utf-8')

print(f'stamped {stamped} asset URLs')
for m in sorted(missing):
    print('  MISSING:', m)

bad = 0
for page in sorted(PUB.rglob('*.html')):
    s = page.read_text(encoding='utf-8')
    for url, h in re.findall(r'(?:src|href)="(/[^"?]+)\?v=([a-f0-9]{8})"', s):
        f = PUB / url.lstrip('/')
        if not f.exists() or hashlib.md5(f.read_bytes()).hexdigest()[:8] != h:
            print(f'  MISMATCH {page.name} {url}'); bad += 1
print('verification:', 'all hashes match' if bad == 0 else f'{bad} MISMATCHES')
sys.exit(1 if bad else 0)
