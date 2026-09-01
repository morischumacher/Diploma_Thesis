Here is the document with the text passages concerning dependency edges removed:

# Thesis Control Document



**Author:** Moritz Jakob Schumacher — TU Wien, Software Engineering (Master)

**Advisor:** Assistant Prof. Dr. René Röpke — First Assistant: Selina Reinhard

**Template:** `vutinfth` (TU Wien Informatics), BibTeX `alpha` style, `bibliography.bib` at repo root

**Last updated:** 2026-08-25 (Evaluation + Discussion rewritten from a two-record re-analysis; codebook back-applied)

> This file replaces the standalone control doc from chat. Pull the repo at the start of a session to pick up where we left off.
> 
> 

---

## 1. Milestone Status



| Milestone | Status |
| --- | --- |
| Proposal | ✅ Done

 |
| Figma Prototype | ✅ Done

 |
| Interview Round 1 (Requirements) | ✅ Done

 |
| Tool Implementation | ✅ Done

 |
| Interview Round 2 (Evaluation) | 🔄 In progress — includes video recordings + additional interviews still to come

 |
| Thesis Writing (Overleaf/GitHub) | 🔄 In progress

 |

---

## 2. Chapter Plan (matches `main.tex` order — as found, not invented)



| # | File | Title in thesis | Status (as of first inspection) | Words | Depends on |
| --- | --- | --- | --- | --- | --- |
| 1 | `chapters/introduction.tex` | Introduction | Stub — research question + motivation drafted, related work woven in

 | 227

 | –

 |
| – | `chapters/methodology.tex` + `chapters/methodology-figure.tex` | Methodology | PR open — split out of the old combined chapter per review comments; now its own chapter, positioned right after Introduction and *before* Related Work

 | ~900

 | –

 |
| – | `chapters/relatedwork.tex` | Related Work | PR open — 3 verified deep-dives + 4 thematic clusters (unsynthesized); now follows Methodology, not combined with it

 | ~1500

 | –

 |
| 2 | `chapters/needfindingwithprototype.tex` | Formative Study: Needfinding with a Prototype | Substantial draft

 | 4,698

 | –

 |
| 3 | `chapters/fromthemestorequirements.tex` | From Themes to Requirements | Partial draft

 | 652

 | Ch. 2

 |
| 4 | `chapters/design.tex` | Design | PR open — all 49 of Moritz's review comments resolved: language and figure fixes, view sections reordered to Graph -> Table -> Sidebar, Onboarding promoted to its own section, two new figures, ordering rationale stated

 | ~11,900

 | Ch. 3

 |
| 5 | `chapters/implementation.tex` | Implementation | PR open — all 25 of Moritz's inline review comments resolved: Frontend section restructured into four subsections, three figures rebuilt, real screenshots inserted, curriculum sources footnoted, language pass for scientific register

 | ~2,900

 | Ch. 4

 |
| 6 | `chapters/evaluation.tex` | Evaluation | PR open — rewritten to Moritz's BLUF/heading/paragraphing brief; all 31 review comments resolved; RQ3 alignment made explicit; recommendation panel now reported and measured; codebook completed to 99/99 codes

 | ~7,200

 | Interview round 2

 |
| 7 | `chapters/discussion.tex` | Discussion | Not started

 | 0

 | Ch. 6

 |
| – | `formalities/abstract.tex` + `kurzfassung.tex` | Abstract (EN + DE) | TBD

 | –

 | All

 |
| – | `formalities/aitools.tex` + `kitools.tex` | AI-tools disclosure (EN + DE) | **Empty — needs attention, see Section 10**<br> | 0

 | Ongoing

 |
| – | `appendix/appendix.tex` | Appendix | Only `formative-interview-plan.tex` currently included; `Traceability Matrix.tex` and `design requirements.tex` exist but aren't wired in yet

 | –

 | –

 |

**No separate "Related Work" chapter exists.** Related work is currently woven directly into the Introduction's motivation narrative (see the citations already there). We'll keep this style unless you'd rather split it into its own chapter — flag if so.

---

## 3. Style Guide (observed from existing text, not guessed)



* **Citations:** BibTeX, `\bibliographystyle{alpha}`. Keys already follow a Better-BibTeX-style auto-key pattern (`author_firstword_year`), consistent with a Zotero + Better BibTeX workflow — to confirm with you.


* **Voice:** first person plural ("we"), e.g. "we formulate the following main research question."


* **Tense:** present tense for framing the research question and motivation; citations integrated inline with `\cite{key}`.


* **Chapter order:** Introduction → Methodology → Related Work → Formative Study → From Themes to Requirements → Design → Implementation → Evaluation → Discussion. Methodology comes before Related Work deliberately: Related Work is stage 1 of the process Methodology describes, so describing the process before executing its first stage reads better than the reverse.


* **Scope structure:** general, evidence-independent scope (OOS1, OOS2) is defined once in Methodology (Section~sec:overall-scope) before any thesis-specific evidence is needed to justify it. Specific, evidence-dependent scope (OOS3, OOS4) is defined later in Chapter 3 (Section~sec:overall-scope-refined), alongside the excluded findings that justify them. Don't restate OOS3/OOS4's reasoning in Methodology, and don't restate OOS1/OOS2's general framing in Chapter 3, each is defined once, in the chapter where it's credible. (Renumbered from an earlier OOS3/OOS4-general, OOS1/OOS2-specific scheme per Moritz's request — the general ones now come first, matching reading order.)


* **Traceability chain (corrected again):** `Literature Review → Formative Interviews → Codes → Themes → Requirements → Features → Design → Implementation → Evaluation`. Requirements come before Features, matching the actual derivation order (Ch3 Steps 1-3: a requirement is formulated first from a code's evidence, features are formed afterward by clustering requirements) — the previous version logged here had this backwards a second time despite claiming to have fixed it once already; triple-check this specific pair before editing again. This chain is explicitly the concrete realization of Munzner's Nested Model (Section~sec:paradigm in the Methodology chapter), not a second framework: domain characterisation = Literature Review..Themes; abstraction = Requirements+Features; encoding/interaction = Design; algorithm = Implementation; Evaluation validates across levels. Keep this exact wording everywhere it's invoked (Ch2, Ch3, Methodology's Process Overview); don't rephrase differently per chapter. Note: Themes organize which codes are reviewed together (Ch2 Step 1), but each Feature's citable evidence is listed as **associated codes**, not a theme label — the code level is what's actually traceable back to verbatim excerpts. Don't reintroduce "Associated themes" in Ch3's feature template.


* **No em-dashes ("—") in thesis prose:** use a comma (or restructure the sentence) instead. Applies to all chapters, not just Ch2; sweep other chapters for this too when next touching them. (Not retroactively applied to this file's own existing notes below, since this rule is about thesis prose, not internal tracking notes.)


* **No bold text in thesis prose**, except as the label of a bullet/`\item` (e.g. `\item \textbf{Reduce information asymmetry.}`). Use `\emph{}` for emphasis elsewhere. Applied to Design in this round; sweep other chapters when next touched.


* **Spelling: "programme"** (British), not "program", when referring to a degree programme. Applied to Design in this round; sweep other chapters when next touched.


* **Citation format for codes/features/requirements**: always spell out `FEATURE-0XX, Req.~Y` (never the bare compact `Req. X.Y` form). Applied to Design in this round (36 existing + 20 converted instances); use this form in any new chapter content.


* **Figure caption length: keep consistent, roughly 100-200 characters.** One or two short sentences stating what the figure shows and the one or two facts a reader needs to interpret it; not a full re-explanation of the surrounding prose. Applied across all 10 figures in Design this round (previously ranged 90-430 characters, now 104-206). Check new figures in any chapter against this range before finalizing.


* **Scientific register throughout: avoid slang/casual phrasing in thesis prose.** Watch for phrasal verbs and colloquialisms that read as informal even when the content is precise: "figure out" -> "determine"/"identify", "kind of X" -> "a type of X" or cut entirely, "a thing" -> a concrete noun (e.g. "a second visual element"), "get around", "end up", "come up with", "deal with", "turn out", "a lot of", "pretty much", "basically". Also watch for vague summary-hedges that assert a conclusion without stating it precisely: "leaves a clear gap" -> name the specific, structural gap directly (what exactly is missing, and where); "in spirit it is closest to X" -> "is most closely aligned with X"; "a large and varied field" -> "a substantial and heterogeneous field" (or similar, but avoid the "large and varied" pairing specifically, it reads as a filler description rather than a precise characterisation). Also watch for redundant casual intensifiers ("themselves", "really", "very" used loosely) and run-on hedging that could be a direct claim instead. Swept in Design (multiple rounds, full line-by-line read-through) and in Related Work (now a full read-through, not just targeted -- also caught a leftover American spelling ("study program" -> "study programme"), "emphasize" -> "emphasise", and a subject-verb agreement slip ("articulate" -> "articulates") in the same pass, since a full style check should catch spelling/grammar too, not just register); other chapters (Introduction, Methodology, the formative-study chapters, Implementation, Evaluation, Discussion) have not yet had a dedicated language pass, only the chapters explicitly worked on so far.


* **Naming the two studies: "the formative study" and "the evaluation study", never "study 1"/"study 2".** The formative study is the prototype-based needfinding of `chapters/needfindingwithprototype.tex` (`\ref{chap:formative-study}`); the evaluation study is the summative study of `chapters/evaluation.tex` (`\ref{chap:evaluation}`). Every chapter except Evaluation already used the descriptive names; the three "study~1" references in Evaluation were converted on 2026-08-31 and each now carries a `\ref` to the chapter it means. A bare ordinal tells the reader nothing about which study is meant and forces a lookup.


* **Forward references: present tense, and used sparingly.** Write "Section~X reports…", never "Section~X will report…". Present tense is the standard for referring to another part of the same document, which exists in full at the moment of reading; the future tense implies the text is being written as the reader reads it. A forward reference is an acceptable exception to the ordering rule when the reader only needs to know that the referenced section exists and roughly what it covers; it is not acceptable when the current sentence cannot be understood without reading ahead.


* **Research paradigm:** Munzner's Nested Model for Visualization Design and Validation (`\cite{munzner2009}`), stated explicitly in the new Methodology chapter (Section~\ref{sec:paradigm}) and already assumed without citation in Design ("this chapter operates at levels 2 and 3"). Any future chapter framing itself in terms of "levels" should point back to this section rather than re-explain the model.



---

## 4. Decision Log



*(Naming/scope decisions made during writing, so later chapters don't drift.)*

* 2026-07-15 — Located interview-round-2 evaluation material in Google Drive (Meet auto-transcripts + recordings, several sessions run already, more planned). Raw transcripts contain participants' real names via Meet's call attribution, despite the study already using pseudonymous codes (P0xA/P0xB) for tool sessions. Decision: pseudonymize using the existing codes before anything enters `context/interviews-round2/`; raw Drive files never enter git.


* 2026-07-15 — Standing practice: before drafting/revising any section, cross-check already-written chapters (not just `context/`) as the primary source of truth — they're the authoritative, processed version of the raw material.


* 2026-07-15 — **Full reading pass completed** (all chapters, proposal, First Open Coding.docx, appendix structure, studyplanner/userstudy code). Two significant findings:


1. **`chapters/evaluation.tex` describes a study that doesn't match what was actually run.** The chapter (early draft) describes: within-subjects Table-vs-Graph condition, N=14 (7 experienced/7 novice), NASA-TLX + SUS instruments. But the **proposal** (Jan 2026) and the **actual collected data** (`US Results.xlsx`, Drive session notes) both show: two persona-based scenarios (not interface conditions), UEQ + TAM (PU/PEU) instruments, participant-controlled graph toggle rather than an assigned condition, 8 participants so far. The proposal and real data agree with each other; only the `.tex` draft diverges — looks like an earlier/alternative study design that was never updated after the actual methodology was finalized. **Needs Moritz's input before any further Evaluation-chapter drafting.**

* **Update (full codebase re-audit):** found a real, concrete interface-condition mechanism in `studyplanner`: `AuthGate.jsx`/`App.jsx` have a persistent, per-account "Disable Graph View" toggle, and its own UI label literally reads **"Disable Graph View (User Study Persona 1)"** — confirming this exists specifically as a research-instrument control, not just a general product setting. This suggests the evaluation design may genuinely be two-dimensional rather than the single dimension either source alone suggested: an interface condition (graph enabled vs. disabled, i.e. "Persona 1"/"Persona 2" — matching evaluation.tex's Table-vs-Graph framing) crossed with a content scenario (Security vs. AI persona, i.e. "Scenario A"/"Scenario B" — matching the real collected data and the `userstudy` questionnaire app, which only ever references "Scenario A/B" timers, never "Persona"). This doesn't fully resolve the mismatch (instrument question — NASA-TLX/SUS vs. UEQ/TAM — is still open, and N=14/7-7 split is still unconfirmed against real recruitment), but it's a real, concrete piece of the puzzle found in the code, not a guess. Still needs Moritz's confirmation before Evaluation-chapter drafting.




2. **Broken LaTeX cross-references** in `needfindingwithprototype.tex`: `\ref{chap:from-needs-to-requirements}` (2x) and `\ref{chap:requirements}` (6x) don't match the actual label `\label{chap:from-themes-to-requirements}` — these would render as "??" in the compiled PDF. Also `chapters/evaluation.tex` ends with a stray `\end{latex}` with no matching `\begin{latex}`, which will break compilation. Low-risk mechanical fixes, not yet made — flagged for confirmation before touching.




* 2026-08-22 — **This CONTROL.md file was significantly stale on pickup** (last updated 2026-07-15; 5+ weeks and PRs #43–#52 of actual work had happened since). Section 2's chapter table said Implementation/Discussion were "Not started, 0 words" (actually 2,559 and 2,297 words), Evaluation was "1,047 words" (actually 5,883, after a full rewrite), and Methodology/Related Work were "PR open" (both long since merged). Corrected Implementation's row this session; the rest of Section 2 (Discussion, Evaluation, appendix wiring) still needs the same refresh next time that's the active task — flagging so it isn't missed again.


* 2026-08-22 — **Full Section 9 checklist pass on `chapters/implementation.tex**` (PR #53). Verified every factual/behavioural claim against the actual `studyplanner` codebase (cloned read-only): exact dependency versions, router/service/migration file lists, the recommender's six scoring lenses, the mock-data caveat, the ancestor-preserving graph filter, cookie/bearer session auth, the materialised catalogue view. All checked out. Found and fixed one citation misattribution (hard rule: read the full paper, not the abstract): `esteban_helping_2020` was cited for "prerequisite and typical-sequence relationships," but its own proposed system uses seven criteria (ratings, grades, branch, professors, course content, knowledge area, competences) — none of them prerequisite or sequence. The only two mentions of "prerequisite"/"sequential" in the 43-page paper are in a related-work comparison table crediting two *other* papers. Dropped from the citation; `wong_sequence_2018` (genuinely about sequence-based recommendation) remains alone. Also fixed four undersized and one oversized figure caption against the Section 3 length rule. **Left open:** the Vercel+Render+Neon deployment claim (System Overview section) couldn't be re-verified from the codebase this session (only Vercel confirmed via `frontend/vercel.json`; live URL returns 403) — git history shows it was deliberately stated in a prior session (commit `cf0752a`, "state the real deployment"), so treated as settled rather than re-litigated, but noting here in case that turns out not to hold.


* 2026-08-31 — **Evaluation chapter rewritten to Moritz's editorial brief, and its 31 review comments resolved** (branch `docs/evaluation-comments`, PR). The brief was BLUF ordering, descriptive headings, no meta-discourse, no one-sentence paragraphs, confidently bounded caveats, explicit RQ3 alignment, no result spoilers in the setup sections, and strict house style.


* 2026-08-31 — **Recommendation panel measured and reported, and the codebook completed** (second commit on `docs/evaluation-comments`, merged with PR #63).


* 2026-08-31 — **Design chapter: the structural half, after Moritz decided** (same branch/PR).


* 2026-08-31 — **Design chapter: the local half of Moritz's 49 review comments applied** (branch `docs/design-comments`, PR).


* 2026-08-31 — **Implementation chapter reworked against Moritz's 25 inline review comments** (branch `docs/implementation-comments`, PR).


* 2026-08-23 — **Implementation-chapter figures rebuilt** (branch `draft/ch5-implementation-figures`), following Moritz's explicit direction...


* 2026-08-23 — **Restyled the three rebuilt figures a second pass**...


* 2026-08-23 — **Fixed real defects found in Moritz's PDF export of PR #54**...


* 2026-07-15 — **Correction:** `FEATURE-001`–`FEATURE-013` is fully defined in `context/interviews-round1/First Open Coding.docx`...


* 2026-08-25 — **Evaluation and Discussion chapters rewritten** (branch `draft/ch8-evaluation-discussion`), from a full re-analysis of the summative study. Two things changed the evidence base. (1) **Screen records re-sampled at 10 s instead of 20 s**, at native resolution, for all 14 scenario runs, producing 1,721 labelled frames (surface, panels open, per-semester lane ECTS, dashboard state, verbatim banner text). Labelling was done blind, without the transcripts or any prior analysis. (2) **The final codebook was back-applied to every participant against BOTH records** (screen + transcript), because the original coding grew session-by-session and codes coined late had never been checked against earlier sessions. **53 of 72 code frequencies changed.** Chapters are reorganised so the planning process leads and the questionnaires are demoted to supporting context, per Moritz's steer that the process (and the A-vs-B process difference) is the contribution and constraint-compliance is a note.


* 2026-08-25 — **Regenerated the whole evaluation-study `analysis/` folder from the second-pass data**...


* 2026-08-27 — **Evaluation and Discussion rebuilt at N=11.**...


* 2026-08-27 — **Figure styling rule, added at Moritz's request.**...



---

## 5. Materials — two distinct locations



* **`appendix/`** — curated content meant to appear in the submitted thesis itself (already has 3 files; only `formative-interview-plan.tex` is currently wired into `appendix.tex`).


* **`context/`** *(new, added this session)* — raw/working material used only to ground drafts, not necessarily thesis content:


* [ ] `context/proposal/`

* [ ] `context/prototype/` (Figma exports, design rationale)


* [ ] `context/interviews-round1/` (coding scheme, extracted requirements, anonymized quotes)


* [ ] `context/interviews-round2/` (protocol, anonymized transcripts/notes/coded themes — **not raw video/audio**, see privacy note below)


* [ ] `context/implementation/` (architecture notes/docs)


* [ ] `context/related-work/` (literature for positioning the thesis)


* [ ] `context/methodology/` (methodology literature and notes)





**Privacy note:** raw interview recordings should not be committed to this repo, even private. Keep them in your university's approved secure storage (e.g. the Drive folder) and bring only anonymized text extracts into `context/interviews-round2/`.

---

## 6. Session Loop (PR-based review)



1. You share/point me to relevant material in `context/`.


2. I propose a short bullet outline for the section — you approve or redirect.


3. I draft prose grounded strictly in your material, on a branch (e.g. `draft/ch5-implementation`), and open a Pull Request against `main`.


4. You review the PR in GitHub's UI — inline comments, suggested edits, approve/request changes.


5. I read the PR comments via the GitHub API, address each with new commits, reply, mark resolved.


6. Repeat 4–5 until approved.


7. I merge into `main`. Notable decisions get logged in Section 4.


8. You click "Pull GitHub changes into Overleaf" (Overleaf syncs from `main`).


9. Mark the chapter's status in Section 2.



---

## 7. GitHub Access



* Fine-grained PAT scoped to this one repo.


* Permissions: Contents (Read & write), Pull requests (Read & write).


* Rotate/regenerate periodically, especially after pasting a fresh one into chat.



---

## 8. Repository Structure (actual, as of first inspection)



```
Diploma-Thesis---Moritz-Schumacher/
├── CONTROL.md                          # this file
├── main.tex
├── bibliography.bib
├── chapters/
│   ├── introduction.tex
│   ├── needfindingwithprototype.tex
│   ├── fromthemestorequirements.tex
│   ├── design.tex
│   ├── implementation.tex
│   ├── evaluation.tex
│   └── discussion.tex
├── formalities/
│   ├── abstract.tex / kurzfassung.tex
│   ├── acknowledgements.tex / danksagung.tex
│   └── aitools.tex / kitools.tex        # AI-use disclosure — currently empty
├── appendix/
│   ├── appendix.tex
│   ├── formative-interview-plan.tex
│   ├── design requirements.tex
│   └── Traceability Matrix.tex
├── graphics/, pictures/                 # figures
└── context/                             # NEW — raw source material, see Section 5
    ├── proposal/
    ├── prototype/
    ├── interviews-round1/
    ├── interviews-round2/
    ├── implementation/
    ├── related-work/
    └── methodology/
```[cite: 1]

---

## 9. Final Reviewing Checklist (built from a full Design-chapter review pass)[cite: 1]

This checklist reflects what an actual comprehensive editorial pass on Design found, not a generic list. Several of these were real bugs, not style nits, use this as a genuine pre-submission checklist for any chapter, not just a formality.[cite: 1]

**The single most important lesson from this pass: verify, don't assume.** Nearly every serious finding below came from checking something directly (the actual codebase, the actual glossary content, the actual bibliography, git history for what changed) rather than trusting that existing text was already correct. A few concrete examples: an entire section (Compliance Engine Design) was silently missing while three other places still referenced it by label; a factual claim about filter logic (OR vs AND across dimensions) was wrong and only caught by reading the actual `GraphFilterEngine.js` source; a citation ("information asymmetry") traced to nothing anywhere in the cited paper. None of these were visible from a normal read-through; they only surfaced by checking.[cite: 1]

**Checklist:**[cite: 1]
1. **Every cross-reference actually resolves, and resolves to the right thing.** Run the repo-wide `\label`/`\ref` check (Python snippet used throughout this project) before considering any chapter done. But don't stop there: also check for references that resolve to a *label that exists* but *isn't the label you meant* (e.g. a stale label left over from a section rename or split) — this doesn't show up in a `\label`/`\ref` completeness check, it needs an actual read of what each reference is claiming.[cite: 1]
2. **If a section, subsection, or block of content was restructured (split, merged, renamed), grep the whole thesis (not just the chapter) for every old label name** before considering the restructuring complete. Renaming a label and updating only the `\label{}` itself leaves every `\ref{}` to it dangling.[cite: 1]
3. **After any large edit (yours or mine), diff-check that nothing got silently dropped.** A full section can vanish during a restructuring pass without any error, LaTeX won't complain about a missing section, only about a missing *label* if something still references it. Cross-referencing a chapter's section list against what its own internal references expect to exist is a real check worth doing.[cite: 1]
4. **Verify factual/behavioural claims about the actual system against the actual code**, not against what sounds plausible or what was previously written. This project's own `studyplanner` codebase is available; when a design claim describes how something behaves (filter combination logic, state transitions, etc.), grep the relevant source file rather than trust prose.[cite: 1]
5. **Verify every citation's claim against the actual source**, not the citation key or a remembered gist. This has caught real misattributions in this thesis: Nielsen heuristics cited for the wrong heuristic (twice), a citation ("information asymmetry") that traced to nothing in the actual paper, weak-fit citations (Shneiderman cited for a claim the paper doesn't actually make) that needed reframing to what the paper actually argues. Grep every `\cite{...}` key and confirm the entry exists in `bibliography.bib` *and* actually says what's claimed.[cite: 1]
6. **British spelling is the house style; check for American spelling systematically, not just a few obvious words.** A single review pass found 27+ instances (personalization, centralization, organize, recognize, minimize, realize, utilize, color, individualized, judgment, and more) introduced in one editing session. Search broadly (`-ize`/`-ized`/`-ization` word-boundary patterns, `color`, `judgment`, `catalog`, `favor`) rather than fixing only the instances noticed in passing, and remember to exclude LaTeX commands (`\itemize`, `\scriptsize`, etc.) from any such sweep, those aren't English words.[cite: 1]
7. **Every figure is referenced by name in the prose that motivates it**, not just floating with a caption. Check every `\label{fig:...}` has at least one `\ref{}` in running text, ideally placed at the exact sentence describing what the figure shows.[cite: 1]
8. **Watch for duplicate/redundant figures or content after a restructuring pass**, especially when one figure's scope has been expanded to also cover what an earlier, separate figure already showed (e.g. a state-machine diagram later re-drawn combined with action buttons, leaving the original standalone diagram now fully redundant).[cite: 1]
9. **A missing Alternatives paragraph is not automatically a defect.** Check whether a real alternative was genuinely weighed during design (worth documenting if so) versus there being no live alternative worth naming (leave it as Why+What only). Never invent a plausible-sounding rejected alternative just to fill a structural template, a fabricated "alternatives considered" record is a false claim about the design process.[cite: 1]
10. **Citation format for features**: `Feature~\ref{feat:XXX}, Req.~Y` from Design onward, never the bare `FEATURE-XXX` string (that bare form is only correct inside Chapter 3 itself, where it's the feature's own heading text).[cite: 1]
11. **`\emph{}` usage**: reserve for a term's first introduction, an alternative-considered label opening a rejection sentence, or genuine single-word emphasis, not routine repeated terms or whole clauses.[cite: 1]
12. **Repeated thesis-specific proper nouns (used more than a couple of times) need a glossary entry.** Check `appendix/glossary.tex` against what's actually used as a fixed system-component name; also check the glossary's own cross-references and spelling for the same issues as the chapter itself, it's thesis content too, not just a reference list exempt from the same standards.[cite: 1]
13. **After any edit, verify brace balance immediately** (`content.count('{') == content.count('}')`), not just at the end of a session. This project has a recurring tool-call bug where a malformed parameter name silently deletes content instead of replacing it; catching it on the next command is far cheaper than catching it several edits later.[cite: 1]
14. **Before pushing to any branch, check whether its PR has already been merged.** This project hit real branch-sync issues multiple times: continuing to commit to a branch after its PR merged, unaware, produces orphaned work that silently never reaches `main`. Check the PR's actual merge status (via the GitHub API, not assumption) before extending work on an existing branch, especially after any gap in the conversation.[cite: 1]

---

## 10. AI-Tools Disclosure — important, currently unresolved[cite: 1]

`main.tex` explicitly requires declaring AI tool usage as part of the statement of originality (`formalities/aitools.tex` in English, `kitools.tex` in German) — both are currently **empty**.[cite: 1]

- Our git history (commits + PR review threads) already forms a running, accurate record of exactly what I drafted versus what you wrote or edited — useful raw material when it's time to fill this in.[cite: 1]
- Worth double-checking with your advisor or TU Wien Informatics' current policy on the specific extent of permitted AI assistance for a thesis, since that shapes both how we work and what needs to go in this statement.[cite: 1]
- I'll help draft the actual disclosure text once you're ready, grounded in what we actually did rather than a generic template.[cite: 1]

```
