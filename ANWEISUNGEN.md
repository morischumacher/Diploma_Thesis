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
| Programmes in scope | 2 — BSc Computer Science UE 033 521, MSc Software Engineering UE 066 937 |
| Bachelor programme total | 180 ECTS, 101 courses |
| Scope boundaries | OOS1–OOS4 |

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

### 1.2 Length — polish, do not restructure
`REVIEW.md`'s shortening plan is **wrong on its headline item**: Chapter 5 already carries only the summary table, and the full feature specs already live in Appendix A.3. Corrected position:

- **Main matter is 110 pages. That is a normal, defensible master's-thesis length. No structural cuts.**
- The only chapter worth trimming on length grounds is **Design (28 pp)**, and only where a "rejected alternative" was never a live alternative — cut those to one sentence, keep the four genuinely weighed ones in full. Expected saving 4–6 pp. This is a by-product of the Design pass, not a goal.
- **Additions are expected to outweigh cuts**: Ch. 4 findings section (§1.4), abstract, Kurzfassung, acknowledgements, AI-tools disclosure. Budget for ~190 pp at submission and stop worrying about it.

### 1.3 Working mode — branch + PR, one chapter at a time

**Never push to `main` directly.** Every change goes on a branch and into a pull request, and what it does is explained in the chat before it is opened. This holds even for merge resolutions and for changes that look purely mechanical — Moritz reviews in GitHub and pulls into Overleaf from `main`, so an unannounced commit on `main` arrives in his editor without him having seen it. Set 2026-09-02 after two direct pushes.
A fine-grained PAT scoped to `Diploma_Thesis` (Contents read/write, Pull requests read/write) is provided; rotate it after submission. Loop per chapter:

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

**Every factual claim about the tool** is checked against the **evaluated tag** of `hypridplanner`, not against `main` and not against a refactor branch. Claims about the system participants used must be true of the version they used. Post-study changes go only in §7.8 (Revisions After the Evaluation Study) and must say they were not in front of a participant.

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

Two further rules that no scanner can check. **A claim verb must match the evidence:** *establishes* only where the design supports the inference, *suggests* or *indicates* for an exploratory pattern, and any finding sentence names its source (a code, a table, a section). And **no rhetorical questions** in prose — a question in the thesis's own voice is either a research question or a sentence that should have been a statement.

**No vague summary-hedges.** "leaves a clear gap" → name the gap; "in spirit closest to X" → "most closely aligned with X"; "a large and varied field" → "a substantial and heterogeneous field". Avoid loose intensifiers (*really, very, themselves*).

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

**Participant quotations — settled 2026-09-02, `\enquote{}` with no italics.** This is the standard form, not merely the cheaper sweep: `csquotes` exists for exactly this and handles nesting and language-sensitive marks, and academic style (Chicago, APA) sets short quotations in quotation marks without italics, reserving italics for emphasis and titles. 161 instances of the `` ``…'' `` forms were converted in Pass 0; none remain. Attribution follows the closing quote as `(C21)` for formative themes and `(P09)` for evaluation participants. Quotations longer than about forty words take a `quote` environment without quotation marks — the longest quotation in the thesis is currently 154 characters, so none does.

**Translations must be declared.** Both studies were conducted in German. Chapter 4 §4.5.1 and Chapter 8 §8.1.6 each carry one sentence saying the quoted excerpts are the author's translations and the German originals are held with the transcripts. Check that sentence exists in both before either chapter is closed, because without it the word "verbatim" is claimed and not delivered.

---

## 5. Terminology and abbreviations

**Fixed names.** Use exactly these, capitalised as shown, everywhere: Table View, Graph View, Parking Stage, Dashboard, Recommendation Panel, Compliance Engine, Semester Picker, Course Catalogue. The artefact is *the tool* or *the study planner*; the instrument is *the study-guide application* (the questionnaire web app). The two studies are **the formative study** and **the evaluation study** — never "study 1 / study 2".

**Every abbreviation is expanded at first use in the running text, then used bare.** Currently broken:

| Abbreviation | Status | Action |
|---|---|---|
| ECTS | 124 uses, **never expanded, not in glossary** | Expand once in Ch. 2 and add a glossary entry |
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

**Deviations from the proposal must be acknowledged, not quietly absorbed.** The proposal (Jan 2026) promised four sub-questions including a recommender learned from students' interaction data (SQ2) and its integration (SQ3), and a counterbalanced within-subjects design against a spreadsheet/paper baseline. The thesis delivers three RQs, a recommender over synthetic prior-student data with quality explicitly out of scope, and an uncounterbalanced graph-off/graph-on design. Each of these is defensible and each is defended somewhere in the text — but they are defended in scattered places. **Add one short paragraph, in Ch. 2, stating how the executed design differs from the proposal and why.** An examiner reading both will look for it.

---

## 9. Numbers and data integrity

**One artefact per number, one number per fact.** Every figure in Ch. 8 and Ch. 9 traces to the evaluation study's `analysis/` folder — the frozen stage-log parser output, `findings-matrix.csv`, `completion-audit.md`, `process-metrics.md`, and the Raw-JSON column of `US Results.xlsx`. When a number changes, regenerate the whole dependent set (chapter table, prose, appendix, discussion) from the same run rather than patching the instance you noticed.

- The frame total is **2,179** and it must sum from Table 8.2's own rows (1,197 + 982). It does today. Any reparse that changes it changes Table 8.2, the loop shares, the appendix labelling-scheme section, and Ch. 9's parenthetical.
- UEQ values use the **population-SD** convention and the **questionnaire app's own item order**, which differs from the standard UEQ order; the spreadsheet's eight UEQ columns are lossy. Anyone recomputing from those columns gets wrong numbers — say so in the appendix if it is not already there.
- Percentages: `\,\%` throughout (58 uses, consistent — keep).
- ECTS: **`~ECTS` with a non-breaking space**, e.g. `30~ECTS`. Currently 25 of 33 comply; eight use a plain space. Sweep.
- Cross-reference words take a non-breaking space: `Section~`, `Chapter~`, `Figure~`, `Table~`, `Feature~`, `Req.~`. Compliant today except a handful of `Table ` instances (all of which are the panel name "Table View", not references — do not "fix" those).
- Spell out numbers under ten in prose ("six participants", "eleven analysed"), use digits for measurements and identifiers.

---

## 10. Definition of done, per chapter

A chapter is finished only when every line below is true. This is the checklist to run before opening the PR.

1. Read end to end in one sitting, not as a diff.
2. Every `\cite` in the chapter verified against the opened source and logged in §14.
3. Every claim about the tool checked against the evaluated tag of `hypridplanner`.
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

**A note that has been dealt with is deleted, not marked done.** Set 2026-09-02. The thesis carries only outstanding work; a green "verified" block in the middle of a chapter is noise for the person reading it, and there were eleven of them. What was checked and what it showed goes in §14's log instead, which is where someone looks to avoid re-checking. The `\TDok` macro is retired.

The only note that may remain in a closed chapter is one **deferred by decision** — kept open on purpose, saying why and when it is revisited. Ch. 1's contributions note is the example: it waits on Ch. 8 and Ch. 9. Any other open note means the chapter is not done.

**Curriculum analytics is out of the thesis** (Moritz, 2026-09-02). It was in the proposal, but Related Work never covered it and it plays no part in either gap the thesis argues, so the Introduction no longer previews it. `archambault_curriculum_2015`, `buck-emden_analyse_2018` and `kapucu_competency-based_2017` are now uncited.
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
| 1 | Introduction | **done 2026-09-02**, two items left for Moritz | All 7 review comments resolved; ED/ERS paragraph rewritten to Ch. 3's argument; TU Wien and both curricula footnoted; contributions sized; Outlook credits Ch. 9 with RQ3. Open for a decision: the opening paragraph's citation fit (Morsy/Wong/Schulte), and whether curriculum analytics returns via Ch. 3 |
| 2 | Methodology | needs edit | second assumption (`%% AIREV`), proposal-deviation paragraph, data-handling `\todo`, ECTS/StEOP expansion |
| 3 | Related Work | needs edit | Positioning gap wording (§1.1), Ma et al. claim already softened — re-verify, five-paper "broad consensus" sentence |
| 4 | Formative Study | **needs new section** | Findings section (§1.4), quotation style sweep, `\todo` on forward references, "Link to Subsequent Chapters" cut to two sentences |
| 5 | From Themes to Requirements | light | opening meta-discourse, cross-check the 13/55 counts against Appendix A.3 |
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
- Codes-vs-themes is resolved: the appendix now calls C1–C64 themes, matching the chapters and the glossary.

**Still open from that review and worth re-checking during the relevant chapter pass:** the E-G18 attribution to P06; the P10 "not placing from the graph at all" framing; the Wienand et al. citations (§14); whether the two inert recommendation channels were inert in `v1.0-evaluated` specifically.

---

## 14. Material I still need from you

**Sources cited in the thesis with no PDF anywhere in the repo or project.** Until each is opened, its claim is unverified. Ranked by how much weight it carries. *Delivered 2026-09-02: Wienand et al. 2024 and Arnold & Pistilli 2012, both verified (§14). Shneiderman 1983 was committed but the file is a one-page browser print of the IEEE Xplore viewer, not the article.*

| Source | Where it carries weight | Why it matters |
|---|---|---|
| **Wienand et al. 2024** | Ch. 6 §6.2.4 (a direct quotation, "index card-like presentation") and §6.9 (three-level progress bars) | A quotation from an unopened source, in a different domain (enterprise-systems e-learning). Open access at doi 10.1007/s44217-024-00165-z |
| **Vessey 1991** (cognitive fit) | Ch. 9, load-bearing in the substitution interpretation | The theory the central design claim is read through |
| **Davis 1989** (TAM) | Ch. 8 instruments | The instrument's provenance |
| **Laugwitz et al. 2008** (UEQ) | Ch. 8 instruments | Same |
| **ISO 9241-11** and **ISO 9241-210** | Ch. 2, Ch. 5, Ch. 8 (the three-dimension mapping) | The framework RQ3 is answered against |
| **Nielsen 1993** (*Usability Engineering*) | Ch. 8 severity ratings | The severity scale's source |
| **Saldaña 2013** (coding manual) | Ch. 4 analysis method | Method citation |
| **Ware 2004**, **Palmer 1992**, **Shneiderman 1983** | Ch. 6 encoding decisions | Conventional uses, but each is cited for a specific perceptual claim |
| **Greenwald 1976** | Ch. 8 fixed-order rationale | Cited to justify not counterbalancing |
| **Arnold & Pistilli 2012**, **Caulfield 2013**, **Denley 2012** | Ch. 3 | The Course Signals retraction argument rests on two of these |

**Also needed:**
- The **GitHub PAT** (fine-grained, `Diploma_Thesis` only, Contents + Pull requests read/write) so I can open PRs.
- Confirmation that **interview round 2 is closed at 12 sessions / 11 analysed**. `CONTROL.md` still lists it as in progress with more interviews to come; every number in Ch. 8 and Ch. 9 assumes it is closed.
- The **thesis title, subtitle decision, submission date and keywords** for `main.tex`.
- Whether **TU Wien Informatics' current AI-use policy** has been checked with René or Selina, since it shapes the disclosure text.
- Access to the **evaluation study's `analysis/` folder** (stage logs, findings matrix, completion audit, `US Results.xlsx`) if you want any number re-derived rather than taken on trust — it lives on your Mac, not in this repo.

**Per-source disposition, set 2026-09-02.** Four must be opened; the rest are reworkable if they cannot be obtained.

| Source | Disposition |
|---|---|
| **Davis 1989** | **Must open.** Ch. 8 claims his reliability coefficients and "validated scales" — a specific numerical claim. `10.2307/249008` |
| **Nielsen 1993** | **Must open.** Carries the severity scale behind every rating in Table 8.8. Book, Academic Press |
| **Caulfield 2013** | **Must open.** A retraction claim against a published result cannot rest on an unread source. Also: the bib title does not match the post findable online — settle which piece and which author |
| **Greenwald 1976** | **Must open.** Cited as the warrant for not counterbalancing, the design choice most likely to be pressed at the defence. `10.1037/0033-2909.83.2.314` |
| Vessey 1991 | Reworkable. The claim made of it is the paper's own central thesis. `10.1111/j.1540-5915.1991.tb00344.x` |
| Laugwitz 2008 | Reworkable. UEQ structure already verified against the deployed instrument. Free from ueq-online.org |
| ISO 9241-11 | Reworkable. Only the three dimensions are cited; they are in the free ANSI preview |
| ISO 9241-210 | Reworkable. `context/related-work/77520.html` is the catalogue page carrying the four HCD activities |
| Ware 2004 | Reworkable. Cited for the concept it is known for; no quotation or number |
| Palmer 1992 | Reworkable. Same |
| Saldaña 2013 | Reworkable. Conventional method attribution |
| Denley 2012 | Reworkable, or droppable. Descriptive only. Free EDUCAUSE ebook |
| Shneiderman 1983 | Re-download from IEEE Xplore; the committed file is the viewer wrapper |

**Never touched, whatever a sweep says.** Questionnaire item 2 in the evaluation appendix reads "The interface improved my productivity when dealing with course dependencies and constraints". It is the instrument as administered and is reproduced verbatim, so it sits outside the house vocabulary by necessity.

**Citation verification log.** Every citation checked during a chapter pass is appended here with its verdict, so nothing is opened twice. Verified in prior sessions and not to be re-checked: Munzner 2009 (all six claims), Braun & Clarke 2022 (page anchors and phase names corrected against the book), Trippel & Röpke 2025, Auvinen 2014, Hirmer 2022, Nielsen 1994 (both heuristics), Sandelowski 2001, Gale 2013, Bhumichitr 2017, Bodily & Verbert 2017 (93 *articles*, 17 %/6 % are shares of articles), Bartel et al. 2024 (nine principles; user-centred design and study-programme-specific personalisation are **one combined principle**).

Verified 2026-09-02 (moved here from in-document notes when those were retired):

- **Chapter 1, opening paragraph.** `judel_supporting_2023` carries the exemplary-plan sentence: its abstract states the plan in the examination regulations "may only fit as long as no adjustments have to be made", and that a failed examination or a postponed module calls for an individual plan. `schulte_large_2017` carries the advisor sentence — "degree and course advisors and student support units find it challenging to provide evidence based advise to students". `morsy_study_2019` carries the outcome clause, and its conclusion is associational, not causal: students clustered by graduation GPA and time to degree differ in when and in what sequence they take courses. Hence "are associated with". `wong_sequence_2018` was dropped from that paragraph, and the claim about motivation with it, since no source supported either.
- **Chapter 1, dashboards sentence.** `schwendimann2017` and `verbert_learning_2020` review learning-analytics dashboards in general, explicitly covering dashboards "ready-made to serve administrators, teachers", so alone they were wider than the sentence. `loboda_mastery_2014` anchors it: *Mastery Grids* is a student-facing "social progress visualization" built on open learner modelling and evaluated in a classroom. `bodily_review_2017` carries "almost always built separately" — 17 % of 93 reviewed articles integrate both.
- **Dependency sweep.** 58 prose occurrences checked against the glossary. Sound in Ch. 1, Ch. 4, Ch. 6, Ch. 9 and the codebook appendix. Still flagged at their sites: Related Work's "broad, multi-layered structural dependencies", and Implementation's two non-course uses.

Verified 2026-09-02, against the PDFs delivered that day:

- **Wienand et al. 2024** — all three uses hold. The quotation "index card-like presentation" is exact and sits beside the frustration finding it rests on; the Dashboard's three-level progress-bar pattern and the "might feel lost on how much progress they already made" quotation are both on p. 691–693; DP9 is literally "motivational elements". The domain caveat in Ch. 6 is what makes the transfer defensible and must stay.
- **Arnold & Pistilli 2012** — the whole sentence holds: the algorithm is "run on-demand by instructors", the output is "a red, yellow or green signal", the inputs include performance and LMS interaction, and §3.1–3.2 report both the grade and the retention outcomes. "Reported to improve" is the correct hedge.
