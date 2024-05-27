import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # Setup: Create tables before tests
    Base.metadata.create_all(bind=engine)
    yield
    # Teardown: Drop tables after tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def api_key():
    response = client.post("/users/register", json={
        "first_name": "Jane",
        "last_name": "Doe",
        "phone_number": "0987654321",
        "password": "supersecret"
    })
    assert response.status_code == 200

    response = client.post("/users/login", json={
        "phone_number": "0987654321",
        "password": "supersecret"
    })
    assert response.status_code == 200
    return response.json()["api_key"]

def test_create_task(api_key):
    response = client.post("/tasks/", headers={"X-API-KEY": api_key}, json={
        "description": "Take for a walk",
        "dog_id": 1
    })
    assert response.status_code == 200
    assert response.json()["description"] == "Take for a walk"

def test_update_task_status(api_key):
    response = client.put("/tasks/1", headers={"X-API-KEY": api_key}, json={
        "status": "completed"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "completed"

def test_list_tasks(api_key):
    response = client.get("/tasks/", headers={"X-API-KEY": api_key})
    assert response.status_code == 200
    assert len(response.json()) > 0
