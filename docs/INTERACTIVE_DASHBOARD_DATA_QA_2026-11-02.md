# Interactive dashboard data QA — 2 November 2026

## Scope and evidence boundary

This review covers the reviewer-facing static website and the supplemental synthetic analytics test pack. The website does not connect to VELOOP production systems. Its figures are not company KPIs, operating results, targets or approved business definitions.

- User profile and onboarding figures: supplied Task 01 simulated workbook, `Users_1000_Clean`.
- Task activity, rewards, wallet, withdrawals, referrals and feature-event figures: supplemental synthetic analytics workbook.
- The separate Task 02 behavior workbook remains out of scope.
- Sample-window filters use the synthetic data's latest date (15 September 2026), not the current date.

## Reconciled sample figures

| Area | Measure | Result | Denominator / note |
|---|---|---:|---|
| Users | Registered | 1,000 | Task 01 clean user sheet |
| Users | Onboarding complete | 722 (72.2%) | 1,000 users |
| Users | Active account status | 568 (56.8%) | 1,000 users |
| Users | Median lifetime sessions | 9 | Task 01 clean user sheet |
| Task activity | Records | 6,000 | Supplemental synthetic table |
| Task activity | Completed status | 3,229 (53.82%) | 6,000 rows |
| Rewards | Records | 5,001 | Supplemental synthetic table |
| Rewards | Credited status | 3,427 (68.53%) | 5,001 rows |
| Wallet | Transactions | 3,552 | Supplemental synthetic table |
| Withdrawals | Requests | 1,200 | Supplemental synthetic table |
| Withdrawals | Completed status | 684 (57.00%) | 1,200 rows |
| Referrals | Records | 900 | Supplemental synthetic table |
| Referrals | Activated status | 340 (37.78%) | 900 rows |
| Data quality | Messy test rows | 700 | Injected synthetic QA data |
| Data quality | Broad wallet-reference review flags | 52 | REVIEW; polymorphic references need owner-approved mapping |
| Data quality | Self-referral rows | 1 | REVIEW; confirm policy and attribution logic |
| Data quality | Chronology violations | 0 | After QA correction in the synthetic test pack |

## Executive sample-window measures

The selector is anchored to the latest sample date (15 September 2026). Each measure uses its own event/request timestamp and denominator.

| Window | Task attempts | Task completion | Rewards credited | Withdrawals completed |
|---|---:|---:|---:|---:|
| 7 sample days | 214 | 56.54% (121 / 214) | 62.56% (127 / 203) | 68.29% (28 / 41) |
| 30 sample days | 1,038 | 55.39% (575 / 1,038) | 66.30% (606 / 914) | 62.62% (129 / 206) |
| 90 sample days | 3,204 | 54.12% (1,734 / 3,204) | 67.05% (1,799 / 2,683) | 59.70% (397 / 665) |

These denominators differ by domain and are not interchangeable. The percentages are descriptive synthetic sample rates, not production performance.

## QA added

A dependency-free Node.js check validates:
- 25 page sections and matching navigation targets;
- uniqueness of HTML IDs;
- required dashboard elements;
- presence of the reconciled sample figures;
- inline JavaScript syntax;
- availability of period filtering, explorer filtering and CSV export;
- presence of the synthetic-data notice and removal of selected stale illustrative KPI figures.

A GitHub Actions workflow runs this check on relevant pushes, pull requests and manual dispatch.

## Remaining validation boundaries

- No live browser end-to-end run is claimed by the static check.
- No VELOOP production database/API access or production KPI certification is claimed.
- The 52 wallet reference flags and one self-referral remain review items, not silently treated as resolved.
- KPI definitions, event eligibility, referral rules, wallet reference types and business thresholds require company owner approval.
- Dashboard design completeness does not imply implementation of production ingestion, semantic models, refresh SLAs, role-based access or monitoring.

## Deployment

Primary reviewer site: https://velop-task01-submission.vercel.app/

The primary and secondary Vercel production deployments were observed in READY state for commit `b95408f0087db8a60718f7109721afae25812522`. Subsequent QA workflow/test-file commits are separate commits and must complete their own checks and deployments before being considered final.
