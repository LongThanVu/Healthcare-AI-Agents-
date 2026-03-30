from shared.schemas.diagnosis import DiagnosisRequest, DiagnosisResult
from services.diagnosis_agent.app.agent.recommendation_engine import RecommendationEngine
from services.diagnosis_agent.app.agent.risk_assessor import RiskAssessor
from services.diagnosis_agent.app.agent.symptom_analyzer import SymptomAnalyzer


class DiagnosisAgent:
    def __init__(self) -> None:
        self.risk_assessor = RiskAssessor()
        self.recommendation_engine = RecommendationEngine()

    def run(self, payload: DiagnosisRequest) -> DiagnosisResult:
        normalized_symptoms = SymptomAnalyzer.normalize(payload.symptoms)
        urgency = self.risk_assessor.assess(normalized_symptoms)
        condition = self._infer_condition(normalized_symptoms)
        confidence = self._estimate_confidence(normalized_symptoms, payload.existing_conditions)
        explanation = self._build_explanation(condition, urgency, payload)
        next_steps = self.recommendation_engine.generate(urgency)
        return DiagnosisResult(
            condition=condition,
            urgency=urgency,
            confidence=confidence,
            explanation=explanation,
            next_steps=next_steps,
        )

    @staticmethod
    def _infer_condition(symptoms: list[str]) -> str:
        joined = " ".join(symptoms)
        if "fever" in joined and "cough" in joined:
            return "Possible respiratory infection"
        if "chest pain" in joined:
            return "Possible cardiovascular or emergency condition"
        if "headache" in joined and "dizziness" in joined:
            return "Possible dehydration, migraine, or blood pressure issue"
        return "General symptom pattern requiring clinical review"

    @staticmethod
    def _estimate_confidence(symptoms: list[str], conditions: list[str]) -> float:
        base_score = 0.55 + min(len(symptoms) * 0.06, 0.25)
        if conditions:
            base_score += 0.05
        return round(min(base_score, 0.95), 2)

    @staticmethod
    def _build_explanation(condition: str, urgency: str, payload: DiagnosisRequest) -> str:
        symptom_summary = ", ".join(payload.symptoms) if payload.symptoms else "no symptoms provided"
        return (
            f"Based on the reported symptoms ({symptom_summary}) and any known medical background, "
            f"the system estimated '{condition}' with {urgency} urgency. "
            "This is a support recommendation and does not replace a licensed clinician."
        )
