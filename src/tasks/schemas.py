from pydantic import BaseModel

class TaskCreate(BaseModel):
    description: str
    dog_id: int

class TaskUpdate(BaseModel):
    status: str

class TaskResponse(BaseModel):
    id: int
    description: str
    status: str
    dog_id: int
    user_id: int

    class Config:
        from_attributes = True
