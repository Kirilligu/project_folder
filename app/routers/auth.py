from fastapi import APIRouter, HTTPException
from app.models.user import User

router = APIRouter()

@router.post("/login")
def login(user: User):
    # Логика аутентификации пользователя
    pass

@router.post("/register")
def register(user: User):
    # Логика регистрации нового пользователя
    pass

