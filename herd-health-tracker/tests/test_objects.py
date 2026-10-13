"""Automated tests for the layered Herd Health Tracker application."""

from datetime import date

import herd_health_tracker as hht
from herd_health_tracker_app.models import HealthRecord, LivestockAnimal
from support import TestBase, add, run


class TestObjectsAndStorage(TestBase):
    def test_13_same_animal_object_reused(self):
        hht.load_demo_data(self.records)
        self.assertIs(self.records[0].animal, self.records[2].animal)
        self.assertIsNot(self.records[0].animal, self.records[1].animal)
        self.assertIsInstance(self.records[0].animal, LivestockAnimal)

    def test_14_historical_status_preserved(self):
        hht.load_demo_data(self.records)
        self.assertEqual(self.records[0].health_status, "Healthy")
        self.assertEqual(self.records[2].health_status, "Veterinary Attention Required")
        self.assertEqual(self.records[0].animal.current_health_status,
                         "Veterinary Attention Required")

    def test_18_duplicate_animal_ids(self):
        add(self.records, "AN-001", date(2026, 10, 1))
        add(self.records, "AN-001", date(2026, 10, 2))
        run(hht.add_health_record, ["an-001", "2026-10-03", "x", "1", "None"], self.records)
        animals = {id(record.animal) for record in self.records}
        self.assertEqual(len(self.records), 3)
        self.assertEqual(len(animals), 1)

    def test_20_one_primary_list_only(self):
        hht.load_demo_data(self.records)
        self.assertIsInstance(self.records, list)
        self.assertTrue(all(isinstance(r, HealthRecord) for r in self.records))
        self.assertGreater(len(self.records), 1)
        # no module-level list or dict that could act as a second store
        stores = [n for n, v in vars(hht).items()
                  if not n.startswith("__") and isinstance(v, (list, dict))]
        self.assertEqual(stores, [])
        # LivestockAnimal keeps no list/dict of records either
        animal = self.records[0].animal
        self.assertEqual([n for n, v in vars(animal).items() if isinstance(v, (list, dict))], [])


class TestMethods(TestBase):
    def test_15_instance_method(self):
        animal = LivestockAnimal("AN-001", "Goat", "Unknown", 12)
        self.assertIsNone(animal.current_health_status)
        self.assertTrue(animal.update_health_status("Healthy", date(2026, 10, 1)))   # first
        self.assertEqual(animal.last_health_record_date, date(2026, 10, 1))
        self.assertTrue(animal.update_health_status("Needs Monitoring", date(2026, 10, 3)))
        self.assertFalse(animal.update_health_status("Healthy", date(2026, 10, 2)))   # older
        self.assertFalse(animal.update_health_status("Healthy", date(2026, 10, 3)))   # same day
        self.assertEqual(animal.current_health_status, "Needs Monitoring")
        with self.assertRaises(ValueError):
            animal.update_health_status("Sick", date(2026, 10, 9))
        self.assertEqual(animal.current_health_status, "Needs Monitoring")

    def test_16_class_method(self):
        self.assertIsInstance(HealthRecord.__dict__["get_total_records"], classmethod)
        self.assertEqual(HealthRecord.get_total_records(), 0)
        animal = LivestockAnimal("AN-001", "Goat", "Unknown", 12)
        HealthRecord("HR-001", animal, date(2026, 10, 1), "a", "Healthy", "None")
        HealthRecord("HR-002", animal, date(2026, 10, 2), "b", "Healthy", "None")
        self.assertEqual(HealthRecord.get_total_records(), 2)
        with self.assertRaises(ValueError):                  # failed creation: not counted
            HealthRecord("HR-003", animal, date(2026, 10, 3), "c", "Sick", "None")
        with self.assertRaises(TypeError):
            HealthRecord("HR-004", "AN-001", date(2026, 10, 3), "c", "Healthy", "None")
        self.assertEqual(HealthRecord.get_total_records(), 2)
        hht.load_demo_data(self.records)
        self.assertEqual(HealthRecord.get_total_records(), 5)

    def test_17_static_method(self):
        self.assertIsInstance(HealthRecord.__dict__["is_valid_health_status"], staticmethod)
        for good in ("Healthy", "Needs Monitoring", "Veterinary Attention Required"):
            self.assertTrue(HealthRecord.is_valid_health_status(good))
        for bad in ("healthy", "Sick", "", None, 1, "Healthy "):
            self.assertFalse(HealthRecord.is_valid_health_status(bad))

    def test_record_holds_animal_object_not_a_string(self):
        record, _ = add(self.records, "AN-001", date(2026, 10, 1))
        self.assertIsInstance(record.animal, LivestockAnimal)
        self.assertEqual(record.animal.animal_id, "AN-001")
