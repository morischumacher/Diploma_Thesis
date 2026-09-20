# CSEDU 2027 paper

Condensed from the thesis for the 19th International Conference on Computer
Supported Education (CSEDU 2027, Rome, 16-18 April 2027). Regular Paper,
double-blind review version.

## Build

    pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper

Template: SCITEPRESS conference LaTeX template (`SCITEPRESS.sty`, `article.cls`,
`apalike.sty`, `apalike.bst`; do not edit). `references.bib` is a copy of the
thesis bibliography with address/url/note fields stripped. `figures/` holds
the screenshots used; `shell_graph_view.png` has the programme code masked.

## Submission limits (Regular Paper)

- 10,000-50,000 characters excluding spaces, including references, tables, figures.
- Full Paper: 12 pages in the proceedings (8 for Short Papers), +4 pages for a fee.
- Deadline (1st stage): 17 November 2026 AoE. Notification 15 January 2027.
- Submit as PDF via PRIMORIS, fully anonymised. Do not post a preprint while under review.

## Before the camera-ready version

- Restore the `\author` block (names, affiliations, e-mails, `\orcidAuthor`).
  `\orcidAuthor` needs `orcid.eps`; on a machine without Ghostscript convert it
  to `orcid-eps-converted-to.pdf` first or compile with `-shell-escape`.
- Un-comment the ACKNOWLEDGEMENTS section and fill in the AI-tools disclosure
  required by the CSEDU policy (tool, affected sections, how it was used).
- Re-insert the institution and curriculum names where they were anonymised
  (Section 3 "a European technical university", Section 5).
- Keep self-citations (papers with a co-author's name) at or below 20 % of the
  reference list; currently 6 of 32.
