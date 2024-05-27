from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/users/register", json={
        "first_name": "Jane",
        "last_name": "Doe",
        "phone_number": "0987654321",
        "password": "supersecret"
    })
    assert response.status_code == 200
    assert response.json()["first_name"] == "Jane"
