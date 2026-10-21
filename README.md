# VELOOP Rewards — Task 01 Analytics Blueprint

**Prepared by:** Gaurav Nikam  
**Task:** Product Analytics, Data Readiness & Data Management Blueprint  
**Status:** Analytical design and interactive demo prototype; production implementation is not verified.

## Live demo
[Open the Streamlit dashboard](https://veloop-task01-data-analytics.streamlit.app/)

The live URL is published separately from this repository. A deployment link alone does not prove the app has passed browser smoke testing.

## Included in this repository
- `app/streamlit_app.py`: self-contained interactive Streamlit dashboard prototype.
- `docs/data_gaps_and_kpi_guardrails.md`: evidence gaps and KPI interpretation rules.
- `requirements.txt`: runtime dependencies.

**Note:** The complete Task 01 submission report, design workbook, supplemental synthetic workbook and diagrams are bundled separately in the QA-clean submission ZIP. They are not currently stored as individual files in this GitHub repository.

## Demo data status
**SIMULATED DATA — CREATED FOR ANALYTICAL TESTING.** The app generates small illustrative sample records in code. These are not VELOOP production data and must not be reported as company performance. No production-system connection is configured.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Before company sign-off
1. Confirm whether authorized production datasets exist for tasks, rewards, wallet, withdrawals, referrals and feature events.
2. Have Product/Engineering confirm live vs planned features, event payloads, identifiers, timezone and status enums.
3. Have Operations/Finance confirm reward units, wallet ledger semantics, withdrawal states and reconciliation rules.
4. Have Security/Legal confirm retention, access roles and consent requirements.
5. Recalculate and approve KPIs using authorized production extracts before reporting business performance.
