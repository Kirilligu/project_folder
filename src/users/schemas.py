from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    password: str

class UserAuth(BaseModel):
    phone_number: str
    password: str

class UserResponse(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    api_key: str

    class Config:
        orm_mode = True
