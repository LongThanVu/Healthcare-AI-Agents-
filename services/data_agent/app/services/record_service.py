from services.data_agent.app.agent.retrieval_engine import RetrievalEngine
from services.data_agent.app.agent.validation_engine import ValidationEngine
from services.data_agent.app.repositories.patient_repository import PatientRepository
from shared.schemas.records import PatientRecord, RecordSearchResponse


class RecordService:
    def __init__(self) -> None:
        self.repository = PatientRepository()
        self.retrieval_engine = RetrievalEngine()

    def search(self, query: str) -> RecordSearchResponse:
        results = [ValidationEngine.validate(record) for record in self.retrieval_engine.search(query)]
        return RecordSearchResponse(results=results)

    def get_by_id(self, patient_id: str) -> PatientRecord | None:
        record = self.repository.find_by_id(patient_id)
        if record is None:
            return None
        return ValidationEngine.validate(record)
