# Data Audit — Production Manual Visual QA

**Date:** 31 October 2026  
**Environment:** Production website  
**URL:** https://veloop-task01-data-analytics.vercel.app/  
**Section:** Data audit  
**Evidence:** User-provided production screenshot captured 31 October 2026 at approximately 11:11 local time.

## Visible interface checks

- Data audit navigation item is selected.
- Section heading reads `What data was actually supplied?`.
- Scope statement distinguishes the original Task 01 user-profile workbook, a separately labelled synthetic test pack, and the isolated Task 02 workbook.
- Four summary KPI cards are visible:
  - Clean user profiles: 1,000
  - Named clean-sheet fields: 27
  - Missing cells: 953 (3.53% of all cells)
  - Repeated IDs in audit tab: 8 across 1,008 rows
- Task 01 source workbook table is visible with source sheet, row count, column count and finding columns.
- Clean sheet is shown with 1,000 rows, 27 columns, 1,000 unique non-null `user_id` values and 0 exact duplicate rows.
- Messy audit sheet is shown with 1,008 rows, 28 columns and 8 repeated IDs.
- Missingness details visible:
  - Clean sheet: 881 missing `referral_source_detail`; 72 missing `last_login_datetime`.
  - Messy sheet: 1 missing registration timestamp; 73 missing last-login timestamps; 885 missing referral details; 4 negative `days_since_registration` values.

## Result

**PASS — section rendering and visible data-audit summary.** The navigation, scope statement, summary cards and source workbook table are visibly rendered in the supplied production screenshot.

## Arithmetic spot-check

- Clean-sheet cells: 1,000 × 27 = 27,000.
- Missing-cell rate: 953 ÷ 27,000 × 100 ≈ 3.53%.

## Evidence boundary / caveats

- This is a manual visual check of the production page, not a fresh recomputation from the source workbook.
- The values describe the supplied assignment workbook, not live VELOOP production data.
- The screenshot is retained in the ChatGPT Library as `/VELOOP QA Evidence/Screenshot 2026-10-31 111127.png`; this report does not claim the image binary is embedded in the GitHub repository.

## Remaining checks

- Scroll further through Data audit to verify synthetic-pack tables, relationship checks, quality checks and explanatory caveats.
- Continue Deliverables, Dashboard plan, What remains, Documents, responsive and accessibility checks.
- Automated end-to-end live QA remains a separate outstanding verification.
