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

## Current interactive workspace: scope and evidence (updated 28 October 2026)

The current reviewer-facing website is the Next.js/Vercel app at https://velop-task01-data-analytics.vercel.app/. It has seven sections: Executive status (Home), Insights & recommendations (Findings), Supplied data audit (Data audit), Deliverable tracker (Deliverables), Seven-dashboard blueprint (Dashboard plan), Acceptance blockers (What remains), and Implementation library (Documents). These are seven navigation sections in a design/evidence workspace, **not seven live production dashboards**.

The separate Streamlit app at https://velop-task01-data-analytics.streamlit.app/ is a legacy/prototype evidence workspace. References below to five navigation views, 22 programmed quality checks, synthetic task/reward/wallet/withdrawal/referral tables, and CSV quality reports describe that Streamlit prototype only; they must not be attributed to the current Vercel app unless the same feature is independently confirmed there.

## Current interactive demo: legacy Streamlit prototype notes

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
- The Streamlit prototype uses five navigation views. The current Vercel workspace has seven navigation sections. Neither should be described as seven independent production dashboards; the seven dashboard areas are a documented blueprint.
- Test the deployed URL after the hosting service finishes redeploying. A successful GitHub commit does not by itself confirm successful deployment or browser rendering.

## Review checklist (deferred by project owner until a later QA pass)

- [ ] Verify the latest Vercel deployment and all seven navigation sections.
- [ ] Verify findings search/priority filters, CSV exports, source/document links, and responsive layout.
- [ ] Verify the separate Streamlit prototype only if it remains in scope: five views, 22 quality rules, CSV outputs, filters and no-match fallback.
- [ ] Confirm synthetic-data warnings are visible in both apps.
- [ ] Confirm no view presents synthetic records as production results.


## Automated smoke-check workflow

A GitHub Actions workflow is now configured at `.github/workflows/streamlit-smoke-test.yml`. On pushes to `main`, pull requests targeting `main`, or manual dispatch, it installs the declared dependencies, compiles the Streamlit app, starts the app headlessly and checks the Streamlit health endpoint. This validates startup/health only; it does not replace interactive browser testing of each view, filter, chart and download.

**Current verification status:** workflow file committed; no completed green workflow result has been confirmed yet. The live Streamlit URL could not be fetched from the current environment, so deployment status and rendered UI remain unverified here.


## Requirement-to-evidence map (reviewer navigation)

| Assignment area | Primary evidence | Website location | Evidence status / caveat |
|---|---|---|---|
| Executive summary, findings and recommendations | Consolidated report; `docs/ANALYTICS_FOUNDATION_IMPLEMENTATION_PACK.md` | Executive status; Insights & recommendations | Design and simulated profile findings; not production performance |
| Product/data coverage and source inventory | Implementation pack; source register; `docs/THREE_SOURCE_FILES_AUDIT.md` | Supplied data audit; Implementation library | Source-limited; Task 02 stays separate pending approval |
| User/account data profile and quality | `docs/SOURCE_DATA_PROFILE_AND_QUALITY_AUDIT.md` | Supplied data audit | Simulated Task 01 user-profile workbook only; clean-sheet column count needs direct source recheck |
| Data dictionary (90 proposed fields) | `docs/DATA_DICTIONARY_FIELD_INDEX.md` | Implementation library | Proposed field inventory; physical schema needs Engineering confirmation |
| KPI catalogue (36 proposed KPIs) | `docs/ANALYTICS_FOUNDATION_IMPLEMENTATION_PACK.md`; companion design workbook | Seven-dashboard blueprint; Implementation library | Definitions need owner approval and authoritative data |
| Logical model / ERD | Implementation pack and proposed ERD companion artifact | Implementation library | Logical proposal, not verified production schema |
| Event tracking and developer handoff | `docs/DEVELOPER_ANALYTICS_HANDOFF.md` | Implementation library; Acceptance blockers | Proposed contracts; implementation and staging validation pending |
| Seven dashboard areas | `docs/DASHBOARD_VISUAL_SPECIFICATIONS.md` | Seven-dashboard blueprint | Blueprint/specification, not seven live dashboards |
| Pipeline, governance and change control | `docs/ANALYTICS_CHANGE_LOG_AND_OPERATING_MODEL.md` | Implementation library; Acceptance blockers | Proposed operating model; owner/security review pending |
| Gaps, assumptions and implementation backlog | `docs/ANALYTICS_FOUNDATION_IMPLEMENTATION_PACK.md`; `docs/data_gaps_and_kpi_guardrails.md` | Acceptance blockers; Deliverable tracker | External decisions and approvals remain open |
| Website architecture and deployment instructions | `vercel-app/README.md`; repository workflows | Current Vercel workspace | Current site is a reviewer workspace; fresh post-change QA intentionally deferred |
| Today's work and requested coordinator feedback | `docs/TODAYS_PROGRESS_REPORT_2026-10-28.md` | Linked from README after this update | Progress report; asks for quality, errors, improvements, additions and priorities |
