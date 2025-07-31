# src/main.py
from fastapi import FastAPI
from modules.users.api.routes import router as user_router

app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["Users"])
