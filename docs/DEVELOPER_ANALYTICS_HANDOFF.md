# Developer Analytics Handoff — Task 01

**Status:** Proposed specification; not evidence that production instrumentation exists. Engineering and Product approval is required before implementation.

## 1. Required event envelope

| Field | Type | Requirement | Validation |
|---|---|---|---|
| event_id | UUID/string | Required | Unique event identity; duplicate delivery must be idempotent |
| event_name | string | Required | Approved snake_case catalogue value |
| event_version | integer/string | Required | Versioned payload contract |
| event_timestamp | UTC timestamp | Required | Parseable; event occurrence time |
| received_timestamp | UTC timestamp | Required | Ingestion time; supports latency monitoring |
| user_id | stable pseudonymous ID | Conditional | Required for account-scoped events; anonymous pre-account events follow approved rules |
| session_id | string/UUID | Conditional | Required for session-scoped analysis |
| transaction_id | string/UUID | Conditional | Required for reward/wallet/withdrawal business transactions |
| attempt_id | string/UUID | Conditional | Required for each task attempt/retry |
| feature_name | controlled string | Required | Approved product-area taxonomy |
| platform | controlled enum | Required | Approved platform list |
| environment | controlled enum | Required | production/staging/test; never infer |
| source_system | string | Required | Client/service/partner producer |
| status | controlled enum | Conditional | State vocabulary approved by domain owner |
| properties | JSON object | Required | Allow-listed event-specific fields only |
| schema_version | string | Required | Version used for validation |
| idempotency_key | string | Conditional | Required for retry-prone transactional events |
| correlation_id | string | Conditional | Workflow correlation; not a replacement for entity IDs |

## 2. Event catalogue and trigger definitions

All events remain Proposed until feature existence and producer implementation are verified.

| Event | Trigger | Producer | Required identifiers / properties | Business outcome measured |
|---|---|---|---|---|
| registration_started | Signup flow begins | Client | event_id, timestamp, platform, source | Signup funnel entry |
| registration_completed | Signup accepted by backend | Backend | user_id, event_id, timestamp | Successful registration |
| login_succeeded | Authentication succeeds | Backend | user_id, session_id, timestamp | Authenticated activity |
| login_failed | Authentication rejected | Backend | timestamp, controlled failure category; avoid secrets | Login failure rate |
| onboarding_step_started | Step opens | Client/backend as agreed | user_id, step_id, timestamp | Step entry |
| onboarding_step_completed | Step validated complete | Backend preferred | user_id, step_id, timestamp | Step completion |
| task_viewed | Task details become visible under approved rule | Client | user_id, task_id, timestamp, placement | Task discovery |
| task_started | Backend accepts task attempt | Backend | user_id, task_id, attempt_id, timestamp | Attempt creation |
| task_submitted | User submits result | Client/backend as agreed | attempt_id, task_id, timestamp | Submission |
| task_validation_succeeded | Server validation passes | Backend | attempt_id, validation_id, timestamp | Validated task completion |
| task_validation_failed | Validation fails | Backend | attempt_id, controlled reason code, timestamp | Failure analysis |
| reward_pending | Eligible reward enters pending state | Backend/ledger | reward_transaction_id, user_id, amount, unit, timestamp | Pending reward queue |
| reward_credited | Authoritative ledger credits reward | Ledger service | reward_transaction_id, transaction_id, amount, unit, timestamp | Actual credit |
| reward_reversed | Reversal transaction is posted | Ledger service | reversal_id, original reward transaction ID, reason, timestamp | Reversal tracking |
| reward_corrected | Correcting transaction is posted | Ledger service | correction_id, original transaction ID, reason, timestamp | Correction tracking |
| wallet_transaction_recorded | Ledger entry commits | Wallet/ledger service | wallet_transaction_id, user_id, direction, amount, unit, related transaction ID | Wallet movement |
| withdrawal_requested | Request accepted for processing | Backend | withdrawal_id, user_id, amount, unit, timestamp | Request volume |
| withdrawal_state_changed | Request state transitions | Backend/operations system | withdrawal_id, old/new state, timestamp, reason code | State aging and processing time |
| withdrawal_payout_result | Payout provider returns result | Backend/provider adapter | withdrawal_id, provider reference, outcome, timestamp | Payout success/failure |
| referral_attributed | Valid referral attribution is assigned | Backend | referral_id, referrer_id, referred_user_id where available, attribution source, timestamp | Referral funnel |
| referral_activated | Approved activation rule is met | Backend/analytics | referral_id, referred_user_id, timestamp, rule version | Referral activation |
| feature_used | Approved feature action succeeds | Client/backend | user_id, feature_name, action, timestamp | Feature adoption |
| analytics_event_rejected | Event fails ingestion validation | Collector | event_id if available, schema version, reason code, received timestamp | Telemetry quality |

## 3. State and ledger rules

- Distinguish action events from validated business outcomes.
- Task completion is not synonymous with task submission.
- A reward is credited only when the authoritative ledger records the credit.
- Reversals and corrections are new traceable transactions linked to the original transaction; do not silently overwrite history.
- Withdrawal request, approval, payout processing, terminal outcome and rejection/failure are distinct states with timestamps.
- Store event time and received time separately.
- Define allowed state transitions with domain owners; reject or quarantine unknown transitions rather than mapping silently.
- Retry-prone transactional writes must use idempotency keys.
- Never put passwords, access tokens, full payment credentials or unnecessary personal information in event payloads.

## 4. Acceptance tests

| Test ID | Scenario | Expected result | Priority |
|---|---|---|---|
| AT-01 | Valid event with all required fields | Accepted and queryable | Critical |
| AT-02 | Duplicate event_id sent twice | One logical event after idempotent handling; duplicate logged | Critical |
| AT-03 | Missing required user_id on an account-scoped event | Rejected/quarantined with reason; not silently assigned a fake ID | High |
| AT-04 | Invalid timestamp or unparseable timezone | Rejected/quarantined; raw payload retained under policy | High |
| AT-05 | Unknown event_name or event_version | Rejected/quarantined and schema-drift alert raised | High |
| AT-06 | Reward credit event without ledger transaction identity | Blocked from financial KPI layer | Critical |
| AT-07 | Reward reversal references a non-existent original transaction | Quarantined and reconciliation alert raised | Critical |
| AT-08 | Withdrawal jumps from requested to an unapproved terminal state | Transition rejected/flagged with evidence | Critical |
| AT-09 | Retry of the same withdrawal/reward transaction | No duplicate business ledger entry | Critical |
| AT-10 | Task submission arrives but validation fails | Submission counted; validated completion not counted | High |
| AT-11 | Stale source load exceeds agreed SLA | Dashboard marked stale; owner alerted | High |
| AT-12 | Critical reconciliation check fails | Financial dashboard publication blocked or clearly marked unavailable | Critical |
| AT-13 | New optional property is added with compatible schema version | Contract compatibility test passes | Medium |
| AT-14 | Breaking field/type change is introduced without version update | CI/schema validation fails | High |
| AT-15 | Payload includes prohibited secret or unapproved sensitive field | Payload rejected/redacted and incident path followed | Critical |

## 5. Minimum handoff package from Engineering

- Approved event catalogue and versioned schemas.
- Example payloads using clearly labelled test values.
- Producer/consumer ownership and expected delivery SLA.
- Identity and idempotency policy.
- Allowed state transitions for tasks, rewards and withdrawals.
- Data contract CI tests and staging test evidence.
- Monitoring and alert routes.
- Backfill/replay policy and duplicate handling.
- Privacy/security review and approved retention.
- Sign-off that events are actually implemented before any dashboard is labelled production-ready.
