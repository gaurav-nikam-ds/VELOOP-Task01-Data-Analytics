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

## 2. Deployed website functional QA — existing screenshot evidence reviewed

The screenshots already supplied in this conversation were retrieved and reviewed; the user does not need to resend them. Vercel screenshots show Executive status/Home, Insights & recommendations, Supplied data audit, Deliverable tracker, Seven-dashboard blueprint and Implementation library. The Acceptance blockers view is also visible in the earlier screenshot set, but that capture is from the separate Streamlit app, not the Vercel app. Findings screenshots show priority-filter states and the export control; the Deliverable tracker screenshot shows a completed CSV download. These are visual evidence of captured UI states, not automated test logs. The user previously reported testing implementation-library links and mobile layout.

The available screenshot evidence supports the following, while keeping the Vercel and legacy Streamlit screenshots clearly distinguished:

- Seven navigation sections open.
- Findings search and priority filters work.
- CSV exports download and open.
- Source/document links open.
- Desktop and mobile layouts are readable.
- Data-limitation disclosure is visible.
- Supplied-data audit, deliverable tracker and dashboard blueprint render.

**Evidence boundary:** Existing screenshots are treated as user-provided visual evidence; no request to resend them is needed. Vercel captures show six main sections. A separate earlier Streamlit capture shows Acceptance blockers, but it must not be treated as proof that this view was captured in the Vercel app. A new independent live browser session was not run in this pass, so screenshots do not independently prove the latest deployment or every interaction. Mobile layout and link behavior were previously reported by the user as tested, but the reviewed screenshots are desktop captures.

| Test ID | Test | Current result | Evidence status / next action |
|---|---|---|---|
| WEB-01 | Public Vercel URL responds in a fresh browser session | Screenshot evidence shows the Vercel URL rendered in Chrome at capture time | Fresh-session status after the latest commit remains unverified |
| WEB-02 | Navigation sections render | Vercel screenshots show Home, Findings, Data audit, Deliverable tracker, Dashboard blueprint and Implementation library. Acceptance blockers is shown in a separate legacy Streamlit screenshot. | Existing screenshots retained; verify Acceptance blockers in Vercel only if that section exists there |
| WEB-03 | Findings search and priority filters | Screenshot shows priority filter set to High and corresponding findings; another screenshot shows Medium | Visual evidence captured; search interaction itself not independently rerun |
| WEB-04 | CSV export downloads and opens | Screenshot shows a completed deliverable-tracker CSV download; findings CSV export control is visible | Download evidence exists for deliverable tracker; findings CSV completion/opening not separately evidenced in this screenshot subset |
| WEB-05 | Source/document links open | Screenshot shows implementation library cards and visible GitHub link destination preview; user also reported links tested | User-reported pass plus visible link UI; no full click-through log |
| WEB-06 | Desktop layout | Multiple Chrome screenshots show desktop layout | Visual evidence available |
| WEB-07 | Mobile/narrow layout | User previously reported mobile layout tested; screenshot subset reviewed here is desktop | User-reported pass; no narrow-viewport screenshot identified in this subset |
| WEB-08 | Data authenticity notice visible | Screenshot shows the data limitation banner on Home, Findings and Deliverable tracker views | Visual evidence available |
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
