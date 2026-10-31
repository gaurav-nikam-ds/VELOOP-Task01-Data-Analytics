# VELOOP Task 01 — Python, SQL & Visualization Evidence

**Data notice:** This analysis uses only the supplied Task 01 simulated user-profile workbook. It is not VELOOP production data. Task 02 is deliberately excluded.

## Included
- Reproducible Python/pandas profiling script.
- SQLite-compatible SQL queries for data quality and descriptive analysis.
- Aggregate-only evidence files; no names or email addresses are exported.

## Run
Install dependencies: `python -m pip install pandas openpyxl matplotlib`

```bash
python analytics/python/analyze_task01.py --input "/path/to/VELoop_Rewards_Data_01.xlsx" --output-dir outputs
```

The script creates a local SQLite database at `outputs/task01_local_analysis.sqlite`. Run `analytics/sql/task01_analysis.sql` against it using DBeaver, DB Browser for SQLite or SQLite CLI. Keep the local database out of GitHub.

## Interpretation boundaries
- `Users_1000_Clean` is the primary descriptive-analysis sheet.
- `Users_Messy_Audit` is used only to compare audit-row and duplicate-ID counts.
- Missing referral details may be conditionally optional; missing last-login may be legitimate for users who have not logged in.
- The source workbook contains no transaction-level task, reward, wallet, withdrawal, referral or event tables. Do not infer those metrics from user-profile fields.
- Generated outputs are aggregates from simulated assignment data, not company performance.
