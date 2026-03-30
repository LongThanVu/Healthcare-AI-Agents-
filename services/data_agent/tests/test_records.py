import asyncio

from shared.database.seed import seed_reference_data
from shared.database.session import get_session_factory, init_db
from services.data_agent.app.services.record_service import RecordService


async def _run_record_search_test() -> None:
    await init_db()
    async with get_session_factory()() as session:
        await seed_reference_data(session)
        service = RecordService(session)
        result = await service.search("hypertension")
    assert len(result.results) >= 1


def test_record_search_returns_patient() -> None:
    asyncio.run(_run_record_search_test())
