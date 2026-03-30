from __future__ import annotations

import base64
import hashlib
import hmac
import os

_ITERATIONS = 100_000
_ALGORITHM = "sha256"


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    derived_key = hashlib.pbkdf2_hmac(_ALGORITHM, password.encode("utf-8"), salt, _ITERATIONS)
    return f"pbkdf2_{_ALGORITHM}${_ITERATIONS}${base64.b64encode(salt).decode()}${base64.b64encode(derived_key).decode()}"


def verify_password(password: str, hashed_password: str) -> bool:
    scheme, raw_iterations, raw_salt, raw_hash = hashed_password.split("$", 3)
    if not scheme.startswith("pbkdf2_"):
        return False
    digest_name = scheme.replace("pbkdf2_", "", 1)
    iterations = int(raw_iterations)
    salt = base64.b64decode(raw_salt.encode())
    expected_hash = base64.b64decode(raw_hash.encode())
    candidate_hash = hashlib.pbkdf2_hmac(digest_name, password.encode("utf-8"), salt, iterations)
    return hmac.compare_digest(candidate_hash, expected_hash)
