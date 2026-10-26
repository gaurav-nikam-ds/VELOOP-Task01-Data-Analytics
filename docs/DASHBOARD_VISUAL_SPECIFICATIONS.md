# Seven-Dashboard Blueprint — Visual-Level Specification

**Status:** proposed design for Task 01. No dashboard metric should be described as production-ready until its source and KPI definition are approved and validated.

## Common specification for every visual

Every visual must show or document: metric and formula, source table/event, eligible population, date field and timezone, date range, dimensions, filters, refresh cadence, business question, decision supported, owner, quality gate, and known limitations. Display last successful refresh and KPI-definition version.

## 1. Executive Overview

| Visual | Metric / calculation | Visualization | Filters / dimensions | Decision supported | Source / refresh |
|---|---|---|---|---|---|
| KPI status cards | Approved DAU, registrations, validated task completion, reward reconciliation exceptions, withdrawal processing SLA, critical DQ failures | Cards with status | Date range, platform where supported | Identify product/operational risks | Governed KPI layer; daily after source SLA agreed |
| Trend overview | Daily/weekly KPI value under approved definition | Line chart | Date, platform, acquisition cohort | Detect meaningful changes | Curated event/transaction tables; daily |
| Data trust panel | Freshness, failed critical checks, unresolved reconciliation count | Status cards/table | Source, pipeline, severity | Decide whether metrics are safe to use | Pipeline metadata; each load |
| Priority exceptions | Open critical/high quality or ledger exceptions by age and owner | Sorted table | Severity, owner, age | Escalate unresolved risk | Quality issue log; each load |

## 2. User Analytics

| Visual | Metric / calculation | Visualization | Filters / dimensions | Decision supported | Source / refresh |
|---|---|---|---|---|---|
| Registration funnel | Started → completed; completion / starts | Funnel | Source, platform, cohort date | Find signup friction | Registration events; daily |
| Onboarding funnel | Eligible users completing each step / users entering step | Funnel/bar | Step, platform, cohort | Prioritize onboarding improvements | Onboarding events; daily |
| Retention cohorts | D1/D7/D30 active users / eligible cohort users | Cohort heatmap | Registration cohort, platform, source | Compare mature cohorts | Registration + approved activity events; daily/weekly |
| Account state trend | Count by state and state transitions over time | Stacked bar/line | State, platform | Investigate state changes | Account state history; daily |

## 3. Engagement

| Visual | Metric / calculation | Visualization | Filters / dimensions | Decision supported | Source / refresh |
|---|---|---|---|---|---|
| Task funnel | View → start → submit → validated completion | Funnel | Task, task type, source, platform | Locate task friction | Task lifecycle events; daily |
| Feature adoption | Distinct eligible users using feature / eligible active users | Bar chart | Feature, cohort, platform | Prioritize feature investigation | Feature events + eligibility; weekly |
| Task completion time | Median and P90 completion minus start | Box plot / percentile cards | Task type, task ID, cohort | Identify slow or inconsistent tasks | Task attempts; daily/weekly |
| Failure reasons | Validation failures by approved reason / all validation attempts | Ranked bar | Task, reason, source | Resolve frequent failures | Validation events; daily |

## 4. Rewards

| Visual | Metric / calculation | Visualization | Filters / dimensions | Decision supported | Source / refresh |
|---|---|---|---|---|---|
| Reward state distribution | Count and amount by pending/credited/reversed/corrected | Stacked bar/table | Reward unit, source, date | Understand queue and adjustments | Authoritative reward ledger; daily |
| Credit latency | Median/P90 credited timestamp − validated timestamp | Percentile cards/trend | Task type, source, unit | Reduce credit delay | Task validation + ledger; daily |
| Reversal/correction trend | Reversed/corrected transactions divided by aligned eligible transactions | Line chart | Reason, task source, cohort | Investigate integrity issues | Reward ledger; daily/weekly |
| Reward reconciliation | Expected vs authoritative credited totals and difference | Variance table | Unit, date, source | Block/resolve unexplained mismatch | Reward ledger + approved source of truth; each load |

## 5. Wallet

| Visual | Metric / calculation | Visualization | Filters / dimensions | Decision supported | Source / refresh |
|---|---|---|---|---|---|
| Ledger movement | Credits, debits and net movement by unit | Diverging bar/line | Unit, transaction type, date | Monitor movement patterns | Wallet ledger; daily |
| Balance reconciliation | Opening + credits − debits vs authoritative closing balance | Variance table | Unit, date | Find ledger mismatches | Ledger + source-of-truth balance; each load |
| Exception register | Invalid, duplicate, orphan or unreconciled transactions | Table | Severity, unit, reason, age | Assign financial data issues | Quality log + ledger; each load |
| Transaction trace | Linked business event → reward/wallet entry → adjustment | Drill-through table | Transaction ID, date, unit | Audit a discrepancy | Ledger-linked transaction model; as needed |

## 6. Withdrawals

| Visual | Metric / calculation | Visualization | Filters / dimensions | Decision supported | Source / refresh |
|---|---|---|---|---|---|
| Request-state funnel | Requests by requested/approved/processed/rejected/failed state | Funnel/bar | Date, payout method category, status | Identify where requests stop | Withdrawal state history; daily |
| Aging queue | Count and age of non-terminal requests | Aging buckets/table | Status, age, owner | Prioritize pending work | Withdrawal state history; each load |
| Processing time | Median/P90 processed timestamp − requested timestamp | Percentile cards/trend | Payout category, cohort, outcome | Reduce delay | Withdrawal and payout timestamps; daily |
| Failure/rejection reasons | Count/share by approved failure/rejection reason | Ranked bar | Reason, payout category, date | Resolve recurring causes | Payout/withdrawal records; daily |

## 7. Referrals

| Visual | Metric / calculation | Visualization | Filters / dimensions | Decision supported | Source / refresh |
|---|---|---|---|---|---|
| Referral funnel | Valid invite/attribution → registration → activation → eligible reward | Funnel | Approved source, cohort | Identify referral drop-off | Referral + user + reward events; daily/weekly |
| Source quality | Activation / eligible referred registrations by source | Bar with sample size | Source, cohort, date | Compare channel quality cautiously | Referral attribution + activity; weekly |
| Time to activation | Median activation timestamp − registration timestamp | Distribution/percentiles | Source, cohort | Identify activation delays | Referral and user lifecycle events; weekly |
| Referral reward integrity | Eligible activations matched to valid reward transactions; exceptions | Reconciliation table | Source, reason, date | Prevent duplicate/ineligible rewards | Referral + reward ledger; each load |

## Global acceptance criteria

- KPI definitions approved and versioned.
- Each visual references an authoritative source and data owner.
- Filters are only exposed where source grain supports them.
- Date logic and timezone are explicit.
- Missing data is not silently converted to zero.
- Critical data-quality or reconciliation failures suppress or clearly invalidate affected metrics.
- No synthetic dataset is presented as actual company performance.
- Each dashboard is tested at desktop and narrow/mobile widths.
