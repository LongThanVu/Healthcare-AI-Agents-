from __future__ import annotations

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shared.core.constants import ACCESS_TOKEN_TYPE
from shared.database.models import User
from shared.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, UserResponse
from shared.security.jwt import create_access_token
from shared.security.passwords import hash_password, verify_password


class AuthService:
    @staticmethod
    async def register(payload: RegisterRequest, db: AsyncSession) -> UserResponse:
        existing_user = await db.scalar(select(User).where(User.email == payload.email.lower().strip()))
        if existing_user is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is already registered")

        user = User(
            email=payload.email.lower().strip(),
            full_name=payload.full_name.strip(),
            password_hash=hash_password(payload.password),
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return UserResponse.model_validate(user, from_attributes=True)

    @staticmethod
    async def login(payload: LoginRequest, db: AsyncSession) -> TokenResponse:
        user = await db.scalar(select(User).where(User.email == payload.email.lower().strip(), User.is_active.is_(True)))
        if user is None or not verify_password(payload.password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

        access_token, expires_in = create_access_token(
            subject=user.id,
            email=user.email,
            full_name=user.full_name,
        )
        return TokenResponse(
            access_token=access_token,
            token_type=ACCESS_TOKEN_TYPE,
            expires_in=expires_in,
            user=UserResponse.model_validate(user, from_attributes=True),
        )
