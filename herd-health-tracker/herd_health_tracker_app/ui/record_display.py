"""Console presentation functions for stored health records."""

from ..models import HealthRecord
from ..services.record_service import get_animal_summary
from .input_helpers import ask_existing_animal


def print_record(record):
    print("Record ID      : " + record.record_id)
    print("Animal ID      : " + record.animal.animal_id)
    print("Species        : " + record.animal.species)
    print("Date checked   : " + str(record.date_checked))
    print("Observed signs : " + record.observed_signs)
    print("Health status  : " + record.health_status)
    print("Notes          : " + record.notes)
    print("-" * 40)


def display_health_records(health_records):
    """Display all stored records in the order they were entered."""
    if not health_records:
        print("\nNo health records have been added yet. Choose option 1 to add one.")
        return
    print("\n--- All health records (in the order entered) ---")
    for record in health_records:
        print_record(record)
    print(
        "Total health records created this session: "
        + str(HealthRecord.get_total_records())
    )


def display_animal_history(health_records):
    """Display all records for one animal, oldest date first."""
    animal = ask_existing_animal(health_records)
    if animal is None:
        return
    history = [record for record in health_records if record.animal is animal]
    history.sort(key=lambda record: record.date_checked)
    print("\n--- Health history for " + animal.animal_id + " (oldest date first) ---")
    print(
        "Species: " + animal.species + " | Breed: " + animal.breed
        + " | Age when first recorded: " + str(animal.age_months) + " months"
    )
    print("-" * 40)
    for record in history:
        print_record(record)
    print("Number of records: " + str(len(history)))


def display_latest_status(health_records):
    """Display an animal's latest status, selected by record date."""
    animal = ask_existing_animal(health_records)
    if animal is None:
        return
    animal_id, status, record_count = get_animal_summary(
        health_records, animal.animal_id
    )
    print("\nLatest recorded status for " + animal_id + ": " + status)
    print("Based on the record dated: " + str(animal.last_health_record_date))
    print("Records on file for this animal: " + str(record_count))
