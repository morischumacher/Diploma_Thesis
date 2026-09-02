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
    ap.add_argument('--submission', action='store_true',
                    help='check the document is in submission state (see ANWEISUNGEN section 15)')
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
    AMERICAN = r'\b(color|colors|behavior|behaviors|catalog|catalogs|judgment|favor|labeled|modeling|analyze|analyzed|fulfillment|program|programs|visualization|personalization|prioritization|organized|recognized|minimize|utilize|emphasize|individualized)\b'
    SLANG = r'\b(figure out|kind of|a lot of|pretty much|basically|end up|deal with|come up with|turn out|get around)\b'
    LANGUAGE = [
        ('hedge or intensifier', r'\b(actually|really|quite|obviously|simply|truly|indeed|very|extremely|highly)\b'),
        ('vague quantifier (give the number)', r'\b(a number of|numerous|a lot of|a variety of)\b'),
        ('conversational verb', r'\b(figure out|come up with|deal with|end up|turn out|get around|leave it to|bring up)\b'),
        ('overclaiming verb', r'\b(prove[sd]?|demonstrates? that|shows conclusively|confirms that)\b'),
        ('filler hedge', r'(leaves a clear gap|in spirit|a large and varied|it is worth noting|it should be noted|needless to say)'),
        ('anthropomorphism', r'\b(the (?:tool|system|engine|graph|table) (?:wants|knows|thinks|believes|decides|feels))\b'),
        ('stance without argument', r'\b(we (?:believe|feel|think))\b'),
        ('first-person singular', r'(?<![A-Za-z])(I(?![0-9])|my|me)(?![A-Za-z])'),
        ('em dash in prose', r'\u2014'),
        ('study named by ordinal', r'\b[Ss]tudy[~ ]?[12]\b'),
        ('study-name variant', r'\b(needfinding study|summative study|first study|second study|user study)\b'),
    ]
    for f in targets:
        t = bodies[f]
        # the glossary defines the study names, so it may use their variants
        if f.endswith('glossary.tex'):
            t = re.sub(r'\b(needfinding study|summative study)\b', '', t)
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
        # Quotations are reproduced as spoken and are outside the house register,
        # so strip them before the language scan or every "I" a participant said
        # is reported as a defect.
        prose = re.sub(r'\\TD(?:block|major|minor|rev|ok)\{.*', '', t)
        prose = re.sub(r'\\enquote\{[^{}]*\}', ' ', prose)
        prose = re.sub(r'\\begin\{quote\}.*?\\end\{quote\}', ' ', prose, flags=re.S)
        for what, pat in LANGUAGE:
            hits = re.findall(pat, prose)
            if hits:
                c = collections.Counter(h if isinstance(h, str) else h[0] for h in hits)
                warn('%s: %s x%d %s' % (f, what, len(hits), dict(c.most_common(5))))
        # ANWEISUNGEN §3, the "rather than" rule. Whether a single comparison is
        # a real distinction or a strawman is a judgement no regex can make, so
        # only the pile-up is flagged: two or more in one paragraph is a tic
        # even when each one would pass on its own.
        COMPARE = r'\brather than\b|\binstead of\b|\bas opposed to\b|\bnot merely\b|\bnot simply\b'
        # A list item and a table row are each their own unit of prose, so they
        # are split out; otherwise a whole itemize counts as one paragraph.
        units = re.split(r'\n\s*\n|\\item\b|\\\\', prose)
        for para in units:
            n = len(re.findall(COMPARE, para))
            if n >= 2:
                opener = ' '.join(para.split())[:60]
                warn(f'{f}: {n} self-comparisons in one paragraph: {opener}')
        for cap in caption_bodies(t):
            p = plain(cap)
            lim = 350 if '\\begin{table' in t[:t.find(cap)][-4000:] else 200
            if not (100 <= len(p) <= lim):
                warn(f'{f}: caption {len(p)} chars (limit 100-{lim}): {p[:60]}')

    if args.submission:
        print('\n--- submission state ---')
        m = read('main.tex')
        if re.search(r'^\\reviewnotestrue', m, re.M):
            bad('main.tex still has \\reviewnotestrue: notes and the To-Do index will print')
        for pat, what in [(r'Title of the Thesis', 'placeholder thesis title'),
                          (r'Optional Subtitle of the Thesis', 'placeholder subtitle'),
                          (r'\\setdate\{01\}\{01\}\{2001\}', 'placeholder date'),
                          (r'a\\sep list\\sep of\\sep keywords', 'placeholder keywords')]:
            if re.search(pat, m):
                bad('main.tex still carries the %s' % what)
        for f in sorted(glob.glob('formalities/*.tex')):
            body = strip_comments(read(f))
            body = re.sub(r'\\TD(block|major|minor|rev|ok)\{.*', '', body, flags=re.S)
            if not body.strip():
                bad('%s is empty and is \\input by main.tex' % f)
        for f, t2 in bodies.items():
            for pat, what in [(r'\\todo\{', 'a raw \\todo'),
                              (r'\\TD(?:block|major|minor|rev|ok)\{', 'a review note')]:
                n = len(re.findall(pat, t2))
                if n: warn('%s still contains %d x %s (hidden by \\reviewnotesfalse, but delete before archiving)' % (f, n, what))
        for f, t2 in texts.items():
            n = len(re.findall(r'%%\s*(?:AI)?REV', t2))
            if n: bad('%s still has %d unresolved %%%% REV comment(s)' % (f, n))

    # --- abbreviations: introduced at their first use in reading order ------
    ORDER = ['chapters/introduction.tex', 'chapters/methodology.tex',
             'chapters/relatedwork.tex', 'chapters/needfindingwithprototype.tex',
             'chapters/fromthemestorequirements.tex', 'chapters/design.tex',
             'chapters/implementation.tex', 'chapters/evaluation.tex',
             'chapters/discussion.tex', 'appendix/formative-interview-plan.tex',
             'appendix/codebook-and-traceability.tex',
             'appendix/evaluation-appendix.tex', 'appendix/glossary.tex']
    # abbreviation -> pattern its expansion must match, at or before first bare use
    ABBREV = {
        'GDPR':  r'General Data Protection Regulation',
        'TAM':   r'Technology Acceptance Model',
        'UEQ':   r'User Experience Questionnaire',
        'ECTS':  r'European Credit Transfer',
        'StEOP': r'Studieneingangs',
        'ERS':   r'Educational Recommender System',
        'ED':    r'Educational Dashboard',
        'OOS':   r'out[- ]of[- ]scope',
        'CMS':   r'course management',
        'LMS':   r'learning management',
        'GPA':   r'grade[- ]point average',
        'TA':    r'thematic analysis',
    }
    doc = ''
    for f in ORDER:
        if f not in bodies:
            continue
        doc += re.sub(r'\\TD(?:block|major|minor|rev|ok)\{.*', '', bodies[f]) + '\n'
    for ab, expansion in ABBREV.items():
        hits = list(re.finditer(r'(?<![A-Za-z\\])' + re.escape(ab) + r'(?![A-Za-z])', doc))
        if len(hits) < 2:
            continue
        i = hits[0].start()
        exp = re.search(expansion, doc[:i + len(ab) + 40], re.I)
        if not exp:
            warn('%s used %d times, first use not introduced: ...%s...'
                 % (ab, len(hits), re.sub(r'\s+', ' ', doc[max(0, i-70):i+len(ab)+12])))

    print('\nBLOCKING CHECKS FAILED' if fail else '\nall blocking checks passed')
    return 1 if fail else 0

if __name__ == '__main__':
    sys.exit(main())
