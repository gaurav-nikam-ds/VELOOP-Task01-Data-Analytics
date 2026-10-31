"""Profile the QA-checked supplemental synthetic analytics workbook.

Usage:
python analytics/python/analyze_synthetic_pack.py --input SIMULATED_Analytics_Test_Data.xlsx --users VELoop_Rewards_Data_01.xlsx --output-dir outputs

All added records are synthetic test data, not VELOOP production records.
Only aggregate evidence is exported; names and email addresses are excluded.
"""
import argparse, json, sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

SHEETS = {
    "Task_Activity": ("activity_id", ["task_viewed_at", "task_started_at", "task_completed_at"], "task_status"),
    "Rewards": ("reward_id", ["created_at"], "reward_status"),
    "Wallet": ("transaction_id", ["transaction_timestamp"], "status"),
    "Withdrawals": ("withdrawal_id", ["requested_at", "processing_at", "final_at"], "status"),
    "Referrals": ("referral_id", ["created_at", "registered_at", "activated_at"], "status"),
    "Feature_Events": ("event_id", ["event_timestamp"], "event_status"),
    "Messy_Data": ("activity_id", ["task_viewed_at", "task_started_at", "task_completed_at"], "task_status"),
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="QA-checked supplemental synthetic workbook")
    parser.add_argument("--users", required=True, help="Task 01 source workbook for user-ID checks")
    parser.add_argument("--output-dir", default="outputs")
    args = parser.parse_args()
    out = Path(args.output_dir)
    charts = out / "charts"
    out.mkdir(parents=True, exist_ok=True)
    charts.mkdir(parents=True, exist_ok=True)

    users = pd.read_excel(args.users, sheet_name="Users_1000_Clean")
    user_ids = set(users["user_id"].dropna().astype(str))
    frames = {name: pd.read_excel(args.input, sheet_name=name, header=1) for name in SHEETS}
    external = pd.read_excel(args.input, sheet_name="External_References", header=1)

    profiles, statuses, quality, relationships = [], [], [], []
    date_ranges = {}
    for name, df in frames.items():
        pk, date_cols, status_col = SHEETS[name]
        row = {"dataset": name, "rows": len(df), "columns": len(df.columns),
               "missing_cells": int(df.isna().sum().sum()), "primary_key": pk,
               "null_primary_keys": int(df[pk].isna().sum()),
               "duplicate_primary_key_extra_rows": int(df[pk].dropna().duplicated().sum()),
               "exact_duplicate_rows": int(df.duplicated().sum())}
        for col in date_cols:
            parsed = pd.to_datetime(df[col], errors="coerce")
            nonblank = df[col].notna() & df[col].astype(str).str.strip().ne("")
            row[col + "_invalid_nonblank"] = int((nonblank & parsed.isna()).sum())
            if parsed.notna().any():
                date_ranges[name + "." + col] = [str(parsed.min()), str(parsed.max())]
        profiles.append(row)
        for status, count in df[status_col].fillna("(Missing)").astype(str).value_counts().items():
            statuses.append({"dataset": name, "status_field": status_col, "status": status, "records": int(count)})
        quality.extend([
            {"check": f"{name}: null primary keys", "records_affected": row["null_primary_keys"], "interpretation": "Primary-key completeness"},
            {"check": f"{name}: duplicate primary keys beyond first", "records_affected": row["duplicate_primary_key_extra_rows"], "interpretation": "Primary-key uniqueness"},
            {"check": f"{name}: exact duplicate rows", "records_affected": row["exact_duplicate_rows"], "interpretation": "Exact-row duplication"},
        ])

    def fk(label, df, col, valid):
        values = df[col].dropna().astype(str)
        missing = int(df[col].isna().sum())
        unmatched = int((~values.isin(valid)).sum())
        relationships.append({"relationship": label, "child_rows": len(df), "nonnull_values": len(values),
                              "null_values": missing, "unmatched_nonnull_values": unmatched,
                              "result": "PASS" if unmatched == 0 else "REVIEW"})

    fk("Task_Activity.user_id -> Task01 Users.user_id", frames["Task_Activity"], "user_id", user_ids)
    fk("Rewards.user_id -> Task01 Users.user_id", frames["Rewards"], "user_id", user_ids)
    fk("Wallet.user_id -> Task01 Users.user_id", frames["Wallet"], "user_id", user_ids)
    fk("Withdrawals.user_id -> Task01 Users.user_id", frames["Withdrawals"], "user_id", user_ids)
    fk("Feature_Events.user_id -> Task01 Users.user_id", frames["Feature_Events"], "user_id", user_ids)
    fk("Referrals.referrer_user_id -> Task01 Users.user_id", frames["Referrals"], "referrer_user_id", user_ids)
    fk("Referrals.referred_user_id -> Task01 Users.user_id", frames["Referrals"], "referred_user_id", user_ids)
    fk("Rewards.source_activity_id -> Task_Activity.activity_id", frames["Rewards"], "source_activity_id", set(frames["Task_Activity"].activity_id.astype(str)))
    fk("Rewards.correction_of_reward_id -> Rewards.reward_id", frames["Rewards"], "correction_of_reward_id", set(frames["Rewards"].reward_id.astype(str)))
    fk("Wallet.reversal_of_transaction_id -> Wallet.transaction_id", frames["Wallet"], "reversal_of_transaction_id", set(frames["Wallet"].transaction_id.astype(str)))

    known_refs = (set(frames["Rewards"].reward_id.astype(str)) |
                  set(frames["Withdrawals"].withdrawal_id.astype(str)) |
                  set(external.reference_id.astype(str)))
    fk("Wallet.reference_id -> known domain/external references (polymorphic)", frames["Wallet"], "reference_id", known_refs)
    self_ref = int((frames["Referrals"].referrer_user_id == frames["Referrals"].referred_user_id).sum())
    relationships.append({"relationship":"Referrals.referrer_user_id != referred_user_id", "child_rows":len(frames["Referrals"]),
                          "nonnull_values":len(frames["Referrals"]), "null_values":0,
                          "unmatched_nonnull_values":self_ref, "result":"REVIEW" if self_ref else "PASS"})

    task, wd, ref, messy = frames["Task_Activity"], frames["Withdrawals"], frames["Referrals"], frames["Messy_Data"]
    task_start = pd.to_datetime(task.task_started_at, errors="coerce")
    task_done = pd.to_datetime(task.task_completed_at, errors="coerce")
    proc = pd.to_datetime(wd.processing_at, errors="coerce")
    final = pd.to_datetime(wd.final_at, errors="coerce")
    registered = pd.to_datetime(ref.registered_at, errors="coerce")
    activated = pd.to_datetime(ref.activated_at, errors="coerce")
    viewed = pd.to_datetime(messy.task_viewed_at, errors="coerce")
    valid_status = {"pending", "completed", "abandoned", "validation_failed", "failed"}
    checks = [
        ("Task_Activity completion before start", int((task_done < task_start).sum()), "Chronology after QA correction; expected 0"),
        ("Withdrawals final before processing", int((final < proc).sum()), "Chronology after QA correction; expected 0"),
        ("Referrals activation before registration", int((activated < registered).sum()), "Chronology; expected 0"),
        ("Messy_Data null activity_id", int(messy.activity_id.isna().sum()), "Injected test defect"),
        ("Messy_Data duplicate non-null activity_id rows beyond first", int(messy.activity_id.dropna().duplicated().sum()), "Injected test defect"),
        ("Messy_Data malformed nonblank task_viewed_at", int((messy.task_viewed_at.notna() & viewed.isna()).sum()), "Injected test defect"),
        ("Messy_Data invalid task_status", int((~messy.task_status.isin(valid_status)).sum()), "Injected test defect"),
        ("Messy_Data whitespace-only failure_reason", int(messy.failure_reason.dropna().astype(str).str.fullmatch(r"\\s+").sum()), "Injected test defect"),
        ("Messy_Data negative numeric reward_status", int(pd.to_numeric(messy.reward_status, errors="coerce").lt(0).sum()), "Injected type/value defect"),
    ]
    for label, count, note in checks:
        quality.append({"check":label, "records_affected":count, "interpretation":note})

    profiles_df = pd.DataFrame(profiles)
    status_df = pd.DataFrame(statuses)
    quality_df = pd.DataFrame(quality)
    rel_df = pd.DataFrame(relationships)
    profiles_df.to_csv(out/"synthetic_dataset_profile.csv", index=False)
    status_df.to_csv(out/"synthetic_status_distribution.csv", index=False)
    quality_df.to_csv(out/"synthetic_quality_checks.csv", index=False)
    rel_df.to_csv(out/"synthetic_relationship_checks.csv", index=False)

    task_completed = int((task.task_status == "completed").sum())
    kpi = {
        "synthetic_notice":"SIMULATED DATA — CREATED FOR ANALYTICAL TESTING",
        "task_activity_rows":len(task),
        "task_started_rows":int(task.task_started_at.notna().sum()),
        "task_completed_status_rows":task_completed,
        "task_completed_status_share_pct":round(task_completed / max(int(task.task_started_at.notna().sum()), 1) * 100, 2),
        "reward_status_counts":frames["Rewards"].reward_status.value_counts().to_dict(),
        "wallet_status_counts":frames["Wallet"].status.value_counts().to_dict(),
        "withdrawal_status_counts":frames["Withdrawals"].status.value_counts().to_dict(),
        "referral_status_counts":frames["Referrals"].status.value_counts().to_dict(),
        "feature_event_status_counts":frames["Feature_Events"].event_status.value_counts().to_dict(),
        "interpretation":"Descriptive synthetic test outputs only; not production rates or targets. Keep reward units separate; pending/open states affect denominators."
    }
    (out/"synthetic_kpi_feasibility.json").write_text(json.dumps(kpi, indent=2), encoding="utf-8")

    summary = {
        "data_notice":"SIMULATED DATA — CREATED FOR ANALYTICAL TESTING",
        "source_workbook":"QA-checked supplemental synthetic test workbook",
        "generation_method":"Deterministic synthetic test data; user IDs sampled from Task 01 clean users; Task 02 workbook excluded.",
        "tables":{r["dataset"]:{"rows":int(r["rows"]),"columns":int(r["columns"])} for r in profiles if r["dataset"]!="Messy_Data"},
        "messy_data":{"rows":len(messy),"null_activity_ids":int(messy.activity_id.isna().sum()),
                      "duplicate_nonnull_activity_id_extra_rows":int(messy.activity_id.dropna().duplicated().sum())},
        "relationship_review_flags":{"unmatched_wallet_reference_ids":int((~frames["Wallet"].reference_id.astype(str).isin(known_refs)).sum()),
                                     "self_referral_rows":self_ref},
        "quality_checks":{label:count for label,count,_ in checks},
        "date_ranges":date_ranges,
        "limitations":"Synthetic logic testing only. One self-referral and unmatched polymorphic wallet references remain review items."
    }
    (out/"synthetic_test_pack_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    # Local SQLite only. Names and email addresses are excluded from the user table.
    with sqlite3.connect(out/"synthetic_test_pack.sqlite") as con:
        users = users.drop(columns=["full_name","email"], errors="ignore")
        users.to_sql("task01_users_clean", con, if_exists="replace", index=False)
        for name, df in frames.items():
            df.to_sql(name.lower(), con, if_exists="replace", index=False)
        external.to_sql("external_references", con, if_exists="replace", index=False)

    chart_df = profiles_df[profiles_df.dataset.isin(list(SHEETS))].sort_values("rows")
    plt.figure(figsize=(9,5))
    plt.barh(chart_df.dataset, chart_df.rows)
    plt.title("Supplemental synthetic test pack — record counts")
    plt.xlabel("Records"); plt.ylabel("Dataset"); plt.tight_layout()
    plt.savefig(charts/"synthetic_dataset_record_counts.svg", format="svg")
    plt.close()
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
