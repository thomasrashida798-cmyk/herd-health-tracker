"""Automated tests for the layered Herd Health Tracker application."""

from datetime import date

import herd_health_tracker as hht
from herd_health_tracker_app.models import HealthRecord, LivestockAnimal
from support import TestBase, add, run


class TestMenu(TestBase):
    def test_19_menu_and_clean_exit(self):
        _, out = run(hht.main, ["n", "2", "9", "", "abc", "5"])
        self.assertIn("1. Add a health record", out)
        self.assertIn("5. Exit", out)
        self.assertEqual(out.count("Invalid choice"), 3)
        self.assertIn("No health records have been added yet", out)
        self.assertIn("Goodbye", out)
        self.assertGreaterEqual(out.count("===== HERD HEALTH TRACKER ====="), 4)

    def test_19b_full_session_with_demo_data(self):
        answers = ["y", "2", "3", "AN-001", "4", "AN-002", "3", "AN-404", "5"]
        _, out = run(hht.main, answers)
        self.assertIn("Fictional demonstration records loaded", out)
        self.assertIn("HR-003", out)
        self.assertIn("Needs Monitoring", out)
        self.assertIn("No animal with ID AN-404 was found", out)
        self.assertIn("Goodbye", out)

    def test_19c_add_through_menu(self):
        answers = ["n", "1", "AN-005", "Cattle", "Unknown", "36", "2026-10-05",
                   "Limping", "3", "None", "2", "5"]
        _, out = run(hht.main, answers)
        self.assertIn("Record HR-001 saved", out)
        self.assertIn("Limping", out)

    def test_19e_eof_exits_cleanly(self):
        _, out = run(hht.main, [EOFError()])
        self.assertIn("Exiting the program", out)
