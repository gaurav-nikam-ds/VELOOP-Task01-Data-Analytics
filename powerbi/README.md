# VELOOP Task 01 — Power BI Starter Project

This folder contains Power BI assets and instructions for building the report in Power BI Desktop. It is **not a .pbix file** and does not claim to be a completed Power BI report.

## What is included
- `theme.json`: restrained enterprise theme (navy, teal, slate, light canvas).
- `measures.dax`: starter measures for the synthetic demo dataset.
- `report_build_guide.md`: page layout and visual mapping.
- `data/`: small illustrative CSV tables for importing into Power BI.

## Open in Power BI Desktop
1. Download the repository (Code → Download ZIP) or clone it.
2. Open Power BI Desktop → **Get data → Text/CSV**.
3. Import the CSV files in `powerbi/data/`.
4. Set the date columns to Date, IDs to Whole number/Text as appropriate, amounts to Decimal number, and status/domain columns to Text.
5. In Model view, create a Date table and relationships as described in `report_build_guide.md`.
6. Import `theme.json` via View → Themes → Browse for themes.
7. Add measures from `measures.dax` using Modeling → New measure.
8. Build the pages following the visual map, then save as `VELOOP_Task01_Product_Analytics.pbix`.

## Data honesty
All rows in these CSVs are synthetic and only for demonstrating visuals and DAX. They are not VELOOP production records, and metrics must not be presented as company performance.

## Suggested report pages
1. Executive Overview
2. Engagement & Tasks
3. Rewards & Wallet
4. Withdrawals & Referrals
5. Data Readiness

A genuine `.pbix` must be saved by Power BI Desktop. This repository currently provides the source assets, not a prebuilt PBIX binary.
