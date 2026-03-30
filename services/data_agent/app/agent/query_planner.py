class QueryPlanner:
    @staticmethod
    def normalize(query: str) -> str:
        return query.strip().lower()
