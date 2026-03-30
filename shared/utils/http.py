import httpx
from shared.core.constants import DEFAULT_TIMEOUT_SECONDS


def build_client() -> httpx.AsyncClient:
    return httpx.AsyncClient(timeout=DEFAULT_TIMEOUT_SECONDS)
