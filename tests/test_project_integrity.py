"""Fast, dependency-free integrity checks for the VELOOP Task 01 workspace."""
from pathlib import Path
import ast
import unittest

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "app" / "streamlit_app.py"
README = ROOT / "README.md"
REQUIREMENTS = ROOT / "requirements.txt"


class ProjectIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = APP.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source, filename=str(APP))

    def test_streamlit_source_compiles(self):
        compile(self.source, str(APP), "exec")

    def test_page_configuration_exists(self):
        self.assertIn("st.set_page_config", self.source)

    def test_all_workspace_sections_are_present(self):
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
                self.assertIn(section, self.source)

    def test_synthetic_data_limitation_is_explicit(self):
        self.assertIn("simulated", self.source.lower())
        self.assertIn("production", self.source.lower())
        self.assertIn("not actual", self.source.lower())

    def test_downloadable_outputs_are_present(self):
        self.assertIn("st.download_button", self.source)
        self.assertIn("to_csv(index=False)", self.source)

    def test_declared_dependencies_cover_imports(self):
        reqs = REQUIREMENTS.read_text(encoding="utf-8").lower()
        for dependency in ("streamlit", "pandas"):
            with self.subTest(dependency=dependency):
                self.assertIn(dependency, reqs)

    def test_readme_documents_local_run_and_limitations(self):
        readme = README.read_text(encoding="utf-8")
        self.assertIn("streamlit run app/streamlit_app.py", readme)
        self.assertIn("production", readme.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
