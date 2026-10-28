# VELOOP Task 01 — Vercel app

This is the deployed Next.js web version of the evidence workspace. It lives in `vercel-app/` so the existing Streamlit app remains intact.

## Live deployment

https://velop-task01-data-analytics.vercel.app/

## Deploy to Vercel

1. Import `gaurav-nikam-ds/VELOOP-Task01-Data-Analytics` into Vercel.
2. In **Configure Project → Root Directory**, select `vercel-app`.
3. Framework preset: **Next.js**. Build command: `npm run build`. Leave output directory on the framework's auto-detected/default value.
4. Deploy and confirm the deployment is ready.
5. Run the acceptance checks below against the deployed URL after any material UI change.

## Local run and build

```bash
cd vercel-app
npm install
npm run dev
```

To verify a production build locally:

```bash
npm install
npm run build
```

The repository has a dedicated [Vercel app build workflow](../.github/workflows/vercel-app-build.yml). It installs the app dependencies and runs the Next.js production build on relevant pushes and pull requests.

## Manual acceptance checklist

**Status:** The project owner reports these checks have been completed on the deployed website on 2026-10-28. This checklist records manual verification; it is not a claim that automated browser tests were run.

- [x] Deployed page loads and the seven navigation sections work.
- [x] Findings search and priority filters work.
- [x] CSV exports download and open.
- [x] Source/document links open.
- [x] Desktop and mobile layouts are readable.
- [x] Data-limitation disclosure is visible.
- [x] The UI does not imply a production connection or claim company performance.
- [x] Supplied-data audit, deliverable tracker and dashboard blueprint render.

## Data authenticity

All metrics shown are findings from the supplied simulated assignment workbooks. The separate behavior workbook is labeled Task 02 and is not merged into Task 01. This site has no production database/API connection. Proposed KPIs, event contracts, data models and business rules require company owner approval.
