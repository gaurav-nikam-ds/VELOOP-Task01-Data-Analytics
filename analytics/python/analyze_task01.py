"""Reproducible profiling for the VELOOP Task 01 simulated user workbook.
Usage: python analyze_task01.py --input /path/to/workbook.xlsx --output-dir outputs
Only aggregate outputs are exported; names and emails are never exported.
"""
import argparse, json, sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True)
    p.add_argument("--output-dir",default="outputs")
    a=p.parse_args()
    out=Path(a.output_dir); charts=out/"charts"
    out.mkdir(parents=True,exist_ok=True); charts.mkdir(parents=True,exist_ok=True)
    clean=pd.read_excel(a.input,sheet_name="Users_1000_Clean")
    messy=pd.read_excel(a.input,sheet_name="Users_Messy_Audit")
    missing=clean.isna().sum().sort_values(ascending=False)
    mt=pd.DataFrame({"column":missing.index,"missing_count":missing.values,
                     "missing_pct":(missing/len(clean)*100).round(2).values})
    mt.to_csv(out/"clean_sheet_missingness.csv",index=False)
    num=lambda c: pd.to_numeric(clean[c],errors="coerce")
    s={"data_notice":"SIMULATED ASSIGNMENT DATA — NOT ACTUAL VELOOP PRODUCTION DATA",
       "source_sheet":"Users_1000_Clean","rows":int(len(clean)),"columns":int(len(clean.columns)),
       "distinct_user_ids":int(clean.user_id.nunique(dropna=True)),
       "null_user_id_rows":int(clean.user_id.isna().sum()),
       "duplicate_user_id_extra_rows":int(clean.user_id.duplicated().sum()),
       "total_missing_cells":int(clean.isna().sum().sum()),
       "missing_cell_rate_pct":round(float(clean.isna().sum().sum()/(clean.shape[0]*clean.shape[1])*100),2),
       "missing_referral_source_detail":int(clean.referral_source_detail.isna().sum()),
       "missing_last_login_datetime":int(clean.last_login_datetime.isna().sum()),
       "age_min":float(num("age").min()),"age_max":float(num("age").max()),
       "median_lifetime_sessions":float(num("lifetime_sessions").median()),
       "median_active_days":float(num("active_days").median()),
       "negative_days_since_registration":int((num("days_since_registration")<0).sum()),
       "messy_sheet_rows":int(len(messy)),
       "messy_sheet_distinct_user_ids":int(messy.user_id.nunique(dropna=True)),
       "messy_sheet_duplicate_user_id_extra_rows":int(messy.user_id.duplicated().sum()),
       "messy_sheet_null_registration_datetime":int(messy.registration_datetime.isna().sum()),
       "method_note":"Missing last-login may be legitimate for users who have not logged in. Duplicate extra rows count repeats after the first occurrence."}
    (out/"quality_summary.json").write_text(json.dumps(s,indent=2),encoding="utf-8")
    for c in ["account_status","email_verification_status","onboarding_status","acquisition_source","platform","primary_device","state"]:
        t=clean[c].fillna("(Missing)").astype(str).value_counts().rename_axis(c).reset_index(name="user_count")
        t.to_csv(out/f"distribution_{c}.csv",index=False)
    with sqlite3.connect(out/"task01_local_analysis.sqlite") as con:
        clean.drop(columns=["full_name","email"],errors="ignore").to_sql("task01_users_clean",con,if_exists="replace",index=False)
        messy.drop(columns=["full_name","email"],errors="ignore").to_sql("task01_users_messy_audit",con,if_exists="replace",index=False)
    top=mt[mt.missing_count>0].head(10).sort_values("missing_count")
    plt.figure(figsize=(10,6)); plt.barh(top.column,top.missing_count)
    plt.title("Task 01 simulated clean-user data: top missing fields")
    plt.xlabel("Missing values (rows)"); plt.ylabel("Field"); plt.tight_layout()
    plt.savefig(charts/"top_missing_fields.png",dpi=180); plt.close()
    status=clean.account_status.fillna("(Missing)").astype(str).value_counts()
    plt.figure(figsize=(8,5)); plt.bar(status.index,status.values)
    plt.title("Task 01 simulated clean-user data: account status")
    plt.xlabel("Account status"); plt.ylabel("Users"); plt.tight_layout()
    plt.savefig(charts/"account_status_distribution.png",dpi=180); plt.close()
    print(json.dumps(s,indent=2))
if __name__=="__main__": main()
