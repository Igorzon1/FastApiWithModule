# src/modules/users/api/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from shared.database import SessionLocal, Base, engine
from modules.users.domain.models import UserCreate, UserOut
from modules.users.infrastructure.user_repository import UserRepository
from modules.users.use_cases.register_user import register_user

router = APIRouter()
Base.metadata.create_all(bind=engine)  # Cria as tabelas no banco

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    try:
        new_user = register_user(user, repo)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
