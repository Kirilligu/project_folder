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

def test_register_user():
    response = client.post("/users/register", json={
        "first_name": "Jane",
        "last_name": "Doe",
        "phone_number": "0987654321",
        "password": "supersecret"
    })
    assert response.status_code == 200
    assert response.json()["first_name"] == "Jane"

def test_login_user():
    response = client.post("/users/login", json={
        "phone_number": "0987654321",
        "password": "supersecret"
    })
    assert response.status_code == 200
    assert "api_key" in response.json()
    return response.json()["api_key"]
