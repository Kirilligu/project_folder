
from fastapi import APIRouter
from app.models.dog import Dog

router = APIRouter()

@router.post("/register")
def register_dog(dog: Dog):
    # Логика регистрации новой собаки
    pass
