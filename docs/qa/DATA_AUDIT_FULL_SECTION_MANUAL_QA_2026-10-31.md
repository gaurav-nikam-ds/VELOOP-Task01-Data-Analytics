# Data Audit — Full Section Manual QA

**Date:** 31 October 2026  
**Environment:** Production website  
**URL:** https://veloop-task01-data-analytics.vercel.app/  
**Section:** Data audit  
**Evidence:** Six user-provided screenshots captured 31 October 2026 at approximately 11:12–11:13 local time.

## Scope and profile-quality evidence

The page distinguishes the original Task 01 user-profile workbook, the supplemental synthetic test layer and the separate Task 02 workbook.

Visible Task 01 profile evidence:
- 1,000 distinct user IDs.
- Median lifetime sessions: 9.
- Median active days: 6.
- Age range: 18–38.
- Clean-sheet missingness chart: 881 missing `referral_source_detail` values (88.1%) and 72 missing `last_login_datetime` values (7.2%).
- Interpretation explicitly cautions that referral detail may be conditional and last-login absence may be legitimate for users who have never logged in.
- Page states that this is simulated assignment data, not actual VELOOP production data.
- Reproducible profiling script, validation queries and aggregate quality results links are visible.

## Supplemental synthetic test layer

The visible summary cards and dataset table show:
| Dataset | Rows | Fields |
|---|---:|---:|
| Task Activity | 6,000 | 12 |
| Rewards | 5,001 | 10 |
| Wallet | 3,552 | 10 |
| Withdrawals | 1,200 | 9 |
| Referrals | 900 | 8 |
| Feature Events | 12,000 | 12 |
| Messy Data | 700 | 12 |
| External References (support) | 1,977 | 5 |

The interface labels this as generated test data, separate from the original source workbook and Task 02 workbook.

Visible relationship and QA summary:
- User IDs and task-to-reward, reward-correction and wallet-reversal links are reported as passed.
- Chronology checks are reported as passed after the synthetic QA correction.
- Review flags remain: 52 unmatched wallet reference IDs in the broad reference check and one self-referral.
- The intentionally messy test sheet reports 8 missing activity IDs, 11 duplicate non-null activity IDs, 9 malformed timestamps, 9 invalid statuses, 12 whitespace-only failure reasons and 14 negative numeric values in the reward_status field.
- A sample completed-status share of 53.82% is explicitly labelled as calculable only on the generated task table, not a production KPI or target; approved eligibility and denominator rules remain required.

## Separate Task 02 workbook

The page keeps Task 02 separate and shows:
- Sessions: 7,913 rows; 984 distinct user IDs; no orphan user IDs against Task 02 profiles.
- Primary feature events: 35,704 rows; 35,704 unique event IDs; date range 2026-04-02 to 2026-09-15; no user ID orphans.
- Event audit: 35,714 rows; 10 exact duplicate rows.
- Daily activity: 6,667 rows; identified as a Task 02 summary, not Task 01 source.

The visible interpretation guardrail says Task 02 data must not be merged into Task 01 analysis without coordinator approval and source-level counts do not establish production-system correctness.

## Result

**PASS — full Data audit section visual review.** The supplied screenshots show the profile-quality evidence, missingness chart and interpretation, synthetic test dataset counts, relationship/quality review flags, separate Task 02 audit and the no-merging guardrail. The content is clearly partitioned by source and simulation status.

## Important limitations

- This is a manual review of the production interface using user-provided screenshots, not a fresh independent recomputation of every source workbook metric.
- The synthetic layer is not production data; the 53.82% status share is not a company KPI.
- The 52 unmatched wallet references and one self-referral remain explicit review flags, not silently treated as passed.
- Task 02 remains separate pending coordinator approval.
- The screenshot binaries are retained in the ChatGPT Library under `/VELOOP QA Evidence/`; this report does not claim the binaries are embedded in the GitHub repository.

## Remaining project QA

- Verify Deliverables links and document accessibility.
- Verify Dashboard plan and all seven wireframes/specifications.
- Verify What remains and Documents sections.
- Continue responsive layout, navigation, accessibility and browser-console checks.
- Run the complete automated 12-point live QA against the current production deployment.
- Company-side KPI, data ownership, security and production-source approvals remain external dependencies.
