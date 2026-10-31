# VELOOP Task 01 — Vercel app

This is the deployed Next.js reviewer workspace and the sole active website/QA target for this repository. It documents the Task 01 analytics proposal and source-data findings; it is **not** connected to VELOOP production systems.

## Live deployment

https://veloop-task01-data-analytics.vercel.app/

## Deploy to Vercel

1. Import `gaurav-nikam-ds/VELOOP-Task01-Data-Analytics` into Vercel.
2. Set **Root Directory** to `vercel-app`.
3. Framework preset: **Next.js**. Build command: `npm run build`. Keep the framework default output directory.
4. Deploy and confirm the deployment is Ready.
5. After UI changes, run the live browser QA workflow and review its report.

## Local run and build

```bash
cd vercel-app
npm install
npm run dev
```

Production build check:

```bash
npm install
npm run build
```

The [Vercel build workflow](../.github/workflows/vercel-app-build.yml) checks the Next.js production build. The [live browser QA workflow](../.github/workflows/live-vercel-qa.yml) tests the deployed site.

## Latest verified QA

**31 October 2026:** [Live browser QA passed 12/12 tests](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/runs/41170725246). The [Next.js production build passed](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/runs/41170709789).

The browser suite verifies:
- Public page response and visible data-authenticity notice
- All seven navigation sections
- Findings search and priority filter
- Findings and deliverable-tracker CSV exports, filenames, headers and row counts
- Narrow mobile use and overflow across 320, 360, 390, 768, 1024 and 1440 pixel widths
- All eight implementation-library links
- Accessible names and unique element IDs
- Automated WCAG 2.1 A/AA checks on all seven sections
- No failed requests/HTTP error responses and no browser JavaScript or console errors

These are automated browser checks against the deployed reviewer workspace. They do not prove production analytics integrations, business correctness of unapproved KPI definitions, or coordinator acceptance.

## Implemented versus proposed

| Area | Status | Boundary |
|---|---|---|
| Seven reviewer navigation sections | Implemented | These are workspace pages, not seven live production dashboards |
| Findings search and priority filtering | Automated browser-tested | Shows Task 01 simulated-source audit findings |
| CSV exports | Automated browser-tested | Exported reviewer/audit content is not production performance data |
| Implementation-library document links | Automated browser-tested | Eight links return successful HTTP responses |
| Responsive layout | Automated browser-tested | No horizontal overflow at tested viewport widths |
| Automated accessibility | WCAG 2.1 A/AA scan passes | Automated scan is not a full manual accessibility audit |
| Seven dashboard areas | Proposed specification | Not deployed production dashboards |
| Production database/API, event tracking and analytics pipeline | Not implemented/configured here | Requires approved source systems and engineering work |
| Task 02 behavior data inside Task 01 | Blocked pending coordinator approval | Keep scopes separate unless written approval is received |

## Data authenticity

The supplied assignment workbooks are simulated. The Task 01 source workbook provides user-profile clean/messy tabs, not a complete authoritative task/reward/wallet/withdrawal/referral/event transaction pack. The separate behavior workbook identifies itself as Task 02 and is not merged into Task 01. No production database/API connection is configured.

**Do not present simulated rows, sample counts, proposed KPIs or synthetic metrics as actual VELOOP company performance.** Proposed fields, event contracts, KPI definitions, data models, governance controls and pipeline steps require review and approval by the relevant company owners.


## Supporting assignment artifacts

The live website is the reviewer workspace; it is not a substitute for the full report and workbook deliverables. The assignment audit is tracked in [the final deliverable audit](../docs/FINAL_DELIVERABLE_AUDIT_2026-10-29.md). Before marking the assignment ready for final submission, confirm that the consolidated report (PDF and editable DOCX), QA-checked master workbook, proposed ERD and dashboard wireframes are individually accessible from this repository or the coordinator-approved submission location. Do not claim these files are hosted here until their links have been verified.



## Data-profile evidence in the reviewer workspace

The profiling results and field-level missingness visualization are integrated into the existing **Supplied data audit** page. There is no separate technology/skills navigation section. Supporting reproducibility files remain in the repository's [analytics folder](../analytics/README.md), including the [profiling script](../analytics/python/analyze_task01.py), [validation queries](../analytics/sql/task01_analysis.sql), [quality summary](../analytics/evidence/quality_summary.json), and [missingness chart](../analytics/evidence/top_missing_fields.svg).

This analysis uses only the supplied Task 01 simulated user-profile sheets. It does not include Task 02 data and does not calculate production task, reward, wallet, withdrawal, referral or event metrics.
