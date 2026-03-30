from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shared.database.models import Patient
from shared.schemas.records import PatientRecord


class PatientRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def find_all(self) -> list[PatientRecord]:
        rows = await self.db.scalars(select(Patient).order_by(Patient.full_name))
        return [self._to_schema(patient) for patient in rows.all()]

    async def find_by_id(self, patient_id: str) -> PatientRecord | None:
        patient = await self.db.get(Patient, patient_id)
        if patient is None:
            return None
        return self._to_schema(patient)

    @staticmethod
    def _to_schema(patient: Patient) -> PatientRecord:
        return PatientRecord(
            patient_id=patient.patient_id,
            full_name=patient.full_name,
            age=patient.age,
            gender=patient.gender,
            allergies=patient.allergies or [],
            chronic_conditions=patient.chronic_conditions or [],
            last_visit=patient.last_visit,
            notes=patient.notes,
        )
