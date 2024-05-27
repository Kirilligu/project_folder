from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from . import models, schemas

router = APIRouter()

@router.post("/collars", response_model=schemas.CollarResponse)
def create_collar(collar: schemas.CollarCreate, db: Session = Depends(get_db)):
    db_collar = db.query(models.Collar).filter(models.Collar.unique_number == collar.unique_number).first()
    if db_collar:
        raise HTTPException(status_code=400, detail="Collar with this unique number already exists")
    new_collar = models.Collar(**collar.dict())
    db.add(new_collar)
    db.commit()
    db.refresh(new_collar)
    return new_collar

@router.post("/dogs", response_model=schemas.DogResponse)
def create_dog(dog: schemas.DogCreate, db: Session = Depends(get_db)):
    new_dog = models.Dog(**dog.dict())
    db.add(new_dog)
    db.commit()
    db.refresh(new_dog)
    return new_dog

@router.put("/dogs/{dog_id}/collar/{collar_id}", response_model=schemas.DogResponse)
def assign_collar_to_dog(dog_id: int, collar_id: int, db: Session = Depends(get_db)):
    dog = db.query(models.Dog).filter(models.Dog.id == dog_id).first()
    if not dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    collar = db.query(models.Collar).filter(models.Collar.id == collar_id).first()
    if not collar:
        raise HTTPException(status_code=404, detail="Collar not found")
    dog.collar_id = collar_id
    db.commit()
    db.refresh(dog)
    return dog

@router.get("/dogs", response_model=list[schemas.DogResponse])
def list_dogs(db: Session = Depends(get_db)):
    dogs = db.query(models.Dog).all()
    return dogs
