from services.data_agent.app.services.record_service import RecordService


def test_record_search_returns_patient() -> None:
    service = RecordService()
    result = service.search("hypertension")
    assert len(result.results) >= 1
