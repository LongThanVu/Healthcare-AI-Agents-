class RecommendationEngine:
    def generate(self, urgency: str) -> list[str]:
        if urgency == "high":
            return [
                "Seek urgent medical evaluation immediately.",
                "Do not delay care if symptoms worsen.",
            ]
        if urgency == "medium":
            return [
                "Book a doctor appointment within 1-2 days.",
                "Track temperature, pain level, and symptom duration.",
            ]
        return [
            "Rest, hydrate, and monitor symptoms.",
            "Consult a doctor if symptoms persist or intensify.",
        ]
