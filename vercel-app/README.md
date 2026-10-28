# VELOOP Task 01 — Vercel app

This is the Vercel-compatible web version of the Streamlit evidence workspace. It lives in a separate folder so the existing Streamlit deployment is not overwritten.

## Deploy to Vercel

1. Import `gaurav-nikam-ds/VELOOP-Task01-Data-Analytics` into Vercel.
2. In **Configure Project → Root Directory**, select `vercel-app`.
3. Framework preset: **Next.js**. Build command: `npm run build`. Output directory: leave the default/auto-detected value.
4. Deploy. Vercel should build from this directory and redeploy on commits.
5. Test the deployed URL using the acceptance checklist below.

## Local run

```bash
cd vercel-app
npm install
npm run dev
```

## Acceptance checklist

- [ ] Build completes successfully on Vercel.
- [ ] All seven navigation sections work.
- [ ] CSV exports download and contain the displayed values.
- [ ] Source/document links resolve.
- [ ] Desktop and mobile layouts are readable.
- [ ] Data-limitation disclosure remains visible.
- [ ] No production connection or company-performance claim is implied.

## Data authenticity

All metrics shown are findings from the supplied simulated assignment workbooks. The separate behavior workbook is labeled Task 02 and is not merged into Task 01. This site has no production database/API connection. Proposed KPIs, event contracts, data models and business rules require company owner approval.
