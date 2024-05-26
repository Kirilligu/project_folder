from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .routers import auth, dogs, tasks
from .models import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(dogs.router)
app.include_router(tasks.router)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

