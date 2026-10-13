"""Non-interactive operations on the primary health-record list."""

from ..models import HealthRecord, LivestockAnimal


def find_animal(health_records, animal_id):
    """Search health_records for an animal ID and return its object or None."""
    for record in health_records:
        if record.animal.animal_id == animal_id:
            return record.animal
    return None


def get_animal_summary(health_records, animal_id):
    """Return (animal_id, current_status, record_count), or None if not found.

    The tuple is constructed on demand and is not stored as another collection.
    """
    animal = find_animal(health_records, animal_id)
    if animal is None:
        return None
    record_count = sum(1 for record in health_records if record.animal is animal)
    return (animal.animal_id, animal.current_health_status, record_count)


def add_record_to_list(
    health_records,
    animal_id,
    species,
    breed,
    age_months,
    date_checked,
    observed_signs,
    health_status,
    notes,
):
    """Create and append a record, reusing an existing animal object when possible.

    Returns a pair: (the new record, whether its date updated current status).
    """
    animal = find_animal(health_records, animal_id)
    if animal is None:
        animal = LivestockAnimal(animal_id, species, breed, age_months)
    record_id = "HR-" + str(len(health_records) + 1).zfill(3)
    record = HealthRecord(
        record_id, animal, date_checked, observed_signs, health_status, notes
    )
    health_records.append(record)
    status_updated = animal.update_health_status(health_status, date_checked)
    return record, status_updated
