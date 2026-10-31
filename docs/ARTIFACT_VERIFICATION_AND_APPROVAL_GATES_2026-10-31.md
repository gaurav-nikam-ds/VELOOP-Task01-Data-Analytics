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
