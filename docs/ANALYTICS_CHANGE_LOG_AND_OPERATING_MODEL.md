# Analytics Change Log & Operating Model — Task 01

**Status:** proposed operating procedure for approval by Product, Engineering, Analytics, Finance/Operations and Security/Legal.

## Change log template

Every event, field, KPI, model, dashboard or pipeline change must record:

| Field | Requirement |
|---|---|
| change_id | Unique identifier |
| submitted_at / effective_at | Request and effective timestamps |
| change_type | Event / schema / KPI / model / dashboard / pipeline / access policy |
| summary | Concise description |
| reason / business question | Why the change is needed |
| requester / owner | Named role or accountable team |
| affected producers / consumers | Services, tables, metrics, dashboards, exports |
| compatibility | Backward-compatible / breaking / migration required |
| data backfill | Required / not required / unknown with reason |
| validation plan | Unit, schema, reconciliation and dashboard tests |
| privacy/security impact | Reviewed / not applicable with rationale / pending |
| approvals | Product, Engineering, Analytics, Finance/Ops, Security as applicable |
| release/version | Schema, metric or model version |
| rollback plan | Steps and owner |
| status | Proposed / In review / Approved / Implemented / Verified / Rolled back |
| evidence | PR, test report, run ID, decision record |

## Proposed change workflow

1. Requester documents business purpose, affected definitions and desired effective date.
2. Data owner checks source evidence and identifies downstream consumers.
3. Product/Engineering approve feature semantics and producer behavior.
4. Analytics approves metric impact, denominator, cohort/date semantics and comparability.
5. Finance/Operations approves any reward, wallet, exchange or withdrawal semantics.
6. Security/Legal reviews sensitive fields, access, retention and export impact.
7. Engineering versions schema/contracts; breaking changes require migration plan and explicit version.
8. CI validates schema, allowed values, uniqueness/idempotency, state transitions and compatibility.
9. Staging test data is validated; production rollout is monitored.
10. Analytics checks dashboards, reconciliation, freshness and historical comparability.
11. Mark Verified only after recorded evidence; otherwise retain Pending/To Be Verified.
12. Communicate the effective date and known comparability breaks to dashboard consumers.

## Proposed operating ownership

| Domain | Accountable role | Responsibilities |
|---|---|---|
| Product semantics | Product Owner | Feature existence, business states, eligibility and user journey |
| Instrumentation | Engineering | Event emission, IDs, timestamps, payload contract and tests |
| Data pipeline | Data Engineering | Ingestion, raw preservation, validation, deduplication, curated models, freshness |
| KPI definitions | Product Analytics | Formula, grain, denominator, cohort logic, interpretation and limitation |
| Reward/wallet integrity | Finance + Engineering | Ledger source of truth, transaction state, reversal/correction and reconciliation |
| Withdrawal operations | Finance/Operations | Request states, payout outcomes, failure categories and SLA |
| Referral attribution | Product/Growth | Attribution source/window, activation and eligibility |
| Access/privacy | Security/Legal | Data minimisation, access, retention, deletion and incident policy |
| Dashboard consumers | Business owners | Decision use, feedback, definition acceptance and escalation |

## Monitoring and incident process

- Alert on failed critical checks, stale loads, schema drift, unusual volume, duplicate business transactions, orphan keys and ledger reconciliation differences.
- Every alert should include source, affected date range, severity, first-seen time, owner, run ID and evidence link.
- Quarantine invalid data where possible; never silently repair financial or identity data.
- Block affected KPI publication when critical correctness is uncertain.
- Keep raw evidence according to approved retention and access policies.
- Record root cause, corrective action, preventive action and verification run.
- Communicate whether historical metrics were restated and why.

## Release acceptance

A change is not complete merely because code merged. It is complete only when the relevant contract tests pass, data is validated, dashboard impact is reviewed, approvals are recorded and rollback/monitoring are ready.
