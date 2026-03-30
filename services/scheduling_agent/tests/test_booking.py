import asyncio

from shared.database.session import get_session_factory, init_db
from services.scheduling_agent.app.services.booking_service import BookingService
from shared.schemas.scheduling import BookingRequest


async def _run_booking_test() -> None:
    await init_db()
    async with get_session_factory()() as session:
        service = BookingService(session)
        response = await service.book(
            BookingRequest(
                patient_id="P-1001",
                patient_name="John Doe",
                department="general-medicine",
                preferred_date="2026-04-03",
            )
        )
    assert response.status == "confirmed"
    assert response.appointment_id.startswith("APT-")


def test_booking_returns_confirmation() -> None:
    asyncio.run(_run_booking_test())
