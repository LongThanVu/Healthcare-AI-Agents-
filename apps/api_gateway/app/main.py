from fastapi import FastAPI

from apps.api_gateway.app.routes.health import router as health_router
from apps.api_gateway.app.routes.workflow import router as workflow_router
from shared.core.config import get_settings
from shared.logging.logger import configure_logging

settings = get_settings()
configure_logging(settings.service_name)

app = FastAPI(title="Healthcare A2A API Gateway", version="1.0.0")
app.include_router(health_router)
app.include_router(workflow_router, prefix="/api/v1")
