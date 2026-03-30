from uuid import uuid4

from services.scheduling_agent.app.agent.availability_checker import AvailabilityChecker
from services.scheduling_agent.app.agent.conflict_resolver import ConflictResolver
from services.scheduling_agent.app.agent.slot_optimizer import SlotOptimizer
from shared.schemas.scheduling import BookingRequest, BookingResponse


class BookingService:
    def __init__(self) -> None:
        self.availability_checker = AvailabilityChecker()

    def book(self, payload: BookingRequest) -> BookingResponse:
        slot = self.availability_checker.get_first_available(payload.department, payload.preferred_date)
        selected_slot = SlotOptimizer.prioritize(slot, payload.urgency)
        ConflictResolver.reserve(selected_slot)
        appointment_id = f"APT-{uuid4().hex[:8].upper()}"
        return BookingResponse(
            appointment_id=appointment_id,
            status="confirmed",
            slot=selected_slot,
            message=f"Appointment confirmed for {payload.patient_name}.",
        )
