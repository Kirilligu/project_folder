from fastapi import FastAPI
from app.routers import auth, collar, dog, task
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(collar.router, prefix="/collar", tags=["collar"])
app.include_router(dog.router, prefix="/dog", tags=["dog"])
app.include_router(task.router, prefix="/task", tags=["task"])
