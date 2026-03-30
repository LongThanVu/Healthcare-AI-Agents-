from services.scheduling_agent.app.services.schedule_store import mark_slot_unavailable
from shared.schemas.scheduling import AppointmentSlot


class ConflictResolver:
    @staticmethod
    def reserve(slot: AppointmentSlot) -> None:
        mark_slot_unavailable(slot)
