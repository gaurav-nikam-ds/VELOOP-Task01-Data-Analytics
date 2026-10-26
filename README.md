# VELOOP Rewards — Task 01 Analytics Blueprint

**Prepared by:** Gaurav Nikam  
**Assignment:** Product Analytics, Data Readiness & Data Management Blueprint  
**Status:** Source-grounded review workspace; production analytics are not connected or verified.

## Live workspace

[Open the published Streamlit workspace](https://velop-task01-data-analytics.streamlit.app/)

The workspace is being changed to use only findings grounded in the supplied assignment files and audit. A GitHub commit or passing CI run does not by itself prove that the public deployment has refreshed; confirm the deployed page after Streamlit finishes redeploying.

## What the workspace contains

- **Executive status:** scope, evidence status and data-authenticity guardrail.
- **Supplied data audit:** source-workbook row counts and documented quality findings.
- **Deliverable tracker:** all 21 required final deliverables and their outstanding dependencies.
- **Seven-dashboard blueprint:** the dashboard areas required by the assignment and their source/approval dependencies.
- **Acceptance blockers:** hosting, production data, scope, owner sign-off and browser-QA gates.

## Source and authenticity rules

The assignment brief identifies the supplied data as simulated. The Task 01 workbook includes user-profile clean and messy tabs; it does not provide the complete task/reward/wallet/withdrawal/referral/event transaction pack described in the brief. The separate behavior workbook identifies itself as Task 02 and is not merged into Task 01 without coordinator approval.

**No generated transaction rows or invented business-performance metrics are presented as VELOOP company results.** The row counts and quality findings shown in the workspace are audit findings from the supplied assignment workbooks, which are simulated source material—not actual production statistics. No production database/API connection is configured.

Proposed fields, events, KPI definitions, data models, governance controls and pipeline steps require confirmation by Product, Engineering, Operations/Finance and Security/Legal before implementation or production reporting.

## Requirements and evidence

- [Task 01 requirements-to-evidence checklist](docs/TASK01_REQUIREMENTS_CHECKLIST.md)
- [Three-source-file audit and acceptance status](docs/THREE_SOURCE_FILES_AUDIT.md)
- [Data gaps and KPI guardrails](docs/data_gaps_and_kpi_guardrails.md)
- [GitHub Actions smoke test](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/workflows/streamlit-smoke-test.yml)

## Local run

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Known acceptance gates

1. The assignment email specifies **Vercel or Netlify**. The current Streamlit Community Cloud URL does not meet that instruction unless the coordinator approves an exception.
2. Authorized production datasets were not supplied; actual company KPIs cannot be calculated.
3. Task 02 scope must be confirmed before reuse.
4. Company owners must approve canonical identifiers, event triggers/payloads, reward units, wallet semantics, withdrawal states and KPI definitions.
5. GitHub Actions checks dependency installation, Python compilation, app startup and health endpoint. Full interactive browser and responsive QA remains separate.

**Integrity rule:** do not claim production readiness or company performance without direct evidence and owner approval.
