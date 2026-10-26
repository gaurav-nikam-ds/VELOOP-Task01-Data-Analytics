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
.insight-card { background:#fff; border:1px solid var(--line); border-radius:12px; padding:1rem; min-height:180px; }
@media (max-width:800px) { .block-container { padding:.65rem .65rem 1.5rem; } .hero { padding:1rem; } }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>VELOOP Rewards — Product Analytics & Data Readiness</h1>
  <p>Evidence-based findings, business questions, recommended actions and implementation dependencies from the supplied assignment materials. This workspace distinguishes source-file findings from unverified production performance.</p>
</div>
""", unsafe_allow_html=True)

st.warning("DATA LIMITATION: The assignment identifies its supplied data as simulated. No authorized production extract or production-system connection was supplied. Findings below describe the supplied workbooks only; they are not claims about actual VELOOP users or business performance.")

with st.sidebar:
    st.markdown("## ◈ VELOOP REWARDS")
    st.caption("TASK 01 · ANALYTICS & DECISION SUPPORT")
    page = st.radio("WORKSPACE", [
        "Executive status",
        "Insights & recommendations",
        "Supplied data audit",
        "Deliverable tracker",
        "Seven-dashboard blueprint",
        "Acceptance blockers",
        "Implementation library",
    ])
    st.markdown("---")
    st.caption("Evidence basis: supplied Task 01 PDF, Task 01 workbook, separate Task 02 workbook and assignment email.")
    st.markdown("[Open full analytics foundation pack](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/blob/main/docs/ANALYTICS_FOUNDATION_IMPLEMENTATION_PACK.md)")
    st.markdown("[Open requirements checklist](https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/blob/main/docs/TASK01_REQUIREMENTS_CHECKLIST.md)")

if page == "Executive status":
    st.subheader("Current submission status")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Required final deliverables", "21")
    c2.metric("Proposed KPI definitions", "36")
    c3.metric("Proposed dictionary fields", "90")
    c4.metric("Production connections", "0")
    st.markdown("""
    **What the evidence supports**
    - The assignment is a product-analytics and data-readiness blueprint.
    - The Task 01 workbook includes clean and messy user-profile tabs, plus dictionary/summary tabs.
    - The separately supplied behavior workbook labels itself Task 02 and is kept separate pending coordinator approval.
    - Reward, wallet, withdrawal and referral business performance cannot be measured from the supplied Task 01 user-profile tabs alone.
    """)
    st.markdown('<div class="note"><b>Decision:</b> first improve data reliability and confirm authoritative business sources. Then calculate and interpret product KPIs from approved data. Do not publish synthetic counts as actual company results.</div>', unsafe_allow_html=True)

elif page == "Insights & recommendations":
    st.subheader("What can an analyst conclude from the supplied evidence?")
    st.caption("The following are source-file quality insights. They are not production performance insights because the supplied assignment data is simulated.")
    a,b,c,d = st.columns(4)
    a.metric("Clean user profiles", "1,000")
    b.metric("Referral detail missing", "88.1%", "881 of 1,000 clean profiles")
    c.metric("Last-login timestamp missing", "7.2%", "72 of 1,000 clean profiles")
    d.metric("Repeated IDs in messy tab", "8", "in 1,008 rows")

    st.markdown("### Descriptive engagement patterns in the supplied simulated user file")
    st.caption("These are calculations on the 1,000-row simulated Users_1000_Clean sheet only. They are useful for demonstrating analytical method, but must not be represented as actual VELOOP performance.")
    e1,e2,e3,e4 = st.columns(4)
    e1.metric("Active in last 7 days", "7.8%", "78 / 1,000 profiles")
    e2.metric("Active in last 30 days", "32.5%", "325 / 1,000 profiles")
    e3.metric("Onboarding completed", "72.2%", "722 / 1,000 profiles")
    e4.metric("Email verified", "85.5%", "855 / 1,000 profiles")

    st.markdown("#### 30-day activity by acquisition source")
    source_activity = pd.DataFrame([
        {"Acquisition source":"Telegram","Users":55,"Active in 30 days":27,"30-day active share":49.1},
        {"Acquisition source":"Referral","Users":119,"Active in 30 days":43,"30-day active share":36.1},
        {"Acquisition source":"Other","Users":102,"Active in 30 days":34,"30-day active share":33.3},
        {"Acquisition source":"Organic Search","Users":244,"Active in 30 days":80,"30-day active share":32.8},
        {"Acquisition source":"WhatsApp","Users":103,"Active in 30 days":32,"30-day active share":31.1},
        {"Acquisition source":"Social Media","Users":160,"Active in 30 days":49,"30-day active share":30.6},
        {"Acquisition source":"Direct","Users":217,"Active in 30 days":60,"30-day active share":27.6},
    ])
    st.dataframe(source_activity, hide_index=True, use_container_width=True)
    st.markdown("**Dataset-only interpretation:** in this simulated file, 30-day active share varies from 27.6% for Direct to 49.1% for Telegram. Telegram has the smallest listed group (55 users), so its higher share should be treated as a hypothesis to validate—not proof that the channel causes better retention.")
    st.markdown("**Recommended next analysis:** validate the active-30-day definition and observation window, compare cohorts by registration date, and check sample sizes and user mix before suggesting acquisition-budget changes.")

    st.markdown("#### Onboarding status and 30-day activity")
    onboarding_activity = pd.DataFrame([
        {"Onboarding status":"Completed","Users":722,"Active in 30 days":249,"30-day active share":34.5},
        {"Onboarding status":"Not Started","Users":132,"Active in 30 days":38,"30-day active share":28.8},
        {"Onboarding status":"Started","Users":146,"Active in 30 days":38,"30-day active share":26.0},
    ])
    st.dataframe(onboarding_activity, hide_index=True, use_container_width=True)
    st.markdown("**Dataset-only interpretation:** completed-onboarding profiles have a higher 30-day active share (34.5%) than profiles marked Started (26.0%). This is an association in simulated data, not evidence that onboarding completion causes retention. Confirm event definitions and analyze real cohorts before product changes.")

    st.markdown("#### Verification status and 30-day activity")
    verification_activity = pd.DataFrame([
        {"Email verification status":"Verified","Users":855,"Active in 30 days":305,"30-day active share":35.7},
        {"Email verification status":"Pending","Users":145,"Active in 30 days":20,"30-day active share":13.8},
    ])
    st.dataframe(verification_activity, hide_index=True, use_container_width=True)
    st.markdown("**Dataset-only interpretation:** the simulated file shows 35.7% 30-day active share for verified profiles versus 13.8% for pending profiles. This is an association, not proof that verification causes activity. It may reflect account eligibility, user intent, or data-generation assumptions.")
    st.markdown("**Recommended action:** validate the verification-state lifecycle and check whether users can meaningfully use the product before verification. In production, compare cohorts and measure the verification funnel before changing onboarding.")

    st.markdown("#### Account status distribution")
    account_status_summary = pd.DataFrame([
        {"Account status":"Active","Users":568,"Share of profiles":56.8,"Active in 30 days":205,"30-day active share":36.1},
        {"Account status":"Inactive","Users":283,"Share of profiles":28.3,"Active in 30 days":95,"30-day active share":33.6},
        {"Account status":"Suspended","Users":77,"Share of profiles":7.7,"Active in 30 days":25,"30-day active share":32.5},
        {"Account status":"Pending Verification","Users":72,"Share of profiles":7.2,"Active in 30 days":0,"30-day active share":0.0},
    ])
    st.dataframe(account_status_summary, hide_index=True, use_container_width=True)
    st.markdown("**Data-definition risk:** some records labelled Inactive or Suspended still have the is_active_30d flag set to Yes. This may be legitimate if fields use different definitions or snapshots, but it must be reconciled before reporting an active-user KPI.")
    st.markdown("**Recommended action:** ask Product/Engineering to define the precedence and timestamp semantics for account_status versus activity flags; add a documented consistency check rather than assuming one field is wrong.")

    st.markdown("### Findings → business risk → recommended action")
    findings = [
        {
            "Finding":"Referral source detail is missing in 881/1,000 clean profiles (88.1%).",
            "Evidence":"Task 01 workbook: Users_1000_Clean.",
            "Risk / limitation":"Referral attribution analysis may be incomplete or biased if missingness is not understood. This does not prove referrals perform poorly.",
            "Recommendation":"Define which referral-source fields are required, distinguish 'unknown/not collected/not applicable', and validate capture at registration/referral entry.",
            "Priority":"High",
            "Owner to confirm":"Product + Engineering",
            "Success check":"Measure missing-source rate on a new, approved extract and reconcile it with the event/attribution source."
        },
        {
            "Finding":"Last-login timestamp is missing in 72/1,000 clean profiles (7.2%).",
            "Evidence":"Task 01 workbook: Users_1000_Clean.",
            "Risk / limitation":"Last-login-based activity or recency metrics could undercount or misclassify users unless missing values have an explicit meaning.",
            "Recommendation":"Confirm the authoritative activity event and timestamp definition; validate timezone, null semantics and update behavior before defining active/retained users.",
            "Priority":"High",
            "Owner to confirm":"Product Analytics + Engineering",
            "Success check":"Compare profile last-login values against approved login/session events and document expected exceptions."
        },
        {
            "Finding":"The messy audit sheet has 1,008 rows but 1,000 unique IDs (8 repeated IDs).",
            "Evidence":"Task 01 workbook: Users_Messy_Audit.",
            "Risk / limitation":"Naive row counts or joins can double-count users and distort profile-level metrics.",
            "Recommendation":"Add a uniqueness test for user_id at the agreed grain; quarantine duplicates and define a deterministic survivorship rule before deduplication.",
            "Priority":"High",
            "Owner to confirm":"Data Engineering / Data Owner",
            "Success check":"Duplicate-ID count is reported on each load and unresolved duplicates are traceable."
        },
        {
            "Finding":"The messy audit sheet contains 4 negative days_since_registration values and 1 missing registration timestamp.",
            "Evidence":"Task 01 workbook: Users_Messy_Audit.",
            "Risk / limitation":"Derived tenure and cohort calculations can be invalid when dates are missing or chronology is impossible.",
            "Recommendation":"Recompute tenure from the canonical registration timestamp and the agreed as-of date; reject or flag impossible chronology rather than silently altering it.",
            "Priority":"High",
            "Owner to confirm":"Data Engineering / Data Owner",
            "Success check":"Invalid chronology is zero in the validated output, or every exception is explicitly logged with a reason."
        },
        {
            "Finding":"The separate Task 02 event audit has 35,714 rows and 10 exact duplicate rows.",
            "Evidence":"Separately supplied Task 02 workbook; not merged into Task 01.",
            "Risk / limitation":"Duplicate events can inflate activity counts if event identity and idempotency rules are not enforced.",
            "Recommendation":"Ask the coordinator to confirm whether Task 02 data may be used; if approved, deduplicate using the agreed event key and add an ingestion idempotency test.",
            "Priority":"Medium",
            "Owner to confirm":"Coordinator + Engineering",
            "Success check":"Approved event dataset has a documented unique event key and duplicate rate is monitored."
        },
    ]
    df = pd.DataFrame(findings)
    for i, item in enumerate(findings):
        with st.container(border=True):
            st.markdown(f"**Finding {i+1}: {item['Finding']}**")
            st.caption("Evidence: " + item["Evidence"])
            st.write("**Business risk / limitation:** " + item["Risk / limitation"])
            st.write("**Recommended action:** " + item["Recommendation"])
            x,y = st.columns(2)
            x.write("**Priority:** " + item["Priority"])
            y.write("**Owner to confirm:** " + item["Owner to confirm"])
            st.write("**Validation / success check:** " + item["Success check"])
    st.download_button("Export evidence-based recommendations (CSV)", df.to_csv(index=False).encode("utf-8"), "velop_task01_evidence_based_recommendations.csv", "text/csv")

    st.markdown("### Business decisions that still need production data")
    st.dataframe(pd.DataFrame([
        {"Business question":"Are users returning and retaining?","Data needed":"Approved login/session/activity events; user IDs; event timestamps","Decision enabled":"Prioritize onboarding or engagement improvements only after cohort analysis"},
        {"Business question":"Which earning tasks perform well?","Data needed":"Task impressions, starts, completions, failures, partner/source, reward and timestamps","Decision enabled":"Investigate task funnel drop-offs and prioritize reliable/high-value task sources"},
        {"Business question":"Are rewards credited accurately?","Data needed":"Authoritative reward ledger with pending/credited/reversed states and transaction IDs","Decision enabled":"Reconcile crediting issues and reduce unexplained reward discrepancies"},
        {"Business question":"Where do withdrawals fail or take too long?","Data needed":"Withdrawal state history, timestamps, failure reasons and payout outcomes","Decision enabled":"Target operational bottlenecks and improve user communication"},
        {"Business question":"Which referrals convert?","Data needed":"Referral attribution, referred-user registration, activation and eligibility events","Decision enabled":"Compare referral channels using approved attribution and conversion definitions"},
    ]), hide_index=True, use_container_width=True)
    st.markdown('<div class="note"><b>Decision rule:</b> the recommendations above are data-readiness actions supported by the supplied files. Product-growth or revenue recommendations must wait for the relevant production records and approved KPI definitions.</div>', unsafe_allow_html=True)

elif page == "Supplied data audit":
    st.subheader("Task 01 source workbook")
    a,b,c,d = st.columns(4)
    a.metric("Clean users", "1,000")
    b.metric("Clean-sheet columns", "27")
    c.metric("Messy audit rows", "1,008")
    d.metric("Repeated IDs in messy tab", "8")
    st.dataframe(pd.DataFrame([
        {"Source sheet":"Users_1000_Clean","Rows":1000,"Columns":27,"Finding":"1,000 unique, non-null user_id values; 0 exact duplicate rows"},
        {"Source sheet":"Users_1000_Clean","Rows":1000,"Columns":27,"Finding":"881 missing referral_source_detail; 72 missing last_login_datetime"},
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
    st.caption("These are findings from the supplied simulated assignment workbooks, not actual VELOOP production statistics. Missingness should be interpreted against field-level rules; do not silently delete or correct records.")

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

elif page == "Implementation library":
    st.subheader("Task 01 implementation specifications")
    st.caption("These are deliverable specifications and source-file findings. Proposed product behavior is not represented as implemented production functionality.")
    library = [
        ("Source data profile & quality audit", "Evidence-backed row/column counts, missingness, duplicate IDs, invalid chronology, cross-tabs and data-quality acceptance rules.", "https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/blob/main/docs/SOURCE_DATA_PROFILE_AND_QUALITY_AUDIT.md"),
        ("Data dictionary field index", "The 90-field logical inventory, metadata contract, sensitivity and validation rules.", "https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/blob/main/docs/DATA_DICTIONARY_FIELD_INDEX.md"),
        ("Developer analytics handoff", "Event envelope, lifecycle event catalogue, ledger/state rules and 15 engineering acceptance tests.", "https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/blob/main/docs/DEVELOPER_ANALYTICS_HANDOFF.md"),
        ("Seven-dashboard visual specifications", "Visual-by-visual measures, calculations, source dependencies, filters, questions and decisions for all seven dashboard areas.", "https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/blob/main/docs/DASHBOARD_VISUAL_SPECIFICATIONS.md"),
        ("Analytics change log & operating model", "Change log schema, review workflow, domain ownership, incident response and release acceptance.", "https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/blob/main/docs/ANALYTICS_CHANGE_LOG_AND_OPERATING_MODEL.md"),
        ("Analytics foundation implementation pack", "Product map, event contract, logical model, quality controls, KPI catalogue, governance, gaps, verification register and backlog.", "https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/blob/main/docs/ANALYTICS_FOUNDATION_IMPLEMENTATION_PACK.md"),
        ("Requirements-to-evidence checklist", "Traceability across all 21 assignment deliverables and explicit acceptance blockers.", "https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/blob/main/docs/TASK01_REQUIREMENTS_CHECKLIST.md"),
        ("Supplied-source audit", "Source scope, what can and cannot be concluded, and the Task 02 separation guardrail.", "https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/blob/main/docs/THREE_SOURCE_FILES_AUDIT.md"),
    ]
    for title, description, url in library:
        with st.container(border=True):
            st.markdown("**" + title + "**")
            st.write(description)
            st.markdown("[Open document](" + url + ")")
    st.markdown("### Minimum event contract")
    st.dataframe(pd.DataFrame([
        {"Field":"event_id","Requirement":"Unique event identity; deduplicate safely"},
        {"Field":"event_name / event_version","Requirement":"Approved event name and versioned schema"},
        {"Field":"event_timestamp / received_timestamp","Requirement":"Occurrence time and ingestion time kept separately"},
        {"Field":"user_id / session_id","Requirement":"Stable identifiers under approved anonymous-event rules"},
        {"Field":"transaction_id / attempt_id","Requirement":"Business transaction and task retry identities where applicable"},
        {"Field":"feature_name / platform / environment","Requirement":"Controlled values; environment must not be inferred"},
        {"Field":"source_system / status / properties","Requirement":"Producer, approved state and allow-listed properties"},
        {"Field":"idempotency_key / correlation_id","Requirement":"Retry safety and workflow traceability"},
    ]), hide_index=True, use_container_width=True)
    st.markdown("### Critical quality gates")
    st.dataframe(pd.DataFrame([
        {"Gate":"Identity integrity","Acceptance":"Required IDs present; uniqueness and foreign-key checks pass or exceptions are quarantined"},
        {"Gate":"Timestamp integrity","Acceptance":"Parseable UTC event and received timestamps; impossible chronology flagged"},
        {"Gate":"State integrity","Acceptance":"Only approved state transitions; unknown values are not silently mapped"},
        {"Gate":"Financial integrity","Acceptance":"Reward/wallet/withdrawal ledger transactions reconcile to approved sources"},
        {"Gate":"Freshness","Acceptance":"Stale sources are visible and affected KPIs are marked unavailable/stale"},
        {"Gate":"Authenticity","Acceptance":"Simulated values remain explicitly labelled; no production performance claims"},
    ]), hide_index=True, use_container_width=True)
    st.info("The assignment's data-authenticity policy is mandatory: supplied workbook metrics are simulated. The workbook alone does not support actual reward, wallet, withdrawal, referral-conversion or production-retention claims.")

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
st.caption("VELOOP Rewards · Task 01 · Evidence-based analysis and decision support · No production system connected")
