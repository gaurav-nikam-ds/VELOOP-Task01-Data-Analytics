# Final Technical QA Report — 2 November 2026

## Outcome

**Result: 11/11 live Playwright tests passed.**

- **Primary reviewer website:** https://velop-task01-submission.vercel.app/
- **Repository:** https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics
- **Successful browser QA run:** https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/runs/41469605990
- **Successful static QA run:** https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/runs/41469495737
- **Verified Vercel production deployment:** `dpl_2KDLaWXujitdfoDLoVtwN3fBey8u` — READY. The primary domain alias is assigned to this verified deployment.

## Test results

| # | Test | Result |
|---:|---|---|
| 1 | Production deployment responds, title/navigation and simulated-data notice are visible | PASS |
| 2 | All 25 analytical and interactive dashboard sections open and render their own heading | PASS |
| 3 | Coverage inventory search, no-match state and reset | PASS |
| 4 | Executive 7/30/90 sample-window filters recalculate all four KPIs | PASS |
| 5 | User, reward, referral, data-quality and operations KPI blocks render expected values | PASS |
| 6 | Data Explorer domain and text filters change the visible result set | PASS |
| 7 | Filtered Data Explorer CSV downloads with expected filename and data | PASS |
| 8 | Responsive layouts at 320, 360, 390, 768, 1024 and 1440 px; no horizontal overflow | PASS |
| 9 | Interactive controls have accessible names and all HTML IDs are unique | PASS |
| 10 | WCAG 2.1 A/AA automated accessibility scan across all 25 sections | PASS |
| 11 | No failed network requests, HTTP errors, uncaught JavaScript errors or console errors | PASS |

## Defects corrected during final QA

- Replaced stale browser tests that targeted the former seven-section Next.js workspace with a 25-section suite for the primary static reviewer website.
- Corrected tests to count visible table rows after filtering, rather than all DOM rows.
- Added accessible names to navigation and coverage search inputs.
- Added keyboard-focusable named regions for scrollable tables.
- Corrected low-contrast text and chart colours in the overview, audit, wireframe, event tracking and dashboard sections.
- Reconciled sample metrics to the actual synthetic test pack and removed selected unsupported illustrative trend/cohort claims.
- Configured the primary Vercel project and verified the production domain against the explicit READY deployment. The public production alias is pinned to the tested READY deployment. The Git-connected project build still needs a stable static-output configuration; future source pushes should be followed by a deployment-state check and alias verification.

## Data and production boundaries

- The user profile figures originate from the simulated Task 01 workbook.
- Task activity, rewards, wallet, withdrawals, referrals, feature events and messy test rows are supplemental synthetic data.
- The 52 wallet-reference flags and one self-referral are review items, not silently resolved business issues.
- No VELOOP production database/API integration, ingestion pipeline or production KPI certification is claimed.
- Task 02 behavior data remains out of scope unless the coordinator approves reuse.
- Product, Engineering, Finance/Operations and Security/Legal approvals remain external acceptance gates.
