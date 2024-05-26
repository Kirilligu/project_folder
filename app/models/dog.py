from pydantic import BaseModel

class Dog(BaseModel):
    id: int
    name: str
    description: str

