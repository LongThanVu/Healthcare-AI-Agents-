from fastapi import APIRouter

from apps.api_gateway.app.services.orchestrator_client import OrchestratorClient
from shared.schemas.diagnosis import DiagnosisRequest
from shared.schemas.records import RecordSearchRequest, RecordSearchResponse
from shared.schemas.scheduling import BookingRequest, BookingResponse

router = APIRouter(tags=["workflows"])
client = OrchestratorClient()


@router.post("/triage")
async def triage_patient(payload: DiagnosisRequest) -> dict:
    return await client.run_triage(payload)


@router.post("/appointments/book", response_model=BookingResponse)
async def book_appointment(payload: BookingRequest) -> BookingResponse:
    return await client.book_appointment(payload)


@router.post("/records/search", response_model=RecordSearchResponse)
async def search_records(payload: RecordSearchRequest) -> RecordSearchResponse:
    return await client.search_records(payload)
