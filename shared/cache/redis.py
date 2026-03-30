from __future__ import annotations

from functools import lru_cache

from redis.asyncio import Redis

from shared.core.config import get_settings


@lru_cache(maxsize=1)
def get_redis() -> Redis:
    settings = get_settings()
    return Redis.from_url(settings.redis_url, decode_responses=True)


async def close_redis() -> None:
    redis = get_redis()
    await redis.aclose()
