from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    status = Column(String, index=True)
    dog_id = Column(Integer, ForeignKey("dogs.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    dog = relationship("Dog", back_populates="tasks")
    user = relationship("User", back_populates="tasks")
