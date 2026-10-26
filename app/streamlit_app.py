import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="VELOOP Rewards | Task 01 Analytics Blueprint",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
:root { --ink:#182230; --muted:#667085; --line:#e4e7ec; --canvas:#f5f7fa; --teal:#087e8b; }
.stApp { background:var(--canvas); color:var(--ink); }
.block-container { max-width:1450px; padding:1.25rem 1.4rem 3rem; }
[data-testid="stSidebar"] { background:#fff; border-right:1px solid var(--line); }
h1,h2,h3 { letter-spacing:-.025em; color:var(--ink); }
[data-testid="stMetric"] { background:#fff; border:1px solid var(--line); border-radius:12px; padding:1rem; }
[data-testid="stDataFrame"] { background:#fff; border:1px solid var(--line); border-radius:10px; }
.hero { background:linear-gradient(115deg,#102a43,#174a63 60%,#087e8b); border-radius:16px; padding:1.5rem; color:white; margin-bottom:1rem; }
.hero h1 { color:white; font-size:1.8rem; }
.hero p { color:#e3f2f4; max-width:950px; }
.note { border-left:4px solid var(--teal); background:white; padding:.85rem 1rem; border-radius:8px; }
@media (max-width:800px) { .block-container { padding:.65rem .65rem 1.5rem; } .hero { padding:1rem; } }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>VELOOP Rewards — Product Analytics & Data Readiness</h1>
  <p>Task 01 deliverable review, source-file audit, dashboard specification and implementation dependencies. This workspace reports only facts recorded in the supplied assignment materials and audit; it does not fabricate production transactions or company performance.</p>
</div>
""", unsafe_allow_html=True)

st.warning("SOURCE LIMITATION: The Task 01 brief identifies its supplied data as simulated. No authorized production extract or production-system connection was supplied. Therefore, real VELOOP business performance cannot be calculated from the available files.")

with st.sidebar:
    st.markdown("## ◈ VELOOP REWARDS")
    st.caption("TASK 01 · ANALYTICS BLUEPRINT")
    page = st.radio("WORKSPACE", [
        "Executive status",
        "Supplied data audit",
        "Deliverable tracker",
        "Seven-dashboard blueprint",
        "Acceptance blockers",
    ])
    st.markdown("---")
    st.caption("Evidence basis: supplied Task 01 PDF, Task 01 workbook, separately supplied Task 02 workbook and assignment email.")

if page == "Executive status":
    st.subheader("Current submission status")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Required final deliverables", "21")
    c2.metric("Proposed KPI definitions", "36")
    c3.metric("Proposed dictionary fields", "90")
    c4.metric("Production connections", "0")
    st.markdown("""
    **What is established**
    - The governing assignment is a product-analytics and data-readiness blueprint, not evidence that a production analytics system already exists.
    - The Task 01 workbook provides user-profile clean and messy tabs, plus dictionary/summary tabs.
    - The separately supplied behavior workbook labels itself Task 02 and is kept separate pending coordinator approval.
    - Event plans, dictionary fields, KPI definitions, logical model, dashboard specifications, governance and pipeline are design proposals until the relevant company owners approve them.
    """)
    st.markdown('<div class="note"><b>Decision:</b> do not publish actual-company KPIs, payout metrics, retention rates or conversion rates until authorized production data and approved definitions are available.</div>', unsafe_allow_html=True)

elif page == "Supplied data audit":
    st.subheader("Task 01 source workbook")
    a,b,c,d = st.columns(4)
    a.metric("Clean users", "1,000")
    b.metric("Columns per user tab", "28")
    c.metric("Messy audit rows", "1,008")
    d.metric("Repeated IDs in messy tab", "8")
    st.dataframe(pd.DataFrame([
        {"Source sheet":"Users_1000_Clean","Rows":1000,"Columns":28,"Finding":"1,000 unique, non-null user_id values; 0 exact duplicate rows"},
        {"Source sheet":"Users_1000_Clean","Rows":1000,"Columns":28,"Finding":"881 missing referral_source_detail; 72 missing last_login_datetime"},
        {"Source sheet":"Users_Messy_Audit","Rows":1008,"Columns":28,"Finding":"1,000 unique IDs; 8 repeated IDs"},
        {"Source sheet":"Users_Messy_Audit","Rows":1008,"Columns":28,"Finding":"1 missing registration timestamp; 73 missing last-login timestamps"},
        {"Source sheet":"Users_Messy_Audit","Rows":1008,"Columns":28,"Finding":"885 missing referral details; 4 negative days_since_registration values"},
    ]), hide_index=True, use_container_width=True)
    st.subheader("Separate Task 02 workbook — not merged")
    st.dataframe(pd.DataFrame([
        {"Dataset":"Sessions","Rows":7913,"Audited finding":"984 distinct user IDs; no orphan user IDs against Task 02 profiles"},
        {"Dataset":"Primary feature events","Rows":35704,"Audited finding":"35,704 unique event IDs; date range 2026-04-02 to 2026-09-15; no user ID orphans"},
        {"Dataset":"Event audit","Rows":35714,"Audited finding":"10 exact duplicate rows"},
        {"Dataset":"Daily activity","Rows":6667,"Audited finding":"Task 02 workbook summary; not treated as Task 01 source"},
        {"Dataset":"Task activity","Rows":9846,"Audited finding":"Task 02 workbook summary; not treated as Task 01 source"},
        {"Dataset":"Milestones","Rows":4799,"Audited finding":"Task 02 workbook summary; not treated as Task 01 source"},
    ]), hide_index=True, use_container_width=True)
    st.caption("These are counts/findings from the supplied simulated assignment workbooks, not actual VELOOP production statistics. Missingness should be interpreted against field-level rules; do not silently delete or correct records.")

elif page == "Deliverable tracker":
    st.subheader("Task 01 required deliverables")
    rows = [
        (1,"Executive summary","Documented","Company-owner unknowns remain"),
        (2,"Product data audit","Documented design","Product owner confirms live vs planned features"),
        (3,"Data coverage matrix","Documented","Validate against source systems"),
        (4,"User/account analytics specification","Documented","Confirm identifiers and account states"),
        (5,"Earning/reward analytics specification","Documented design","Authoritative reward/task records not supplied"),
        (6,"Wallet/withdrawal specification","Documented design","Finance/Operations must confirm ledger and payout semantics"),
        (7,"Referral/engagement specification","Documented design","Approve activation and conversion definitions"),
        (8,"Event tracking plan","Proposed","Engineering approval and staging validation"),
        (9,"Data dictionary (75+ fields)","90 proposed fields","Confirm physical schema and constraints"),
        (10,"Logical data model and ERD","Proposed","Not verified production schema"),
        (11,"KPI catalogue (30+ KPIs)","36 proposed KPIs","Approve formulas, units, sources and denominators"),
        (12,"Simulated data profiling","Source-limited","Full Task 01 transaction/event pack not supplied"),
        (13,"Data-quality audit","Partial/source-limited","Production datasets not supplied"),
        (14,"Dashboard blueprint","Seven areas specified","Blueprint is not a production dashboard implementation"),
        (15,"Developer analytics handoff","Proposed","Engineering sign-off required"),
        (16,"Data pipeline and operating model","Proposed","Not deployed"),
        (17,"Privacy/access/governance","Proposed","Security/Legal review required"),
        (18,"Analytics change management","Proposed process","Internal owner adoption required"),
        (19,"Gap assessment","Documented","Update after company review"),
        (20,"Assumption and verification register","Documented","Resolve To Be Verified items"),
        (21,"Prioritized implementation backlog","Documented proposal","Confirm owners and priorities"),
    ]
    df = pd.DataFrame(rows, columns=["#","Deliverable","Evidence status","Remaining dependency"])
    st.dataframe(df, hide_index=True, use_container_width=True)
    st.download_button("Export deliverable tracker (CSV)", df.to_csv(index=False).encode("utf-8"), "velop_task01_deliverable_tracker.csv", "text/csv")

elif page == "Seven-dashboard blueprint":
    st.subheader("Dashboard areas required by the assignment")
    dashboards = [
        ("01","Executive Overview","Approved core KPIs, trends, alerts and definitions","Product / leadership","Production sources and approved KPI definitions"),
        ("02","User Analytics","Registration, onboarding, account lifecycle and cohorts","Product / growth","Canonical user IDs and lifecycle events"),
        ("03","Engagement","Active/returning users, task activity and feature usage","Product / analytics","Session/event data and approved activity definition"),
        ("04","Rewards","Earned, pending, credited, reversed and corrected rewards","Rewards operations / finance","Authoritative reward ledger and reward units"),
        ("05","Wallet","Ledger credits/debits, balances and reconciliation","Finance / operations","Wallet ledger, transaction IDs and reconciliation rules"),
        ("06","Withdrawals","Requests, outcomes, failure reasons and processing time","Operations / finance","Payout source of truth, status history and timestamps"),
        ("07","Referrals","Referral creation, registration, activation and conversion","Growth / product","Referral attribution and approved conversion definition"),
    ]
    for num,name,metrics,owner,dependency in dashboards:
        with st.expander(f"{num} · {name}", expanded=(num=="01")):
            st.write("**Business measures:** " + metrics)
            st.write("**Primary stakeholder:** " + owner)
            st.write("**Source/approval dependency:** " + dependency)
            st.write("**Specification status:** Blueprint only; visual-level metric formulas, dimensions, filters, date range and refresh rules are in the submission report/workbook and require owner validation.")
    st.caption("This page describes the seven dashboard areas required by the assignment. It does not claim that production dashboards have been implemented.")

elif page == "Acceptance blockers":
    st.subheader("Items preventing an honest claim of full completion")
    blockers = [
        ("Hosting platform","Open","The assignment email specifies Vercel or Netlify. The current public URL is Streamlit Community Cloud; this is not compliant unless the coordinator approves an exception."),
        ("Production data","Open","No authorized production extracts or API/database credentials were supplied. Actual company performance cannot be shown."),
        ("Scope confirmation","Open","The behavior workbook identifies itself as Task 02. Do not merge it into Task 01 without coordinator approval."),
        ("Company definitions","Open","Product/Engineering must confirm event implementation, canonical IDs, statuses, timestamps and source systems."),
        ("Finance/Operations sign-off","Open","Reward units, wallet ledger semantics, withdrawal states and reconciliation rules need authoritative confirmation."),
        ("Browser QA","Open","GitHub Actions verifies dependency installation, Python compilation, app startup and health endpoint; it does not prove all browser interactions or mobile breakpoints."),
        ("Live deployment freshness","Unverified","A successful GitHub commit/CI run alone does not prove that the public URL has redeployed to that commit."),
    ]
    st.dataframe(pd.DataFrame(blockers, columns=["Gate","Status","Evidence / next action"]), hide_index=True, use_container_width=True)
    st.markdown('<div class="note"><b>Acceptance rule:</b> only mark a gate complete after evidence exists. Do not replace missing company facts with invented transactions or metrics.</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("VELOOP Rewards · Task 01 · Source-grounded analytical blueprint · No production system connected")
