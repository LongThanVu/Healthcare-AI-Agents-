from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shared.core.config import get_settings
from shared.database.models import Patient, User
from shared.security.passwords import hash_password


async def seed_reference_data(session: AsyncSession) -> None:
    await _seed_default_admin(session)
    await _seed_patients(session)


async def _seed_default_admin(session: AsyncSession) -> None:
    settings = get_settings()
    existing_user = await session.scalar(select(User).where(User.email == settings.default_admin_email))
    if existing_user is not None:
        return

    session.add(
        User(
            email=settings.default_admin_email,
            full_name=settings.default_admin_full_name,
            password_hash=hash_password(settings.default_admin_password),
        )
    )
    await session.commit()


async def _seed_patients(session: AsyncSession) -> None:
    existing_patient = await session.scalar(select(Patient.patient_id).limit(1))
    if existing_patient is not None:
        return

    session.add_all(
        [
            Patient(
                patient_id="P-1001",
                full_name="John Doe",
                age=37,
                gender="male",
                allergies=["penicillin"],
                chronic_conditions=["hypertension"],
                last_visit="2026-03-25",
                notes="Monitor blood pressure and sleep quality.",
            ),
            Patient(
                patient_id="P-1002",
                full_name="Maria Lopez",
                age=29,
                gender="female",
                allergies=[],
                chronic_conditions=["asthma"],
                last_visit="2026-03-18",
                notes="Asthma inhaler prescription renewed.",
            ),
        ]
    )
    await session.commit()
