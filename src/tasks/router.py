
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from . import models, schemas
from ..users.models import User
from ..devices.models import Dog

router = APIRouter()

@router.post("/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    dog = db.query(Dog).filter(Dog.id == task.dog_id).first()
    if not dog
