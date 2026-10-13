"""Herd Health Tracker: beginner-level livestock health recordkeeping application."""

from .constants import APPROVED_STATUSES, MAX_AGE_MONTHS
from .models import HealthRecord, LivestockAnimal
from .services import (
    DEMO_DATA, add_record_to_list, find_animal, get_animal_summary, load_demo_data,
)
from .ui import (
    add_health_record, ask_age, ask_date, ask_existing_animal,
    ask_required_text, ask_status, display_animal_history,
    display_health_records, display_latest_status, display_menu, print_record,
)
from .main import main
from .utils.validation import normalise_status, parse_age, parse_date

__all__ = [
    "APPROVED_STATUSES", "MAX_AGE_MONTHS", "HealthRecord", "LivestockAnimal",
    "DEMO_DATA", "add_record_to_list", "find_animal", "get_animal_summary",
    "load_demo_data", "add_health_record", "ask_age", "ask_date",
    "ask_existing_animal", "ask_required_text", "ask_status",
    "display_animal_history", "display_health_records", "display_latest_status",
    "display_menu", "print_record", "main", "normalise_status", "parse_age",
    "parse_date",
]
