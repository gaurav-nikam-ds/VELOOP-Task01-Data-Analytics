# Power BI report build guide

## Visual direction
Use the included theme. Keep a light canvas, white visual surfaces, restrained teal/blue accents, consistent typography, clear titles, and ample whitespace. Avoid unnecessary gradients, 3D charts, and decorative gauges.

## Page 1 — Executive Overview
- Top row: Task Records, Task Completion Rate, Distinct Demo Users, Points on Completed Tasks.
- Left: daily task volume and completed records as a two-line chart.
- Right: task record share by domain as a doughnut chart.
- Bottom left: task status distribution as a horizontal bar chart.
- Bottom right: domain comparison (records vs completion rate), bubble size = distinct demo users.
- Add a small visible banner: “Synthetic demo data — not VELOOP production results.”

## Page 2 — Engagement & Tasks
- Line/area chart: Started, Completed, Validated records over date.
- Matrix heatmap: day of week × domain with record count conditional formatting.
- Box plot (custom visual optional) or clustered bar: duration distribution by domain.
- Funnel-like stage comparison only if clearly labelled as status counts, not a validated user conversion funnel.

## Page 3 — Rewards & Wallet
- Reward records by state.
- Record count by reward unit.
- Daily reward activity by state.
- Wallet movements by movement type.
- Do not sum unlike reward units (e.g. VE, XP, Gems) into one total.

## Page 4 — Withdrawals & Referrals
- Withdrawal status distribution.
- Processing time distribution in hours.
- Referral stage distribution.
- Label all values as illustrative; production SLA requires approved start/end timestamps and business-hour rules.

## Page 5 — Data Readiness
- Table with data domain, evidence available, validation needed, and priority.
- Bar chart of readiness actions by priority.
- KPI card: Production source connections = 0.
- Callout: source access, metric definitions, ownership, and reconciliation must be approved before production reporting.

## Slicers
Add a Date slicer to the task analysis pages and a Domain slicer where relevant. Keep slicers in consistent positions. Avoid implying that a filter applies to unrelated tables unless relationships are configured.

## Suggested relationships
Create a Date table and relate it one-to-many to each fact table’s date column. Use single-direction filtering from Date to fact tables. Do not relate fact tables directly unless a real business key and grain are defined. Keep separate reward units and wallet accounting semantics.

## Before presentation
- Verify all relationships and DAX measures.
- Confirm percentage formats and decimal places.
- Test slicers and cross-filter interactions.
- Show the synthetic-data banner on every page.
- Do not present demo metrics as actual company results.
