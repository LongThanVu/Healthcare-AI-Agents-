from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.scheduling_agent.app.services.booking_service import BookingService
from shared.database.session import get_db
from shared.schemas.scheduling import BookingRequest, BookingResponse

router = APIRouter(tags=["appointments"])


@router.post("/appointments/book", response_model=BookingResponse)
async def book_appointment(
    payload: BookingRequest,
    db: AsyncSession = Depends(get_db),
) -> BookingResponse:
    return await BookingService(db).book(payload)
