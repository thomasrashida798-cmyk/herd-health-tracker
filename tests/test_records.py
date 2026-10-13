"""Automated tests for the layered Herd Health Tracker application."""

from datetime import date

import herd_health_tracker as hht
from herd_health_tracker_app.models import HealthRecord, LivestockAnimal
from support import TestBase, add, run


class TestAddAndDisplay(TestBase):
    FIRST = ["an-001", "Goat", "Unknown", "24", "2026-10-01",
             "No abnormal signs reported", "1", "None"]

    def test_01_add_valid_first_record(self):
        record, out = run(hht.add_health_record, self.FIRST, self.records)
        self.assertEqual(len(self.records), 1)
        self.assertEqual(record.animal.animal_id, "AN-001")
        self.assertEqual(record.animal.current_health_status, "Healthy")
        self.assertEqual(record.animal.last_health_record_date, date(2026, 10, 1))
        self.assertEqual(record.record_id, "HR-001")
        self.assertIn("saved", out)

    def test_02_second_record_same_animal(self):
        run(hht.add_health_record, self.FIRST, self.records)
        # existing animal: species/breed/age are NOT asked again
        second, out = run(hht.add_health_record,
                          ["AN-001", "2026-10-04", "Follow-up", "3", "None"], self.records)
        self.assertEqual(len(self.records), 2)
        self.assertIn("already registered", out)
        self.assertEqual(second.animal.current_health_status, "Veterinary Attention Required")

    def test_03_display_all_records(self):
        hht.load_demo_data(self.records)
        _, out = run(hht.display_health_records, [], self.records)
        for text in ("HR-001", "HR-002", "HR-003", "AN-001", "AN-002", "Sheep",
                     "Reduced appetite reported"):
            self.assertIn(text, out)

    def test_04_history_shows_all_records_oldest_first(self):
        hht.load_demo_data(self.records)
        _, out = run(hht.display_animal_history, ["an-001"], self.records)
        self.assertIn("HR-001", out)
        self.assertIn("HR-003", out)
        self.assertNotIn("HR-002", out)          # belongs to AN-002
        self.assertLess(out.index("2026-10-01"), out.index("2026-10-04"))
        self.assertIn("Number of records: 2", out)

    def test_05_latest_status(self):
        hht.load_demo_data(self.records)
        _, out = run(hht.display_latest_status, ["AN-001"], self.records)
        self.assertIn("Veterinary Attention Required", out)
        self.assertIn("2026-10-04", out)

    def test_06_older_record_after_newer_record(self):
        add(self.records, "AN-001", date(2026, 10, 4), "Veterinary Attention Required")
        _, updated = add(self.records, "AN-001", date(2026, 10, 1), "Healthy")
        animal = self.records[0].animal
        self.assertFalse(updated)
        self.assertEqual(animal.current_health_status, "Veterinary Attention Required")
        self.assertEqual(animal.last_health_record_date, date(2026, 10, 4))
        self.assertEqual(len(self.records), 2)    # older record still stored
        self.assertEqual(self.records[1].health_status, "Healthy")

    def test_06b_out_of_order_message_via_menu_function(self):
        add(self.records, "AN-001", date(2026, 10, 4), "Veterinary Attention Required")
        _, out = run(hht.add_health_record,
                     ["AN-001", "2026-10-01", "Earlier note", "1", "None"], self.records)
        self.assertIn("not newer", out)
