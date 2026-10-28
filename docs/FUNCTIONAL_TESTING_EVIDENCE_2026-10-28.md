# VELOOP Task 01 — Testing Evidence & Pending QA

**Review date:** 28 October 2026  
**Live reviewer workspace:** https://velop-task01-data-analytics.vercel.app/  
**Repository:** https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics

## 1. Source workbook validation — performed

Original workbook inspected: `VELoop_Rewards_Data_01(2).xlsx`. The original file was retained unchanged. Checks were run against the workbook in the current analysis environment.

| Sheet | Data rows (excluding header) | Header cells | Named headers | Blank header cells | Unique non-null user IDs | Duplicate user-ID values | Exact duplicate data rows |
|---|---:|---:|---:|---:|---:|---:|---:|
| `Users_1000_Clean` | 1,000 | 28 | 27 | 1 (column 28) | 1,000 | 0 | 0 |
| `Users_Messy_Audit` | 1,008 | 28 | 28 | 0 | 1,000 | 8 | 8 |

### Resolution of the workbook mismatch

The clean sheet has **28 physical header cells but only 27 named fields** because the final header cell is blank. The earlier discrepancy was a difference in counting conventions, not evidence of a 27-field versus 28-field named schema. Documentation now states both counts. The source workbook was not modified; do not treat the blank trailing column as a usable field.

## 2. Deployed website functional QA — evidence boundary

The repository's `vercel-app/README.md` records that the project owner manually checked the deployed site on 28 October 2026. The checks recorded as owner-reported are:

- Seven navigation sections open.
- Findings search and priority filters work.
- CSV exports download and open.
- Source/document links open.
- Desktop and mobile layouts are readable.
- Data-limitation disclosure is visible.
- Supplied-data audit, deliverable tracker and dashboard blueprint render.

**Independent verification status:** A fresh browser fetch of the public Vercel URL could not be completed from this QA environment (the web retrieval returned a cache-miss/internal fetch error). This is an environment limitation; it does **not** prove the website is down or broken. Therefore, these checks remain owner-reported rather than independently re-run in this pass. Attach screenshots or a browser-run log to make the evidence package stronger.

| Test ID | Test | Current result | Evidence status / next action |
|---|---|---|---|
| WEB-01 | Public Vercel URL responds in a fresh browser session | Not independently verified in this environment | Re-run in Chrome and record timestamp/status |
| WEB-02 | All seven navigation sections render | Owner-reported PASS | Attach screenshot(s) or screen recording |
| WEB-03 | Findings search and priority filters | Owner-reported PASS | Capture a before/after filtered result |
| WEB-04 | CSV export downloads and opens | Owner-reported PASS | Attach exported sample and screenshot; confirm caveat is included |
| WEB-05 | Source/document links open | Owner-reported PASS | Capture link destinations or click-through evidence |
| WEB-06 | Desktop layout | Owner-reported PASS | Attach desktop screenshot |
| WEB-07 | Mobile/narrow layout | Owner-reported PASS | Attach narrow viewport/mobile screenshot |
| WEB-08 | Data authenticity notice visible | Owner-reported PASS | Capture notice in deployed UI |
| WEB-09 | No production connection or actual company KPI claims | Owner-reported PASS; docs/code claims reviewed | Final visual recheck required |
| WEB-10 | Latest Vercel deployment is ready after current commits | Pending | Check Vercel deployment status before final submission |

## 3. Automated checks and limits

- Repository workflow `.github/workflows/vercel-app-build.yml` is configured to install the Next.js app dependencies and run `npm run build` for relevant pushes/pull requests.
- The Vercel commit status observed during this review was **pending**, so a successful deployment after the latest documentation change is not claimed.
- The separate Streamlit smoke workflow checks Python compilation, startup and the health endpoint. That is a different app and does not validate the Vercel UI.
- No automated browser/E2E test suite for all seven Vercel sections was found in the inspected project documentation. Manual browser evidence remains necessary.

## 4. Data scope guardrail

- Task 01 workbook contains simulated user-profile clean/messy sheets, not the full transaction-level task/reward/wallet/withdrawal/referral/event pack.
- The behavior workbook labels itself Task 02. Keep it separate until coordinator approval.
- All findings from supplied workbooks are simulated-source findings, not actual VELOOP production performance.
- Dashboard visual specifications, KPI definitions, event contracts, data model and pipeline are proposed designs unless separately verified as implemented.

## 5. Pending items before final submission

1. Confirm the latest Vercel deployment status is Ready.
2. Independently run WEB-01 through WEB-10 and save screenshots/logs; replace owner-reported statuses with verified results only after evidence exists.
3. Keep Task 01 and Task 02 files separate until written coordinator approval.
4. Obtain internal approval of feature status, identifiers, event definitions, reward units, wallet/withdrawal states and KPI formulas.
5. Include this testing-evidence document and the implemented-vs-planned feature matrix in the final review package.
