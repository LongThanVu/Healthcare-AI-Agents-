from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    service_name: str = "service"
    orchestrator_url: str = "http://localhost:8001"
    diagnosis_agent_url: str = "http://localhost:8002"
    scheduling_agent_url: str = "http://localhost:8003"
    data_agent_url: str = "http://localhost:8004"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False, extra="ignore")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
