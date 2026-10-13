"""Shared helpers for the automated test suite."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import herd_health_tracker as hht
from herd_health_tracker_app.models import HealthRecord, LivestockAnimal


def run(func, answers, *args):
    """Call func(*args) with scripted input; return result and captured output."""
    buffer = io.StringIO()
    with patch("builtins.input", side_effect=answers), redirect_stdout(buffer):
        result = func(*args)
    return result, buffer.getvalue()


def add(records, animal_id, day, status="Healthy", species="Goat"):
    """Add a test record without requiring keyboard input."""
    return hht.add_record_to_list(
        records, animal_id, species, "Unknown", 12, day, "Test signs", status, "None"
    )


class TestBase(unittest.TestCase):
    def setUp(self):
        HealthRecord.total_records = 0  # Isolate the class-level counter per test.
        self.records = []
