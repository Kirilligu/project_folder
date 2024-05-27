from pydantic import BaseModel

class CollarCreate(BaseModel):
    unique_number: str
    characteristics: str

class DogCreate(BaseModel):
    name: str
    description: str

class DogResponse(BaseModel):
    id: int
    name: str
    description: str
    collar_id: int

    class Config:
        orm_mode = True

class CollarResponse(BaseModel):
    id: int
    unique_number: str
    characteristics: str

    class Config:
        orm_mode = True
