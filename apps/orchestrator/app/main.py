from fastapi import FastAPI

from apps.orchestrator.app.routes.health import router as health_router
from apps.orchestrator.app.routes.workflows import router as workflows_router
from shared.core.config import get_settings
from shared.logging.logger import configure_logging

settings = get_settings()
configure_logging(settings.service_name)

app = FastAPI(title="Healthcare A2A Orchestrator", version="1.0.0")
app.include_router(health_router)
app.include_router(workflows_router)
