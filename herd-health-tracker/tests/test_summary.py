"""Automated tests for the layered Herd Health Tracker application."""

from datetime import date

import herd_health_tracker as hht
from herd_health_tracker_app.models import HealthRecord, LivestockAnimal
from support import TestBase, add, run


class TestTupleSummary(TestBase):
    """Optional tuple bonus: read-only summary built from the one list."""

    def test_summary_tuple_values(self):
        hht.load_demo_data(self.records)
        summary = hht.get_animal_summary(self.records, "AN-001")
        self.assertIsInstance(summary, tuple)
        self.assertEqual(summary, ("AN-001", "Veterinary Attention Required", 2))
        self.assertEqual(hht.get_animal_summary(self.records, "AN-002"),
                         ("AN-002", "Needs Monitoring", 1))

    def test_summary_unknown_animal_and_empty_list(self):
        self.assertIsNone(hht.get_animal_summary(self.records, "AN-001"))
        hht.load_demo_data(self.records)
        self.assertIsNone(hht.get_animal_summary(self.records, "AN-404"))

    def test_summary_is_read_only_and_creates_no_storage(self):
        hht.load_demo_data(self.records)
        before = len(self.records)
        summary = hht.get_animal_summary(self.records, "AN-001")
        with self.assertRaises(TypeError):
            summary[1] = "Healthy"                      # tuples cannot be changed
        self.assertEqual(len(self.records), before)
        self.assertEqual(self.records[0].animal.current_health_status,
                         "Veterinary Attention Required")

    def test_latest_status_screen_shows_record_count(self):
        hht.load_demo_data(self.records)
        _, out = run(hht.display_latest_status, ["AN-001"], self.records)
        self.assertIn("Records on file for this animal: 2", out)
