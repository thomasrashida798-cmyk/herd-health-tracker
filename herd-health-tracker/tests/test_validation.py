"""Automated tests for the layered Herd Health Tracker application."""

from datetime import date

import herd_health_tracker as hht
from herd_health_tracker_app.models import HealthRecord, LivestockAnimal
from support import TestBase, add, run


class TestValidation(TestBase):
    def test_07_negative_age_rejected(self):
        self.assertIsNone(hht.parse_age("-5"))
        _, out = run(hht.add_health_record,
                     ["AN-9", "Goat", "Unknown", "-5", "24", "2026-10-01", "ok", "1", "None"],
                     self.records)
        self.assertIn("Invalid age", out)
        self.assertEqual(self.records[0].animal.age_months, 24)

    def test_08_non_numeric_age_rejected(self):
        for bad in ("abc", "2.5", "", "twelve"):
            self.assertIsNone(hht.parse_age(bad))
        self.assertEqual(hht.parse_age(" 0 "), 0)
        # regression: a 5000-digit string used to crash int(); limits now reject it
        self.assertIsNone(hht.parse_age("9" * 5000))
        self.assertIsNone(hht.parse_age("1201"))
        self.assertIsNone(hht.parse_age("99999999999"))
        self.assertEqual(hht.parse_age("1200"), 1200)
        self.assertEqual(hht.parse_age("18"), 18)

    def test_09_invalid_date_rejected(self):
        for bad in ("2026-02-30", "2026-13-01", "01-10-2026", "2026-1-5", "tomorrow", ""):
            self.assertIsNone(hht.parse_date(bad), bad)
        self.assertEqual(hht.parse_date("2024-02-29"), date(2024, 2, 29))   # leap day
        _, out = run(hht.ask_date, ["2026-02-30", "2026-10-01"])
        self.assertIn("Invalid date", out)

    def test_10_unsupported_status_rejected(self):
        status, out = run(hht.ask_status, ["Sick", "7", "2"])
        self.assertEqual(out.count("Unsupported status"), 2)
        self.assertEqual(status, "Needs Monitoring")
        status, _ = run(hht.ask_status, ["healthy"])      # capitals do not matter
        self.assertEqual(status, "Healthy")

    def test_empty_required_fields_rejected(self):
        value, out = run(hht.ask_required_text, ["", "   ", "Goat"], "Species: ", "Species")
        self.assertEqual(value, "Goat")
        self.assertEqual(out.count("cannot be empty"), 2)

    def test_11_unknown_animal_id(self):
        add(self.records, "AN-001", date(2026, 10, 1))
        for func in (hht.display_animal_history, hht.display_latest_status):
            _, out = run(func, ["AN-999"], self.records)
            self.assertIn("No animal with ID AN-999 was found", out)
        _, out = run(hht.display_animal_history, ["   "], self.records)
        self.assertIn("cannot be empty", out)

    def test_12_empty_record_list(self):
        for func, answers in ((hht.display_health_records, []),
                              (hht.display_animal_history, []),
                              (hht.display_latest_status, [])):
            _, out = run(func, answers, self.records)    # must not ask for input
            self.assertIn("No health records have been added yet", out)
