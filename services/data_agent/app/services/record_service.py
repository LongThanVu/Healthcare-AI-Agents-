from __future__ import annotations

import logging

from redis.exceptions import RedisError
from sqlalchemy.ext.asyncio import AsyncSession

from services.data_agent.app.agent.retrieval_engine import RetrievalEngine
from services.data_agent.app.agent.validation_engine import ValidationEngine
from services.data_agent.app.repositories.patient_repository import PatientRepository
from shared.cache.redis import get_redis
from shared.core.constants import DEFAULT_REDIS_CACHE_TTL_SECONDS
from shared.schemas.records import PatientRecord, RecordSearchResponse

logger = logging.getLogger(__name__)


class RecordService:
    def __init__(self, db: AsyncSession) -> None:
        self.repository = PatientRepository(db)
        self.retrieval_engine = RetrievalEngine(self.repository)

    async def search(self, query: str) -> RecordSearchResponse:
        cache_key = f"record-search:{query.strip().lower()}"
        cached_response = await self._get_cached_response(cache_key)
        if cached_response is not None:
            return cached_response

        results = [ValidationEngine.validate(record) for record in await self.retrieval_engine.search(query)]
        response = RecordSearchResponse(results=results)
        await self._set_cached_response(cache_key, response)
        return response

    async def get_by_id(self, patient_id: str) -> PatientRecord | None:
        record = await self.repository.find_by_id(patient_id)
        if record is None:
            return None
        return ValidationEngine.validate(record)

    async def _get_cached_response(self, cache_key: str) -> RecordSearchResponse | None:
        try:
            payload = await get_redis().get(cache_key)
        except RedisError as exc:
            logger.warning("Redis unavailable during get: %s", exc)
            return None

        if payload is None:
            return None
        return RecordSearchResponse.model_validate_json(payload)

    async def _set_cached_response(self, cache_key: str, response: RecordSearchResponse) -> None:
        try:
            await get_redis().set(cache_key, response.model_dump_json(), ex=DEFAULT_REDIS_CACHE_TTL_SECONDS)
        except RedisError as exc:
            logger.warning("Redis unavailable during set: %s", exc)
