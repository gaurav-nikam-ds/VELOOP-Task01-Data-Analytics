# Deliverables — Full Tracker and CSV Export Manual QA

**Date:** 31 October 2026  
**Environment:** Production website  
**URL:** https://veloop-task01-data-analytics.vercel.app/  
**Evidence:** User-provided production screenshots and downloaded CSV.

## Tracker visual review

- All 21 deliverable rows are visible across the supplied screenshots.
- Table columns: `#`, `Deliverable`, `Evidence status`, `Remaining dependency`.
- Row numbering runs from 01 through 21.
- Status and dependency columns distinguish completed documentation from proposed designs and pending company decisions.
- Explicit dependencies include scope approval, owner review, source-system validation, Engineering approval, Finance/Operations confirmation, KPI formula approval, Security/Legal review, stakeholder prioritisation and coordinator acceptance.
- The tracker correctly describes final handoff as `Prepared for review`, with coordinator/stakeholder acceptance still required.

## Downloaded CSV inspection

Uploaded file: `velop-task01-deliverable-tracker (3).csv`

| Check | Result |
|---|---:|
| Rows | 21 |
| Columns | 3 |
| Headers | Deliverable; Evidence status; Remaining dependency |
| Missing cells | 0 |
| Duplicate rows | 0 |
| Duplicate deliverable names | 0 |
| CSV parse | Successful |

Evidence-status distribution:
| Status | Rows |
|---|---:|
| Documented | 5 |
| Proposed | 5 |
| Documented design | 3 |
| Documented proposal | 2 |
| 36 proposed KPIs | 1 |
| 90 proposed fields | 1 |
| Profiled and cross-checked | 1 |
| Automated validation checks; documented proposal | 1 |
| Documented blueprint | 1 |
| Prepared for review | 1 |

## Result

**PASS — tracker rendering and downloaded CSV content verified.** The downloaded file contains 21 unique deliverables, all three expected columns, no blank cells and no duplicate rows. The visible table and export agree on the deliverable count and dependency/status model.

## Interpretation guardrail

The tracker is an evidence and dependency register. Its documented/proposed statuses are not company approval, production implementation, or final stakeholder acceptance. Several items explicitly remain dependent on external owners.

## Evidence files

- CSV committed as `docs/qa/evidence/deliverable_tracker_export_2026-10-31.csv`.
- Screenshots retained in ChatGPT Library: `/VELOOP QA Evidence/Screenshot 2026-10-31 111546.png` and `/VELOOP QA Evidence/Screenshot 2026-10-31 111553.png`. The image binaries are not embedded in this GitHub commit.

## Remaining project checks

- Dashboard plan, What remains and Documents sections.
- Responsive layout, accessibility and browser-console checks.
- Full automated 12-point live QA against current production.
- Company-side scope, KPI, data ownership, Security/Legal and production-source approvals.
