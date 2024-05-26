from pydantic import BaseModel

class Collar(BaseModel):
    id: int
    collar_number: str
    characteristics: str

