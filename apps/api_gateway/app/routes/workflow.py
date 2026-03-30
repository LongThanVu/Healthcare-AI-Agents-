from fastapi import APIRouter, Depends

from apps.api_gateway.app.services.orchestrator_client import OrchestratorClient
from shared.database.models import User
from shared.schemas.diagnosis import DiagnosisRequest
from shared.schemas.records import RecordSearchRequest, RecordSearchResponse
from shared.schemas.scheduling import BookingRequest, BookingResponse
from shared.security.dependencies import get_current_user

router = APIRouter(tags=["workflows"])
client = OrchestratorClient()


@router.post("/triage")
async def triage_patient(
    payload: DiagnosisRequest,
    _: User = Depends(get_current_user),
) -> dict:
    return await client.run_triage(payload)


@router.post("/appointments/book", response_model=BookingResponse)
async def book_appointment(
    payload: BookingRequest,
    _: User = Depends(get_current_user),
) -> BookingResponse:
    return await client.book_appointment(payload)


@router.post("/records/search", response_model=RecordSearchResponse)
async def search_records(
    payload: RecordSearchRequest,
    _: User = Depends(get_current_user),
) -> RecordSearchResponse:
    return await client.search_records(payload)
