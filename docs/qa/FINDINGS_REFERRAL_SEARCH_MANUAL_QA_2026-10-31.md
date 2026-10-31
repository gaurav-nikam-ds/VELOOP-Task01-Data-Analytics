# Live Findings Search QA Evidence — 31 October 2026

## Test record

- Environment: Vercel production canonical URL
- URL: https://veloop-task01-data-analytics.vercel.app/
- Page: Findings
- Test action: Entered `referral` in the findings search field
- Expected: Only findings matching the search term remain visible
- Observed: Exactly one card remained: **Finding 1 — Referral source detail missing**
- Displayed metric: **881 / 1,000 · 88.1%**
- Source label: `Task 01 workbook · Users_1000_Clean`
- Search control retained the entered query; priority filter remained `All`; CSV export control remained visible.

## Result

**PASS — visual/manual verification.** The production page filtered the four-finding list down to the single referral-related finding. The screenshot supplied by the project owner is the visual evidence for this test.

## Scope and limitation

This is a screenshot-based manual UI check, not a complete automated interaction test. It does not verify CSV file contents, priority filtering, keyboard accessibility, mobile layout, or browser-console status. The displayed data is simulated assignment data, not live VELOOP production data.

## Screenshot evidence

The source screenshot was captured on 31 October 2026 at approximately 11:05 (local device clock), showing the canonical production URL, the entered query `referral`, and the single matching finding. A compressed working copy was prepared locally as `velop_findings_referral_search_qa.jpg`. The binary screenshot is not embedded in this repository commit; this record documents the screenshot evidence and observed result without claiming that the image itself is hosted in GitHub.
