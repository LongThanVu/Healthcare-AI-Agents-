from services.scheduling_agent.app.services.schedule_store import AVAILABLE_SLOTS
from shared.schemas.scheduling import AppointmentSlot


class AvailabilityChecker:
    def get_first_available(self, department: str, preferred_date: str) -> AppointmentSlot:
        for slot in AVAILABLE_SLOTS:
            if slot.department == department and slot.start_time.startswith(preferred_date) and slot.available:
                return slot
        for slot in AVAILABLE_SLOTS:
            if slot.department == department and slot.available:
                return slot
        raise ValueError(f"No available slots for department={department}")
