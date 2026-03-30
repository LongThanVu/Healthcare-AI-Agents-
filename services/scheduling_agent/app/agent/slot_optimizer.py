from shared.schemas.scheduling import AppointmentSlot


class SlotOptimizer:
    @staticmethod
    def prioritize(slot: AppointmentSlot, urgency: str) -> AppointmentSlot:
        return slot
