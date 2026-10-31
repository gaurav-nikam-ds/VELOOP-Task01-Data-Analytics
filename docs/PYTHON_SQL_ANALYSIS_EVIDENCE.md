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
