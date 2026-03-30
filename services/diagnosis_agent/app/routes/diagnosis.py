from fastapi import APIRouter

from services.diagnosis_agent.app.services.diagnosis_service import DiagnosisService
from shared.schemas.diagnosis import DiagnosisRequest, DiagnosisResult

router = APIRouter(tags=["diagnosis"])
service = DiagnosisService()


@router.post("/diagnose", response_model=DiagnosisResult)
async def diagnose(payload: DiagnosisRequest) -> DiagnosisResult:
    return service.diagnose(payload)
