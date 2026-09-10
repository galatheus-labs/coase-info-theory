> Historical document. The canonical paper and `docs/revision-1.3-notes.md` supersede mathematical, measurement, and demo claims in this file.

# arXiv Submission Plan

Prepared: 2026-06-07

## Submission decision

Submit the paper as a working paper in arXiv with this category strategy:

- Primary category: `cs.MA` - Multiagent Systems. This is the best fit because the paper is about agent boundaries, software agents, coordinated interactions, and AI-mediated organizational design.
- Cross-list: `econ.TH` - Theoretical Economics. This is appropriate because the paper generalizes Coase's firm-boundary problem and uses transaction-cost, decision, and market/hierarchy language.
- Do not use `cs.IT` as the primary category. The paper uses information-theoretic vocabulary, but it is not primarily a coding/information-theory contribution.
- Optional but lower-priority cross-list: `cs.CY` only if the submission interface and moderation fit seem favorable. The paper is not mainly policy, ethics, or social-impact analysis, so `cs.CY` should not be the primary route.

Official references:

- arXiv category taxonomy: https://arxiv.org/category_taxonomy
- arXiv submission overview: https://info.arxiv.org/help/submit/index.html
- arXiv TeX submission guidance: https://info.arxiv.org/help/submit_tex.html
- arXiv metadata guidance: https://info.arxiv.org/help/prep.html
- arXiv license guidance: https://info.arxiv.org/help/license/index.html
- arXiv availability schedule: https://info.arxiv.org/help/availability.html

## Endorsement expectation

Assume endorsement may be required unless the submitting account is already
endorsed in the relevant arXiv endorsement domain.

As of arXiv's January 21, 2026 endorsement-policy update, an institutional email
address alone is no longer enough for new submitters. A new submitter can usually
avoid personal endorsement only if both conditions hold:

1. The arXiv account uses an institutional academic or research email.
2. The account has claimed ownership of an existing arXiv paper in the same
   endorsement domain as the target category.

For this paper:

- `cs.MA` is within the Computer Science area. If the submitting account is not
  already endorsed for the relevant `cs` endorsement domain, arXiv will likely
  require endorsement when the submission is started.
- `econ.TH` is within the Economics area. Adding it as a cross-list may require
  separate endorsement in the relevant `econ` endorsement domain if the account
  is not already endorsed there.
- If endorsement becomes a blocker, submit first with primary `cs.MA` only and
  request/add the `econ.TH` cross-list later if arXiv permits it or moderators
  agree it is appropriate.

The submission system is the authoritative check: start the submission, select
the category, and arXiv will state whether endorsement is required and send the
endorsement-request email if needed. arXiv support staff state that they cannot
grant or waive endorsement.

## Current paper state

- Source: `paper/coase-information-theory.tex`
- Local PDF: `paper/coase-information-theory.pdf`
- Current length: 14 pages
- Dependencies: standard TeX Live packages only; no external figures or custom style files.
- Bibliography: embedded `thebibliography`; no `.bib` or `.bbl` needed.
- Companion repository referenced in the paper: `https://github.com/galatheus-labs/coase-info-theory`
- Latest local build command completed cleanly:

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error coase-information-theory.tex
```

## Metadata to enter

Title:

```text
From the Boundary of the Firm to the Boundary of the Agent: Coase-Information Theory for AI-Mediated Organizations
```

Authors:

```text
Brian Guarraci
```

Abstract:

```text
Coase explained the firm as an alternative to market coordination when using the price mechanism is costly. This paper generalizes the problem from the boundary of the firm to the boundary of the agent. In AI-mediated organizations, the relevant units of coordination are not only firms and markets, but recursively composed humans, teams, vendors, workflows, software services, and autonomous agents. Boundaries form when shared representations and control loops reduce surprise, delay, error, or misalignment more than they add coordination and governance cost. Boundaries split when modularity, protocols, or market interfaces preserve enough information while lowering internal coordination burden. The paper contributes a formal language for this agent-boundary problem, a decomposition of coordination cost into measurable information-processing terms, and a definition of organizational agility based on decision-value per unit time. Mutual information is retained as an idealized proxy for information fidelity, but loss reduction is the primary quality quantity. The main claim is that software agents are boundary-shifting infrastructure: by making sensing, routing, interpretation, escalation, and execution programmable, they change the relative cost of hierarchy, market, and hybrid organization.
```

Comments:

```text
14 pages, 1 figure, 3 tables. Companion simulation: https://github.com/galatheus-labs/coase-info-theory
```

ACM-class, if desired:

```text
I.2.11; J.4
```

Leave these blank for v1:

- Journal-ref
- DOI
- Report-no, unless there is an institutional report number to use

## License choice

Recommended default: `CC BY 4.0` if the goal is broad public reuse and there is no planned venue with a conflicting preprint policy.

Conservative alternative: arXiv perpetual, non-exclusive license if later publication venue uncertainty matters more than reuse.

Do not choose a license casually. arXiv states that the selected license for a version is irrevocable.

## Source package

Upload TeX source, not the locally compiled PDF. arXiv currently prefers TeX/LaTeX source and says not to submit a PDF generated from TeX/LaTeX source.

The v1 source package should contain only:

```text
coase-information-theory.tex
```

Do not include:

```text
coase-information-theory.pdf
coase-information-theory.aux
coase-information-theory.log
coase-information-theory.out
coase-information-theory.fdb_latexmk
coase-information-theory.fls
```

Package command:

```sh
rm -rf dist/arxiv-v1
mkdir -p dist/arxiv-v1
cp paper/coase-information-theory.tex dist/arxiv-v1/
(cd dist/arxiv-v1 && zip ../coase-info-theory-arxiv-v1.zip coase-information-theory.tex)
```

Clean-package smoke test:

```sh
rm -rf /tmp/coase-arxiv-test
mkdir -p /tmp/coase-arxiv-test
unzip -q dist/coase-info-theory-arxiv-v1.zip -d /tmp/coase-arxiv-test
(cd /tmp/coase-arxiv-test && latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error coase-information-theory.tex)
```

## Pre-submission checklist

1. Confirm author metadata and affiliation choices.
2. Confirm the GitHub repository is public before submitting, because the paper footnote points to it.
3. Confirm the local PDF still builds cleanly from `paper/coase-information-theory.tex`.
4. Confirm the source package smoke test builds from a clean directory.
5. Confirm no generated files or unrelated HTML examples are included in the arXiv upload.
6. Confirm metadata fields are ASCII. Do not paste text copied from the PDF if it introduces curly quotes, long dashes, ligatures, or other Unicode characters.
7. Confirm references remain as currently audited, with DOI/arXiv/OpenReview/publisher links for the high-risk entries.
8. If the arXiv submission system asks for a compiler, use `PDFLaTeX`.
9. After arXiv compiles the source, inspect the generated PDF page by page before final submission.
10. Compare the arXiv-generated PDF against the local `paper/coase-information-theory.pdf` for title page, Figure 1, Tables 1-3, bibliography links, and total page count.

## Submission timing

As of the current arXiv schedule, new submissions received by 14:00 Eastern are generally announced at 20:00 Eastern, subject to moderation and quality checks. arXiv also notes that quality-assurance checks can take one to four days, sometimes longer.

Because today is Sunday, 2026-06-07, a practical target is:

- Finish repo-public and package checks on Sunday.
- Submit before Monday, 2026-06-08 11:00 Pacific / 14:00 Eastern if a Monday evening announcement is desired.
- Expect possible delay if the category requires endorsement or moderation review.

## Submission flow

1. Log in to arXiv with the author account.
2. Start a new submission.
3. Upload `dist/coase-info-theory-arxiv-v1.zip`.
4. Let arXiv check files and auto-detect the top-level TeX file.
5. Select `coase-information-theory.tex` if the detector asks.
6. Select `PDFLaTeX` if the detector asks.
7. Delete or exclude any file arXiv marks as extraneous.
8. Enter metadata from this plan.
9. Select `cs.MA` as primary and `econ.TH` as cross-list.
10. Choose license.
11. Compile.
12. Review the arXiv-generated PDF carefully.
13. Submit only after the generated PDF matches the local release PDF.

## Post-announcement steps

1. Record the arXiv identifier in `README.md`.
2. Add the arXiv link to the paper page or repository landing page.
3. Tag the repository, for example `arxiv-v1`.
4. If the paper is revised later, submit an arXiv replacement rather than creating a new submission.
5. Add journal reference or DOI later only if a venue publication creates one.
