from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from .models import User, Dog, Collar, Task, SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

