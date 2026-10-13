"""Console prompts and validation-aware input helpers."""

from ..constants import MAX_AGE_MONTHS, APPROVED_STATUSES
from ..models import HealthRecord
from ..services.record_service import find_animal
from ..utils.validation import normalise_status, parse_age, parse_date


def ask_required_text(prompt, field_name):
    """Keep asking until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(field_name + " cannot be empty. Please try again.")


def ask_age():
    while True:
        age = parse_age(input("Age in months (whole number, for example 24): "))
        if age is not None:
            return age
        print(
            "Invalid age. Please enter a whole number of months from 0 to "
            + str(MAX_AGE_MONTHS)
            + ", such as 24."
        )


def ask_date():
    while True:
        date_checked = parse_date(
            input("Date checked (YYYY-MM-DD, for example 2026-10-01): ")
        )
        if date_checked is not None:
            return date_checked
        print("Invalid date. Use the format YYYY-MM-DD and a real calendar date.")


def ask_status():
    print("Health status options:")
    for number, status in enumerate(APPROVED_STATUSES, start=1):
        print("  " + str(number) + ". " + status)
    while True:
        status = normalise_status(
            input("Enter 1, 2 or 3, or type the status name: ")
        )
        if HealthRecord.is_valid_health_status(status):
            return status
        print("Unsupported status. Please choose one of the three options listed.")


def ask_existing_animal(health_records):
    """Ask for an animal ID and return its object, or None with a message."""
    if not health_records:
        print("\nNo health records have been added yet. Choose option 1 to add one.")
        return None
    animal_id = input("Enter the animal ID (for example AN-001): ").strip().upper()
    if not animal_id:
        print("Animal ID cannot be empty.")
        return None
    animal = find_animal(health_records, animal_id)
    if animal is None:
        print("No animal with ID " + animal_id + " was found.")
    return animal
