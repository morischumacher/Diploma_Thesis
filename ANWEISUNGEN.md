# ANWEISUNGEN — Thesis Finalisation Guidelines

**Owner:** Moritz Jakob Schumacher · **Advisor:** Assistant Prof. Dr. René Röpke · **First assistant:** Selina Reinhard
**Repo:** `morischumacher/Diploma_Thesis` (branch `main`) · **Template:** `vutinfth`, BibTeX `alpha`
**Deadline:** 10 September 2026 · **Created:** 2 September 2026 (session 1)

This file governs the chapter-by-chapter finalisation. It is the single source of house rules. `CONTROL.md` remains the project history and decision log; `REVIEW.md` is the 31 Aug examiner-style review and is now partly stale (§13 records what it got wrong). Where the three disagree, **this file wins**.

---

## 0. Baseline established this session

The thesis compiles cleanly. `pdflatex → bibtex → makeglossaries → makeindex → pdflatex ×2` produces **184 pages** with **zero undefined references and zero undefined citations**, 30 overfull and 38 underfull boxes.

| Part | Pages | Notes |
|---|---|---|
| Front matter (i–xv) | 16 | Kurzfassung, Abstract, Acknowledgements all **empty files** |
| 1 Introduction | 4 | |
| 2 Methodology | 8 | |
| 3 Related Work | 6 | |
| 4 Formative Study | 12 | reports no findings — see §1.4 |
| 5 From Themes to Requirements | 4 | already a summary table only; full specs are in App. A.3 |
| 6 Design | 28 | the one genuinely long chapter |
| 7 Implementation | 16 | |
| 8 Evaluation | 20 | |
| 9 Discussion | 12 | |
| **Main matter total** | **110** | |
| AI-tools disclosure | 4 | **both files empty** — renders as empty headed pages |
| Lists of figures/tables | 6 | |
| Bibliography | 8 | 70 keys cited, 91 entries, 21 uncited |
| Appendix A (formative) | 22 | |
| Appendix B (evaluation) + Glossary | ~34 | |

**Table 8.8 does not match its own appendix.** Found 2026-09-02 by comparing every row of the problems table against the codebook and the code matrix. E-P15's row is a different code entirely (chapter: "The graph makes soft dependencies visible", 6/11; codebook: "Layout-axis configuration popup surfaces mid-task", 1/11) and contradicts §8.7 and Ch. 9. E-P50 is 9/9 in the matrix and in the chapter's own prose but 9/11 in the table; E-P68 is 4/9 in both but 4/11 in the table. E-P29 is severity 2–3 in the table and 2 in the codebook. **Run this comparison for Table 8.9 and the unmet-capabilities table too before Ch. 8 is closed** — one systematic mismatch means the tables were not generated from the artefacts.

**What closing Chapter 8 must trigger.** Chapters 1 and 2 are closed while Chapter 8 is still open, so four sentences in them assert Chapter 8 *content* rather than merely pointing at it. Each is a hostage to an unfinished chapter, and none of them is visible from inside Chapter 8. When Chapter 8 closes, re-check all four before anything else:

| Where | Rests on |
|---|---|
| Ch. 1 §1.4, contribution 3 | the graph displaces the catalogue at the find step and not at the commit step |
| Ch. 1 §1.4, contribution 4 | every participant reported success where no plan met its brief |
| Ch. 1 §1.4, closing paragraph | frame-sampled log, participant-level frequencies, ISO 9241-11 dimensions, fixed scenario order, eleven analysed |
| Ch. 2 §2.5, "What a curriculum encodes" | two formal prerequisite pairs, near-empty overlay, and Ch. 8's own bounding sentence. **A drafted correction is already in the chapter as a `\TDrev`**, deferred 2026-09-03 because Ch. 8 is not final: the current second sentence claims the evaluation tested the premise, which Ch. 8 explicitly disclaims. |

Ch. 1's contributions already carry a `\TDrev` for the first three. Ch. 2's is the note added 2026-09-03.

**Consistency register — the canonical values.** Any number below appears in more than one chapter. Change it in one place and you must change it everywhere; never introduce a variant.

| Quantity | Canonical value |
|---|---|
| Formative study participants | 6 (I1–I6), 3 BSc + 3 MSc |
| Initial codes | 435 |
| Consolidated themes | 64 (C1–C64); 51 carried, 11 out of scope, 2 procedural |
| Features / requirements | 13 features, 55 numbered requirements |
| Evaluation sessions run / analysed | 12 run, **11 analysed** (P08 excluded, no screen recording) |
| Scenario runs | 22 |
| Sampled frames | **2,179** (Scenario A 1,197 + Scenario B 982) |
| Evaluation codes | 99 total: 68 E-P, 22 E-G, 9 E-N |
| Unmet capabilities | 27 distinct |
| Programmes in scope | 2 — BSc Computer Science UE 033 521, MSc **Software Engineering** UE 066 937. *Not* "Software Engineering & Internet Computing": the programme was renamed, confirmed against the curriculum's own title page (Senate 16 June 2025, in force 1 October 2025) |
| Bachelor programme total | 180 ECTS, 101 courses |
| Scope boundaries | OOS1–OOS5 (see §5; OOS5 bounds what is claimed, so the exclusion sites legitimately cite OOS1–OOS4) |

**The evaluation study has two counts, and which one is correct depends on the verb.** Twelve sessions were conducted; eleven are analysed. P08 was excluded because the session ran without a screen recording, and the analysis method needs both records. Neither number is "the" number:

| The sentence is about | Number | Examples |
|---|---|---|
| What was run, recruited, consented, used | **twelve** | "twelve moderated observational sessions"; "the system used in the evaluation study" |
| What was analysed, coded, counted, concluded | **eleven** | "the eleven analysed participants"; every finding, every table, every claim |
| A frequency denominator | **/11** | a smaller denominator (9/9, 4/9) marks a code that could not be evidenced in every session and must say so where it appears |

Never write "eleven sessions were conducted" or "twelve analysed". Never a `/12` denominator. Where the count is incidental to the point, prefer naming the study over counting heads: `implementation.tex` §7.9 said "the system the eleven participants used", which is wrong because twelve used it, and now says "the system used in the evaluation study". `tools/check.py` fails on the contradictory phrasings and lists every count statement for review.

---

## 0a. Open when work resumes (3 September)

1. **Read Chapter 2 end to end** now that all thirteen comments are resolved and §2.6 is gone, before starting Chapter 3.
2. **Improve the consistency checker** (`tools/check.py`). Moritz asked for time on this specifically. The brief: every miss so far has been an edit in one place silently invalidating a claim in another, which a chapter-by-chapter read cannot catch. See §10 item 18 (proposed) and the miss log.
3. The two stale `overleaf-*` branches to delete once Overleaf has pulled `main`.
4. **When Chapter 8 closes**, work the forward-dependency table in §0 before anything else. Two of the four items are known-wrong today and are waiting on it.

*Closed 2 September:* Methodology §2.6 "Expected Results" was cut (PR #19). Its evaluation-evidence paragraph moved to Ch. 1 §1.4 Contributions; Ch. 9 §9.7 now cross-references Ch. 1 §1.4.

---

## 1. Decisions taken in this session

### 1.1 The dependency seam — resolved by qualifying the front, not the back
The front of the thesis (RQ1, RQ2, the Related Work gap statement) promises understanding of *course dependencies*; Chapters 8–9 report that the evaluated graph rendered containment plus **two** formal prerequisite pairs. The gap is not in the tool. Two facts settle it and both must be stated the same way everywhere:

1. **The evaluated graph did render the hard (formal) prerequisite relation**, as a togglable overlay across the exam-subject bands. What it did not render is the **soft (recommended)** orderings the compliance engine holds as non-blocking advisories.
2. **The soft-dependency edge layer was built after the evaluation study**, in response to participant feedback (E-P44). No finding in Chapter 8 concerns it, and every mention of it must say so.
3. The reason the overlay is thin is the **curricula**, not the design: outside StEOP and within-module ordering, the two TU Wien curricula publish almost no sequencing.

**Edits that follow** (to be made when we reach each chapter, kept close to the proposal's wording):
- **RQ1 / RQ2 (Ch. 1) — done in Pass 0.** The RQ sentences are untouched. One sentence after RQ1's explanatory paragraph bounds the term: *course dependencies* means an ordering relation a curriculum encodes, in the two glossary forms, and how much of either the two programmes carry is itself a finding.
- **RQ3 stays interface-only — Moritz's decision, 2026-09-02.** "and its embedded recommendations" is deliberately *not* in RQ3. Naming recommendations in the question would presuppose a second component before the formative study had decided one was wanted; the hybrid graph-table concept is the only component this thesis assumes, and that assumption is declared in Ch. 2. Had the formative study found recommendations unwelcome, an RQ naming them would have been wrong. Ch. 8 and Ch. 9 were aligned to Ch. 1 rather than the reverse, and Ch. 8 now says explicitly that the recommendation panel is one component of the interface under test rather than a separate object of the question.
- **Ch. 3 Positioning:** replace "a browsable, dependency-revealing graph" with a formulation that names what is revealed: a browsable curriculum graph that renders programme structure together with the curriculum's formal prerequisites. Same claim, no over-promise.
- **Glossary — done in Pass 0, simplified on Moritz's instruction.** Two terms, and the split is by *what the curriculum fixes* rather than by hard/soft within one word. **Dependency** = the structure a curriculum itself fixes: its containment hierarchy together with the hard constraints published alongside it. That is exactly what the evaluated Graph View drew. **Soft dependency** = a recommended ordering, curated for this tool rather than published, advisory in the compliance engine throughout the study, drawn in no view until the edge layer built afterwards. **A bare "dependency" never includes the soft form.** `Containment` keeps its own entry as one half of the first term.
- **The sweep was run as a first pass on 2026-09-02** and its result is recorded as a note in each file, so no chapter starts by re-reading all of them. 58 prose occurrences across nine files.
- **The only occurrences that had to change immediately are the post-study ones**, because there a bare "dependency" would silently exclude the soft form the edge layer added. Both were corrected: Ch. 7 §7.8.2 and Ch. 9 §9.8 now read "a view drawing dependencies and soft dependencies together" instead of "a dependency-revealing view". Everywhere else the word already reads correctly under the new definition and is re-confirmed during that chapter's own pass, item 15 of the definition of done.
- **Two flagged for their chapter's pass:** Related Work's "broad, multi-layered structural dependencies", which is this thesis's own argument and is what Ch. 8–9 report these curricula do not have; and Implementation's two non-course uses ("Dependencies point downward only" is the software-module sense; "focus-area dependency matrix" is a gate). One must never be touched: questionnaire item 2 in the evaluation appendix is the instrument as administered.

### 1.1a Scope, assumption, limitation — where the line runs
Asked by Moritz on 2026-09-02, and worth keeping because the three are easy to conflate.

| | Question it answers | What breaks if it is wrong |
|---|---|---|
| **Scope** | what did we choose not to cover? | nothing — coverage is narrower, conclusions stay true |
| **Assumption** | what did we take as true without testing it? | conclusions *inside* scope become wrong |
| **Limitation** | what follows from how we worked? | nothing new — it bounds how far findings travel |

The test is **can the thesis be wrong because of it?** If yes it is an assumption; if it is merely not covered it is scope; if it is a residue of how the work was done it is a limitation. One item may appear twice but never as the same sentence: the *choice* goes under Scope, the *consequence* under Limitations.

### 1.2 Length — polish, do not restructure
`REVIEW.md`'s shortening plan is **wrong on its headline item**: Chapter 5 already carries only the summary table, and the full feature specs already live in Appendix A.3. Corrected position:

- **Main matter is 110 pages. That is a normal, defensible master's-thesis length. No structural cuts.**
- The only chapter worth trimming on length grounds is **Design (28 pp)**, and only where a "rejected alternative" was never a live alternative — cut those to one sentence, keep the four genuinely weighed ones in full. Expected saving 4–6 pp. This is a by-product of the Design pass, not a goal.
- **Additions are expected to outweigh cuts**: Ch. 4 findings section (§1.4), abstract, Kurzfassung, acknowledgements, AI-tools disclosure. Budget for ~190 pp at submission and stop worrying about it.

### 1.3 Working mode — branch + PR, one chapter at a time

**Never push to `main` directly.** Every change goes on a branch and into a pull request, and what it does is explained in the chat before it is opened. This holds even for merge resolutions and for changes that look purely mechanical — Moritz reviews in GitHub and pulls into Overleaf from `main`, so an unannounced commit on `main` arrives in his editor without him having seen it. Set 2026-09-02 after two direct pushes.
**A merged branch is closed, and `tools/push.sh` now enforces it.** Push with `GH_TOKEN=... tools/push.sh`, never with a bare `git push`: it asks GitHub whether a PR for this branch has been merged and refuses if commits sit past the merge point. Written 2026-09-03 after the rule below failed three times in one day. The naive test, whether the branch tip is an ancestor of `main`, does not work, because after the merge the branch grows past the merged commit and looks live again.

**A merged branch is closed.** Once its PR is merged, never commit to that branch again: the commits sit on a merged head, no PR is watching them, and they silently never reach `main`. Any further work starts with `git checkout -b <new> origin/main`. Set 2026-09-02, after two commits were pushed to the #19 branch after #19 had been merged and had to be recovered as #20.

A fine-grained PAT scoped to `Diploma_Thesis` (Contents read/write, Pull requests read/write) is provided; rotate it after submission. Never pass it to `git push -u`, which writes it into `.git/config`. Loop per chapter:

1. Pull `main`. Re-read the chapter end to end, not the diff.
2. Post the chapter's finding list here first (defects, inconsistencies, citations to verify) and agree what changes.
3. Branch `polish/chNN-<name>`, commit in small, described steps, open a PR against `main`.
4. You review inline in GitHub; I address every comment with a new commit and reply, then mark resolved.
5. Merge, update §12 status table, and you pull into Overleaf.

Never extend a branch whose PR has already merged — check merge status via the API first. Brace-balance every edited file immediately after editing (`content.count('{') == content.count('}')`), and run §11's check script before opening the PR.

### 1.4 Chapter 4 gets a Findings section
Chapter 4 currently ends at analysis method, and Chapter 5 opens from "the final theme set" the reader has never seen. This is the first thing a TA-literate examiner asks about. Add a **Findings** section before "Output Artefacts and Traceability", presenting the 64 themes grouped into a small number of need areas, each with prevalence and two or three verbatim excerpts, closing with the disposition (51 / 11 / 2). The material already exists in Appendix A.2 — the section synthesises it, it does not duplicate the table.

---

## 2. The standing rule: verify, do not assume

This is the rule the whole pass is built on, and it is stated first because nearly every serious defect found in this project so far came from checking something rather than from reading it.

**Every reference, at the moment it appears in the text.** When a `\cite{}` comes up during a chapter pass:

1. Confirm the key exists in `bibliography.bib` and that the entry's type, author, year, venue and page range are correct.
2. **Open the source** (`context/related-work/` holds most PDFs) and confirm the sentence in the thesis says what that source actually says — not what the citation key suggests, not a remembered gist, and never the abstract alone.
3. If the source does not support the claim: either reword the claim to what the source supports, or drop the citation. Never leave a plausible-sounding attribution standing.
4. Record the verdict in §14's citation log, with the page or section that carries the claim. A reference verified once is not re-verified.

This has already caught real misattributions here (`esteban_helping_2020` for prerequisite relationships; Ma et al. 2021 for ease-of-use; Bodily & Verbert articles-vs-systems; Braun & Clarke page anchors and phase names; Wong cited as a standard technique when it is a doctoral-consortium proposal). Assume more remain.

**When a source cannot be obtained.** An unopened source may **not** carry a direct quotation, a specific number, or a finding attributed to that study. It **may** stand as a conventional attribution for an established concept a reader could confirm from any textbook in the field. Every such case is recorded in §14's log as a deliberate decision, with the reason, so that it reads as a judgement made rather than a check skipped. If neither applies, the sentence is reworded to what an available source supports, or the claim goes.

**Every factual claim about the tool** is checked against **`main` of `hypridplanner`** (Moritz, 2026-09-04; this replaces the earlier rule naming an evaluated tag, whose name nobody has verified exists). The check is against the code, not against any document about the code.

One thing this rule cannot do on its own: `main` is the tool as it stands now, while Chapters 6 to 8 describe the tool participants used. Where the two differ, the difference belongs in §7.8 (Revisions After the Evaluation Study), which must say the change was not in front of a participant. So a claim that checks out against `main` still has to be asked one further question: was it true during the sessions? The session dates in Chapter 8 bound the code that was running.

**Every number** traces to one artefact (§9).

**Every cross-reference** must resolve *and* resolve to the thing meant. A `\ref` to a label that exists but was renamed under you passes the automated check and is still wrong.

---

## 3. Language and register

**English variety: British.** `programme` (degree programme) never `program`; `-ise/-isation` (visualisation, personalisation, prioritisation, organised, recognised, anonymised, synthesises); `colour`, `behaviour`, `catalogue`, `judgement`, `labelled`, `modelling`, `analyse`, `favour`. Current state is clean apart from three `color` inside TikZ (correct, they are commands) — keep it that way. When sweeping, exclude LaTeX commands (`\itemize`, `\scriptsize`, `\normalsize`, `\definecolor`) from `-ize`/`color` searches.

**Scientific register.** No slang or phrasal-verb casualness: *figure out* → determine/identify; *kind of X* → a type of X, or cut; *a thing* → a concrete noun; also avoid *get around, end up, come up with, deal with, turn out, a lot of, pretty much, basically*. Four `kind of` remain (design ×2, evaluation ×2) — two are inside participant quotations and stay verbatim; the other two go.

**Scientific register — the specific checks.** `tools/check.py` scans for all of these; the judgement calls after them are yours.

| Reject | Because | Instead |
|---|---|---|
| *actually, really, quite, obviously, simply, truly, indeed* | rhetorical emphasis doing no analytical work | delete |
| *very, extremely, highly* | unmeasured degree | give the degree, or delete |
| *a number of, numerous, a variety of* | the thesis usually knows the number | give the number |
| *figure out, come up with, deal with, end up, turn out, get around, leave it to* | conversational | determine, formulate, address, result in, prove to be, avoid, delegate to |
| *proves, demonstrates that, confirms that* | stronger than any design here supports | establishes / indicates / is consistent with |
| *it is worth noting, it should be noted, needless to say* | says nothing | delete and state the point |
| *the tool knows / wants / decides* | anthropomorphism | the engine reports / the rule blocks |
| *we believe, we feel, we think* | stance without an argument | we argue (with the argument), or state the claim |
| *I, my, me* | the thesis uses "we" for research acts | we |
| an em dash (—) | not house punctuation, in the thesis or in anything drafted in chat | a comma, or restructure |
| *study 1, study 2, the needfinding study, the user study* | the two studies have fixed names | the formative study / the evaluation study |

Two further rules that no scanner can check. **A claim verb must match the evidence:** *establishes* only where the design supports the inference, *suggests* or *indicates* for an exploratory pattern, and any finding sentence names its source (a code, a table, a section). And **no rhetorical questions** in prose — a question in the thesis's own voice is either a research question or a sentence that should have been a statement.

**No vague summary-hedges.** "leaves a clear gap" → name the gap; "in spirit closest to X" → "most closely aligned with X"; "a large and varied field" → "a substantial and heterogeneous field". Avoid loose intensifiers (*really, very, themselves*).

**No self-flattering comparison — the "rather than" rule.** Do not write a sentence whose comparative half exists only to make this thesis's choice look better than an alternative nobody proposed. The forms are *X rather than Y*, *not Y but X*, *X instead of Y*, *X as opposed to Y*. The construction is banned whenever Y is an inferior option the thesis did not take and does not otherwise discuss: Y is then a foil, and the sentence is persuading rather than reporting. State what was done and let the reader judge it.

*The test.* Cover the comparative half. If the sentence still carries every fact the reader needs, the half was decoration — cut it. It stays only if removing it loses information, **and** Y is one of:

1. **A source's own contrast**, reported as that source's claim. "Munzner asks that assumptions be stated rather than left implicit."
2. **A limitation**, where the unchosen half is the *stronger* option this thesis did not reach. "The evidence is inferential, drawn from adjacent systems rather than from research that tests hybrid interfaces against alternatives." Here the comparison costs us something, so it is not flattery.
3. **A precise category distinction** the reader needs both halves of, where both terms are real and neither is a strawman. "descriptive rather than causal"; "perceived rather than actual completion"; "decision support rather than decision automation".

*Banned, with the fix.* "rest on two records rather than on self-report alone" → name the two records. "treats that as an empirical question rather than a design assumption" → say what was asked and of whom. The tell is that Y describes a weaker way of doing our own work that no one in the thesis is doing.

*Density.* Even where every use is allowed, they should not stack: three in four sentences reads as a tic regardless of whether each is defensible on its own. This was a `tools/check.py` warning until 2026-09-03, flagging any paragraph with two or more. It was removed on Moritz's call, because the only paragraph still firing held two of the cited authors' own contrasts, and a check that fires forever on text already judged fine teaches everyone to skim warnings. Density is now a judgement made during the read, like the per-sentence test above.

**No meta-discourse.** Delete sentences that describe the writing rather than say something. Known sites: `design.tex` §6.2 opening and §6.11 opening; `evaluation.tex` §8.1 sentence 2 and §8.2 sentence 3; `methodology.tex` chapter opening; `fromthemestorequirements.tex` opening (keep the RQ1-completion sentence). A chapter's structure is visible from its headings.

**Voice: `we` for research acts, "this thesis" for the document.** Both are already in use (42 vs 50) and both are correct — the rule is *which* is used where, not which one wins. `we` when the sentence describes something the researcher did ("we sampled every recording", "we do not interpret the small differences"). "This thesis" when the sentence describes the document or its scope ("this thesis covers two programmes"). Never "the author" in running prose, and never "I".

**Tense.** Present for the document and for the state of the art ("Section 8.3 reports…", "Hirmer et al. frame study planning as…"). Simple past for what was done and what happened ("six students were interviewed", "P02 planned against 102 ECTS"). **Never future tense for the document**: "Section X reports", never "will report". Ten `will` remain; each must be either a genuine future (future work, a participant quotation) or rewritten.

**Sentence economy.** Long sentences are permitted where the qualification is load-bearing, which is often here. They are not permitted where they hedge a claim that could be stated directly. The clusters worth shortening are `design.tex`'s alternatives paragraphs and `methodology.tex` §2.1's second half.

**No one-sentence paragraphs** and no result spoilers in setup sections (the Evaluation brief, already applied there, extends to every chapter).

---

## 4. Punctuation, emphasis and quotation

| Rule | Form |
|---|---|
| Em dash | **Never in prose.** Use a comma or restructure. Three remain in `design.tex` — remove. |
| En dash `--` | Numeric and page ranges only (`pp.~227--228`, `Chapters~\ref{a}--\ref{b}`, `C1--C64`, `OOS1--OOS4`). Not as a parenthetical dash. |
| Bold `\textbf{}` | **Only** as the label opening a bullet or `\item`, as an RQ label (`\textbf{Research Question~1}`), and in table headers. Never for emphasis in running prose. |
| Italic `\emph{}` | A term's first introduction; the label opening a rejected-alternative sentence; a genuine single-word contrast (*what* vs *how*). Not for routine repeated terms and not for whole clauses. 198 uses, 121 of them in Design — that chapter needs a thinning pass. |
| Quotation marks | **`\enquote{}` everywhere.** `csquotes` is loaded. |
| Participant quotations | See below — this is currently the largest single inconsistency in the thesis. |
| Oxford comma | Used consistently. Keep. |
| Page anchors in citations | **For direct quotations and close paraphrase of a specific passage only**, as `\cite[p.~10]{key}`. Not for a citation that supports a claim in general. This is why Chapter 4 carries ten and most chapters carry none: it is the only section that quotes and paraphrases a single book closely. Settled 2026-09-03; the alternative, dropping them, would make three verbatim quotations unlocatable in a 300-page book. |

**Participant quotations — settled 2026-09-02, `\enquote{}` with no italics.** This is the standard form, not merely the cheaper sweep: `csquotes` exists for exactly this and handles nesting and language-sensitive marks, and academic style (Chicago, APA) sets short quotations in quotation marks without italics, reserving italics for emphasis and titles. 161 instances of the `` ``…'' `` forms were converted in Pass 0; none remain. Attribution follows the closing quote as `(C21)` for formative themes and `(P09)` for evaluation participants. Quotations longer than about forty words take a `quote` environment without quotation marks — the longest quotation in the thesis is currently 154 characters, so none does.

**Translations must be declared.** Both studies were conducted in German. Chapter 4 §4.5.1 and Chapter 8 §8.1.6 each carry one sentence saying the quoted excerpts are the author's translations and the German originals are held with the transcripts. Check that sentence exists in both before either chapter is closed, because without it the word "verbatim" is claimed and not delivered.

---

## 5. Terminology and abbreviations

**Fixed names.** Use exactly these, capitalised as shown, everywhere: Table View, Graph View, Parking Stage, Dashboard, Recommendation Panel, Compliance Engine, Semester Picker, Course Catalogue. The artefact is *the tool* or *the study planner*; the instrument is *the study-guide application* (the questionnaire web app). The two studies are **the formative study** and **the evaluation study** — never "study 1 / study 2".

**Themes are T1--T64, codes are unlabelled.** Renamed from C1--C64 on 2026-09-04, because "C" read as *code* while the identifiers name *themes*, which is the level above codes. The rename touched 392 occurrences in five files (codebook appendix 242, `design.tex` 68, `fromthemestorequirements.tex` 51, `needfindingwithprototype.tex` 30, glossary 1). The 435 initial codes have no identifiers and are never cited individually; only themes are. One deliberate exception exists and must stay: `design.tex` has a generic TikZ figure with a node labelled "Module C1", which is not a theme. `tools/check.py` fails the build on any other bare `C<number>`.

**The codebook appendix is generated, not written.** `appendix/theme-codebook-table.tex` is built by `tools/build_codebook.py` from three inputs: the open-coding document (`context/interviews-round1/First Open Coding.docx`, the source of the 64 themes and their 437 German excerpts), `tools/codebook_themes.json` (label, `n`, disposition per theme, extracted once from the table it replaced), and `tools/codebook_translations.json` (the 437 English translations, written by hand). Never edit the `.tex`; edit an input and rebuild. `tools/check.py` fails if the file is out of date, and fails if any quotation attributed to a theme anywhere in the thesis is missing from it, so a quote and its source cannot drift apart. Two quotations currently sit in an exceptions list in that check because they match nothing in either study's data (§13).

**The OOS labels are document-wide, not a Chapter 2 local.** OOS1 to OOS5 are defined once, in Chapter 2 §2.3, and then used as bare labels in five other places: Chapter 4 (naming which OOS item excluded which theme), Chapter 5 §5.1 (restating OOS3 and OOS4 with the evidence that justifies them), Chapter 6 §6.1 (treating them as settled inputs to design), the codebook appendix, and the glossary. Adding, removing or renumbering one is therefore an edit to six files. What breaks is never the definition; it is the **counts and ranges** elsewhere: "all four boundaries", "OOS1--OOS4", and any sentence claiming where a given item is stated.

Broken twice already by the same change. Adding OOS5 on 2026-09-02 left Chapter 5 saying "all four boundaries" (fixed then), and left `design.tex` §6.1 saying "all four OOS boundaries" and the glossary saying "one of the four system-wide scope boundaries (OOS1--OOS4)" with a stale account of where each item lives (both fixed 2026-09-03, found only because Moritz asked for this note). `tools/check.py` now derives the count from the definitions in `methodology.tex` and fails on any range or spelled count that disagrees, so the third time is caught by the build.

**Every abbreviation is expanded at its first use in reading order across the whole document, then used bare.** *Reading order*, not first use in the chapter being edited: that distinction is what this rule kept getting wrong. `tools/check.py` now enforces it, walking the chapters in the order `main.tex` inputs them and requiring each abbreviation's expansion to appear at or before its first bare occurrence. Previously broken, all now fixed:

| Abbreviation | Status | Action |
|---|---|---|
| ECTS | 124 uses; expanded 2026-09-04 at its **first use in reading order**, which is Ch. 4 §4.2, not Ch. 2 as this row previously said. Glossary entry exists and is linked there | done |
| StEOP | 8 uses, **never expanded** | Expand once (Studieneingangs- und Orientierungsphase) at first use in Ch. 6 or 7, add to glossary |
| TAM | 6 uses, expanded once in Ch. 2 but **not in Ch. 8 where it is introduced as an instrument** | Expand at first use in Ch. 8 |
| UEQ, ED, ERS, TA, OOS, CMS/LMS, GDPR | expanded correctly | keep |
| VU / VO / UE / PR | used, covered by the glossary's Course entry | keep |

**Glossary terms are hyperlinked at their first occurrence in the thesis, and only there.** Settled 2026-09-02 on Moritz's instruction. Every entry in `appendix/glossary.tex` carries a `\phantomsection\label{gls:<slug>}` anchor (26 of them), and `\gterm{<slug>}{<display text>}` links to it: `\gterm{dependency}{course dependencies}`. This is a house convention, so it applies to every chapter, not only the one where it was introduced — a chapter is not done until its first mentions of glossary terms are linked. Done so far: Ch. 1 (`dependency`). Not linking a term more than once is deliberate; a link on every occurrence turns running prose into a field of boxes.

**Acronym list and index are currently empty pages.** `main.tex` loads `glossaries[acronym,toc]` and calls `\printindex` and `\printglossaries`, but the thesis contains no `\newacronym`, no `\gls`, and no `\index{}`. Decide once: either populate a real acronym list with `\newacronym` for the table above, or comment out `\printindex` and `\printglossaries` and keep the hand-written Appendix glossary as the only glossary. **Recommended: comment out both**, keep the Appendix glossary, add the four missing entries. An empty index in a submitted thesis reads as an unfinished build.

**A repeated thesis-specific proper noun needs a glossary entry.** The Appendix glossary is thesis content and is held to every rule in this file. Missing entries to add: **Dependency** (§1.1), **ECTS**, **StEOP**, **Scenario A / Scenario B**.

---

## 6. Structure

**Chapter order is settled** and Methodology deliberately precedes Related Work, because Related Work is stage 1 of the process Methodology describes: Introduction → Methodology → Related Work → Formative Study → From Themes to Requirements → Design → Implementation → Evaluation → Discussion.

**Chapter openings use one pattern.** Chapter 4's opening is the template: what the chapter does, then the research question it contributes to, quoted, then what the chapter's output is and where it goes next. Apply the same shape to every chapter that names an RQ (currently Ch. 1, 4, 6, 7, 8, 9 all do it differently). **The RQ text quoted in a chapter must be character-identical to the RQ text in Chapter 1.** Two mismatches exist today:

- RQ1 in Ch. 1 says "curriculum structure and course dependencies"; the block quote in Ch. 4 says only "course dependencies".
- RQ3 in Ch. 1 omits "and its embedded recommendations"; Ch. 8 and Ch. 9 include it (following the proposal). **Fix by restoring the proposal's wording in Ch. 1**, since the proposal is the fixed point.

**Each chapter hands the next what it needs, and says so.** This holds from Ch. 4 to Ch. 9 today; do not break it. A chapter may not silently assume something its predecessor never delivered.

**Answers to the research questions live in Ch. 9 §9.1**, which now exists. Every RQ must be answerable by pointing at one place — RQ1 at the specification, RQ2 at the artefact and its recorded reasoning, RQ3 at the three ISO dimensions. Keep RQ1 and RQ2 named in that section; they were previously absent from the Discussion entirely.

**Scope is stated once, where it is credible.** OOS1/OOS2 (general) in Ch. 2 §2.3; OOS3/OOS4 (evidence-dependent) in Ch. 5 §5.2 beside the excluded findings that justify them. Do not restate either set in the other chapter.

**The traceability chain has exactly one wording**, used identically in Ch. 2, Ch. 4 and Ch. 5:

> Literature Review → Formative Interviews → Codes → Themes → Requirements → Features → Design → Implementation → Evaluation

Requirements precede Features — that is the derivation order (Ch. 5 states it). This has been reversed twice before; check this pair specifically before any edit near it. The chain is explicitly the artefact-level realisation of Munzner's nested model, not a second framework: domain characterisation = Literature Review..Themes; abstraction = Requirements + Features; encoding/interaction = Design; algorithm = Implementation; Evaluation validates across levels. Evidence is cited at the **code** level (`C21`), not by theme label.

**Forward references: present tense, sparing, and only where the reader needs to know a section exists** — not where the current sentence is unintelligible without reading ahead.

**Restructuring discipline.** If a section is split, merged or renamed, grep the *whole thesis* for the old label before calling it done, and diff-check that nothing was silently dropped — LaTeX will not complain about a missing section, only about a missing label.

---

## 7. Figures and tables

- **Every float is referenced by name in the prose that motivates it**, at the sentence describing what it shows. Currently unreferenced: `fig:nested-model-mapping-alt`, `tab:app-codebook-problems`, `tab:app-codebook-positives`, `tab:app-codebook-neutral`, `tab:app-unmet`, `tab:app-interview`, `tab:interview-structure`. Either reference each or remove it. `methodology-figure-nested.tex` appears to be an unused alternative rendering — decide and delete one.
- **Figure captions: 100–200 characters.** State what the figure shows and the one or two facts needed to interpret it. Not a re-explanation of the prose. Currently out of range: `fig:state-machine` (94), `fig:three-panels` (207), `fig:curriculum-hierarchy` (215), `fig:workflow` (202), `fig:impl-architecture` (314), `fig:impl-edit-flow` (227), `fig:impl-backend-components` (207), `fig:eval-loop` (216), both methodology figures (253, 264).
- **Table captions may run to ~350 characters**, because a table caption legitimately carries how to read the denominators, what a tick means, and which values are descriptive. This is a deliberate relaxation of the old single rule, which no table in the thesis obeys. Cap at 350; `tab:problems` (441) is the one genuine over-runner.
- **Caption placement:** below figures, above tables. Consistent today — keep.
- **TikZ figure text is black**, except deliberately greyed annotation. Three of your `%% REV` comments ask for exactly this (`fig:status-encoding`, `fig:card-text`, `fig:rec-panel`) and are still open.
- **No duplicate figures after restructuring.** Appendix C.5's process-state model duplicates Table 8.2 — drop one.
- **Screenshots:** nine PNGs in `pictures/` are unused. Either bring them in where the prose needs them or delete them from the repo. `\todo{update graph screenshot}` in Ch. 7 is open.
- **Overfull boxes:** 30 remain. Fix the ones over ~10 pt (they visibly bleed into the margin); ignore the sub-5 pt ones.

---

## 8. Methodological rigour

**Separate what the study establishes from what it suggests.** Ch. 9 does this well and the vocabulary is now fixed: *establishes* for a claim the design supports; *suggests* / *exploratory pattern* for a hypothesis the design generates. Anything resting on fewer than roughly three participants, or on a contrast the fixed scenario order confounds, is exploratory and must be labelled at the point of the claim, not only in the Limitations list.

**State the bound where the claim is made.** Three bounds recur and each has a fixed formulation:
- *Order confound:* graph availability is perfectly collinear with second exposure and with the change of persona topic. Only the **substitution** result survives it. The placement-rate result is reported as a description of the second run.
- *Construct substitution:* self-report measures felt completion, not actual; the frame record measures which panels were configured, not where attention was.
- *External validity:* one institution, two programmes, 6 and 11 participants.

**Frequencies are always `n/m` with the denominator explained.** `m` is the number of participants for whom the code could be decided. `9/9` means every session in which the question arose, not nine of eleven. Never report a bare count where a denominator exists.

**Feature and requirement citation format.** From Chapter 6 onward: `Feature~\ref{feat:004}, Req.~1`. The bare string `FEATURE-004` is correct **only** inside Chapter 5 and Appendix A, where it is the feature's own heading text. Current state is compliant (106 bare uses, all in Ch. 5 and Appendix A) — keep it that way.

**A missing "alternatives considered" paragraph is not a defect.** Record an alternative only where one was genuinely weighed. Never invent a plausible rejected alternative to fill a template — that is a false claim about the design process.

**Deviations from the proposal are defended where they arise, not gathered** (Moritz, 2026-09-02). OOS5 covers the recommender in Ch. 2 §2.3, the fixed order is defended in Ch. 8 §8.1.2, and the RQ scope is settled in Ch. 1. A single collecting paragraph was considered and rejected. Superseded guidance, kept for the record: the proposal (Jan 2026) promised four sub-questions including a recommender learned from students' interaction data (SQ2) and its integration (SQ3), and a counterbalanced within-subjects design against a spreadsheet/paper baseline. The thesis delivers three RQs, a recommender over synthetic prior-student data with quality explicitly out of scope, and an uncounterbalanced graph-off/graph-on design. Each of these is defensible and each is defended somewhere in the text — but they are defended in scattered places. **Add one short paragraph, in Ch. 2, stating how the executed design differs from the proposal and why.** An examiner reading both will look for it.

---

## 9. Numbers and data integrity

**One artefact per number, one number per fact.** Every figure in Ch. 8 and Ch. 9 traces to the evaluation study's `analysis/` folder — the frozen stage-log parser output, `findings-matrix.csv`, `completion-audit.md`, `process-metrics.md`, and the Raw-JSON column of `US Results.xlsx`. When a number changes, regenerate the whole dependent set (chapter table, prose, appendix, discussion) from the same run rather than patching the instance you noticed.

- The frame total is **2,179** and it must sum from Table 8.2's own rows (1,197 + 982). It does today. Any reparse that changes it changes Table 8.2, the loop shares, the appendix labelling-scheme section, and Ch. 9's parenthetical.
- UEQ values use the **population-SD** convention and the **questionnaire app's own item order**, which differs from the standard UEQ order; the spreadsheet's eight UEQ columns are lossy. Anyone recomputing from those columns gets wrong numbers — say so in the appendix if it is not already there.
- Percentages: `\,\%` throughout (58 uses, consistent — keep).
- ECTS: **`~ECTS` with a non-breaking space**, e.g. `30~ECTS`. Currently 25 of 33 comply; eight use a plain space. Sweep.
- Cross-reference words take a non-breaking space: `Section~`, `Chapter~`, `Figure~`, `Table~`, `Feature~`, `Req.~`. Compliant today except a handful of `Table ` instances (all of which are the panel name "Table View", not references — do not "fix" those).
- Spell out numbers under ten in prose ("six participants"), use digits from ten up and for measurements and identifiers. Swept 2026-09-04: the specification is **13 features carrying 55 numbered requirements** in all five places that state it (Ch. 1, Ch. 5 twice, Ch. 9, both appendix intros); "eleven analysed" stays spelled out because it is the participant count, which §0 fixes in words.

---

## 10. Definition of done, per chapter

A chapter is finished only when every line below is true. This is the checklist to run before opening the PR.

1. Read end to end in one sitting, not as a diff.
2. Every `\cite` in the chapter verified against the opened source and logged in §14.
3. Every claim about the tool checked against `main` of `hypridplanner`, and anything that changed since the evaluation recorded in §7.8.
4. Every number checked against its source artefact and against the register in §0.
5. Every `\ref` resolves *and* points at the intended target; every figure and table is referenced in prose.
6. British spelling sweep; register sweep; no em dashes; no bold outside item labels; `\enquote{}` only; `\emph{}` thinned.
7. Every abbreviation expanded at first use in this chapter.
8. Figure captions 100–200 chars, table captions ≤350; caption placement correct.
9. RQ text, if quoted, character-identical to Chapter 1.
10. Terminology matches §5; the two studies named descriptively.
11. Frequencies carry denominators; exploratory claims labelled.
12. Brace balance verified; the full build runs clean (§11); no new overfull box over 10 pt.
13. All `%% REV`, `%% AIREV` and `\todo{}` markers in the chapter resolved and removed.
14. §12 status table updated.
16. Glossary terms hyperlinked with `\gterm` at their first occurrence in the thesis (§5).
17. Scientific-register table in §3 applied, and every claim verb checked against the strength of the evidence behind it.
18. **No rhetorical build-up.** A sentence whose only work is to announce that something notable follows is not a statement, and an examiner reads it as padding. Delete it and let the next sentence carry the point. The test is mechanical: cover the sentence, and if no fact is lost, it was build-up. Known forms, one of them written by me in Chapter 3 on 2026-09-03 and caught by Moritz: *One system has attracted sustained attention.* · *It is worth noting that…* · *Interestingly,…* · *This raises an important question.* · *A closer look reveals…* · *Notably,…* used as a paragraph opener. The related trap is the comparative lead-in that exists to flatter the thesis, which §3's "rather than" rule covers separately.

**Every chapter opens with its full open-items list, before any work on it.** Set 2026-09-03 at Moritz's instruction, after Chapter 3's audit findings sat in a queue he had not agreed to and only surfaced when he asked, three chapters later. The rule has two halves.

*At the start of a chapter*, survey it and put the complete list in front of him: every note by severity, every unverified citation, every number that disagrees with §0 or with its source artefact, every checker warning, and everything the chapter needs from him. Then start work. He decides what is deferred; that decision is not mine to make by filing something under a heading.

*At the end of a chapter*, nothing may be described as done while a check I ran has open findings. If something should be deferred it is deferred **by his decision, in writing**, and it stays visible as a `\TDrev` in the chapter. "Done with a queue attached" is not done.

**A note that has been dealt with is deleted, not marked done.** Set 2026-09-02. The thesis carries only outstanding work; a green "verified" block in the middle of a chapter is noise for the person reading it, and there were eleven of them. What was checked and what it showed goes in §14's log instead, which is where someone looks to avoid re-checking. The `\TDok` macro is retired.

The only note that may remain in a closed chapter is one **deferred by decision** — kept open on purpose, saying why and when it is revisited. Ch. 1's contributions note is the example: it waits on Ch. 8 and Ch. 9. Any other open note means the chapter is not done.

**Curriculum analytics is out of the thesis** (Moritz, 2026-09-02, **confirmed 2026-09-03**). It was in the proposal, but Related Work never covered it and it plays no part in either gap the thesis argues, so the Introduction no longer previews it. `archambault_curriculum_2015`, `buck-emden_analyse_2018` and `kapucu_competency-based_2017` were cut from `bibliography.bib` on 3 September, since an uncited entry left in the file is an invitation to re-add the topic by accident.
15. Every `dependenc*` occurrence in the chapter checked against the glossary mapping (§1.1).

---

## 11. Build and checks

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main && makeglossaries main && makeindex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Required TeX Live packages beyond a base install: `texlive-latex-extra`, `texlive-latex-recommended`, `texlive-fonts-recommended`, `lmodern`, `texlive-plain-generic`, `texlive-lang-german`, `texlive-bibtex-extra`, `texlive-pictures`, `texlive-science`.

Before every PR, run the repo check script (`tools/check.py`, to be committed): dangling and duplicate labels; unreferenced float labels; cite keys absent from the bib; bib entries never cited; American spellings excluding LaTeX commands; em dashes; `\textbf` outside item labels; `` `` `` vs `\enquote`; caption lengths; ECTS and percent spacing; unexpanded abbreviations; brace balance per file; `%% REV` / `\todo` inventory.

---

## 11a. Submission state — what must be removed

The review apparatus is designed to leave with one edit, and this is verified, not assumed: building with the toggle flipped gives **184 pages, no errors, and zero residue** (no "Review Annotations" page, no To-Do index, no coloured boxes, no severity words anywhere in the extracted text).

**`python3 tools/check.py --submission`** checks all of the following and fails on any of them.

1. **`main.tex`: `\reviewnotestrue` → `\reviewnotesfalse`.** This one line removes every `\TDblock` / `\TDmajor` / `\TDminor` / `\TDrev` / `\TDok` note, the "Review Annotations" chapter and its ToC entry, the generated To-Do index, and the explanatory paragraph. Nothing else in the document changes.
2. **No `%% REV` or `%% AIREV` comments left in any source file.** These are invisible in the PDF but are working notes and should not ship in the sources.
3. **`main.tex` metadata:** real title, subtitle (or removed), submission date, keywords. All four still print the template's placeholders today.
4. **No empty `formalities/` file.** Abstract, Kurzfassung, acknowledgements, Danksagung and both AI-tools disclosures are `\input` by `main.tex`, so an empty file renders as an empty headed page.
5. **No raw `\todo{}`** — all five have been converted; the check catches any reintroduced.
6. **Clean build:** no errors, no undefined references, no undefined citations.

Two things the check deliberately does *not* do. It does not delete the notes from the sources: `\reviewnotesfalse` is enough for the submitted PDF, and keeping them means the annotated version can be rebuilt afterwards. And it says nothing about `ANWEISUNGEN.md`, `CONTROL.md`, `REVIEW.md`, `tools/` or `context/` — none of them reaches the PDF. Whether they stay in the repository is a separate decision, and `context/` in particular holds the consent PDF flagged in §13.

---

## 12. Chapter status and order of work

Order is chosen so that the chapters whose content is still moving come after the ones that fix the vocabulary.

| # | Chapter | State | Main work |
|---|---|---|---|
| 1 | Introduction | **done 2026-09-03**, DoD run | All 7 review comments resolved (2 Sep). All 17 citations now opened against **this chapter's** sentences, not Ch. 3's: Morsy corrected (GPA correlation is explicitly weaker than TTD), Wong dropped (proposal, no results), Srisamutr moved to the table-based sentence (a GA scheduler, not a recommender), ED lead-in reworded (Schwendimann's corpus is 75 % teacher-facing), Rollande's dependency level narrowed. Two sentences realigned after the Ch. 3 fixes: the ED framing and the "in isolation" claim. **Decisions closed 3 Sep:** curriculum analytics stays out, and its three bib entries are cut. **One open `\TDrev`**, deferred by decision: contribution two's "explainable recommendations", waiting on Ch. 8. |
| 2 | Methodology | **done 2026-09-03**, DoD run | 13 review comments (2 Sep) plus 5 more (3 Sep) resolved. §2.6 Expected Results cut into Ch. 1. Munzner claim corrected twice: "anticipates" and then "validates" both overstate §4, which is post-hoc analysis. Assumption definition cut. Participant count restored to twelve run / eleven analysed. DoD: items 1 and 3 done by Moritz; 14, 16, 17, 18 and register done 3 Sep. **One open `\TDrev`**, deferred by decision: §2.5's "What a curriculum encodes", waiting on Ch. 8. |
| 3 | Related Work | **done 2026-09-03**, DoD run | All 46 sources opened and claim-checked (§14); 7 unsupported claims fixed, 7 bib defects found. All 18 of Moritz's REV comments closed. Chaturapruek moved to the ED half: Carta is a dashboard, not a recommender. Zero notes and zero REV comments remain. DoD: items 1 and 3 done by Moritz; 14, 16, 17, 18 and register done 3 Sep, including the Teasley duplication. **Open queue**: 4 majors from the audit, named so the count cannot go stale again (Arnold's four-input risk model; Hirmer filed as table-based though its prototype draws a dependency graph; Trippel's "most participants"; Siirtola's "unnecessary overlap"), the minors, and the 7 bib defects. |
| 4 | Formative Study | **done 2026-09-04**, DoD run twice | Two rounds of Moritz's REV comments closed (29 in total). Findings rewritten to lead with the five themes present in all six interviews. "Link to Subsequent Chapters" deleted outright; Ch. 5's reference repointed. Themes renamed T1--T64. Codebook appendix now reproduces all 437 excerpts, translated beside the German, and the chapter's claims about it rewritten to match. Second DoD pass 4 Sep found and fixed: Step 3 calling themes "codes", ECTS unexpanded at its thesis-first use, six glossary terms unlinked at their thesis-first occurrence, an unreferenced figure, one flattering "rather than", and the appendix contents described three times. Zero notes, zero REV comments. |
| 5 | From Themes to Requirements | **done 2026-09-04**, DoD run, comments closed | Opening rebuilt on Chapter 4's pattern with RQ1 quoted. All three sources opened and anchored (§14); the Nuseibeh claim that a theme is a "citable expression of a stakeholder need" was unsupported and now rests on what the paper says. Counts cross-checked against Appendix A.3: 13 features, 55 requirements, per-feature counts and the four unimplemented requirements agree; two defects found there and fixed (FEATURE-006's score, FEATURE-010's theme list). Then 14 review comments closed: §5.2 "Scope Refinement" deleted with its four references repointed at Chapter 4, the derivation paragraph and the sum-versus-mean paragraph shortened, the delineation claim corrected twice (not every feature has one; a delineation is not only an intentional exclusion), 13 and 55 as digits. Zero notes, zero REV comments, no checker warnings of its own. **Open, outside the chapter:** DoD item 3 is deferred to the end, when the tool is checked against `main` of `hypridplanner`; the claim that four requirements were not implemented is unchecked until then. |
| 6 | Design | largest pass | `\emph` thinning, quotation style, 3 open `%% REV` figure fixes, em dashes, never-live alternatives to one sentence, Wienand citations (§13) |
| 7 | Implementation | needs edit | 19 open `%% REV` incl. the data-model cardinalities, `\todo` on §7.4.1 length and the graph screenshot, post-study section shortened per your own note |
| 8 | Evaluation | near done | 4 open `%% REV`, opening-pattern alignment with Ch. 4, quotation style, Table 8.8 caption length |
| 9 | Discussion | near done | generalisability `\todo`, cross-check Table 9.1 against Appendix B.7 (now aligned) |
| — | Appendices | light | unreferenced tables, duplicate process-state figure, glossary additions |
| — | Abstract / Kurzfassung | **empty** | write last, from the finished chapters |
| — | Acknowledgements / Danksagung | **empty** | yours to write |
| — | AI-tools disclosure (EN + DE) | **empty** | draft from the git history; check TU Wien's current policy first |
| — | Pass 0 (cross-cutting) | **done 2026-09-02** | glossary vocabulary, RQ wording settled and propagated, Related Work gap reworded, 161 quotations converted, ECTS and StEOP expanded, empty index and acronym list removed |
| — | `main.tex` metadata | **placeholder** | title, subtitle, date, keywords — blocker, see §13 |

---

## 13. Open blockers and stale claims

**Blockers — these print in the submitted PDF as they stand.**

1. `main.tex`: `\thesistitle` is "Title of the Thesis", the subtitle is the template placeholder, `\setdate` is 01.01.2001, `\Keywords` is "a list of keywords". The proposal's title is a ready candidate: *Design and Evaluation of a Hybrid Graph–Table Interface with Embedded Recommender System for Study Planning* — though "Embedded Recommender System" now over-promises relative to what was built and evaluated, so it likely wants adjusting.
2. Abstract, Kurzfassung, Acknowledgements, Danksagung, and both AI-tools disclosure files are empty and are `\input` — they render as empty headed pages.
3. `\printindex` and `\printglossaries` render empty pages (§5).
4. Consent PDF with a real name and birthdate sits in `context/interviews-round2/` and in git history. Decide on removal and history rewrite before the repo is shown to anyone.
5. Storage location and retention period for raw recordings and transcripts are not stated in Ch. 2 and the outline template asks for both.

**Where `REVIEW.md` is now stale — do not re-apply these.**

- Its shortening plan item 1 (feature specs to appendix) is already done.
- Its frame-count finding (2,158 / 2,157 / 2,192) is resolved: the thesis is internally consistent at 2,179 and Table 8.2 sums to it.
- The webcam contradiction is fixed (Ch. 8 now scopes the claim to the four most recent sessions).
- The "defects have since been corrected, each with a regression test" sentence is scoped ("the first of them have been fixed"; Ch. 7 says five, with regression tests). Re-verify against the repo once, then close.
- Appendix B.7 is regenerated at N=11 and now agrees with Discussion Table 9.1.
- The Ch. 7 §7.4.1 broken sentence is complete.
- Codes-vs-themes is resolved: the appendix now calls T1–T64 themes, matching the chapters and the glossary (renamed from C1–C64 on 2026-09-04, §5).

**Two quotations in Chapter 6 had no source. Resolved 2026-09-04.** A second scan covering the six raw transcripts, the open-coding document, the generated codebook table, the translations file, the round-two notes and results, and the evaluation appendix settled both.

- \enquote{like a table, semesters in columns, courses in rows}, attributed to T18, **is the moderator's own speech.** The only occurrence of *Spalten* in any transcript is in I4, where Moritz describes the prototype: "Eine Tabelle, in dem man Items tracken kann. Tabelle, drei Spalten in dem Fall". It was reported as participants' visualisation of their ideal arrangement, under a theme (future-state preview) that has nothing to do with layout. 6.7 now rests on T47, \enquote{I simply find it easier with tables}, plus the prototype's unchallenged column arrangement.
- \enquote{the damage is done}, attributed to T20, **has no source anywhere**, in either language. It is no longer a quotation; the sentence states the point and cites T35 and T4, which are the themes that actually carry semester load.

`UNSOURCED` in `tools/check.py` is now empty and must stay empty: every quotation attributed to a theme has to appear in the codebook table, and the build fails otherwise. **Whenever a quotation is attributed to a participant, check that the speaker is the participant.**

**Parked, raised by Moritz, to be settled later.**

- **Section 6.9's design/implementation drift. Moritz's go given 2026-09-04, to be done at the very end and as its own MR so he can read the diff alone.** The supervisor's general remark about jumping between abstraction levels (`Design_SR.pdf` p. 1) had two halves. The Chapter 6 half is fixed: the data model is now declared as such in Section 6.1, and Section 6.12 no longer restates Section 7.5.3's scoring. The remaining half is Section 6.9, which describes what the rule engine returns and how each message is constructed — level-4 material by Munzner's own division, and the level this chapter says it is not working at. Move that to Chapter 7 and leave the design decisions behind: real-time rather than on-demand checking, hard blocking against soft advisory, and messages naming the course, semester and action rather than a category. Check first whether Chapter 7 already carries any of it, as it did for the recommendation families.
- **Transferable skills as a fourth obligation category (Section 6.10). Moritz, 2026-09-04: it is not to become a fourth obligation type; it is another pool of courses.** Section 6.1.5 fixes the interface encoding at three tiers (mandatory, constrained elective, fully elective), and the Dashboard's category level then lists "mandatory, constrained elective, fully elective, transferable skills" as obligation categories, which contradicts it. The sentence is left as it stands until the code check settles what the tool actually groups by; the fix is then to move transferable skills out of the obligation parenthesis, not to add a tier.
- **The Master programme's ECTS total is not in the Section 0 register.** Section 6.5.3 says "a fully expanded 120-ECTS Master programme contains well over 100 nodes". The register fixes the Bachelor at 180~ECTS and 101 courses but has no Master row, and no curriculum PDF is in the repo to verify either the 120 or the node count. Both come from the curriculum data in `hypridplanner`, so settle them in the code check and add the Master row to Section 0 then.

- **How many recommendation families the tool actually has, and what marks each one. Deferred to the code check, 2026-09-04, on Moritz's instruction; it survives until then and covers Chapters 6 and 7 together.** The thesis says six families in three places (Ch. 6 §6.12.1 lists six; §6.12.2 says the toggle bar shows or hides individual families; Ch. 7 §7.5.3 says six channels, four of which could fire during the study). Two things in the chapter do not agree with that six. Figure~6.12 draws **five** toggle chips, because the two peer-data families are merged into one chip labelled \emph{Other students} — which the supervisor counted, hence her note "evtl. nur die 5 Symbole" on p. 26 of `Design_SR.pdf`. And **four** of the six carry a symbol ($\star$, $\approx$, $\to$, $\triangleright$) while the two peer-data families carry none, although §6.12.2 says every card shows a badge naming its family. Moritz's reading is that there are six in general. Settle all three counts in one pass against `main` of `hypridplanner` (§2): how many families the recommender exposes, how many toggles the panel draws, and what badge each family renders. Then fix the figure, the two chapter texts and the badge claim together, and ask the second question §2 requires — whether the answer was the same during the evaluation sessions, since Ch. 7 already records that two families were inert then. Note that Ch. 7's `\TDminor` on this names `v1.0-evaluated`, a tag nobody has verified exists; that check is now against `main` plus the session dates.
- `appendix/glossary.tex` line 26, the *Soft dependency* entry: "they are mentioned, but are advisory". The entry defines a soft dependency as a recommended ordering; the open question is whether the thesis is consistent about what the system does with one. Deferred 2026-09-04 on Moritz's instruction; the `%% REV` comment stays in the file so the checker keeps counting it.

**Still open from that review and worth re-checking during the relevant chapter pass:** the E-G18 attribution to P06; the P10 "not placing from the graph at all" framing; the Wienand et al. citations (§14); whether the two inert recommendation channels were inert during the evaluation sessions, not merely in `main` today.

---

## 14. Material I still need from you

**Sources cited in the thesis with no PDF anywhere in the repo or project.** Until each is opened, its claim is unverified. Ranked by how much weight it carries. *Delivered 2026-09-02: Wienand et al. 2024 and Arnold & Pistilli 2012, both verified (§14). Shneiderman 1983 was committed but the file is a one-page browser print of the IEEE Xplore viewer, not the article.*

| Source | Where it carries weight | Why it matters |
|---|---|---|
| **Wienand et al. 2024** | Ch. 6 §6.2.4 (a direct quotation, "index card-like presentation") and §6.9 (three-level progress bars) | A quotation from an unopened source, in a different domain (enterprise-systems e-learning). Open access at doi 10.1007/s44217-024-00165-z |
| **Vessey 1991** (cognitive fit) | Ch. 9, load-bearing in the substitution interpretation | The theory the central design claim is read through |
| **Davis 1989** (TAM) | Ch. 8 instruments | The instrument's provenance |
| **Laugwitz et al. 2008** (UEQ) | Ch. 8 instruments | Same |
| **ISO 9241-210** | Ch. 5 (the human-centred design activities) | Optional. The catalogue page in `context/related-work/77520.html` carries the scope text those four activities come from. *ISO 9241-11 was on this list and is now verified — see the log.* |
| **Nielsen 1993** (*Usability Engineering*) | Ch. 8 severity ratings | The severity scale's source |
| **Saldaña 2013** (coding manual) | Ch. 4 analysis method | Method citation |
| ~~**Ware 2004**, **Palmer 1992**, **Shneiderman 1983**~~ | Ch. 6 encoding decisions | Settled 2026-09-04 (§14): Palmer and Shneiderman verified from the published abstracts and their sentences narrowed to what each states; Ware cut. |
| **Greenwald 1976** | Ch. 8 fixed-order rationale | Cited to justify not counterbalancing |
| **Arnold & Pistilli 2012**, **Caulfield 2013**, **Denley 2012** | Ch. 3 | The Course Signals retraction argument rests on two of these |

**Also needed:**
- The **GitHub PAT** (fine-grained, `Diploma_Thesis` only, Contents + Pull requests read/write) so I can open PRs.
- Confirmation that **interview round 2 is closed at 12 sessions / 11 analysed**. `CONTROL.md` still lists it as in progress with more interviews to come; every number in Ch. 8 and Ch. 9 assumes it is closed.
- The **thesis title, subtitle decision, submission date and keywords** for `main.tex`.
- Whether **TU Wien Informatics' current AI-use policy** has been checked with René or Selina, since it shapes the disclosure text.
- Access to the **evaluation study's `analysis/` folder** (stage logs, findings matrix, completion audit, `US Results.xlsx`) if you want any number re-derived rather than taken on trust — it lives on your Mac, not in this repo.

**Per-source disposition, set 2026-09-02.** Four were marked must-open; ISO 9241-11 has since been verified, leaving three. The rest are reworkable if they cannot be obtained.

| Source | Disposition |
|---|---|
| **Davis 1989** | **Must open.** Ch. 8 claims his reliability coefficients and "validated scales" — a specific numerical claim. `10.2307/249008` |
| **Nielsen 1993** | **Must open.** Carries the severity scale behind every rating in Table 8.8. Book, Academic Press |
| **Caulfield 2013** | **Must open.** A retraction claim against a published result cannot rest on an unread source. Also: the bib title does not match the post findable online — settle which piece and which author |
| **Greenwald 1976** | **Must open.** Cited as the warrant for not counterbalancing, the design choice most likely to be pressed at the defence. `10.1037/0033-2909.83.2.314` |
| Vessey 1991 | Reworkable. The claim made of it is the paper's own central thesis. `10.1111/j.1540-5915.1991.tb00344.x` |
| Laugwitz 2008 | Reworkable. UEQ structure already verified against the deployed instrument. Free from ueq-online.org |
| ~~ISO 9241-11~~ | **Verified 2026-09-02** from the free ANSI preview, without buying the standard. See the log. |
| ISO 9241-210 | Reworkable. `context/related-work/77520.html` is the catalogue page carrying the four HCD activities |
| Ware 2004 | Reworkable. Cited for the concept it is known for; no quotation or number |
| Palmer 1992 | Reworkable. Same |
| Saldaña 2013 | Reworkable. Conventional method attribution |
| Denley 2012 | Reworkable, or droppable. Descriptive only. Free EDUCAUSE ebook |
| Shneiderman 1983 | Re-download from IEEE Xplore; the committed file is the viewer wrapper |

**Never touched, whatever a sweep says.** Questionnaire item 2 in the evaluation appendix reads "The interface improved my productivity when dealing with course dependencies and constraints". It is the instrument as administered and is reproduced verbatim, so it sits outside the house vocabulary by necessity.

**Citation verification log.** Every citation checked during a chapter pass is appended here with its verdict, so nothing is opened twice.

**A source is cleared per claim, not per key.** A verified entry covers the citation instances that existed when it was written, and nothing else. New instances of a cleared key inherit a green mark they never earned, which is how the Munzner overclaim survived: the entry read "all six claims" while the thesis had grown to eight instances. Entries therefore record the instance count at verification time, and a source that gains instances is re-opened for the new ones only.

**Munzner 2009, re-checked 2026-09-03.** 8 instances. The six original claims stand. The seventh, added in Overleaf after Chapter 2 closed, read "Munzner explicitly anticipates such an adaptation" of using a requirements specification as the level-2 output. **She does not.** §2.3 is firm that the level-2 output is operations and data types, and no passage anticipates anything richer. Two things in the paper do support the weaker claim that the model accommodates it: §7 says the model "combines well with" van Wijk's requirements-first process, applied to the three design levels; and in §4.2 and §4.4 she reads the abstraction level of MatrixExplorer (Henry and Fekete) and LiveRAC (her own co-authored system) as an explicit requirements list containing generic operations. Section~2.1 now cites the second of these. Do not restore "anticipates", "recommends" or "endorses" for this source: §4 is post-hoc analysis of published papers, not a design method she proposes. Our own spec meets her stated condition, the generic operations appearing in the appendix requirements (`filter` 13, `select` 14, `overview` 6, `sort` 2), not in Chapter 5's prose.

### Chapter 3 (Related Work), full audit 2026-09-03

**All 46 cited sources opened and claim-checked.** 42 PDFs in `context/related-work/`, one blog post fetched, plus Santos 2012 and Denley 2012 obtained during the pass. Nothing in this chapter is now unopened. The count after each key is its citation instances **across the whole thesis** at audit time; a key that gains instances is re-opened for the new ones (see the per-claim rule above).

**Supported, no action** (verdict holds for every instance at the count shown):
`auvinen_stops_2014` 3 · `bartel_design_2024` 16 (nine principles; every one used in Ch. 6 checks out) · `bercovitz_courserank_2009` 2 · `bhumichitr_recommender_2017` 3 · `bodily_review_2017` 2 (93 articles, 17 %, 6 % all exact; "reported a needs assessment" is the authors' own hedge and is more accurate than "conducted") · `caulfield2013` 1 · `chun_planglow_2025` 1 · `dexter_ontology-based_2009` 1 · `govaerts_student_2012` 1 · `huberth_computer-tailored_2015` 1 · `jivet_awareness_2017` 1 · `judel_supporting_2023` 7 · `kabicher_coordinating_2009` 1 · `laghari_academic_2023` 1 · `loboda_mastery_2014` 2 · `ma_courseq_2021` 2 (N=32 within-subjects; four significant improvements; algorithm held constant; the ease-of-use reversal is also significant) · `mahidashti_elcano_2024` 1 · `masiello_current_2024` 1 · `pardos_designing_2020` 1 · `rollande_graph_2013` 2 · `sommaruga_curriculum_2007` 1 · `srisamutr_course_2018` 2 · `verbert_learning_2020` 2 · `wasfi_optimizing_2023` 1

**Findings recorded, so they are not re-derived:**

| Key | Instances | Finding |
|---|---|---|
| `caulfield2013` | 1 | **Blocker cleared 2026-09-03.** Post fetched. Bib title is correct and both halves of the claim are supported verbatim: he asks whether "the number of classes a student took is controlled for" and proposes that "students are taking more Course Signals courses because they persist, rather than persisting because they are taking more Signals courses". The old note's worry about a title mismatch was unfounded. Remaining question is editorial only: whether a blog post should carry a retraction claim against a peer-reviewed result. |
| `chaturapruek_how_2018` | 1 | Design is a **randomised encouragement design**, not random assignment to the platform: "we deemed it both impractical and unethical to compel or prevent use of Carta" (uptake 80 % vs 52 %). The **0.28 SD is the 2SLS instrumental-variable estimate**; the intention-to-treat effect is 0.05 SD. The within-course mechanism is **exploratory** in the source ("Our exploratory analysis suggests…"; "our study design prevents us from identifying the psychological mechanisms"). Do not restore "randomised undergraduates to a platform" or state the mechanism as established. |
| `santos_empowering_2012` | 1 | **Claim unsupported by the correct paper.** The 2012 ARTEL paper was obtained and is an evaluation of an already-built tool ("we focus on the evaluation by students of this tool"), 27 students, SUS-based. "Brainstorming" appears only as a topic in the students' own HCI coursework, tracked as a Toggl activity. There is no participatory co-design of the dashboard. Also note `context/` holds Santos et al. 2013, which is **cited nowhere** and is a stray from a collection pass. |
| `arnold_course_2012` | 1 | The risk model has **four** inputs, not two: "performance… effort… prior academic history… and student characteristics". Reported effects are exact: As and Bs +10.37 pp, Ds/Fs/withdrawals −6.41 pp; 2007 cohort one-year retention 96.71 % vs 83.44 %. The signal reaches students **through an instructor-initiated email**, so this is not a directly student-facing system. |
| `teasley_student_2017` | 2 | Both uses supported, but the second strictly contains the first, four sentences apart. Teasley also classes Course Signals as designed "primarily by course instructors", which contradicts the section's framing sentence. |
| `esteban_helping_2020` | 3 | Their genetic algorithm tunes the **recommender's own configuration**; it never builds or optimises a study plan. Not an optimisation-based planner. `srisamutr_course_2018` is the only genuine one in that group. |
| `wang_discovering_2015` | 1 | Process discovery and cohort-path comparison, on **simulated** data; "We are currently building such a recommender system." Not conformance checking: the word appears once, in the conclusion, as a general capability. |
| `bendatu_sequence_2015` | 1 | Instructor-facing curriculum conformance analysis. **No recommendation component**, so it does not belong under course recommendation. |
| `wardani_major_2020` | 1 | Pre-enrolment **major**-choice decision support. Wrong granularity for a course recommender, and "specialisation" is unsupported. |
| `siirtola_interactive_2013` | 1 | Descriptive; detects topic overlap between **courses**. The word "unnecessary" never appears and the paper makes no such judgement. |
| `trippel_developing_2025` | 7 | Requirements from four institutional stakeholders, confirmed, though one of the four is a student in a committee role; the prototype was then evaluated with 15 CS students. **"Most participants liked the graph visualisation" overstates**: "most" is verbatim for wanting to use the tool, but for the visualisation the paper says "well-received" and "many participants appreciated", with no counts. |
| `hirmer_requirements_2022` | 3 | 12 students, semi-structured, confirmed. **Its prototype is not purely table-based**: "dependencies are visualized additionally to the user as a graph". This is the nearest counterexample to the thesis's gap claim and is the reason the "treated in isolation" premise needs narrowing. Short-term planning is characterised in their **results** (participant data), not defined by the authors. |
| `roepke_study_2024` | 4 | Supplies the matrix axes verbatim: "columns of the interface indicate semesters, rows indicate different areas of a study program". Prerequisite highlighting and rule-violation warnings come from `judel_supporting_2023`, not from here. Roepke also says implemented feedback is "only limited to fixed feedback on module cycles and hard requirements". |
| `judel_supporting_2023` | 7 | Hover-arrow dependency display and the orange/red violation icons. Note it **never uses the name AIStudyBuddy**; Roepke 2024 describes it as an RWTH precursor prototype folded into StudyBuddy. |
| `wagner_combined_2023` | 1 | Genuinely an AIStudyBuddy paper (Roepke and Judel are co-authors). Architecture and methods only, **no UI description**, so it supports project identity and not any interface specific. |
| `zucker_vicurrias_2009` | 2 | Students reach the tool **through an advisor** rather than directly. |
| `holman_gradecraft_2013` | 1 | "Additive" is not the paper's word; it is points-and-levels, and the paper also uses subtractive framing. The predictor is prospective, which contradicts "ED focus on visualising past or current progress". |
| `denley_austin_2012` | 1 | EDUCAUSE published *Game Changers* as web chapters, so the web text **is** the chapter; no PDF exists to obtain. Degree Compass ranks on **three** factors, not two: remaining requirements, **centrality to the curriculum and major**, and only then a predicted-grade model "overlaid" on that ranking. |
| `wong_sequence_2018` | 3 | A four-page doctoral-consortium **proposal**, future tense, no results. |
| `arndt_ki-basierte_2023` | 1 | Answer Set Programming, which is constraint-based rather than rule-based. Two-page position paper, nothing implemented. |
| `yuan_research_2024` | 1 | Adult education; internally inconsistent domain claims and implausibly clean numbers. Weak support for any load-bearing claim. |
| `schwendimann2017` | 3 | **Does not support the actionability-convergence claim.** Its actionability sentence is background framing citing a third party; its own findings concern evaluation immaturity ("58 percent contained no evaluation"). `verbert_learning_2020` and `masiello_current_2024` do support it. |
| `nuutinen_visualization_2003` | 1 | Claim fine; bib venue was wrong (see below). |

**Chapter 4, 2026-09-03.** Three citations: `gale_using_2013` and `sandelowski_real_2001` were verified in earlier sessions. `saldana_coding_2013` was **cut**, not verified: both uses were generic ("first-cycle coding guidance for labelling codes and attaching them to excerpts"), no claim, number, quotation or procedure rested on it, and Braun and Clarke is cited eight times in the same chapter with page anchors as the method authority the thesis actually follows. It was the chapter's only unopened source; removing it removes the dependency.

**435 initial codes: confirmed by the artefact, 2026-09-04.** This entry previously recorded 435 as a decision taken against a disagreeing document, citing "493 code rows with 488 distinct labels". That count was wrong. `context/interviews-round1/First Open Coding.docx` (byte-identical to the copy under `context/prototype/`) holds eight tables; the **six per-interview code tables hold exactly 435 rows** — 81, 75, 56, 88, 69 and 66 across I1--I6 — with 434 distinct labels, one label being used twice. The 493 came from counting all eight tables (494 rows including headers), the other two being a category-count table and the requirements table. The document's own header line claims 438; its rows say 435. Ch. 4 §4.5.2 now prints the per-interview breakdown, so the number can be re-derived from the source in a minute.

**434 of 435 code labels are unique**, which is why the appendix reproduces excerpts and not codes: each initial code labels a single excerpt and groups nothing, so a code column beside the excerpts would repeat them in paraphrase.

**Chapter 1, three sources opened 2026-09-03.** The Chapter 3 audit verified Chapter 3's claims; Chapter 1 reuses fifteen of the same sources for different claims, which the per-claim rule above makes a separate job. The three never opened for their Ch. 1 claim:

- `schulte_large_2017` (1 instance) **supported**, near-verbatim: "Degree and course advisors and student support units find it challenging to provide evidence based advise to students." Our "at scale" is fair, the paper being "a whole university scale approach"; "scheduling advice" narrows their "evidence based advise" slightly and is acceptable.
- `morsy_study_2019` (1 instance) **was a partial, now fixed.** We had timing and sequencing "associated with a student's final grade and time to degree", giving both equal weight. The abstract: "TTD is highly correlated with both the timing and ordering of courses that students follow in their degree plans, **while the correlation between graduation GPA and the course timing and ordering is not as high**." Ch. 1 now says "associated with time to degree, and less strongly with final grade".
- `judel_supporting_2023` (2 instances in Ch. 1) **supported**, near-verbatim: "While this exemplary plan and its adaptations all try to outline suitable paths through the study program, they usually do not account for any kind of deviation. If students fail exams or postpone modules, an individual study plan is needed."

Two Chapter 1 sentences also had to follow the Chapter 3 corrections: the ED framing ("visualise what a student has done") and the claim that graph and table tools sit "in isolation from one another", which Judel and Hirmer both contradict. Fixing a claim in Related Work does not fix its copy in the Introduction; check both.

**Chapter 5, 2026-09-04.** All three sources opened and each claim checked against the passage it rests on.

- `nuseibeh_requirements_2000` (2 instances) **supported, now anchored.** The definition is verbatim on p.~37: requirements engineering is "the process of discovering that purpose, by identifying stakeholders and their needs, and documenting these in a form that is amenable to analysis, communication, and subsequent implementation". The second use asserted that a theme is the "operative, citable expression of a stakeholder need", which the paper nowhere says; it now rests on what the paper does say, p.~39, that information gathered during elicitation "has to be interpreted, analysed, modelled and validated" and is not "out there to be collected simply by asking the right questions". Printed page = PDF page + 34.
- `gotel_analysis_1994` (2 instances) **supported, now anchored.** p.~94 defines traceability as the ability "to describe and follow the life of a requirement, in both a forwards and backwards direction", which carries the backwards claim in 5.1. p.~96 defines pre-RS traceability as "those aspects of a requirement's life prior to its inclusion in the RS", which is what the chain sentence now says. Printed page = PDF page + 93.
- `iso9241_210` **verified against the cited edition, 2026-09-04.** The earlier note here was wrong: `context/related-work/77520.html` is only the ISO catalogue page and carries the abstract, not the scope text. The published sample of the second edition, reachable from that page's "Read sample" and archived at `cdn.standards.iteh.ai/samples/77520/...ISO-9241-210-2019.pdf`, gives the contents in full. Second edition, 2019-07, matching the bibliography entry. Clause 5.2: "The design is based upon an explicit understanding of users, tasks and environments", which is the first half of the opening sentence. Clause 7, "Human-centred design activities": 7.2 "Understanding and specifying the context of use", 7.3 "Specifying the user requirements", 7.4 "Producing design solutions", 7.5 "Evaluating the design", which is the second half. Note for anyone re-checking against older material: the 2010 edition numbered these 4.2 and 6.2--6.5, so a clause number quoted from a textbook may not match this edition. Our sentence cites no clause number.

**Two count defects in the feature specifications, found by the cross-check.** FEATURE-006 was recorded with importance score 14 while its themes (T5, T7, T59) sum to 12; the chapter table was right and the appendix is now corrected. FEATURE-010 listed T28 among its themes while both the chapter table and the traceability matrix list four themes, and its recorded score of 5 is the sum of those four; T28's requirement home is Feature~13, Req.~2, so it was dropped from FEATURE-010 and that evidence sentence now rests on T32, which states the same need. Correcting FEATURE-006 also broke the appendix's claim that features appear in descending score order, since identifier order and score order now differ at that one pair; the appendix says identifier order instead, which keeps `\ref{feat:0XX}` printing the number that matches the identifier.

**Chapter 6's three perceptual sources, 2026-09-04.** All three claims settled without buying anything.

- `palmer1992` **supported, claim narrowed.** The abstract states that grouping by "elements being located within a common region of space" is "capable of overcoming the effects of other powerful grouping factors such as proximity and similarity" (*Cognitive Psychology* 24(3), 436--447). Our sentence had said such elements are perceived as belonging together **pre-attentively**, which Palmer does not claim; it now says what he demonstrates, that common region overrides proximity and similarity.
- `shneiderman1983` **supported.** The published abstract carries the three principles the sentence rests on: "visibility of the object of interest; rapid, reversible, incremental actions; and replacement of complex command language syntax by direct manipulation of the objects of interest" (*Computer* 16(8), 57--69). The sentence now states that principle rather than paraphrasing it as a "drag metaphor". The file in `context/related-work/` is still a browser print of the IEEE Xplore viewer rather than the article; the claim does not depend on the body text, but replace the file if the PDF is ever obtained.
- `ware2004` **cut.** The sentence citing it stated a design decision, that border weight encodes obligation in three steps, and attributed it to a book nobody in this project can open. The decision is now stated without an attribution it does not need, and the bibliography entry is removed.

**Bibliography defects found in the same pass**, 7 of 46: `wagner_combined_2023` was missing three authors (Helal, Roepke, Judel), the only one that changed a printed `alpha` label; `huberth_computer-tailored_2015` had three wrong given names; `zucker_vicurrias_2009` was typed as `@inproceedings` for a journal article (*Journal of Computing Sciences in Colleges* 25(2), 138–145) with an unresolvable `10.5555/` ACM placeholder DOI; `nuutinen_visualization_2003` omitted "Learning" from ICALT's name; `chun_planglow_2025` had authors two and three swapped; `siirtola_interactive_2013` dropped the diacritic in Räihä; `wang_discovering_2015` carried a stray period inside the title braces.

Refuted leads, recorded so they are not chased again: `santos_empowering_2012` is correctly three authors (CEUR Vol-931), Govaerts is **not** among them; `masiello_current_2024` correctly points at the 2024 *Education Sciences* overview and not the Mohseni and Masiello 2025 co-design paper also on disk; `govaerts_student_2012` and `wasfi_optimizing_2023` author orders are right despite misleading multi-column title-page layouts.

Verified in prior sessions and not to be re-checked: Braun & Clarke 2022 (page anchors and phase names corrected against the book), Trippel & Röpke 2025, Auvinen 2014, Hirmer 2022, Nielsen 1994 (both heuristics), Sandelowski 2001, Gale 2013, Bhumichitr 2017, Bodily & Verbert 2017 (93 *articles*, 17 %/6 % are shares of articles), Bartel et al. 2024 (nine principles; user-centred design and study-programme-specific personalisation are **one combined principle**).

Verified 2026-09-02 (moved here from in-document notes when those were retired):

- **ISO 9241-11:2018**, verified without buying the standard. Clause 3 is paywalled, but the introduction, which is inside the free ANSI preview at `webstore.ansi.org/preview-pages/ISO/preview_ISO+9241-11-2018.pdf`, states the definition in the standard's own words: usability is "the extent to which a system, product or service can be used by specified users to achieve specified goals with **effectiveness, efficiency and satisfaction** in a specified context of use". That is exactly and only what the two citing sentences claim, in Ch. 2 §2.6 and Ch. 8 §8.1, both of which map codes to "an ISO 9241-11 dimension". Second edition, published 2018-03; the bibliography entry now records both. One thing to know rather than to act on: the 2018 edition reframes usability as *an outcome of use* rather than as a property to be measured, so if a later chapter ever describes the three dimensions as a checklist, that is the wording to watch.

- **Chapter 1, opening paragraph.** `judel_supporting_2023` carries the exemplary-plan sentence: its abstract states the plan in the examination regulations "may only fit as long as no adjustments have to be made", and that a failed examination or a postponed module calls for an individual plan. `schulte_large_2017` carries the advisor sentence — "degree and course advisors and student support units find it challenging to provide evidence based advise to students". `morsy_study_2019` carries the outcome clause, and its conclusion is associational, not causal: students clustered by graduation GPA and time to degree differ in when and in what sequence they take courses. Hence "are associated with". `wong_sequence_2018` was dropped from that paragraph, and the claim about motivation with it, since no source supported either.
- **Chapter 1, dashboards sentence.** `schwendimann2017` and `verbert_learning_2020` review learning-analytics dashboards in general, explicitly covering dashboards "ready-made to serve administrators, teachers", so alone they were wider than the sentence. `loboda_mastery_2014` anchors it: *Mastery Grids* is a student-facing "social progress visualization" built on open learner modelling and evaluated in a classroom. `bodily_review_2017` carries "almost always built separately" — 17 % of 93 reviewed articles integrate both.
- **Dependency sweep.** 58 prose occurrences checked against the glossary. Sound in Ch. 1, Ch. 4, Ch. 6, Ch. 9 and the codebook appendix. Still flagged at their sites: Related Work's "broad, multi-layered structural dependencies", and Implementation's two non-course uses.

Verified 2026-09-02, against the PDFs delivered that day:

- **Wienand et al. 2024** — all three uses hold. The quotation "index card-like presentation" is exact and sits beside the frustration finding it rests on; the Dashboard's three-level progress-bar pattern and the "might feel lost on how much progress they already made" quotation are both on p. 691–693; DP9 is literally "motivational elements". The domain caveat in Ch. 6 is what makes the transfer defensible and must stay.
- **Arnold & Pistilli 2012** — the whole sentence holds: the algorithm is "run on-demand by instructors", the output is "a red, yellow or green signal", the inputs include performance and LMS interaction, and §3.1–3.2 report both the grade and the retention outcomes. "Reported to improve" is the correct hedge.

---

## 15. The final pass

Run **once**, after every chapter is closed and every PR merged, on the built PDF and not on the source. This is not the per-chapter Definition of Done (§10) run nine more times. §10 is deliberately blind to everything outside the chapter in hand, and every defect this project has produced has been of exactly that kind: an edit in one place quietly invalidating a claim somewhere else. The final pass exists to catch what a chapter-by-chapter read structurally cannot.

**Preconditions.** All chapters marked done in §12. No open `\TDblock`, `\TDmajor` or `\TDminor` anywhere. Every §0 forward-dependency row worked. Every blocker in §13 closed or consciously accepted.

### A. Mechanical gates

Automated, and nothing else starts until they are green.

1. `python3 tools/check.py` passes with no blocking failures, and every remaining warning has been looked at and consciously accepted.
2. `python3 tools/check.py --submission` passes: notes off, no `%% REV`, real metadata, no empty `formalities/` file, no raw `\todo`, clean build (§11a).
3. Full build clean: no errors, **zero undefined references, zero undefined citations**.
4. Notes-off build produces zero residue: no Review Annotations chapter, no To-Do index, no coloured boxes, no severity word anywhere in the extracted text.
5. Bibliography: every cited key present, and a decision recorded for each uncited entry (cut it or use it). Currently 26 uncited.
6. Abbreviations expanded at first use **in reading order across the whole document**, not per chapter.
7. Every glossary term hyperlinked with `\gterm` at its first occurrence in the thesis.
8. Every figure and table referenced in prose; caption lengths within §7.

### B. Cross-chapter consistency

The part no chapter pass can do. Work from §0's consistency register and check every number, name and count **everywhere it appears**, not where it was last edited.

9. Every value in the §0 register, at every site. Participant counts follow the verb rule: twelve run, eleven analysed, `/11` denominators.
10. Every claim one chapter makes **about another chapter's content**. Chapters 1, 2 and 9 all assert what Chapter 8 found; those assertions are checked against the finished Chapter 8, not against memory. The §0 forward-dependency table is the starting list, not the complete one.
11. The research questions: character-identical wherever quoted, and each one actually answered where the thesis says it is answered.
12. Terminology and fixed names per §5. A bare "dependency" never includes the soft form.
13. Tables against their source artefacts, row by row. Chapter 8's tables were built by hand once and did not match the appendix; assume the same of any table not generated from data.
14. Every citation still supports the claim it is attached to, using §14's instance counts: any key whose count has grown since it was cleared is re-opened for the new instances only.

### C. Is it clear that this research is exploratory?

**The specific review Moritz asked for, 2026-09-03.** Read the whole thesis once with this single question in mind. The work is a design study: two small samples at one institution, one fixed scenario order, one coder, and descriptive statistics. That is a legitimate and appropriate design, and it is not a weakness to be hidden. The failure mode is not admitting it in the limitations, which the thesis already does. The failure mode is **prose elsewhere that quietly reads as more than exploratory**, so that an examiner meets a confident claim in Chapter 1 or 9 and only finds the qualification in §2.4.

Check, in this order, because the risk rises as you go:

15. **The front matter.** Abstract, Kurzfassung, and the conclusion. These are written last, when everything else is already careful, and they are where the framing is most likely to be lost. They must say what kind of study this is, in their own words, not rely on the reader reaching Chapter 2. Both files are empty today, so this is a writing instruction as much as a check.
16. **Claim verbs against evidence, everywhere** (§3, §10 item 17). *Establishes*, *demonstrates*, *shows*, *proves*, *confirms* are almost never right here. *Indicates*, *suggests*, *is consistent with*, *describes* usually are. A single sign test on eleven participants supports none of the strong verbs.
17. **Causal language.** Eleven participants, a fixed scenario order, and no counterbalancing mean the design describes what students did; it cannot attribute a behaviour to a component. Any sentence of the form "the graph caused / led to / improved X" is wrong regardless of how the data looks.
18. **The word "significant"** used loosely where no test was run, and every reported number checked for whether it is descriptive or inferential. UEQ and TAM results are a descriptive layer and must read as one.
19. **Frequencies.** Every one carries its denominator, and none is presented as if it generalised. `9/11` is nine of eleven students in this study, not 82 % of students.
20. **Generalisation claims.** Chapter 9 §9.7 separates what is specific to the hybrid from what might carry further. Nothing elsewhere in the thesis should quietly claim the wider version.
21. **The contributions (§1.4) and the RQ answers (§9.1)** read together, back to back. These are the two places a reader looks for the headline, they are written at different times, and they are the most likely pair to drift apart in confidence.

A useful test for any suspect sentence: **could this claim be false and the thesis still be fine?** If yes, the sentence is describing a finding and needs its hedge. If no, it is describing what was done and can be stated plainly.

### D. The read

22. Read the **printed PDF** end to end, in one sitting, notes off. Not the source, not a diff, not chapter by chapter. Anything that has never been read in sequence has never been read.
23. Read Chapters 1, 2 and 9 again immediately afterwards, in that order, as a set. They are the argument; the middle chapters are the evidence.

### E. Submission hygiene

24. **Re-check every page-anchored citation against the source**, Moritz's request 2026-09-03. There are twenty-one in the thesis as of 2026-09-04, sixteen in Chapter 4 and three in Chapter 5; sixteen point at a specific page of Braun and Clarke; the others are Sandelowski p.~239, Nuseibeh and Easterbrook pp.~37 and~39, and Gotel and Finkelstein p.~96, all verified 2026-09-04 against the papers' own page markers. Gotel p.~94 was verified too and then dropped: the sentence it sat on describes this thesis's theme set, not a claim of theirs. Page anchors are the citations an examiner is most likely to open, and the ones a later edit can silently invalidate. Establish the PDF-to-printed page offset first: for the Braun and Clarke file it is printed = PDF minus 35.
24. §11a in full, plus PDF/A validity, correct metadata, and the declaration and disclosure files complete.
25. The data-protection items in §13 settled: the consent PDF carrying a real name and birthdate in git history, and the retention of the recordings.

