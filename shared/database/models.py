from __future__ import annotations

from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from shared.database.base import Base


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255))
    password_hash: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


class Patient(TimestampMixin, Base):
    __tablename__ = "patients"

    patient_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    full_name: Mapped[str] = mapped_column(String(255), index=True)
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(20))
    allergies: Mapped[list[str]] = mapped_column(JSON, default=list)
    chronic_conditions: Mapped[list[str]] = mapped_column(JSON, default=list)
    last_visit: Mapped[str] = mapped_column(String(50))
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)


class Appointment(TimestampMixin, Base):
    __tablename__ = "appointments"

    appointment_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    patient_id: Mapped[str] = mapped_column(String(50), index=True)
    patient_name: Mapped[str] = mapped_column(String(255))
    department: Mapped[str] = mapped_column(String(100), index=True)
    urgency: Mapped[str] = mapped_column(String(20), default="medium")
    doctor_name: Mapped[str] = mapped_column(String(255))
    slot_start: Mapped[str] = mapped_column(String(50), index=True)
    slot_end: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(30), default="confirmed")
    created_by_user_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
