# VELOOP Task 01 — Testing Evidence & QA Status

**Updated:** 31 October 2026  
**Live reviewer workspace:** https://veloop-task01-data-analytics.vercel.app/  
**Repository:** https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics

## 1. Source workbook validation

Original workbook inspected: `VELoop_Rewards_Data_01(2).xlsx`. The source file was retained unchanged.

| Sheet | Data rows (excluding header) | Header cells | Named headers | Blank header cells | Unique non-null user IDs | Duplicate user-ID values | Exact duplicate data rows |
|---|---:|---:|---:|---:|---:|---:|---:|
| `Users_1000_Clean` | 1,000 | 28 | 27 | 1 (column 28) | 1,000 | 0 | 0 |
| `Users_Messy_Audit` | 1,008 | 28 | 28 | 0 | 1,000 | 8 | 8 |

The clean sheet has 28 physical header cells but 27 named fields because the final header cell is blank. The workbook was not modified; do not treat the blank trailing column as a usable field.

## 2. Latest deployed Vercel browser QA — passed

- **Run:** [Live browser QA — 12/12 tests passed](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/runs/41170725246)
- **Build:** [Next.js production build passed](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/runs/40846636252)
- **Date:** 31 October 2026
- **Result:** The live-browser job and build job both completed successfully.

### Browser test coverage

| Test | Result |
|---|---|
| Public site responds; title, data-authenticity notice and navigation visible | PASS |
| All seven navigation sections show expected content | PASS |
| Findings search and priority filter update results | PASS |
| Findings CSV export: filename, headers, 4 data rows and expected content | PASS |
| Deliverables CSV export: filename, headers, 21 data rows and expected content | PASS |
| Narrow mobile viewport remains usable | PASS |
| No horizontal overflow at 320, 360, 390, 768, 1024 and 1440 px | PASS |
| All eight implementation-library document links return successful responses | PASS |
| Interactive controls have accessible names; IDs are unique | PASS |
| Automated WCAG 2.1 A/AA accessibility scan on all seven sections | PASS |
| No failed requests/HTTP error responses during navigation | PASS |
| No uncaught JavaScript errors or console errors | PASS |

The run output reports **11 passed (14.1 seconds)**. The two CSV export checks are covered within one test case.

## 3. What these checks do and do not prove

The automated tests verify the deployed reviewer workspace and the tested browser interactions. They do **not** prove:
- That the app is connected to VELOOP production data (it is not configured to be).
- That proposed KPIs or business definitions have been approved by VELOOP.
- That event tracking or an analytics pipeline has been deployed.
- That all assistive-technology workflows have passed a full manual accessibility audit.
- That the coordinator has accepted the assignment or that every external submission requirement is satisfied.

## 4. Data scope and authenticity guardrails

- Task 01 workbook contains simulated user-profile clean/messy sheets, not the full authoritative transaction-level task/reward/wallet/withdrawal/referral/event pack.
- The behavior workbook identifies itself as Task 02. Keep it separate until the coordinator explicitly approves reuse.
- Findings from supplied workbooks are simulated-source findings, not actual VELOOP production performance.
- Dashboard visual specifications, KPI definitions, event contracts, data model and pipeline are proposed designs unless separately verified as implemented.

## 5. Remaining actions before final submission

1. Verify that the final consolidated report, design workbook and companion diagrams are available in the submission location required by the assignment.
2. Obtain coordinator confirmation about Task 02 scope and any additional submission requirements.
3. Obtain company owner approval for product feature status, canonical identifiers, event definitions, reward units, wallet/withdrawal states, KPI formulas and governance.
4. Keep all synthetic-data warnings and proposal/production distinctions explicit in the final handoff.


## 5. Subsequent website change — 31 October 2026

The 31 October correction removed the separate technology-labelled navigation tab and integrated the profile metrics, missingness chart and supporting links into the existing Data audit section. The live browser suite now asserts exactly seven navigation items and validates the integrated evidence. The current live run passed 12/12 tests; the Next.js production build passed on the corresponding page-change commit.
