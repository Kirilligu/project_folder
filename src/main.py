from fastapi import FastAPI
from .database import engine
from . import models
from .users import router as user_router
from .devices import router as device_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(device_router)

