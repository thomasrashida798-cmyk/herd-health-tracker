"""Fictional demonstration records for teaching and screenshots."""

from ..services.record_service import add_record_to_list
from ..utils.validation import parse_date

# Fields: animal_id, species, breed, age_months, date, signs, status, notes.
# These are fictional seed values, not real livestock observations.
DEMO_DATA = (
    ("AN-001", "Goat", "West African Dwarf", 24, "2026-10-01",
     "No abnormal signs reported", "Healthy", "Fictional demonstration record"),
    ("AN-002", "Sheep", "Djallonke", 18, "2026-10-02",
     "Reduced appetite reported", "Needs Monitoring", "Fictional demonstration record"),
    ("AN-001", "Goat", "West African Dwarf", 24, "2026-10-04",
     "Follow-up observation recorded", "Veterinary Attention Required",
     "Fictional demonstration record"),
)


def load_demo_data(health_records):
    """Add the fictional demonstration records through normal record logic."""
    for (animal_id, species, breed, age, date_text, signs, status, notes) in DEMO_DATA:
        add_record_to_list(
            health_records,
            animal_id,
            species,
            breed,
            age,
            parse_date(date_text),
            signs,
            status,
            notes,
        )
