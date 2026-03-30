from fastapi import APIRouter

from services.scheduling_agent.app.services.booking_service import BookingService
from shared.schemas.scheduling import BookingRequest, BookingResponse

router = APIRouter(tags=["appointments"])
service = BookingService()


@router.post("/appointments/book", response_model=BookingResponse)
async def book_appointment(payload: BookingRequest) -> BookingResponse:
    return service.book(payload)
