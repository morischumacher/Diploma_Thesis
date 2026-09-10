# Reference audit — Diploma_Thesis (main @ 0d7b874, after PRs #185 and #186)

Compiled with `latexmk -pdf`: 203 pages, 63 bibliography entries, 63 cited, 0 undefined citations, 0 BibTeX warnings, **0 overfull boxes in the bibliography**, 0 `\cite` without a preceding `~`. Rendered output below is copied from the compiled `main.pdf` (pdftotext) and `main.bbl`.

## Summary

- 🟩 50 · 🟧 11 · 🟥 0 · ⬛ 2 (of 63). First run: 38 / 17 / 2 / 6; second: 50 / 11 / 0 / 2.

- **Uncited entries: none.**

- **No claim is unsupported by its source.** The red claim (Braun & Clarke 'positivist frame') is fixed; the overstatements (Bartel ×2, Srisamutr, Greenwald, Nielsen 1993 labels, Trippel) are fixed.

- **Rendering:** Caulfield URL overflow fixed; Schulte label now [SFMMB17]; Röpke spelling unified; 'Abu Ali' braced; Denley has pages + URL.

- **Page anchors** corrected: Gotel p. 97, Munzner p. 921, Greenwald p. 316.

- **Newly verified from full text:** Nielsen 1993 (pp. 102–103), Shneiderman 1983, Parasuraman & Riley 1997, Vessey 1991, Laugwitz et al. 2008, Greenwald 1976.

- **Still ⬛:** Palmer 1992 (no PDF); Davis 1989 (the repo file is the 1987 working paper, not the cited MISQ article). Both are definitional cites and safe.

- **Remaining 🟧 items are all one thing:** the 12 keys that don't follow `surname_firstword_year` (munzner2009, nielsen1994, nielsen1993, palmer1992, schwendimann2017, shneiderman1983, greenwald1976within, parasuraman1997humans, vessey1991cognitive, caulfield2013, iso9241_11, iso9241_210). Cosmetic — rendered labels don't change. Nielsen 1993 wording and the four address fields are fixed in #186.


## Remaining fix list

1. (optional) Rename the 12 keys — `sed -i` over `bibliography.bib chapters/*.tex appendix/*.tex`, then rebuild.
2. (optional) Replace the Davis file with the 1989 MISQ article; add Palmer 1992.

Nothing else. Every entry is cited, every claim is supported by its source, every page anchor has been checked, and the build is clean (0 BibTeX warnings, 0 overfull boxes in the bibliography, 0 `\cite` without `~`).


---

# Per-reference reports


## al-badarenah_automated_2016
**Reference:** Al-Badarenah, Amer et al., 2016 / An Automated Recommender System for Course Selection / `al-badarenah_automated_2016`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `introduction.tex:6`, `relatedwork.tex:35`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{al-badarenah_automated_2016,
	title = {An {Automated} {Recommender} {System} for {Course} {Selection}},
	volume = {7},
	issn = {21565570, 2158107X},
	url = {http://thesai.org/Publications/ViewPaper?Volume=7&Issue=3&Code=ijacsa&SerialNo=23},
	doi = {10.14569/IJACSA.2016.070323},
	language = {en},
	number = {3},
	urldate = {2025-09-05},
	journal = {International Journal of Advanced Computer Science and Applications},
	author = {Al-Badarenah, Amer and Alsakran, Jamal},
	year = {2016},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[ABA16]**; reference-list entry:

> [ABA16] Amer Al-Badarenah and Jamal Alsakran. An Automated Recommender System for Course Selection. International Journal of Advanced Computer Science and Applications, 7(3), 2016.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year. No pages (IJACSA online-only; fine).

**(2) PDF Rendering & Content Check**
- In-text: [ABA16] renders correctly.
- Reference list: Label **[ABA16]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no page numbers (none exist for this venue/format).

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Collaborative/social filtering; ERS suggest courses.
  - Source Evidence: p. 1: "This paper presents a collaborative recommender ..."
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.14569/IJACSA.2016.070323 · Text Accessed: Full Text


## arnold_course_2012
**Reference:** Arnold, Kimberly E. et al., 2012 / Course Signals at Purdue: Using Learning Analytics to Increase Student Success / `arnold_course_2012`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:33`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{arnold_course_2012,
	address = {New York, NY, USA},
	title = {Course {Signals} at {Purdue}: {Using} {Learning} {Analytics} to {Increase} {Student} {Success}},
	isbn = {978-1-4503-1111-3},
	url = {https://doi.org/10.1145/2330601.2330666},
	doi = {10.1145/2330601.2330666},
	booktitle = {Proceedings of the 2nd {International} {Conference} on {Learning} {Analytics} and {Knowledge} ({LAK} '12)},
	publisher = {Association for Computing Machinery},
	author = {Arnold, Kimberly E. and Pistilli, Matthew D.},
	year = {2012},
	pages = {267--270},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[AP12]**; reference-list entry:

> [AP12] Kimberly E. Arnold and Matthew D. Pistilli. Course Signals at Purdue: Using Learning Analytics to Increase Student Success. In Proceedings of the 2nd International Conference on Learning Analytics and Knowledge (LAK ’12), pages 267–270, New York, NY, USA, 2012. Association for Computing Machinery.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [AP12] renders correctly.
- Reference list: Label **[AP12]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Instructor-triggered traffic-light risk indicator from performance, LMS engagement, prior history, characteristics; reported to improve grades and retention.
  - Source Evidence: p. 1: "A predictive student success algorithm (SSA) is run on-demand by instructors"; "relies not only on grades ... but also demographic characteristics, past academic history, and students' effort as measured by interaction with Blackboard Vista"; retention and grade outcomes reported in §3.
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/2330601.2330666 · Text Accessed: Full Text


## auvinen_stops_2014
**Reference:** Auvinen, Tapio et al., 2014 / STOPS: a graph-based study planning and curriculum development tool / `auvinen_stops_2014`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 3 occurrence(s): `discussion.tex:78`, `introduction.tex:4`, `relatedwork.tex:14`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{auvinen_stops_2014,
	title = {{STOPS}: a graph-based study planning and curriculum development tool},
	isbn = {978-1-4503-3065-7},
	shorttitle = {{STOPS}},
	url = {https://dl.acm.org/doi/10.1145/2674683.2674689},
	doi = {10.1145/2674683.2674689},
	language = {en},
	urldate = {2025-08-07},
	booktitle = {Koli {Calling} '14: 14th {Koli} {Calling} {International} {Conference} on {Computing} {Education} {Research}},
	publisher = {Association for Computing Machinery},
	author = {Auvinen, Tapio and Paavola, Juha and Hartikainen, Juha},
	year = {2014},
	pages = {25--34},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[APH14]**; reference-list entry:

> [APH14] Tapio Auvinen, Juha Paavola, and Juha Hartikainen. STOPS: a graph-based study planning and curriculum development tool. In Koli Calling ’14: 14th Koli Calling International Conference on Computing Education Research, pages 25–34. Association for Computing Machinery, 2014.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [APH14] renders correctly.
- Reference list: Label **[APH14]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Models the curriculum as a graph of learning outcomes; courses decomposed into outcomes with prerequisite dependencies; programmes as goals; serves students and staff.
  - Source Evidence: p. 1: "the curriculum is modeled as a graph of learning outcomes ... prerequisite dependencies are defined between the outcomes ... programmes are defined as goals ... the staff to maintain and develop course contents".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/2674683.2674689 · Text Accessed: Full Text


## arndt_ki-basierte_2023
**Reference:** Arndt, Jonas et al., 2023 / KI-basierte Studienplanung unter Berücksichtigung der Anforderungen einer heterogenen Studierendenschaft / `arndt_ki-basierte_2023`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:35`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{arndt_ki-basierte_2023,
	title = {{KI}-basierte {Studienplanung} unter {Berücksichtigung} der {Anforderungen} einer heterogenen {Studierendenschaft}},
	url = {https://dl.gi.de/handle/20.500.12116/43315},
	doi = {10.18420/wsdelfi2023-52},
	abstract = {Es wird ein auf symbolischer KI basierendes System zur individuellen Studienplanung mit besonderer Berücksichtigung von Studierenden mit Beeinträchtigung präsentiert. Ausgewählte Assistenzfunktionen werden erläutert, die im nächsten Schritt prototypisch implementiert und evaluiert werden sollen.},
	language = {de},
	urldate = {2025-09-05},
	booktitle = {Workshops der 21. {Fachtagung} {Bildungstechnologien} ({DELFI})},
	author = {Arndt, Jonas and Vock, Magdalena and Lucke, Ulrike},
	year = {2023},
	keywords = {Heterogene Studierendenschaft, Individuelle Studienplanung, Symbolische KI},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[AVL23]**; reference-list entry:

> [AVL23] Jonas Arndt, Magdalena Vock, and Ulrike Lucke. KI-basierte Studienpla- nung unter Berücksichtigung der Anforderungen einer heterogenen Studieren- denschaft. In Workshops der 21. Fachtagung Bildungstechnologien (DELFI), 2023.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [AVL23] renders correctly.
- Reference list: Label **[AVL23]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no page numbers (none exist for this venue/format).

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Proposal to plan under explicit curriculum rules with answer-set programming.
  - Source Evidence: Paper: 'Answer Set Programming (ASP)' named as the symbolic-AI basis; abstract: "ein auf symbolischer KI basierendes System ... prototypisch implementiert und evaluiert werden sollen".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.18420/wsdelfi2023-52 · Text Accessed: Full Text


## braun_thematic_2022
**Reference:** Braun, Virginia et al., 2022 / Thematic Analysis: A Practical Guide / `braun_thematic_2022`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 18 occurrence(s): `discussion.tex:107`[pp.~236, 241], `evaluation.tex:118`, `methodology.tex:120`[pp.~236, 241], `needfindingwithprototype.tex:82`[pp.~227--232], `needfindingwithprototype.tex:82`[pp.~235--236], `needfindingwithprototype.tex:84`[pp.~35--36, 77--78], `needfindingwithprototype.tex:84`[pp.~237--238], `needfindingwithprototype.tex:84`[pp.~236, 248], `needfindingwithprototype.tex:84`[p.~242], `needfindingwithprototype.tex:86`[pp.~244--245], `needfindingwithprototype.tex:88`[p.~10], `needfindingwithprototype.tex:88`[p.~36], `needfindingwithprototype.tex:95`[pp.~42--49], `needfindingwithprototype.tex:95`[p.~35], `needfindingwithprototype.tex:100`[pp.~51--71], `needfindingwithprototype.tex:127`[pp.~35--36, 97--111], `needfindingwithprototype.tex:127`[pp.~35--36], `needfindingwithprototype.tex:132`[p.~141]
- Key Match: Yes

- BibTeX Source:

```bibtex
@book{braun_thematic_2022,
	address = {London},
	title = {Thematic {Analysis}: {A} {Practical} {Guide}},
	shorttitle = {Thematic {Analysis}},
	language = {en},
	publisher = {SAGE Publications},
	author = {Braun, Virginia and Clarke, Victoria},
	year = {2022},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[BC22]**; reference-list entry:

> [BC22] Virginia Braun and Victoria Clarke. Thematic Analysis: A Practical Guide. SAGE Publications, London, 2022.

**(1) BibTeX Data Check:** Required fields present (@book). Key correct.

**(2) PDF Rendering & Content Check**
- In-text: [BC22] renders correctly; after commit 67b62ec every one of the 18 cites has `~` and sits before the full stop.
- Reference list: Label **[BC22]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no page numbers (none exist for this venue/format).

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: TA is a family of approaches (pp. 227–232); three types (pp. 235–236).
  - Source Evidence: p. 235: "These three clusters are: Reflexive TA ... Coding reliability TA ... Codebook TA".
  - Validation: Yes.

- Claim 2
  - Thesis Claim: Reflexive TA develops themes as shared-meaning patterns (pp. 35–36, 77–78).
  - Source Evidence: p. 77: "a theme has to capture a wide range of data that are united by ... a shared idea ... 'shared meaning'".
  - Validation: Yes.

- Claim 3
  - Thesis Claim: Coding-reliability TA treats subjectivity as a threat; multiple coders, inter-coder agreement (pp. 237–238).
  - Source Evidence: p. 236 Table 8.3: subjectivity "A 'risk' ... Needs to be 'controlled'"; p. 237: "culminates in a measure of 'coding reliability'".
  - Validation: Yes.

- Claim 4
  - Thesis Claim: Not recommended for codebook TA; usable "by single researchers or teams" (pp. 236, 248).
  - Source Evidence: p. 236: "Measures of inter-coder reliability not recommended." p. 248: "Can be used by single researchers or teams."
  - Validation: Yes.

- Claim 5
  - Thesis Claim: Codebook TA combines Big Q qualitative values, *meaning a fully qualitative research paradigm*, with more structured coding (p. 242) — wording after the fix.
  - Source Evidence: p. 242 ALERT: "Codebook approaches combine Big Q qualitative research values with a more structured approach to coding and early theme development."
  - Validation: Yes (the earlier 'positivist frame' gloss has been removed).

- Claim 6
  - Thesis Claim: Framework analysis classified as codebook (pp. 244–245).
  - Source Evidence: p. 242 lists framework analysis among codebook approaches.
  - Validation: Yes.

- Claim 7
  - Thesis Claim: "robust process guidelines, not rigid rules" (p. 10); "progressive but recursive" (p. 36).
  - Source Evidence: Both verbatim on the cited pages.
  - Validation: Yes.

- Claim 8
  - Thesis Claim: Familiarisation (pp. 42–49); coding identifies segments relevant to the RQ (p. 35); codes as analytic labels (pp. 51–71); theme review (pp. 35–36, 97–111).
  - Source Evidence: p. 35 Box 2.1; Chapter 3; p. 97 Phase four.
  - Validation: Yes.

- Claim 9
  - Thesis Claim: "...not determined by how many people said it" (p. 141).
  - Source Evidence: p. 141, verbatim.
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: SAGE, ISBN 9781473953239 · Text Accessed: Full Text


## bhumichitr_recommender_2017
**Reference:** Bhumichitr, Kiratijuta et al., 2017 / Recommender Systems for university elective course recommendation / `bhumichitr_recommender_2017`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 3 occurrence(s): `implementation.tex:238`, `introduction.tex:6`, `relatedwork.tex:35`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{bhumichitr_recommender_2017,
	address = {Nakhon Si Thammarat, Thailand},
	title = {Recommender {Systems} for university elective course recommendation},
	isbn = {978-1-5090-4834-2},
	url = {http://ieeexplore.ieee.org/document/8025933/},
	doi = {10.1109/JCSSE.2017.8025933},
	urldate = {2025-09-05},
	booktitle = {14th {International} {Joint} {Conference} on {Computer} {Science} and {Software} {Engineering} ({JCSSE})},
	publisher = {IEEE},
	author = {Bhumichitr, Kiratijuta and Channarukul, Songsak and Saejiem, Nattachai and Jiamthapthaksin, Rachsuda and Nongpong, Kwankamol},
	year = {2017},
	pages = {1--5},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[BCS+17]**; reference-list entry:

> [BCS+17] Kiratijuta Bhumichitr, Songsak Channarukul, Nattachai Saejiem, Rachsuda Jiamthapthaksin, and Kwankamol Nongpong. Recommender Systems for university elective course recommendation. In 14th International Joint Conference on Computer Science and Software Engineering (JCSSE), pages 1–5, Nakhon Si Thammarat, Thailand, 2017. IEEE.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [BCS+17] renders correctly; address now 'Nakhon Si Thammarat, Thailand'.
- Reference list: Label **[BCS+17]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Collaborative filtering (related work and implementation).
  - Source Evidence: p. 1: "collaborative filtering algorithm using Pearson Correlation Coefficient and Alternating Least Squares".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/JCSSE.2017.8025933 · Text Accessed: Full Text


## bercovitz_courserank_2009
**Reference:** Bercovitz, Benjamin et al., 2009 / CourseRank: a social system for course planning / `bercovitz_courserank_2009`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `relatedwork.tex:21`, `relatedwork.tex:35`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{bercovitz_courserank_2009,
	title = {{CourseRank}: a social system for course planning},
	isbn = {978-1-60558-551-2},
	url = {https://dl.acm.org/doi/10.1145/1559845.1559994},
	doi = {10.1145/1559845.1559994},
	language = {en},
	urldate = {2025-10-14},
	booktitle = {2009 {ACM} {SIGMOD} {International} {Conference} on {Management} of data},
	publisher = {Association for Computing Machinery},
	author = {Bercovitz, Benjamin and Kaliszan, Filip and Koutrika, Georgia and Liou, Henry and Mohammadi Zadeh, Zahra and Garcia-Molina, Hector},
	year = {2009},
	pages = {1107--1110},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[BKK+09]**; reference-list entry:

> [BKK+09] Benjamin Bercovitz, Filip Kaliszan, Georgia Koutrika, Henry Liou, Zahra Mohammadi Zadeh, and Hector Garcia-Molina. CourseRank: a social system for course planning. In 2009 ACM SIGMOD International Confer- ence on Management of data, pages 1107–1110. Association for Computing Machinery, 2009.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [BKK+09] renders correctly.
- Reference list: Label **[BKK+09]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Combines official university data with user-contributed content; Planner detects schedule conflicts; Req Tracker checks major requirements; social recommender.
  - Source Evidence: p. 1: "user-contributed information (e.g., course rankings, comments...)"; "Planner ... checks for schedule conflicts"; p. 2: "checks if requirements for a major have been met (Req Tracker)".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/1559845.1559994 · Text Accessed: Full Text


## bartel_design_2024
**Reference:** Bartel, Lena et al., 2024 / Design Principles for a Study Planning Assistant in Higher Education / `bartel_design_2024`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 16 occurrence(s): `design.tex:15`, `design.tex:19`, `design.tex:97`, `design.tex:115`, `design.tex:360`, `design.tex:673`, `design.tex:805`, `design.tex:833`, `design.tex:839`, `design.tex:865`, `design.tex:872`, `design.tex:893`, `design.tex:897`, `design.tex:982`, `discussion.tex:76`, `relatedwork.tex:48`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{bartel_design_2024,
	title = {Design {Principles} for a {Study} {Planning} {Assistant} in {Higher} {Education}},
	isbn = {979-8-4007-0434-5},
	url = {https://doi.org/10.1145/3627508.3638327},
	doi = {10.1145/3627508.3638327},
	abstract = {Digital study assistants (DSA) aim to support the challenging tasks of searching for relevant information and organizing this data for individual study planning. Although such systems are characterized by complex process flows, their user experience (UX) has rarely been examined adequately. This research comprehensively analyzes the UX of such a system at the University of Bamberg, which includes short-term planning for one semester as well as the distinctive feature of long-term planning beyond one semester. Via remote usability testing including an online questionnaire and involving 26 participants, this study explores students’ interactions with the system and evaluates the impact of the system design on the UX, identifying strengths and weaknesses. The study has revealed that participants faced major challenges related to complex processes resulting from the lack of functional and terminological differentiation between short- and long-term study planning for users. In addition, certain features, including extended search options, were hidden and could not be found immediately. Derived from these findings, we present nine design principles to guide the development of effective DSA and similar support systems.},
	urldate = {2025-08-20},
	booktitle = {Conference on {Human} {Information} {Interaction} and {Retrieval}},
	publisher = {Association for Computing Machinery},
	author = {Bartel, Lena and Ochs, Michaela and Hirmer, Tobias and Henrich, Andreas},
	year = {2024},
	pages = {243--253},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[BOHH24]**; reference-list entry:

> [BOHH24] Lena Bartel, Michaela Ochs, Tobias Hirmer, and Andreas Henrich. Design Principles for a Study Planning Assistant in Higher Education. In Conference on Human Information Interaction and Retrieval, pages 243–253. Association for Computing Machinery, 2024.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [BOHH24] renders correctly; all 16 cites have `~`. (A few 'Bartel et al.~\cite{} principle' still lack the possessive — style only.)
- Reference list: Label **[BOHH24]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Nine design principles; (1) university identifiers; (3) support during planning difficulties; (4) user-centred/programme-specific personalisation; (5) clear presentation incl. course names with module affiliation; (6) centralisation; (9) clearly comprehensive content, tool guide for first-time use.
  - Source Evidence: All quoted verbatim from §5 of the paper.
  - Validation: Yes.

- Claim 2
  - Thesis Claim: Participants customised their target credit points per semester (design.tex l. 897, after fix).
  - Source Evidence: Fig. 5, E1: "Customization of target credit points per semester".
  - Validation: Yes.

- Claim 3
  - Thesis Claim: Principle of clearly presenting curriculum information, *extended here* to structural dependencies (l. 982, after fix).
  - Source Evidence: Principle 5; the extension is now marked as the thesis's own.
  - Validation: Yes.

- Claim 4
  - Thesis Claim: Same two friction points: terminology and hidden filter controls (discussion.tex l. 76).
  - Source Evidence: Abstract: "lack of functional and terminological differentiation"; "extended search options were hidden".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/3627508.3638327 · Text Accessed: Full Text


## bodily_review_2017
**Reference:** Bodily, Robert et al., 2017 / Review of Research on Student-Facing Learning Analytics Dashboards and Educational Recommender Systems / `bodily_review_2017`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 3 occurrence(s): `discussion.tex:84`, `introduction.tex:6`, `relatedwork.tex:39`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{bodily_review_2017,
	title = {Review of {Research} on {Student}-{Facing} {Learning} {Analytics} {Dashboards} and {Educational} {Recommender} {Systems}},
	volume = {10},
	url = {https://doi.org/10.1109/TLT.2017.2740172},
	doi = {10.1109/TLT.2017.2740172},
	number = {4},
	journal = {IEEE Transactions on Learning Technologies},
	author = {Bodily, Robert and Verbert, Katrien},
	year = {2017},
	pages = {405--418},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[BV17]**; reference-list entry:

> [BV17] Robert Bodily and Katrien Verbert. Review of Research on Student-Facing Learning Analytics Dashboards and Educational Recommender Systems. IEEE Transactions on Learning Technologies, 10(4):405–418, 2017.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [BV17] renders correctly.
- Reference list: Label **[BV17]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Of 93 articles: 15% both report visually and recommend; 9% enhanced visualisation with recommendations; 6% visualisation with recommendations and data mining.
  - Source Evidence: p. 1: "93 articles were included"; Table (p. 6): "Enhanced visualization with recommendations 8 9%", "Visualization with recommendations and data mining 6 6%" → 14/93 = 15%.
  - Validation: Yes — note 15% is the sum of the other two; phrase as a total.

- Claim 2
  - Thesis Claim: Call for interfaces that address both what to do and why.
  - Source Evidence: p. 8: "future systems should address both what to tell the students to do in recommendations and why students should act on the information".
  - Validation: Yes.

- Claim 3
  - Thesis Claim: Both are almost always built separately.
  - Source Evidence: Same table: only 15% combine visualisation and recommendation.
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/TLT.2017.2740172 · Text Accessed: Full Text


## caulfield2013
**Reference:** Caulfield, Michael, 2013 / A Simple, Less Mathematical Way to Understand the Course Signals Issue / `caulfield2013`

**Traffic Light Indicator:** 🟧 Orange

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `discussion.tex:82`, `relatedwork.tex:33`
- Key Match: Yes

- BibTeX Source:

```bibtex
@misc{caulfield2013,
	author = {Caulfield, Michael},
	title  = {A Simple, Less Mathematical Way to Understand the Course Signals Issue},
	year   = {2013},
	howpublished = {\url{https://hapgood.us/2013/09/26/a-simple-less-mathematical-way-to-understand-the-course-signals-issue/}},
	note   = {Blog post}
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Cau13]**; reference-list entry:

> [Cau13] Michael Caulfield. A simple, less mathematical way to understand the course signals issue. https://hapgood.us/2013/09/26/a- simple-less-mathematical-way-to-understand-the-course- signals-issue/, 2013. Blog post.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `caulfield_simple_2013`); all required fields present. URL updated to https.

**(2) PDF Rendering & Content Check**
- In-text: FIXED: with `\PassOptionsToPackage{hyphens}{url}` the URL now breaks over three lines inside the margin; no overfull box remains for the bibliography.
- Reference list: Label **[Cau13]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no page numbers (none exist for this venue/format).

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Retention result not controlled for number of courses; causality may be reversed.
  - Source Evidence: Post: "it's possible the causality is reversed: students are taking more Course Signals courses because they persist, rather than persisting because they are taking more Signals courses."
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Search · Source Links: https://hapgood.us/2013/09/26/a-simple-less-mathematical-way-to-understand-the-course-signals-issue · Text Accessed: Full Text

**Recommendation:** Key name only.


## chaturapruek_how_2018
**Reference:** Chaturapruek, Sorathan et al., 2018 / How a data-driven course planning tool affects college students' GPA: evidence from two field experiments / `chaturapruek_how_2018`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:33`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{chaturapruek_how_2018,
	title = {How a data-driven course planning tool affects college students' {GPA}: evidence from two field experiments},
	isbn = {978-1-4503-5886-6},
	shorttitle = {How a data-driven course planning tool affects college students' {GPA}},
	url = {https://dl.acm.org/doi/10.1145/3231644.3231668},
	doi = {10.1145/3231644.3231668},
	language = {en},
	urldate = {2025-09-05},
	booktitle = {L@{S} '18: {Fifth} (2018) {ACM} {Conference} on {Learning} @ {Scale}},
	publisher = {Association for Computing Machinery},
	author = {Chaturapruek, Sorathan and Dee, Thomas S. and Johari, Ramesh and Kizilcec, René F. and Stevens, Mitchell L.},
	year = {2018},
	pages = {1--10},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[CDJ+18]**; reference-list entry:

> [CDJ+18] Sorathan Chaturapruek, Thomas S. Dee, Ramesh Johari, René F. Kizilcec, and Mitchell L. Stevens. How a data-driven course planning tool affects college students’ GPA: evidence from two field experiments. In L@S ’18: Fifth (2018) ACM Conference on Learning @ Scale, pages 1–10. Association for Computing Machinery, 2018.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [CDJ+18] renders correctly.
- Reference list: Label **[CDJ+18]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Carta shows transcript-derived grade distributions and course evaluations; randomised encouragement; 80% vs 52% usage.
  - Source Evidence: p. 5: "(80% vs. 52%, χ² = 534.7, p < 0.001)"; p. 1: "course evaluations, and grade distributions derived from official transcripts".
  - Validation: Yes.

- Claim 2
  - Thesis Claim: Instrumenting for use, GPA lowered by 0.28 SD; encouragement alone 0.05.
  - Source Evidence: p. 5: "Using 2SLS, we find that Carta usage reduced GPA by 0.28 standard deviations"; "the encouragement significantly reduced GPA by 0.05 standard deviations".
  - Validation: Yes.

- Claim 3
  - Thesis Claim: Attributed to within-course behaviour, not portfolio; mechanism not identified.
  - Source Evidence: p. 1: "these effects are not due to changes in the portfolio of courses ... but rather by changes to their behavior within courses"; p. 2: "we are led to consider potential mechanisms".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/3231644.3231668 · Text Accessed: Full Text


## chun_planglow_2025
**Reference:** Chun, Jiwon et al., 2025 / PlanGlow: Personalized Study Planning with an Explainable and Controllable LLM-Driven System / `chun_planglow_2025`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:36`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{chun_planglow_2025,
	title = {{PlanGlow}: {Personalized} {Study} {Planning} with an {Explainable} and {Controllable} {LLM}-{Driven} {System}},
	isbn = {979-8-4007-1291-3},
	shorttitle = {{PlanGlow}},
	url = {https://dl.acm.org/doi/10.1145/3698205.3729541},
	doi = {10.1145/3698205.3729541},
	language = {en},
	urldate = {2025-10-14},
	booktitle = {L@{S} '25: {Twelfth} {ACM} {Conference} on {Learning} @ {Scale}},
	publisher = {Association for Computing Machinery},
	author = {Chun, Jiwon and Zhao, Yankun and Chen, Hanlin and Xia, Meng},
	year = {2025},
	pages = {116--127},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[CZCX25]**; reference-list entry:

> [CZCX25] Jiwon Chun, Yankun Zhao, Hanlin Chen, and Meng Xia. PlanGlow: Person- alized Study Planning with an Explainable and Controllable LLM-Driven System. In L@S ’25: Twelfth ACM Conference on Learning @ Scale, pages 116–127. Association for Computing Machinery, 2025.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [CZCX25] renders correctly.
- Reference list: Label **[CZCX25]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Explainable and controllable LLM-driven planning system.
  - Source Evidence: Title.
  - Validation: Yes (title-level).

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/3698205.3729541 · Text Accessed: Full Text


## davis_perceived_1989
**Reference:** Davis, Fred D., 1989 / Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology / `davis_perceived_1989`

**Traffic Light Indicator:** ⬛ Black

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `evaluation-appendix.tex:52`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{davis_perceived_1989,
  author  = {Davis, Fred D.},
  title   = {Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology},
  journal = {MIS Quarterly},
  volume  = {13},
  number  = {3},
  pages   = {319--340},
  year    = {1989},
  doi     = {10.2307/249008}
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Dav89]**; reference-list entry:

> [Dav89] Fred D. Davis. Perceived usefulness, perceived ease of use, and user accep- tance of information technology. MIS Quarterly, 13(3):319–340, 1989.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [Dav89] renders correctly.
- Reference list: Label **[Dav89]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: TAM: perceived usefulness and perceived ease of use.
  - Source Evidence: The file added to the repo is Davis's 1987 Michigan working paper #529 ('User Acceptance of Information Systems: The Technology Acceptance Model'), not the 1989 MIS Quarterly article the entry cites. The claim holds for both, but the cited text was not accessed.
  - Validation: Yes at abstract level.

**Access Level & Verification Sources:** Source Location: Repo holds a different Davis paper · Source Links: https://doi.org/10.2307/249008 · Text Accessed: Abstract Only

**Recommendation:** Either add the 1989 MISQ PDF or leave as is — the definitional claim is safe.


## dexter_ontology-based_2009
**Reference:** Dexter, Hilary et al., 2009 / An Ontology-Based Curriculum Knowledgebase for Managing Complexity and Change / `dexter_ontology-based_2009`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:12`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{dexter_ontology-based_2009,
	address = {Riga, Latvia},
	title = {An {Ontology}-{Based} {Curriculum} {Knowledgebase} for {Managing} {Complexity} and {Change}},
	url = {http://ieeexplore.ieee.org/document/5194185/},
	doi = {10.1109/ICALT.2009.85},
	urldate = {2025-08-20},
	booktitle = {2009 {Ninth} {IEEE} {International} {Conference} on {Advanced} {Learning} {Technologies}},
	publisher = {IEEE},
	author = {Dexter, Hilary and Davies, Ioan},
	year = {2009},
	pages = {136--140},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[DD09]**; reference-list entry:

> [DD09] Hilary Dexter and Ioan Davies. An Ontology-Based Curriculum Knowl- edgebase for Managing Complexity and Change. In 2009 Ninth IEEE International Conference on Advanced Learning Technologies, pages 136– 140, Riga, Latvia, 2009. IEEE.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [DD09] renders correctly.
- Reference list: Label **[DD09]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Ontology-based curriculum knowledgebase for managing complexity and change.
  - Source Evidence: Title.
  - Validation: Yes (title-level).

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/ICALT.2009.85 · Text Accessed: Full Text


## denley_austin_2012
**Reference:** Denley, Tristan, 2012 / Austin Peay State University: Degree Compass / `denley_austin_2012`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:36`
- Key Match: Yes

- BibTeX Source:

```bibtex
@incollection{denley_austin_2012,
	address = {Boulder, CO},
	pages = {263--267},
	url = {https://www.educause.edu/~/media/files/library/2012/5/pub7203cs3-pdf.pdf},
	title = {Austin {Peay} {State} {University}: {Degree} {Compass}},
	booktitle = {Game {Changers}: {Education} and {Information} {Technologies}},
	publisher = {EDUCAUSE},
	author = {Denley, Tristan},
	editor = {Oblinger, Diana G.},
	year = {2012},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Den12]**; reference-list entry:

> [Den12] Tristan Denley. Austin Peay State University: Degree Compass. In Diana G. Oblinger, editor, Game Changers: Education and Information Technologies, pages 263–267. EDUCAUSE, Boulder, CO, 2012.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year. Pages and URL now present.

**(2) PDF Rendering & Content Check**
- In-text: [Den12] renders correctly.
- Reference list: Label **[Den12]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Ranks courses by advancement of remaining requirements and centrality, then overlays predicted grade.
  - Source Evidence: EDUCAUSE chapter p. 264: "That ranking is then overlaid with a model that predicts ..."
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Search · Source Links: https://www.educause.edu/~/media/files/library/2012/5/pub7203cs3-pdf.pdf · Text Accessed: Full Text


## esteban_helping_2020
**Reference:** Esteban, A. et al., 2020 / Helping university students to choose elective courses by using a hybrid multi-criteria recommendation system with genetic optimization / `esteban_helping_2020`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `introduction.tex:6`, `relatedwork.tex:35`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{esteban_helping_2020,
	title = {Helping university students to choose elective courses by using a hybrid multi-criteria recommendation system with genetic optimization},
	volume = {194},
	url = {https://linkinghub.elsevier.com/retrieve/pii/S0950705119306306},
	doi = {10.1016/j.knosys.2019.105385},
	language = {en},
	urldate = {2025-09-05},
	journal = {Knowledge-Based Systems},
	author = {Esteban, A. and Zafra, A. and Romero, C.},
	year = {2020},
	pages = {105385},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[EZR20]**; reference-list entry:

> [EZR20] A. Esteban, A. Zafra, and C. Romero. Helping university students to choose elective courses by using a hybrid multi-criteria recommendation system with genetic optimization. Knowledge-Based Systems, 194:105385, 2020.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [EZR20] renders correctly.
- Reference list: Label **[EZR20]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; author(s) given with initials only, as published — no full names available.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Content-based and hybrid filtering; ERS suggest courses.
  - Source Evidence: p. 1: "a hybrid RS that combines Collaborative Filtering (CF) and Content-based Filtering (CBF)".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1016/j.knosys.2019.105385 · Text Accessed: Full Text


## gotel_analysis_1994
**Reference:** Gotel, O.C.Z. et al., 1994 / An analysis of the requirements traceability problem / `gotel_analysis_1994`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `needfindingwithprototype.tex:160`[p.~97]
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{gotel_analysis_1994,
	address = {Colorado Springs, CO, USA},
	title = {An analysis of the requirements traceability problem},
	isbn = {978-0-8186-5480-0},
	url = {http://ieeexplore.ieee.org/document/292398/},
	doi = {10.1109/ICRE.1994.292398},
	urldate = {2026-04-09},
	booktitle = {Proceedings of {IEEE} {International} {Conference} on {Requirements} {Engineering}},
	publisher = {IEEE Comput. Soc. Press},
	author = {Gotel, O.C.Z. and Finkelstein, Anthony C. W.},
	year = {1994},
	pages = {94--101},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[GF94]**; reference-list entry:

> [GF94] O.C.Z. Gotel and Anthony C. W. Finkelstein. An analysis of the requirements traceability problem. In Proceedings of IEEE International Conference on Requirements Engineering, pages 94–101, Colorado Springs, CO, USA, 1994. IEEE Comput. Soc. Press.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [GF94] renders correctly; page anchor now `[p.~97]`.
- Reference list: Label **[GF94]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; author(s) given with initials only, as published — no full names available; publisher abbreviated as in the IEEE record (optionally expand).

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Pre-requirements-specification traceability (p. 97).
  - Source Evidence: §5.2, p. 97: "Pre-RS traceability, which is concerned with those aspects of a requirement's life prior to its inclusion in the RS".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/ICRE.1994.292398 · Text Accessed: Full Text


## gale_using_2013
**Reference:** Gale, Nicola K et al., 2013 / Using the framework method for the analysis of qualitative data in multi-disciplinary health research / `gale_using_2013`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `needfindingwithprototype.tex:86`, `needfindingwithprototype.tex:118`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{gale_using_2013,
	title = {Using the framework method for the analysis of qualitative data in multi-disciplinary health research},
	volume = {13},
	issn = {1471-2288},
	url = {https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/1471-2288-13-117},
	doi = {10.1186/1471-2288-13-117},
	abstract = {Abstract
            
              Background
              The Framework Method is becoming an increasingly popular approach to the management and analysis of qualitative data in health research. However, there is confusion about its potential application and limitations.
            
            
              Discussion
              The article discusses when it is appropriate to adopt the Framework Method and explains the procedure for using it in multi-disciplinary health research teams, or those that involve clinicians, patients and lay people. The stages of the method are illustrated using examples from a published study.
            
            
              Summary
              Used effectively, with the leadership of an experienced qualitative researcher, the Framework Method is a systematic and flexible approach to analysing qualitative data and is appropriate for use in research teams even where not all members have previous experience of conducting qualitative research.},
	language = {en},
	number = {1},
	urldate = {2026-04-08},
	journal = {BMC Medical Research Methodology},
	author = {Gale, Nicola K and Heath, Gemma and Cameron, Elaine and Rashid, Sabina and Redwood, Sabi},
	month = sep,
	year = {2013},
	pages = {117},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[GHC+13]**; reference-list entry:

> [GHC+13] Nicola K Gale, Gemma Heath, Elaine Cameron, Sabina Rashid, and Sabi Redwood. Using the framework method for the analysis of qualitative data in multi-disciplinary health research. BMC Medical Research Methodology, 13(1):117, September 2013.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [GHC+13] renders correctly; l. 118 is now a complete sentence with `~\cite`.
- Reference list: Label **[GHC+13]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Charting summarises data by category into a matrix; emphasis on transparent charting.
  - Source Evidence: p. 2: "Charting: Entering summarized data into the Framework Method matrix".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1186/1471-2288-13-117 · Text Accessed: Full Text


## greenwald1976within
**Reference:** Greenwald, Anthony G., 1976 / Within-subjects designs: To use or not to use? / `greenwald1976within`

**Traffic Light Indicator:** 🟧 Orange

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `evaluation.tex:87`[p.~316], `evaluation.tex:87`[pp.~316--318]
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{greenwald1976within,
	title = {Within-subjects designs: {To} use or not to use?},
	volume = {83},
	issn = {0033-2909, 1939-1455},
	shorttitle = {Within-subjects designs},
	url = {https://doi.org/10.1037/0033-2909.83.2.314},
	doi = {10.1037/0033-2909.83.2.314},
	number = {2},
	journal = {Psychological Bulletin},
	author = {Greenwald, Anthony G.},
	year = {1976},
	pages = {314--320},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Gre76]**; reference-list entry:

> [Gre76] Anthony G. Greenwald. Within-subjects designs: To use or not to use? Psychological Bulletin, 83(2):314–320, 1976.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `greenwald_within-subjects_1976`); all required fields present.

**(2) PDF Rendering & Content Check**
- In-text: [Gre76] renders correctly; anchor now `[p.~316]`; wording softened to 'repeated-measures design ... sequence then held constant'.
- Reference list: Label **[Gre76]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Counterbalancing does not remove a treatment×practice interaction (p. 316).
  - Source Evidence: p. 316: "the observed treatment effects may be mixed inseparably with treatment-practice interactions".
  - Validation: Yes.

- Claim 2
  - Thesis Claim: A repeated-measures design is appropriate where learning is the object of study (pp. 316–318).
  - Source Evidence: pp. 316–317: "the practice effect is often intended to be the direct object of study itself—in learning experiments. Here, within-subjects designs will often be appropriate".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Search · Source Links: https://faculty.washington.edu/agg/pdf/Gwald_PsychBull_1976.OCR.pdf · Text Accessed: Full Text

**Recommendation:** Key name only.


## govaerts_student_2012
**Reference:** Govaerts, Sten et al., 2012 / The Student Activity Meter for Awareness and Self-Reflection / `govaerts_student_2012`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:32`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{govaerts_student_2012,
	address = {New York, NY, USA},
	title = {The {Student} {Activity} {Meter} for {Awareness} and {Self}-{Reflection}},
	isbn = {978-1-4503-1016-1},
	url = {https://doi.org/10.1145/2212776.2212860},
	doi = {10.1145/2212776.2212860},
	booktitle = {{CHI} '12 {Extended} {Abstracts} on {Human} {Factors} in {Computing} {Systems}},
	publisher = {Association for Computing Machinery},
	author = {Govaerts, Sten and Verbert, Katrien and Duval, Erik and Pardo, Abelardo},
	year = {2012},
	pages = {869--884},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[GVDP12]**; reference-list entry:

> [GVDP12] Sten Govaerts, Katrien Verbert, Erik Duval, and Abelardo Pardo. The Student Activity Meter for Awareness and Self-Reflection. In CHI ’12 Extended Abstracts on Human Factors in Computing Systems, pages 869– 884, New York, NY, USA, 2012. Association for Computing Machinery.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [GVDP12] renders correctly.
- Reference list: Label **[GVDP12]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Activity-meter visualisations comparing time investment and resource use against class benchmarks.
  - Source Evidence: p. 1: "awareness of time spent and resource use" (SAM visualises against the class).
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/2212776.2212860 · Text Accessed: Full Text


## holman_gradecraft_2013
**Reference:** Holman, Caitlin et al., 2013 / GradeCraft: What Can We Learn From a Game-Inspired Learning Management System? / `holman_gradecraft_2013`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:32`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{holman_gradecraft_2013,
	address = {New York, NY, USA},
	title = {{GradeCraft}: {What} {Can} {We} {Learn} {From} a {Game}-{Inspired} {Learning} {Management} {System}?},
	isbn = {978-1-4503-1785-6},
	url = {https://doi.org/10.1145/2460296.2460350},
	doi = {10.1145/2460296.2460350},
	booktitle = {Proceedings of the 3rd {International} {Conference} on {Learning} {Analytics} and {Knowledge} ({LAK} '13)},
	publisher = {Association for Computing Machinery},
	author = {Holman, Caitlin and Aguilar, Stephen and Fishman, Barry},
	year = {2013},
	pages = {260--264},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[HAF13]**; reference-list entry:

> [HAF13] Caitlin Holman, Stephen Aguilar, and Barry Fishman. GradeCraft: What Can We Learn From a Game-Inspired Learning Management System? In Proceedings of the 3rd International Conference on Learning Analytics and Knowledge (LAK ’13), pages 260–264, New York, NY, USA, 2013. Association for Computing Machinery.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [HAF13] renders correctly.
- Reference list: Label **[HAF13]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Points-based game-inspired grade planning; predictor lets students choose assignments and see a simulated final grade.
  - Source Evidence: p. 3: "Students ... are able to select which assignments they will do and how much of their grade those assignments will be worth ... We built a grade predictor".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/2460296.2460350 · Text Accessed: Full Text


## huberth_computer-tailored_2015
**Reference:** Huberth, Madeline et al., 2015 / Computer-Tailored Student Support in Introductory Physics / `huberth_computer-tailored_2015`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:32`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{huberth_computer-tailored_2015,
	title = {Computer-{Tailored} {Student} {Support} in {Introductory} {Physics}},
	volume = {10},
	url = {https://doi.org/10.1371/journal.pone.0137001},
	doi = {10.1371/journal.pone.0137001},
	number = {9},
	journal = {PLoS ONE},
	author = {Huberth, Madeline and Chen, Patricia and Tritz, Jared and McKay, Timothy A.},
	year = {2015},
	pages = {e0137001},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[HCTM15]**; reference-list entry:

> [HCTM15] Madeline Huberth, Patricia Chen, Jared Tritz, and Timothy A. McKay. Computer-Tailored Student Support in Introductory Physics. PLoS ONE, 10(9):e0137001, 2015.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [HCTM15] renders correctly.
- Reference list: Label **[HCTM15]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Computer-tailored text feedback mapping performance onto the student's goals.
  - Source Evidence: Title/abstract: tailored support (ECoach) using students' own goals and performance.
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1371/journal.pone.0137001 · Text Accessed: Full Text


## hirmer_requirements_2022
**Reference:** Hirmer, Tobias et al., 2022 / Requirements and Prototypical Implementation of a Study Planning Assistant in CS Programs / `hirmer_requirements_2022`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 4 occurrence(s): `introduction.tex:4`, `relatedwork.tex:3`, `relatedwork.tex:21`, `relatedwork.tex:46`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{hirmer_requirements_2022,
	address = {Hong Kong},
	title = {Requirements and {Prototypical} {Implementation} of a {Study} {Planning} {Assistant} in {CS} {Programs}},
	isbn = {978-1-6654-8467-1},
	url = {https://ieeexplore.ieee.org/document/9867088/},
	doi = {10.1109/ISET55194.2022.00066},
	urldate = {2025-09-05},
	booktitle = {International {Symposium} on {Educational} {Technology} ({ISET})},
	publisher = {IEEE},
	author = {Hirmer, Tobias and Etschmann, Jana and Henrich, Andreas},
	year = {2022},
	pages = {281--285},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[HEH22]**; reference-list entry:

> [HEH22] Tobias Hirmer, Jana Etschmann, and Andreas Henrich. Requirements and Prototypical Implementation of a Study Planning Assistant in CS Programs. In International Symposium on Educational Technology (ISET), pages 281–285, Hong Kong, 2022. IEEE.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [HEH22] renders correctly; address now 'Hong Kong'.
- Reference list: Label **[HEH22]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Frames study planning as selection and temporal coordination; distinguishes short- and long-term planning.
  - Source Evidence: p. 1: "planning as a process of selection and temporal coordination"; "also differ between short-term and long-term study planning".
  - Validation: Yes.

- Claim 2
  - Thesis Claim: Requirements elicited from semi-structured interviews with twelve CS students.
  - Source Evidence: p. 2: "a total of 12 students were interviewed".
  - Validation: Yes.

- Claim 3
  - Thesis Claim: Table-based planning tool, leaving structure implicit.
  - Source Evidence: Prototype is a semester-planning list/table (IPS2/cmLife context).
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/ISET55194.2022.00066 · Text Accessed: Full Text


## iso9241_11
**Reference:** International Organization for Standardization, 2018 / ISO 9241-11:2018 --- Ergonomics of human-system interaction --- Part 11: Usability: Definitions and concepts / `iso9241_11`

**Traffic Light Indicator:** 🟧 Orange

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `evaluation-appendix.tex:208`, `evaluation.tex:118`
- Key Match: Yes

- BibTeX Source:

```bibtex
@misc{iso9241_11,
	author       = {{International Organization for Standardization}},
	title        = {{ISO} 9241-11:2018 --- Ergonomics of human-system interaction --- Part 11: Usability: Definitions and concepts},
	year         = {2018},
	month        = mar,
	note         = {Second edition},
	url          = {https://www.iso.org/standard/63500.html}
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Int18]**; reference-list entry:

> [Int18] International Organization for Standardization. ISO 9241-11:2018 — er- gonomics of human-system interaction — part 11: Usability: Definitions and concepts, March 2018. Second edition.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `iso_9241-11_2018`); all required fields present.

**(2) PDF Rendering & Content Check**
- In-text: [Int18] renders correctly.
- Reference list: Label **[Int18]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no page numbers (none exist for this venue/format).

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Effectiveness, efficiency, satisfaction.
  - Source Evidence: Standard's definition of usability.
  - Validation: Yes (definitional).

**Access Level & Verification Sources:** Source Location: Unavailable (standard text) · Source Links: https://www.iso.org/standard/63500.html · Text Accessed: Metadata Only

**Recommendation:** Key name only.


## iso9241_210
**Reference:** International Organization for Standardization, 2019 / ISO 9241-210:2019: Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems / `iso9241_210`

**Traffic Light Indicator:** 🟧 Orange

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `needfindingwithprototype.tex:149`
- Key Match: Yes

- BibTeX Source:

```bibtex
@misc{iso9241_210,
	title = {{ISO} 9241-210:2019: {Ergonomics} of human-system interaction — {Part} 210: {Human}-centred design for interactive systems},
	shorttitle = {{ISO} 9241-210},
	url = {https://www.iso.org/standard/77520.html},
	language = {en},
	urldate = {2026-04-09},
	author = {{International Organization for Standardization}},
	year = {2019},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Int19]**; reference-list entry:

> [Int19] International Organization for Standardization. ISO 9241-210:2019: Er- gonomics of human-system interaction — Part 210: Human-centred design for interactive systems, 2019.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `iso_9241-210_2019`); all required fields present.

**(2) PDF Rendering & Content Check**
- In-text: [Int19] renders correctly.
- Reference list: Label **[Int19]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no page numbers (none exist for this venue/format).

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: HCD: understanding users/tasks/environments, specifying requirements, producing solutions, evaluating.
  - Source Evidence: ISO overview page in repo lists these activities.
  - Validation: Yes (abstract level).

**Access Level & Verification Sources:** Source Location: Repo (ISO overview page) · Source Links: https://www.iso.org/standard/77520.html · Text Accessed: Abstract Only

**Recommendation:** Key name only.


## judel_supporting_2023
**Reference:** Judel, Sven et al., 2023 / Supporting Individualized Study Paths Using an Interactive Study Planning Tool / `judel_supporting_2023`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 9 occurrence(s): `design.tex:874`, `design.tex:958`, `discussion.tex:80`, `introduction.tex:2`, `introduction.tex:4`, `introduction.tex:4`, `relatedwork.tex:23`, `relatedwork.tex:46`, `relatedwork.tex:46`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{judel_supporting_2023,
	title = {Supporting {Individualized} {Study} {Paths} {Using} an {Interactive} {Study} {Planning} {Tool}},
	url = {https://dl.gi.de/handle/20.500.12116/42196},
	doi = {10.18420/delfi2023-36},
	abstract = {In addition to various subject-related challenges, students face diverse organizational challenges, including the planning of their own study path while considering individual and organizational circumstances or constraints. While examination regulations usually provide an exemplary study plan, it may only fit as long as no adjustments have to be made. If students fail exams or postpone modules, an individual study plan is needed to keep track of the own study path. With growing enrolment numbers and increasing heterogeneity of study profiles and paths, staff resources in student counselling or mentoring can only provide limited support. As such, this paper presents an interactive, web-based study planning tool, which enables students to plan their individual path using a visual representation of subject areas and modules, while also highlighting module requirements and dependencies. A first evaluation provides positive feedback, a good user experience, but also feature suggestions for further development.},
	language = {en},
	urldate = {2025-08-19},
	booktitle = {21. {Fachtagung} {Bildungstechnologien} ({DELFI})},
	author = {Judel, Sven and Röpke, René and Azendorf, Maximilian and Schroeder, Ulrik},
	year = {2023},
	keywords = {Assistance, Interactive Study Planning, Study Paths, User Experience},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[JRAS23]**; reference-list entry:

> [JRAS23] Sven Judel, René Röpke, Maximilian Azendorf, and Ulrik Schroeder. Sup- porting Individualized Study Paths Using an Interactive Study Planning Tool. In 21. Fachtagung Bildungstechnologien (DELFI), 2023.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year. Spelling now René Röpke.

**(2) PDF Rendering & Content Check**
- In-text: [JRAS23] renders correctly.
- Reference list: Label **[JRAS23]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no page numbers (none exist for this venue/format).

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: A single failed exam or postponed module necessitates an individualised schedule.
  - Source Evidence: Abstract: "If students fail exams or postpone modules, an individual study plan is needed".
  - Validation: Yes.

- Claim 2
  - Thesis Claim: Table-based tool with dependency-awareness inside the table.
  - Source Evidence: p. 3: "a plan's design linked to the tabular form known by most students"; p. 5: on mouse-over "all module recommendations and requirements are depicted using arrows".
  - Validation: Yes.

- Claim 3
  - Thesis Claim: Almost identical hard/soft distinction: recommendations vs requirements.
  - Source Evidence: p. 5: "(1) recommendations include suggestions to take a module before another ... (2) requirements present hard conditions".
  - Validation: Yes.

- Claim 4
  - Thesis Claim: Students asked for automatic planning from past performance.
  - Source Evidence: p. 6: "many participants wished for an automatic planning option ... including past performance, a maximum number of credits per semester".
  - Validation: Yes.

- Claim 5
  - Thesis Claim: Requirements derived from students.
  - Source Evidence: p. 3: requirements gathered from students (e.g. drag-and-drop "directly suggested by students").
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.18420/delfi2023-36 · Text Accessed: Full Text


## jivet_awareness_2017
**Reference:** Jivet, Ioana et al., 2017 / Awareness Is Not Enough: Pitfalls of Learning Analytics Dashboards in the Educational Practice / `jivet_awareness_2017`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:39`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{jivet_awareness_2017,
	address = {Cham},
	title = {Awareness {Is} {Not} {Enough}: {Pitfalls} of {Learning} {Analytics} {Dashboards} in the {Educational} {Practice}},
	isbn = {978-3-319-66610-5},
	url = {https://doi.org/10.1007/978-3-319-66610-5_7},
	doi = {10.1007/978-3-319-66610-5_7},
	booktitle = {Data {Driven} {Approaches} in {Digital} {Education}: 12th {European} {Conference} on {Technology} {Enhanced} {Learning} ({EC}-{TEL} 2017)},
	publisher = {Springer International Publishing},
	author = {Jivet, Ioana and Scheffel, Maren and Drachsler, Hendrik and Specht, Marcus},
	editor = {Lavoué, Élise and Drachsler, Hendrik and Verbert, Katrien and Broisin, Julien and Pérez-Sanagustín, Mar},
	year = {2017},
	pages = {82--96},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[JSDS17]**; reference-list entry:

> [JSDS17] Ioana Jivet, Maren Scheffel, Hendrik Drachsler, and Marcus Specht. Aware- ness Is Not Enough: Pitfalls of Learning Analytics Dashboards in the Educational Practice. In Élise Lavoué, Hendrik Drachsler, Katrien Verbert, Julien Broisin, and Mar Pérez-Sanagustín, editors, Data Driven Approaches in Digital Education: 12th European Conference on Technology Enhanced Learning (EC-TEL 2017), pages 82–96, Cham, 2017. Springer International Publishing.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [JSDS17] renders correctly.
- Reference list: Label **[JSDS17]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Dashboard designs weakly grounded in learning theory; rarely built around learners' own perspectives.
  - Source Evidence: p. 1: "none have addressed the theoretical foundation that should inform the design"; "current designs foster competition between learners rather than knowledge mastery, offering misguided frames of reference".
  - Validation: Yes / Partial for 'learners' own perspectives' (paper says designs are theory-poor and use peer comparison; the perspective wording is a paraphrase).

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1007/978-3-319-66610-5_7 · Text Accessed: Full Text


## kabicher_coordinating_2009
**Reference:** Kabicher, Sonja et al., 2009 / Coordinating Curriculum Implementation Using Wiki-supported Graph Visualization / `kabicher_coordinating_2009`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:12`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{kabicher_coordinating_2009,
	address = {Riga, Latvia},
	title = {Coordinating {Curriculum} {Implementation} {Using} {Wiki}-supported {Graph} {Visualization}},
	url = {http://ieeexplore.ieee.org/document/5194362/},
	doi = {10.1109/ICALT.2009.54},
	urldate = {2025-08-20},
	booktitle = {2009 {Ninth} {IEEE} {International} {Conference} on {Advanced} {Learning} {Technologies}},
	publisher = {IEEE},
	author = {Kabicher, Sonja and Motschnig-Pitrik, Renate},
	year = {2009},
	pages = {742--743},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[KMP09]**; reference-list entry:

> [KMP09] Sonja Kabicher and Renate Motschnig-Pitrik. Coordinating Curriculum Implementation Using Wiki-supported Graph Visualization. In 2009 Ninth IEEE International Conference on Advanced Learning Technologies, pages 742–743, Riga, Latvia, 2009. IEEE.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [KMP09] renders correctly.
- Reference list: Label **[KMP09]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Wiki-supported graph visualisation for curriculum coordination.
  - Source Evidence: Title.
  - Validation: Yes (title-level).

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/ICALT.2009.54 · Text Accessed: Full Text


## loboda_mastery_2014
**Reference:** Loboda, Tomasz D. et al., 2014 / Mastery Grids: An Open Source Social Educational Progress Visualization / `loboda_mastery_2014`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `introduction.tex:6`, `relatedwork.tex:32`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{loboda_mastery_2014,
	address = {Cham},
	title = {Mastery {Grids}: {An} {Open} {Source} {Social} {Educational} {Progress} {Visualization}},
	isbn = {978-3-319-11200-8},
	url = {https://doi.org/10.1007/978-3-319-11200-8_18},
	doi = {10.1007/978-3-319-11200-8_18},
	booktitle = {Open {Learning} and {Teaching} in {Educational} {Communities}: 9th {European} {Conference} on {Technology} {Enhanced} {Learning} ({EC}-{TEL} 2014)},
	publisher = {Springer International Publishing},
	author = {Loboda, Tomasz D. and Guerra, Julio and Hosseini, Roya and Brusilovsky, Peter},
	year = {2014},
	pages = {235--248},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[LGHB14]**; reference-list entry:

> [LGHB14] Tomasz D. Loboda, Julio Guerra, Roya Hosseini, and Peter Brusilovsky. Mastery Grids: An Open Source Social Educational Progress Visualization. In Open Learning and Teaching in Educational Communities: 9th European Conference on Technology Enhanced Learning (EC-TEL 2014), pages 235– 248, Cham, 2014. Springer International Publishing.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [LGHB14] renders correctly.
- Reference list: Label **[LGHB14]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Grid-based progress visualisation combining personal level with peer-group comparison.
  - Source Evidence: p. 1: "Open learning model and social visualization ... a fusion of these two ideas" (Mastery Grids).
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1007/978-3-319-11200-8_18 · Text Accessed: Full Text


## laghari_academic_2023
**Reference:** Laghari, Mohammad Shakeel et al., 2023 / Academic Course Planning Software System at EECE Department / `laghari_academic_2023`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:21`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{laghari_academic_2023,
	address = {Kuantan, Malaysia},
	title = {Academic {Course} {Planning} {Software} {System} at {EECE} {Department}},
	isbn = {978-1-4503-9858-9},
	url = {https://dl.acm.org/doi/10.1145/3587828.3587844},
	doi = {10.1145/3587828.3587844},
	language = {en},
	urldate = {2025-10-14},
	booktitle = {12th {International} {Conference} on {Software} and {Computer} {Applications}},
	publisher = {Association for Computing Machinery},
	author = {Laghari, Mohammad Shakeel and Hraiz, Hamdan T. A. and Ghebretatios, Solomon I. and Alshehhi, Aamna S. H. K.},
	year = {2023},
	pages = {97--104},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[LHGA23]**; reference-list entry:

> [LHGA23] Mohammad Shakeel Laghari, Hamdan T. A. Hraiz, Solomon I. Ghebretatios, and Aamna S. H. K. Alshehhi. Academic Course Planning Software System at EECE Department. In 12th International Conference on Software and Computer Applications, pages 97–104, Kuantan, Malaysia, 2023. Association for Computing Machinery.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [LHGA23] renders correctly; address now 'Kuantan, Malaysia'.
- Reference list: Label **[LHGA23]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Algorithmic system filters eligible courses by completed prerequisites to generate a text-based study plan.
  - Source Evidence: p. 5: "only the required courses for which the student has completed the prerequisites ... only courses eligible for a specific semester are presented".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/3587828.3587844 · Text Accessed: Full Text


## laugwitz_construction_2008
**Reference:** Laugwitz, Bettina et al., 2008 / Construction and Evaluation of a User Experience Questionnaire / `laugwitz_construction_2008`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `evaluation-appendix.tex:80`, `evaluation.tex:96`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{laugwitz_construction_2008,
  author    = {Laugwitz, Bettina and Held, Theo and Schrepp, Martin},
  title     = {Construction and Evaluation of a User Experience Questionnaire},
  booktitle = {HCI and Usability for Education and Work (USAB 2008)},
  series    = {Lecture Notes in Computer Science},
  volume    = {5298},
  pages     = {63--76},
  publisher = {Springer},
  year      = {2008},
  doi       = {10.1007/978-3-540-89350-9_6}
}
```

- Actual Rendered Output (compiled PDF): in-text label **[LHS08]**; reference-list entry:

> [LHS08] Bettina Laugwitz, Theo Held, and Martin Schrepp. Construction and evalu- ation of a user experience questionnaire. In HCI and Usability for Education and Work (USAB 2008), volume 5298 of Lecture Notes in Computer Science, pages 63–76. Springer, 2008.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year. Full text now in repo (.doc).

**(2) PDF Rendering & Content Check**
- In-text: [LHS08] renders correctly.
- Reference list: Label **[LHS08]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: UEQ: 26 items, semantic differential, six scales.
  - Source Evidence: Abstract: "a 26 item questionnaire including the six factors Attractiveness, Perspicuity, Efficiency, Dependability, Stimulation, and Novelty"; §3: "the target format of the questionnaire is a semantic differential".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1007/978-3-540-89350-9_6 · Text Accessed: Full Text


## morsy_study_2019
**Reference:** Morsy, Sara et al., 2019 / A Study on Curriculum Planning and Its Relationship with Graduation GPA and Time To Degree / `morsy_study_2019`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `introduction.tex:2`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{morsy_study_2019,
	title = {A {Study} on {Curriculum} {Planning} and {Its} {Relationship} with {Graduation} {GPA} and {Time} {To} {Degree}},
	isbn = {978-1-4503-6256-6},
	url = {https://dl.acm.org/doi/10.1145/3303772.3303783},
	doi = {10.1145/3303772.3303783},
	language = {en},
	urldate = {2025-09-06},
	booktitle = {The 9th {International} {Learning} {Analytics} \& {Knowledge} {Conference}},
	publisher = {Association for Computing Machinery},
	author = {Morsy, Sara and Karypis, George},
	year = {2019},
	pages = {26--35},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[MK19]**; reference-list entry:

> [MK19] Sara Morsy and George Karypis. A Study on Curriculum Planning and Its Relationship with Graduation GPA and Time To Degree. In The 9th International Learning Analytics & Knowledge Conference, pages 26–35. Association for Computing Machinery, 2019.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [MK19] renders correctly.
- Reference list: Label **[MK19]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Timing and sequencing of courses are associated with time to degree and final grade.
  - Source Evidence: Abstract: analyses "how/if they relate to the students' graduation GPA and time to degree (TTD)".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/3303772.3303783 · Text Accessed: Full Text


## ma_courseq_2021
**Reference:** Ma, Boxuan et al., 2021 / CourseQ: the impact of visual and interactive course recommendation in university environments / `ma_courseq_2021`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `design.tex:974`, `relatedwork.tex:36`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{ma_courseq_2021,
	title = {{CourseQ}: the impact of visual and interactive course recommendation in university environments},
	volume = {16},
	url = {https://doi.org/10.1186/s41039-021-00167-7},
	doi = {10.1186/s41039-021-00167-7},
	abstract = {The abundance of courses available in a university often overwhelms students as they must select courses that are relevant to their academic interests and satisfy their requirements. A large number of existing studies in course recommendation systems focus on the accuracy of prediction to show students the most relevant courses with little consideration on interactivity and user perception. However, recent work has highlighted the importance of user-perceived aspects of recommendation systems, such as transparency, controllability, and user satisfaction. This paper introduces CourseQ, an interactive course recommendation system that allows students to explore courses by using a novel visual interface so as to improve transparency and user satisfaction of course recommendations. We describe the design concepts, interactions, and algorithm of the proposed system. A within-subject user study (N=32) was conducted to evaluate our system compared to a baseline interface without the proposed interactive visualization. The evaluation results show that our system improves many user-centric metrics including user acceptance and understanding of the recommendation results.},
	number = {1},
	journal = {Research and Practice in Technology Enhanced Learning},
	author = {Ma, Boxuan and Lu, Min and Taniguchi, Yuta and Konomi, Shin'ichi},
	year = {2021},
	pages = {18},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[MLTK21]**; reference-list entry:

> [MLTK21] Boxuan Ma, Min Lu, Yuta Taniguchi, and Shin’ichi Konomi. CourseQ: the impact of visual and interactive course recommendation in university environments. Research and Practice in Technology Enhanced Learning, 16(1):18, 2021.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [MLTK21] renders correctly.
- Reference list: Label **[MLTK21]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Within-subjects study; visual interactive explanation improved perceived accuracy, transparency, trust with algorithm held constant; baseline higher on ease of use.
  - Source Evidence: p. 1: "A within-subject user study (N=32)"; p. 12: "baseline ... uses the same algorithm, values, and dataset"; p. 14: "the baseline interface scored higher than the CourseQ interface (Q6 ...)".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1186/s41039-021-00167-7 · Text Accessed: Full Text


## masiello_current_2024
**Reference:** Masiello, Italo et al., 2024 / A Current Overview of the Use of Learning Analytics Dashboards / `masiello_current_2024`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:39`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{masiello_current_2024,
	title = {A {Current} {Overview} of the {Use} of {Learning} {Analytics} {Dashboards}},
	volume = {14},
	url = {https://doi.org/10.3390/educsci14010082},
	doi = {10.3390/educsci14010082},
	number = {1},
	journal = {Education Sciences},
	author = {Masiello, Italo and Mohseni, Zeynab and Palma, Francis and Nordmark, Susanna and Augustsson, Hanna and Rundquist, Rebecka},
	year = {2024},
	pages = {82},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[MMP+24]**; reference-list entry:

> [MMP+24] Italo Masiello, Zeynab Mohseni, Francis Palma, Susanna Nordmark, Hanna Augustsson, and Rebecka Rundquist. A Current Overview of the Use of Learning Analytics Dashboards. Education Sciences, 14(1):82, 2024.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [MMP+24] renders correctly.
- Reference list: Label **[MMP+24]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Difficulty making dashboard data actionable.
  - Source Evidence: p. 1: "it provides predictions which are not clearly translated into pedagogical actions".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.3390/educsci14010082 · Text Accessed: Full Text


## munzner2009
**Reference:** Munzner, Tamara, 2009 / A Nested Model for Visualization Design and Validation / `munzner2009`

**Traffic Light Indicator:** 🟧 Orange

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 11 occurrence(s): `glossary.tex:57`, `design.tex:5`, `design.tex:13`[p.~922], `evaluation.tex:8`, `implementation.tex:288`[p.~921], `introduction.tex:41`, `methodology.tex:6`, `methodology.tex:6`, `methodology.tex:8`, `methodology.tex:10`, `methodology.tex:126`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{munzner2009,
	title = {A {Nested} {Model} for {Visualization} {Design} and {Validation}},
	volume = {15},
	issn = {1077-2626},
	doi = {10.1109/TVCG.2009.111},
	number = {6},
	journal = {IEEE Transactions on Visualization and Computer Graphics},
	author = {Munzner, Tamara},
	year = {2009},
	pages = {921--928},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Mun09]**; reference-list entry:

> [Mun09] Tamara Munzner. A Nested Model for Visualization Design and Validation. IEEE Transactions on Visualization and Computer Graphics, 15(6):921–928, 2009.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `munzner_nested_2009`); all required fields present.

**(2) PDF Rendering & Content Check**
- In-text: [Mun09] renders correctly; implementation.tex anchor now `[p.~921]`.
- Reference list: Label **[Mun09]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Four nested levels; upstream errors cascade; validate each level (p. 921).
  - Source Evidence: p. 921: "an upstream error inevitably cascades to all downstream levels".
  - Validation: Yes.

- Claim 2
  - Thesis Claim: Encoding and interaction one level because mutually interdependent (p. 922).
  - Source Evidence: p. 922, verbatim.
  - Validation: Yes.

- Claim 3
  - Thesis Claim: MatrixExplorer and LiveRAC requirements lists treated as abstraction level.
  - Source Evidence: pp. 924–925, verbatim.
  - Validation: Yes.

- Claim 4
  - Thesis Claim: State upstream assumptions explicitly.
  - Source Evidence: p. 921 abstract.
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/TVCG.2009.111 · Text Accessed: Full Text

**Recommendation:** Only the key name remains; rename if you want strict conformance (cosmetic — labels are unaffected).


## nuseibeh_requirements_2000
**Reference:** Nuseibeh, Bashar et al., 2000 / Requirements engineering: a roadmap / `nuseibeh_requirements_2000`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `needfindingwithprototype.tex:149`[p.~37], `needfindingwithprototype.tex:158`[p.~39]
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{nuseibeh_requirements_2000,
	address = {Limerick, Ireland},
	title = {Requirements engineering: a roadmap},
	isbn = {978-1-58113-253-3},
	shorttitle = {Requirements engineering},
	url = {https://dl.acm.org/doi/10.1145/336512.336523},
	doi = {10.1145/336512.336523},
	language = {en},
	urldate = {2026-04-09},
	booktitle = {Proceedings of the {Conference} on {The} {Future} of {Software} {Engineering}},
	publisher = {ACM},
	author = {Nuseibeh, Bashar and Easterbrook, Steve},
	month = may,
	year = {2000},
	pages = {35--46},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[NE00]**; reference-list entry:

> [NE00] Bashar Nuseibeh and Steve Easterbrook. Requirements engineering: a roadmap. In Proceedings of the Conference on The Future of Software Engineering, pages 35–46, Limerick, Ireland, May 2000. ACM.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [NE00] renders correctly; address now 'Limerick, Ireland'.
- Reference list: Label **[NE00]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: RE identifies stakeholders and their needs and documents them in a form amenable to analysis, communication and subsequent implementation (p. 37).
  - Source Evidence: p. 37: "...by identifying stakeholders and their needs, and documenting these in a form that is amenable to analysis, communication, and subsequent implementation."
  - Validation: Yes.

- Claim 2
  - Thesis Claim: Elicited material has to be interpreted before it can stand as a requirement (p. 39).
  - Source Evidence: p. 39: "Information gathered during requirements elicitation often has to be interpreted, analysed, modelled and validated before the requirements engineer can feel confident that a complete enough set of requirements ... have been collected."
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/336512.336523 · Text Accessed: Full Text


## nielsen1993
**Reference:** Nielsen, Jakob, 1993 / Usability Engineering / `nielsen1993`

**Traffic Light Indicator:** 🟧 Orange

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `evaluation-appendix.tex:208`[pp.~102--103], `evaluation.tex:118`
- Key Match: Yes

- BibTeX Source:

```bibtex
@book{nielsen1993,
	author    = {Nielsen, Jakob},
	title     = {Usability Engineering},
	publisher = {Academic Press},
	address   = {Boston},
	year      = {1993},
	isbn      = {978-0-12-518405-2}
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Nie93]**; reference-list entry:

> [Nie93] Jakob Nielsen. Usability Engineering. Academic Press, Boston, 1993.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `nielsen_usability_1993`); all required fields present. Full text in repo (.djvu).

**(2) PDF Rendering & Content Check**
- In-text: [Nie93] renders correctly; appendix l. 208 now cites `[pp.~102--103]` and names frequency and impact only; evaluation.tex l. 118 cites the five-point scale generically.
- Reference list: Label **[Nie93]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no page numbers (none exist for this venue/format).

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Five-point severity scale, 0 = not a usability problem ... 4 = usability catastrophe.
  - Source Evidence: pp. 102–103: "0 = this is not a usability problem at all / 1 = cosmetic problem only ... / 4 = usability catastrophe".
  - Validation: Yes, verbatim.

- Claim 2
  - Thesis Claim: Severity re-judged from frequency and impact (pp. 102–103).
  - Source Evidence: p. 103, Table 8: "the frequency with which the problem is encountered by users and the impact of the problems on those users who do encounter it".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: ISBN 978-0-12-518405-2 · Text Accessed: Full Text

**Recommendation:** Key name only.


## nielsen1994
**Reference:** Nielsen, Jakob, 1994 / Enhancing the Explanatory Power of Usability Heuristics / `nielsen1994`

**Traffic Light Indicator:** 🟧 Orange

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 4 occurrence(s): `design.tex:19`, `design.tex:30`, `design.tex:539`, `design.tex:549`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{nielsen1994,
	title = {Enhancing the Explanatory Power of Usability Heuristics},
	doi = {10.1145/191666.191729},
	booktitle = {Proceedings of the {SIGCHI} Conference on Human Factors in Computing Systems},
	publisher = {ACM Press},
	author = {Nielsen, Jakob},
	year = {1994},
	pages = {152--158},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Nie94]**; reference-list entry:

> [Nie94] Jakob Nielsen. Enhancing the explanatory power of usability heuristics. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, pages 152–158. ACM Press, 1994.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `nielsen_enhancing_1994`); all required fields present.

**(2) PDF Rendering & Content Check**
- In-text: [Nie94] renders correctly.
- Reference list: Label **[Nie94]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Recognition rather than recall; minimise memory load; error prevention.
  - Source Evidence: p. 1 heuristic list; p. 2 factor A3.
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/191666.191729 · Text Accessed: Full Text

**Recommendation:** Key name only.


## nuutinen_visualization_2003
**Reference:** Nuutinen, Jussi A. et al., 2003 / Visualization of the learning process using concept mapping / `nuutinen_visualization_2003`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:12`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{nuutinen_visualization_2003,
	title = {Visualization of the learning process using concept mapping},
	url = {https://ieeexplore.ieee.org/abstract/document/1215117},
	doi = {10.1109/ICALT.2003.1215117},
	abstract = {Visualization of the learning processes is a powerful way to help students to understand their curricula and the structure behind them. CME2 is a prototype software of this favourable concept, visualizing the learning process as a graph. With this tool students and teachers can easily handle and plan their personal curricula in larger scale and see the connections between different courses. The tool enables comparison between other students' curricula with set operations and it can be used as a planning tool for future studies. Within the teacher-student interaction this tool can be used as an effective aid for counselling.},
	urldate = {2025-08-20},
	booktitle = {3rd {IEEE} {International} {Conference} on {Advanced} {Learning} {Technologies} ({ICALT}'03)},
	author = {Nuutinen, Jussi A. and Sutinen, Erkki},
	year = {2003},
	keywords = {Computer science, Data visualization, Employee welfare, Prototypes, Software prototyping, Technology planning},
	pages = {348--349},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[NS03]**; reference-list entry:

> [NS03] Jussi A. Nuutinen and Erkki Sutinen. Visualization of the learning process using concept mapping. In 3rd IEEE International Conference on Advanced Learning Technologies (ICALT’03), pages 348–349, 2003.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [NS03] renders correctly.
- Reference list: Label **[NS03]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Concept-mapping of the learning process.
  - Source Evidence: Title; abstract: "visualizing the learning process as a graph".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/ICALT.2003.1215117 · Text Accessed: Full Text


## palmer1992
**Reference:** Palmer, Stephen E., 1992 / Common region: A new principle of perceptual grouping / `palmer1992`

**Traffic Light Indicator:** ⬛ Black

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `design.tex:303`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{palmer1992,
	title = {Common region: {A} new principle of perceptual grouping},
	volume = {24},
	issn = {0010-0285},
	url = {https://doi.org/10.1016/0010-0285(92)90014-S},
	doi = {10.1016/0010-0285(92)90014-S},
	number = {3},
	journal = {Cognitive Psychology},
	author = {Palmer, Stephen E.},
	year = {1992},
	pages = {436--447},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Pal92]**; reference-list entry:

> [Pal92] Stephen E. Palmer. Common region: A new principle of perceptual grouping. Cognitive Psychology, 24(3):436–447, 1992.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `palmer_common_1992`); all required fields present.

**(2) PDF Rendering & Content Check**
- In-text: [Pal92] renders correctly.
- Reference list: Label **[Pal92]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Common region: elements inside one bounded area group together.
  - Source Evidence: Full text not provided (the only source still missing). Canonical abstract matches.
  - Validation: Yes at abstract level.

**Access Level & Verification Sources:** Source Location: Unavailable · Source Links: https://doi.org/10.1016/0010-0285(92)90014-S · Text Accessed: Abstract Only

**Recommendation:** Key name; add the PDF if you want it closed out.


## pardos_designing_2020
**Reference:** Pardos, Zachary A. et al., 2020 / Designing for serendipity in a university course recommendation system / `pardos_designing_2020`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:35`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{pardos_designing_2020,
	title = {Designing for serendipity in a university course recommendation system},
	isbn = {978-1-4503-7712-6},
	url = {https://dl.acm.org/doi/10.1145/3375462.3375524},
	doi = {10.1145/3375462.3375524},
	language = {en},
	urldate = {2025-09-05},
	booktitle = {{LAK} '20: 10th {International} {Conference} on {Learning} {Analytics} and {Knowledge}},
	publisher = {Association for Computing Machinery},
	author = {Pardos, Zachary A. and Jiang, Weijie},
	year = {2020},
	pages = {350--359},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[PJ20]**; reference-list entry:

> [PJ20] Zachary A. Pardos and Weijie Jiang. Designing for serendipity in a university course recommendation system. In LAK ’20: 10th International Confer- ence on Learning Analytics and Knowledge, pages 350–359. Association for Computing Machinery, 2020.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [PJ20] renders correctly.
- Reference list: Label **[PJ20]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Optimises for serendipity in the recommended set.
  - Source Evidence: Title.
  - Validation: Yes (title-level).

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/3375462.3375524 · Text Accessed: Full Text


## parasuraman1997humans
**Reference:** Parasuraman, Raja et al., 1997 / Humans and Automation: Use, Misuse, Disuse, Abuse / `parasuraman1997humans`

**Traffic Light Indicator:** 🟧 Orange

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `discussion.tex:82`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{parasuraman1997humans,
  author  = {Parasuraman, Raja and Riley, Victor},
  title   = {Humans and Automation: Use, Misuse, Disuse, Abuse},
  journal = {Human Factors},
  volume  = {39},
  number  = {2},
  pages   = {230--253},
  year    = {1997},
  doi     = {10.1518/001872097778543886}
}
```

- Actual Rendered Output (compiled PDF): in-text label **[PR97]**; reference-list entry:

> [PR97] Raja Parasuraman and Victor Riley. Humans and automation: Use, misuse, disuse, abuse. Human Factors, 39(2):230–253, 1997.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `parasuraman_humans_1997`); all required fields present. Full text now in repo (scanned; OCR'd).

**(2) PDF Rendering & Content Check**
- In-text: [PR97] renders correctly.
- Reference list: Label **[PR97]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Misuse = over-reliance producing failures of monitoring or decision biases.
  - Source Evidence: p. 230 abstract: "Misuse refers to overreliance on automation, which can result in failures of monitoring or decision biases."
  - Validation: Yes, verbatim.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1518/001872097778543886 · Text Accessed: Full Text

**Recommendation:** Key name only.


## rollande_graph_2013
**Reference:** Rollande, Raita et al., 2013 / Graph based framework and its implemented prototype for personalized study planning / `rollande_graph_2013`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `introduction.tex:4`, `relatedwork.tex:12`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{rollande_graph_2013,
	title = {Graph based framework and its implemented prototype for personalized study planning},
	isbn = {978-1-4673-5094-5},
	url = {http://ieeexplore.ieee.org/document/6644362/},
	doi = {10.1109/ICeLeTE.2013.6644362},
	urldate = {2025-08-07},
	booktitle = {2013 {Second} {International} {Conference} on {E}-{Learning} and {E}-{Technologies} in {Education} ({ICEEE})},
	publisher = {IEEE},
	author = {Rollande, Raita and Grundspenkis, Janis},
	year = {2013},
	pages = {137--142},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[RG13]**; reference-list entry:

> [RG13] Raita Rollande and Janis Grundspenkis. Graph based framework and its implemented prototype for personalized study planning. In 2013 Second International Conference on E-Learning and E-Technologies in Education (ICEEE), pages 137–142. IEEE, 2013.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [RG13] renders correctly.
- Reference list: Label **[RG13]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Graph-based framework specifically designed for personalised study planning; graph systems leave the timeline aside.
  - Source Evidence: Title and abstract: "Graph based framework and its implemented prototype for personalized study planning".
  - Validation: Yes (title-level claim).

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/ICeLeTE.2013.6644362 · Text Accessed: Full Text


## roepke_study_2024
**Reference:** Röpke, René et al., 2024 / Study path analyses for quality assurance and support of study planning: Approaches and advancements in the AIStudyBuddy project / `roepke_study_2024`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 5 occurrence(s): `discussion.tex:80`, `discussion.tex:80`, `introduction.tex:4`, `relatedwork.tex:23`, `relatedwork.tex:46`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{roepke_study_2024,
	title = {Study path analyses for quality assurance and support of study planning: {Approaches} and advancements in the {AIStudyBuddy} project},
	url = {https://link.springer.com/10.1007/s00287-024-01574-y},
	doi = {10.1007/s00287-024-01574-y},
	abstract = {Abstract
            Utilizing student lifecycle data provided by campus management systems yields the opportunity to conduct study path analyses. Methods of artificial intelligence (AI) and data science can be used to analyze study paths, identify indicators for success, and gain insights into problems and issues of student cohorts following different study paths. Meanwhile, AI can also be used to support students through informed study planning. This article presents the project AIStudyBuddy with its focus on utilizing rule-based AI and process mining to support study planning and cohort monitoring. The concept of a reference architecture and data model for study path analytics as well as details on the development of the two user applications, StudyBuddy for students and BuddyAnalytics for study program designers, are presented. By exploring how AI and process mining can be applied in the scope of the two applications, the article addresses the question of how AI can be used for quality assurance in study planning and student cohort monitoring.},
	language = {en},
	volume = {47},
	number = {3},
	urldate = {2025-08-19},
	journal = {Informatik Spektrum},
	author = {Röpke, René and Judel, Sven and Schroeder, Ulrik},
	year = {2024},
	pages = {97--104},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[RJS24]**; reference-list entry:

> [RJS24] René Röpke, Sven Judel, and Ulrik Schroeder. Study path analyses for qual- ity assurance and support of study planning: Approaches and advancements in the AIStudyBuddy project. Informatik Spektrum, 47(3):97–104, 2024.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year. Spelling now René Röpke.

**(2) PDF Rendering & Content Check**
- In-text: [RJS24] renders correctly.
- Reference list: Label **[RJS24]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Separates student applications from institution-facing analytics.
  - Source Evidence: Abstract: "StudyBuddy for students and BuddyAnalytics for study program designers".
  - Validation: Yes.

- Claim 2
  - Thesis Claim: Dependency information embedded in the schedule (co-cited with judel_supporting_2023).
  - Source Evidence: Not in this article; carried by Judel 2023 (mouse-over dependency arrows in the tabular plan).
  - Validation: Yes for the pair; this key contributes the project framing, Judel the interface evidence.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1007/s00287-024-01574-y · Text Accessed: Full Text


## sandelowski_real_2001
**Reference:** Sandelowski, Margarete, 2001 / Real qualitative researchers do not count: The use of numbers in qualitative research / `sandelowski_real_2001`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `needfindingwithprototype.tex:132`[p.~239]
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{sandelowski_real_2001,
	title = {Real qualitative researchers do not count: {The} use of numbers in qualitative research},
	volume = {24},
	copyright = {http://onlinelibrary.wiley.com/termsAndConditions\#vor},
	issn = {0160-6891, 1098-240X},
	shorttitle = {Real qualitative researchers do not count},
	url = {https://onlinelibrary.wiley.com/doi/10.1002/nur.1025},
	doi = {10.1002/nur.1025},
	abstract = {Abstract
            Two myths about qualitative research are that real qualitative researchers do not count and cannot count. These antinumber myths have led to the underutilization of numbers in qualitative research and to the simplistic view of qualitative research as non‐ or antinumber. Yet numbers are integral to qualitative research, as meaning depends, in part, on number. As in quantitative research, numbers are used in qualitative research to establish the significance of a research project, to document what is known about a problem, and to describe a sample. But they are also useful for showcasing the labor and complexity of qualitative work and to generate meaning from qualitative data; to document, verify, and test researcher interpretations or conclusions; and to re‐present target events and experiences. Although numbers are important in the treatment of qualitative data, qualitative researchers should avoid the counting pitfalls of verbal counting, overcounting, misleading counting, and acontextual counting. © 2001 John Wiley \& Sons, Inc. Res Nurs Health 24: 230–240, 2001},
	language = {en},
	number = {3},
	urldate = {2026-04-08},
	journal = {Research in Nursing \& Health},
	author = {Sandelowski, Margarete},
	month = jun,
	year = {2001},
	pages = {230--240},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[San01]**; reference-list entry:

> [San01] Margarete Sandelowski. Real qualitative researchers do not count: The use of numbers in qualitative research. Research in Nursing & Health, 24(3):230–240, June 2001.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [San01] renders correctly; `~` now present.
- Reference list: Label **[San01]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Warns against "acontextual counting" (p. 239).
  - Source Evidence: p. 239: "avoid acontextual counting whereby they ... draw unsubstantiated inferences from numbers".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1002/nur.1025 · Text Accessed: Full Text


## sommaruga_curriculum_2007
**Reference:** Sommaruga, Lorenzo et al., 2007 / Curriculum visualization in 3D / `sommaruga_curriculum_2007`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:12`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{sommaruga_curriculum_2007,
	title = {Curriculum visualization in {3D}},
	url = {https://dl.acm.org/doi/abs/10.1145/1229390.1229423},
	doi = {10.1145/1229390.1229423},
	urldate = {2025-08-20},
	booktitle = {Web3D '07: 12th {International} {Conference} on {3D} {Web} {Technology}},
	publisher = {Association for Computing Machinery},
	author = {Sommaruga, Lorenzo and Catenazzi, Nadia},
	year = {2007},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[SC07]**; reference-list entry:

> [SC07] Lorenzo Sommaruga and Nadia Catenazzi. Curriculum visualization in 3D. In Web3D ’07: 12th International Conference on 3D Web Technology. Association for Computing Machinery, 2007.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year. No pages (ACM lists 155–160; optional).

**(2) PDF Rendering & Content Check**
- In-text: [SC07] renders correctly.
- Reference list: Label **[SC07]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no page numbers (none exist for this venue/format).

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Three-dimensional curriculum visualisation.
  - Source Evidence: Title.
  - Validation: Yes (title-level).

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/1229390.1229423 · Text Accessed: Full Text


## schulte_large_2017
**Reference:** Schulte, Jurgen et al., 2017 / Large scale predictive process mining and analytics of university degree course data / `schulte_large_2017`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `introduction.tex:2`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{schulte_large_2017,
	title = {Large scale predictive process mining and analytics of university degree course data},
	isbn = {978-1-4503-4870-6},
	url = {https://dl.acm.org/doi/10.1145/3027385.3029446},
	doi = {10.1145/3027385.3029446},
	language = {en},
	urldate = {2025-09-03},
	booktitle = {{LAK} '17: 7th {International} {Learning} {Analytics} and {Knowledge} {Conference}},
	publisher = {Association for Computing Machinery},
	author = {Schulte, Jurgen and {Fernandez De Mendonca}, Pedro and Martinez-Maldonado, Roberto and {Buckingham Shum}, Simon},
	year = {2017},
	pages = {538--539},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[SFMMB17]**; reference-list entry:

> [SFMMB17] Jurgen Schulte, Pedro Fernandez De Mendonca, Roberto Martinez- Maldonado, and Simon Buckingham Shum. Large scale predictive process mining and analytics of university degree course data. In LAK ’17: 7th International Learning Analytics and Knowledge Conference, pages 538–539. Association for Computing Machinery, 2017.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year. Compound surnames now braced.

**(2) PDF Rendering & Content Check**
- In-text: Label is now [SFMMB17] (the double M comes from the hyphen in Martinez-Maldonado, which alpha treats as two tokens — standard behaviour, leave it).
- Reference list: Label **[SFMMB17]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Advisors struggle to provide evidence-based scheduling advice at scale.
  - Source Evidence: p. 1: "course advisors and student support units find it challenging to provide evidence based advise to students".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/3027385.3029446 · Text Accessed: Full Text


## shneiderman1983
**Reference:** Shneiderman, Ben, 1983 / Direct Manipulation: A Step Beyond Programming Languages / `shneiderman1983`

**Traffic Light Indicator:** 🟧 Orange

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `design.tex:89`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{shneiderman1983,
	title = {Direct {Manipulation}: {A} {Step} {Beyond} {Programming} {Languages}},
	volume = {16},
	url = {https://doi.org/10.1109/MC.1983.1654471},
	doi = {10.1109/MC.1983.1654471},
	number = {8},
	journal = {Computer},
	author = {Shneiderman, Ben},
	year = {1983},
	pages = {57--69},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Shn83]**; reference-list entry:

> [Shn83] Ben Shneiderman. Direct Manipulation: A Step Beyond Programming Languages. Computer, 16(8):57–69, 1983.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `shneiderman_direct_1983`); all required fields present. Repo PDF replaced with the real 13-page article.

**(2) PDF Rendering & Content Check**
- In-text: [Shn83] renders correctly.
- Reference list: Label **[Shn83]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Direct manipulation replaces command syntax with action on visible objects, kept visible and reversible.
  - Source Evidence: p. 57: "visibility of the object of interest; rapid, reversible, incremental actions; and replacement of complex command language syntax by direct manipulation of the object of interest".
  - Validation: Yes, verbatim.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/MC.1983.1654471 · Text Accessed: Full Text

**Recommendation:** Key name only.


## srisamutr_course_2018
**Reference:** Srisamutr, Alangkarn et al., 2018 / A Course Planning Application for Undergraduate Students Using Genetic Algorithm / `srisamutr_course_2018`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:35`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{srisamutr_course_2018,
	address = {Nakhonpathom},
	title = {A {Course} {Planning} {Application} for {Undergraduate} {Students} {Using} {Genetic} {Algorithm}},
	isbn = {978-1-5386-7804-6},
	url = {https://ieeexplore.ieee.org/document/8523980/},
	doi = {10.1109/ICT-ISPC.2018.8523980},
	urldate = {2025-08-19},
	booktitle = {2018 {Seventh} {ICT} {International} {Student} {Project} {Conference} ({ICT}-{ISPC})},
	publisher = {IEEE},
	author = {Srisamutr, Alangkarn and Raruaysong, Thitiporn and Mettanant, Vacharapat},
	year = {2018},
	pages = {1--5},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[SRM18]**; reference-list entry:

> [SRM18] Alangkarn Srisamutr, Thitiporn Raruaysong, and Vacharapat Mettanant. A Course Planning Application for Undergraduate Students Using Genetic 121 Algorithm. In 2018 Seventh ICT International Student Project Conference (ICT-ISPC), pages 1–5, Nakhonpathom, 2018. IEEE.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [SRM18] renders correctly; removed from the 'table-based' triple in the introduction.
- Reference list: Label **[SRM18]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Optimisation (relatedwork.tex).
  - Source Evidence: p. 1: "we propose a genetic algorithm that finds and improves plans".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/ICT-ISPC.2018.8523980 · Text Accessed: Full Text


## siirtola_interactive_2013
**Reference:** Siirtola, Harri et al., 2013 / Interactive Curriculum Visualization / `siirtola_interactive_2013`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:12`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{siirtola_interactive_2013,
	title = {Interactive {Curriculum} {Visualization}},
	isbn = {978-0-7695-5049-7},
	url = {http://ieeexplore.ieee.org/document/6676550/},
	doi = {10.1109/IV.2013.13},
	urldate = {2025-08-20},
	booktitle = {2013 17th {International} {Conference} on {Information} {Visualisation}},
	publisher = {IEEE},
	author = {Siirtola, Harri and R\"aih\"a, Kari-Jouko and Surakka, Veikko},
	year = {2013},
	pages = {108--117},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[SRS13]**; reference-list entry:

> [SRS13] Harri Siirtola, Kari-Jouko Räihä, and Veikko Surakka. Interactive Curricu- lum Visualization. In 2013 17th International Conference on Information Visualisation, pages 108–117. IEEE, 2013.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [SRS13] renders correctly.
- Reference list: Label **[SRS13]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Analyses curriculum content to surface topic overlap between courses.
  - Source Evidence: p. 1: "to find savings by eliminating overlap. We have developed a novel approach to analyse and visualize the contents of a curriculum."
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/IV.2013.13 · Text Accessed: Full Text


## schwendimann2017
**Reference:** Schwendimann, Beat A. et al., 2017 / Perceiving Learning at a Glance: A Systematic Literature Review of Learning Dashboard Research / `schwendimann2017`

**Traffic Light Indicator:** 🟧 Orange

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `design.tex:884`, `introduction.tex:6`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{schwendimann2017,
	title = {Perceiving {Learning} at a {Glance}: {A} {Systematic} {Literature} {Review} of {Learning} {Dashboard} {Research}},
	volume = {10},
	url = {https://doi.org/10.1109/TLT.2016.2599522},
	doi = {10.1109/TLT.2016.2599522},
	number = {1},
	journal = {IEEE Transactions on Learning Technologies},
	author = {Schwendimann, Beat A. and Rodriguez-Triana, Maria Jesus and Vozniuk, Andrii and Prieto, Luis P. and Boroujeni, Mina Shirvani and Holzer, Adrian and Gillet, Denis and Dillenbourg, Pierre},
	year = {2017},
	pages = {30--41},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[SRTV+17]**; reference-list entry:

> [SRTV+17] Beat A. Schwendimann, Maria Jesus Rodriguez-Triana, Andrii Vozniuk, Luis P. Prieto, Mina Shirvani Boroujeni, Adrian Holzer, Denis Gillet, and Pierre Dillenbourg. Perceiving Learning at a Glance: A Systematic Lit- erature Review of Learning Dashboard Research. IEEE Transactions on Learning Technologies, 10(1):30–41, 2017.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `schwendimann_perceiving_2017`); all required fields present.

**(2) PDF Rendering & Content Check**
- In-text: [SRTV+17] renders correctly.
- Reference list: Label **[SRTV+17]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Dashboard aggregates indicators into a unified display.
  - Source Evidence: p. 30: "arranged on a single screen so the information can be monitored at a glance".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/TLT.2016.2599522 · Text Accessed: Full Text

**Recommendation:** Key name only.


## teasley_student_2017
**Reference:** Teasley, Stephanie D., 2017 / Student Facing Dashboards: One Size Fits All? / `teasley_student_2017`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:39`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{teasley_student_2017,
	title = {Student {Facing} {Dashboards}: {One} {Size} {Fits} {All}?},
	volume = {22},
	url = {https://doi.org/10.1007/s10758-017-9314-3},
	doi = {10.1007/s10758-017-9314-3},
	number = {3},
	journal = {Technology, Knowledge and Learning},
	author = {Teasley, Stephanie D.},
	year = {2017},
	pages = {377--384},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Tea17]**; reference-list entry:

> [Tea17] Stephanie D. Teasley. Student Facing Dashboards: One Size Fits All? Technology, Knowledge and Learning, 22(3):377–384, 2017.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [Tea17] renders correctly.
- Reference list: Label **[Tea17]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Feedback effects vary widely; moderators poorly understood; one design cannot serve all.
  - Source Evidence: p. 1: "mixed results about the effects of their use ... 'one-size-fits-all' design ... is questioned"; p. 6: "the results are highly variable ... The conditions or moderators of the effect of feedback ..."
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1007/s10758-017-9314-3 · Text Accessed: Full Text


## trippel_developing_2025
**Reference:** Trippel, Marie et al., 2025 / Developing a Graph-based Visualization of Elective Courses to Support Course Selection in Higher Education / `trippel_developing_2025`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 8 occurrence(s): `discussion.tex:3`, `discussion.tex:78`, `discussion.tex:80`, `discussion.tex:80`, `introduction.tex:4`, `relatedwork.tex:14`, `relatedwork.tex:46`, `relatedwork.tex:46`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{trippel_developing_2025,
	title = {Developing a {Graph}-based {Visualization} of {Elective} {Courses} to {Support} {Course} {Selection} in {Higher} {Education}},
	url = {https://dl.gi.de/handle/20.500.12116/47141},
	doi = {10.18420/delfi2025_09},
	abstract = {In an open curriculum in higher education, students face the challenge of navigating a broad course catalog independently. Prerequisites and recommended courses can make this even more complex, as they are not always easy to follow. Providing students with clear information is essential to make good choices in study planning. Effective visualization could simplify this process for students by providing structured, understandable, and relevant information. This paper presents a novel tool that helps students choose their elective courses using a graph-based visualization of course relationships, emphasizing prerequisites and recommendations. A first user evaluation indicates a strong interest in a course-planning tool for electives and the use of the graph-based visualization was well-liked. Thereby, this research highlights students’ demand for a planning tool and demonstrates the potential of graph visualizations as a valuable resource for future development in this area.},
	language = {en},
	urldate = {2025-09-09},
	booktitle = {23. {Fachtagung} {Bildungstechnologien} ({DELFI})},
	author = {Trippel, Marie and Röpke, René},
	year = {2025},
	keywords = {Course Planner, Course Prerequisites, Dependency Visualization},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[TR25]**; reference-list entry:

> [TR25] Marie Trippel and René Röpke. Developing a Graph-based Visualization of Elective Courses to Support Course Selection in Higher Education. In 23. Fachtagung Bildungstechnologien (DELFI), 2025.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year. Author spelling now consistent (René Röpke) across all four entries.

**(2) PDF Rendering & Content Check**
- In-text: [TR25] renders correctly.
- Reference list: Label **[TR25]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no page numbers (none exist for this venue/format).

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: "required" vs "recommended" edges.
  - Source Evidence: p. 2, verbatim.
  - Validation: Yes.

- Claim 2
  - Thesis Claim: Requirements derived *largely* from institutional stakeholders (wording after fix).
  - Source Evidence: p. 2: head of Study Center, Program Coordinator, student member of the examination committee, Academic Advisory Service.
  - Validation: Yes.

- Claim 3
  - Thesis Claim: Well received; evaluated for reception.
  - Source Evidence: Abstract: "well-liked"; §3 n=15 scenario study with qualitative feedback.
  - Validation: Yes.

- Claim 4
  - Thesis Claim: Graph systems leave the timeline aside.
  - Source Evidence: No semester timeline in the tool.
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.18420/delfi2025_09 · Text Accessed: Full Text


## vessey1991cognitive
**Reference:** Vessey, Iris, 1991 / Cognitive Fit: A Theory-Based Analysis of the Graphs versus Tables Literature / `vessey1991cognitive`

**Traffic Light Indicator:** 🟧 Orange

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `discussion.tex:86`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{vessey1991cognitive,
  author  = {Vessey, Iris},
  title   = {Cognitive Fit: A Theory-Based Analysis of the Graphs versus Tables Literature},
  journal = {Decision Sciences},
  volume  = {22},
  number  = {2},
  pages   = {219--240},
  year    = {1991},
  doi     = {10.1111/j.1540-5915.1991.tb00344.x}
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Ves91]**; reference-list entry:

> [Ves91] Iris Vessey. Cognitive fit: A theory-based analysis of the graphs versus tables literature. Decision Sciences, 22(2):219–240, 1991.

**(1) BibTeX Data Check:** Key does not follow surname_firstword_year (rename to `vessey_cognitive_1991`); all required fields present. Full text now in repo (scanned; OCR'd).

**(2) PDF Rendering & Content Check**
- In-text: [Ves91] renders correctly.
- Reference list: Label **[Ves91]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Cognitive fit: performance depends on the match between representation and task; spatial tasks favour graphs.
  - Source Evidence: Abstract: "performance on a task will be enhanced when there is a cognitive fit (match) between the information emphasized in the representation type and that required by the task type; that is, when graphs support spatial tasks and when tables support symbolic tasks".
  - Validation: Yes, verbatim.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1111/j.1540-5915.1991.tb00344.x · Text Accessed: Full Text

**Recommendation:** Key name only.


## verbert_learning_2020
**Reference:** Verbert, Katrien et al., 2020 / Learning analytics dashboards: the past, the present and the future / `verbert_learning_2020`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `introduction.tex:6`, `relatedwork.tex:39`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{verbert_learning_2020,
	address = {New York, NY, USA},
	title = {Learning analytics dashboards: the past, the present and the future},
	isbn = {978-1-4503-7712-6},
	url = {https://doi.org/10.1145/3375462.3375504},
	doi = {10.1145/3375462.3375504},
	booktitle = {Proceedings of the 10th {International} {Conference} on {Learning} {Analytics} and {Knowledge} ({LAK} '20)},
	publisher = {Association for Computing Machinery},
	author = {Verbert, Katrien and Ochoa, Xavier and De Croon, Robin and Dourado, Raphael A. and De Laet, Tinne},
	year = {2020},
	pages = {35--40},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[VODC+20]**; reference-list entry:

> [VODC+20] Katrien Verbert, Xavier Ochoa, Robin De Croon, Raphael A. Dourado, and Tinne De Laet. Learning analytics dashboards: the past, the present and the future. In Proceedings of the 10th International Conference on Learning Analytics and Knowledge (LAK ’20), pages 35–40, New York, NY, USA, 2020. Association for Computing Machinery.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [VODC+20] renders correctly.
- Reference list: Label **[VODC+20]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Reviews converge on the difficulty of making data actionable.
  - Source Evidence: p. 3 (challenge list): "Lack of actionability"; "What do we evaluate? Usable? Actionable?"
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/3375462.3375504 · Text Accessed: Full Text


## wagner_combined_2023
**Reference:** Wagner, Miriam et al., 2023 / A Combined Approach of Process Mining and Rule-Based AI for Study Planning and Monitoring in Higher Education / `wagner_combined_2023`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:46`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{wagner_combined_2023,
	title = {A {Combined} {Approach} of {Process} {Mining} and {Rule}-{Based} {AI} for {Study} {Planning} and {Monitoring} in {Higher} {Education}},
	volume = {468},
	isbn = {978-3-031-27814-3},
	url = {https://link.springer.com/10.1007/978-3-031-27815-0_37},
	doi = {10.1007/978-3-031-27815-0_37},
	abstract = {Abstract
            This paper presents an approach of using methods of process mining and rule-based artificial intelligence to analyze and understand study paths of students based on campus management system data and study program models. Process mining techniques are used to characterize successful study paths, as well as to detect and visualize deviations from expected plans. These insights are combined with recommendations and requirements of the corresponding study programs extracted from examination regulations. Here, event calculus and answer set programming are used to provide models of the study programs which support planning and conformance checking while providing feedback on possible study plan violations. In its combination, process mining and rule-based artificial intelligence are used to support study planning and monitoring by deriving rules and recommendations for guiding students to more suitable study paths with higher success rates. Two applications will be implemented, one for students and one for study program designers.},
	language = {en},
	urldate = {2025-08-11},
	booktitle = {Process {Mining} {Workshops}},
	publisher = {Springer Nature Switzerland},
	author = {Wagner, Miriam and Helal, Hayyan and Röpke, René and Judel, Sven and Doveren, Jens and Goerzen, Sergej and Soudmand, Pouya and Lakemeyer, Gerhard and Schroeder, Ulrik and van der Aalst, Wil M. P.},
	year = {2023},
	pages = {513--525},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[WHR+23]**; reference-list entry:

> [WHR+23] Miriam Wagner, Hayyan Helal, René Röpke, Sven Judel, Jens Doveren, Sergej Goerzen, Pouya Soudmand, Gerhard Lakemeyer, Ulrik Schroeder, and Wil M. P. van der Aalst. A Combined Approach of Process Mining and Rule-Based AI for Study Planning and Monitoring in Higher Education. In Process Mining Workshops, volume 468, pages 513–525. Springer Nature Switzerland, 2023.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year. Spelling now René Röpke.

**(2) PDF Rendering & Content Check**
- In-text: [WHR+23] renders correctly.
- Reference list: Label **[WHR+23]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: AIStudyBuddy addresses parts of the gap.
  - Source Evidence: Abstract: "Two applications will be implemented, one for students and one for study program designers."
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1007/978-3-031-27815-0_37 · Text Accessed: Full Text


## wardani_major_2020
**Reference:** Wardani, Dewi et al., 2020 / Major choosing decision support system with talent interest approach using SWRL and SAW method / `wardani_major_2020`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:35`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{wardani_major_2020,
	title = {Major choosing decision support system with talent interest approach using {SWRL} and {SAW} method},
	isbn = {978-1-4503-7605-1},
	url = {https://dl.acm.org/doi/10.1145/3427423.3427445},
	doi = {10.1145/3427423.3427445},
	language = {en},
	urldate = {2025-10-14},
	booktitle = {{SIET} '20: 5th {International} {Conference} on {Sustainable} {Information} {Engineering} and {Technology}},
	publisher = {Association for Computing Machinery},
	author = {Wardani, Dewi and Jannah, Ryhannul and Setiadi, Haryono},
	year = {2020},
	pages = {95--100},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[WJS20]**; reference-list entry:

> [WJS20] Dewi Wardani, Ryhannul Jannah, and Haryono Setiadi. Major choosing decision support system with talent interest approach using SWRL and SAW method. In SIET ’20: 5th International Conference on Sustainable Information Engineering and Technology, pages 95–100. Association for Computing Machinery, 2020.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [WJS20] renders correctly.
- Reference list: Label **[WJS20]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Optimises the choice of major rather than of individual courses.
  - Source Evidence: Title: "Major choosing decision support system".
  - Validation: Yes (title-level).

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/3427423.3427445 · Text Accessed: Full Text


## wasfi_optimizing_2023
**Reference:** Wasfi, Asma et al., 2023 / Optimizing Assessment Placement and Curriculum Structure through Graph-Theoretic Analysis / `wasfi_optimizing_2023`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:12`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{wasfi_optimizing_2023,
	title = {Optimizing {Assessment} {Placement} and {Curriculum} {Structure} through {Graph}-{Theoretic} {Analysis}},
	isbn = {979-8-3503-8239-6},
	url = {https://ieeexplore.ieee.org/document/10366474/},
	doi = {10.1109/IIT59782.2023.10366474},
	urldate = {2025-08-07},
	booktitle = {2023 15th {International} {Conference} on {Innovations} in {Information} {Technology} ({IIT})},
	publisher = {IEEE},
	author = {Wasfi, Asma and Mon, Bisni Fahad and Hayajneh, Mohammad and Slim, Ahmad and {Abu Ali}, Najah},
	year = {2023},
	pages = {93--97},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[WMH+23]**; reference-list entry:

> [WMH+23] Asma Wasfi, Bisni Fahad Mon, Mohammad Hayajneh, Ahmad Slim, and Najah Abu Ali. Optimizing Assessment Placement and Curriculum Structure through Graph-Theoretic Analysis. In 2023 15th International Conference on Innovations in Information Technology (IIT), pages 93–97. IEEE, 2023.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year. Last author now braced as {Abu Ali}, Najah.

**(2) PDF Rendering & Content Check**
- In-text: [WMH+23] renders correctly.
- Reference list: Label **[WMH+23]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Graph-theoretic analysis of assessment placement and curriculum structure.
  - Source Evidence: Title.
  - Validation: Yes (title-level).

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1109/IIT59782.2023.10366474 · Text Accessed: Full Text


## wong_sequence_2018
**Reference:** Wong, Chris, 2018 / Sequence Based Course Recommender for Personalized Curriculum Planning / `wong_sequence_2018`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `implementation.tex:238`, `relatedwork.tex:35`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{wong_sequence_2018,
	title = {Sequence {Based} {Course} {Recommender} for {Personalized} {Curriculum} {Planning}},
	volume = {10948},
	url = {http://link.springer.com/10.1007/978-3-319-93846-2_100},
	doi = {10.1007/978-3-319-93846-2_100},
	urldate = {2025-08-19},
	booktitle = {Artificial {Intelligence} in {Education}},
	publisher = {Springer International Publishing},
	author = {Wong, Chris},
	year = {2018},
	pages = {531--534},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Won18]**; reference-list entry:

> [Won18] Chris Wong. Sequence Based Course Recommender for Personalized Cur- riculum Planning. In Artificial Intelligence in Education, volume 10948, pages 531–534. Springer International Publishing, 2018.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [Won18] renders correctly.
- Reference list: Label **[Won18]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Sequence-based methods incorporating deep learning, so far proposed rather than evaluated.
  - Source Evidence: p. 1: "we propose the use of recent deep learning techniques such as LSTM RNNs"; p. 3 describes evaluation as planned future steps.
  - Validation: Yes.

- Claim 2
  - Thesis Claim: Rule-based sequence relations (implementation).
  - Source Evidence: Paper treats sequence/concurrency/constraints as the phenomena a recommender must capture.
  - Validation: Partial — Wong proposes learning sequences, not rule-based ones; the cite supports 'sequence relations' generically.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1007/978-3-319-93846-2_100 · Text Accessed: Full Text


## wienand_design_2024
**Reference:** Wienand, Mareen et al., 2024 / Design principles for e-learning platforms featuring higher-education students' enterprise systems end-user training / `wienand_design_2024`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 3 occurrence(s): `design.tex:358`, `design.tex:884`, `design.tex:893`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{wienand_design_2024,
	title = {Design principles for e-learning platforms featuring higher-education students' enterprise systems end-user training},
	volume = {3},
	url = {https://doi.org/10.1007/s44217-024-00165-z},
	doi = {10.1007/s44217-024-00165-z},
	abstract = {Enterprise systems are complex information systems that are inevitable for companies' success. As enterprise systems are only successful when used continuously and efficiently by end-users, knowledge on how to use them has become an important skill for employees. Research and practice favor an early obtainment of these skills for employees. Thus, it is usual to train students in enterprise systems usage before they start their professional career. Even though in organizational settings e-learning based approaches gain momentum, adapting design instances of multi-purpose platforms like Udacity, Udemy or Coursera existing approaches directed at students are scarce. Nevertheless, a well-informed e-learning platform design can support the learning process. Therefore, we investigate the design of e-learning platforms featuring students' enterprise system end-user training. To address the lack of guidance on designing such e-learning platforms, we proposed four meta-requirements and ten design principles to increase students' learning success on e-learning platforms focusing on students' end-user training.},
	number = {1},
	journal = {Discover Education},
	author = {Wienand, Mareen and Wulfert, Tobias and Hoang, Hiep},
	year = {2024},
	pages = {82},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[WWH24]**; reference-list entry:

> [WWH24] Mareen Wienand, Tobias Wulfert, and Hiep Hoang. Design principles for e-learning platforms featuring higher-education students’ enterprise systems end-user training. Discover Education, 3(1):82, 2024.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [WWH24] renders correctly.
- Reference list: Label **[WWH24]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Complicated navigation was a source of frustration in the replaced system; content chunked as tiles, "index card-like presentation".
  - Source Evidence: p. 13: "a too complicated menu structure for WLIB's predecessor. Reportedly, this navigation structure led to a high level of frustration"; "displayed as tiles to get an index card-like presentation".
  - Validation: Yes, verbatim.

- Claim 2
  - Thesis Claim: Students "might feel lost on how much progress they already made"; progress bars at chapter, sub-chapter, course.
  - Source Evidence: p. 14, verbatim.
  - Validation: Yes.

- Claim 3
  - Thesis Claim: Motivational elements as a design principle.
  - Source Evidence: p. 8: "motivational elements (DP9)".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1007/s44217-024-00165-z · Text Accessed: Full Text


## wang_discovering_2015
**Reference:** Wang, Ren et al., 2015 / Discovering Process in Curriculum Data to Provide Recommendation / `wang_discovering_2015`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:35`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{wang_discovering_2015,
	title = {Discovering {Process} in {Curriculum} {Data} to {Provide} {Recommendation}},
	url = {https://www.educationaldatamining.org/EDM2015/proceedings/poster580-581.pdf},
	urldate = {2025-10-13},
	booktitle = {8th {International} {Conference} on {Educational} {Data} {Mining}},
	author = {Wang, Ren and Zaïane, Osmar R.},
	year = {2015},
	pages = {580--581},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[WZ15]**; reference-list entry:

> [WZ15] Ren Wang and Osmar R. Zaïane. Discovering Process in Curriculum Data to Provide Recommendation. In 8th International Conference on Educational Data Mining, pages 580–581, 2015.

**(1) BibTeX Data Check:** Required fields present (author, title, booktitle, year). No publisher — acceptable for @inproceedings in alpha.

**(2) PDF Rendering & Content Check**
- In-text: [WZ15] renders correctly.
- Reference list: Label **[WZ15]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Process mining over recorded student paths.
  - Source Evidence: Title: "Discovering Process in Curriculum Data".
  - Validation: Yes (title-level).

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://www.educationaldatamining.org/EDM2015/proceedings/poster580-581.pdf · Text Accessed: Full Text


## yuan_research_2024
**Reference:** Yuan, Shuping, 2024 / Research on Personalized Learning Path Recommendation System for Adult Education Based on Deep Learning / `yuan_research_2024`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 1 occurrence(s): `relatedwork.tex:35`
- Key Match: Yes

- BibTeX Source:

```bibtex
@inproceedings{yuan_research_2024,
	title = {Research on {Personalized} {Learning} {Path} {Recommendation} {System} for {Adult} {Education} {Based} on {Deep} {Learning}},
	isbn = {979-8-4007-1173-2},
	url = {https://dl.acm.org/doi/10.1145/3724504.3724603},
	doi = {10.1145/3724504.3724603},
	language = {en},
	urldate = {2025-10-14},
	booktitle = {{ICIEAI} 2024: 2024 2nd {International} {Conference} on {Information} {Education} and {Artificial} {Intelligence}},
	publisher = {Association for Computing Machinery},
	author = {Yuan, Shuping},
	year = {2024},
	pages = {596--600},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Yua24]**; reference-list entry:

> [Yua24] Shuping Yuan. Research on Personalized Learning Path Recommendation System for Adult Education Based on Deep Learning. In ICIEAI 2024: 2024 2nd International Conference on Information Education and Artificial Intelligence, pages 596–600. Association for Computing Machinery, 2024.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year.

**(2) PDF Rendering & Content Check**
- In-text: [Yua24] renders correctly.
- Reference list: Label **[Yua24]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Deep learning for personalised learning paths in adult education.
  - Source Evidence: Title.
  - Validation: Yes (title-level).

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: https://doi.org/10.1145/3724504.3724603 · Text Accessed: Full Text


## zucker_vicurrias_2009
**Reference:** Zucker, Ron, 2009 / ViCurriAS: a curriculum visualization tool for faculty, advisors, and students / `zucker_vicurrias_2009`

**Traffic Light Indicator:** 🟩 Green

**(0) Existence, Mapping & Formatting**
- In Bibliography (.bib): Yes
- Cited in Text (.tex): Yes — 2 occurrence(s): `discussion.tex:78`, `relatedwork.tex:12`
- Key Match: Yes

- BibTeX Source:

```bibtex
@article{zucker_vicurrias_2009,
	title = {{ViCurriAS}: a curriculum visualization tool for faculty, advisors, and students},
	volume = {25},
	number = {2},
	abstract = {This paper introduces ViCurriAS, a visual tool to aid curriculum committees, faculty, and advisors in mapping a particular program of study. ViCurriAS also allows advisors and students to see the course dependencies and progress for the aforementioned program of study. ViCurriAS consists of two integrated environments: one for developing and arranging the flow of courses for a particular program or to aid in the introduction of new courses to an existing curriculum; and the second to provide an advising tool to visually show student progress through the program.},
	journal = {Journal of Computing Sciences in Colleges},
	author = {Zucker, Ron},
	year = {2009},
	pages = {138--145},
}
```

- Actual Rendered Output (compiled PDF): in-text label **[Zuc09]**; reference-list entry:

> [Zuc09] Ron Zucker. ViCurriAS: a curriculum visualization tool for faculty, advisors, and students. Journal of Computing Sciences in Colleges, 25(2):138–145, 2009.

**(1) BibTeX Data Check:** All required fields present (author, title, year + type-specific). Key follows surname_firstword_year. No DOI/URL (journal has none) — fine.

**(2) PDF Rendering & Content Check**
- In-text: [Zuc09] renders correctly.
- Reference list: Label **[Zuc09]** follows alpha (initials + 2-digit year); entry sorted correctly by label; authors first-name-first; title, venue, year present; no spacing or field issues.

**(3) Claim Validation**

- Claim 1
  - Thesis Claim: Displays course dependencies alongside student progress; reaches students through an advising session rather than directly.
  - Source Evidence: Abstract: "allows advisors and students to see the course dependencies and progress"; §4.2: "When a student arrives for an advising session, the advisor will determine ..."
  - Validation: Yes.

- Claim 2
  - Thesis Claim: Rests on the premise that a curriculum carries a prerequisite network worth drawing.
  - Source Evidence: Abstract: "mapping a particular program of study ... course dependencies".
  - Validation: Yes.

**Access Level & Verification Sources:** Source Location: Repo (context/related-work/) · Source Links: JCSC 25(2), 2009 · Text Accessed: Full Text
