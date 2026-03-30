from shared.core.config import get_settings
from shared.schemas.diagnosis import DiagnosisRequest
from shared.schemas.records import RecordSearchRequest, RecordSearchResponse
from shared.schemas.scheduling import BookingRequest, BookingResponse
from shared.utils.http import build_client


class OrchestratorClient:
    def __init__(self) -> None:
        self.settings = get_settings()

    async def run_triage(self, payload: DiagnosisRequest) -> dict:
        async with build_client() as client:
            response = await client.post(f"{self.settings.orchestrator_url}/workflows/triage", json=payload.model_dump())
            response.raise_for_status()
            return response.json()

    async def book_appointment(self, payload: BookingRequest) -> BookingResponse:
        async with build_client() as client:
            response = await client.post(
                f"{self.settings.orchestrator_url}/workflows/appointments/book",
                json=payload.model_dump(),
            )
            response.raise_for_status()
            return BookingResponse.model_validate(response.json())

    async def search_records(self, payload: RecordSearchRequest) -> RecordSearchResponse:
        async with build_client() as client:
            response = await client.post(
                f"{self.settings.orchestrator_url}/workflows/records/search",
                json=payload.model_dump(),
            )
            response.raise_for_status()
            return RecordSearchResponse.model_validate(response.json())
