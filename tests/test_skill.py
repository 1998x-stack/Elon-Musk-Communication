"""Regression tests for skill packaging, installation and email structure."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.email_lint import lint_email
from scripts.install import plan
from scripts.sync_mirrors import check
from scripts.validate_skill import validate


class EmailStructureTests(unittest.TestCase):
    def test_three_line_routine(self):
        content = ("Subject: [Decision] Capacity gap\n\n"
                   "Throughput is 12.5% below target.\n"
                   "We recommend moving one test runner.\n"
                   "Please approve the $25k capacity plan.\n")
        self.assertEqual(lint_email(content), [])

    def test_missing_subject(self):
        self.assertTrue(lint_email("Something broke."))

    def test_routine_requires_three_lines(self):
        self.assertTrue(lint_email("Subject: Update\nOnly one line."))

    def test_incidents_not_forced_to_three_lines(self):
        content = ("Subject: [Urgent] Incident alert\n"
                   "Confirmed outage.\n"
                   "Containment underway.\n"
                   "Next update soon.\n"
                   "Compliance paging initiated.\n")
        self.assertEqual(lint_email(content, "incident"), [])

    def test_incident_needs_urgency_signal(self):
        self.assertTrue(lint_email("Subject: A thing\nAlert.", "incident"))


class PackagingTests(unittest.TestCase):
    def test_manifest_and_files(self):
        self.assertEqual(validate(), [])

    def test_all_mirrors_identical(self):
        self.assertEqual(check(), [])

    def test_install_copies_complete_skill_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            base = [sys.executable, str(ROOT / "scripts/install.py"),
                    "--agent", "codex", "--scope", "project",
                    "--project", str(project)]
            first = subprocess.run(base, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            target = project / ".agents/skills/elon-musk-communication"
            self.assertTrue((target / "SKILL.md").exists())
            self.assertTrue((target / "references/bad-news-playbook.md").exists())
            self.assertTrue((target / "assets/templates/README.md").exists())
            again = subprocess.run(base, capture_output=True, text=True)
            self.assertNotEqual(again.returncode, 0)
            self.assertIn("refusing to overwrite", again.stderr)

    def test_cursor_project_rule_install(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            cmd = [sys.executable, str(ROOT / "scripts/install.py"), "--agent", "cursor",
                   "--scope", "project", "--project", str(project)]
            result = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((project / ".cursor/rules/elon-musk-communication.mdc").is_file())


if __name__ == "__main__":
    unittest.main()
