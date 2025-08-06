from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from modules.auth.domain.models import LoginInput, TokenResponse
from modules.auth.use_cases.login_user import login_user
from shared.database import get_db

router = APIRouter(
    prefix="",
    tags=["Auth"]  # 👈 aqui igual ao main.py
)

@router.post("/login", response_model=TokenResponse)
def login_route(login_data: LoginInput, db: Session = Depends(get_db)):
    return login_user(login_data, db)
