from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shared.database.models import Appointment


class AppointmentRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_booked_slot_starts(self, *, department: str, preferred_date: str) -> set[str]:
        rows = await self.db.scalars(
            select(Appointment.slot_start).where(
                Appointment.department == department,
                Appointment.slot_start.startswith(preferred_date),
                Appointment.status == "confirmed",
            )
        )
        return set(rows.all())

    async def create(self, appointment: Appointment) -> Appointment:
        self.db.add(appointment)
        await self.db.commit()
        await self.db.refresh(appointment)
        return appointment
