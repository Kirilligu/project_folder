from passlib.context import CryptContext
from app.models import User
from app.database import SessionLocal

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(db, phone_number: str, password: str):
    user = db.query(User).filter(User.phone_number == phone_number).first()
    if user and verify_password(password, user.password):
        return user
    return None

def create_access_token(data: dict):
    # Create access token logic here
    return "access_token"

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

