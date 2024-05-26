from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from app.auth import authenticate_user, create_access_token
from app.models import User, Dog, Collar, Task
from app.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register/", response_model=User)
def register_user(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    return user

@app.post("/login/")
def login_user(phone_number: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, phone_number, password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect phone number or password")
    access_token = create_access_token({"sub": user.phone_number})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/collars/", response_model=Collar)
def register_collar(collar: Collar, db: Session = Depends(get_db)):
    db.add(collar)
    db.commit()
    return collar

@app.post("/dogs/", response_model=Dog)
def register_dog(dog: Dog, db: Session = Depends(get_db)):
    db.add(dog)
    db.commit()
    return dog

@app.post("/assign-collar/")
def assign_collar_to_dog(collar_id: int, dog_id: int, db: Session = Depends(get_db)):
    dog = db.query(Dog).filter(Dog.id == dog_id).first()
    if not dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    dog.collar_id = collar_id
    db.commit()
    return {"message": "Collar assigned to dog successfully"}

@app.get("/dogs/", response_model=List[Dog])
def get_dogs(db: Session = Depends(get_db)):
    dogs = db.query(Dog).all()
    return dogs

@app.post("/tasks/", response_model=Task)
def create_task(task: Task, db: Session = Depends(get_db)):
    db.add(task)
    db.commit()
    return task

@app.post("/tasks/{task_id}/update-status/")
def update_task_status(task_id: int, status: str, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.status = status
    db.commit()
    return {"message": "Task status updated successfully"}

