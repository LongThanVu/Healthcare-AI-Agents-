from services.diagnosis_agent.app.services.diagnosis_service import DiagnosisService
from shared.schemas.diagnosis import DiagnosisRequest


def test_diagnosis_high_risk() -> None:
    service = DiagnosisService()
    result = service.diagnose(
        DiagnosisRequest(
            patient_name="Alice",
            age=44,
            symptoms=["chest pain", "shortness of breath"],
        )
    )
    assert result.urgency == "high"
