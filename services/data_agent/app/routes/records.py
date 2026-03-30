from fastapi import APIRouter, HTTPException

from services.data_agent.app.services.record_service import RecordService
from shared.schemas.records import PatientRecord, RecordSearchRequest, RecordSearchResponse

router = APIRouter(tags=["records"])
service = RecordService()


@router.post("/records/search", response_model=RecordSearchResponse)
async def search_records(payload: RecordSearchRequest) -> RecordSearchResponse:
    return service.search(payload.query)


@router.get("/records/summary/{patient_id}", response_model=PatientRecord)
async def get_patient_summary(patient_id: str) -> PatientRecord:
    record = service.get_by_id(patient_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Patient record not found")
    return record
