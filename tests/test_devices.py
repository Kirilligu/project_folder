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

def test_register_collar():
    response = client.post("/devices/register_collar", json={
        "unique_number": "1234-5678",
        "characteristics": "Red color, Medium size"
    })
    assert response.status_code == 200
    assert response.json()["unique_number"] == "1234-5678"

def test_register_dog():
    response = client.post("/devices/register_dog", json={
        "name": "Buddy",
        "description": "Golden Retriever"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Buddy"

def test_assign_collar():
    response = client.post("/devices/assign_collar", json={
        "dog_id": 1,
        "collar_id": 1
    })
    assert response.status_code == 200
    assert response.json()["collar_id"] == 1
