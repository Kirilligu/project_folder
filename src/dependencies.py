from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.orm import Session
from .database import get_db
from .users.models import User

api_key_header = APIKeyHeader(name="X-API-KEY")

def get_current_user(api_key: str = Security(api_key_header), db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.api_key == api_key).first()
    if not user:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return user
