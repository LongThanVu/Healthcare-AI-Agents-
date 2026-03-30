from pydantic import BaseModel, Field


class PatientRecord(BaseModel):
    patient_id: str
    full_name: str
    age: int
    gender: str
    allergies: list[str] = Field(default_factory=list)
    chronic_conditions: list[str] = Field(default_factory=list)
    last_visit: str
    notes: str | None = None


class RecordSearchRequest(BaseModel):
    query: str


class RecordSearchResponse(BaseModel):
    results: list[PatientRecord]
