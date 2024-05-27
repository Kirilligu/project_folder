from fastapi import FastAPI
from .database import engine, Base
from .users.router import router as users_router
from .devices.router import router as devices_router
from .tasks.router import router as tasks_router

# Создание базы данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Регистрация роутеров
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(devices_router, prefix="/devices", tags=["devices"])
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
