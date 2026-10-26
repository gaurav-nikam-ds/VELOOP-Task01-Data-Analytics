# VELOOP Rewards — Task 01 Analytics Blueprint

**Prepared by:** Gaurav Nikam  
**Task:** Product Analytics, Data Readiness & Data Management Blueprint  
**Status:** Analytical design and interactive demo prototype; production implementation is not verified.

## Live demo
[Open the Streamlit dashboard](https://veloop-task01-data-analytics.streamlit.app/)

The live URL is published separately from this repository. A deployment link alone does not prove the app has passed browser smoke testing.

## Included in this repository
- `app/streamlit_app.py`: interactive dashboard with executive KPI cards, daily trend lines, domain mix, lifecycle bars, domain comparison, engagement heatmap, duration distributions, reward/wallet views, referral and withdrawal funnels, processing-time analysis, readiness matrix, and sidebar date/domain filters.
- `docs/data_gaps_and_kpi_guardrails.md`: evidence gaps and KPI interpretation rules.
- `docs/THREE_SOURCE_FILES_AUDIT.md`: audit of the supplied Task 01 PDF, Task 01 workbook, Task 02 workbook, hosting requirement and remaining acceptance gates.
- `docs/TASK01_REQUIREMENTS_CHECKLIST.md`: 21-deliverable traceability checklist.
- `requirements.txt`: runtime dependencies.

**Note:** The complete Task 01 submission report, design workbook, supplemental synthetic workbook and diagrams are bundled separately in the QA-clean submission ZIP. They are not currently stored as individual files in this GitHub repository.

## Demo data status
**SIMULATED DATA — CREATED FOR ANALYTICAL TESTING.** The app generates small illustrative sample records in code. These are not VELOOP production data and must not be reported as company performance. No production-system connection is configured.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Latest review improvements

- **Executive Overview:** decision notes summarize the highest-volume domain, the highest observed sample completion-rate domain, and the combined rejected/expired share for the currently selected synthetic sample.
- **Data Readiness:** 22 programmed data-quality rules cover task, reward, wallet, withdrawal and referral demo tables. Each rule reports observed count, PASS/REVIEW and an interpretation.
- **Export:** download the data-quality report as CSV for review. Existing filtered task and KPI-summary exports remain available.
- **Requirements traceability:** [Task 01 requirements-to-evidence checklist](docs/TASK01_REQUIREMENTS_CHECKLIST.md) maps the original assignment deliverables to evidence and outstanding dependencies.

These are genuine prototype improvements, not production data validation. The app still uses synthetic data and has no production source connection. A PASS means only that a programmed check passed on the demo records.

## Before company sign-off
1. Confirm whether authorized production datasets exist for tasks, rewards, wallet, withdrawals, referrals and feature events.
2. Have Product/Engineering confirm live vs planned features, event payloads, identifiers, timezone and status enums.
3. Have Operations/Finance confirm reward units, wallet ledger semantics, withdrawal states and reconciliation rules.
4. Have Security/Legal confirm retention, access roles and consent requirements.
5. Recalculate and approve KPIs using authorized production extracts before reporting business performance.


## Source-scope and submission compliance note

- The Task 01 source workbook supplied for this assignment contains user-profile clean/messy tabs; it does not contain the complete transaction-level task/reward/wallet/withdrawal/referral/event set described in the brief. Supplemental tables are explicitly synthetic testing assets.
- The separately supplied `VELOOP_Simulated_User_Behavior_1000.xlsx` identifies itself as **Task 02**. It is not merged into Task 01 unless the coordinator explicitly approves that scope.
- See [three-file audit and completion status](docs/THREE_SOURCE_FILES_AUDIT.md) for measured findings and the 21-deliverable tracker.
- The current demo is hosted on Streamlit Community Cloud. The assignment email asks for Vercel or Netlify; obtain written approval for Streamlit or deploy a compatible front end on an approved platform before claiming full email compliance.
- GitHub Actions validates Python compilation and app startup/health. It does not replace interactive browser testing across responsive breakpoints, views, filters and downloads.

## Reviewer navigation

- [Task 01 requirements checklist](docs/TASK01_REQUIREMENTS_CHECKLIST.md)
- [Three-source-file audit and acceptance gates](docs/THREE_SOURCE_FILES_AUDIT.md)
- [Data gaps and KPI guardrails](docs/data_gaps_and_kpi_guardrails.md)
- [GitHub Actions smoke test](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/workflows/streamlit-smoke-test.yml)
- [Live interactive demo](https://velop-task01-data-analytics.streamlit.app/)

## Submission integrity

This repository and live demo are a proposed analytical blueprint and interactive prototype, not a production analytics system. Proposed events, fields, KPIs, data models, dashboard specifications, access controls and pipeline steps require owner review. Synthetic data outputs are not VELOOP company performance. The supplied email's Vercel/Netlify hosting instruction remains an open compliance gate until the host is changed or written approval is obtained.