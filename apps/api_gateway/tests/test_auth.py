from fastapi.testclient import TestClient

from apps.api_gateway.app.main import app


def test_login_with_seeded_admin_and_access_protected_route() -> None:
    with TestClient(app) as client:
        login_response = client.post(
            "/api/v1/auth/login",
            json={"email": "admin@healthcare.local", "password": "admin123456"},
        )
        assert login_response.status_code == 200

        token = login_response.json()["access_token"]
        me_response = client.get(
            "/api/v1/auth/me",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert me_response.status_code == 200
        assert me_response.json()["email"] == "admin@healthcare.local"
