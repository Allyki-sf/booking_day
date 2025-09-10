from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from users.views import router as users_router
from core.init_db import init_db

from app import views


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(views.router)
app.include_router(users_router)

@app.get("/")
async def root():
    return {"message": "Hello API"}







if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)