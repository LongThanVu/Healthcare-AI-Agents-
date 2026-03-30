from contextlib import asynccontextmanager

from fastapi import FastAPI

from services.data_agent.app.routes.health import router as health_router
from services.data_agent.app.routes.records import router as records_router
from shared.cache.redis import close_redis
from shared.core.config import get_settings
from shared.database.seed import seed_reference_data
from shared.database.session import get_session_factory, init_db
from shared.logging.logger import configure_logging

settings = get_settings()
configure_logging(settings.service_name)


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_db()
    async with get_session_factory()() as session:
        await seed_reference_data(session)
    yield
    await close_redis()


app = FastAPI(title="Data Agent", version="1.0.0", lifespan=lifespan)
app.include_router(health_router)
app.include_router(records_router)
