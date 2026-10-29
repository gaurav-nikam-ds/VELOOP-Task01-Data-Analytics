"""Dependency-free integrity checks for the Vercel-only VELOOP workspace."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "vercel-app"
PAGE = APP / "app" / "page.jsx"
STYLES = APP / "app" / "globals.css"
LAYOUT = APP / "app" / "layout.jsx"
PACKAGE = APP / "package.json"
README = ROOT / "README.md"
WORKFLOW = ROOT / ".github" / "workflows" / "live-vercel-qa.yml"


class ProjectIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = PAGE.read_text(encoding="utf-8")
        cls.styles = STYLES.read_text(encoding="utf-8")
        cls.layout = LAYOUT.read_text(encoding="utf-8")
        cls.package = PACKAGE.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_vercel_app_entrypoints_exist(self):
        for path in (PAGE, STYLES, LAYOUT, PACKAGE):
            with self.subTest(path=path.name):
                self.assertTrue(path.is_file(), f"Missing Vercel app file: {path}")

    def test_all_seven_workspace_sections_are_present(self):
        for section in (
            "Executive status",
            "Insights & recommendations",
            "Supplied data audit",
            "Deliverable tracker",
            "Seven-dashboard blueprint",
            "Acceptance blockers",
            "Implementation library",
        ):
            with self.subTest(section=section):
                self.assertIn(section, self.page)

    def test_simulated_data_limitation_is_explicit(self):
        text = (self.page + self.readme).lower()
        self.assertIn("simulated", text)
        self.assertTrue("production" in text or "not actual" in text)

    def test_csv_exports_are_implemented(self):
        self.assertIn("downloadCSV", self.page)
        self.assertIn("text/csv", self.page)

    def test_navigation_and_accessibility_hooks_are_present(self):
        self.assertIn("aria-label", self.page)
        self.assertIn("nav-item", self.page)
        self.assertIn("@media(max-width:720px)", self.styles)

    def test_package_has_build_script(self):
        import json
        package = json.loads(self.package)
        self.assertIn("build", package.get("scripts", {}))

    def test_live_qa_workflow_targets_vercel(self):
        self.assertIn("veloop-task01-data-analytics.vercel.app", self.workflow)
        self.assertIn("tests/live-qa.spec.js", self.workflow)

    def test_streamlit_artifacts_are_not_active(self):
        self.assertFalse((ROOT / "app" / "streamlit_app.py").exists())
        self.assertFalse((ROOT / "requirements.txt").exists())
        self.assertFalse((ROOT / ".github" / "workflows" / "streamlit-smoke-test.yml").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
