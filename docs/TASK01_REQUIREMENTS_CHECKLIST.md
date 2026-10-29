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

The Vercel/Next.js website is the sole active reviewer workspace and QA target: https://velop-task01-data-analytics.vercel.app/. It has seven navigation sections, which are reviewer pages in a design/evidence workspace—not seven live production dashboards.

## Current live QA status (29 October 2026)

- [x] Live Playwright browser QA passed **11/11 tests**: [GitHub Actions run](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/runs/40846636363).
- [x] Next.js production build passed: [GitHub Actions run](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/runs/40846636252).
- [x] All seven navigation sections, findings search/priority filter, two CSV exports, eight implementation-library links, accessible control names/unique IDs, and no failed requests or browser errors were tested.
- [x] Responsive overflow check passed at 320, 360, 390, 768, 1024 and 1440 px.
- [x] Automated WCAG 2.1 A/AA scan passed on all seven sections.
- [x] Data-authenticity notice is checked by the browser suite.
- [ ] Obtain coordinator/company approval for scope and proposed specifications.
- [ ] Publish or attach the required final report, design workbook and companion diagrams in the submission location specified by the assignment.

## Validation boundaries

- A passing programmed check only confirms the tested behavior on the deployed reviewer workspace.
- The supplied assignment data is simulated; it is not evidence of actual VELOOP performance or production data quality.
- No production database/API integration, event instrumentation or analytics pipeline is configured.
- Task 02 behavior data must remain separate from Task 01 unless the coordinator explicitly approves reuse.
- Seven dashboard areas are documented specifications, not seven deployed production dashboards.
- Company confirmation, authoritative production extracts, event implementation, metric approval, reconciliation and governance sign-off remain external dependencies.

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
| Website architecture and deployment instructions | `vercel-app/README.md`; repository workflows | Current Vercel workspace | Current site is a reviewer workspace; owner-reported manual checks are documented, but independent post-change browser re-run remains unverified |
| Today's work and requested coordinator feedback | `docs/TODAYS_PROGRESS_REPORT_2026-10-28.md` | Linked from README after this update | Progress report; asks for quality, errors, improvements, additions and priorities |
