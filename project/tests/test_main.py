from fastapi.testclient import TestClient
from app.main import app
from app.database import engine
from app.models import Base, User, Dog, Collar, Task
from sqlalchemy.orm import sessionmaker
import pytest

# Create a test database session
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Test registration endpoint
def test_register_user():
    response = client.post("/register/", json={"first_name": "John", "last_name": "Doe", "phone_number": "123456789", "password": "password"})
    assert response.status_code == 200
    user = response.json()
    assert user["first_name"] == "John"
    assert user["last_name"] == "Doe"
    assert user["phone_number"] == "123456789"

# Add other test cases for login, collar registration, dog registration, etc.

