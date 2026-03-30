from services.data_agent.app.agent.query_planner import QueryPlanner
from services.data_agent.app.repositories.patient_repository import PatientRepository
from shared.schemas.records import PatientRecord


class RetrievalEngine:
    def __init__(self) -> None:
        self.repository = PatientRepository()

    def search(self, query: str) -> list[PatientRecord]:
        normalized = QueryPlanner.normalize(query)
        results: list[PatientRecord] = []
        for patient in self.repository.find_all():
            blob = " ".join(
                [
                    patient.patient_id,
                    patient.full_name,
                    patient.gender,
                    " ".join(patient.allergies),
                    " ".join(patient.chronic_conditions),
                    patient.notes or "",
                ]
            ).lower()
            if normalized in blob:
                results.append(patient)
        return results
