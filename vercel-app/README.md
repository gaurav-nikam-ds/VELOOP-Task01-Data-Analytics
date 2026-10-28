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

**Status:** Existing user-provided screenshots from 2026-10-28 have been reviewed and are retained as visual evidence; the user does not need to resend them. Screenshots show Home, Findings, Supplied data audit, Deliverable tracker, Seven-dashboard blueprint and Implementation library; Findings priority-filter states and a completed deliverable-tracker CSV download are visible. The user also reported testing links and mobile layout. A fresh independent browser session after the latest repository commit has not been run. Automated browser tests are not configured by the current Vercel workflow.

- [x] Existing screenshots show the deployed page rendered and six main sections open; the Acceptance blockers view is listed in the sidebar but a dedicated screenshot was not identified in the reviewed set.
- [x] Findings screenshots show the priority filter at High and Medium and the corresponding findings; the text search interaction itself was not independently re-run.
- [x] Screenshot shows a completed deliverable-tracker CSV download; findings export control is visible. User also reported testing downloads.
- [x] Implementation-library document links are visible; user reported checking link behavior.
- [x] Desktop screenshots available; user reported mobile layout check (no mobile screenshot identified in reviewed subset).
- [x] Data-limitation disclosure is visible.
- [x] The UI does not imply a production connection or claim company performance.
- [x] Screenshots show supplied-data audit, deliverable tracker and seven-dashboard blueprint rendering.

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
