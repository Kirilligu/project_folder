from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

