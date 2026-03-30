from fastapi import FastAPI

from services.diagnosis_agent.app.routes.health import router as health_router
from services.diagnosis_agent.app.routes.diagnosis import router as diagnosis_router
from shared.core.config import get_settings
from shared.logging.logger import configure_logging

settings = get_settings()
configure_logging(settings.service_name)

app = FastAPI(title="Diagnosis Agent", version="1.0.0")
app.include_router(health_router)
app.include_router(diagnosis_router)
