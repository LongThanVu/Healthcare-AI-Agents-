from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any

import jwt

from shared.core.config import get_settings


def create_access_token(*, subject: str, email: str, full_name: str) -> tuple[str, int]:
    settings = get_settings()
    expires_delta = timedelta(minutes=settings.jwt_access_token_expire_minutes)
    expires_at = datetime.now(UTC) + expires_delta
    payload = {
        "sub": subject,
        "email": email,
        "full_name": full_name,
        "exp": expires_at,
        "iat": datetime.now(UTC),
    }
    token = jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return token, int(expires_delta.total_seconds())


def decode_access_token(token: str) -> dict[str, Any]:
    settings = get_settings()
    return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
