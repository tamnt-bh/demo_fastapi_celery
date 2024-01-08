from app.routes import auth
from common import database
from common.config import settings
from fastapi import FastAPI

app = FastAPI(title=settings.PROJECT_NAME)


@app.on_event("startup")
def create_db_client():
    database.connect()


@app.on_event("shutdown")
def shutdown_db_client():
    database.disconnect()


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
