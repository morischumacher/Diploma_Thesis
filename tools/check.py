#!/usr/bin/env python3
"""Repo-wide consistency checks for the thesis. See ANWEISUNGEN.md.

Usage:  python3 tools/check.py [--chapter chapters/design.tex]
Exit code 1 if any BLOCKING check fails (dangling refs, duplicate labels,
unknown cite keys, unbalanced braces); style findings are reported but do
not fail the run.
"""
import re, sys, glob, os, collections, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

TEX = ['main.tex'] + sorted(glob.glob('chapters/*.tex')) + \
      sorted(glob.glob('appendix/*.tex')) + sorted(glob.glob('formalities/*.tex'))

def read(f): return open(f, encoding='utf-8').read()

def strip_comments(t):
    return re.sub(r'(?<!\\)%.*', '', t)

def caption_bodies(t):
    for m in re.finditer(r'\\caption\{', t):
        i, d, j = m.end(), 1, m.end()
        while d and j < len(t):
            d += (t[j] == '{') - (t[j] == '}')
            j += 1
        yield t[i:j-1]

def plain(s):
    s = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?', '', s)
    return s.replace('{', '').replace('}', '').strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--chapter', help='restrict style checks to one file')
    args = ap.parse_args()

    texts = {f: read(f) for f in TEX}
    bodies = {f: strip_comments(t) for f, t in texts.items()}
    fail = False
    def bad(msg):
        nonlocal fail; fail = True; print('FAIL ', msg)
    def warn(msg): print('warn ', msg)

    # --- structural: labels and references -------------------------------
    labels = collections.Counter()
    for t in bodies.values():
        labels.update(re.findall(r'\\label\{([^}]*)\}', t))
    refs = collections.defaultdict(list)
    for f, t in bodies.items():
        for r in re.findall(r'\\(?:ref|autoref|nameref|cref)\{([^}]*)\}', t):
            refs[r].append(f)
    for r, fs in sorted(refs.items()):
        if r not in labels:
            bad(f'dangling \\ref{{{r}}} in {sorted(set(fs))}')
    for l, n in labels.items():
        if n > 1:
            bad(f'duplicate \\label{{{l}}} ({n}x)')
    for l in sorted(labels):
        if (l.startswith('fig:') or l.startswith('tab:')) and l not in refs:
            warn(f'float label never referenced: {l}')

    # --- structural: citations -------------------------------------------
    cites = collections.Counter()
    for t in bodies.values():
        for m in re.finditer(r'\\cite[a-zA-Z]*(?:\[[^\]]*\])*\{([^}]*)\}', t):
            cites.update(k.strip() for k in m.group(1).split(','))
    bib = read('bibliography.bib')
    bibkeys = set(re.findall(r'@\w+\{([^,]+),', bib))
    for k in sorted(cites):
        if k not in bibkeys:
            bad(f'cite key not in bibliography.bib: {k}')
    uncited = sorted(k for k in bibkeys if k not in cites)
    if uncited:
        warn(f'{len(uncited)} bib entries never cited: {", ".join(uncited[:6])}...')

    # --- structural: brace balance ---------------------------------------
    for f, t in texts.items():
        if t.count('{') != t.count('}'):
            bad(f'brace imbalance in {f}: {t.count("{")} open, {t.count("}")} close')

    # --- style ------------------------------------------------------------
    targets = [args.chapter] if args.chapter else \
              [f for f in TEX if f.startswith(('chapters/', 'appendix/'))]
    AMERICAN = r'\b(color|colors|behavior|behaviour?s|catalog|catalogs|judgment|favor|labeled|modeling|analyze|analyzed|fulfillment|program|programs|visualization|personalization|prioritization|organized|recognized|minimize|utilize|emphasize|individualized)\b'
    SLANG = r'\b(figure out|kind of|a lot of|pretty much|basically|end up|deal with|come up with|turn out|get around)\b'
    for f in targets:
        t = bodies[f]
        for pat, msg in [(AMERICAN, 'American spelling'), ('—', 'em dash in prose'),
                         (r'``', 'TeX quotes -- house form is \\enquote{}'),
                         (SLANG, 'colloquialism'),
                         (r'\bwill\b', 'future tense "will"'),
                         (r'\d+ ECTS', 'ECTS without ~'),
                         (r'%%\s*(AI)?REV', 'unresolved source comment'),
                         (r'\\todo\{', 'raw \\todo -- use \\TDblock/\\TDmajor/\\TDminor/\\TDrev')]:
            hits = re.findall(pat, t)
            if hits:
                c = collections.Counter(h if isinstance(h, str) else h[0] for h in hits)
                warn(f'{f}: {msg} x{len(hits)} {dict(c.most_common(5))}')
        for cap in caption_bodies(t):
            p = plain(cap)
            lim = 350 if '\\begin{table' in t[:t.find(cap)][-4000:] else 200
            if not (100 <= len(p) <= lim):
                warn(f'{f}: caption {len(p)} chars (limit 100-{lim}): {p[:60]}')

    print('\nBLOCKING CHECKS FAILED' if fail else '\nall blocking checks passed')
    return 1 if fail else 0

if __name__ == '__main__':
    sys.exit(main())
