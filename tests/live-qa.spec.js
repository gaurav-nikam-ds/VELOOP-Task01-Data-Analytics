import { test, expect } from "@playwright/test";
import { readFile } from "node:fs/promises";

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

    for (const section of sections) {
      await page.getByRole("navigation").getByRole("button", { name: section.nav }).click();
      await expect(page.getByRole("heading", { name: section.heading, exact: true })).toBeVisible();
      await expect(page.getByRole("navigation").getByRole("button", { name: section.nav })).toHaveClass(/selected/);
    }
  });

  test("findings search and priority filter change the visible results", async ({ page }) => {
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    await page.getByRole("navigation").getByRole("button", { name: "Findings" }).click();

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
    const findingsLines = findingsCsv.trim().split(/\\r?\\n/);
    expect(findingsLines.length, "Findings export should contain a header and data rows").toBeGreaterThan(1);
    expect(findingsLines[0].toLowerCase()).toContain("finding");

    await page.getByRole("navigation").getByRole("button", { name: "Deliverables" }).click();
    const deliverablesDownloadPromise = page.waitForEvent("download");
    await page.getByRole("button", { name: /Export deliverable tracker/ }).click();
    const deliverablesDownload = await deliverablesDownloadPromise;
    expect(deliverablesDownload.suggestedFilename()).toBe("velop-task01-deliverable-tracker.csv");
    const deliverablesPath = await deliverablesDownload.path();
    const deliverablesCsv = await readFile(deliverablesPath, "utf8");
    const deliverablesLines = deliverablesCsv.trim().split(/\\r?\\n/);
    expect(deliverablesLines.length, "Deliverables export should contain a header and data rows").toBeGreaterThan(1);
    expect(deliverablesLines[0].toLowerCase()).toContain("deliverable");
  });

  test("the site remains usable at a narrow mobile viewport", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(baseURL, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("navigation")).toBeVisible();
    await page.getByRole("navigation").getByRole("button", { name: "Findings" }).click();
    await expect(page.getByRole("heading", { name: "What needs attention in the supplied files?" })).toBeVisible();
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
