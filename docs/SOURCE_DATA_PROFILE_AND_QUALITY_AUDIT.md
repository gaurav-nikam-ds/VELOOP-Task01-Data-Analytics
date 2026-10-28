# Task 01 — Supplied Source Data Profile & Quality Audit

## Scope and authenticity

Source inspected: `VELoop_Rewards_Data_01(2).xlsx`, sheets `Users_1000_Clean`, `Users_Messy_Audit`, `Data_Dictionary`, `Synthetic_Summary`, and `README_Data_Status`.

The workbook labels the assignment data as simulated. All results below describe this supplied file only; they are not production VELOOP statistics.

## Workbook inventory

| Sheet | Grain / purpose | Rows | Columns | Review status |
|---|---|---:|---:|---|
| Users_1000_Clean | Simulated user-profile table | 1,000 | 28 header cells (27 named fields + 1 blank trailing header) | Profiled; header count directly rechecked 28 October 2026 |
| Users_Messy_Audit | Intentionally messy user-profile audit table | 1,008 | 28 | Profiled |
| Data_Dictionary | Supplied field definitions | 25 | 5 | Reviewed |
| Synthetic_Summary | Source-provided summary | Inspect source tab before reuse | — | Source sheet retained |
| README_Data_Status | Source-provided data status and caveats | Inspect source tab before reuse | — | Source sheet retained |

**Column-count reconciliation (verified 28 October 2026):** the original `VELoop_Rewards_Data_01(2).xlsx` workbook was reopened and the `Users_1000_Clean` header row was counted directly. It contains **28 header cells, of which 27 are named fields and the final header cell is blank (`None`)**. `Users_Messy_Audit` contains 28 named fields, including `data_environment`. The earlier 27-vs-28 discrepancy arose from counting only non-empty clean-sheet header names in one record versus all header cells in another. For schema clarity, report both counts: 28 physical header cells / 27 named fields. The source workbook remains unchanged.

## Clean user-profile findings

| Check | Result | Interpretation |
|---|---:|---|
| Row count | 1,000 | Supplied simulated profile records |
| Header cells / named fields | 28 / 27 | The last header cell is blank; 27 fields have names. Do not treat the blank header as a usable field. |
| Unique non-null user IDs | 1,000 | User ID is unique at the row grain in this sheet |
| Exact duplicate rows | 0 | No exact duplicate rows detected |
| Missing referral_source_detail | 881 / 1,000 (88.1%) | High missingness; confirm whether detail is optional, not collected, unknown, or not applicable |
| Missing last_login_datetime | 72 / 1,000 (7.2%) | Last-login recency should not be inferred for missing timestamps |
| is_active_7d = Yes | 78 / 1,000 (7.8%) | Supplied simulated flag only; active-user definition is not independently established by this flag |
| is_active_30d = Yes | 325 / 1,000 (32.5%) | Supplied simulated flag only; not production retention |
| onboarding_status = Completed | 722 / 1,000 (72.2%) | Profile attribute distribution; not an event-based funnel conversion |
| email_verification_status = Verified | 855 / 1,000 (85.5%) | Profile attribute distribution; state history not supplied |

## Recomputed 30-day activity cross-tabs

The following were recalculated from the 1,000 rows in `Users_1000_Clean` using `is_active_30d == "Yes"`. The percentage is active-flagged profiles divided by all profiles in that category.

### Acquisition source

| Acquisition source | Profiles | Active flag Yes | Share |
|---|---:|---:|---:|
| Telegram | 55 | 27 | 49.1% |
| Referral | 119 | 43 | 36.1% |
| Other | 102 | 34 | 33.3% |
| Organic Search | 244 | 80 | 32.8% |
| WhatsApp | 103 | 32 | 31.1% |
| Social Media | 160 | 49 | 30.6% |
| Direct | 217 | 60 | 27.6% |

### Onboarding status

| Status | Profiles | Active flag Yes | Share |
|---|---:|---:|---:|
| Completed | 722 | 249 | 34.5% |
| Not Started | 132 | 38 | 28.8% |
| Started | 146 | 38 | 26.0% |

### Email verification status

| Status | Profiles | Active flag Yes | Share |
|---|---:|---:|---:|
| Verified | 855 | 305 | 35.7% |
| Pending | 145 | 20 | 13.8% |

### Account status consistency caution

| Account status | Profiles | Active flag Yes | Active share |
|---|---:|---:|---:|
| Active | 568 | 205 | 36.1% |
| Inactive | 283 | 95 | 33.6% |
| Suspended | 77 | 25 | 32.5% |
| Pending Verification | 72 | 0 | 0.0% |

The file contains profiles marked Inactive or Suspended while the `is_active_30d` flag is Yes. This is not automatically an error because the fields may represent different states or timestamps. It is a **definition/timing inconsistency to verify** before using account status as an eligibility filter.

## Messy user-profile audit findings

| Check | Result | Severity | Recommended handling |
|---|---:|---|---|
| Rows | 1,008 | Informational | Preserve raw row count for audit |
| Columns | 28 | Informational | One additional field vs clean sheet requires schema comparison |
| Unique user IDs | 1,000 | High | Eight excess rows relative to unique ID count |
| Repeated user IDs | 8 repeated IDs | High | Inspect duplicate groups; do not blindly drop rows without a survivorship rule |
| Missing registration timestamp | 1 | High | Quarantine/flag for lifecycle/cohort metrics |
| Missing last-login timestamp | 73 | Medium/High | Preserve null semantics; don't infer inactivity |
| Missing referral_source_detail | 885 | Medium/High | Classify missingness before attribution analysis |
| Negative days_since_registration | 4 | High | Recompute from canonical registration timestamp and agreed as-of date; flag impossible chronology |

## Quality rules to run on every authorized extract

1. Schema/column contract and data-type checks.
2. Primary-key uniqueness and null checks at the declared grain.
3. Duplicate exact-row and duplicate-business-key checks separately.
4. Timestamp parsing, timezone normalization and chronology checks.
5. Allowed-value checks for account, onboarding, verification, platform and consent fields.
6. Numeric range and integer/precision checks for counts, age and balances.
7. Missingness by field and segment; separate unknown/not collected/not applicable where source semantics support it.
8. Foreign-key/orphan checks when linked tables are supplied.
9. Cross-field consistency checks, including account status vs activity flag.
10. Source freshness and load completeness checks.
11. Reconciliation checks for rewards, wallet and withdrawals when authoritative ledgers are supplied.
12. Duplicate event/idempotency checks only when event-level sources are authorized and their event key is defined.

## Findings that cannot be made from this user-profile workbook

The workbook alone does not establish task completion, reward crediting, wallet balances/reconciliation, withdrawal approvals/failures/latency, referral conversion, revenue, or event delivery quality. These require authoritative event/transaction tables and approved metric definitions.

## Acceptance criteria

- The source workbook is retained unchanged as evidence.
- Every issue has an identifier, field, issue type, affected-record count, severity, detection logic, likely cause, correction, prevention, owner and status.
- Corrections are applied in a derived layer, not by overwriting raw source values.
- KPI publication is blocked when critical financial or identity checks fail.
- Every output carries the simulated-data warning until approved production sources are used.
