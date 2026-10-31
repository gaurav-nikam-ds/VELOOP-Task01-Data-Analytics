# Findings — High Priority Filter Manual QA

**Date:** 31 October 2026  
**Environment:** Production website  
**URL:** https://veloop-task01-data-analytics.vercel.app/  
**Section:** Findings  
**Test:** Set the priority dropdown to `High`.

## Observed result

- The priority dropdown visibly displays `High`.
- Four finding cards remain visible.
- All four cards display the `High priority` label:
  1. Referral source detail missing
  2. Last-login timestamp missing
  3. Repeated IDs in messy audit tab
  4. Invalid or missing registration dates
- The search field is empty, so the result is attributable to the priority filter rather than a combined search query.
- The CSV export control remains visible.

## Result

**PASS — visual/manual verification.** The High filter state is selected and all displayed findings are marked High priority. This screenshot verifies the visible filter state and matching cards; it does not independently validate the exported CSV contents or prove the behavior of other priority values.

## Screenshot evidence

The original user-provided screenshot was captured on 31 October 2026 at approximately 11:08 (local time). A compressed copy is saved in the ChatGPT Library at:

`/VELOOP QA Evidence/velop_findings_high_priority_filter_qa.jpg`

The screenshot binary is retained in the Library; it is not embedded in this repository commit.

## Remaining checks

- Test the other priority values, if available.
- Download the findings CSV and inspect its rows and headers.
- Continue remaining production navigation, audit, deliverables, dashboard, responsive and accessibility checks.

---
This is manual visual QA evidence for the supplied assignment interface, not evidence of live VELOOP production data or company approval.
