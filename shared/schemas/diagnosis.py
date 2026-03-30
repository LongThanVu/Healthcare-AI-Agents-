from typing import Literal
from pydantic import BaseModel, Field


class DiagnosisRequest(BaseModel):
    patient_id: str | None = Field(default=None, examples=["P-1001"])
    patient_name: str = Field(..., examples=["John Doe"])
    age: int = Field(..., ge=0, le=120)
    symptoms: list[str] = Field(default_factory=list)
    notes: str | None = None
    existing_conditions: list[str] = Field(default_factory=list)


class DiagnosisResult(BaseModel):
    condition: str
    urgency: Literal["low", "medium", "high"]
    confidence: float = Field(..., ge=0.0, le=1.0)
    explanation: str
    next_steps: list[str] = Field(default_factory=list)
