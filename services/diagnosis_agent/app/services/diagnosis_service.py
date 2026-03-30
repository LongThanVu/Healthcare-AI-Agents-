from services.diagnosis_agent.app.agent.diagnosis_agent import DiagnosisAgent
from shared.schemas.diagnosis import DiagnosisRequest, DiagnosisResult


class DiagnosisService:
    def __init__(self) -> None:
        self.agent = DiagnosisAgent()

    def diagnose(self, payload: DiagnosisRequest) -> DiagnosisResult:
        return self.agent.run(payload)
