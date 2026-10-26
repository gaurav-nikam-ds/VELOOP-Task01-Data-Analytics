# VELOOP Rewards — Task 01 Final Submission Overview

## Purpose and scope

This repository implements a proposed product-analytics foundation for VELOOP Rewards Task 01. It is an analytical design and synthetic-data prototype. It is not connected to VELOOP production systems, and it does not establish company performance.

## Review links

- Live interactive prototype: https://velop-task01-data-analytics.streamlit.app/
- Source repository: https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics
- Requirements-to-evidence checklist: [TASK01_REQUIREMENTS_CHECKLIST.md](TASK01_REQUIREMENTS_CHECKLIST.md)
- Supplied-source audit and open gates: [THREE_SOURCE_FILES_AUDIT.md](THREE_SOURCE_FILES_AUDIT.md)
- KPI/data-gap guardrails: [data_gaps_and_kpi_guardrails.md](data_gaps_and_kpi_guardrails.md)
- CI smoke test: https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/actions/workflows/streamlit-smoke-test.yml

## Required deliverables and current status

| # | Deliverable | Evidence/status | Acceptance dependency |
|---:|---|---|---|
| 1 | Executive summary | Included in consolidated submission package; summarized in source audit | Review of assumptions and internal unknowns |
| 2 | Product data audit | Documented analytical design | Product owner confirms live vs planned features |
| 3 | Data coverage matrix | Included in design workbook | Verify against authoritative source systems |
| 4 | User/account specification | Documented proposal | Confirm IDs, statuses and privacy requirements |
| 5 | Earning/reward specification | Documented proposal | Task 01 workbook lacks the full authoritative reward ledger |
| 6 | Wallet/withdrawal specification | Documented proposal | Operations/Finance approve ledger and payout semantics |
| 7 | Referral/engagement specification | Documented proposal | Approve activation/conversion definitions |
| 8 | Event tracking plan | Proposed event catalogue | Engineering review and staging validation |
| 9 | Data dictionary | 90 proposed field definitions | Physical schema and field constraints require approval |
| 10 | Logical model and ERD | Proposed model and diagram | Not a verified production schema |
| 11 | KPI catalogue | 36 proposed KPIs | Approve formula, denominator, source, units and frequency |
| 12 | Simulated profiling | Task 01 user workbook profiled; Task 02 workbook separately audited | Do not silently mix task scopes |
| 13 | Data quality audit | Source-specific profile and synthetic prototype checks | Run on authorized source data when supplied |
| 14 | Dashboard blueprint | Seven dashboard areas specified; interactive prototype groups them into five views | Prototype is not seven deployed production dashboards |
| 15 | Developer handoff | Proposed implementation specification | Engineering sign-off |
| 16 | Data pipeline proposal | Documented design | Confirm source systems, ownership and operating constraints |
| 17 | Privacy/governance | Proposed controls and access model | Security/Legal review |
| 18 | Analytics readiness assessment | Documented scorecard/design | Owners confirm evidence and readiness state |
| 19 | Assumption/verification register | Documented | Resolve outstanding verification items |
| 20 | Implementation backlog | Prioritized proposal | Company confirms owners, dependencies and priorities |
| 21 | Final consolidated report | Prepared in the QA-clean submission package | Companion artifacts must be published alongside the repository for a complete GitHub handover |

## Interactive prototype

The live app has five views: Executive overview; Engagement & tasks; Rewards & wallet; Withdrawals & referrals; Data readiness. Sidebar controls filter the synthetic task sample by date and domain. Exports are prototype-level CSVs. The app sidebar links back to this repository's checklist, audit and guardrail documents.

## Verification

The GitHub Actions workflow installs dependencies, compiles the Python app, starts Streamlit and checks its health endpoint. A green workflow is a startup smoke test only; it does not certify all charts, interactions, downloads, responsive layouts or the hosted deployment.

## Non-negotiable integrity rules

- Label every generated dataset and metric as simulated.
- Do not report synthetic counts, rates, withdrawals, rewards or retention as actual VELOOP performance.
- Treat proposed events and fields as proposed until engineering confirms implementation.
- Do not add Task 02 data to Task 01 reporting unless the coordinator authorizes reuse.
- Do not claim full hosting compliance until the email's Vercel/Netlify requirement is met or written approval for Streamlit is obtained.

## Final blockers before calling this fully complete

1. Publish the report, design workbook, synthetic test workbook and diagrams as individual repository artifacts or a clearly versioned release asset.
2. Complete live browser QA on desktop and mobile/narrow viewport.
3. Meet the Vercel/Netlify hosting requirement or obtain written approval for the current Streamlit host.
4. Obtain company sign-off for internal assumptions and proposed specifications.
5. Re-run final smoke tests after all changes and record the result.