from fastapi import FastAPI
from app.db.data_base import Base, engine

# 👇 Import all your models here before calling create_all
from app.models import account, agent  # adjust to your actual model paths

Base.metadata.create_all(bind=engine)

from app.controller.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Welcome to Transfer Check API"}
