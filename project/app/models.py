
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String, unique=True, index=True)
    password = Column(String)

class Dog(Base):
    __tablename__ = "dogs"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    collar_id = Column(Integer, ForeignKey('collars.id'))
    collar = relationship("Collar", back_populates="dogs")

class Collar(Base):
    __tablename__ = "collars"
    
    id = Column(Integer, primary_key=True, index=True)
    collar_number = Column(String, unique=True, index=True)
    # Add other characteristics of the collar
    
    dogs = relationship("Dog", back_populates="collar")

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    dog_id = Column(Integer, ForeignKey('dogs.id'))
    status = Column(String)
    # Add other fields for task
