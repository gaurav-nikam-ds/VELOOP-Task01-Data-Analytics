import { test, expect } from "@playwright/test";
import { readFile } from "node:fs/promises";
import AxeBuilder from "@axe-core/playwright";

const baseURL = process.env.BASE_URL || "https://veloop-task01-data-analytics.vercel.app/";

test.describe("VELOOP live reviewer workspace", () => {
  test("loads the public site and shows the data-authenticity notice", async ({ page }) => {
    const response = await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    expect(response, "The browser should receive a document response").not.toBeNull();
    expect(response.status(), "The live page should respond successfully").toBeLessThan(400);
    await expect(page).toHaveTitle(/VELOOP Rewards/i);
    await expect(page.getByText("PLEASE NOTE", { exact: true })).toBeVisible();
    await expect(page.getByRole("navigation")).toBeVisible();
  });

  test("all seven navigation sections open their expected content", async ({ page }) => {
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    const sections = [
      { nav: "Home", heading: "What this project delivers" },
      { nav: "Findings", heading: "What needs attention in the supplied files?" },
      { nav: "Data audit", heading: "What data was actually supplied?" },
      { nav: "Deliverables", heading: "What has been documented for the assignment?" },
      { nav: "Dashboard plan", heading: "What each future dashboard should answer" },
      { nav: "What remains", heading: "What the project cannot finish without VELOOP" },
      { nav: "Documents", heading: "Detailed evidence and technical handoff" },
    ];

    const navigationButtons = page.getByRole("navigation").getByRole("button");
    await expect(navigationButtons).toHaveCount(7);
    await expect(page.getByRole("navigation").getByRole("button", { name: "Python + SQL", exact: true })).toHaveCount(0);

    for (const section of sections) {
      await page.getByRole("navigation").getByRole("button", { name: section.nav }).click();
      await expect(page.getByRole("heading", { name: section.heading, exact: true })).toBeVisible();
      await expect(page.getByRole("navigation").getByRole("button", { name: section.nav })).toHaveClass(/selected/);
    }
  });

  test("data profiling evidence is integrated into the supplied data audit", async ({ page }) => {
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    await page.getByRole("navigation").getByRole("button", { name: "Data audit" }).click();
    await expect(page.getByRole("heading", { name: "Profile and quality evidence", exact: true })).toBeVisible();
    await expect(page.getByText("953", { exact: true })).toBeVisible();
    await expect(page.getByText(/881 rows/)).toBeVisible();
    await expect(page.getByText(/88.1%/)).toBeVisible();
    await expect(page.locator('img[alt^="Top missing fields"]')).toBeVisible();
    expect(await page.getByRole("link", { name: /Open reproducible profiling script/ }).getAttribute("href")).toContain("analytics/python/analyze_task01.py");
    expect(await page.getByRole("link", { name: /Open validation queries/ }).getAttribute("href")).toContain("analytics/sql/task01_analysis.sql");
    await expect(page.getByRole("heading", { name: "Supplemental synthetic test layer", exact: true })).toBeVisible();
    await expect(page.getByText(/52 wallet reference IDs/)).toBeVisible();
    await expect(page.getByText(/one self-referral/)).toBeVisible();
    await expect(page.locator('img[alt^="Supplemental synthetic test pack record counts"]')).toBeVisible();
    expect(await page.getByRole("link", { name: /Open reproducible dataset checks/ }).getAttribute("href")).toContain("analytics/python/analyze_synthetic_pack.py");
    expect(await page.getByRole("link", { name: /Open relationship and KPI queries/ }).getAttribute("href")).toContain("analytics/sql/synthetic_test_pack_analysis.sql");
  });

  test("findings search and priority filter change the visible results", async ({ page }) => {
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    await page.getByRole("navigation").getByRole("button", { name: "Findings" }).click();
    await expect(page.getByRole("heading", { name: "What needs attention in the supplied files?" })).toBeVisible();

    const findingCards = page.locator(".finding-card");
    await expect(findingCards).toHaveCount(4);

    await page.getByRole("combobox", { name: "Filter by priority" }).selectOption("High");
    await expect(findingCards).toHaveCount(4);
    await expect(page.getByText("High priority").first()).toBeVisible();

    await page.getByRole("textbox", { name: "Search findings" }).fill("Repeated IDs");
    await expect(findingCards).toHaveCount(1);
    await expect(page.getByRole("heading", { name: "Repeated IDs in messy audit tab" })).toBeVisible();

    await page.getByRole("textbox", { name: "Search findings" }).fill("no-such-finding-term");
    await expect(findingCards).toHaveCount(0);
  });

  test("findings and deliverable CSV exports download with expected filenames", async ({ page }) => {
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    await page.getByRole("navigation").getByRole("button", { name: "Findings" }).click();
    const findingsDownloadPromise = page.waitForEvent("download");
    await page.getByRole("button", { name: /Export findings CSV/ }).click();
    const findingsDownload = await findingsDownloadPromise;
    expect(findingsDownload.suggestedFilename()).toBe("velop-task01-evidence-findings.csv");
    const findingsPath = await findingsDownload.path();
    const findingsCsv = await readFile(findingsPath, "utf8");
    const findingsLines = findingsCsv.trim().split(/\r?\n/);
    expect(findingsLines.length, "Findings export should contain a header and data rows").toBeGreaterThan(1);
    expect(findingsLines[0]).toBe('"Finding","Metric","Evidence","Risk","Recommended action","Priority"');
    expect(findingsLines).toHaveLength(5);
    expect(findingsCsv).toContain('"Repeated IDs in messy audit tab"');
    expect(findingsCsv).toContain('"High"');

    await page.getByRole("navigation").getByRole("button", { name: "Deliverables" }).click();
    const deliverablesDownloadPromise = page.waitForEvent("download");
    await page.getByRole("button", { name: /Export deliverable tracker/ }).click();
    const deliverablesDownload = await deliverablesDownloadPromise;
    expect(deliverablesDownload.suggestedFilename()).toBe("velop-task01-deliverable-tracker.csv");
    const deliverablesPath = await deliverablesDownload.path();
    const deliverablesCsv = await readFile(deliverablesPath, "utf8");
    const deliverablesLines = deliverablesCsv.trim().split(/\r?\n/);
    expect(deliverablesLines.length, "Deliverables export should contain a header and data rows").toBeGreaterThan(1);
    expect(deliverablesLines[0]).toBe('"Deliverable","Evidence status","Remaining dependency"');
    expect(deliverablesLines).toHaveLength(22);
    expect(deliverablesCsv).toContain('"Final handoff and recommendations"');
  });

  test("the site remains usable at a narrow mobile viewport", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("navigation")).toBeVisible();
    await page.getByRole("navigation").getByRole("button", { name: "Findings" }).click();
    await expect(page.getByRole("heading", { name: "What needs attention in the supplied files?" })).toBeVisible();
  });

  test("responsive layouts do not create horizontal page overflow", async ({ page }) => {
    for (const width of [320, 360, 390, 768, 1024, 1440]) {
      await page.setViewportSize({ width, height: 900 });
      await page.goto(baseURL, { waitUntil: "domcontentloaded" });
      const dimensions = await page.evaluate(() => ({ viewport: document.documentElement.clientWidth, page: document.documentElement.scrollWidth }));
      expect(dimensions.page, `Horizontal overflow at width ${width}: ${JSON.stringify(dimensions)}`).toBeLessThanOrEqual(dimensions.viewport + 1);
      await page.getByRole("navigation").getByRole("button", { name: "Findings" }).click();
      await expect(page.getByRole("heading", { name: "What needs attention in the supplied files?" })).toBeVisible();
    }
  });

  test("all eight implementation-library document links resolve", async ({ page, request }) => {
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    await page.getByRole("navigation").getByRole("button", { name: "Documents" }).click();
    const links = await page.locator("a.library-card").evaluateAll(nodes => nodes.map(a => ({ title: a.querySelector("h3")?.textContent?.trim() || a.textContent.trim(), href: a.href })));
    expect(links.length).toBe(8);
    for (const link of links) {
      const response = await request.get(link.href, { timeout: 20000 });
      expect(response.status(), `Broken document link: ${link.title} -> ${link.href}`).toBeLessThan(400);
    }
  });

  test("interactive controls have accessible names and IDs are unique", async ({ page }) => {
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    const unnamed = await page.locator("button, a, input, select").evaluateAll(nodes => nodes.filter(node => {
      if (node.matches("input,select")) return !(node.getAttribute("aria-label") || node.labels?.length || node.getAttribute("title"));
      return !((node.getAttribute("aria-label") || node.innerText || node.getAttribute("title") || "").trim());
    }).map(node => node.outerHTML.slice(0, 180)));
    expect(unnamed, "Interactive controls without accessible names").toEqual([]);
    const ids = await page.locator("[id]").evaluateAll(nodes => nodes.map(node => node.id));
    expect(ids.length, "Duplicate id attributes detected").toBe(new Set(ids).size);
  });

  test("automated accessibility scan reports no WCAG 2.1 A/AA violations", async ({ page }) => {
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    for (const nav of ["Home", "Findings", "Data audit", "Deliverables", "Dashboard plan", "What remains", "Documents"]) {
      await page.getByRole("navigation").getByRole("button", { name: nav }).click();
      const scan = await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]).analyze();
      expect(scan.violations.map(v => ({ id: v.id, impact: v.impact, help: v.help, nodes: v.nodes.length })), `Accessibility violations in ${nav}`).toEqual([]);
    }
  });

  test("no failed requests or HTTP error responses while navigating", async ({ page }) => {
    const failed = [];
    const badResponses = [];
    page.on("requestfailed", request => {
      const url = request.url();
      if (!url.startsWith("data:") && !url.startsWith("blob:")) failed.push(`${request.method()} ${url}: ${request.failure()?.errorText || "request failed"}`);
    });
    page.on("response", response => { if (response.status() >= 400) badResponses.push(`${response.status()} ${response.url()}`); });
    await page.goto(baseURL, { waitUntil: "networkidle" });
    for (const nav of ["Findings", "Data audit", "Deliverables", "Dashboard plan", "What remains", "Documents", "Home"]) {
      await page.getByRole("navigation").getByRole("button", { name: nav }).click();
    }
    expect(failed, "Failed requests: " + failed.join(" | ")).toEqual([]);
    expect(badResponses, "HTTP error responses: " + badResponses.join(" | ")).toEqual([]);
  });

  test("no uncaught JavaScript page errors occur while navigating", async ({ page }) => {
    const pageErrors = [];
    const consoleErrors = [];
    page.on("pageerror", error => pageErrors.push(error.message));
    page.on("console", message => { if (message.type() === "error") consoleErrors.push(message.text()); });
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    for (const nav of ["Findings", "Data audit", "Deliverables", "Dashboard plan", "What remains", "Documents", "Home"]) {
      await page.getByRole("navigation").getByRole("button", { name: nav }).click();
    }
    expect(pageErrors, "Uncaught browser errors: " + pageErrors.join(" | ")).toEqual([]);
    expect(consoleErrors, "Browser console errors: " + consoleErrors.join(" | ")).toEqual([]);
  });
});
