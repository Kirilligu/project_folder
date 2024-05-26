from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class Collar(Base):
    __tablename__ = "collars"

    id = Column(Integer, primary_key=True, index=True)
    characteristics = Column(String)
    dog_id = Column(Integer, ForeignKey("dogs.id"))

    dog = relationship("Dog", back_populates="collars")

Dog.collars = relationship("Collar", back_populates="dog")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    dog_id = Column(Integer, ForeignKey("dogs.id"))
    api_key = Column(String)
    status = Column(String)

    dog = relationship("Dog", back_populates="tasks")

