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

    # --- structural: every \includegraphics resolves (blocking) -----------
    # main.tex stopped producing a PDF because pictures/Full_view_crop.png was
    # referenced and absent, and every check still reported green: the checker
    # read the source and never asked whether the files it points at exist.
    for f, t in bodies.items():
        for m in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}', t):
            g = m.group(1)
            if not any(os.path.exists(g + e) for e in ('', '.pdf', '.png', '.jpg', '.jpeg', '.eps')):
                bad(f'{f}: \\includegraphics file not found: {g}')

    # --- structural: brace balance ---------------------------------------
    for f, t in texts.items():
        if t.count('{') != t.count('}'):
            bad(f'brace imbalance in {f}: {t.count("{")} open, {t.count("}")} close')

    # --- style ------------------------------------------------------------
    targets = [args.chapter] if args.chapter else \
              [f for f in TEX if f.startswith(('chapters/', 'appendix/'))]
    AMERICAN = r'\b(color|colors|behavior|behaviors|catalog|catalogs|judgment|favor|labeled|modeling|analyze|analyzed|fulfillments?|programs?|visualization|personalization|prioritization|organized|recognized|minimize|utilize|emphasize|individualized)\b'
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
        # %% REV markers live in comments, so this one check reads the raw
        # file. Running it on the comment-stripped body, as it did until
        # 2026-09-03, meant it could never fire: sixteen open REV comments sat
        # in relatedwork.tex with the checker silent. Only --submission caught
        # them, and only at the very end.
        n_rev = len(re.findall(r'%%\s*(?:AI)?REV', texts[f]))
        if n_rev:
            warn('%s: %d unresolved %%%% REV comment(s)' % (f, n_rev))

        t = bodies[f]
        # the glossary defines the study names, so it may use their variants
        if f.endswith('glossary.tex'):
            t = re.sub(r'\b(needfinding study|summative study)\b', '', t)
        for pat, msg in [(AMERICAN, 'American spelling'), ('—', 'em dash in prose'),
                         (r'``', 'TeX quotes -- house form is \\enquote{}'),
                         (SLANG, 'colloquialism'),
                         (r'\bwill\b', 'future tense "will"'),
                         (r'\d+ ECTS', 'ECTS without ~'),
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

    # --- OOS count agreement (blocking) ----------------------------------
    # The OOS items are defined once in methodology.tex and then counted and
    # ranged over in five other files. Adding one has twice left a stale "all
    # four boundaries" or "OOS1--OOS4" behind, so the count is derived from the
    # definitions and every count and range elsewhere must agree with it.
    WORD = {2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}
    defined = sorted(int(n) for n in
                     re.findall(r'\\textbf\{OOS(\d+),', bodies.get('chapters/methodology.tex', '')))
    if defined:
        n = max(defined)
        if defined != list(range(1, n + 1)):
            bad(f'OOS items defined in methodology.tex are not contiguous: {defined}')
        for f, t in bodies.items():
            # A range is only wrong if it claims more items than exist. A prefix
            # sub-range can be deliberate: OOS5 bounds what the thesis claims
            # rather than what the artefact omits, so the exclusion sites in
            # Chapter 4 and the codebook legitimately say OOS1--OOS4.
            for m in re.finditer(r'OOS1\s*-{2,3}\s*OOS(\d+)', t):
                k = int(m.group(1))
                if k > n:
                    bad(f'{f}: range {m.group(0)} but only {n} OOS items are defined')
                elif k < n:
                    warn(f'{f}: range {m.group(0)} is a sub-range of OOS1--OOS{n}; '
                         'confirm it is deliberate')
            # A count attached to the word "boundaries" is a totality claim and
            # must match. This is what went stale twice.
            for m in re.finditer(r'\b(two|three|four|five|six|seven)\s+'
                                 r'(?:OOS\s+|scope\s+)?boundaries\b', t, re.I):
                if m.group(1).lower() != WORD[n]:
                    ctx = re.sub(r'\s+', ' ', t[max(0, m.start() - 45):m.start() + 55])
                    bad(f'{f}: says "{m.group(0)}" where {n} OOS items are defined: ...{ctx}...')

    # --- evaluation participant counts -----------------------------------
    # Twelve sessions were conducted, eleven are analysed (P08, no screen
    # recording). Which number is right depends on the verb, so the blocking
    # checks are only the phrasings that are contradictions on their face;
    # everything else is listed for a human to judge.
    # Judged per clause, not per window: "Twelve sessions were conducted and
    # eleven are analysed" is the canonical sentence and holds both numbers, so
    # a window-based match flags the one sentence that is definitely right.
    def clauses(text):
        return re.split(r'[.;:,]|\band\b|\bwhereas\b|\bwhile\b', text)

    CONTRADICTIONS = [
        (lambda c: re.search(r'\beleven\b', c, re.I)
                   and re.search(r'\b(?:sessions?|interviews?)\b', c, re.I)
                   and re.search(r'\b(?:conducted|were run|were held|ran|held)\b', c, re.I),
         'eleven sessions conducted: twelve were conducted, eleven analysed'),
        (lambda c: re.search(r'\btwelve\b', c, re.I) and re.search(r'\banalys', c, re.I),
         'twelve analysed: eleven are analysed'),
        # A denominator, not one number in a slash-separated sequence: the
        # appendix plan tables hold ECTS runs like 32/31/32/30/27/12/16.
        (lambda c: re.search(r'(?<![\d/])\d+\s*/\s*12(?![\d/])', c),
         'denominator /12: frequencies are over the eleven analysed participants'),
    ]
    EVAL_FILES = ('chapters/evaluation.tex', 'chapters/discussion.tex',
                  'chapters/implementation.tex', 'chapters/methodology.tex',
                  'chapters/introduction.tex', 'appendix/evaluation-appendix.tex',
                  'appendix/glossary.tex')
    seen = []
    for f in EVAL_FILES:
        t = bodies.get(f)
        if not t:
            continue
        prose = re.sub(r'\\TD(?:block|major|minor|rev|ok)\{.*', '', t)
        for c in clauses(prose):
            for test, msg in CONTRADICTIONS:
                if test(c):
                    bad('%s: %s: ...%s...' % (f, msg, re.sub(r'\s+', ' ', c.strip())[:90]))
        for m in re.finditer(r'\b(eleven|twelve)\b[^.]{0,45}?'
                             r'\b(participants?|students?|sessions?)\b', prose, re.I):
            seen.append(re.sub(r'\s+', ' ', m.group(0)))
    if seen:
        warn('%d evaluation count statements (12 run / 11 analysed; check each '
             'against §0): %s ...' % (len(seen), ' | '.join(seen[:4])))

    print('\nBLOCKING CHECKS FAILED' if fail else '\nall blocking checks passed')
    return 1 if fail else 0

if __name__ == '__main__':
    sys.exit(main())
