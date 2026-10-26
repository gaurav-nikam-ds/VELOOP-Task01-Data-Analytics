import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="VELOOP | Product Intelligence", page_icon="◈", layout="wide", initial_sidebar_state="expanded")

# Visual system: restrained enterprise palette, high contrast, consistent spacing.
st.markdown("""
<style>
:root { --ink:#182230; --muted:#667085; --line:#e4e7ec; --canvas:#f5f7fa; --teal:#087e8b; --blue:#4677c8; --violet:#8064a2; --amber:#d58b22; }
.stApp { background:var(--canvas); color:var(--ink); }
.block-container { max-width:1500px; padding:1.25rem 2rem 3rem; }
[data-testid="stHeader"] { background:rgba(245,247,250,.92); }
[data-testid="stSidebar"] { background:#fff; border-right:1px solid var(--line); }
[data-testid="stSidebar"] * { color:var(--ink); }
h1,h2,h3 { color:var(--ink); letter-spacing:-.035em; }
h1 { font-size:2rem!important; font-weight:750!important; }
h2 { font-size:1.32rem!important; font-weight:700!important; }
h3 { font-size:1rem!important; font-weight:650!important; }
[data-testid="stMetric"] { background:#fff; border:1px solid var(--line); border-radius:14px; padding:1rem 1.05rem; box-shadow:0 1px 2px rgba(16,24,40,.025); min-height:118px; }
[data-testid="stMetricLabel"] p { color:var(--muted); font-size:.79rem; font-weight:600; }
[data-testid="stMetricValue"] { color:var(--ink); font-weight:750; font-size:1.8rem; }
[data-testid="stMetricDelta"] { font-size:.76rem; }
[data-testid="stPlotlyChart"] { background:#fff; border:1px solid var(--line); border-radius:14px; padding:.35rem; }
[data-testid="stDataFrame"] { background:#fff; border:1px solid var(--line); border-radius:12px; }
[data-testid="stAlert"] { border-radius:12px; }
hr { border-color:var(--line); }
div[data-testid="stVerticalBlockBorderWrapper"] { border-color:var(--line)!important; border-radius:14px!important; }
.hero { background:linear-gradient(115deg,#102a43 0%,#174a63 52%,#087e8b 100%); border-radius:18px; padding:1.5rem 1.7rem; color:#fff; margin-bottom:1rem; box-shadow:0 8px 24px rgba(16,42,67,.12); }
.hero-kicker { color:#b8e5e8; font-size:.73rem; font-weight:750; letter-spacing:.14em; text-transform:uppercase; }
.hero-title { color:#fff; font-size:1.8rem; line-height:1.2; font-weight:760; margin:.35rem 0 .45rem; letter-spacing:-.04em; }
.hero-sub { color:#e3f2f4; font-size:.94rem; max-width:850px; line-height:1.55; }
.section-label { color:#667085; font-size:.72rem; font-weight:750; letter-spacing:.12em; text-transform:uppercase; margin:.25rem 0 .65rem; }
.insight { background:#fff; border:1px solid var(--line); border-left:4px solid var(--teal); border-radius:10px; padding:.9rem 1rem; color:#344054; line-height:1.55; }
.mini-note { color:#667085; font-size:.78rem; }
@media (max-width:800px) { .block-container { padding:.7rem .7rem 1.5rem; } .hero { padding:1.1rem; } .hero-title { font-size:1.45rem; } h1 { font-size:1.55rem!important; } }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def build_demo():
    # Deterministic synthetic data for visual prototyping; never production records.
    rng = np.random.default_rng(42)
    n = 1800
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=90, freq="D")
    day_idx = rng.integers(0, len(dates), n)
    domain = rng.choice(["Surveys", "Games", "Offers", "Learning", "Referrals"], n, p=[.30,.22,.24,.14,.10])
    status = rng.choice(["Completed", "Started", "Validated", "Rejected", "Expired"], n, p=[.48,.22,.13,.09,.08])
    user_ids = rng.integers(10001, 10601, n)
    category_multiplier = pd.Series(domain).map({"Surveys":1.0,"Games":1.2,"Offers":1.5,"Learning":.8,"Referrals":1.1}).to_numpy()
    points = np.maximum(0, np.round(rng.gamma(2.1, 18, n) * category_multiplier, 0)).astype(int)
    task = pd.DataFrame({"date":dates[day_idx],"domain":domain,"status":status,"user_id":user_ids,"points":points,
                         "duration_min":np.round(rng.gamma(2.5, 4.5, n),1)})
    task["completed_flag"] = task["status"].eq("Completed")
    task["month_day"] = task["date"].dt.strftime("%d %b")
    reward = pd.DataFrame({"date":dates[rng.integers(0,90,850)],"type":rng.choice(["Earned","Redeemed","Reversed","Pending"],850,p=[.56,.22,.08,.14]),
                           "unit":rng.choice(["VE","XP","Gems"],850,p=[.52,.33,.15]),"amount":np.round(rng.gamma(2,24,850),0)})
    wallet = pd.DataFrame({"date":dates[rng.integers(0,90,620)],"movement":rng.choice(["Credit","Debit","Reversal"],620,p=[.59,.33,.08]),
                           "amount":np.round(rng.gamma(2.4,32,620),2)})
    withdrawal = pd.DataFrame({"date":dates[rng.integers(0,90,240)],"status":rng.choice(["Completed","Pending","Under review","Failed"],240,p=[.62,.16,.13,.09]),
                               "amount":np.round(rng.gamma(2.6,110,240),2),"processing_hours":np.round(rng.gamma(2.5,8,240),1)})
    referral = pd.DataFrame({"date":dates[rng.integers(0,90,310)],"stage":rng.choice(["Registered","Activated","Converted","Pending"],310,p=[.37,.27,.20,.16])})
    return task, reward, wallet, withdrawal, referral

tasks, rewards, wallet, withdrawals, referrals = build_demo()
PALETTE = {"teal":"#087e8b","blue":"#4677c8","violet":"#8064a2","amber":"#d58b22","red":"#c65d5d","green":"#27856b"}
STATUS_COLORS = {"Completed":PALETTE["teal"],"Started":PALETTE["blue"],"Validated":PALETTE["green"],"Rejected":PALETTE["red"],"Expired":"#98a2b3",
                 "Earned":PALETTE["teal"],"Redeemed":PALETTE["blue"],"Reversed":PALETTE["red"],"Pending":PALETTE["amber"],
                 "Credit":PALETTE["teal"],"Debit":PALETTE["blue"],"Reversal":PALETTE["red"],"Under review":PALETTE["violet"],"Failed":PALETTE["red"],
                 "Registered":PALETTE["blue"],"Activated":PALETTE["teal"],"Converted":PALETTE["green"]}

def polish(fig, height=340, legend=False):
    fig.update_layout(template="plotly_white",height=height,margin=dict(l=18,r=18,t=54,b=18),
        font=dict(family="Inter, Arial, sans-serif",size=12,color="#344054"),
        title=dict(font=dict(size=15,color="#182230"),x=.025,xanchor="left"),
        paper_bgcolor="#ffffff",plot_bgcolor="#ffffff",showlegend=legend,
        legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1) if legend else None,
        hoverlabel=dict(bgcolor="#182230",font_size=12,font_color="#ffffff"))
    fig.update_xaxes(showgrid=False,zeroline=False,automargin=True,linecolor="#eaecf0")
    fig.update_yaxes(showgrid=True,gridcolor="#f0f2f5",zeroline=False,automargin=True)
    return fig

def section(label, title, subtitle=None):
    st.markdown(f'<div class="section-label">{label}</div>',unsafe_allow_html=True)
    st.subheader(title)
    if subtitle: st.caption(subtitle)

def metric_row(df):
    completed = df["completed_flag"].mean()*100 if len(df) else 0
    active = df["user_id"].nunique()
    points = int(df.loc[df["completed_flag"],"points"].sum())
    avg_duration = df.loc[df["completed_flag"],"duration_min"].mean() if df["completed_flag"].any() else 0
    cols=st.columns(4)
    cols[0].metric("Task records",f"{len(df):,}",help="Synthetic task records after selected filters")
    cols[1].metric("Completion rate",f"{completed:.1f}%",help="Completed records / all displayed task records")
    cols[2].metric("Distinct demo users",f"{active:,}")
    cols[3].metric("Points on completed tasks",f"{points:,}",help="Illustrative points; not a financial value")
    return avg_duration

with st.sidebar:
    st.markdown("## ◈ VELOOP")
    st.caption("PRODUCT INTELLIGENCE · TASK 01")
    st.markdown("---")
    view=st.radio("WORKSPACE",["Executive overview","Engagement & tasks","Rewards & wallet","Withdrawals & referrals","Data readiness"],label_visibility="visible")
    st.markdown("---")
    st.markdown("**Demo controls**")
    date_range=st.date_input("Activity window",value=(tasks.date.min().date(),tasks.date.max().date()),min_value=tasks.date.min().date(),max_value=tasks.date.max().date())
    domains=st.multiselect("Task domains",options=sorted(tasks.domain.unique()),default=sorted(tasks.domain.unique()))
    st.markdown("---")
    st.caption("Prototype build 02 · Synthetic data")
    st.caption("No production source connection")

if isinstance(date_range,(tuple,list)) and len(date_range)==2:
    start_date,end_date=pd.Timestamp(date_range[0]),pd.Timestamp(date_range[1])
else:
    start_date,end_date=tasks.date.min(),tasks.date.max()
filtered=tasks[tasks.date.between(start_date,end_date)&tasks.domain.isin(domains)].copy()
if filtered.empty:
    st.info("No records match the selected date window and domains. Clear or widen the filters in the sidebar to see task activity.")
    filtered=tasks.iloc[0:0].copy()

# Lightweight exports make the prototype easier to review and inspect.
export_summary = pd.DataFrame([
    {"Metric":"Filtered task records","Value":int(len(filtered)),"Definition":"Number of synthetic task records after current sidebar filters"},
    {"Metric":"Completion rate (%)","Value":round(float(filtered["completed_flag"].mean()*100),2) if len(filtered) else 0,"Definition":"Completed records divided by displayed task records"},
    {"Metric":"Distinct demo users","Value":int(filtered["user_id"].nunique()),"Definition":"Distinct synthetic user IDs in displayed task records"},
    {"Metric":"Points on completed tasks","Value":int(filtered.loc[filtered["completed_flag"],"points"].sum()),"Definition":"Illustrative points on completed task records; not cash value"},
])
st.sidebar.download_button("Download filtered task CSV",data=filtered.to_csv(index=False).encode("utf-8"),file_name="velop_demo_filtered_tasks.csv",mime="text/csv",use_container_width=True,disabled=filtered.empty)
st.sidebar.download_button("Download KPI summary CSV",data=export_summary.to_csv(index=False).encode("utf-8"),file_name="velop_demo_kpi_summary.csv",mime="text/csv",use_container_width=True)

st.markdown(f"""
<div class="hero">
 <div class="hero-kicker">VELOOP REWARDS · ANALYTICS BLUEPRINT</div>
 <div class="hero-title">Product performance, at a glance.</div>
 <div class="hero-sub">An interactive demonstration of how task engagement, reward movement, wallet activity and operational readiness can be explored. All records are synthetic and are used only to demonstrate visual design and analytical workflows.</div>
</div>
""",unsafe_allow_html=True)
st.warning("DEMO DATA ONLY  ·  These charts are generated synthetic examples, not actual VELOOP performance or production data.")
st.markdown("")

if view=="Executive overview":
    section("01 / BUSINESS SNAPSHOT","Executive overview","A high-level scan of engagement, sample activity and domain mix. Use the sidebar filters to explore the demo.")
    avg_duration=metric_row(filtered)
    c1,c2=st.columns([1.55,1])
    with c1:
        daily=filtered.groupby("date").agg(records=("user_id","size"),completed=("completed_flag","sum")).reset_index()
        daily["completion_rate"]=np.where(daily["records"]>0,daily["completed"]/daily["records"]*100,0)
        fig=go.Figure()
        fig.add_trace(go.Scatter(x=daily.date,y=daily.records,mode="lines",name="Task records",line=dict(color=PALETTE["blue"],width=2.5),fill="tozeroy",fillcolor="rgba(70,119,200,.09)"))
        fig.add_trace(go.Scatter(x=daily.date,y=daily.completed,mode="lines",name="Completed",line=dict(color=PALETTE["teal"],width=2.5)))
        fig.update_layout(title="Activity trend · daily volume",xaxis_title=None,yaxis_title="Records",hovermode="x unified")
        st.plotly_chart(polish(fig,360,True),use_container_width=True)
    with c2:
        mix=filtered.domain.value_counts().rename_axis("Domain").reset_index(name="Records")
        fig=px.pie(mix,names="Domain",values="Records",hole=.68,color="Domain",color_discrete_sequence=[PALETTE["teal"],PALETTE["blue"],PALETTE["violet"],PALETTE["amber"],"#98a2b3"])
        fig.update_traces(textposition="inside",textinfo="percent",hovertemplate="%{label}<br>%{value:,} records<extra></extra>")
        fig.add_annotation(text=f"<b>{len(filtered):,}</b><br><span style='font-size:11px'>records</span>",x=.5,y=.5,showarrow=False,font=dict(size=20,color="#182230"))
        fig.update_layout(title="Activity mix by domain")
        st.plotly_chart(polish(fig,360),use_container_width=True)
    c3,c4=st.columns(2)
    with c3:
        status=filtered.status.value_counts().rename_axis("Status").reset_index(name="Records")
        fig=px.bar(status,x="Records",y="Status",orientation="h",color="Status",color_discrete_map=STATUS_COLORS)
        fig.update_layout(title="Task lifecycle distribution",yaxis={"categoryorder":"total ascending"},xaxis_title="Records",yaxis_title=None)
        st.plotly_chart(polish(fig,330),use_container_width=True)
    with c4:
        domain_summary=filtered.groupby("domain").agg(records=("user_id","size"),completion_rate=("completed_flag","mean"),unique_users=("user_id","nunique")).reset_index()
        domain_summary["completion_rate"]*=100
        fig=px.scatter(domain_summary,x="records",y="completion_rate",size="unique_users",color="domain",text="domain",
                       color_discrete_sequence=[PALETTE["teal"],PALETTE["blue"],PALETTE["violet"],PALETTE["amber"],"#98a2b3"],
                       labels={"records":"Task records","completion_rate":"Completion rate (%)","domain":"Domain","unique_users":"Distinct users"})
        fig.update_traces(textposition="top center",marker=dict(opacity=.82,line=dict(width=1,color="#ffffff")))
        fig.update_layout(title="Domain comparison · volume vs completion",showlegend=False)
        st.plotly_chart(polish(fig,330),use_container_width=True)
    st.markdown('<div class="insight"><b>How to read this:</b> Compare volume with completion rate rather than ranking domains by volume alone. In a production dashboard, confirm eligible-task definitions, deduplication and final task states before interpreting these metrics.</div>',unsafe_allow_html=True)
    with st.expander("Inspect filtered demo records"):
        st.caption("Exports and preview contain synthetic sample records only.")
        st.dataframe(filtered.sort_values("date",ascending=False),hide_index=True,use_container_width=True)
        st.download_button("Export visible task records (CSV)",data=filtered.to_csv(index=False).encode("utf-8"),file_name="velop_visible_task_records.csv",mime="text/csv",disabled=filtered.empty)

elif view=="Engagement & tasks":
    section("02 / ENGAGEMENT","Engagement & tasks","Explore when sample activity occurs, which domains are active, and how lifecycle statuses differ.")
    metric_row(filtered)
    c1,c2=st.columns(2)
    with c1:
        daily=filtered.groupby("date").agg(Started=("status",lambda x:(x=="Started").sum()),Completed=("completed_flag","sum"),Validated=("status",lambda x:(x=="Validated").sum())).reset_index()
        fig=px.area(daily,x="date",y=["Started","Completed","Validated"],title="Lifecycle activity over time",color_discrete_sequence=[PALETTE["blue"],PALETTE["teal"],PALETTE["violet"]])
        fig.update_layout(xaxis_title=None,yaxis_title="Records",legend_title=None)
        st.plotly_chart(polish(fig,360,True),use_container_width=True)
    with c2:
        heat=filtered.pivot_table(index=filtered.date.dt.day_name(),columns="domain",values="user_id",aggfunc="count",fill_value=0)
        order=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        heat=heat.reindex([x for x in order if x in heat.index])
        fig=px.imshow(heat,text_auto=True,aspect="auto",color_continuous_scale=["#edf7f7","#087e8b"],labels=dict(x="Domain",y="Day of week",color="Records"),title="Activity heatmap · day × domain")
        st.plotly_chart(polish(fig,360),use_container_width=True)
    c3,c4=st.columns(2)
    with c3:
        fig=px.box(filtered,x="domain",y="duration_min",color="domain",points=False,color_discrete_sequence=[PALETTE["teal"],PALETTE["blue"],PALETTE["violet"],PALETTE["amber"],"#98a2b3"],title="Task duration distribution")
        fig.update_layout(xaxis_title=None,yaxis_title="Minutes",showlegend=False)
        st.plotly_chart(polish(fig,330),use_container_width=True)
    with c4:
        funnel=pd.DataFrame({"Stage":["Started","Validated","Completed"],"Records":[int(filtered.status.eq("Started").sum()),int(filtered.status.eq("Validated").sum()),int(filtered.completed_flag.sum())]})
        fig=go.Figure(go.Funnel(y=funnel.Stage,x=funnel.Records,textinfo="value+percent initial",marker=dict(color=[PALETTE["blue"],PALETTE["violet"],PALETTE["teal"]]),connector={"line":{"color":"#d0d5dd","width":1}}))
        fig.update_layout(title="Illustrative lifecycle stage counts")
        st.plotly_chart(polish(fig,330),use_container_width=True)
    st.caption("The lifecycle chart shows status counts, not a validated user-level conversion funnel. Production funnel stages need event-level identities and sequential timestamps.")

elif view=="Rewards & wallet":
    section("03 / REWARD ECONOMY","Rewards & wallet","Separate reward states, reward units and wallet movements to avoid misleading aggregation.")
    a,b,c=st.columns(3)
    a.metric("Reward sample records",f"{len(rewards):,}")
    b.metric("Wallet sample movements",f"{len(wallet):,}")
    c.metric("Reward units",f"{rewards.unit.nunique()}")
    r1,r2=st.columns(2)
    with r1:
        by_status=rewards.type.value_counts().rename_axis("State").reset_index(name="Records")
        fig=px.bar(by_status,x="State",y="Records",color="State",color_discrete_map=STATUS_COLORS,title="Reward records by state")
        st.plotly_chart(polish(fig,350),use_container_width=True)
    with r2:
        by_unit=rewards.groupby("unit",as_index=False).agg(records=("amount","size"),sample_amount=("amount","sum"))
        fig=px.bar(by_unit,x="unit",y="records",color="unit",color_discrete_sequence=[PALETTE["teal"],PALETTE["blue"],PALETTE["violet"]],title="Records by reward unit")
        fig.update_layout(xaxis_title=None,yaxis_title="Records",showlegend=False)
        st.plotly_chart(polish(fig,350),use_container_width=True)
    daily=rewards.groupby([rewards.date.dt.date,"type"]).size().reset_index(name="records").rename(columns={"date":"day"})
    fig=px.area(daily,x="day",y="records",color="type",title="Reward state activity · daily",color_discrete_map=STATUS_COLORS)
    st.plotly_chart(polish(fig,330,True),use_container_width=True)
    st.dataframe(by_unit.rename(columns={"unit":"Reward unit","records":"Sample records","sample_amount":"Illustrative amount total"}),hide_index=True,use_container_width=True)
    st.warning("VE, XP and Gems are different units and must not be added together. Amounts are synthetic and are not a verified financial ledger.")

elif view=="Withdrawals & referrals":
    section("04 / OPERATIONS","Withdrawals & referrals","Illustrative operational monitoring patterns for status mix, processing time and referral lifecycle.")
    a,b,c=st.columns(3)
    a.metric("Withdrawal samples",f"{len(withdrawals):,}")
    b.metric("Referral samples",f"{len(referrals):,}")
    c.metric("Median processing time",f"{withdrawals.processing_hours.median():.1f} h")
    c1,c2=st.columns(2)
    with c1:
        w=withdrawals.status.value_counts().rename_axis("Status").reset_index(name="Records")
        fig=px.bar(w,x="Status",y="Records",color="Status",color_discrete_map=STATUS_COLORS,title="Withdrawal status distribution")
        st.plotly_chart(polish(fig,350),use_container_width=True)
    with c2:
        r=referrals.stage.value_counts().rename_axis("Stage").reset_index(name="Records")
        fig=go.Figure(go.Funnel(y=r.Stage,x=r.Records,textinfo="value+percent initial",marker=dict(color=[PALETTE["blue"],PALETTE["teal"],PALETTE["green"],PALETTE["amber"]])))
        fig.update_layout(title="Referral stage distribution")
        st.plotly_chart(polish(fig,350),use_container_width=True)
    fig=px.histogram(withdrawals,x="processing_hours",color="status",nbins=24,barmode="overlay",opacity=.78,color_discrete_map=STATUS_COLORS,title="Withdrawal processing-time distribution")
    fig.update_layout(xaxis_title="Illustrative hours",yaxis_title="Requests",legend_title=None)
    st.plotly_chart(polish(fig,350,True),use_container_width=True)
    st.caption("Production SLA reporting requires authoritative request, completion and failure timestamps plus approved business-hour rules.")

else:
    section("05 / TRUST & READINESS","Data readiness","A senior-style view of what can be measured now, what remains unverified, and what must be approved before production reporting.")
    c1,c2,c3=st.columns(3)
    c1.metric("Demo domains", "5")
    c2.metric("Production sources connected", "0")
    c3.metric("Metric status", "Proposed")
    gaps=pd.DataFrame([
        ["User/account","Simulated Task 01 sample available","Profile completeness, duplicate and valid-value checks","Medium"],
        ["Task lifecycle","No production extract supplied","Confirm eligible population, stable task ID and final status","High"],
        ["Rewards ledger","Synthetic sample only","Approve units, reversal rules and immutable ledger","High"],
        ["Wallet","Synthetic sample only","Reconcile credits, debits, reversals and balances","High"],
        ["Withdrawals","Synthetic sample only","Confirm state machine, timestamps and SLA clock","High"],
        ["Referrals","Synthetic sample only","Define registration, activation and qualified conversion","High"],
        ["Product events","Synthetic sample only","Approve event taxonomy, user/session IDs and timezone","High"],
        ["Privacy & retention","Design recommendation only","Confirm access roles, minimisation and retention policy","High"],
    ],columns=["Data domain","Evidence available","Validation needed","Priority"])
    st.dataframe(gaps,hide_index=True,use_container_width=True)
    c1,c2=st.columns(2)
    with c1:
        fig=px.bar(gaps.groupby("Priority").size().reset_index(name="Domains"),x="Priority",y="Domains",color="Priority",color_discrete_map={"High":PALETTE["red"],"Medium":PALETTE["amber"]},title="Readiness actions by priority")
        st.plotly_chart(polish(fig,320),use_container_width=True)
    with c2:
        fig=go.Figure(go.Pie(labels=["Production-connected","Synthetic / unverified"],values=[0,100],hole=.72,marker_colors=[PALETTE["teal"],"#d0d5dd"],textinfo="none",hoverinfo="label+percent"))
        fig.add_annotation(text="<b>0%</b><br><span style='font-size:11px'>production connected</span>",x=.5,y=.5,showarrow=False,font=dict(size=20,color="#182230"))
        fig.update_layout(title="Production data connectivity")
        st.plotly_chart(polish(fig,320),use_container_width=True)
    st.markdown('<div class="insight"><b>Decision gate:</b> treat these pages as a visual prototype until source access, metric definitions, ownership and reconciliation checks are approved. Do not use synthetic counts for operational decisions.</div>',unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div class="mini-note">VELOOP Task 01 · Visual prototype for review · Synthetic data only · No production connection configured</div>',unsafe_allow_html=True)
