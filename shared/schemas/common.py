from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = "ok"
    service: str


class ErrorResponse(BaseModel):
    detail: str = Field(..., examples=["Unexpected error occurred"])
