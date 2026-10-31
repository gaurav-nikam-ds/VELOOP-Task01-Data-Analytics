# Dashboard Plan — Production Manual QA

**Date:** 31 October 2026  
**Production URL:** https://veloop-task01-data-analytics.vercel.app/  
**Section:** Dashboard plan  
**Evidence:** Five user-provided production screenshots captured between approximately 11:17 and 11:18 local time.

## Navigation and overview

- Dashboard plan navigation is selected and page renders.
- Page heading: `What each future dashboard should answer`.
- Introductory copy explicitly states these are specifications, not live dashboards.
- Production URL notice and simulated-data disclaimer are visible.
- Seven dashboard specification accordions are present, numbered 01–07:
  1. Executive Overview
  2. User Analytics
  3. Engagement
  4. Rewards
  5. Wallet
  6. Withdrawals
  7. Referrals

## Expanded specification review

The supplied screenshots show the expanded details for all seven dashboards.

| Dashboard | Business measures | Primary stakeholder | Source / approval dependency |
|---|---|---|---|
| Executive Overview | Approved core KPIs, trends, alerts and definitions | Product / leadership | Production sources and approved KPI definitions |
| User Analytics | Registration, onboarding, account lifecycle and cohorts | Product / growth | Canonical user IDs and lifecycle events |
| Engagement | Active/returning users, task activity and feature usage | Product / analytics | Session/event data and approved activity definition |
| Rewards | Earned, pending, credited, reversed and corrected rewards | Rewards operations / finance | Authoritative reward ledger and reward units |
| Wallet | Ledger credits/debits, balances and reconciliation | Finance / operations | Wallet ledger, transaction IDs and reconciliation rules |
| Withdrawals | Requests, outcomes, failure reasons and processing time | Operations / finance | Payout source of truth, status history and timestamps |
| Referrals | Referral creation, registration, activation and conversion | Growth / product | Referral attribution and approved conversion definition |

Each expanded specification displays the same guardrail: blueprint only; formulas, dimensions, filters, date range and refresh rules require owner validation.

## Result

**PASS — seven dashboard specifications are present and expandable; the visible business measures, stakeholders and source dependencies are documented.** The supplied screenshots show all seven expanded sections across the review.

## Scope and accuracy guardrails

- These are dashboard specifications, not operational dashboards.
- No production source system is connected, as stated in the website footer.
- KPI definitions, dimensions, date ranges and refresh rules remain subject to owner validation.
- Rewards, wallet and withdrawal dashboards depend on authoritative Finance/Operations data.
- User and engagement dashboards depend on canonical IDs and approved event/lifecycle definitions.
- No production KPI values or company approvals are implied.

## Screenshot evidence

The five screenshots were supplied in this conversation:
- `Screenshot 2026-10-31 111733.png`
- `Screenshot 2026-10-31 111744.png`
- `Screenshot 2026-10-31 111803.png`
- `Screenshot 2026-10-31 111812.png`
- `Screenshot 2026-10-31 111818.png`

A combined contact sheet was created in the working session as `VELOOP_dashboard_plan_QA_screenshots_2026-10-31.jpg`. Screenshot binaries are not embedded in this repository commit; the source screenshots remain conversation attachments.

## Remaining live QA

- What remains section.
- Documents section and each document destination/link.
- Browser console, responsive and accessibility checks.
- Full automated live QA rerun against production.
