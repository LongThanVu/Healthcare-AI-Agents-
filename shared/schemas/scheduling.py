from pydantic import BaseModel, Field


class BookingRequest(BaseModel):
    patient_id: str
    patient_name: str
    department: str = Field(..., examples=["general-medicine"])
    preferred_date: str = Field(..., examples=["2026-04-03"])
    urgency: str = Field(default="medium", examples=["low", "medium", "high"])


class AppointmentSlot(BaseModel):
    doctor_name: str
    department: str
    start_time: str
    end_time: str
    available: bool = True


class BookingResponse(BaseModel):
    appointment_id: str
    status: str
    slot: AppointmentSlot
    message: str
