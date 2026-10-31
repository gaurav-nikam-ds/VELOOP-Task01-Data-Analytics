# Task 01 — Python, SQL and Visualization Evidence

**Analysis date:** 31 October 2026  
**Source:** supplied Task 01 workbook, sheets `Users_1000_Clean` and `Users_Messy_Audit`  
**Classification:** simulated assignment data; not VELOOP production data  
**Scope:** Task 01 only. The separate Task 02 workbook was not used.

## Reproducible implementation

- Python: pandas profiling, missingness, duplicate-ID checks, numeric range summaries, clean-versus-messy comparison and aggregate chart generation.
- SQL: SQLite-compatible queries for row counts, distinct IDs, duplicates, key-field missingness, account status, onboarding status, acquisition source and descriptive activity summaries.
- Visualization: field-level missingness chart generated from aggregate counts.
- Privacy: names and email addresses are excluded from the local SQL tables and are never exported in the aggregate evidence files.

Code and run instructions are in [analytics/README.md](../analytics/README.md).

## Rechecked results

| Check | Result |
|---|---:|
| Clean user sheet | 1,000 rows × 27 named columns |
| Distinct non-null user IDs | 1,000 |
| Duplicate user IDs in clean sheet | 0 |
| Null user IDs in clean sheet | 0 |
| Missing cells in clean sheet | 953 (3.53% of 27,000 cells) |
| Missing `referral_source_detail` | 881 (88.1%) |
| Missing `last_login_datetime` | 72 (7.2%) |
| Age range | 18–38 |
| Median lifetime sessions | 9 |
| Median active days | 6 |
| Messy audit sheet | 1,008 rows × 28 columns |
| Distinct user IDs in messy audit sheet | 1,000 |
| Duplicate extra ID rows in messy audit sheet | 8 |
| Missing registration timestamp in messy audit sheet | 1 |

The account-status distribution in the clean sheet is: Active 568, Inactive 283, Suspended 77, Pending Verification 72. The onboarding distribution is: Completed 722, Started 146, Not Started 132.

## Interpretation

1. The clean sheet has a unique, non-null user identifier for every row in this supplied sample.
2. Missing referral-source detail is concentrated and substantial. Its requiredness must be defined conditionally (for example, referral-attributed registrations versus other acquisition routes) before using it for attribution reporting.
3. A missing last-login timestamp is not automatically a defect; it may be valid for a user who has never logged in. Confirm null semantics with the product owner.
4. The messy audit sheet has eight repeated user-ID rows and one missing registration timestamp. Preserve the audit trail; do not silently delete or overwrite records.
5. The source workbook has no transaction-level task, reward, wallet, withdrawal, referral or event fact tables. These results do not support task-completion, earnings, payout, retention or conversion KPIs.

## Validation

- Python script executed successfully against the supplied workbook.
- SQLite database generated locally with names and emails excluded.
- SQL file parsed and executed successfully against the generated SQLite database.
- Aggregate CSV and JSON evidence generated and checked.
- Missing-field SVG chart generated and committed.

## Limitations

The dataset is simulated, the analysis is descriptive, and there is no production source connection. The findings must not be represented as VELOOP company performance or production validation. Missing-value thresholds, field requiredness, identity rules and business definitions require owner confirmation.


## Supplemental synthetic test pack — separate testing layer

The Task 01 brief expects dataset-level profiling, relationship tests, data-quality checks and sample KPI feasibility. The original Task 01 workbook contains only user-profile clean/messy sheets, so a separately labelled QA-checked synthetic workbook was used to exercise the proposed model. The separate Task 02 workbook was not imported.

| Synthetic dataset | Records | Fields |
|---|---:|---:|
| Task Activity | 6,000 | 12 |
| Rewards | 5,001 | 10 |
| Wallet | 3,552 | 10 |
| Withdrawals | 1,200 | 9 |
| Referrals | 900 | 8 |
| Feature Events | 12,000 | 12 |
| Messy Data | 700 | 12 |
| External References (support table) | 1,977 | 5 |

The 5,001 Rewards and 3,552 Wallet rows include synthetic support records added for correction/reversal testing. All added records are marked as synthetic test data.

### Relationship and chronology results

- Zero unmatched user IDs across the tested synthetic user relationships.
- Zero unmatched reward-to-task-activity links.
- Zero unmatched reward correction links among populated values.
- Zero unmatched wallet reversal links among populated values.
- Zero chronology violations in task completion-before-start, withdrawal final-before-processing, and referral activation-before-registration checks after QA correction.
- Review flags remain: one self-referral and 52 wallet reference IDs not matched in the broad domain/external-reference check. These are explicitly reported rather than silently treated as passes.

### Intentional defects in the Messy_Data test sheet

| Check | Records |
|---|---:|
| Missing activity IDs | 8 |
| Duplicate non-null activity ID rows beyond first | 11 |
| Malformed nonblank task-viewed timestamps | 9 |
| Invalid task statuses | 9 |
| Whitespace-only failure reasons | 12 |
| Negative numeric values in reward_status | 14 |

### KPI feasibility example

The synthetic Task Activity table contains 6,000 rows with 6,000 start timestamps and 3,229 rows whose status is `completed`. This yields a **53.82% completed-status share** for this generated test pack only. It is not a production completion rate or a company target; a business KPI still requires an approved eligibility definition, denominator and cohort-maturity rule.

Reward amounts are grouped by unit and status; units are never combined. Pending/open withdrawal states are kept separate from terminal states.

Reproducible files: [synthetic profiling script](../analytics/python/analyze_synthetic_pack.py), [SQL checks](../analytics/sql/synthetic_test_pack_analysis.sql), [dataset profile](../analytics/evidence/synthetic_dataset_profile.csv), [relationship checks](../analytics/evidence/synthetic_relationship_checks.csv), [quality checks](../analytics/evidence/synthetic_quality_checks.csv), and [dataset-size visualization](../analytics/evidence/synthetic_dataset_record_counts.svg).

**Limit:** This layer tests analytical logic with generated data. It does not establish actual reward, wallet, withdrawal, referral or feature-event performance at VELOOP.
