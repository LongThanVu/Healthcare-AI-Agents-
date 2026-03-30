from apps.orchestrator.app.services.agent_clients import AgentClients
from shared.schemas.diagnosis import DiagnosisRequest
from shared.schemas.records import RecordSearchRequest, RecordSearchResponse
from shared.schemas.scheduling import BookingRequest, BookingResponse


class WorkflowService:
    def __init__(self) -> None:
        self.clients = AgentClients()

    async def run_triage(self, payload: DiagnosisRequest) -> dict:
        patient_record = None
        if payload.patient_id:
            patient_record = await self.clients.get_patient_summary(payload.patient_id)

        diagnosis = await self.clients.diagnose(payload, patient_record)

        return {
            "patient": {
                "patient_id": payload.patient_id,
                "patient_name": payload.patient_name,
                "age": payload.age,
            },
            "record_context": patient_record.model_dump() if patient_record else None,
            "diagnosis": diagnosis.model_dump(),
            "suggested_action": self._suggest_action(diagnosis.urgency),
        }

    async def book_appointment(self, payload: BookingRequest) -> BookingResponse:
        return await self.clients.book_appointment(payload)

    async def search_records(self, payload: RecordSearchRequest) -> RecordSearchResponse:
        return await self.clients.search_records(payload)

    @staticmethod
    def _suggest_action(urgency: str) -> str:
        if urgency == "high":
            return "Immediate medical attention recommended."
        if urgency == "medium":
            return "Schedule an appointment within 24-48 hours."
        return "Self-monitor and follow up if symptoms persist."
