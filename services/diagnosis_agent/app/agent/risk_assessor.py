from shared.core.constants import HIGH_RISK_KEYWORDS, MEDIUM_RISK_KEYWORDS


class RiskAssessor:
    def assess(self, symptoms: list[str]) -> str:
        joined = " ".join(symptoms)
        if any(keyword in joined for keyword in HIGH_RISK_KEYWORDS):
            return "high"
        if any(keyword in joined for keyword in MEDIUM_RISK_KEYWORDS):
            return "medium"
        return "low"
