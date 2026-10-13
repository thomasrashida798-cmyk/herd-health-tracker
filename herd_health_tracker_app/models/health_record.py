"""Domain model for a single animal health observation."""

from ..constants import APPROVED_STATUSES
from .livestock_animal import LivestockAnimal


class HealthRecord:
    """One health observation for one animal."""

    APPROVED_STATUSES = APPROVED_STATUSES

    # Counts objects created during this program session; no persistence is used.
    total_records = 0

    def __init__(self, record_id, animal, date_checked, observed_signs, health_status, notes):
        if not isinstance(animal, LivestockAnimal):
            raise TypeError("animal must be a LivestockAnimal object")
        if not self.is_valid_health_status(health_status):
            raise ValueError("Unsupported health status: " + str(health_status))
        self.record_id = record_id
        self.animal = animal  # Reference to the animal object, not a copied ID.
        self.date_checked = date_checked
        self.observed_signs = observed_signs
        self.health_status = health_status
        self.notes = notes
        HealthRecord.total_records += 1

    @classmethod
    def get_total_records(cls):
        """Return the number of HealthRecord objects created during this run."""
        return cls.total_records

    @staticmethod
    def is_valid_health_status(status):
        """Return True only for the three approved status values."""
        return status in HealthRecord.APPROVED_STATUSES
