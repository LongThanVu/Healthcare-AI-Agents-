from services.scheduling_agent.app.services.booking_service import BookingService
from shared.schemas.scheduling import BookingRequest


def test_booking_returns_confirmation() -> None:
    service = BookingService()
    response = service.book(
        BookingRequest(
            patient_id="P-1001",
            patient_name="John Doe",
            department="general-medicine",
            preferred_date="2026-04-03",
        )
    )
    assert response.status == "confirmed"
    assert response.appointment_id.startswith("APT-")
