Evaluation round material: protocol, anonymized transcripts/notes/coded themes.
Used for grounding chapters/evaluation.tex and chapters/discussion.tex.
Raw video/audio should NOT be committed here -- see CONTROL.md privacy note. Use anonymized text extracts only.

## us-results.csv

The eleven analysed participants, one row each, derived from the study guide's
JSON payload. P08 is excluded, as everywhere in the analysis.

Written because `US Results.xlsx` is the raw export and is not usable as the
source of the appendix tables: it stops at P08, and its derived time columns
were coerced to dates by the spreadsheet, so only its Raw JSON column is
trustworthy. The four later sessions (P09 to P12) are in this file and not yet
in the workbook; the workbook should be re-exported.

Two normalisations, both applied here and nowhere else:

- **Participant identifiers are upper case.** The later sessions recorded
  `p09` to `p12`; the thesis writes P01 to P12 throughout.
- **`programme` carries the label of Table~7.1**, mapped from the free-text
  `major` the participant typed, which is kept verbatim in
  `major_as_reported`. The mapping is: `Informatics` and `Computer Science` to
  Computer Science (BSc); `Software Engineering`, `MSc Program Software
  Engineering` and `Software Engineering & Internet Computing` to Software
  Engineering (MSc). Semester and prior experience are unchanged and already
  agree with Table~7.1 for all eleven.

Item names follow the appendix: `a_` and `b_` for the two scenarios, `pu` and
`peu` for the six TAM-derived items, and `ueq1` to `ueq26` as administered and
untransformed.
