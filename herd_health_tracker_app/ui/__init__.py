"""Console user-interface functions."""

from .input_helpers import (
    ask_age, ask_date, ask_existing_animal, ask_required_text, ask_status,
)
from .menu import display_menu
from .record_display import (
    display_animal_history, display_health_records, display_latest_status,
    print_record,
)
from .record_entry import add_health_record

__all__ = [
    "ask_age", "ask_date", "ask_existing_animal", "ask_required_text",
    "ask_status", "display_menu", "display_animal_history",
    "display_health_records", "display_latest_status", "print_record",
    "add_health_record",
]
