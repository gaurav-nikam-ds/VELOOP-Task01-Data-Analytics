"use client";

import { useMemo, useState } from "react";

const NAV = [
  ["Executive status","Overview"],
  ["Insights & recommendations","Insights"],
  ["Supplied data audit","Audit"],
  ["Deliverable tracker","Deliverables"],
  ["Seven-dashboard blueprint","Blueprint"],
  ["Acceptance blockers","Blockers"],
  ["Implementation library","Library"]
];

const deliverables = [
["Assignment scope and source register","Documented","Confirm approved scope"],
["Executive summary and decision framing","Documented","Owner review"],
["Data coverage matrix","Documented","Validate against source systems"],
["User/account analytics specification","Documented","Confirm identifiers and account states"],
["Earning/reward analytics specification","Documented design","Authoritative reward/task records not supplied"],
["Wallet/withdrawal specification","Documented design","Finance/Operations must confirm ledger semantics"],
["Referral/engagement specification","Documented design","Approve activation and conversion definitions"],
["Event tracking plan","Proposed","Engineering approval and staging validation"],
["Data dictionary (75+ fields)","90 proposed fields","Confirm physical schema and constraints"],
["Logical data model and ERD","Proposed","Not verified against production schema"],
["KPI catalogue (30+ KPIs)","36 proposed KPIs","Approve formulas, units, sources and denominators"],
["Simulated data profiling","Source-limited","Full Task 01 transaction/event pack not supplied"],
["Data quality rules and acceptance gates","Documented proposal","Agree thresholds and exception handling"],
["Dashboard visual specifications","Documented blueprint","Validate with dashboard owners"],
["Data pipeline and refresh plan","Proposed","Confirm source access and SLA"],
["Governance and ownership model","Proposed","Assign accountable owners"],
["Privacy, access and retention considerations","Proposed","Security/Legal review"],
["Data gaps and risk register","Documented","Track owners and due dates"],
["Implementation backlog","Documented proposal","Prioritise with stakeholders"],
["Testing and acceptance checklist","Documented proposal","Run QA and record evidence"],
["Final handoff and recommendations","Prepared for review","Coordinator / stakeholder acceptance"]
];

const dashboardAreas = [
["01","Executive Overview","Approved core KPIs, trends, alerts and definitions","Product / leadership","Production sources and approved KPI definitions"],
["02","User Analytics","Registration, onboarding, account lifecycle and cohorts","Product / growth","Canonical user IDs and lifecycle events"],
["03","Engagement","Active/returning users, task activity and feature usage","Product / analytics","Session/event data and approved activity definition"],
["04","Rewards","Earned, pending, credited, reversed and corrected rewards","Rewards operations / finance","Authoritative reward ledger and reward units"],
["05","Wallet","Ledger credits/debits, balances and reconciliation","Finance / operations","Wallet ledger, transaction IDs and reconciliation rules"],
["06","Withdrawals","Requests, outcomes, failure reasons and processing time","Operations / finance","Payout source of truth, status history and timestamps"],
["07","Referrals","Referral creation, registration, activation and conversion","Growth / product","Referral attribution and approved conversion definition"]
];

const findings = [
{title:"Referral source detail missing",metric:"881 / 1,000 · 88.1%",evidence:"Task 01 workbook · Users_1000_Clean",risk:"Referral attribution analysis may be incomplete or biased if missingness is not understood.",action:"Define required referral fields and distinguish unknown, not collected, not applicable and genuine missing values.",priority:"High"},
{title:"Last-login timestamp missing",metric:"72 / 1,000 · 7.2%",evidence:"Task 01 workbook · Users_1000_Clean",risk:"Last-login activity or recency metrics may undercount or misclassify users.",action:"Confirm the authoritative activity event, timezone, null semantics and update behavior.",priority:"High"},
{title:"Repeated IDs in messy audit tab",metric:"1,008 rows · 8 repeated IDs",evidence:"Task 01 workbook · Users_Messy_Audit",risk:"Naive row counts or joins can double-count users and distort profile-level metrics.",action:"Apply uniqueness tests at the agreed grain and quarantine duplicates with traceable exceptions.",priority:"High"},
{title:"Invalid or missing registration dates",metric:"4 negative tenure values · 1 missing registration timestamp",evidence:"Task 01 workbook · Users_Messy_Audit",risk:"Derived tenure and cohort calculations may be invalid when chronology is impossible.",action:"Recompute tenure from the canonical registration timestamp and flag impossible chronology.",priority:"High"},
{title:"Task 02 event audit has duplicate rows",metric:"35,714 rows · 10 exact duplicate rows",evidence:"Separate Task 02 workbook; not merged into Task 01",risk:"Duplicate events can inflate activity counts if event identity and idempotency rules are not enforced.",action:"Ask the coordinator to confirm Task 02 reuse; if approved, define a unique event key and deduplication test.",priority:"Medium"}
];

const sources = [
["Users_1000_Clean","1,000","27","1,000 unique, non-null user_id values; 0 exact duplicate rows"],
["Users_1000_Clean","1,000","27","881 missing referral_source_detail; 72 missing last_login_datetime"],
["Users_Messy_Audit","1,008","28","1,000 unique IDs; 8 repeated IDs"],
["Users_Messy_Audit","1,008","28","1 missing registration timestamp; 73 missing last-login timestamps"],
["Users_Messy_Audit","1,008","28","885 missing referral details; 4 negative days_since_registration values"]
];

const blockers = [
["Vercel deployment","Verified","The live website is deployed and the project owner has confirmed the live-site checks."],
["Website usability checks","Verified","Navigation, findings filters, CSV downloads, document links and mobile layout have been checked by the project owner."],
["Production data access","External dependency","No authorized production extracts, API credentials or database connection were supplied. This is not a website defect."],
["Task 02 scope approval","External dependency","The behavior workbook identifies itself as Task 02. Keep it separate unless the coordinator approves reuse."],
["KPI and event definitions","External dependency","Product/Engineering must confirm event implementation, canonical identifiers and KPI definitions."],
["Rewards, wallet and withdrawals","External dependency","Finance/Operations must confirm reward units, ledger semantics, withdrawal states and reconciliation rules."]
];

function downloadCSV(filename, rows) {
  const csv = rows.map(row => row.map(value => {
    const text = String(value ?? "");
    return '"' + text.replaceAll('"','""') + '"';
  }).join(",")).join("\r\n");
  const blob = new Blob(["\uFEFF" + csv], {type:"text/csv;charset=utf-8;"});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url; a.download = filename; a.click();
  URL.revokeObjectURL(url);
}

function Metric({label,value,sub}) {
  return <div className="metric"><div className="metric-label">{label}</div><div className="metric-value">{value}</div>{sub && <div className="metric-sub">{sub}</div>}</div>;
}
function Panel({title,subtitle,children,action}) {
  return <section className="panel"><div className="panel-head"><div><h2>{title}</h2>{subtitle && <p>{subtitle}</p>}</div>{action}</div>{children}</section>;
}
function DataTable({headers,rows}) {
  return <div className="table-wrap"><table><thead><tr>{headers.map(h=><th key={h}>{h}</th>)}</tr></thead><tbody>{rows.map((row,i)=><tr key={i}>{row.map((cell,j)=><td key={j}>{cell}</td>)}</tr>)}</tbody></table></div>;
}

export default function Home() {
  const [active,setActive] = useState("Executive status");
  const [query,setQuery] = useState("");
  const [priority,setPriority] = useState("All");
  const filteredFindings = useMemo(()=>findings.filter(f=>(priority==="All"||f.priority===priority)&&[f.title,f.metric,f.risk,f.action].join(" ").toLowerCase().includes(query.toLowerCase())),[priority,query]);
  const exportDeliverables = () => downloadCSV("velop-task01-deliverable-tracker.csv",[["Deliverable","Evidence status","Remaining dependency"],...deliverables]);
  const exportFindings = () => downloadCSV("velop-task01-evidence-findings.csv",[["Finding","Metric","Evidence","Risk","Recommended action","Priority"],...findings.map(f=>[f.title,f.metric,f.evidence,f.risk,f.action,f.priority])]);

  return <div className="shell">
    <aside className="sidebar">
      <div className="brand"><span className="brand-mark">◈</span><span>VELOOP REWARDS</span></div>
      <div className="eyebrow">TASK 01 · ANALYTICS & DECISION SUPPORT</div>
      <div className="side-label">WORKSPACE</div>
      <nav>{NAV.map(([name,short])=><button key={name} className={active===name?"nav-item selected":"nav-item"} onClick={()=>{setActive(name);window.scrollTo({top:0,behavior:"smooth"});}}><span className="nav-dot"/>{name}</button>)}</nav>
      <div className="side-note">Evidence basis: supplied Task 01 PDF, Task 01 workbook, separate Task 02 workbook and assignment email.</div>
      <a className="side-link" href="https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics" target="_blank" rel="noreferrer">Open GitHub repository ↗</a>
      <a className="side-link" href="https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/tree/main/docs" target="_blank" rel="noreferrer">Browse documentation ↗</a>
      <div className="side-footer">Evidence-based analysis<br/>No production system connected</div>
    </aside>
    <main className="main">
      <header className="hero"><div className="hero-top"><span className="pill">TASK 01 · REVIEW WORKSPACE</span><span className="live-dot">SOURCE-GROUNDED</span></div><h1>VELOOP Rewards — Product Analytics & Data Readiness</h1><p>Evidence-based findings, business questions, recommended actions and implementation dependencies from the supplied assignment materials.</p></header>
      <div className="notice"><strong>DATA LIMITATION</strong> The supplied assignment data is simulated. No authorized production extract or production-system connection was supplied. Findings describe the supplied workbooks only, not actual VELOOP users or business performance.</div>
      <div className="content">
      {active==="Executive status" && <>
        <div className="page-title"><div><span className="eyebrow">WORKSPACE OVERVIEW</span><h2>Current submission status</h2></div><span className="status-chip">Prototype · Review pending</span></div>
        <div className="metrics-grid"><Metric label="Tracked assignment deliverables" value="21" sub="Evidence and dependencies recorded"/><Metric label="Proposed KPIs" value="36" sub="Require owner approval"/><Metric label="Proposed data fields" value="90" sub="Logical design, not production schema"/><Metric label="Production data connections" value="0" sub="No live company data supplied"/></div>
        <Panel title="Start here: how to read this workspace" subtitle="A quick guide before exploring the details"><ul className="evidence-list"><li><b>Insights & recommendations:</b> what the supplied files show, why it matters and what to do next.</li><li><b>Supplied data audit:</b> counts and quality issues found in the assignment workbooks.</li><li><b>Deliverable tracker:</b> what has been documented and what still depends on approval or missing data.</li><li><b>Seven-dashboard blueprint:</b> a proposed design for future dashboards—not seven live production dashboards.</li><li><b>Acceptance blockers:</b> remaining business dependencies that cannot be resolved from the supplied files alone.</li><li><b>Implementation library:</b> detailed technical documents for reviewers and developers.</li></ul></Panel>
        <Panel title="What the evidence supports" subtitle="Conclusions grounded in the supplied assignment files"><ul className="evidence-list"><li>The assignment is a product-analytics and data-readiness blueprint.</li><li>The Task 01 workbook includes clean and messy user-profile tabs plus dictionary/summary tabs.</li><li>The separate behavior workbook labels itself Task 02 and remains separate pending coordinator approval.</li><li>Reward, wallet, withdrawal and referral business performance cannot be measured from the supplied Task 01 user-profile tabs alone.</li></ul></Panel>
        <div className="decision-callout"><b>Decision rule</b><p>Improve data reliability and confirm authoritative business sources before calculating or interpreting production KPIs. Do not publish simulated figures as actual VELOOP performance.</p></div>
        <Panel title="Readiness at a glance" subtitle="Items that still need evidence or owner confirmation"><DataTable headers={["Gate","Status","Required next step"]} rows={blockers.slice(0,5)}/><div className="panel-actions"><button className="button secondary" onClick={()=>setActive("Acceptance blockers")}>Review all blockers →</button></div></Panel>
      </>}
      {active==="Insights & recommendations" && <>
        <div className="page-title"><div><span className="eyebrow">EVIDENCE-BASED FINDINGS</span><h2>What did the supplied data show?</h2><p className="lead">Each finding includes the evidence, why it matters and a recommended next step. These are simulated assignment-data findings—not actual VELOOP business results.</p></div></div>
        <div className="filter-row"><input aria-label="Search findings" value={query} onChange={e=>setQuery(e.target.value)} placeholder="Search findings, risks or actions…"/><select aria-label="Filter by priority" value={priority} onChange={e=>setPriority(e.target.value)}><option>All</option><option>High</option><option>Medium</option></select><button className="button secondary" onClick={exportFindings}>Export findings CSV ↓</button></div>
        <div className="finding-grid">{filteredFindings.map((f,i)=><article className="finding-card" key={f.title}><div className="finding-top"><span className="finding-index">FINDING {findings.indexOf(f)+1}</span><span className={f.priority==="High"?"priority high":"priority medium"}>{f.priority} priority</span></div><h3>{f.title}</h3><div className="finding-metric">{f.metric}</div><div className="evidence-tag">{f.evidence}</div><div className="finding-section"><b>Business risk / limitation</b><p>{f.risk}</p></div><div className="finding-section"><b>Recommended action</b><p>{f.action}</p></div></article>)}</div>
      </>}
      {active==="Supplied data audit" && <>
        <div className="page-title"><div><span className="eyebrow">SOURCE QUALITY</span><h2>What is in the supplied files?</h2><p className="lead">These counts and issues come from the simulated assignment workbooks. Task 02 is shown separately and is not combined with Task 01.</p></div></div>
        <div className="metrics-grid"><Metric label="Clean user profiles" value="1,000"/><Metric label="Clean-sheet columns" value="27"/><Metric label="Messy audit rows" value="1,008"/><Metric label="Repeated IDs in messy tab" value="8"/></div>
        <Panel title="Task 01 source workbook" subtitle="Workbook-level profile and quality findings"><DataTable headers={["Source sheet","Rows","Columns","Finding"]} rows={sources}/></Panel>
        <Panel title="Separate Task 02 workbook — not merged" subtitle="Shown only as a separate source audit"><DataTable headers={["Dataset","Rows","Audited finding"]} rows={[["Sessions","7,913","984 distinct user IDs; no orphan user IDs against Task 02 profiles"],["Primary feature events","35,704","35,704 unique event IDs; date range 2026-04-02 to 2026-09-15; no user ID orphans"],["Event audit","35,714","10 exact duplicate rows"],["Daily activity","6,667","Task 02 workbook summary; not treated as Task 01 source"]]}/></Panel>
        <div className="decision-callout"><b>Interpretation guardrail</b><p>Task 02 data must not be merged into Task 01 analysis without coordinator approval. Source-level counts do not establish production-system correctness.</p></div>
      </>}
      {active==="Deliverable tracker" && <>
        <div className="page-title"><div><span className="eyebrow">ASSIGNMENT CHECKLIST</span><h2>Required deliverables and what remains</h2><p className="lead">“Documented” means included in the handoff; it does not mean the company has approved or implemented it.</p></div><button className="button primary" onClick={exportDeliverables}>Export deliverable tracker ↓</button></div>
        <div className="metrics-grid compact"><Metric label="Tracked deliverables" value="21"/><Metric label="Proposed KPIs" value="36"/><Metric label="Dictionary fields" value="90"/></div>
        <DataTable headers={["#","Deliverable","Evidence status","Remaining dependency"]} rows={deliverables.map((d,i)=>[String(i+1).padStart(2,"0"),d[0],<span className="status-text" key={d[0]}>{d[1]}</span>,d[2]])}/>
      </>}
      {active==="Seven-dashboard blueprint" && <>
        <div className="page-title"><div><span className="eyebrow">PROPOSED DESIGN</span><h2>Seven dashboards the business could use</h2><p className="lead">Open each item to see its purpose, intended stakeholder and the data/approval needed. These dashboards are specified, not connected to live company data.</p></div></div>
        <div className="blueprint-list">{dashboardAreas.map(d=><details className="blueprint-card" key={d[0]}><summary><span className="blueprint-number">{d[0]}</span><span>{d[1]}</span><span className="summary-arrow">+</span></summary><div className="blueprint-detail"><div><b>Business measures</b><p>{d[2]}</p></div><div><b>Primary stakeholder</b><p>{d[3]}</p></div><div><b>Source / approval dependency</b><p>{d[4]}</p></div><div className="blueprint-status">Specification status: Blueprint only; formulas, dimensions, filters, date range and refresh rules require owner validation.</div></div></details>)}</div>
      </>}
      {active==="Acceptance blockers" && <>
        <div className="page-title"><div><span className="eyebrow">STATUS & DEPENDENCIES</span><h2>What is done—and what still needs others</h2><p className="lead">Website checks are complete. Remaining items require company data or decisions from the coordinator and business owners.</p></div></div>
        <Panel title="Remaining dependencies" subtitle="These are external business/data requirements, not unfinished website features"><DataTable headers={["Gate","Status","Evidence / next action"]} rows={blockers.map(b=>[b[0],<span className={b[1]==="External dependency"?"dependency-chip":b[1]==="Verified"?"verified-chip":"status-chip"} key={b[0]}>{b[1]}</span>,b[2]])}/></Panel>
        <div className="decision-callout"><b>Acceptance rule</b><p>Do not replace missing company facts with invented transaction data. Production readiness requires approved data, owner definitions and validation evidence.</p></div>
      </>}
      {active==="Implementation library" && <>
        <div className="page-title"><div><span className="eyebrow">DETAILS FOR REVIEWERS</span><h2>Technical documents and handoff files</h2><p className="lead">Start with the source audit for evidence, the requirements checklist for coverage, or the developer handoff for implementation details.</p></div></div>
        <div className="library-grid">{[
["Source data profile & quality audit","Evidence-backed row/column counts, missingness, duplicate IDs and quality rules.","SOURCE_DATA_PROFILE_AND_QUALITY_AUDIT.md"],
["Data dictionary field index","90-field logical inventory, metadata contract, sensitivity and validation rules.","DATA_DICTIONARY_FIELD_INDEX.md"],
["Developer analytics handoff","Event envelope, lifecycle events, ledger/state rules and acceptance tests.","DEVELOPER_ANALYTICS_HANDOFF.md"],
["Seven-dashboard visual specifications","Visual-level measures, sources, filters, questions and decisions.","DASHBOARD_VISUAL_SPECIFICATIONS.md"],
["Analytics change log & operating model","Ownership, review workflow, monitoring, incident response and release acceptance.","ANALYTICS_CHANGE_LOG_AND_OPERATING_MODEL.md"],
["Analytics foundation implementation pack","Product map, event contract, logical model, quality controls, KPI catalogue, governance and backlog.","ANALYTICS_FOUNDATION_IMPLEMENTATION_PACK.md"],
["Requirements-to-evidence checklist","Traceability across the 21 assignment deliverables and acceptance blockers.","TASK01_REQUIREMENTS_CHECKLIST.md"],
["Three-source-file audit","Source scope, data limitations and Task 02 separation guardrail.","THREE_SOURCE_FILES_AUDIT.md"]
].map(doc=><a className="library-card" key={doc[2]} href={"https://github.com/gaurav-nikam-ds/VELOOP-Task01-Data-Analytics/blob/main/docs/"+doc[2]} target="_blank" rel="noreferrer"><span className="file-icon">DOC</span><div><h3>{doc[0]}</h3><p>{doc[1]}</p><span className="open-link">Open document ↗</span></div></a>)}</div>
        <Panel title="Minimum event contract" subtitle="Proposed contract — not production instrumentation"><DataTable headers={["Field","Requirement"]} rows={[["event_id","Unique event identity; deduplicate safely"],["event_name / event_version","Approved event name and versioned schema"],["event_timestamp / received_timestamp","Occurrence time and ingestion time kept separate"],["user_id / session_id","Stable identifiers under approved anonymous-event rules"],["transaction_id / attempt_id","Business transaction and retry identities where applicable"],["source_system / status / properties","Producer, approved state and allow-listed properties"],["idempotency_key / correlation_id","Retry safety and workflow traceability"]]}/></Panel>
      </>}
      <footer className="footer">VELOOP Rewards · Task 01 · Evidence-based analysis and decision support <span>· No production system connected</span></footer>
      </div>
    </main>
  </div>;
}
