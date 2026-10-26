# Task 01 Requirements-to-Evidence Checklist

**Source of truth:** VELOOP Rewards Data Analyst Internship — Task 01, *Product Analytics, Data Readiness & Data Management Blueprint* (the supplied 44-page assignment PDF).

**Status key**
- **Designed/documented:** included in the analytical proposal.
- **Prototype:** demonstrated with synthetic data only.
- **Pending verification:** requires real source data, internal confirmation, or engineering approval.
- **Not claimed:** must not be represented as production functionality.

## Assignment requirements and evidence

| # | Assignment requirement | Evidence expected | Current status | Remaining dependency / guardrail |
|---|---|---|---|---|
| 1 | Executive summary (2–4 pages) | Investigation, findings, unknowns, recommendations, risks, priorities | Designed/documented in consolidated report | Confirm internal unknowns with company owners |
| 2 | Product data audit | Product areas, features, actions, system outcomes, transactions, states, measurable outcomes | Designed/documented | Product/Engineering must confirm live vs planned features |
| 3 | Data coverage matrix | Product area, user/system action, outcome, data, event, source, business question, status, priority | Designed/documented in workbook | Validate against actual source systems |
| 4 | User analytics specification | Registration, login, onboarding, account lifecycle and identity keys | Designed/documented | Confirm real identifiers and status semantics |
| 5 | Earning/reward analytics | Task lifecycle, failure categories, pending/credited/reversed/corrected reward states | Designed/documented | Obtain authoritative task and reward data |
| 6 | Wallet/withdrawal analytics | Transaction ledger, units, IDs, states, timestamps, reversals and withdrawal KPIs | Designed/documented | Finance/Operations to confirm ledger and payout source of truth |
| 7 | Referral/engagement analytics | Created → registered → activated → converted; active/returning/feature use | Designed/documented | Approve activation and conversion definitions |
| 8 | Event tracking plan | Event name, trigger, definition, IDs, timestamp, feature, status, properties, types, validation, source, KPI, implementation status | Designed/documented | Engineering review required; proposed events are not live events |
| 9 | Data dictionary: at least 75 meaningful fields | Entity, field, type, definition, example, required, allowed values, validation, source, sensitivity, use, status | 90 proposed field definitions documented | Confirm fields and constraints with Engineering |
| 10 | Logical data model and ER diagram | Entities, keys, relationships and relationship explanations | Designed/documented | Logical model is not a statement of the physical production schema |
| 11 | KPI catalogue: 30+ KPIs | Definition, formula, required fields, source, frequency, stakeholder, purpose, interpretation, limitation, status | 36 KPI definitions documented | Do not publish KPIs until definitions and source data are approved |
| 12 | Simulated data profiling | Profile supplied simulated data and document findings | Original user/audit data profiled; supplemental synthetic datasets exist for testing | Supplemental synthetic tables are not actual company data |
| 13 | Data quality audit | Workbook/report, validation rules, anomalies and interpretation | Prototype now demonstrates 22 checks across five synthetic tables; report downloadable as CSV | This is not the full production audit; run against authorized datasets when supplied |
| 14 | Dashboard blueprint | Seven dashboard areas; every visual specifies metric, calculation, source, visualization, filters, dimensions, date range, refresh, question and decision | Seven dashboard areas specified in report/workbook; interactive demo currently groups some areas into five views | The interactive demo is a prototype, not seven separate production dashboards |
| 15 | Developer analytics handoff | Critical event trigger/payload/validation/deduplication/timestamp/source/KPI/acceptance test/priority | Designed/documented | Engineering sign-off and implementation required |
| 16 | Data pipeline and operating model | Sources, collection, storage, raw layer, validation, transformation, analytics layer, dashboard, refresh, monitoring, failure handling, ownership | Proposed architecture documented | Do not imply pipeline has been deployed |
| 17 | Data access, privacy and governance | Role-based access, data minimisation, secret handling, retention and ownership | Proposed controls documented | Security/Legal review required |
| 18 | Analytics change management | Versioned event/metric change log with impact and owner | Proposed process documented | Adopt with internal owners |
| 19 | Analytics gap assessment | Current vs future needs, evidence gaps, prioritized actions | Documented | Update after company feedback |
| 20 | Assumption & verification register | Unknown, impact, source, risk, owner, verification status | Documented | Keep unconfirmed items marked To Be Verified |
| 21 | Prioritized implementation backlog | Requirement, reason, dependency, owner and stage | Documented | Reprioritize after engineering/product review |
| 22 | Data authenticity policy | Synthetic data must never be reported as actual users, earnings, withdrawals, revenue, retention, conversion or performance | Explicit warnings in report and app | Preserve warning in screenshots, exports and reviews |

## Current interactive demo: recent improvements

1. Decision notes on the Executive Overview calculate the highest-volume domain, highest observed sample completion-rate domain, and rejected/expired share from the selected synthetic sample.
2. Data Readiness now evaluates 22 programmed quality rules across task, reward, wallet, withdrawal and referral prototype tables.
3. The quality table reports observed counts, PASS/REVIEW and an interpretation for each rule.
4. A downloadable CSV quality report is available from the Data Readiness view.
5. The existing date/domain filters and filtered task/KPI CSV exports remain in place.
6. Synthetic-data and no-production-connection warnings remain explicit.

## Validation boundaries

- A passing programmed check means only that the specific rule passed on the generated synthetic records.
- The sample data is not evidence of actual VELOOP performance or production data quality.
- No production database/API integration is configured.
- Company confirmation, production extracts, event implementation, metric approval, reconciliation and governance sign-off remain dependencies.
- The demo uses five navigation views, while the assignment asks for a seven-dashboard **blueprint**. The blueprint is documented separately; do not claim the current app contains seven independent production dashboards.
- Test the deployed URL after the hosting service finishes redeploying. A successful GitHub commit does not by itself confirm successful deployment or browser rendering.

## Review checklist

- [ ] Latest commit is visible in GitHub.
- [ ] Streamlit deployment has completed without errors.
- [ ] Executive Overview shows decision notes that change with filters.
- [ ] Data Readiness displays 22 quality rules.
- [ ] Downloaded quality CSV opens and contains Check, Observed, Result and Interpretation.
- [ ] Existing filtered task and KPI CSV downloads still work.
- [ ] All five navigation views open.
- [ ] Synthetic-data warning remains visible.
- [ ] No-match filter fallback behaves as documented.
