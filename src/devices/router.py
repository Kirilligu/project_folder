from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models
from ..database import SessionLocal, engine

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/collars/", response_model=schemas.Collar)
def register_collar(collar: schemas.CollarCreate, db: Session = Depends(get_db)):
    db_collar = models.Collar(
        unique_number=collar.unique_number
    )
    db.add(db_collar)
    db.commit()
    db.refresh(db_collar)
    return db_collar

@router.post("/dogs/", response_model=schemas.Dog)
def register_dog(dog: schemas.DogCreate, db: Session = Depends(get_db)):
    db_dog = models.Dog(
        name=dog.name,
        description=dog.description
    )
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog

