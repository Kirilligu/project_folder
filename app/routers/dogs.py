from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .dependencies import get_db
from ..models import Dog, Collar

router = APIRouter()

@router.post("/dogs/")
def create_dog(dog: Dog, db: Session = Depends(get_db)):
    db.add(dog)
    db.commit()
    db.refresh(dog)
    return dog

@router.post("/collars/")
def create_collar(collar: Collar, db: Session = Depends(get_db)):
    db.add(collar)
    db.commit()
    db.refresh(collar)
    return collar

@router.post("/dogs/{dog_id}/collars/")
def attach_collar_to_dog(dog_id: int, collar_id: int, db: Session = Depends(get_db)):
    dog = db.query(Dog).filter(Dog.id == dog_id).first()
    if not dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    collar = db.query(Collar).filter(Collar.id == collar_id).first()
    if not collar:
        raise HTTPException(status_code=404, detail="Collar not found")
    collar.dog_id = dog_id
    db.commit()
    return {"message": "Collar attached to dog successfully"}

