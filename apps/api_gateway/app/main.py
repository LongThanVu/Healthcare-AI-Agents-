from contextlib import asynccontextmanager

from fastapi import FastAPI

from apps.api_gateway.app.routes.auth import router as auth_router
from apps.api_gateway.app.routes.health import router as health_router
from apps.api_gateway.app.routes.workflow import router as workflow_router
from shared.database.seed import seed_reference_data
from shared.database.session import get_session_factory, init_db
from shared.core.config import get_settings
from shared.logging.logger import configure_logging

settings = get_settings()
configure_logging(settings.service_name)


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_db()
    async with get_session_factory()() as session:
        await seed_reference_data(session)
    yield


app = FastAPI(title="Healthcare A2A API Gateway", version="1.0.0", lifespan=lifespan)
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(workflow_router, prefix="/api/v1")
