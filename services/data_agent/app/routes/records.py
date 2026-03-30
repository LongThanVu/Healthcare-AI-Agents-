from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from services.data_agent.app.services.record_service import RecordService
from shared.database.session import get_db
from shared.schemas.records import PatientRecord, RecordSearchRequest, RecordSearchResponse

router = APIRouter(tags=["records"])


@router.post("/records/search", response_model=RecordSearchResponse)
async def search_records(
    payload: RecordSearchRequest,
    db: AsyncSession = Depends(get_db),
) -> RecordSearchResponse:
    return await RecordService(db).search(payload.query)


@router.get("/records/summary/{patient_id}", response_model=PatientRecord)
async def get_patient_summary(
    patient_id: str,
    db: AsyncSession = Depends(get_db),
) -> PatientRecord:
    record = await RecordService(db).get_by_id(patient_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Patient record not found")
    return record
