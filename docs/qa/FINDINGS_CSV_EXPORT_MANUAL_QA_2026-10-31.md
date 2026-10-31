# Findings CSV Export — Manual QA

**Date:** 31 October 2026  
**Environment:** Production website  
**Section:** Findings  
**Export file received:** `velop-task01-evidence-findings (1).csv`

## File inspection

The downloaded CSV was opened and parsed successfully.

| Check | Observed | Result |
|---|---:|---|
| Data rows | 4 | PASS |
| Columns | 6 | PASS |
| Required headers | Finding, Metric, Evidence, Risk, Recommended action, Priority | PASS |
| Finding names | 4 expected Task 01 findings | PASS |
| Priority values | 4 × High | PASS |
| Missing values | 0 | PASS |
| Duplicate finding names | 0 | PASS |
| CSV parsing | Successful | PASS |

## Cross-check against visible UI

- The four exported finding names match the four cards shown on the Findings page.
- All four rows have Priority = `High`, matching the manually selected High priority filter screenshot.
- The exported metrics and source workbook labels match the visible finding cards and prior Findings screenshot.
- The CSV contains the expected six fields, including risk and recommended action.

## Result

**PASS — downloaded CSV content verified against the visible Findings interface and selected High filter.**

The exported file is committed as `docs/qa/evidence/findings_export_2026-10-31.csv`.

## Evidence boundary

This verifies the uploaded CSV's contents and consistency with the supplied screenshots. The export is a four-row findings summary, not a raw user-level dataset. It describes simulated Task 01 assignment data and must not be represented as live VELOOP production performance.

## Remaining checks

- Verify any other priority filter options, if present.
- Continue the remaining navigation, Data audit, Deliverables, Dashboard plan, responsive and accessibility checks.
- Full automated 12-point live QA remains separate from this manual export check.
