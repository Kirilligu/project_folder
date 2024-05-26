
from fastapi import APIRouter
from app.models.collar import Collar

router = APIRouter()

@router.post("/register")
def register_collar(collar: Collar):
    # Логика регистрации нового ошейника
    pass
