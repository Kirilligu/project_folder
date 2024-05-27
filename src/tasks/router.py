from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from . import models, schemas
from ..users.models import User
from ..devices.models import Dog
from ..dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    dog = db.query(Dog).filter(Dog.id == task.dog_id).first()
    if not dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    new_task = models.Task(description=task.description, status="pending", dog_id=task.dog_id, user_id=user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db
