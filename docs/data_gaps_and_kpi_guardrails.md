# Data Gaps and KPI Guardrails — Task 01

## Evidence limitations
- The Task 01 user/account workbook is simulated; it is not production evidence.
- Production transaction-level tables for task activity, rewards, wallet transactions, withdrawals, referrals and feature events were not supplied with the Task 01 source workbook.
- Supplemental dashboard records are illustrative synthetic samples generated for interface testing only.
- Public help pages provide product context but do not independently prove internal implementation, production volumes or operational performance.
- Production instrumentation, data retention controls, access permissions and source-of-truth ownership require confirmation from the relevant company owners.

## KPI calculation guardrails
- **DAU/WAU/MAU:** agree qualifying activity events, timezone, identity resolution and inclusive/exclusive window rules first.
- **Task conversion:** define eligible starts, deduplication, completion, validation and rejection semantics.
- **Reward volume:** report by unit. Do not add XP, VE, Gems, Tokens or currency without an approved conversion policy.
- **Wallet net movement:** use an authoritative ledger, posting status, linked reversals and reconciliation rules.
- **Withdrawal success and duration:** define terminal states and use source-of-truth request and completion timestamps. Pending items are not completed.
- **Referral conversion:** registration, activation and conversion are distinct lifecycle stages.
- **Synthetic metrics:** dashboard counts demonstrate layout and logic only, not company performance.

## Prioritized next steps
1. Confirm authoritative source tables and stable identifiers.
2. Approve event taxonomy, payload schema, timezone and lifecycle states.
3. Implement schema, chronology, duplicate, foreign-key and reconciliation checks.
4. Validate KPI formulas with Product, Engineering, Operations and Finance.
5. Publish production dashboards only after source data and metric definitions are approved.
