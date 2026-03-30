from fastapi import APIRouter

from apps.orchestrator.app.services.workflow_service import WorkflowService
from shared.schemas.diagnosis import DiagnosisRequest
from shared.schemas.records import RecordSearchRequest, RecordSearchResponse
from shared.schemas.scheduling import BookingRequest, BookingResponse

router = APIRouter(prefix="/workflows", tags=["workflows"])
service = WorkflowService()


@router.post("/triage")
async def triage(payload: DiagnosisRequest) -> dict:
    return await service.run_triage(payload)


@router.post("/appointments/book", response_model=BookingResponse)
async def book(payload: BookingRequest) -> BookingResponse:
    return await service.book_appointment(payload)


@router.post("/records/search", response_model=RecordSearchResponse)
async def search(payload: RecordSearchRequest) -> RecordSearchResponse:
    return await service.search_records(payload)
