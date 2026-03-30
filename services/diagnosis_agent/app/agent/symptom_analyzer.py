from collections.abc import Iterable


class SymptomAnalyzer:
    @staticmethod
    def normalize(symptoms: Iterable[str]) -> list[str]:
        return [symptom.strip().lower() for symptom in symptoms if symptom.strip()]
