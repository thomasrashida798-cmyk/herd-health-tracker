"""Application services that operate on health-record data."""

from .demo_data import DEMO_DATA, load_demo_data
from .record_service import add_record_to_list, find_animal, get_animal_summary

__all__ = [
    "DEMO_DATA", "load_demo_data", "add_record_to_list", "find_animal",
    "get_animal_summary",
]
