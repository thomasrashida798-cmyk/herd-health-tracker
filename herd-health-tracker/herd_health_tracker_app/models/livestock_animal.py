"""Domain model for an individual livestock animal."""



class LivestockAnimal:
    """One individual animal, identified by its animal_id."""

    def __init__(self, animal_id, species, breed, age_months):
        self.animal_id = animal_id
        self.species = species
        self.breed = breed
        self.age_months = age_months
        self.current_health_status = None  # Set by the first valid health record.
        self.last_health_record_date = None  # Date of the newest-dated record.

    def update_health_status(self, new_status, record_date):
        """Update status only for a newer date; return True if an update occurs."""
        from .health_record import HealthRecord

        if not HealthRecord.is_valid_health_status(new_status):
            raise ValueError("Unsupported health status: " + str(new_status))
        if (
            self.last_health_record_date is None
            or record_date > self.last_health_record_date
        ):
            self.current_health_status = new_status
            self.last_health_record_date = record_date
            return True
        return False
