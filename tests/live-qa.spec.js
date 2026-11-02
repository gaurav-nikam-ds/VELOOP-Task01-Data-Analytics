import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

const baseURL = process.env.BASE_URL || "https://velop-task01-submission.vercel.app/";
const sections = [
  ["overview","Executive summary"],["audit","Product & data audit"],["coverage","Coverage matrix"],
  ["user","User analytics"],["earning","Earning & rewards"],["wallet","Wallet & withdrawals"],
  ["referral","Referral & engagement"],["tracking","Event tracking plan"],["dictionary","Data dictionary"],
  ["model","Logical data model"],["kpis","KPI catalogue"],["quality","Data quality & profiling"],
  ["blueprints","Dashboard blueprints"],["pipeline","Data pipeline"],["governance","Privacy & governance"],
  ["readiness","Readiness & assumptions"],["backlog","Developer handoff & backlog"],["deliverables","Assignment checklist"],
  ["dash-executive","Executive control tower"],["dash-users","User intelligence"],["dash-rewards","Rewards & wallet"],
  ["dash-referrals","Referral performance"],["dash-quality","Data quality monitor"],
  ["dash-operations","Operations & pipeline"],["dash-explorer","Data explorer"]
];

test.describe("VELOOP Task 01 — live 25-section submission QA", () => {
  test("production deployment loads and identifies the prototype accurately", async ({ page }) => {
    const response = await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    expect(response).not.toBeNull();
    expect(response.status()).toBeLessThan(400);
    await expect(page).toHaveTitle(/VELOOP.*Task 01/i);
    await expect(page.getByRole("navigation")).toBeVisible();
    await expect(page.getByText("SIMULATED / ILLUSTRATIVE ONLY", { exact: true })).toBeVisible();
    await expect(page.locator("#nav button[data-page]")).toHaveCount(25);
  });

  test("all 25 sections open and render their own content", async ({ page }) => {
    test.setTimeout(90000);
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    for (const [id, label] of sections) {
      const button = page.locator(`#nav button[data-page="${id}"]`);
      await expect(button, `Navigation item missing: ${label}`).toBeVisible();
      await button.click();
      await expect(page.locator(`#${id}.page.active`), `Section did not become active: ${label}`).toBeVisible();
      await expect(page.locator(`#${id} h1`).first(), `Section heading missing: ${label}`).toBeVisible();
    }
  });

  test("coverage inventory search filters rows correctly", async ({ page }) => {
    await page.goto(baseURL);
    await page.locator('#nav button[data-page="coverage"]').click();
    const rows = page.locator("#covTable tr:visible");
    const initial = await rows.count();
    await page.locator("#covSearch").fill("registration");
    await expect(rows).toHaveCount(2);
    await expect(rows.nth(1)).toContainText(/registration/i);
    await page.locator("#covSearch").fill("no-such-event");
    await expect(rows).toHaveCount(1);
    expect(initial).toBeGreaterThan(5);
    await page.locator("#covSearch").fill("");
    await expect(rows).toHaveCount(initial);
  });

  test("executive sample-window filter recalculates all four KPIs", async ({ page }) => {
    await page.goto(baseURL);
    await page.locator('#nav button[data-page="dash-executive"]').click();
    const kpis = page.locator("#exec-kpis");
    await expect(kpis).toContainText("1,038");
    await expect(kpis).toContainText("55.39%");
    await page.locator("#period").selectOption("7");
    await expect(kpis).toContainText("214");
    await expect(kpis).toContainText("56.54%");
    await expect(kpis).toContainText("62.56%");
    await page.locator("#period").selectOption("90");
    await expect(kpis).toContainText("3,204");
    await expect(kpis).toContainText("54.12%");
    await expect(kpis).toContainText("59.70%");
    await page.locator("#period").selectOption("30");
    await expect(kpis).toContainText("1,038");
  });

  test("user, reward, wallet, referral, quality and operations KPI blocks render", async ({ page }) => {
    await page.goto(baseURL);
    const checks = [
      ["dash-users","#user-kpis",["1,000","722","568","9"]],
      ["dash-rewards","#reward-kpis",["5,001","3,427","3,552","1,200"]],
      ["dash-referrals","#ref-kpis",["900","340","292","1"]],
      ["dash-quality","#quality-kpis",["700","52","1","0"]],
      ["dash-operations","#ops-kpis",["7","4","Apr–Sep 2026","Not live"]]
    ];
    for (const [section, selector, values] of checks) {
      await page.locator(`#nav button[data-page="${section}"]`).click();
      for (const value of values) await expect(page.locator(selector)).toContainText(value);
    }
  });

  test("data explorer domain and text filters change the result set", async ({ page }) => {
    await page.goto(baseURL);
    await page.locator('#nav button[data-page="dash-explorer"]').click();
    const rows = page.locator("#explorer-table tbody tr:visible");
    await expect(rows).toHaveCount(5);
    await page.locator("#explore-domain").selectOption("Rewards");
    await expect(rows).toHaveCount(1);
    await expect(rows.first()).toContainText("5,001");
    await page.locator("#explore-domain").selectOption("all");
    await page.locator("#explore-q").fill("onboarding");
    await expect(rows).toHaveCount(1);
    await expect(rows.first()).toContainText("722");
    await page.getByRole("button", { name: /Reset/ }).click();
    await expect(rows).toHaveCount(5);
  });

  test("filtered data explorer CSV downloads with correct data", async ({ page }) => {
    await page.goto(baseURL);
    await page.locator('#nav button[data-page="dash-explorer"]').click();
    await page.locator("#explore-domain").selectOption("Wallet");
    const downloadPromise = page.waitForEvent("download");
    await page.getByRole("button", { name: /Export visible CSV/ }).click();
    const download = await downloadPromise;
    expect(download.suggestedFilename()).toBe("velop_simulated_data_explorer.csv");
    const stream = await download.createReadStream();
    let csv = "";
    for await (const chunk of stream) csv += chunk.toString("utf8");
    expect(csv).toContain('"Wallet","Unmatched references","52"');
    expect([1,2]).toContain(csv.split(/\r?\n/).length);
    if (csv.startsWith('"Domain","Metric","Value","Note"')) expect(csv.split(/\r?\n/)).toHaveLength(2);
  });

  test("responsive layouts remain usable without horizontal page overflow", async ({ page }) => {
    for (const width of [320,360,390,768,1024,1440]) {
      await page.setViewportSize({ width, height: 900 });
      await page.goto(baseURL, { waitUntil: "domcontentloaded" });
      const dimensions = await page.evaluate(() => ({
        viewport: document.documentElement.clientWidth,
        page: document.documentElement.scrollWidth
      }));
      expect(dimensions.page, `Horizontal overflow at ${width}px: ${JSON.stringify(dimensions)}`)
        .toBeLessThanOrEqual(dimensions.viewport + 1);
      if (width <= 700) await page.locator("button.mobile").click();
      if (width <= 700) await page.locator("button.mobile").first().click();
      await page.locator('#nav button[data-page="dash-explorer"]').click();
      await expect(page.locator("#explore-domain")).toBeVisible();
    }
  });

  test("interactive controls have accessible names and all IDs are unique", async ({ page }) => {
    await page.goto(baseURL);
    const unnamed = await page.locator("button, a, input, select").evaluateAll(nodes => nodes.filter(node => {
      if (node.matches("input,select")) return !(node.getAttribute("aria-label") || node.labels?.length || node.getAttribute("title"));
      return !((node.getAttribute("aria-label") || node.innerText || node.getAttribute("title") || "").trim());
    }).map(node => node.outerHTML.slice(0, 180)));
    expect(unnamed, "Controls without accessible names").toEqual([]);
    const ids = await page.locator("[id]").evaluateAll(nodes => nodes.map(node => node.id));
    expect(ids.length, "Duplicate IDs detected").toBe(new Set(ids).size);
  });

  test("WCAG 2.1 A/AA automated scan on all 25 sections", async ({ page }) => {
    test.setTimeout(180000);
    test.setTimeout(120_000);
    await page.goto(baseURL);
    const failures = [];
    for (const [id, label] of sections) {
      await page.locator(`#nav button[data-page="${id}"]`).click();
      const scan = await new AxeBuilder({ page }).withTags(["wcag2a","wcag2aa","wcag21a","wcag21aa"]).analyze();
      if (scan.violations.length) failures.push({
        section: label,
        violations: scan.violations.map(v => ({
          id: v.id,
          impact: v.impact,
          help: v.help,
          nodes: v.nodes.map(n => ({ target: n.target, html: n.html, failureSummary: n.failureSummary }))
        }))
      });
    }
    if (failures.length) console.log("AXE_DETAILS " + JSON.stringify(failures));
    expect(failures, "WCAG 2.1 A/AA violations by section").toEqual([]);
  });

  test("no failed network requests, HTTP errors or uncaught JS errors", async ({ page }) => {
    test.setTimeout(90000);
    const failed = [], badResponses = [], pageErrors = [], consoleErrors = [];
    page.on("requestfailed", request => failed.push(`${request.method()} ${request.url()}: ${request.failure()?.errorText}`));
    page.on("response", response => { if (response.status() >= 400) badResponses.push(`${response.status()} ${response.url()}`); });
    page.on("pageerror", error => pageErrors.push(error.message));
    page.on("console", message => { if (message.type() === "error") consoleErrors.push(message.text()); });
    await page.goto(baseURL, { waitUntil: "networkidle" });
    for (const [id] of sections) await page.locator(`#nav button[data-page="${id}"]`).click();
    expect(failed).toEqual([]);
    expect(badResponses).toEqual([]);
    expect(pageErrors).toEqual([]);
    expect(consoleErrors).toEqual([]);
  });
});
