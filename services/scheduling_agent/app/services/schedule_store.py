from shared.schemas.scheduling import AppointmentSlot

AVAILABLE_SLOTS = [
    AppointmentSlot(
        doctor_name="Dr. Emily Carter",
        department="general-medicine",
        start_time="2026-04-03T09:00:00",
        end_time="2026-04-03T09:30:00",
        available=True,
    ),
    AppointmentSlot(
        doctor_name="Dr. Daniel Kim",
        department="general-medicine",
        start_time="2026-04-03T10:00:00",
        end_time="2026-04-03T10:30:00",
        available=True,
    ),
    AppointmentSlot(
        doctor_name="Dr. Sarah Nguyen",
        department="cardiology",
        start_time="2026-04-03T11:00:00",
        end_time="2026-04-03T11:30:00",
        available=True,
    ),
]


def mark_slot_unavailable(target: AppointmentSlot) -> None:
    for slot in AVAILABLE_SLOTS:
        if (
            slot.doctor_name == target.doctor_name
            and slot.start_time == target.start_time
            and slot.department == target.department
        ):
            slot.available = False
            return
