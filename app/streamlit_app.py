import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="VELOOP Rewards | Analytics Prototype", page_icon="📊", layout="wide")
st.title("VELOOP Rewards — Product Analytics Prototype")
st.warning("SIMULATED DATA — CREATED FOR ANALYTICAL TESTING. This demo uses illustrative records generated in code; it is not production VELOOP data.")
st.caption("Task 01: Product Analytics, Data Readiness & Data Management | Prepared by Gaurav Nikam")

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
    st.header("Prototype controls")
    view = st.radio("Dashboard view", ["Executive overview", "Engagement & tasks", "Rewards & wallet", "Withdrawals & referrals", "Data readiness"])
    st.caption("Illustrative sample counts only. Do not report as company performance.")

if view == "Executive overview":
    cols = st.columns(4)
    for col, label, value in zip(cols, ["Task sample rows", "Reward sample rows", "Wallet sample rows", "Feature event samples"], [len(activity), len(rewards), len(wallet), len(events)]):
        col.metric(label, value)
    coverage = pd.DataFrame({"Domain": ["Task activity", "Rewards", "Wallet", "Withdrawals", "Referrals", "Feature events"], "Illustrative rows": [len(activity), len(rewards), len(wallet), len(withdrawals), len(referrals), len(events)]})
    st.plotly_chart(px.bar(coverage, x="Domain", y="Illustrative rows", title="Illustrative sample records by domain"), use_container_width=True)
    st.info("The source Task 01 workbook supplied user/account data only. Transaction-domain samples here are generated in code solely to demonstrate proposed dashboard layouts.")
elif view == "Engagement & tasks":
    st.subheader("Engagement and task diagnostics")
    st.plotly_chart(px.bar(activity["task_status"].value_counts().rename_axis("Status").reset_index(name="Sample records"), x="Status", y="Sample records"), use_container_width=True)
    st.plotly_chart(px.bar(events["event_name"].value_counts().head(15).rename_axis("Event").reset_index(name="Sample events"), x="Event", y="Sample events"), use_container_width=True)
    st.plotly_chart(px.histogram(activity, x="task_category", title="Illustrative task categories"), use_container_width=True)
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
    st.markdown("**Recommended order**\n1. Confirm source-of-truth tables, stable IDs, timezone and status enums.\n2. Instrument critical lifecycle events and maintain immutable reward/wallet ledgers.\n3. Add duplicate, chronology, foreign-key and reconciliation checks.\n4. Validate KPI formulas with business owners.\n5. Publish business dashboards only after source data and definitions are approved.")

st.divider()
st.caption("No connection to VELOOP production systems is configured. All displayed records are illustrative demo data.")
