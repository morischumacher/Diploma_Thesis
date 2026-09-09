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
- **`programme` carries the label of Table~7.1.** Participants typed a free-text
  major and five variants came back, so the column is the programme, not the
  string. What each participant wrote, and the programme it belongs to:

  | Participant | Typed | Programme |
  |---|---|---|
  | P01 | Software Engineering (MSc) | Software Engineering (MSc) |
  | P02, P06, P07, P09, P12 | Software Engineering | Software Engineering (MSc) |
  | P04 | MSc Program Software Engineering | Software Engineering (MSc) |
  | P05 | Software Engineering & Internet Computing | Software Engineering (MSc) |
  | P03 | Computer Science | Computer Science (BSc) |
  | P10, P11 | Informatics | Computer Science (BSc) |

  "Informatics" is the faculty rather than a programme, and "Software
  Engineering & Internet Computing" is the Master's former name. The verbatim
  strings for P01 to P08 remain in the workbook's Raw JSON column.

Semester and prior experience needed no normalisation: both already agree with
Table~7.1 for all eleven, which this file makes checkable.

Item names follow the appendix: `a_` and `b_` for the two scenarios, `pu` and
`peu` for the six TAM-derived items, and `ueq1` to `ueq26` as administered and
untransformed.
