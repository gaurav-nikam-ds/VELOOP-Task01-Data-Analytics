# Companion artifact verification — 31 October 2026

## Local package verification

The following supplied working-package files were opened/read locally. These checks establish that the files exist and can be parsed; they do **not** establish that a coordinator or external reviewer can access them.

| Artifact | Verification | Result |
|---|---|---|
| QA-reviewed consolidated report PDF | pdfinfo and text extraction | Pass — 13 pages, 30,189 extracted text characters, not encrypted |
| Editable consolidated report DOCX | Opened with python-docx | Pass — 140 paragraphs and 9 tables |
| QA-checked master workbook XLSX | Opened with openpyxl | Pass — 32 sheets; workbook structure readable |
| Proposed ERD PNG | Opened with Pillow | Pass — 2,321 × 1,421 pixels, RGBA |
| Seven-dashboard wireframes PNG | Opened with Pillow | Pass — 2,224 × 2,544 pixels, RGBA |

Verified local working-package paths:
- `/mnt/data/velop_task01_package/VELOOP_Task01_Final_Consolidated_Report_QA_Reviewed(1).pdf`
- `/mnt/data/velop_task01_package/Final_Consolidated_Report.docx`
- `/mnt/data/velop_task01_package/VELOOP_Task01_Review_Ready_Project_Package_QA_Checked.xlsx`
- `/mnt/data/velop_task01_package/VELOOP_Task01_Proposed_ERD(3).png`
- `/mnt/data/velop_task01_package/VELOOP_Task01_Seven_Dashboard_Wireframes(1).png`

## Accessibility boundary

These five files are present in the working package but are not present as standalone binary assets in the public GitHub repository tree. No public download links have been verified for them. A local path is not a reviewer-accessible URL.

Before final submission, the coordinator must confirm the accepted handoff destination (for example, an approved company drive or assignment portal). Then publish/attach these exact files there and test each link while signed out or with reviewer-level access. Do not treat the repository README or this manifest as a substitute for the five binary deliverables.

## Technical status

- Live Vercel reviewer workspace: 12/12 browser checks passed on the official production URL in run [41172267582](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/runs/41172267582).
- Next.js build: passed for app commit [9b017b9](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/commit/9b017b939297e20db0f1ce2b4f2e337fc45f55c0).
- A clear production-domain link has been added to the workspace to prevent confusion with deployment-specific preview URLs.
- The synthetic profile script now parses mixed timestamp formats explicitly with pandas `format="mixed"`; the local rerun completed without the prior mixed-date inference warnings.
- Task 01 and supplemental synthetic datasets remain simulated. No production database, API, KPI owner approval or company sign-off is implied.

## External approval request checklist

The following must be confirmed by the coordinator/company owners; the analyst cannot approve these on their behalf:

1. **Coordinator:** confirm Task 01 scope, final submission destination/date, and whether Task 02 data may be used. Current instruction remains progress updates only.
2. **Product owner:** confirm live versus planned features, lifecycle meanings and KPI business intent.
3. **Engineering/data owner:** confirm canonical identifiers, event names/payloads, physical schema, source-of-truth systems, refresh cadence and data access.
4. **Finance/Operations:** confirm reward units, wallet ledger semantics, reversal/correction handling, withdrawal states and reconciliation rules.
5. **KPI owners:** approve formulas, eligible populations, denominators, exclusions, time windows and reporting cadence.
6. **Security/Legal:** review access control, consent, privacy, retention, sharing and governance controls.

No approvals have been received or fabricated in this audit. Keep these gates open until written confirmation is available.


## Expanded local artifact QA — 31 October 2026

The five primary handoff assets were re-opened in the current working session, and the workbook was checked beyond basic file readability.

| Artifact | Current local check | Result |
|---|---|---|
| Primary consolidated PDF | 13 pages; 287,551 bytes; unencrypted; text extraction succeeds | Pass |
| Editable DOCX companion | 140 paragraphs; 9 tables; 52,284 bytes | Pass |
| Master workbook | 32 visible sheets; 105,496 bytes; workbook opens without parser errors | Pass |
| Proposed ERD | 2,321 × 1,421 RGBA; 206,732 bytes | Pass |
| Seven-dashboard wireframes | 2,224 × 2,544 RGBA; 239,457 bytes | Pass |
| Executive dashboard wireframe (additional) | 2,473 × 1,422 RGBA; 189,686 bytes | Pass |

### Master workbook structural checks

- 32 worksheets are present and visible.
- All sheets have freeze panes and autofilters configured.
- Data dictionary: 90 proposed field rows plus header.
- KPI catalogue: 36 proposed KPI rows plus header.
- No formula cells, formula error cells, external workbook links, defined names, hyperlinks or data-validation rules were detected.
- The workbook is a specification and evidence register, not a live calculation engine. The absence of formulas is therefore not a defect in itself; reviewers should use its source/evidence notes and the separate reproducible Python/SQL analysis.

### Supplemental source/test files

- Original Task 01 workbook: 5 sheets; 1,000 clean user records and 1,008 messy audit rows.
- Supplemental synthetic test workbook: 9 sheets; 6,000 task-activity rows, 5,001 reward rows, 3,552 wallet rows, 1,200 withdrawal rows, 900 referral rows and 12,000 feature-event rows (plus support/readme/test tabs).
- These remain simulated assignment/test data, not VELOOP production extracts.

### Documents-page evidence update

The project owner supplied live screenshots showing the Documents section, eight document cards and the proposed minimum event contract. All eight Markdown destinations were fetched successfully from the GitHub default branch. The card hrefs in `vercel-app/app/page.jsx` construct the expected `blob/main/docs/<filename>` URLs and open a new tab. This establishes destination existence and link construction, but not eight physical browser clicks.

### Current automated QA evidence

- Previous production browser QA run 41172267582: 12/12 checks passed.
- Later QA run 41172588945: failed (10 passed, 2 failed).
- Later QA run 41172596454: failed due the production content/version mismatch at that point.
- The current screenshots now show the canonical production banner, the seven dashboard sections, the remaining-dependencies table and the Documents section. These are useful manual visual checks, but do not replace a fresh automated production run after the latest deployment.

### Outstanding handoff blockers

1. The five primary binary assets are still local working files, not verified public reviewer downloads.
2. Publishing those assets into the public GitHub repository would expose them publicly. Obtain explicit confirmation of the approved destination/publication permission, or use the coordinator's approved private drive/portal.
3. The Vercel team integration requires one-time team-scope authorization before deployment metadata and fresh live QA can be inspected.
4. Coordinator/company approvals listed above remain external; no production access, definitions or sign-off are inferred from the screenshots.
