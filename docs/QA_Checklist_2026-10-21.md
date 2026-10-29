> **Historical snapshot — 21 October 2026.** This checklist describes the earlier Streamlit prototype and its then-current checks. It is not the current application acceptance record. The active application is the Vercel/Next.js reviewer workspace. For current results, see [Functional Testing Evidence](FUNCTIONAL_TESTING_EVIDENCE_2026-10-28.md) and [the latest 11/11 live QA run](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/runs/40846636363).

# Task 01 — QA checklist (21 October 2026)

## Automated checks completed
- Python syntax parse for `app/streamlit_app.py`: **PASS**.
- Submission report PDF and editable DOCX present: **PASS**.
- Analytics design workbook contains 32 worksheets: **PASS**.
- Data Dictionary populated entries: **90** (assignment minimum: 75) — **PASS**.
- KPI Catalogue populated entries: **36** (assignment minimum: 30) — **PASS**.
- Event Catalogue populated entries: **40** proposed events — **PASS as a proposal, not proof of live tracking**.
- Supplemental synthetic workbook contains the required task, reward, wallet, withdrawal, referral, feature-event and messy-test domains: **PASS**.
- ERD, proposed pipeline and seven dashboard wireframes included in the submission package: **PASS**.
- ZIP integrity verified; temporary PDF-build files and Python bytecode caches excluded: **PASS**.

## Data and scope controls
- Supplied assignment workbook and supplemental analytics test data are simulated; no output is claimed as actual VELOOP business performance.
- Supplemental transaction-domain records are generated for analytical testing, not extracted from production.
- Task 02 behavior data is not silently merged into Task 01.
- Product implementation, event instrumentation, internal KPI definitions, ledger rules, retention controls and company sign-off remain unverified dependencies.

## Not verified from this environment
- The live Streamlit website could not be fetched from this execution environment because outbound DNS/network access is unavailable. This does **not** prove the site is down.
- Browser rendering, deployment logs, sidebar navigation and chart interactions require a real browser smoke test on the published URL.
- Streamlit is not installed in this environment, so a full local server run was not performed. Python syntax and workbook/schema compatibility were checked.

## Manual release smoke test
1. Open the live dashboard in a browser and confirm it loads without a Streamlit exception.
2. Select all five views in the sidebar and confirm charts/tables appear.
3. Confirm the synthetic-data warning remains visible.
4. Refresh once and verify the page returns normally.
5. If an error appears, capture the full message and fix it before sharing the link.
