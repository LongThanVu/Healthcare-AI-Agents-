from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

TEST_DB_PATH = ROOT / "test_healthcare_a2a.db"
if TEST_DB_PATH.exists():
    TEST_DB_PATH.unlink()

os.environ.setdefault("DATABASE_URL", f"sqlite+aiosqlite:///{TEST_DB_PATH}")
os.environ.setdefault("REDIS_URL", "redis://localhost:6390/0")
os.environ.setdefault("JWT_SECRET_KEY", "unit-test-secret-key-123")
os.environ.setdefault("DEFAULT_ADMIN_EMAIL", "admin@healthcare.local")
os.environ.setdefault("DEFAULT_ADMIN_PASSWORD", "admin123456")
os.environ.setdefault("DEFAULT_ADMIN_FULL_NAME", "System Admin")

from shared.core.config import get_settings
from shared.database.session import get_engine, get_session_factory

get_settings.cache_clear()
get_engine.cache_clear()
get_session_factory.cache_clear()
