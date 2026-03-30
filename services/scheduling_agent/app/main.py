from fastapi import FastAPI

from services.scheduling_agent.app.routes.health import router as health_router
from services.scheduling_agent.app.routes.appointments import router as appointment_router
from shared.core.config import get_settings
from shared.logging.logger import configure_logging

settings = get_settings()
configure_logging(settings.service_name)

app = FastAPI(title="Scheduling Agent", version="1.0.0")
app.include_router(health_router)
app.include_router(appointment_router)
