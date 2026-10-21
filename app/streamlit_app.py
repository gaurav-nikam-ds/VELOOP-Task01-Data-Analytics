import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="VELOOP Rewards | Analytics Prototype", page_icon="📊", layout="wide")

st.markdown("""
<style>
.stApp { background: #f7f8fa; color: #202938; }
.block-container { max-width: 1320px; padding-top: 1.25rem; padding-bottom: 2.5rem; }
[data-testid="stHeader"] { background: #f7f8fa; }
[data-testid="stSidebar"] { background: #ffffff; border-right: 1px solid #e5e7eb; }
[data-testid="stSidebar"] * { color: #202938; }
h1, h2, h3 { color: #202938; letter-spacing: -0.02em; }
h1 { font-size: 1.9rem !important; font-weight: 700 !important; }
h2 { font-size: 1.35rem !important; font-weight: 650 !important; }
h3 { font-size: 1.05rem !important; font-weight: 650 !important; }
[data-testid="stMetric"] { background: #fff; border: 1px solid #e5e7eb; padding: .85rem 1rem; border-radius: 10px; }
[data-testid="stMetricLabel"] p { color: #667085; font-size: .82rem; }
[data-testid="stMetricValue"] { color: #176b63; font-weight: 700; }
[data-testid="stPlotlyChart"], [data-testid="stDataFrame"] { background: #fff; border: 1px solid #e5e7eb; border-radius: 10px; padding: .25rem; }
[data-testid="stAlert"] { border-radius: 9px; }
hr { border-color: #e5e7eb; }
@media (max-width: 768px) {
 .block-container { padding: .8rem .7rem 1.5rem; }
 h1 { font-size: 1.55rem !important; }
}
</style>
""", unsafe_allow_html=True)

st.title("VELOOP Rewards Analytics")
st.warning("SIMULATED DATA — CREATED FOR ANALYTICAL TESTING. These illustrative records are not production VELOOP data.")
st.caption("Task 01 · Product analytics and data readiness")

@st.cache_data
def make_demo_data():
    # Deterministic illustrative data only; no production records or personal data.
    tasks = pd.DataFrame({
        "task_status": ["completed", "started", "validated", "rejected", "completed", "started", "validated", "completed", "rejected", "started"],
        "task_category": ["survey", "game", "offer", "survey", "game", "offer", "survey", "game", "offer", "survey"],
    })
    rewards = pd.DataFrame({
        "reward_status": ["credited", "pending", "credited", "reversed", "pending", "credited"],
        "unit": ["VE", "VE", "XP", "VE", "Gems", "XP"],
        "amount": [12, 8, 40, -5, 3, 25],
    })
    wallet = pd.DataFrame({"transaction_type": ["credit", "debit", "credit", "reversal", "credit", "debit"]})
    withdrawals = pd.DataFrame({"status": ["completed", "pending", "failed", "completed", "under_review"]})
    referrals = pd.DataFrame({"status": ["registered", "activated", "pending", "converted", "registered"]})
    events = pd.DataFrame({"event_name": ["app_open", "task_viewed", "task_started", "task_completed", "app_open", "reward_viewed", "task_started", "withdrawal_viewed"]})
    return tasks, rewards, wallet, withdrawals, referrals, events

activity, rewards, wallet, withdrawals, referrals, events = make_demo_data()
with st.sidebar:
    st.markdown("#### Dashboard views")
    view = st.radio("Dashboard view", ["Executive overview", "Engagement & tasks", "Rewards & wallet", "Withdrawals & referrals", "Data readiness"])
    st.caption("Prototype · sample data only")

if view == "Executive overview":
    cols = st.columns(4)
    for col, label, value in zip(cols, ["Task sample rows", "Reward sample rows", "Wallet sample rows", "Feature event samples"], [len(activity), len(rewards), len(wallet), len(events)]):
        col.metric(label, value)
    coverage = pd.DataFrame({"Domain": ["Task activity", "Rewards", "Wallet", "Withdrawals", "Referrals", "Feature events"], "Illustrative rows": [len(activity), len(rewards), len(wallet), len(withdrawals), len(referrals), len(events)]})
    fig = px.bar(coverage, x="Domain", y="Illustrative rows", title="Sample records by domain", color_discrete_sequence=["#287d73"])
    fig.update_layout(template="plotly_white", margin=dict(l=16, r=16, t=55, b=16), font=dict(family="Arial, sans-serif", color="#344054"), title_font_size=16, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    st.info("The source Task 01 workbook supplied user/account data only. Transaction-domain samples here are generated in code solely to demonstrate proposed dashboard layouts.")
elif view == "Engagement & tasks":
    st.subheader("Engagement and task diagnostics")
    fig = px.bar(activity["task_status"].value_counts().rename_axis("Status").reset_index(name="Sample records"), x="Status", y="Sample records", title="Task status", color_discrete_sequence=["#287d73"])
    fig.update_layout(template="plotly_white", margin=dict(l=16, r=16, t=55, b=16), font=dict(family="Arial, sans-serif", color="#344054"), title_font_size=16, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    fig = px.bar(events["event_name"].value_counts().head(15).rename_axis("Event").reset_index(name="Sample events"), x="Event", y="Sample events", title="Feature event samples", color_discrete_sequence=["#6486b8"])
    fig.update_layout(template="plotly_white", margin=dict(l=16, r=16, t=55, b=16), font=dict(family="Arial, sans-serif", color="#344054"), title_font_size=16, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    fig = px.histogram(activity, x="task_category", title="Task category samples", color_discrete_sequence=["#6486b8"])
    fig.update_layout(template="plotly_white", margin=dict(l=16, r=16, t=55, b=16), font=dict(family="Arial, sans-serif", color="#344054"), title_font_size=16, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("A production conversion funnel requires an approved eligible-start denominator and authoritative completion/validation states.")
elif view == "Rewards & wallet":
    left, right = st.columns(2)
    left.plotly_chart(px.bar(rewards["reward_status"].value_counts().rename_axis("Status").reset_index(name="Sample records"), x="Status", y="Sample records", title="Illustrative reward statuses"), use_container_width=True)
    right.plotly_chart(px.bar(wallet["transaction_type"].value_counts().rename_axis("Type").reset_index(name="Sample records"), x="Type", y="Sample records", title="Illustrative wallet transaction types"), use_container_width=True)
    st.dataframe(rewards.groupby("unit", dropna=False)["amount"].sum().reset_index(), use_container_width=True)
    st.warning("Values are illustrative. Different reward units must not be summed together; production ledger and reversal rules are unverified.")
elif view == "Withdrawals & referrals":
    left, right = st.columns(2)
    left.plotly_chart(px.bar(withdrawals["status"].value_counts().rename_axis("Status").reset_index(name="Sample records"), x="Status", y="Sample records", title="Illustrative withdrawal statuses"), use_container_width=True)
    right.plotly_chart(px.bar(referrals["status"].value_counts().rename_axis("Status").reset_index(name="Sample records"), x="Status", y="Sample records", title="Illustrative referral statuses"), use_container_width=True)
    st.caption("Withdrawal durations need approved terminal-state timestamps. Referral registration, activation and conversion are distinct lifecycle stages.")
else:
    st.subheader("Data readiness and evidence gaps")
    gaps = pd.DataFrame([
        ["User/account records", "Simulated Task 01 workbook exists", "Profile only the supplied simulated records"],
        ["Task/reward/wallet/withdrawal/referral/events", "No production extracts supplied", "Demo samples are synthetic; obtain authorized source data"],
        ["Event instrumentation", "Not verified", "Engineering to confirm event names, payloads, IDs and timezone"],
        ["Reward units and ledger states", "Not internally confirmed", "Product/Operations/Finance to approve units, reversals and reconciliation"],
        ["DAU/WAU/MAU", "Qualifying event rules not approved", "Define event list, timezone and window convention"],
        ["Privacy and retention", "Design recommendations only", "Security/legal owner to approve retention and access roles"],
    ], columns=["Area", "Evidence available", "Gap / next action"])
    st.dataframe(gaps, use_container_width=True, hide_index=True)
    st.markdown("**Recommended order**
1. Confirm source-of-truth tables, stable IDs, timezone and status enums.
2. Instrument critical lifecycle events and maintain immutable reward/wallet ledgers.
3. Add duplicate, chronology, foreign-key and reconciliation checks.
4. Validate KPI formulas with business owners.
5. Publish business dashboards only after source data and definitions are approved.")

st.divider()
st.markdown("<div style=\"padding:.85rem 1rem;border:1px solid #dbe3ed;border-radius:12px;background:#fff;color:#64748b;font-size:.82rem\">No connection to VELOOP production systems is configured. All displayed records are illustrative demo data.</div>", unsafe_allow_html=True)
