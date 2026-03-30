from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    service_name: str = "service"

    orchestrator_url: str = "http://localhost:8001"
    diagnosis_agent_url: str = "http://localhost:8002"
    scheduling_agent_url: str = "http://localhost:8003"
    data_agent_url: str = "http://localhost:8004"

    database_url: str = "postgresql+asyncpg://postgres:postgres@postgres:5432/healthcare_a2a"
    redis_url: str = "redis://redis:6379/0"

    jwt_secret_key: str = Field(default="change-me-in-production", min_length=16)
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 120

    default_admin_email: str = "admin@healthcare.local"
    default_admin_password: str = "admin123456"
    default_admin_full_name: str = "System Admin"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False, extra="ignore")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
