# VELOOP Task 01 — Proposed Logical ERD

**Status:** logical design proposal only. This is not a verified physical production schema. Entity names, keys, cardinalities and field constraints require Product/Engineering/Finance approval.

```mermaid
erDiagram
    USER ||--o{ SESSION : starts
    USER ||--o{ TASK_ATTEMPT : performs
    TASK ||--o{ TASK_ATTEMPT : defines
    TASK_ATTEMPT ||--o{ REWARD_TRANSACTION : may_generate
    USER ||--o{ REWARD_TRANSACTION : receives
    USER ||--o{ WALLET_TRANSACTION : owns
    REWARD_TRANSACTION ||--o{ WALLET_TRANSACTION : may_post
    USER ||--o{ WITHDRAWAL : requests
    WITHDRAWAL ||--o{ WITHDRAWAL_STATE_HISTORY : transitions
    WITHDRAWAL ||--o{ WALLET_TRANSACTION : may_settle
    USER ||--o{ REFERRAL : refers
    USER ||--o{ REFERRAL : is_referred
    USER ||--o{ FEATURE_EVENT : generates
    SESSION ||--o{ FEATURE_EVENT : groups

    USER {
      string user_id PK
      timestamp registration_datetime
      string account_status
      string onboarding_status
      string acquisition_source
    }
    SESSION {
      string session_id PK
      string user_id FK
      timestamp started_at
      timestamp ended_at
      string platform
    }
    TASK {
      string task_id PK
      string task_type
      string task_status
    }
    TASK_ATTEMPT {
      string task_activity_id PK
      string task_id FK
      string user_id FK
      string session_id FK
      timestamp started_at
      timestamp completed_at
      string task_status
      string validation_status
    }
    REWARD_TRANSACTION {
      string reward_id PK
      string user_id FK
      string source_activity_id FK
      decimal reward_amount
      string reward_unit
      string reward_status
      string related_reward_id
    }
    WALLET_TRANSACTION {
      string transaction_id PK
      string user_id FK
      string transaction_type
      decimal amount
      string unit
      string transaction_status
      string reference_id
      string idempotency_key
    }
    WITHDRAWAL {
      string withdrawal_id PK
      string user_id FK
      decimal requested_amount
      string withdrawal_method
      string withdrawal_status
    }
    WITHDRAWAL_STATE_HISTORY {
      string state_history_id PK
      string withdrawal_id FK
      string old_state
      string new_state
      timestamp changed_at
      string reason_category
    }
    REFERRAL {
      string referral_id PK
      string referring_user_id FK
      string referred_user_id FK
      timestamp referral_created_at
      timestamp referral_activated_at
      string referral_status
    }
    FEATURE_EVENT {
      string event_id PK
      string user_id FK
      string session_id FK
      string event_name
      timestamp event_timestamp
      timestamp received_at
      string schema_version
    }
```

## Grain and integrity rules

- One row per user, session, task attempt, immutable reward transaction, wallet ledger movement, withdrawal, withdrawal state transition, referral and feature event.
- Keep `event_id`, `session_id`, `task_activity_id`, `reward_id`, `transaction_id`, `withdrawal_id` and `referral_id` distinct.
- Keep event occurrence time separate from received/ingested time.
- Reward reversals and corrections are new traceable transactions linked to the original; do not overwrite history.
- Amounts require explicit units and approved precision; do not aggregate unlike units.
- Every FK, uniqueness rule, status transition and nullable field requires owner-approved validation.
- No production schema or actual data integration is implied.
