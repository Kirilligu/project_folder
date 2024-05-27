from pydantic import BaseModel

class CollarBase(BaseModel):
    unique_number: str

class CollarCreate(CollarBase):
    pass

class Collar(CollarBase):
    id: int

    class Config:
        orm_mode = True

class DogBase(BaseModel):
    name: str
    description: str

class DogCreate(DogBase):
    pass

class Dog(DogBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

