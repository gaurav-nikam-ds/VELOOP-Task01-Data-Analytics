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

**Status:** These are owner-reported manual checks dated 2026-10-28, not independently re-run by the current assistant QA environment. A fresh independent request to the deployed URL could not be completed in this pass. Automated browser tests are not configured by the current Vercel workflow.

- [x] Deployed page loads and the seven navigation sections work.
- [x] Findings search and priority filters work.
- [x] CSV exports download and open.
- [x] Source/document links open.
- [x] Desktop and mobile layouts are readable.
- [x] Data-limitation disclosure is visible.
- [x] The UI does not imply a production connection or claim company performance.
- [x] Supplied-data audit, deliverable tracker and dashboard blueprint render.

## Implemented versus planned

The Vercel workspace is a reviewer/evidence interface. Its seven navigation sections and their rendered reviewer content are implemented UI features; they are not seven production analytics dashboards. Search/priority filtering, CSV exports and document links are listed as owner-reported manual checks in the acceptance checklist below. No production database/API connection or live analytics pipeline is configured.

| Feature area | Status | Evidence / caveat |
|---|---|---|
| Seven reviewer navigation sections and reviewer pages | Implemented in the workspace UI | Reviewer pages only; not separate production dashboards |
| Findings search and priority filters | Owner-reported as tested | Attach screenshots or browser-run evidence to the final QA package |
| CSV exports | Owner-reported as tested | Synthetic/profile-audit content only; retain caveats in exports |
| Document/source links | Owner-reported as tested | Independent post-change recheck pending |
| Responsive layout | Owner-reported as tested | Independent post-change recheck pending |
| Seven dashboard specifications | Planned/proposed analytics design | Not seven live production dashboards |
| Production data connection, event tracking, data pipeline | Not implemented / not configured in this workspace | Requires engineering implementation, approved source systems and internal sign-off |
| Task 02 behavior data inside Task 01 | Blocked pending approval | Keep separate unless coordinator approves reuse |

## Data authenticity

All metrics shown are findings from the supplied simulated assignment workbooks. The separate behavior workbook is labeled Task 02 and is not merged into Task 01. This site has no production database/API connection. Proposed KPIs, event contracts, data models and business rules require company owner approval.
