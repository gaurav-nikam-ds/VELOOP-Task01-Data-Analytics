# VELOOP Rewards — Task 01 Analytics Blueprint

**Prepared by:** Gaurav Nikam  
**Assignment:** Product Analytics, Data Readiness & Data Management Blueprint  
**Status:** Deployed evidence workspace; production analytics are not connected or verified.

## Live workspaces

- **Current Vercel workspace:** https://velop-task01-data-analytics.vercel.app/
- [Existing Streamlit evidence workspace](https://velop-task01-data-analytics.streamlit.app/)
- Vercel app source and deployment instructions: [vercel-app/README.md](vercel-app/README.md)

The project owner has recorded manual checks of the deployed Vercel workspace (seven sections, filters, CSV exports, links and responsive layout). In this review, an independent fresh browser fetch could not be completed and the latest Vercel status was pending; do not treat deployment-after-latest-commit as verified. See [Testing evidence & pending QA](docs/FUNCTIONAL_TESTING_EVIDENCE_2026-10-28.md) and [Implemented vs planned features](docs/IMPLEMENTED_VS_PLANNED_FEATURES.md). The [Vercel build workflow](.github/workflows/vercel-app-build.yml) runs the Next.js build for relevant changes.

## What the workspace contains

- **Executive status:** scope, evidence status, data-authenticity guardrail, plain-English glossary and status legend.
- **Insights & recommendations:** four Task 01 user-profile findings; the Task 02 event audit stays separate until scope approval.
- **Supplied data audit:** source-workbook row counts and documented quality findings.
- **Deliverable tracker:** 21 tracked deliverables and outstanding dependencies.
- **Seven-dashboard blueprint:** dashboard areas required by the assignment and their source/approval dependencies.
- **Acceptance blockers:** production data, scope, owner sign-off and remaining acceptance gates.
- **Implementation library:** implementation specifications and handoff documents.

## Source and authenticity rules

The assignment brief identifies the supplied data as simulated. The Task 01 workbook includes user-profile clean and messy tabs; it does not provide the complete task/reward/wallet/withdrawal/referral/event transaction pack described in the brief. The separate behavior workbook identifies itself as Task 02 and is not merged into Task 01 without coordinator approval.

**No generated transaction rows or invented business-performance metrics are presented as VELOOP company results.** The row counts and quality findings shown in the workspace are audit findings from the supplied assignment workbooks, which are simulated source material—not actual production statistics. No production database/API connection is configured.

Proposed fields, events, KPI definitions, data models, governance controls and pipeline steps require confirmation by Product, Engineering, Operations/Finance and Security/Legal before implementation or production reporting.

## Today's progress report

- [Daily progress report — 28 October 2026](docs/TODAYS_PROGRESS_REPORT_2026-10-28.md) — today's documentation/scope alignment, remaining dependencies, and coordinator questions about work quality, errors, improvements and additions.

## Requirements and evidence

- [Analytics foundation implementation pack](docs/ANALYTICS_FOUNDATION_IMPLEMENTATION_PACK.md) — source register, product/data coverage map, event contract, identity/grain model, quality controls, proposed KPIs, seven-dashboard blueprint, pipeline, governance, gaps, verification register, backlog and acceptance checklist.
- [Source data profile & quality audit](docs/SOURCE_DATA_PROFILE_AND_QUALITY_AUDIT.md) — recalculated Task 01 workbook profile, missingness, duplicate IDs and cross-tab findings.
- [Data dictionary field index](docs/DATA_DICTIONARY_FIELD_INDEX.md) — 90-field inventory and field governance rules.
- [Developer analytics handoff](docs/DEVELOPER_ANALYTICS_HANDOFF.md) — proposed event contract, lifecycle events and acceptance tests.
- [Seven-dashboard visual specifications](docs/DASHBOARD_VISUAL_SPECIFICATIONS.md) — visual-level formulas, sources, filters, questions and decisions for all seven areas.
- [Analytics change log & operating model](docs/ANALYTICS_CHANGE_LOG_AND_OPERATING_MODEL.md) — ownership, review workflow, monitoring, incident handling and release acceptance.
- [Task 01 requirements-to-evidence checklist](docs/TASK01_REQUIREMENTS_CHECKLIST.md)
- [Implemented vs planned features](docs/IMPLEMENTED_VS_PLANNED_FEATURES.md)
- [Functional testing evidence and pending QA](docs/FUNCTIONAL_TESTING_EVIDENCE_2026-10-28.md)
- [Three-source-file audit and acceptance status](docs/THREE_SOURCE_FILES_AUDIT.md)
- [Data gaps and KPI guardrails](docs/data_gaps_and_kpi_guardrails.md)
- [Streamlit smoke test workflow](.github/workflows/streamlit-smoke-test.yml)
- [Vercel app build workflow](.github/workflows/vercel-app-build.yml)

## Run locally

### Vercel / Next.js version

```bash
cd vercel-app
npm install
npm run dev
```

Build validation:

```bash
npm install
npm run build
```

### Streamlit version

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Remaining external acceptance gates

1. Authorized production datasets were not supplied; actual company KPIs cannot be calculated.
2. Task 02 scope must be confirmed before reuse.
3. Company owners must approve canonical identifiers, event triggers/payloads, reward units, wallet semantics, withdrawal states and KPI definitions.
4. The project owner/coordinator must confirm whether any additional company-specific submission or sign-off is required.

**Integrity rule:** do not claim production readiness or company performance without direct evidence and owner approval.
