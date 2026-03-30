from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from apps.api_gateway.app.services.auth_service import AuthService
from shared.database.models import User
from shared.database.session import get_db
from shared.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, UserResponse
from shared.security.dependencies import get_current_user

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])
service = AuthService()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(payload: RegisterRequest, db: AsyncSession = Depends(get_db)) -> UserResponse:
    return await service.register(payload, db)


@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)) -> TokenResponse:
    return await service.login(payload, db)


@router.get("/me", response_model=UserResponse)
async def me(current_user: User = Depends(get_current_user)) -> UserResponse:
    return UserResponse.model_validate(current_user, from_attributes=True)
