from shared.core.config import get_settings
from shared.schemas.diagnosis import DiagnosisRequest, DiagnosisResult
from shared.schemas.records import PatientRecord, RecordSearchRequest, RecordSearchResponse
from shared.schemas.scheduling import BookingRequest, BookingResponse
from shared.utils.http import build_client


class AgentClients:
    def __init__(self) -> None:
        self.settings = get_settings()

    async def diagnose(self, payload: DiagnosisRequest, patient_record: PatientRecord | None = None) -> DiagnosisResult:
        request_body = payload.model_dump()
        if patient_record is not None:
            request_body["existing_conditions"] = patient_record.chronic_conditions
            if patient_record.notes:
                note_prefix = request_body.get("notes") or ""
                request_body["notes"] = (
                    f"{note_prefix}\nPatient record note: {patient_record.notes}".strip()
                )
        async with build_client() as client:
            response = await client.post(f"{self.settings.diagnosis_agent_url}/diagnose", json=request_body)
            response.raise_for_status()
            return DiagnosisResult.model_validate(response.json())

    async def search_records(self, payload: RecordSearchRequest) -> RecordSearchResponse:
        async with build_client() as client:
            response = await client.post(f"{self.settings.data_agent_url}/records/search", json=payload.model_dump())
            response.raise_for_status()
            return RecordSearchResponse.model_validate(response.json())

    async def get_patient_summary(self, patient_id: str) -> PatientRecord | None:
        async with build_client() as client:
            response = await client.get(f"{self.settings.data_agent_url}/records/summary/{patient_id}")
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return PatientRecord.model_validate(response.json())

    async def book_appointment(self, payload: BookingRequest) -> BookingResponse:
        async with build_client() as client:
            response = await client.post(f"{self.settings.scheduling_agent_url}/appointments/book", json=payload.model_dump())
            response.raise_for_status()
            return BookingResponse.model_validate(response.json())
