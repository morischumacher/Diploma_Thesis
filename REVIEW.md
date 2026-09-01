# Examiner-style review — full pass, 2026-08-31

Branch: `review/examiner-pass`. Every finding below was verified against the repository, the
study material in `evaluation-study/` on your Mac (stage logs, findings matrix, codebook,
session files, transcripts, `US Results.xlsx` raw JSON), the source PDFs in
`context/related-work/`, and the `studyplanner` codebase. Where I could not open a source, I
say so in §7 rather than assessing it. In-text comments use `%% AIREV [severity]` and are
distinct from your supervisor's `%% REV` comments, which I have left untouched and inventoried
in §3.C.

---

## 1. The argument, and whether it holds

As the text currently makes it: **students' elicited needs justify a hybrid graph–table
planner whose evaluation shows that planning under it is a single checklist-driven loop, into
which the graph enters at exactly one point — replacing the catalogue as the surface where a
named gap becomes candidate courses — while the compliance layer students trust certifies
plans it has not fully checked.**

My judgement: the argument from Chapter 4 onward is strong, unusually well-evidenced, and the
evaluation's process account survives independent re-derivation almost everywhere I checked
(§3.C). It does not yet hold end to end, for one reason: the front of the thesis still
promises what the back of the thesis disproves. RQ1 and RQ2 name "understanding of course
dependencies", the Related Work gap statement names a "dependency-revealing graph", and
today's commit `492d9af` removed the sentences that reconciled that promise with Chapter 8's
finding that the graph renders containment only and the curricula barely encode dependencies.
The commit's rationale (this thesis defines dependency as containment) is stated nowhere in
the document, and Chapter 8 itself uses "dependency" in the prerequisite sense
("Structural Legibility Without Dependency Information"). Until the two halves use the word
in one sense, or the front qualifies its promise, the thread is broken at its most quotable
point. Everything needed to close it already exists in the deleted text of `9c1bd75`.

---

## 2. Blockers

Each also carries an `%% AIREV [BLOCKER]` comment at the exact line.

1. **`chapters/introduction.tex`, Research Question 1 (and RQ2).** The RQs promise
   "understanding of course dependencies"; Chapter 8 reports no dependency information was
   rendered and none was missed by the curricula. Restore a qualifier (the removed sentence
   from `9c1bd75` did the job) or reword the RQs. As it stands, an examiner reads RQ1 aloud
   and then Table 8.8's E-G08 at 2/11.

2. **`chapters/relatedwork.tex`, Positioning.** The gap this thesis "sets out to close" is
   still "a browsable, **dependency-revealing** graph … over a single, synchronised plan".
   The built artefact reveals no dependencies. "Browsable curriculum graph" is true and
   costs nothing.

3. **`chapters/evaluation.tex`, Participants.** "Participant webcams were not captured in
   any session" contradicts `chapters/methodology.tex` §2.7, which states (verifiably) that
   the earlier recordings retain the meeting window and webcam tile. One of the two
   sentences is false in the same document. Scope the Evaluation sentence to the four later
   sessions, or drop it.

4. **`chapters/evaluation.tex`, §8.3.4 (graph's role).** E-G18 is misattributed to P06. The
   matrix records P06 as *undecided* for E-G18; the session files evidence it for P09
   (season × not-planned filter, acted on the negative answer) and P12. The filter named in
   the text ("category") is also not the one used (season/semester). Suggested replacement
   sentence is in the comment.

5. **`chapters/evaluation.tex`, Summary, final sentence.** "The defects this study surfaced
   have since been corrected in the tool, each with a regression test" is not supported by
   the codebase: `studyplanner` `main` contains none of these fixes; they live on the
   unmerged branch `fix/evaluation-defects`, whose own register (`docs/known-defects.md`)
   lists the study's E-P codes as **open** and marks a different set (defects found by
   reading the code) as fixed. Delete or scope the sentence.

6. **`appendix/evaluation-appendix.tex`, Catalogue of unmet requirements.** The table is
   still the seven-participant version (every denominator is 7), while Discussion Table 9.1
   reports the same capabilities at /10 and /11. Every shared row disagrees between chapter
   and appendix. Regenerate at N=11 or state the cohort mismatch explicitly.

7. **`main.tex`, metadata.** Title is "Title of the Thesis", subtitle is the template
   placeholder, date is 01.01.2001, keywords are "a list of keywords". These print on the
   title pages of the submitted PDF. (I set the author name and PDF language; the rest only
   you can supply.)

8. **`chapters/implementation.tex`, §7.4.1.** The sentence "Attempting to abstract the
   remaining logic into a unified base class" breaks off mid-sentence and prints incomplete
   in the PDF (it sits beside your own `%% REV` asking for a future-work note; completing it
   answers both).

Adjacent to blockers, decided by you: three open `\todo{}` markers (methodology: recordings
storage/retention + consent PDF with real name and birthdate in git history + webcam tiles;
discussion: concrete redesign-vs-reparameterise split; formative study: forward-reference
structure) and the 23 new `%% REV` comments (19 implementation, 4 evaluation) — inventoried
in §3.C below.

---

## 3. Major findings, by the brief's categories

### A. Story and structure

- **Each chapter hands the next what it needs, and says so** — this genuinely holds from
  Chapter 4 through 9: formative study → features (stated at both ends), features → design
  (every decision cites its source), design → implementation ("realises, does not restate"),
  implementation → evaluation (system under test named component by component), evaluation →
  discussion (each Discussion paragraph opens from a Chapter 8 result). I looked for a
  chapter that silently assumes something its predecessor never delivered and did not find
  one — with the single exception of the dependency promise (§2.1–2.2).
- **The formative study chapter reports no findings.** It is all method: goal, prototype,
  participants, procedure, analysis method — and then Chapter 5 starts from "the final theme
  set" the reader has never seen. The themes are never named, listed, or counted anywhere in
  the thesis. (`%% AIREV [MAJOR]` at §4.5.5; see also B on codes vs themes.) This is the
  first question a TA-literate examiner asks.
- **RQ referencing is uneven.** RQ1 is restated verbatim as a quote block in Chapter 4 and
  answered by declaration in Chapter 5's intro; RQ2 is addressed by one sentence each at the
  top of Design and Implementation; RQ3 is restated in bold-italic at the top of Chapter 8
  and is the only one explicitly mapped to measures (the ISO dimension mapping — the
  strongest RQ treatment in the thesis). No chapter states "RQ1 is now answered: the answer
  is the specification of Table X" in a form you could point to at the defence. A three-
  sentence "answers to the research questions" block in the Discussion would fix all three
  at once — currently the Discussion never mentions RQ1 or RQ2 by name at all
  ("RQ3" appears once).
- **Abstraction level** is stable inside almost every section — the Design chapter's
  dimension-first organisation does what its intro promises. The one repeated wobble:
  Implementation §7.2.4's reconciliation qualification (already covered by your REV) and
  Evaluation §8.1's intro doing methods work that §8.2 then redoes.
- **Content in the wrong place:** the methodology's Expected Results section restates the
  Introduction's contributions and the Discussion's generalisability argument
  (`%% AIREV [MAJOR]`, saves ~1.5pp); appendix "Process state model" repeats Chapter 8's
  Table 8.2 as a figure (`%% AIREV [MAJOR]`); the interview-plan appendix carries scope
  clarifications that duplicate §4.4.
- **Missing:** abstract, Kurzfassung, acknowledgements, AI-tools disclosure (both
  languages) are all empty files — `main.tex` inputs them, so they render as empty headed
  pages. Not commented in-text since they are known work items (CONTROL.md §10).

### B. Consistency

- **Codes vs themes is the biggest terminological fault after "dependency".** Appendix D
  presents C1–C64 as "the complete consolidated codebook produced during Step 2" — the
  output of theme consolidation. Chapter 5, the Design chapter, and the glossary call the
  same C-items "codes" attached to excerpts during *initial* coding. The source
  (`First Open Coding.docx`) holds 438 initial codes consolidated into the 64 C-items. So
  the C-items sit exactly where the chapters say "themes" live, yet nothing is ever called
  a theme. Comments at `needfindingwithprototype.tex` (§4.5.5) and `glossary.tex`. The fix
  is a decision, not a rewrite: say once what C1–C64 are, and align the glossary's Code and
  Theme entries.
- **The two studies**: named consistently ("the formative study" / "the evaluation study"
  everywhere — I checked; no "study 1/2" survives). Method depth is now roughly comparable —
  the evaluation's §8.1 (design, conditions, order rationale, instruments, cohort,
  two-record analysis) is, if anything, the fuller of the two; the asymmetry your brief
  remembered has been repaired. What remains asymmetric: the formative study's method is
  *justified* at three times the length (see E) while the evaluation's is merely *stated* —
  the imbalance is now in the other direction.
- **Artefact naming** is stable: "the tool"/"the study planner" for the artefact,
  "study-guide application"/"questionnaire application" for the instrument (both terms used,
  but defined as the same thing at first use in §8.1.3 and §7.6 — acceptable), panel names
  capitalised consistently (Parking Stage, Dashboard, Recommendation Panel, Table View,
  Graph View). One slip fixed silently ("dependency-oriented view" in Implementation).
- **Punctuation**: no em-dashes in prose anywhere (checked); no bold in prose outside item
  labels (checked; the RQ restatements use `\textbf` for the RQ label, consistent across
  chapters); Oxford-comma usage is consistent.
- **Figure captions**: six were outside the 100–200-character house range; fixed silently
  (§4). The rest conform.
- **The appendix is internally consistent** in format except the unmet-requirements table's
  stale cohort (§2.6) and the codebook table's conversion garbage (fixed, §4).

### C. Rigour — what I traced, what matched, what did not

**Verified correct, from the raw material** (this is the part of the thesis I could not
break, and I tried):

- **Every UEQ number**: all six scale means, SDs (population-SD convention), ranges,
  pragmatic/hedonic/overall aggregates, and all eleven per-participant overall scores in
  Table 8.1 reproduce exactly from the Raw-JSON column of `US Results.xlsx` under the
  questionnaire app's own item order (which I took from the app's source, not the standard
  UEQ order — the app's order differs, and the spreadsheet's 8 UEQ columns are lossy;
  anyone recomputing from those will get wrong numbers). P08's −0.96 reproduces.
- **Every TAM/acceptance number**: PU 6.18/6.45, PEU-two-item 5.59/6.09, overview item
  6.36/6.55, satisfaction 6.27/5.91, difficulty 6.18/6.00, and the item-level correlations
  (+0.88/+0.74 in B, +0.66/+0.34 in A) all reproduce. The instrument's item wordings in the
  appendix match the deployed app's HTML verbatim, including which item is the overview
  item. The chapter's TAM handling implements the documented tam-check analysis correctly.
- **The code matrix**: all 101 rows of Appendix D.3 match `findings-matrix.csv` cell-for-
  cell; every frequency matches its own dot count; all 99 codes cited anywhere in the text
  have definitions; every "(E-Pxx, n/m)" in chapter prose matches the matrix. Zero
  discrepancies.
- **Process metrics, Scenario A**: my independent parser reproduces occupancy, entries,
  dwell, and the transition shares (27.5 %, 17.4 %, 44.9 %, 3.1 %) exactly; recommendation-
  panel occupancy (24 %), entries (23/8), dwell (125 s/244 s), the 880-second longest
  episode, the five non-openers and three half-run-openers in B, and the per-participant
  catalogue-occupancy medians (27.4 → 4.5) all reproduce. The completion audit's 22 rows
  match `completion-audit.md` row for row, including P12-A's deliberate "unresolved".
  The sign test (p = 0.55 for 7/11) is correct. P02's 102-planned/24-parked and the
  437-frame warnings-panel observation trace to the session files.
- **Quotes**: every quoted utterance I checked (12 of them: P01×2, P02, P03, P04×2, P06,
  P09×2, P10×2, P12) exists in the named participant's transcript with the meaning quoted.

**Did not match / not supported:**

- **The frame count is three numbers** (BLOCKER-adjacent, `%% AIREV [MAJOR]` at §8.1.5):
  chapter text and appendix say 2,158; the chapter's own Table 8.2 sums to 2,157;
  `process-metrics.md` says 2,157; my re-parse of the same stage-log folder finds 2,192,
  surplus entirely in `off` frames. Under my parse Scenario B's headline loop shares come
  out 15–17 % rather than 20.0/20.0, and "eight episodes longer than three minutes" comes
  out nine. Direction and every conclusion survive; the numbers as printed are not
  reproducible from the material as it stands. One frozen parser, one total, all documents.
- **E-G18 misattributed to P06** (§2.4).
- **P10 framed as "not placing from the graph at all"** while his next utterance places
  from the graph successfully (`%% AIREV [MAJOR]`; the honest version is stronger for your
  claim).
- **The "defects since corrected" sentence** (§2.5).
- **Translated quotes are nowhere declared as translations** (`%% AIREV [MINOR]` at §4.5.1;
  one sentence fixes both studies). Note P09's "wow" is not in the transcript ("ganz schön
  viel") — with a translation sentence in place, light smoothing is defensible; without
  one, "verbatim" is claimed and not delivered.
- **Citations** (all weight-bearing ones opened; details in the comment at each site):
  - *Ma et al. 2021*: significant effects are on perceived accuracy, sufficiency,
    transparency, trust; ease-of-use was significantly better for the **baseline**;
    "significantly improves user acceptance and understanding" overstates (MAJOR).
  - *Bodily & Verbert 2017*: 93 **articles**, not systems; 17 %/6 % are shares of articles
    (fixed silently, exactly per the source).
  - *Bartel et al. 2024*: nine principles confirmed, quoted principle texts confirmed
    verbatim; but "user-centred design" and "study-programme-specific personalisation" are
    **one combined principle**, not two (fixed where miscounted); and the two problems the
    Discussion "confirms" were reported for Bartel's own prototype, not for assistants in
    general (MINOR).
  - *Braun & Clarke 2022*: the p. 242 / "pp. 242–245, 271" page anchors for the tripartite
    claims were wrong (correct: pp. 227–228, 235–237; reflexive themes pp. 77–78) and the
    six phase names in §4.5 were the 2006 paper's, which this book explicitly renamed —
    both fixed silently against the book. All other page-anchored claims verified,
    including the p. 141 frequency quote verbatim.
  - *Munzner 2009*: all six claims the Methodology rests on verified with quotes.
  - *Trippel & Röpke 2025, Auvinen 2014 (STOPS), Hirmer 2022, Davis 1989 (via the full
    tam-check), Nielsen 1994 (both heuristics), Sandelowski 2001, Gale 2013*: verified.
  - *Wienand et al. 2024*: **could not verify** — no PDF, and the bibliography shows it is
    about enterprise-systems training e-learning, not study planning; the "index card-like
    presentation" quotation and the multi-level-progress-bars claim rest on an unopened
    source from another domain (MAJOR at design.tex §6.2.4).
  - The five-paper "broad consensus" sentence in Related Work: four of five support it
    directly; Schwendimann 2017 is descriptive rather than advocating — mild overreach,
    left uncommented.
- **The recommender's six channels**: `studyplanner`'s defect branch records that two of
  the six could never fire against real data in the evaluated build ("four channels were
  live during the study, not six"). If that holds for `v1.0-evaluated`, Implementation §7.4.2
  and the Evaluation's system-under-test description need one scoping sentence (MAJOR at
  §7.4.2).
- **Claims vs. evidence proportionality**: generally exemplary — the fixed-order bound, the
  reported null, the "description of the second run" framing, and the Discussion's
  establishes/suggests split are the thesis's best defensive armour. The two places the
  text claims more than the design supports are the two BLOCKERs above (defects-corrected;
  webcams), plus Discussion Table 9.1's unexplained 10/11 row (MINOR).

**Open `%% REV` and `\todo{}` inventory** (yours; untouched): 19 in `implementation.tex`,
4 in `evaluation.tex`, all still in the files. They are indexed one-to-one, with location,
bucket and status, in the D4 table of `REVIEW-PLAN.md`; that table is the authoritative
list, because the prose summary that stood here omitted four of them, including the
edit-flow figure's colliding arrow labels (`implementation.tex:121`). Three now carry an
`%% AIREV` answer beside them and each turned out to be a defect: the curriculum-as-data
claim, the Wong citation, and the one-plan-per-account cardinality. `\todo{}` ×3 as in §2.

### D. Language and economy

Meta-discourse sentences that describe the writing rather than say anything — candidates for
deletion (they are roadmap-only; each chapter's structure is visible from its headings):

- design.tex §6.2 opening: "This section details the visual encoding strategies used to…"
- design.tex §6.11 opening two sentences ("This section covers the design of how…").
- evaluation.tex §8.1 opening sentence 2 ("This section states the system under test…").
- evaluation.tex §8.2 opening sentence 3 ("This section establishes that loop…").
- methodology.tex chapter opening ("This chapter sets out the methodological frame…").
- fromthemestorequirements.tex opening sentence ("This chapter translates…") — keep the
  RQ1-completion sentence, cut the rest of the paragraph's scaffolding.
- needfindingwithprototype.tex "Link to Subsequent Chapters" subsection is one page of
  pointing forward; two sentences would do.

Boilerplate/register: the thesis is largely clean of generated-sounding filler; the
remaining ornate spots are the Analysis Method's TA apologia (see E) and Chapter 5's
step-by-step methods citations for self-evident moves. Sentences that could be half as
long without loss cluster in design.tex's alternatives paragraphs and methodology.tex §2.1's
second half — both covered by shortening comments rather than listed exhaustively here.

### E. Length (see §5 for the plan)

Where the 182 pages sit: front matter 15, Intro 4, Methodology 8, Related Work 6, Formative
12, Themes→Requirements 14, Design 30, Implementation 12, Evaluation 20, Discussion 10,
back matter (AI tools, lists, bibliography) 18, appendices 31.

Over-explained relative to importance: TA positioning (Ch. 4), the five derivation steps and
per-feature evidence walls (Ch. 5), rejected alternatives (Ch. 6), Expected Results (Ch. 2).
Under-explained relative to importance: the formative study's *findings* (nothing), the
answers to RQ1/RQ2 as answers (one sentence each), and the dependency definition (absent).

---

## 4. Silent fixes, by category and count

| Category | Count |
|---|---|
| Conversion-garbage strings (`**``****''''**`) removed from Appendix D codebook table | 13 |
| American → British spellings (Appendix D labels, interview-plan appendix, methodology "rigor") | 29 |
| Grammar/typo (missing article, "the a label", missing conjunction, sentence fragment, contrasts-with, Notta.ai) | 6 |
| Citation-accuracy corrections applied verbatim from the opened source (Bodily articles/percent bases ×3; Bartel combined-principle ×1; Braun & Clarke page anchors ×3 and phase names ×1) | 8 |
| Cross-reference corrections (glossary "Programme" pointed to Scope, not Limitations) | 1 |
| Internal-consistency corrections ("dependency-oriented" → "structure-oriented" view; appendix TAM wording aligned with the chapter's deliberate "TAM-derived" framing; "above E-P46" → "after"; `CONTROL.md` reference removed from thesis prose) | 4 |
| Figure captions brought into the 100–200-character house range (3 undersized prototype captions, 3 oversized) | 6 |
| Bibliography repairs (duplicate `laghari_academic_2023` removed; ISO 9241-210 given author/year so BibTeX can sort it; `bodily_review_2017` retyped `@article`, fixing the empty-booktitle and volume+number warnings) | 3 |
| Appendix D traceability matrix regenerated by its own stated rule (design-section column now matches the chapter's actual section titles; "PREAMBLE" and five phantom section names gone; FEATURE-003/-013 titles aligned with Chapter 5) | 1 table |
| `main.tex` metadata (author name set; PDF language de-AT → en-GB) | 2 |

All edits brace-checked at edit time; compile, `\label`/`\ref` sweep, and `\cite` check in §8.

## 5. Shortening plan — route from 182 to ≈ 130–140 pages

Ordered by pages saved against cost. Nothing below is cut; the first five carry
`%% AIREV [MAJOR]` comments at the site. Items 1–6 ≈ 26 pp → ~156. Adding item 7 (the
structural move) reaches ≈ 140–145; ≈ 130 is only reachable with items 7 **and** 8, which
change the thesis's shape and are yours to call.

| # | Item | Location | Est. saved | What is lost |
|---|---|---|---|---|
| 1 | Full feature specs → appendix; 2-page summary table stays | Ch. 5 §5.2 | 8–10 pp | Nothing evidential (specs remain citable in the appendix); the chapter reads as the answer to RQ1 rather than a catalogue |
| 2 | Rejected-alternatives paragraphs cut to one sentence where the alternative was never live | Ch. 6, ~10 of ~20 sites | 5–6 pp | A record of non-decisions; keep the four genuinely weighed ones in full |
| 3 | TA positioning to one paragraph + recursion caveat stated once | Ch. 4 §4.5 | 2–3 pp | Methodological self-defence an examiner doesn't need three times |
| 4 | Expected Results to one paragraph; nested-model fitness argument stated once | Ch. 2 | 2 pp | Duplication of Intro and Discussion |
| 5 | Appendix: drop the process-state-model duplicate figure; compress interview-plan script (prompts as run-in lists) | App. C.5, App. A | 3 pp | A redundant rendering; verbatim staging directions |
| 6 | Scenario briefs to appendix (your own REV); Ch. 5 derivation steps 1–5 to one page | Ch. 8 §8.1.2, Ch. 5 §5.1 | 3 pp | Nothing; the briefs stay reproduced in full |
| 7 | Design chapter to ~20 pp: fold Visual Legend + Onboarding into General Architecture's tail; run Why/What/Alternatives tighter per section; merge the two module-interaction discussions | Ch. 6 | 6–8 pp | Some of the per-decision narrative rhythm; traceability chain untouched |
| 8 | Halve the evaluation codebook tables by moving definitions ≤2 lines into a compact two-column layout, and cut Discussion Table 9.1 (pointing at the regenerated appendix catalogue instead) | App. C, Ch. 9 | 4–5 pp | In-chapter convenience; nothing evidential |

## 6. If I had one day

1. **Close the dependency seam**: restore a one-sentence qualifier at RQ1, change
   "dependency-revealing" to "browsable" in the Related Work gap, add the glossary entry.
   Three edits; removes the thesis's most quotable self-contradiction.
2. **Make the evaluation's numbers reproducible**: rerun one frozen stage-log parser, pick
   one frame total, regenerate Table 8.2, the loop shares, the appendix, and the N=11
   unmet-requirements catalogue from it, and fix the E-G18 attribution while in there. After
   that, the chapter's every number survives an adversarial recount — it is already 95 %
   of the way there.
3. **Delete the two unsupportable sentences**: "defects have since been corrected…" and
   "webcams were not captured in any session". Both are one-line fixes to claims a single
   `git log` or a single early recording falsifies.

## 7. What I could not check

- **Wienand et al. 2024** — no PDF anywhere in `context/`; the design chapter's two claims
  from it (including a direct quotation) are unverified. Open access at
  doi 10.1007/s44217-024-00165-z; five minutes with the PDF settles it.
- **Vessey 1991 (cognitive fit), Laugwitz 2008 (UEQ construction), Ware 2004, Palmer 1992,
  Shneiderman 1983** — no PDFs locally; the uses are conventional (and the UEQ structure I
  verified against the instrument itself), but I did not open the sources, so I have not
  assessed them.
- **P12-A's two unreadable lanes** — unresolvable by design; correctly reported as unknown.
- **FAC coding for P09–P12** — uncodeable per the recordings' format; the thesis says so.
- **Whether the two inert recommendation channels were inert in `v1.0-evaluated`
  specifically** — the defect register's finding is from the current code; confirming it for
  the evaluated tag needs a checkout and one grep of the knowledge-graph course codes
  against the catalogue (`git show v1.0-evaluated:...`), which I flagged rather than ran,
  since the consequence is a wording decision that is yours either way.
- **The seven-participant recordings' German transcripts** are Notta/Gemini auto-transcripts
  with garbled passages; quote verification was against meaning, not character-for-character
  (see the translation finding).
### Corrections to this document (second pass, same day)

Two first-pass claims were wrong, both because I checked the `studyplanner` refactor branch
where I should have checked the evaluated tag. Both are now findings in their own right:

- I recorded the **curriculum-as-data** claim (Implementation §7.4.1) as verified against the
  code. It is not true of the evaluated build: `v1.0-evaluated` contains no curriculum
  configuration file, and the bachelor checker's constructor alone is 391 lines of curriculum
  written as Python statements. The separation the chapter describes exists on the unmerged
  `fix/evaluation-defects` branch, whose own ADR 0002 states the problem in the same words the
  chapter uses to claim it solved. Now an `%% AIREV [BLOCKER]` at that paragraph.
- I recorded the **two recommender citations** as checking out. Bhumichitr does, precisely
  (user-based CF with Pearson plus ALS, on real elective-enrolment data). Wong does not: it is
  a four-page doctoral-consortium proposal for an LSTM over transcript sequences, it supports
  the typical-sequence half of the clause and mentions prerequisites only as a constraint a
  future system "will need to consider", and it self-describes as "a novel approach" while
  being cited as a standard, well-established technique. Now an `%% AIREV [MAJOR]` at that
  clause. This is the same misattribution that was moved off `esteban_helping_2020` in an
  earlier session and left resting on Wong alone.

- **Compile-time only**: `\printindex` renders an empty index (nothing is ever `\index`ed);
  either populate or comment it out before submission — not flagged in-text as it is a
  build-configuration choice.
