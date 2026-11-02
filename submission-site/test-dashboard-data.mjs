import assert from "node:assert/strict";
import { readFileSync, writeFileSync, unlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { execFileSync } from "node:child_process";

const html = readFileSync(new URL("./index.html", import.meta.url), "utf8");
const pages = [...html.matchAll(/<section class="page(?: active)?" id="([^"]+)"/g)].map(m => m[1]);
const nav = [...html.matchAll(/data-page="([^"]+)"/g)].map(m => m[1]);
const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(m => m[1]);

assert.equal(pages.length, 25, "Expected 25 pages (18 assignment + 7 dashboards)");
assert.equal(new Set(pages).size, pages.length, "Page IDs must be unique");
assert.equal(new Set(ids).size, ids.length, "All HTML IDs must be unique");
assert.deepEqual([...new Set(nav)].sort(), [...pages].sort(), "Navigation must map to all pages");

for (const id of ["dash-executive","dash-users","dash-rewards","dash-referrals","dash-quality","dash-operations","dash-explorer","exec-kpis","exec-task-status-bars","user-onboarding-bars","reward-kpis","withdraw-bars","ref-kpis","quality-kpis","ops-kpis","explorer-table"]) {
  assert.ok(ids.includes(id), "Missing dashboard element: " + id);
}
for (const value of ["3,229","5,001","3,427","3,552","1,200","52","722","72.2%","56.54%","55.39%","54.12%","62.56%","66.30%","67.05%","68.29%","62.62%","59.70%"]) {
  assert.ok(html.includes(value), "Missing verified sample value: " + value);
}

const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
assert.equal(scripts.length, 1, "Expected one inline app script");
const temp = join(tmpdir(), "velop-submission-site-" + process.pid + ".js");
try {
  writeFileSync(temp, scripts[0][1], "utf8");
  execFileSync(process.execPath, ["--check", temp], { stdio: "pipe" });
} finally {
  try { unlinkSync(temp); } catch {}
}
assert.match(scripts[0][1], /function filterExplore\(/);
assert.match(scripts[0][1], /function exportExplore\(/);
assert.match(scripts[0][1], /function changePeriod\(/);
assert.match(html, /SIMULATED DATA — CREATED FOR ANALYTICAL TESTING/);
for (const stale of ["68.4%","92.1%","87.6%","72.4%","4,605","4,450"]) {
  assert.ok(!scripts[0][1].includes(stale), "Stale unsupported figure: " + stale);
}
console.log("PASS: 25 pages, navigation, unique IDs, dashboard evidence, interactions and JavaScript syntax.");
