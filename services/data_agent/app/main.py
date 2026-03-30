from fastapi import FastAPI

from services.data_agent.app.routes.health import router as health_router
from services.data_agent.app.routes.records import router as records_router
from shared.core.config import get_settings
from shared.logging.logger import configure_logging

settings = get_settings()
configure_logging(settings.service_name)

app = FastAPI(title="Data Agent", version="1.0.0")
app.include_router(health_router)
app.include_router(records_router)
