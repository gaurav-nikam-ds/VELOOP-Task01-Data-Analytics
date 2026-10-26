# Data Dictionary Field Index — Task 01

**Scope:** 90 proposed field definitions in the Task 01 design workbook. This index publishes the field inventory in GitHub. Full metadata (type, definition, example, requiredness, allowed values, validation, source, sensitivity, analytical use and status) must be maintained in the design workbook and approved with the relevant source owner before production implementation.

**Status rule:** a field present in the supplied simulated workbook does not prove it exists in VELOOP production. All proposed physical-schema claims remain To Be Verified.

## Field inventory by logical entity

| Entity | Field names |
|---|---|
| Users | user_id, registration_datetime, acquisition_source, primary_device, platform, account_status, onboarding_status, last_login_datetime, lifetime_sessions, active_days, xp_balance, referral_code, is_active_7d, is_active_30d, consent_status, marketing_opt_in, event_id, session_id |
| Tasks | task_id, task_type |
| Task Activity | task_activity_id, task_started_at, task_completed_at, task_status, validation_status, partner_id, external_reference_id, failure_category |
| Rewards | reward_id, source_activity_id, reward_amount, reward_unit, reward_status, related_reward_id |
| Wallet Transactions | transaction_id, transaction_type, amount, unit, transaction_status, reference_id, related_transaction_id, idempotency_key |
| Withdrawals | withdrawal_id, requested_amount, withdrawal_method, requested_at, processing_at, final_at, withdrawal_status, reason_category |
| Referrals | referral_id, referring_user_id, referred_user_id, referral_created_at, referral_registered_at, referral_activated_at, referral_status |
| Feature Events | event_name, event_timestamp, received_at, event_source, schema_version, validation_result, correlation_id |
| Engagement | mission_id, mission_attempt_id, badge_id, streak_count, xp_delta |
| Content | article_id |
| Support | ticket_id, support_category |
| Privacy | preference_type, preference_value |
| Common | occurred_at, ingested_at, platform, app_version, country, source, reason_category, status, unit, amount, related_record_id, deduplication_key, privacy_policy_version, partner_id, placement, campaign_id |

## Metadata contract for every dictionary row

| Metadata | Required documentation |
|---|---|
| Entity and field name | Logical entity and stable snake_case name |
| Data type | String, integer, decimal, boolean/enum, timestamp, or structured object as applicable |
| Definition | One unambiguous meaning; avoid overloaded fields |
| Example | Clearly labelled test/example value, never mistaken for a real customer record |
| Requiredness | Required / conditional / recommended / optional, with event/entity context |
| Allowed values | Controlled vocabulary, unit list or valid range |
| Validation | Nullability, uniqueness, type, chronology, foreign-key and domain constraints |
| Source | Authoritative producer/system or proposed producer requiring verification |
| Sensitivity | Public/internal/restricted classification approved by Security/Legal |
| Analytical use | KPIs, joins, lifecycle or operational decisions supported |
| Status | Present in supplied simulated data / Proposed / To Be Verified / Approved for production |

## Critical field rules

1. A stable user_id is the join key; direct identifiers such as name/email should not be required for general analytics.
2. event_id is distinct from session_id, task_activity_id, transaction_id, reward_id, withdrawal_id and referral_id; do not reuse one identifier for different grains.
3. Keep occurrence time and ingestion time separate (occurred_at and ingested_at or event-specific equivalents).
4. Amounts must always have an explicit unit and approved precision; never aggregate unlike units.
5. Reward/wallet/withdrawal changes must be traceable through immutable transaction references and idempotency controls.
6. status, reason_category, platform, source and other categorical values require approved vocabularies; don't silently normalize unknown business states.
7. Consent and preference data require restricted access and approved purpose/retention.
8. Partner identifiers and external references must be assessed for access restrictions and contract requirements.
9. Every field in a production contract requires an accountable owner and validation evidence.
10. Do not infer production implementation from a proposed field or from its appearance in a simulated assignment workbook.

## Data dictionary acceptance

- At least 75 meaningful fields: the design workbook contains 90 proposed field rows.
- Every row contains the metadata contract above.
- Entity grain, primary/foreign keys, allowed values and null rules are documented.
- Sensitive fields are minimised and access-controlled.
- Proposed fields remain clearly labelled until Product/Engineering approve them.
- Schema changes are versioned and validated through CI/staging acceptance tests.
