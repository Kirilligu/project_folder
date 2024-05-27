from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Collar(Base):
    __tablename__ = "collars"
    id = Column(Integer, primary_key=True, index=True)
    unique_number = Column(String, unique=True, index=True)
    characteristics = Column(String)

class Dog(Base):
    __tablename__ = "dogs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    collar_id = Column(Integer, ForeignKey("collars.id"))

    collar = relationship("Collar", back_populates="dog")
    Collar.dog = relationship("Dog", back_populates="collar", uselist=False)
    tasks = relationship("Task", back_populates="dog")
