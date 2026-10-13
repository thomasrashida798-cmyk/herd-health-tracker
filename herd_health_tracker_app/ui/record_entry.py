"""Interactive console workflow for creating a health record."""

from ..services.record_service import add_record_to_list, find_animal
from .input_helpers import ask_age, ask_date, ask_required_text, ask_status


def add_health_record(health_records):
    """Ask the user for a health record and add it to the primary list."""
    print("\n--- Add a health record ---")
    animal_id = ask_required_text(
        "Animal ID (for example AN-001): ", "Animal ID"
    ).upper()
    animal = find_animal(health_records, animal_id)
    if animal is not None:
        print(
            "Animal " + animal_id + " is already registered (" + animal.species
            + "). A new health record will be added for this animal."
        )
        species, breed, age_months = animal.species, animal.breed, animal.age_months
    else:
        species = ask_required_text("Species (for example Goat): ", "Species")
        breed = ask_required_text("Breed (type Unknown if not known): ", "Breed")
        age_months = ask_age()

    date_checked = ask_date()
    observed_signs = ask_required_text(
        "Observed signs (describe what you saw): ", "Observed signs"
    )
    health_status = ask_status()
    notes = ask_required_text("Notes (type None if there are no notes): ", "Notes")

    record, status_updated = add_record_to_list(
        health_records,
        animal_id,
        species,
        breed,
        age_months,
        date_checked,
        observed_signs,
        health_status,
        notes,
    )
    print("Record " + record.record_id + " saved for animal " + animal_id + ".")
    if status_updated:
        print(
            "The current recorded status of " + animal_id + " is now: " + health_status
        )
    else:
        print(
            "This record is not newer than the latest record ("
            + str(record.animal.last_health_record_date)
            + "), so the current status stays: "
            + record.animal.current_health_status
        )
    return record
