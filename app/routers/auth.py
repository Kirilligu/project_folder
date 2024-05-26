from fastapi import APIRouter, Depends, HTTPException
from .dependencies import get_db
from ..models import User

router = APIRouter()

fake_users_db = {
    "user1": {
        "username": "user1",
        "password": "password1"
    },
    "user2": {
        "username": "user2",
        "password": "password2"
    }
}

@router.post("/login/")
async def login_user(username: str, password: str):
    user_data = fake_users_db.get(username)
    if not user_data or user_data["password"] != password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"message": "Login successful"}

