from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.database import Base, get_db

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
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

def test_register_user():
    response = client.post(
        "/users/register",
        json={"first_name": "John", "last_name": "Doe", "phone_number": "1234567890", "password": "password123"}
    )
    assert response.status_code == 200
    assert response.json()["phone_number"] == "1234567890"

def test_authenticate_user():
    client.post(
        "/users/register",
        json={"first_name": "Jane", "last_name": "Doe", "phone_number": "0987654321", "password": "password123"}
    )
    response = client.post(
        "/users/auth",
        json={"phone_number": "0987654321", "password": "password123"}
    )
    assert response.status_code == 200
    assert "api_key" in response.json()
