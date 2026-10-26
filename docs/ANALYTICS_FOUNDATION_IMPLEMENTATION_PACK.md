# VELOOP Rewards — Task 01 Analytics Foundation Implementation Pack

**Purpose:** consolidated, source-grounded working specification for the required Task 01 deliverables.  
**Source of truth:** the supplied 44-page Data Analyst Internship — Task 01: Product Analytics, Data Readiness & Data Management Blueprint.  
**Evidence rule:** product implementation facts remain To Be Verified unless directly supported by an approved official/internal source. Supplied assignment workbooks are simulated and must not be represented as production data.

## 1. Executive summary

Task 01 asks for a reusable analytics foundation for a developing product ecosystem, not manufactured performance statistics. The supplied Task 01 workbook contains user-profile clean and messy tabs, dictionary/summary information, but does not provide a complete authoritative production task/reward/wallet/withdrawal/referral/event transaction pack. The separate behavior workbook identifies itself as Task 02 and is not merged into Task 01 without coordinator approval.

The objective is to define what must be collected, how it should be structured, how trustworthiness will be tested, what management should measure, what Engineering must implement, and what the future analytics team should be able to see.

### Decision summary

1. Establish stable user, event, session and transaction identifiers.
2. Implement event tracking across user lifecycle, earning/task lifecycle, reward lifecycle, wallet, withdrawal, referral and feature engagement.
3. Preserve state changes and event timestamps; do not infer successful business outcomes from user actions alone.
4. Add automated quality controls at collection, raw, transformation and reporting layers.
5. Approve KPI definitions and source-of-truth tables before publishing performance metrics.
6. Build the seven specified dashboard areas after reliable source data and definitions exist.
7. Keep unknown product facts, proposed fields/events and owner decisions in a verification register.

## 2. Source and verification register

| ID | Information | Source | Source type | Status | Verification owner / notes |
|---|---|---|---|---|---|
| SRC-01 | Task 01 is an analytics foundation / data-readiness blueprint | Supplied Task 01 PDF, title and final expectation | Official assignment brief | Confirmed | Governing scope |
| SRC-02 | Assignment datasets are fictional/simulated | Supplied Task 01 PDF, data-authenticity policy | Official assignment brief | Confirmed | Never call supplied metrics actual VELOOP performance |
| SRC-03 | Task 01 workbook includes user clean/messy sheets | Supplied Task 01 workbook | Simulated assignment data | Confirmed | Workbook-level scope only |
| SRC-04 | Full authoritative task/reward/wallet/withdrawal/referral/event transaction pack is not present in the reviewed Task 01 workbook | Supplied workbook inspection | Simulated assignment data | Confirmed within reviewed file | Request approved extracts if available |
| SRC-05 | Separate user-behavior workbook labels itself Task 02 | Supplied behavior workbook | Simulated assignment data | Confirmed | Keep separate unless coordinator approves reuse |
| SRC-06 | Current production event coverage, database schema and source-of-truth systems | Not supplied | Unknown | To Be Verified | Product + Engineering |
| SRC-07 | Reward units, conversion rules and ledger semantics | Not supplied | Unknown | To Be Verified | Finance / Operations |
| SRC-08 | Withdrawal state machine and authoritative payout timestamps | Not supplied | Unknown | To Be Verified | Finance / Operations |
| SRC-09 | Hosting approval for Streamlit instead of Vercel/Netlify | Assignment email requests Vercel or Netlify; current URL is Streamlit | Internal instruction / current deployment | To Be Verified | Obtain written exception or deploy compliant frontend |

## 3. Product area and data coverage map

All proposed events below are Proposed until Product/Engineering confirms the feature exists and the event can be emitted.

| Product area | User action | System action / business outcome | Proposed event(s) | Required data | Business question | Status |
|---|---|---|---|---|---|---|
| Registration | Opens/signs up | Account created | registration_started, registration_completed, account_created | user_id, event_id, timestamp, source, platform | Where does signup fail? | Proposed |
| Login/session | Logs in / starts session | Session opened/closed | login_succeeded, login_failed, session_started, session_ended | user_id, session_id, timestamp, platform | How often do users return? | Proposed |
| Onboarding | Starts/completes step | Step recorded | onboarding_step_started, onboarding_step_completed | user_id, step_id, timestamp | Which step has friction? | Proposed |
| Account lifecycle | Views/updates profile | Account state changes | account_status_changed | user_id, old/new status, timestamp, approved reason code | Are account states consistent? | Proposed |
| Task discovery | Views task/offer | Impression recorded | task_viewed, offer_impression | user_id, task_id, source, timestamp | Which tasks are discovered? | Proposed |
| Task execution | Opens/starts task | Task attempt created | task_opened, task_started | user_id, task_id, attempt_id, timestamp | Where do users abandon? | Proposed |
| Task completion | Submits/finishes task | Completion received/validated | task_submitted, task_completed, task_validation_failed | attempt_id, task_id, status, timestamps, failure category | What is completion and failure rate? | Proposed |
| External offer/tracking | Completes partner action | Callback accepted or rejected | partner_postback_received, partner_postback_rejected | partner_event_id, click/reference ID, received_at, outcome | Are partner events lost or duplicated? | Proposed |
| Reward lifecycle | Earns / sees pending reward | Reward pending/credited/reversed/corrected | reward_pending, reward_credited, reward_reversed, reward_corrected | reward_transaction_id, user_id, amount, unit, state, timestamp, source | Are rewards issued accurately? | Proposed |
| Wallet | Opens wallet / transaction | Ledger entry recorded | wallet_transaction_recorded, wallet_balance_snapshot_created | transaction_id, user_id, direction, amount, unit, resulting balance if authoritative | Do ledger entries reconcile? | Proposed |
| Exchange/conversion | Exchanges units | Conversion applied | exchange_requested, exchange_completed, exchange_failed | transaction_id, input/output units and amounts, rate/version, timestamp | Can conversion be audited? | Proposed |
| Withdrawal | Requests payout | Request moves through states | withdrawal_requested, withdrawal_approved, withdrawal_processed, withdrawal_rejected, withdrawal_failed | withdrawal_id, user_id, amount, payout method category, status, state timestamps, failure reason | Where do withdrawals fail or slow down? | Proposed |
| Referral | Shares code / invitee joins | Referral attributed/activated | referral_created, referral_registered, referral_activated, referral_rewarded | referrer_id, referred_user_id, referral_id, attribution source, state timestamps | Which referrals activate? | Proposed |
| Daily reward/streak | Claims daily reward | Claim accepted/rejected; streak updated | daily_reward_claimed, daily_reward_rejected, streak_updated | user_id, claim_id, streak count, reward reference, timestamp | Does the claim flow work reliably? | Proposed |
| Mission/badge/level | Starts/completes milestone | Progress / unlock recorded | mission_started, mission_completed, badge_unlocked, level_changed | user_id, feature_id, milestone_id, timestamp | Which features are used? | Proposed |
| Support/help | Opens FAQ / creates ticket | Article viewed / ticket created | help_article_viewed, support_request_created | user_id where appropriate, article/category, timestamp | What issues create support demand? | Proposed |
| System/data quality | No direct user action required | Event rejected, retry, deduplication | analytics_event_rejected, ingestion_retry, duplicate_event_detected | event_id, schema version, failure code, pipeline timestamp | Is telemetry reliable? | Proposed |

## 4. Minimum event contract

Every event should use a consistent envelope. Fields that are unavailable or not applicable must follow documented rules; do not invent IDs or replace missing values with misleading defaults.

| Field | Type | Required | Rule / purpose | Status |
|---|---|---:|---|---|
| event_id | string/UUID | Yes | Unique event identity; enables deduplication | Proposed |
| event_name | string | Yes | Stable snake_case name from approved catalogue | Proposed |
| event_version | integer/string | Yes | Payload schema version | Proposed |
| event_timestamp | UTC timestamp | Yes | Time the event occurred at source | Proposed |
| received_timestamp | UTC timestamp | Yes | Time ingestion received it; supports latency checks | Proposed |
| user_id | string/UUID | Conditional | Stable pseudonymous account identifier; null only for approved pre-account events | Proposed |
| session_id | string/UUID | Conditional | Session-scoped analysis where relevant | Proposed |
| transaction_id | string/UUID | Conditional | Stable business transaction identity for reward/wallet/withdrawal events | Proposed |
| feature_name | string | Yes | Approved product area / feature | Proposed |
| platform | enum | Yes | Approved client platform values | Proposed |
| environment | enum | Yes | production/staging/test, never inferred | Proposed |
| source_system | string | Yes | Producer service or client source | Proposed |
| status | enum/string | Conditional | Approved lifecycle state, not free-form variants | Proposed |
| properties | object | Yes | Event-specific allow-listed attributes | Proposed |
| schema_version | string | Yes | Contract version used for validation | Proposed |
| idempotency_key | string | Conditional | Required for retry-prone business events | Proposed |
| correlation_id | string | Conditional | Links related workflow events without replacing entity IDs | Proposed |

## 5. Identity, grain and logical model rules

- User grain: one canonical account row per user_id; profile snapshots must be timestamped if history is needed.
- Event grain: one emitted event per event_id; duplicate delivery must be idempotent.
- Session grain: one session per session_id, linked to a user when known.
- Task-attempt grain: one row per attempt_id; task ID alone cannot distinguish retries.
- Reward transaction grain: one immutable reward ledger transaction per reward_transaction_id; reversals/corrections should reference the original transaction rather than silently overwrite it.
- Wallet ledger grain: one immutable ledger entry per wallet_transaction_id; balance snapshots are not a substitute for the ledger.
- Withdrawal grain: one request per withdrawal_id, with a separate state-history record for each transition.
- Referral grain: one referral relationship per referral_id, with referrer and referred-user identities governed by privacy controls.
- Feature event grain: one event per event_id; use a common event envelope and event-specific properties.

### Logical entities and relationships (proposed)

- users(user_id PK) 1-to-many sessions(session_id PK, user_id FK).
- users(user_id PK) 1-to-many task_attempts(attempt_id PK, user_id FK, task_id FK).
- tasks(task_id PK) 1-to-many task_attempts.
- task_attempts 1-to-many reward_transactions where business rules permit multiple reward adjustments.
- users 1-to-many reward_transactions.
- users 1-to-many wallet_transactions; each wallet row should reference the related business transaction where available.
- users 1-to-many withdrawals(withdrawal_id PK, user_id FK); withdrawals 1-to-many withdrawal_state_history.
- users 1-to-many referrals as referrer and/or referred user; enforce approved attribution rules.
- users 1-to-many feature_events; events may reference task, reward, wallet or withdrawal identifiers.
- These are logical proposals, not verified production tables.

## 6. Data-quality controls and issue handling

Apply controls at ingestion and before KPI publication.

| Rule ID | Check | Detection | Severity | Response / prevention |
|---|---|---|---|---|
| DQ-01 | Event ID uniqueness | Duplicate event_id within event grain | Critical | Idempotent ingestion; quarantine duplicates |
| DQ-02 | Stable user key | Missing/invalid user_id where required | High | Reject or route to approved anonymous-event handling |
| DQ-03 | Timestamp validity | Unparseable timestamp, impossible future time, inconsistent timezone | High | Preserve raw value; normalize to UTC; quarantine invalid records |
| DQ-04 | Allowed statuses | Status outside approved enum | High | Contract validation; no silent status mapping |
| DQ-05 | State transition validity | Transition not allowed by documented lifecycle | High | Keep state history; flag impossible transitions |
| DQ-06 | Numeric validity | Non-numeric, unexpected negative amount, invalid precision/unit | Critical for ledger | Block financial metric publication; reconcile with source of truth |
| DQ-07 | Foreign-key integrity | Orphan task/user/reward/wallet/withdrawal references | High | Quarantine or resolve via documented late-arrival policy |
| DQ-08 | Required fields | Missing event-specific mandatory fields | High | Schema validation before ingestion |
| DQ-09 | Duplicate business transactions | Duplicate transaction/idempotency key | Critical for ledger | Idempotent write and ledger reconciliation |
| DQ-10 | Cross-system reconciliation | Reward credit totals do not reconcile to approved source/ledger | Critical | Alert Finance/Operations; do not publish until explained |
| DQ-11 | Naming/casing/whitespace | Unapproved values, leading/trailing spaces, inconsistent labels | Medium | Controlled enums and canonicalization at transform layer |
| DQ-12 | Referential chronology | Completion before start, registration after later lifecycle event | High | Validate ordering and timestamp semantics |
| DQ-13 | Profile-field consistency | Account status conflicts with activity/verification flags | Medium/High | Confirm field definitions and snapshot timing; flag, don't guess |
| DQ-14 | Data freshness | Latest successful load exceeds agreed SLA | High | Freshness alert and dashboard stale-data banner |
| DQ-15 | Volume anomaly | Abrupt unexplained change in event counts | Medium/High | Thresholds after baseline exists; alert owner |

### Required quality issue log fields

issue_id, dataset, field, issue_type, affected_records, severity, detection_logic, likely_cause, correction, prevention, owner, status, first_seen_at, last_seen_at, evidence_reference.

Do not mark a production issue fixed until rerun evidence exists. Simulated-workbook findings should be labelled as findings in supplied simulated data.

## 7. KPI catalogue — proposed definitions

KPI names and formulas must be approved by Product/Engineering/Finance. Numerators and denominators must use the same observation window and documented eligibility rules.

| KPI | Proposed definition/formula | Minimum source | Frequency | Stakeholder / decision | Main limitation |
|---|---|---|---|---|---|
| Registrations | Count distinct users created in period | Account creation | Daily/weekly | Growth: acquisition volume | Exclude test/internal accounts by approved rule |
| Signup completion rate | Completed registrations / registration starts | Registration events | Daily/weekly | Product: signup friction | Requires reliable start and completion events |
| Onboarding completion rate | Eligible new users completing onboarding / eligible onboarding starters | Onboarding events | Weekly cohort | Product: prioritize steps | Eligibility/window must be defined |
| Verified-account share | Verified eligible accounts / eligible accounts | Verification state history | Daily | Product/Ops: verification funnel | Current-state snapshots can hide history |
| DAU | Distinct eligible users active on day under approved activity definition | Event/session data | Daily | Product: daily engagement | Activity event definition required |
| WAU | Distinct eligible users active in rolling 7 days | Event/session data | Daily | Product: weekly engagement | Rolling window needs timezone rule |
| MAU | Distinct eligible users active in rolling 30 days | Event/session data | Daily | Leadership: monthly reach | Not comparable if definitions change |
| DAU/MAU | DAU divided by MAU for aligned date | Event/session data | Daily | Product: engagement frequency | Small/new user base may make volatile |
| Returning-user share | Active users in period who were active in prior period / active users in period | Event/session data | Weekly | Product: return behavior | Period and eligibility must be fixed |
| D1 retention | Eligible cohort users active on day 1 / eligible cohort users | Registration + activity events | Cohort | Product: early retention | Calendar vs rolling day must be defined |
| D7 retention | Eligible cohort users active on day 7 / eligible cohort users | Registration + activity events | Cohort | Product: first-week retention | Same cohort/window caveat |
| D30 retention | Eligible cohort users active on day 30 / eligible cohort users | Registration + activity events | Cohort | Product: long-term retention | Requires sufficient maturity |
| Task impressions | Count valid task-view/impression events | Task events | Daily | Product: task discovery | Instrumentation coverage required |
| Task start rate | Unique task starts / eligible task impressions | Task events | Daily/weekly | Product: task appeal | Must deduplicate users/attempts consistently |
| Task completion rate | Validated completions / started attempts | Task lifecycle | Daily/weekly | Product/Ops: funnel friction | Do not equate submitted with validated |
| Task abandonment rate | Abandoned attempts / started attempts | Task lifecycle | Weekly | Product: investigate friction | Abandonment timeout must be defined |
| Task validation failure rate | Validation failures / validation attempts | Validation events | Daily | Engineering/Ops: failure causes | Failure reason taxonomy must be approved |
| Time to task completion | Median completion timestamp minus start timestamp for valid attempts | Task lifecycle | Weekly | Product: task complexity | Exclude invalid/negative durations |
| Reward pending share | Pending reward transactions / eligible reward transactions | Reward ledger | Daily | Ops: pending queue | State timing and denominator required |
| Reward credit success rate | Credited valid rewards / eligible validated reward attempts | Reward + task ledger | Daily | Ops/Finance: credit reliability | Reconcile with authoritative ledger |
| Reward reversal rate | Reversed reward transactions / credited transactions in aligned cohort | Reward ledger | Weekly | Finance/Ops: reversal monitoring | Cohort alignment and reason codes required |
| Reward correction rate | Corrected transactions / eligible reward transactions | Reward ledger | Weekly | Finance/Ops: correction monitoring | Correction semantics need approval |
| Reward credit latency | Median credited timestamp minus validation timestamp | Reward lifecycle | Daily | Ops: improve credit delay | Requires both authoritative timestamps |
| Wallet ledger balance | Opening balance + credits − debits under approved rules | Wallet ledger | Daily | Finance: reconcile balances | Units/currency and reversals must be explicit |
| Ledger reconciliation difference | Authoritative balance − calculated ledger balance | Wallet ledger + source of truth | Daily | Finance: investigate discrepancy | Cannot publish without trusted source |
| Withdrawal request count | Count distinct valid withdrawal IDs created in period | Withdrawal records | Daily | Ops: demand and workload | Retry semantics must be defined |
| Withdrawal approval rate | Approved eligible requests / requests reaching decision | Withdrawal state history | Daily/weekly | Ops: review outcomes | Exclude still-pending requests or show separately |
| Withdrawal rejection rate | Rejected eligible requests / decided requests | Withdrawal state history | Daily/weekly | Ops: investigate rejection causes | Rejection categories required |
| Withdrawal processing time | Median processed timestamp − requested timestamp | Withdrawal state history | Daily/weekly | Ops: reduce delays | Must define terminal processed state |
| Withdrawal failure rate | Failed payout attempts / payout attempts | Payout system | Daily | Finance/Ops: reliability | Requires payout-attempt events, not just request rows |
| Referral registration conversion | Referred registrations / valid attributed referral clicks/invites | Referral + registration | Weekly cohort | Growth: referral funnel | Attribution window and duplicates required |
| Referral activation rate | Activated referred users / eligible referred registrations | Referral + activity | Weekly cohort | Growth: referral quality | Activation definition must be approved |
| Referral reward rate | Valid referral rewards / eligible activated referrals | Referral + reward ledger | Weekly | Growth/Finance: reward integrity | Eligibility and reversal rules required |
| Feature adoption rate | Users using feature / eligible active users | Feature events + user eligibility | Weekly/monthly | Product: feature adoption | Feature eligibility must be documented |
| Event delivery success | Accepted valid events / expected emitted events where measurable | Client/server telemetry | Daily | Engineering: tracking reliability | Needs emitted-vs-received instrumentation |
| Event duplication rate | Duplicate events / received events | Event pipeline | Daily | Data Engineering: ingestion quality | Stable event identity required |
| Data freshness SLA | Successful load time vs agreed refresh deadline | Pipeline metadata | Per load | Analytics/Ops: trust reporting | SLA must be agreed |
| Critical data-quality pass rate | Passed critical checks / executed critical checks | Quality framework | Per load | Data owner: release gate | Checks must be versioned and weighted by severity |

## 8. Seven-dashboard blueprint

The assignment requires a blueprint with visual-level specification; it does not mean seven production dashboards can be populated before production data exists.

| Dashboard | Recommended visual / metric | Business question | Decision supported | Source dependency |
|---|---|---|---|---|
| Executive Overview | KPI cards and time trends for approved active users, task completion, reward integrity, withdrawal processing and data quality | Is the product operating reliably and where is risk rising? | Prioritize engineering/operations work | Approved user/activity/task/reward/wallet/withdrawal sources |
| User Analytics | Registration funnel, onboarding funnel, cohorts, D1/D7/D30 retention | Where are users dropping and which cohorts return? | Improve onboarding or lifecycle communication | User, onboarding and activity events |
| Engagement | Task funnel, feature adoption, activity frequency, time-to-complete distributions | Which features are used and where do attempts fail? | Investigate friction and instrument missing steps | Session, feature and task events |
| Rewards | Pending/credited/reversed/corrected counts and credit latency | Are validated activities rewarded accurately and on time? | Resolve crediting failures and backlog | Authoritative reward ledger + task validation |
| Wallet | Credit/debit trends, ledger balance reconciliation, transaction exceptions | Do balances reconcile and are ledger movements traceable? | Investigate discrepancies before user impact | Wallet ledger and authoritative balance source |
| Withdrawals | Request funnel, status aging, processing-time percentiles, failure/rejection reasons | Where are requests delayed or failing? | Fix operational bottlenecks and improve status communication | Withdrawal state history and payout outcomes |
| Referrals | Invite → registration → activation → reward funnel by approved source | Which referral cohorts activate and qualify? | Validate channel quality and referral rules | Referral attribution, user lifecycle and reward ledger |

### Standard controls for every dashboard

- Display data source, last successful refresh, date range and KPI definition/version.
- Show sample size and missing/invalid-data warnings where relevant.
- Apply role-based access and minimum necessary detail.
- Distinguish zero from unknown/missing.
- Do not show metrics if critical quality/reconciliation gates fail; show a clear stale/unavailable status instead.
- Provide filters only where supported by the grain and approved definition.
- Keep simulated/test data visibly labelled and separate from production.

## 9. Pipeline and operating model proposal

Proposed flow: Product clients/services/partners → event collector/API → immutable raw landing → schema and identity validation → deduplication and state-history processing → curated analytical tables → governed KPI layer → dashboards/exports.

1. Collection: versioned event contracts, required fields, producer ownership and event IDs.
2. Raw layer: retain original payload, source, received time and ingestion metadata under approved retention controls.
3. Validation: schema, type, allowed-value, timestamp, identifier and duplicate checks.
4. Transformation: canonical timezone, approved status mapping, idempotent deduplication, relationship integrity and derived fields.
5. Curated layer: user/account, session, task attempt, reward ledger, wallet ledger, withdrawal state history, referral and feature-event models.
6. Metrics layer: centrally defined KPI formulas with version, owner, denominator, filters and effective date.
7. Serving: dashboard views with freshness metadata, role controls and quality gates.
8. Monitoring: load success, freshness, volume drift, schema drift, duplicate/orphan rates and reconciliation exceptions.
9. Incident process: alert owner → assess scope/impact → quarantine/block unsafe metric → correct source/pipeline → rerun checks → document resolution.
10. Ownership: Product defines meaning; Engineering instruments events; Data Engineering owns pipeline and contracts; Analytics owns KPI definitions; Finance/Operations owns ledger/payout reconciliation; Security/Legal approves access and retention.

This is a design proposal, not a deployed production pipeline.

## 10. Privacy, access and governance

- Collect only fields needed for documented product/business purposes.
- Prefer stable pseudonymous identifiers in analytical datasets; keep direct identifiers out of general-purpose analytics unless approved.
- Define role-based access for Product, Analytics, Engineering, Finance/Operations and administrators.
- Apply least privilege to raw data; aggregate or mask sensitive values in reporting.
- Do not store credentials, tokens or secrets in code, public repository, exported reports or event payloads.
- Define retention/deletion, access logging, export controls and incident escalation with Security/Legal.
- Treat partner identifiers and payout details as restricted fields where applicable.
- Maintain metric, event schema and source changes in a versioned change log.
- Obtain owner approval before production rollout.

## 11. Analytics gaps requiring verification

| Gap ID | Unknown / missing evidence | Why it matters | Priority | Owner | Status |
|---|---|---|---|---|---|
| GAP-01 | Canonical user ID and merge policy | Cross-event user counts and joins | Critical | Engineering | To Be Verified |
| GAP-02 | Event ID and idempotency standard | Duplicate delivery can inflate metrics | Critical | Engineering | To Be Verified |
| GAP-03 | Production event coverage and actual emitted events | Cannot measure uninstrumented behavior | Critical | Engineering | To Be Verified |
| GAP-04 | Task attempt identity and lifecycle | Retries, abandonment and completion denominator | High | Product + Engineering | To Be Verified |
| GAP-05 | Task validation source and failure taxonomy | Submitted work is not necessarily valid completion | High | Product/Ops | To Be Verified |
| GAP-06 | Reward ledger source of truth and units | Credit, reversal and correction integrity | Critical | Finance/Ops | To Be Verified |
| GAP-07 | Wallet ledger and balance reconciliation rule | Financial correctness | Critical | Finance/Ops | To Be Verified |
| GAP-08 | Withdrawal state history and payout source | Processing-time and failure analysis | Critical | Finance/Ops | To Be Verified |
| GAP-09 | Referral attribution window and eligibility | Referral conversion cannot be consistently calculated | High | Product/Growth | To Be Verified |
| GAP-10 | Active user and retention definitions | Reporting varies by arbitrary definitions | High | Product Analytics | To Be Verified |
| GAP-11 | Timezone and event-time/received-time policy | Ordering, cohorting and latency errors | High | Engineering | To Be Verified |
| GAP-12 | Feature existence vs planned state | Avoid treating proposed areas as live features | High | Product | To Be Verified |
| GAP-13 | Source refresh/freshness SLAs | Stale reports can mislead decisions | Medium | Data/Engineering | To Be Verified |
| GAP-14 | Access, retention and export policy | Privacy/security exposure | High | Security/Legal | To Be Verified |
| GAP-15 | Task 02 reuse authorization | Scope mixing risks invalid conclusions | Medium | Coordinator | To Be Verified |

## 12. Assumption and verification register

| ID | Unknown | Why it matters | Risk | Source checked | Status | Owner |
|---|---|---|---|---|---|---|
| A001 | Does backend emit task completion events today? | Required for task funnel | False completeness | Task 01 brief/workbook | To Be Verified | Engineering |
| A002 | Are reward states stored as immutable transactions? | Required for reversals/reconciliation | Financial misstatement | Task 01 brief/workbook | To Be Verified | Finance/Engineering |
| A003 | Which wallet ledger is authoritative? | Balance accuracy | Critical discrepancy | Task 01 brief/workbook | To Be Verified | Finance |
| A004 | Are withdrawal state transitions timestamped? | Processing-time KPIs | Invalid latency | Task 01 brief/workbook | To Be Verified | Operations |
| A005 | How is referral source assigned and retained? | Attribution | Biased channel reporting | Task 01 user workbook | To Be Verified | Product/Growth |
| A006 | What is the official active-user definition? | DAU/WAU/MAU/retention | Incomparable metrics | No approved definition supplied | To Be Verified | Product Analytics |
| A007 | Is Task 02 data authorized for Task 01 use? | Scope integrity | Unapproved mixing | Task 02 workbook title | To Be Verified | Coordinator |
| A008 | Is Streamlit accepted despite email requesting Vercel/Netlify? | Submission compliance | Hosting requirement unmet | Assignment email | To Be Verified | Coordinator |

## 13. Prioritized implementation backlog

| Priority | Requirement | Reason | Dependency | Owner | Stage / acceptance test |
|---|---|---|---|---|---|
| Critical | Approve canonical IDs and event contract | Cross-event joins and deduplication | Product/Engineering agreement | Engineering | Pre-implementation; sample payloads pass schema tests |
| Critical | Define reward and wallet source of truth | Financial integrity | Finance/Ops approval | Finance + Engineering | Pre-implementation; ledger reconciliation test specified |
| Critical | Define withdrawal lifecycle and timestamps | Reliable payout reporting | Ops/Finance agreement | Operations + Engineering | Pre-implementation; every terminal state has timestamps |
| High | Implement task lifecycle instrumentation | Funnel and failure analysis | Approved event catalogue | Engineering | Staging events pass acceptance tests |
| High | Establish user/onboarding lifecycle events | Cohorts and retention | Identity and event contract | Engineering | New test cohort can be traced end-to-end |
| High | Add automated quality gates | Prevent invalid reporting | Rules and owners | Data Engineering | Critical failures block publication and alert owner |
| High | Publish approved KPI definitions | Consistent management reporting | Data source and business definition | Product Analytics | KPI review/sign-off recorded |
| High | Build seven dashboards from approved specs | Future decision support | Reliable curated data + KPI layer | Analytics/BI | Each visual has source, formula, filter and decision documented |
| High | Approve privacy/access/retention model | Protect user and financial data | Security/Legal review | Security/Legal | Access matrix and retention policy approved |
| Medium | Establish freshness and schema-drift monitoring | Trustworthy operations | Pipeline metadata | Data Engineering | Stale-load alert test passes |
| Medium | Establish analytics change log | Keep producers and consumers aligned | Ownership process | Product + Engineering + Analytics | Schema/KPI changes include impact and version |
| Medium | Confirm Task 02 reuse and hosting exception | Submission scope/compliance | Coordinator response | Intern / Coordinator | Written decision recorded |

## 14. Supplied-data findings vs. production conclusions

### Findings about the supplied simulated Task 01 workbook

- The clean user sheet contains 1,000 profiles.
- 881 of 1,000 clean profiles have missing referral_source_detail (88.1%).
- 72 of 1,000 clean profiles have missing last_login_datetime (7.2%).
- The messy user sheet has 1,008 rows and 1,000 unique user IDs, with 8 repeated IDs.
- The messy sheet has 1 missing registration timestamp, 73 missing last-login timestamps, 885 missing referral details and 4 negative days_since_registration values.

These are properties of supplied simulated assignment data. They are not claims about production users.

### Business performance that cannot be established from the Task 01 user sheet

The user-profile workbook alone cannot establish real task completion, actual reward crediting, wallet reconciliation, withdrawal failure/delay, referral conversion, revenue or product retention. Those require authoritative event/transaction sources and approved definitions.

Any supplemental simulated data used to test code must be kept separate, labelled simulated, and never used to claim company performance.

## 15. Final acceptance checklist

- [ ] All 21 required deliverables are present and traceable to the assignment.
- [ ] Every product fact has a source and Confirmed / Proposed / To Be Verified status.
- [ ] At least 10 analytics gaps are recorded with risk, priority and owner.
- [ ] User/account, task/reward, wallet/withdrawal and referral/engagement specifications are documented.
- [ ] Event catalogue includes trigger, identifiers, timestamps, properties, source, validation and KPI mapping.
- [ ] Data dictionary has at least 75 meaningful fields with required metadata.
- [ ] Logical model and ERD document keys and relationships and are labelled proposed.
- [ ] KPI catalogue has at least 30 definitions with formulas, sources, frequency, stakeholder, purpose and limitations.
- [ ] Simulated source profiling and messy-data quality audit are evidence-backed.
- [ ] Quality controls cover collection, raw, transformation, analytics and dashboard layers.
- [ ] Seven-dashboard blueprint specifies metrics, calculations, sources, visuals, filters, dimensions, date range, refresh, business question and decision.
- [ ] Developer handoff includes acceptance tests and implementation priorities.
- [ ] Pipeline, operating model, privacy/access/governance and change management are documented.
- [ ] Assumption/verification register and prioritized backlog are maintained.
- [ ] No simulated metric is presented as actual VELOOP performance.
- [ ] Browser QA is completed on desktop and narrow/mobile viewport.
- [ ] Hosting meets the assignment email's Vercel/Netlify requirement or a written exception is recorded.
- [ ] Company-owner sign-off dependencies are explicitly recorded; no production readiness claim is made without them.

**Current truth:** this is a detailed proposed analytics foundation. It does not certify that VELOOP's production systems, events, dashboards or pipeline have been implemented.
