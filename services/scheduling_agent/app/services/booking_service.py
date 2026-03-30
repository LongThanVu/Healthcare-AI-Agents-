from __future__ import annotations

from uuid import uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from services.scheduling_agent.app.repositories.appointment_repository import AppointmentRepository
from services.scheduling_agent.app.services.schedule_store import AVAILABLE_SLOTS
from shared.database.models import Appointment
from shared.schemas.scheduling import AppointmentSlot, BookingRequest, BookingResponse


class BookingService:
    def __init__(self, db: AsyncSession) -> None:
        self.repository = AppointmentRepository(db)

    async def book(self, payload: BookingRequest) -> BookingResponse:
        booked_slot_starts = await self.repository.get_booked_slot_starts(
            department=payload.department,
            preferred_date=payload.preferred_date,
        )
        selected_slot = self._pick_slot(payload.department, payload.preferred_date, booked_slot_starts)

        appointment = await self.repository.create(
            Appointment(
                appointment_id=f"APT-{uuid4().hex[:8].upper()}",
                patient_id=payload.patient_id,
                patient_name=payload.patient_name,
                department=selected_slot.department,
                urgency=payload.urgency,
                doctor_name=selected_slot.doctor_name,
                slot_start=selected_slot.start_time,
                slot_end=selected_slot.end_time,
                status="confirmed",
            )
        )

        return BookingResponse(
            appointment_id=appointment.appointment_id,
            status=appointment.status,
            slot=selected_slot,
            message=f"Appointment confirmed for {payload.patient_name}.",
        )

    @staticmethod
    def _pick_slot(department: str, preferred_date: str, booked_slot_starts: set[str]) -> AppointmentSlot:
        same_day_candidates = [
            slot
            for slot in AVAILABLE_SLOTS
            if slot.department == department and slot.start_time.startswith(preferred_date)
        ]
        fallback_candidates = [slot for slot in AVAILABLE_SLOTS if slot.department == department]

        for candidate in same_day_candidates + fallback_candidates:
            if candidate.start_time not in booked_slot_starts:
                return candidate

        raise ValueError(f"No available slots for department={department}")
